# example_plot.py

import matplotlib.pyplot as plt
import numpy as np

# demo data
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

# plot
fig, ax = plt.subplots()

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
legend = ax.legend(title='Fruit color') # must define as this
ax.set_facecolor("lightblue")

plt.savefig('plot.png')