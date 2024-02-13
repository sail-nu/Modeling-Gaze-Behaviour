import numpy as np
import matplotlib.pyplot as plt

# Sample data
subjects = ['Novices Coffee', 'Experts Coffee', 'Novices Pinwheels',  'Experts Pinwheels']
parameters = ['Background stimuli', 
'Non-step related AOI', 
'Step-related AOI']

# Set the bar width
bar_width = 0.2
font = {
        # 'weight' : 'bold',
        'size'   : 32
        }

plt.rc('font', **font)


# Set the positions of the bars on the x-axis
r1 = np.arange(len(subjects))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create the grouped bar chart
# plt.bar(r1, values[:, 0], color='b', width=bar_width, edgecolor='white', label=parameters[0])
# plt.bar(r2, values[:, 1], color='g', width=bar_width, edgecolor='white', label=parameters[1])
# plt.bar(r3, values[:, 2], color='r', width=bar_width, edgecolor='white', label=parameters[2])

plt.bar(r1, [60.2, 66.2, 48.1, 34.9], color='b', width=bar_width, edgecolor='white', label=parameters[0])
plt.bar(r2, [30.4, 29.5, 42, 53], color='g', width=bar_width, edgecolor='white', label=parameters[1])
plt.bar(r3, [9.3, 4.1, 9.8, 12], color='r', width=bar_width, edgecolor='white', label=parameters[2])





# Add labels, title, and legend
plt.xlabel('Subject/Task', fontsize=32)
plt.ylabel('Percentage of Fixated Frames', fontsize=32)
plt.title('Distribution of Fixation on Different Stimuli', fontsize=32)
plt.xticks([r + bar_width for r in range(len(subjects))], subjects, size=24)
plt.yticks([(i*10) for i in range(0, 11)], size=20)
plt.legend()

# Display the plot
plt.show()
