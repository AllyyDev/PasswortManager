import os, json

def load() -> dict:
    """
    Loads application data from json file.

    Returns:
        dict: App data
    """
    if os.path.exists("data.json"):
        with open('data.json', 'r') as file:
            return json.load(file)
    else:
        return {"users": []}

def save(data: dict):
    """
    Stores application data in json file.

    Args:
        data (dict): App data
    """
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

