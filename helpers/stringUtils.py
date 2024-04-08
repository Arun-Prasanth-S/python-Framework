class StringUtils:
    @staticmethod
    def replace_all_string_for_value(value, str_to_replace, symbol):
        return value.replace(str_to_replace, symbol)

    @staticmethod
    def get_string_to_upper_case(value):
        return value.upper()

    @staticmethod
    def get_string_to_lower_case(value):
        return value.lower()
