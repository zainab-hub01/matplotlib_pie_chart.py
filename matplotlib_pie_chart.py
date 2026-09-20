import matplotlib.pyplot as plt
x =["c++","java","c sharp","ruby"]
y=[20,30,50,60]
ex=[0.0,0.0,0.5,0.0]
plt.pie(y,labels=x,explode=ex,autopct="%0.2f%%",shadow=True,radius=0.6,labeldistance=2,startangle=90,textprops={"fontsize":15},counterclock=False,wedgeprops={'linewidth':2,'width':1,"edgecolor":"r"},center=(8,6),rotatelabels=True)#autopct="%0.2f%%" ya os ka ander likhny ka liyai 
# create multiple pie chart 

plt.legend(loc=2)
plt.show()








