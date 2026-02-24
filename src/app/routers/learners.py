"""Router for learner endpoints."""

from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners
from app.models.learner import Learner

router = APIRouter()

@router.get("/", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all learners, optionally filtered by enrollment date."""
    return await read_learners(session, enrolled_after)
