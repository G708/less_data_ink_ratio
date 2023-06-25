import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['#d3d3d3', '#d3d3d3', '#d3d3d3', 'tab:blue']


sord_oder = np.argsort(counts)[::-1]


ax.bar([fruits[i] for i in sord_oder], [counts[i] for i in sord_oder], label=[bar_labels[i] for i in sord_oder], color=[bar_colors[i] for i in sord_oder])


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

plt.savefig('plot.png')