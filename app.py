import uvicorn
from fastapi import APIRouter
from fastapi import FastAPI

from handlers.handlers import task_router

app = FastAPI()
main_router = APIRouter()

main_router.include_router(task_router, prefix="/calc", tags=["calc"])
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
