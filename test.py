import json
import matplotlib.pyplot as plt


with open("data.json", "r") as f:
    data = json.load(f)

ls = [x for x in range(1000)]

plt.plot(ls, data["pyx"])
plt.plot(ls, data["py"])
plt.legend(["Cython", "Python"])
plt.xlabel("Input Size")
plt.ylabel("Time taken")
plt.show()
