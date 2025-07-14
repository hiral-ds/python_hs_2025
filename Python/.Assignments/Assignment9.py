temps = [30, 32, 35, 28, 31, 33, 29]

print("Hottest Day:", max(temps))
print("Coldest Day:", min(temps))

avg = sum(temps) / len(temps)
above_avg_days = [t for t in temps if t > avg]
print("Days above average:", len(above_avg_days))

print("First 3 days:", temps[:3])
print("Last 2 days:", temps[-2:])