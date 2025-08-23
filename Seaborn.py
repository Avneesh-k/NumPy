# Seaborn

# Visualize Distributions With Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.



# Displots
# Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.
import matplotlib.pyplot as plt 
import seaborn as sea 

sea.displot([0,1,1,2,3,4,4,5,5],bins=7)
# plt.show()



# Plotting a Displot Without the Histogram
sea.displot([0,1,2,33,4,5],kind="kde")
plt.show()