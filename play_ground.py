import json

dict_test = {
    "asd": {
        "email": "aksky9835@gmail.com",
        "password": "+5s$YgbXX5oo*"
    }
}
with open('data.json', 'r') as file:
    data_dict = json.load(fp=file)
    # json.dump(dict_test, fp=file, indent=4)

dict_test.update({'akash:123':123})
dict_test.update(data_dict)

with open('data.json', 'w') as file:
    json.dump(dict_test, fp=file, indent=4)

print(dict_test)