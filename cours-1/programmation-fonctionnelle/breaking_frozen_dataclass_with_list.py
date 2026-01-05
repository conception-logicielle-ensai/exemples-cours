from dataclasses import FrozenInstanceError, dataclass

@dataclass(frozen=True)
class Order:
    id: int
    items: list
    total: float = 0.0
order = Order(id=2,items=["vans"],total=0)

print(order)
liste = order.items
liste.append("converse")
print(order)
