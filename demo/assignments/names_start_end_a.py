def start_or_end(name):
    lowername = name.lower()
    return lowername.startswith("a") or lowername.endswith("a")

names = ["Andy", "Jack", "Larry", "Belinda", "arnold"]

for name in filter(start_or_end, names):
    print(name)
