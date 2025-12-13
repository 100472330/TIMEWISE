import sys
from pathlib import Path
# Añade la raíz del proyecto al sys.path para que 'backend' se pueda importar
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

#Importamos las "DBs" en memoria para poder resetearlas entre tests
from backend.app.api.v1 import auth, tasks

@pytest.fixture(autouse=True)
def reset_in_memory_db():
    auth.fake_users_db.clear()
    auth.user_id_counter = 1

    tasks.fake_tasks_db.clear()
    tasks.task_id_counter = 1

    yield

@pytest.fixture()
def client():
    return TestClient(app)