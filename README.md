# FabricaDeSoftware - ProjetoDjango
 Projeto Django desenvolvido para a Fábrica de Software @UNIPE

README.txt
==========

Projeto Django com CRUD e Integração de API Externa
---------------------------------------------------

Este é um projeto básico em Django que demonstra como configurar um CRUD completo para duas entidades (Autor e Detalhe) e integrar uma API externa gratuita para importar dados.

### Estrutura do Projeto

- **myproject/**: Diretório principal do projeto Django.
- **myapp/**: Aplicativo Django que contém as entidades Author e Book.
- **templates/myapp/**: Diretório com os templates HTML utilizados pelas views.
- **db.sqlite3**: Banco de dados SQLite padrão utilizado pelo Django.

### Funcionalidades

1. **CRUD para Author e Detalhe**:
   - Listagem de Autores e Detalhes.
   - Visualização dos detalhes de um Autor.
   - Criação, atualização e exclusão de Autores e Detalhes.

2. **Integração com API Externa**:
   - Consome dados da API externa JSONPlaceholder para importar uma lista de autores.
   - URL para importar dados: `/fetch-autors/`.

### Como Executar o Projeto

1. **Requisitos**:
   - Python 3.x
   - pip (Python package installer)
   - Django (versão mais recente)
   - requests (para consumo da API externa)

2. **Instalação**:

   - Clone o repositório ou baixe o código-fonte.
   - Crie um ambiente virtual para o projeto
   - Ative o ambiente virtual
   - Instale as dependências
     

3. **Configuração**:

   - Navegue até o diretório do projeto
   - Aplique as migrações do banco de dados


4. **Executar o Servidor de Desenvolvimento**:

   - Inicie o servidor:
   - Acesse `http://127.0.0.1:8000/` no navegador para visualizar o projeto em execução.


### Observações

Este projeto é uma introdução básica ao Django e é projetado para fins educacionais. Pode ser expandido para incluir mais funcionalidades, como autenticação de usuário, segurança, e otimização.

### Contato

Para dúvidas ou sugestões, entre em contato com o desenvolvedor.
rigelsouza@gmail.com
