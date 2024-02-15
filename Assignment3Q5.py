import matplotlib.pyplot as plt

left=[1,2,3]
height=[31,32,33]
labels=['Android','DW-DM','Python']
colors=['red','green','blue']
plt.bar(left,height,tick_label=labels,color=colors)
plt.xlabel("Subject Name")
plt.ylabel("Subject ID")
plt.title("TY BCA")
plt.show()
