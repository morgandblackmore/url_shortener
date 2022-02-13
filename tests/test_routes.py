import flask_unittest
from url_shortener import create_app

class TestRoutes(flask_unittest.ClientTestCase):
    app = create_app()

    def test_index(self, client):
        self.assertStatus(client.get("/"), 200)

    def test_add_link(self, client):
        # self.assertStatus(client.get("/add_link"), 200)

        response = client.post('/add_link', data={'original_url': 'https://www.google.com'}, follow_redirects=True)
        print('morgan')
        # with app.app_context():
        #     self.assertIsNotNone(
        #         get_db().execute("select * from Link where original_url = 'https://www.google.com'").fetchone()
        #     )

    def test_errorhandler(self, client):
        self.assertStatus(client.get("/404"), 404)
        