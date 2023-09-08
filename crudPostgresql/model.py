#!/usr/bin/env python3
# coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

BASE = declarative_base()

class Book(BASE):
    __tablename__: str = "books"

    id = Column(Integer, primary_key=True)
    title  = Column(String)
    author = Column(String)
    pages  = Column(Integer)
    published = Column(Date)

    def __repr__(self) -> str:
        return f"<Book(title='{self.title}', author='{self.author}', pages={self.pages}, published={self.published})"