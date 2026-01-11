import os
world = os.getenv("WORLD")
if world is None:
    print("hello ENSAI, install me in version 0.1.3 to continue your quest")
else:
    print(f"hello {world}, 👏👏")

