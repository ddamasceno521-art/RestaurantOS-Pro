# Guia da estrutura

- `app.py`: define as rotas HTTP, recebe dados dos formulários e prepara as informações enviadas aos templates.
- `database.py`: abre conexões SQLite e cria as tabelas e dados de demonstração.
- `templates/`: contém os arquivos HTML renderizados pelo Flask.
- `templates/base.html`: layout compartilhado entre as páginas.
- `static/css/style.css`: regras visuais da interface.
- `static/js/app.js`: interações executadas no navegador.
- `requirements.txt`: lista as bibliotecas Python necessárias para executar o projeto.

## Fluxo simplificado

1. O navegador faz uma requisição para uma rota.
2. O Flask executa a função correspondente em `app.py`.
3. Quando necessário, a aplicação consulta ou altera o banco por meio de `database.py`.
4. O Flask renderiza um template HTML com os dados.
5. O navegador exibe a página e carrega os arquivos estáticos de CSS e JavaScript.
