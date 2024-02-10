import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_cities(self):
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)
        self.assertIn('New York', response.data.decode('utf-8'))

if __name__ == "__main__":
    unittest.main()
