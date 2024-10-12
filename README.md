# Aula 16 - Revisão de POO (Programação Orientada a Objetos) + Introdução ORM (Object Relational Mapper), SQLModel - Semana do CRUD

#### CRUD (Create Read Update Delete)

Representa operações de banco de dados

## Container (docker)

`git clone https://github.com/lvgalvao/crud-fastapi-postgres-streamlit.git`
`sudo docker-compose up -d --build`

Faz o container com base no documento docker-compose.yml

## Banco de dados

PostgreSQL

## Frontend

Streamlit

## Backend

FastAPI

## Mapeador de Relação de Objetos (ORM - Object Relational Mapper)

Para bancos de dados relacionais, facilita a comunicação (abstração)

sqlalchemy e;

sql model que é muito roubado, utiliza a comunicação do sqlalchemy e a validação do pydantic

2024-10-11 23:01:11,511 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-11 23:01:11,511 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("hero")
2024-10-11 23:01:11,511 INFO sqlalchemy.engine.Engine [raw sql] ()
2024-10-11 23:01:11,511 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("hero")
2024-10-11 23:01:11,511 INFO sqlalchemy.engine.Engine [raw sql] ()
2024-10-11 23:01:11,512 INFO sqlalchemy.engine.Engine 
CREATE TABLE hero (
        id INTEGER NOT NULL, 
        name VARCHAR NOT NULL, 
        secret_name VARCHAR NOT NULL, 
        age INTEGER, 
        PRIMARY KEY (id)
)


2024-10-11 23:01:11,512 INFO sqlalchemy.engine.Engine [no key 0.00004s] ()
2024-10-11 23:01:11,514 INFO sqlalchemy.engine.Engine COMMIT
2024-10-11 23:01:11,514 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-11 23:01:11,515 INFO sqlalchemy.engine.Engine INSERT INTO hero (name, secret_name, age) VALUES (?, ?, ?) RETURNING id
2024-10-11 23:01:11,515 INFO sqlalchemy.engine.Engine [generated in 0.00007s (insertmanyvalues) 1/3 (ordered; batch not supported)] ('Deadpond', 'Dive Wilson', None)
2024-10-11 23:01:11,515 INFO sqlalchemy.engine.Engine INSERT INTO hero (name, secret_name, age) VALUES (?, ?, ?) RETURNING id
2024-10-11 23:01:11,515 INFO sqlalchemy.engine.Engine [insertmanyvalues 2/3 (ordered; batch not supported)] ('Spider-Boy', 'Pedro Parqueador', None)
2024-10-11 23:01:11,515 INFO sqlalchemy.engine.Engine INSERT INTO hero (name, secret_name, age) VALUES (?, ?, ?) RETURNING id
2024-10-11 23:01:11,515 INFO sqlalchemy.engine.Engine [insertmanyvalues 3/3 (ordered; batch not supported)] ('Rusty-Man', 'Tommy Sharp', 48)
2024-10-11 23:01:11,515 INFO sqlalchemy.engine.Engine COMMIT


========================================================================================
CREATE TABLE hero (
		id INTEGER NOT NULL,
		name VARCHAR NOT NULL,
		secret_name VARCHAR NOT NULL,
		age INTEGER,
		PRIMARY KEY (id)
);

INSERT INTO hero (name, secret_name) VALUES ('Deadpond', 'Dive Wilson');

INSERT INTO hero (name, secret_name) VALUES ('Spider-Boy', 'Pedro Parqueador');

INSERT INTO hero (name, secret_name, age) VALUES ('Rusty-Man', 'Tommy Sharp', 48);
=======================================================================================

cuidado com o text('tal') por causa do SQL injection, que pode acabar apagando o banco. então utilize o add() que tem o tratamento