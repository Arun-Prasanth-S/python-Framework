import unittest

class Assertions(unittest.TestCase):
    @staticmethod
    def expect_to_equal(result, expected_result, error_message):
        Assertions().assertEqual(result, expected_result, error_message)

    @staticmethod
    def expect_to_not_equal(result, expected_result, error_message):
        Assertions().assertNotEqual(result, expected_result, error_message)

    @staticmethod
    def expect_to_display(element, error_message):
        Assertions().assertTrue(element.is_displayed(), error_message)

    @staticmethod
    def expect_to_not_display(element, error_message):
        Assertions().assertFalse(element.is_displayed(), error_message)

    @staticmethod
    def expect_to_be_enabled(element, error_message):
        Assertions().assertTrue(element.is_enabled(), error_message)

    @staticmethod
    def expect_to_be_disabled(element, error_message):
        Assertions().assertFalse(element.is_enabled(), error_message)
