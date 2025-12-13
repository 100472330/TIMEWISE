from fastapi import FastAPI
from backend.app.api.v1.auth import router as auth_router
from backend.app.api.v1.tasks import router as tasks_router
app = FastAPI(title="Focus Planner API")


@app.get("/health")
def health_check():
    return {"status": "ok"}

#Registramos el router de autenticación
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
