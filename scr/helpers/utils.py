#Help you to read json file & provide you json data
import json


def get_payload_auth():
    # read from auth.json and return json
    file_data = open("scr/Resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data