import read
from modify import modify
import charts
import retrieve

filename = "./data.csv"

content = read.readFile(filename)

# Chart global population
'''
countryNames = modify("Country/Territory", content)
countryPop = modify("2022 Population", content)

charts.generatePieChart(countryNames, countryPop)
'''


# Chart one country population over time

country = ""

while not country or not list( filter(lambda ctry: ctry["Country/Territory"] == country.capitalize(), content) ):
	country = input("Choose a country: ")

chosenCountry = retrieve.getCountry("Country/Territory", country.capitalize(), content)
countryPops = retrieve.getPopulations(chosenCountry)

labels = []
values = []

for pop in countryPops:
	item = list( pop.items() )[0]
	labels.append(item[0])
	values.append(int(item[1]))

charts.generateBarChart(labels, values)
