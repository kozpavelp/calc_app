import json


async def test_add(client_app):
    values = {"x": 12, "y": 234, "operator": "+"}
    resp = client_app.post("/calc/create_task", data=json.dumps(values))
    assert resp.status_code == 200


async def test_mul(client_app):
    values = {"x": 12, "y": 234, "operator": "*"}
    resp = client_app.post("/calc/create_task", data=json.dumps(values))
    assert resp.status_code == 200


async def test_division(client_app):
    values = {"x": 12, "y": 234, "operator": "/"}
    resp = client_app.post("/calc/create_task", data=json.dumps(values))
    assert resp.status_code == 200


async def test_sub(client_app):
    values = {"x": 12, "y": 234, "operator": "-"}
    resp = client_app.post("/calc/create_task", data=json.dumps(values))
    assert resp.status_code == 200


async def test_division_by_zero(client_app):
    values = {"x": 12, "y": 0, "operator": "/"}
    resp = client_app.post("/calc/create_task", data=json.dumps(values))
    assert resp.status_code == 400


async def test_wrong_operator(client_app):
    values = {"x": 12, "y": 2, "operator": "&"}
    resp = client_app.post("/calc/create_task", data=json.dumps(values))
    assert resp.status_code == 400


async def test_create_task_get_result(client_app):
    values = {"x": 12, "y": 2666, "operator": "*"}
    create_task_resp = client_app.post("/calc/create_task", data=json.dumps(values))
    assert create_task_resp.status_code == 200
    task_id = create_task_resp.json()
    assert task_id is not None
    task_status_resp = client_app.get("/calc/status")
    assert task_status_resp.status_code == 200
    assert task_id in task_status_resp.json()
    assert task_status_resp.json()[task_id]["status"] == "pending"
    get_result_resp = client_app.get(f"/calc/get_result?task_id={task_id}")
    result = get_result_resp.json()
    assert get_result_resp.status_code == 200
    assert result == 31992
    task_status_resp = client_app.get("/calc/status")
    assert task_status_resp.json()[task_id]["status"] == "done"
