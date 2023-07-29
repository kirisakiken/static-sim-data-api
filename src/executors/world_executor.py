from typing import Optional, List

from sqlalchemy.orm import Session

from src.database.schemas.world_schema import WorldSchema
from src.models.world_model import WorldModel


def query_worlds(db: Session, limit: Optional[int] = None, offset: int = 0) -> List[WorldSchema]:
    # return db.query(WorldModel)\
    #     .offset(offset)\
    #     .limit(limit)\
    #     .all()
    return db.query(WorldModel).all()


def get_world_by_id(db: Session, world_id: str) -> Optional[WorldSchema]:
    return db.query(WorldModel).\
        filter(WorldModel.id == world_id)\
        .first()


def create_world(db: Session, model: WorldModel) -> WorldSchema:
    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def update_world(db: Session, model: WorldModel) -> Optional[WorldSchema]:
    _world = get_world_by_id(db, model.id)
    if not _world:
        return

    _world.name = model.name
    db.commit()
    db.refresh(_world)
    return _world


def delete_world(db: Session, world_id: str) -> Optional[WorldSchema]:
    _world = get_world_by_id(db, world_id)
    if not _world:
        return

    db.delete(_world)
    db.commit()
    return _world
