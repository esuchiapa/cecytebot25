import unittest
from src.nlp.responses import generate_response

class TestNLP(unittest.TestCase):
    def test_generate_response(self):
        response = generate_response("How do I create a function in Python?")
        self.assertEqual(response, "Para crear una función en Python, usa la palabra clave 'def' seguida del nombre de la función y paréntesis.")

if __name__ == '__main__':
    unittest.main()
