# Gerenciador_de_Tarefas
Este é um gerenciador de tarefas simples desenvolvido com Django, que permite aos usuários criar, atualizar, visualizar e deletar tarefas. Além disso, os usuários podem criar categorias para organizar melhor suas tarefas.
Claro! Aqui está uma descrição README para o seu projeto no GitHub, incluindo instruções sobre como configurar e executar o projeto:

---

## Funcionalidades

- Cadastro e login de usuários
- Criação, edição, visualização e exclusão de tarefas
- Adição de categorias para as tarefas
- Filtragem de tarefas por status e busca por título/descrição
- Sistema de comentários nas tarefas

## Pré-requisitos

- Python 3.6+
- Django 3.2+
- Um ambiente virtual Python (recomendado)

## Configuração do Ambiente de Desenvolvimento

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/taskmanager.git
cd taskmanager
```

### Passo 2: Criar e Ativar o Ambiente Virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar as Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Aplicar as Migrações do Banco de Dados

```bash
python manage.py migrate
```

### Passo 5: Criar um Superusuário

```bash
python manage.py createsuperuser
```

### Passo 6: Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

## Uso

1. Acesse o painel de administração em `http://127.0.0.1:8000/admin/` e faça login com o superusuário criado.
2. Gerencie usuários, tarefas e categorias através da interface de administração do Django.
3. Acesse a aplicação em `http://127.0.0.1:8000/tasks/` para começar a gerenciar suas tarefas.

## Contribuição

Se você deseja contribuir com este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
