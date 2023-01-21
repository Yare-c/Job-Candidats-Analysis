# The analization code, which show who is smarter, girls or boys by exam marks




import csv
import matplotlib.pyplot as plt
import numpy as np


with open('job.csv', 'r') as c: 
	reader = csv.reader(c)
	y = list(reader)
	y.pop(0)
	



def sort_sex_values():
	global men, women
	men = []
	women = []
	i = 0
	
	while i < len(y):
		x = y[i]
		if x[0] == 'M':
			men.append(x[1])
			i = i + 1
		if x[0] == 'F':
			women.append(x[1])
			i = i + 1

	
	
	
sort_sex_values()

men_res = [eval(i) for i in men]
women_res = [eval(i) for i in women]



def average():
	men_average = sum(men_res)/len(men_res)
	women_average = sum(women_res)/len(women_res)
	print(men_average)
	print(women_average)

average()


def plotting():
	h1 = np.arange(start=0, stop=len(men_res), step=1)
	h2 = np.arange(start=0, stop=len(women_res), step=1)
	plt.style.use('ggplot')
	fig, axs = plt.subplots(2)
	axs[0].set_title("men")
	axs[0].bar(h1, men_res)
	axs[1].set_title('women')
	axs[1].bar(h2, women_res)
	plt.show()
plotting()














