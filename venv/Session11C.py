import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))

jobs = [100, 80, 60]
fields = ["Java", "Python", "C++"]

plt.pie(jobs, labels=fields)

plt.legend()

plt.show()
