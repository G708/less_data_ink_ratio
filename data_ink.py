import matplotlib.pyplot as plt
import numpy as np

# demo data
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['#d3d3d3', '#d3d3d3', '#d3d3d3', 'tab:blue']

sord_oder = np.argsort(counts)[::-1]
fruits_oder = [fruits[i] for i in sord_oder]
counts_oder = [counts[i] for i in sord_oder]
bar_labels_oder = [bar_labels[i] for i in sord_oder]
bar_colors_oder = [bar_colors[i] for i in sord_oder]

# plot
fig, ax = plt.subplots()
ax.bar(fruits_oder, counts_oder, label=bar_labels_oder, color=bar_colors_oder)

ax.set_title('Fruit supply')

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')

plt.tick_params(labelbottom=True, labelleft=False, labelright=False, labeltop=False, bottom=True, left=False, right=False, top=False)

plt.gca().axis('off')
plt.savefig('data_ink.png')