from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_303_SEE_OTHER

from app import routers

app = FastAPI()
app.include_router(routers.router)

client = TestClient(app)


def test__read_root__redirected() -> None:
    response = client.get("/", allow_redirects=False)
    assert response.status_code == HTTP_303_SEE_OTHER
    assert response.text == ""
    assert response.headers["Location"] == "/docs"


def test__update_graph__redirected() -> None:
    response = client.patch("/api/v0/graph", json={})
    assert response.status_code == HTTP_200_OK
    assert response.json() == "Success"