import matplotlib.pyplot as plt

years = []
percentage = []

# 房产成本
base = 200
# 回本年限
year = 10
# 每年收益
yearly_earn = base / year

# 期望年限 （从回本后开始）
want = 60

for i in range(1, want):
    years.append(i + 10)
    percentage.append(i * yearly_earn / ((i + year) * base))

plt.plot(years, percentage)
plt.show()
