import re

def getCountry(key, value, dataset):
  country = list(
    filter(lambda countryDic: countryDic[key] == value, dataset)
  )
  return country[0]

def getPopulations(countryset):
  allEntries = list( countryset.items() )
  popEntries = list( filter(lambda entry: "Population" in entry[0], allEntries) )

  pops = [
    {key.split(" ")[0]: value} for key, value in popEntries if re.match("[\d]{4,4}", key.split(" ")[0])
  ]

  return pops


if __name__ == "__main__":
  print("Hi")