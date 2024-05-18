import json

class DataProvider:
    URL = "url"

    @staticmethod
    def provide_test_data(file_name, data_key):
        try:
            with open(f"{file_name}.json", 'r') as file:
                data = json.load(file)
                output = data.get(data_key, "")
                return output
        except (IOError, ValueError) as e:
            print(e)
            return ""

    @staticmethod
    def get_url_test_data(url_name):
        return DataProvider.provide_test_data(DataProvider.URL, url_name)
