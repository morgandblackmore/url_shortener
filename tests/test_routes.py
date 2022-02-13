import flask_unittest
from url_shortener import create_app

class TestRoutes(flask_unittest.ClientTestCase):
    app = create_app()

    def test_index(self, client):
        self.assertStatus(client.get("/"), 200)

    def test_add_link(self, client, app):
        response = client.post('/add_link', data={'original_url': 'https://www.google.com'}, follow_redirects=True)
        

    def test_errorhandler(self, client):
        self.assertStatus(client.get("/404"), 404)
        