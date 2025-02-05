from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate, ItemResponse
from app.database import get_session


router = APIRouter()


@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_session)):
    new_item = Item(name=item.name, description=item.description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.get("/", response_model=list[ItemResponse])
def list_items(db: Session = Depends(get_session)):
    return db.query(Item).all()


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_session)):
    return db.query(Item).filter(Item.id == item_id).first()
