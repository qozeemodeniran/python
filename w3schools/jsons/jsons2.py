import json

info_python = {
    "name": "Qozeem Odeniran",
    "age": 28,
    "married": False,
    "divorced": False,
    "sublings": ("Jibtil", "Neema"),
    "pets": None,
    "cars": [
        {"model": "Benz", "mpg": 30.76},
        {"model": "BMW", "mpg": 24.89}
    ]
}

print(json.dumps(info_python, indent=3, sort_keys=True))