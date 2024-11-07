# test_app.py
import pytest
from app import app
from bs4 import BeautifulSoup

@pytest.fixture
def client():
    # Set up the test client for the Flask app
    with app.test_client() as client:
        yield client

@pytest.fixture
def soup(client):
    # Fetch the response and parse it with BeautifulSoup
    response = client.get("/")
    return BeautifulSoup(response.data, "html.parser")

def test_index_route_status_code(client):
    # Test if the index route ("/") returns a 200 status code
    response = client.get("/")
    assert response.status_code == 200

def test_index_page_title(soup):
    # Test if the title of the index page is "Flask App"
    title = soup.title.string
    assert title == "Flask App"

def test_index_page_h1_tag(soup):
    # Test if the <h1> tag contains the expected text
    h1_tag = soup.find("h1")
    assert h1_tag is not None
    assert h1_tag.text == "Hello, Utkarsh Gaikwad!"
