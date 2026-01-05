order = {
    "id": 42,
    "items": [
        {"name": "vans", "price": 80},
        {"name": "converse-xxx", "price": 100},
        {"name": "noname", "price": 120}
    ],
    "total": 0
}
def calculate_total(order):
    total = sum(item["price"] for item in order["items"])
    order["total"] = total
    return order

print(order)
calculate_total(order)
print(order)
print("❌ order a été modifié")