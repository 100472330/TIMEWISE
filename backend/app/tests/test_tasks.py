#TEST TASKS
def test_tasks_crud_flow(client):
    # Crear tarea
    response = client.post("/tasks/", json={
        "title": "Test task",
        "description": "Description"
    })
    assert response.status_code == 201
    data = response.json()
    task_id = data["id"]
    assert data["title"] == "Test task"

    # Listar tareas
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert any(t["id"] == task_id for t in tasks)

    # Obtener detalle
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id

    # Actualizar
    response = client.put(f"/tasks/{task_id}", json={
        "title": "Updated task"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated task"

    # Borrar
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    # Comprobar que ya no existe
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
