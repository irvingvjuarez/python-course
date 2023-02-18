import matplotlib.pyplot as plt

def generatePieChart(labels, values):
	fig, ax = plt.subplots()
	ax.pie(values, labels=labels)
	ax.axis("equal")
	plt.savefig("./figures/pie.png")
	plt.close()

def generateBarChart(labels, values):
	fig, ax = plt.subplots()
	ax.bar(labels, values)
	plt.savefig("./figures/bar.png")
	plt.close()

if __name__ == "__main__":
	generatePieChart([10, 12, 8], ["a", "b", "c"])