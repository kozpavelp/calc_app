from uuid import uuid4

from fastapi import APIRouter

from db.fake_db import result
from handlers.actions import calculate
from schemas.schemas import GetValues

task_router = APIRouter()


@task_router.post("/create_task")
async def create_calculation_task(values: GetValues):
    task_id = str(uuid4())
    result[task_id] = {
        "result": await calculate(values.x, values.y, values.operator),
        "status": "pending",
    }
    return task_id


@task_router.get("/get_result")
async def get_calculation_result(task_id: str):
    result[task_id]["status"] = "done"
    return result[task_id]["result"]


@task_router.get("/status")
async def get_status():
    return result
