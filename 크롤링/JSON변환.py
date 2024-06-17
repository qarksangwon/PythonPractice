import json

customer = {
    "id" : 12345,
    "name" : "SW",
    "history" : [
        {"date" : "2023-06-17", "product" : "iPhone 15 Pro"},
        {"date" : "2023-06-17", "product" : "Galaxy 24"}
    ]
}

jsonString = json.dumps(customer)
print("dict to json ")
print(jsonString)

dict = json.loads(jsonString)
print("json to dict, show history")
for h in dict["history"]:
    print(h["date"], h["product"])