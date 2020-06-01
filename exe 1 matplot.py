import matplotlib.pyplot as plt

year = [1950,1960,1970,1980]
pop = [2.519,3.629,5.263,6.972]

plt.plot(year,pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population projections')
plt.yticks([0,2,4,6,8,],
           ['0B','2B','4B','6B','8B'])


plt.show()