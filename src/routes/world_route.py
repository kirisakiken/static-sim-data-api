from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.common.response import Response
from src.database.database_manager import get_db
from src.executors.world_executor import query_worlds, get_world_by_id


router = APIRouter()


@router.post("/worlds")
async def r_query_worlds(db: Session = Depends(get_db)):
    res = query_worlds(db)
    return Response(
        code=200,
        status="Ok",
        result=res
    ).dict(exclude_none=True)


@router.get("/worlds/{world_id}")
async def r_get_world_by_id(world_id: str, db: Session = Depends(get_db)):
    res = get_world_by_id(db, world_id)
    return Response(
        code=200,
        status="Ok",
        result=res,
    ).dict(exclude_none=True)

