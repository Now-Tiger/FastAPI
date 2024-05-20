#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List
import hashlib

import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    sessionmaker,
    relationship,
    declarative_base,
)


db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    auth: Mapped["UserAuth"] = relationship(
        "UserAuth", back_populates="user", uselist=False
    )
    posts: Mapped[List["UserPost"]] = relationship("UserPost", back_populates="user")

    def __init__(self, username: str, email: str, password: str) -> None:
        super().__init__()
        self.auth = UserAuth(username=username, email=email)
        self.auth.set_password(password)

    def __repr__(self) -> str:
        return f"<User(username: {self.auth.username}, email: {self.auth.email})>"


class UserAuth(Base):
    __tablename__ = "user_auth"

    id = sa.Column(
        sa.Integer,
        sa.ForeignKey("users.id"),
        primary_key=True,
        index=True,
        unique=True,
    )
    username = sa.Column(sa.String, unique=True)
    email = sa.Column(sa.String, unique=True)
    password_hash = sa.Column(sa.String)
    user: Mapped["User"] = relationship("User", back_populates="auth")

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def set_password(self, password: str) -> None:
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> sa.ColumnElement[bool] | bool:
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    def __repr__(self) -> str:
        return f"<UserAuth(username: {self.username}, email: {self.email})>"


class UserPost(Base):
    __tablename__ = "user_posts"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(
        sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True
    )
    content = sa.Column(sa.String)
    user: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"<UserPost (user: {self.user}, content: {self.content})>"


def main() -> None:
    Base.metadata.create_all(db)

    with Session.begin() as session:
        user = User(username="Tiger", email="tiger@mail.com", password="strongpassword")
        # TODO: Populate database with few more users and posts
        post = UserPost(content="Artifical Intelligence summit!", user=user)

        session.add(user)
        session.add(post)

    with Session.begin() as session:
        user = session.query(User).first()
        print(user)
        # FIX: auth is not a known attribute of None - linting/typing error
        print(user.auth)
        print(user.posts)

        print(f">> Check password: {user.auth.check_password('strongpassword')}")
        print(f">> Check password: {user.auth.check_password('wrongpassword')}")

        posts = session.query(UserPost).filter(UserPost.user == user).all()
        print(posts)


if __name__ == "__main__":
    main()
