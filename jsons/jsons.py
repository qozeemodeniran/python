import json

info_json = '{"name": "Qozeem Odeniran", "age": 28, "city": "Statesboro"}'

convert_2_python = json.loads(info_json)

print("My age is: ", convert_2_python["age"])

info_python = {
    "name": "Qozeem Banji Odeniran",
    "occupation": "Software Engineer",
    "years_of_experience": 3
}

convert_2_json = json.dumps(info_python)
print(convert_2_json)
