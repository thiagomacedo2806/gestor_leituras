# Gestor de Leituras

Este é um projeto funcional e minimalista construído em Django para gerenciar uma fila de livros, artigos ou links de interesse que você planeja ler de forma ágil.

## Funcionalidades

- Listar itens de leitura cadastrados.
- Criar novos itens de leitura via requisição JSON.

## Como Executar

1. Instale o Django:
```bash
pip install django
```

2. Inicialize as tabelas do banco de dados (SQLite embutido):
```bash
python manage.py migrate
```

3. Inicie o servidor:
```bash
python manage.py runserver
```

## Como Testar

Para executar os testes automatizados da aplicação:
```bash
python manage.py test tests
```