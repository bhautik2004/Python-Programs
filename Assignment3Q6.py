import matplotlib.pyplot as plt

principal=15000
interest_rate=8.5
years=10
values=[]

for i in range(1, years + 1):
    values.append(principal * (1 + interest_rate / 100) ** i)
    
plt.plot(range(1, years + 1), values)
plt.xlabel("Year of Compounding")
plt.ylabel("Value of Principal (Rs.)")
plt.show()
