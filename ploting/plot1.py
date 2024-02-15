from matplotlib import pyplot as p

# Line Chart
'''
x=[1,4,6,8]
y=[2,5,3,6]
p.plot(x,y,color='r')
p.show()
'''

#Line Chart With Additional Features
'''
x=[1,4,6,8]
y=[2,5,3,6]
x1=[2,5,7,4]
y1=[1,3,6,9]
p.plot(x,y,color='r',label="Line1")
p.plot(x1,y1,color='b',label="Line2")
p.xlabel("X-Axis")
p.ylabel("Y-Axis")
p.title("Line Chart Demo")
p.legend()
p.show()
'''
#Bar Chart
'''
left=[1,2,3,4,5,6]
height=[10,20,30,40,50,60]
tick_label=['One','Two','Three','Four','Five','Six']
p.bar(left,height,tick_label=tick_label,width=0.8,color=['r','g','b','y','m','k'])
p.show()
'''
#Horizontal Bar Chart
'''
left=[1,2,3,4,5,6]
height=[10,20,30,40,50,60]
tick_label=['One','Two','Three','Four','Five','Six']
p.barh(left,height,tick_label=tick_label,color=['r','g','b','y','m','k'])
p.show()
'''

# Pie Chart


languages = ['C', 'C++', 'Java', 'Python', 'Kotlin']
marks = [9, 8, 7, 5, 4]

p.pie(marks, labels=languages, colors=['red', 'green', 'blue', 'yellow', 'magenta'],
        startangle=180, shadow=True, radius=1.2, autopct='%1.1f%%')
p.title("Mark Analysis")
p.show()





