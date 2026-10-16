from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import init_db, get_db

app = Flask(__name__)
app.secret_key = "troque-esta-chave-antes-de-publicar"

@app.before_request
def prepare_database():
    init_db()

@app.route("/")
def home():
    if "role" not in session:
        return redirect(url_for("login"))
    return redirect(url_for("dashboard"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form.get("role", "manager")
        if role not in ("admin", "manager"):
            role = "manager"
        session["role"] = role
        session["user_name"] = "Administrador" if role == "admin" else "Gerente"
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if "role" not in session:
        return redirect(url_for("login"))
    db = get_db()
    products = db.execute("SELECT * FROM products ORDER BY name").fetchall()
    low_stock = db.execute("SELECT * FROM products WHERE stock <= min_stock ORDER BY stock ASC").fetchall()
    orders = db.execute("SELECT * FROM orders ORDER BY id DESC LIMIT 6").fetchall()
    total_products = db.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    total_orders = db.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    revenue = db.execute("SELECT COALESCE(SUM(total), 0) FROM orders WHERE status = 'Concluído'").fetchone()[0]
    pending = db.execute("SELECT COUNT(*) FROM orders WHERE status IN ('Recebido', 'Em preparo')").fetchone()[0]
    return render_template("dashboard.html", products=products, low_stock=low_stock, orders=orders,
        total_products=total_products, total_orders=total_orders, revenue=revenue, pending=pending,
        role=session["role"], user_name=session.get("user_name", "Equipe"))

@app.route("/products", methods=["GET", "POST"])
def products_page():
    if "role" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "Geral").strip()
        stock = request.form.get("stock", type=int, default=0)
        min_stock = request.form.get("min_stock", type=int, default=5)
        price = request.form.get("price", type=float, default=0)
        if name:
            db = get_db()
            db.execute("INSERT INTO products (name, category, stock, min_stock, price) VALUES (?, ?, ?, ?, ?)",
                       (name, category, max(stock, 0), max(min_stock, 0), max(price, 0)))
            db.commit()
            flash("Produto cadastrado com sucesso.", "success")
        else:
            flash("Informe o nome do produto.", "error")
        return redirect(url_for("products_page"))
    products = get_db().execute("SELECT * FROM products ORDER BY name").fetchall()
    return render_template("products.html", products=products, role=session["role"], user_name=session.get("user_name", "Equipe"))

@app.route("/orders", methods=["GET", "POST"])
def orders_page():
    if "role" not in session:
        return redirect(url_for("login"))
    db = get_db()
    if request.method == "POST":
        table_name = request.form.get("table_name", "Balcão").strip() or "Balcão"
        item_name = request.form.get("item_name", "").strip()
        total = request.form.get("total", type=float, default=0)
        if item_name and total > 0:
            db.execute("INSERT INTO orders (table_name, item_name, total, status) VALUES (?, ?, ?, 'Recebido')",
                       (table_name, item_name, total))
            db.commit()
            flash("Pedido lançado na fila.", "success")
        else:
            flash("Informe o item e um valor maior que zero.", "error")
        return redirect(url_for("orders_page"))
    orders = db.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()
    return render_template("orders.html", orders=orders, role=session["role"], user_name=session.get("user_name", "Equipe"))

@app.route("/orders/<int:order_id>/status", methods=["POST"])
def update_order_status(order_id):
    if "role" not in session:
        return redirect(url_for("login"))
    status = request.form.get("status")
    allowed = {"Recebido", "Em preparo", "Concluído", "Cancelado"}
    if status in allowed:
        db = get_db()
        db.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
        db.commit()
        flash("Status do pedido atualizado.", "success")
    return redirect(request.referrer or url_for("orders_page"))

@app.route("/reports")
def reports_page():
    if "role" not in session:
        return redirect(url_for("login"))
    db = get_db()
    daily = db.execute("SELECT status, COUNT(*) AS amount, COALESCE(SUM(total),0) AS total FROM orders GROUP BY status").fetchall()
    bestsellers = db.execute("SELECT item_name, COUNT(*) AS quantity FROM orders GROUP BY item_name ORDER BY quantity DESC LIMIT 5").fetchall()
    return render_template("reports.html", daily=daily, bestsellers=bestsellers, role=session["role"], user_name=session.get("user_name", "Equipe"))

if __name__ == "__main__":
    app.run(debug=True)
