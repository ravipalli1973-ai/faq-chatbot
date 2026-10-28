import unittest
from nlp_engine import FAQMatcher

class TestFAQEngine(unittest.TestCase):
    def setUp(self):
        self.matcher = FAQMatcher()

    def test_business_hours_match(self):
        reply, score = self.matcher.get_response("When do you open and close?")
        self.assertIn("Monday through Friday", reply)
        self.assertGreater(score, 0.20)

    def test_out_of_scope_query(self):
        reply, score = self.matcher.get_response("What is the recipe for chocolate cake?")
        self.assertIn("couldn't find an answer", reply)

if __name__ == "__main__":
    unittest.main()
