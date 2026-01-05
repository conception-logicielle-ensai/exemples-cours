from dataclasses import FrozenInstanceError, dataclass

@dataclass(frozen=True)
class Order:
    id: int
    items: list
    total: float = 0.0
order = Order(id=2,items=["vans"],total=0)
try:
    order.total = 100  # ❌ FrozenInstanceError
except FrozenInstanceError:
    print("Exception jetée FrozenInstanceError")
print("reaffectation once again")
try:
    order = Order(id=order.id,items=order.items, total=100)
    print("la reaffectation fonctionne")
    print(order)
except FrozenInstanceError:
    print("Ne s'affichera jamais")
print(order)
liste = order.items
liste.append("converse")
print(order)
