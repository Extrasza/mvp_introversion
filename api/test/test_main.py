import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

# Teste de sucesso caso introversão.
def test_personalidade_introvertido(client):
    payload = {
        "Time_spent_Alone": 8,
        "Stage_fear": True,
        "Social_event_attendance": 1,
        "Going_outside": 1,
        "Drained_after_socializing": True,
        "Friends_circle_size": 1,
        "Post_frequency": 0
    }

    response = client.post("/personalidade", json=payload)
    assert response.status_code == 200
    assert "resultado" in response.json
    assert response.json["resultado"] in ["Introvertido", "Extrovertido"]

# Teste de sucesso caso extroversão.
def test_personalidade_extrovertido(client):
    payload = {
        "Time_spent_Alone": 1,
        "Stage_fear": False,
        "Social_event_attendance": 5,
        "Going_outside": 4,
        "Drained_after_socializing": False,
        "Friends_circle_size": 5,
        "Post_frequency": 5
    }

    response = client.post("/personalidade", json=payload)
    assert response.status_code == 200
    assert "resultado" in response.json
    assert response.json["resultado"] in ["Introvertido", "Extrovertido"]

# Teste de falha caso campo faltando.
def test_personalidade_campo_faltando(client):
    payload = {
        # "Stage_fear": "True",
        "Time_spent_Alone": 4,
        "Social_event_attendance": 2,
        "Going_outside": 2,
        "Drained_after_socializing": True,
        "Friends_circle_size": 2,
        "Post_frequency": 1
    }

    response = client.post("/personalidade", json=payload)
    assert response.status_code == 400 or response.status_code == 422

# Teste de falha caso tipagem errada.
def test_personalidade_tipo_incorreto(client):
    payload = {
        "Time_spent_Alone": 4,
        "Stage_fear": "sim", #Tipagem incorreta
        "Social_event_attendance": 2,
        "Going_outside": 2,
        "Drained_after_socializing": False,
        "Friends_circle_size": 2,
        "Post_frequency": 1
    }

    response = client.post("/personalidade", json=payload)
    assert response.status_code == 400 or response.status_code == 422

