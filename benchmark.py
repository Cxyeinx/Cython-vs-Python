from timeit import timeit
import json


lst_pyx = []
lst_py = []

for i in range(1000):
    pyx = timeit(f"Cython_example.primes({i})", setup="import Cython_example", number=100)
    py = timeit(f"Python_example.primes({i})", setup="import Python_example", number=100)
    lst_pyx.append(pyx)
    lst_py.append(py)

with open("data.json", "r") as f:
    data = json.load(f)

data["pyx"] = lst_pyx
data["py"] = lst_py

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
