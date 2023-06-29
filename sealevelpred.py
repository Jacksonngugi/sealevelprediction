import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  
    # Create scatter plot
  fig,ax=plt.subplots()
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']

  plt.scatter(x,y)

    # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(x,y)
  
  x1 = list(range(1880,2050))
  y1 = []

  for year in x1:
    y1.append((round(intercept+(slope*year),7)))

  print(x1[0],x1[len(x1)-1])

  plt.plot(x1,y1,'r',label='first line of best fit')
  plt.legend()
  
    # Create second line of best fit
  x2 = df[ df['Year'] >= 2000 ]['Year']
  y2 = df[ df['Year'] >= 2000 ]['CSIRO Adjusted Sea Level']
 
  bestfit2 = linregress(x2, y2)
  new_slope = bestfit2.slope
  new_intercept = bestfit2.intercept

  x3 = list(range(2000, 2050))
  y3 = []

  for year in x3:
      y3.append(new_intercept + (new_slope * year))

  plt.plot(x3, y3, 'm', label = 'second line of best fit')
  plt.legend()

    # Add labels and title

  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise In Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.show()
  #plt.savefig('sea_level_plot.png')
  return plt.gca()
draw_plot()