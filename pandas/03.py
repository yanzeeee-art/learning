import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('workoutdata.csv')

df.plot()
plt.show()