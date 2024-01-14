import unittest
import json
from application import app


class FlaskJWTExtendedTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_login(self):
        # Test a valid login and check the response
        response = self.app.post(
            '/api/public/login', json={"username": "apple", "password": "pass_word"})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", data)
        print("test_valid_login completed")

    def test_invalid_login(self):
        # Test an invalid login and check the response
        response = self.app.post(
            '/api/public/login', json={"username": "jack", "password": "wrong_password"})
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["message"], "Invalid credentials")
        print("test_invalid_login completed")

    def test_protected_resource_with_token(self):
        # Test access to a protected resource with a valid token
        token_response = self.app.post(
            '/api/public/login', json={"username": "apple", "password": "pass_word"})
        token_data = json.loads(token_response.get_data(as_text=True))
        token = token_data["access_token"]

        headers = {"Authorization": f"Bearer {token}"}
        print("token git in testing :", headers)
        response = self.app.get('/api/welcomeuser', headers=headers)

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("message", data)
        self.assertIn("Hello, apple", data["message"])
        print("test_protected_resource_with_token completed")

    def test_protected_resource_without_token(self):
        # Test access to a protected resource without a token
        response = self.app.get('/api/welcomeuser')
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["message"], "Missing Authorization Header")


if __name__ == '__main__':
    unittest.main()
