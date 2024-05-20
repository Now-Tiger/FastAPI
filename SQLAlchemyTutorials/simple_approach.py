#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any
import sqlalchemy as sa


engine = sa.create_engine(url="sqlite:///:memory:")
connection = engine.connect()
metadata = sa.MetaData()


user_table = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, index=True, primary_key=True, autoincrement="auto"),
    sa.Column("username", sa.String, index=True, unique=True),
    sa.Column("password", sa.String),
)


def insert_user(username: str, password: str) -> None:
    query = user_table.insert().values(username=username, password=password)
    connection.execute(query)


def get_user_name(username: str) -> sa.engine.Row | None:
    query = user_table.select().where(user_table.c.username == username)
    result = connection.execute(query)
    return result.fetchone()


def get_users():
    query = user_table.select()
    result = connection.execute(query)
    return result.fetchall()


def main() -> None:
    metadata.create_all(engine)
    insert_user(username="Now_Tiger", password="strongpassword")
    insert_user("JohnCena", "ucantseeme")
    insert_user("PacMan", "pacmansworld")
    insert_user("LilYachyt", "666")
    print(get_user_name("Now_Tiger"))
    print(get_users())
    connection.close()


if __name__ == "__main__":
    main()
