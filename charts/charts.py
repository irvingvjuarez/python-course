import matplotlib.pyplot as plt

def generatePieChart(labels, values):
	fig, ax = plt.subplots()
	ax.pie(values, labels=labels)
	ax.axis("equal")
	plt.show()

def generateBarChart(labels, values):
	fig, ax = plt.subplots()
	ax.bar(labels, values)
	plt.show()

if __name__ == "__main__":
	generatePieChart([10, 12, 8], ["a", "b", "c"])