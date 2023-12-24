#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event


events = list()
eventRouter = APIRouter(tags=["Events"])


@eventRouter.get("/", response_model=List[Event])
async def retrive_all_events() -> List[Event]:
    return events


@eventRouter.get("/{id}", response_model=Event)
async def retrive_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist",
    )


@eventRouter.post("/new")
async def create_event(body: Event = Body(...)) -> dict[str, str]:
    events.append(body)
    return {"Message": "Event added successfully"}


@eventRouter.delete("/{id}")
async def delete_event(id: int) -> dict[str, str]:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"Message": "Even deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with given ID does not exits",
    )


@eventRouter.delete("/")
async def delete_all_events() -> dict[str, str]:
    events.clear()
    return {"Message": "Evenets deleted successfully"}
