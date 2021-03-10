import matplotlib.pyplot as plt

nationalities = ['American', 'German', 'French', 'Other']
students = [60, 23, 17, 34]

pairs = zip(students, nationalities)
pairs = sorted(list(pairs))
students, nationalities = zip(*pairs)

explode = [0, 0, 0.1, 0]
plt.pie(students, labels=nationalities, autopct='%.2f%%', explode=explode, counterclock=False, startangle=90)

plt.title('Student Nationalities')
plt.show()
