#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base

# Establish database connection
db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base()


# User table creation
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement="auto")
    username: Mapped[str]
    email: Mapped[str]

    def __repr__(self) -> str:
        return f"User: (id={self.id} username={self.username}, email={self.email})"


def main():
    # create database in the memory
    Base.metadata.create_all(db)

    # create dummy users to populate the database
    user = User(username="Tiger", email="tiger@mail.com")
    user_new = User(username="JohnCena", email="john@champ.com")
    user_pvt = User(username="Luke", email="lukamodrick@gmail.com")

    with Session() as session:
        # add user to the database using session
        session.add(user)
        # Add mutiple users
        session.add_all([user_new, user_pvt])
        session.commit()
        print(session.query(User).all())


if __name__ == "__main__":
    main()
