from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):  #  table=True diz que isso é uma tabela de banco de dados
    id: Optional[int] = Field(default=None, primary_key=True)  # Field da mais dalhes sobre uma coluna
    name: str
    secret_name: str
    age: Optional[int] = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

engine = create_engine('sqlite:///database.db', echo=True)  #echo para mostrar no bash

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
