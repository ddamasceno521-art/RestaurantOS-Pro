# Roadmap — RestaurantOS Pro

Lista de melhorias sugeridas. Marque cada item quando ele estiver implementado e testado.

## Prioridade alta — segurança e confiabilidade

- [ ] Configurar a `SECRET_KEY` por variável de ambiente.
- [ ] Implementar login real e armazenamento seguro de senhas.
- [ ] Validar permissões de administrador e gerente no servidor.
- [ ] Adicionar proteção CSRF aos formulários.
- [ ] Validar todos os campos e limites numéricos.
- [ ] Desativar `debug` em execução de produção.
- [ ] Criar testes para rotas e operações do banco.

## Funcionalidades de negócio

- [ ] Permitir editar e excluir produtos.
- [ ] Registrar movimentações de entrada e saída do estoque.
- [ ] Baixar estoque de acordo com os itens de cada pedido.
- [ ] Impedir estoque negativo e registrar alertas.
- [ ] Criar cadastro de produtos do cardápio separado dos insumos.
- [ ] Permitir vários itens em um único pedido.
- [ ] Adicionar filtros de data e status nos relatórios.

## Qualidade do repositório

- [ ] Adicionar capturas de tela reais da aplicação em `docs/screenshots/`.
- [ ] Publicar instruções de instalação testadas em Linux e Windows.
- [ ] Adicionar testes automatizados e integração contínua.
- [ ] Escolher e incluir uma licença se o autor quiser definir como o código pode ser reutilizado.
