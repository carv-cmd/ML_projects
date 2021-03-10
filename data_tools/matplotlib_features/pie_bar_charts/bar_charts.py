import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# First define the skills and assign a value at each index for each person
python = (85, 67, 23, 98)
java = (50, 67, 89, 34)
networking = (60, 20, 56, 69)
machine_learning = (88, 23, 40, 87)

# Create list of names which the above attributes relate to
people = ['Bob', 'Alice', 'Eve', 'Ben']

# Enter values into the bar chart fields
index = np.arange(4)
plt.bar(index, python, width=0.2, label='Python')
plt.bar(index + 0.2, java, width=0.2, label='Java')
plt.bar(index + 0.4, networking, width=0.2, label='Networking')
plt.bar(index + 0.6, machine_learning, width=0.2, label='Machine Learning')

# Add styling and labels to chart
style.use('ggplot')
plt.title('Computing Skills')
plt.xlabel('Persons Names')
plt.ylabel('Skill Levels')
plt.xticks(index + 0.2, people)

# Activate legend and show bars
plt.legend(loc='upper left')
plt.ylim(0, 125)
plt.show()
