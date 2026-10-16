# RestaurantOS Pro

Sistema web demonstrativo para organização de operações de restaurantes, desenvolvido com **Python, Flask, SQLite, HTML, CSS e JavaScript**.

O projeto foi criado para estudo, demonstração de portfólio e evolução incremental de funcionalidades.

## Funcionalidades atuais

- Painel inicial com indicadores de operação.
- Seleção demonstrativa de perfil: Administrador ou Gerente.
- Cadastro e listagem de produtos.
- Acompanhamento de estoque mínimo e itens com estoque baixo.
- Registro de pedidos e atualização de status.
- Relatórios simples por status e itens mais registrados.
- Interface web com navegação e estilos responsivos.

> **Estado do projeto:** protótipo educacional. A seleção de perfil não é autenticação real e não deve ser usada como controle de acesso em um ambiente comercial.

## Tecnologias

- **Python**
- **Flask**
- **SQLite**
- **HTML5 e CSS3**
- **JavaScript**

## Requisitos

- Python 3.10 ou superior recomendado
- `pip`

## Como executar

### Linux

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd RestaurantOS_Pro
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

### Windows (PowerShell)

```powershell
git clone <URL_DO_SEU_REPOSITORIO>
cd RestaurantOS_Pro
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

Abra `http://127.0.0.1:5000` no navegador.

> Se o repositório tiver outro nome, entre na pasta criada pelo `git clone` em vez de usar `cd RestaurantOS_Pro`.

## Estrutura do projeto

```text
RestaurantOS_Pro/
├── app.py                 # Rotas e lógica principal da aplicação Flask
├── database.py            # Conexão e inicialização do banco SQLite
├── requirements.txt       # Dependências Python
├── README.md              # Documentação do projeto
├── .gitignore              # Arquivos que não devem ir para o Git
├── docs/
│   ├── ESTRUTURA.md        # Guia rápido da organização do código
│   └── ROADMAP.md          # Melhorias planejadas
├── static/
│   ├── css/
│   │   └── style.css       # Estilos da interface
│   └── js/
│       └── app.js          # JavaScript do front-end
└── templates/
    ├── base.html           # Layout compartilhado
    ├── login.html          # Seleção demonstrativa de perfil
    ├── dashboard.html      # Painel principal
    ├── products.html       # Produtos e estoque
    ├── orders.html         # Pedidos
    └── reports.html        # Relatórios
```

## Banco de dados

O projeto utiliza SQLite. O arquivo `restaurantos.db` é criado localmente quando a aplicação é executada e está listado no `.gitignore`, portanto não deve ser enviado ao repositório. A aplicação insere dados de demonstração quando as tabelas estão vazias.

## Próximas melhorias

Veja [`docs/ROADMAP.md`](docs/ROADMAP.md) para uma lista de evoluções recomendadas.

## Segurança e uso comercial

Antes de disponibilizar o sistema para clientes ou publicar em produção, é necessário implementar e testar, no mínimo:

- autenticação real com senhas armazenadas de forma segura;
- autorização por função validada no servidor;
- chave secreta configurada por variável de ambiente;
- proteção CSRF nos formulários;
- validação de entradas e tratamento de erros;
- testes automatizados;
- configuração de produção e servidor WSGI apropriado;
- estratégia de backup e proteção dos dados.

Não use o servidor de desenvolvimento do Flask nem o modo `debug` em produção.

## Autor

**Daniel Damasceno**  
Desenvolvimento Back-end Júnior — projeto de portfólio.

Adicione aqui, quando estiverem prontos, os links do seu GitHub e LinkedIn.
