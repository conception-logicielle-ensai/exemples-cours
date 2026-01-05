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
    return {
        **order,
        "total": total
    }

print(order)
calculate_total(order)
print(order)
print("👌 order n'a pas été modifié")
# comment on fait du coup ?
print("reaffectation")
order = calculate_total(order)
print(order)
print("👌 order a été modifié mais on a pu le contrôler")
