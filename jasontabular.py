import json

products = [
    {"name":"Mobile", "price":200000 , "quantity":15},
    {"name":"Laptops", "price":250000, "quantity":10},
    {"name":"Smart Watch", "price":2500, "quantity":50}
]

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

with open("products.json", "r") as file:
    data = json.load(file)

print("\nName\tPrice\tQuantity")

for item in data:
    print(item["name"], "\t",item["price"], "\t",item["quantity"])