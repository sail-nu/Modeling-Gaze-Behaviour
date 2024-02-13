import numpy as np
import matplotlib.pyplot as plt

# Sample data
subjects = ['Novices Coffee', 'Experts Coffee', 'Novices Pinwheels', 'Experts Pinwheels']

# AFD parameters
# parameters = ['Step related objects AFD', 'Non-step related objects AFD']

# ASD parameters
parameters = ['AFD', 'ASD']


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

plt.bar(r2, [450.22, 698.27, 411.84, 735.59], color='blue', width=bar_width, edgecolor='white', label=parameters[0])
plt.bar(r3, [143.43, 182.70, 146.53, 188.56], color='red', width=bar_width, edgecolor='white', label=parameters[1])



# Add labels, title, and legend
plt.xlabel('Subject/Task', fontsize=32)

#AFD
# plt.ylabel('Average Fixation Duration (mm)')
# plt.title('Average Fixation Duration based on Task-Relevant AOIs')

#ASD
plt.ylabel('Duration (ms)', fontsize=32)
plt.title('Average Saccade Duration (ASD) and Average Fixation Duration (AFD)', fontsize=32)

plt.xticks([r + (1.5 * bar_width) for r in range(len(subjects))], subjects, size=24)
plt.legend()

# Display the plot
plt.show()
