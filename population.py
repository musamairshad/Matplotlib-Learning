import matplotlib.pyplot as plt

year = [1950, 1951, 1952, 1953]
pop = [2.538, 2.57, 2.62, 2.68]

# Add some more data:
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop
plt.plot(year, pop)
plt.xlabel("Year") # lable on x-axis.
plt.ylabel("Population") # lable on y-axis.
plt.title("World Population Projections") # lable on the top.
plt.yticks([0, 2, 4, 6, 8, 10], # ticks on y-axis
           ['0', '2B', '4B', '6B', '8B', '10B'] # name of the ticks.
           # B stands for billions.
           )
plt.show()