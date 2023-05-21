import unittest
from credit_card_validation import validate_credit_card

class CreditCardValidationTestCase(unittest.TestCase):
    def test_valid_credit_card_numbers(self):
        self.assertEqual(validate_credit_card("4253625879615786"), "Valid")
        self.assertEqual(validate_credit_card("4424424424442444"), "Valid")
        self.assertEqual(validate_credit_card("5122-2368-7954-3214"), "Valid")

    def test_invalid_credit_card_numbers(self):
        self.assertEqual(validate_credit_card("42536258796157867"), "Invalid")
        self.assertEqual(validate_credit_card("4424444424442444"), "Invalid")
        self.assertEqual(validate_credit_card("5122-2368-7954 - 3214"), "Invalid")
        self.assertEqual(validate_credit_card("44244x4424442444"), "Invalid")
        self.assertEqual(validate_credit_card("0525362587961578"), "Invalid")
        self.assertEqual(validate_credit_card("5123 - 3567 - 8912 - 3456"), "Invalid")
        self.assertEqual(validate_credit_card("5123_3567_8912_3456"), "Invalid")

    def test_hackerrank_testrun_credit_card_numbers(self):
        self.assertEqual(validate_credit_card("6"),"Invalid")
        self.assertEqual(validate_credit_card("4123456789123456"),"Valid")
        self.assertEqual(validate_credit_card("5123-4567-8912-3456"),"Valid")
        self.assertEqual(validate_credit_card("61234-567-8912-3456"),"Invalid")
        self.assertEqual(validate_credit_card("4123356789123456"),"Valid")
        self.assertEqual(validate_credit_card("5133-3367-8912-3456"),"Invalid")
        self.assertEqual(validate_credit_card("5123 - 3567 - 8912 - 3456"),"Invalid")
if __name__ == '__main__':
    unittest.main()
