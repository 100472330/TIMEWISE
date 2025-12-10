from fastapi import FastAPI

app = FastAPI(title="Focus Planner API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
