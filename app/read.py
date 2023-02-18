import csv

def readFile(path):
  with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    headers = next(reader)
    dataArr = []

    for row in reader:
      tupleArr = zip(headers, row)
      dataArr.append( {header: column for header, column in tupleArr} )

    return dataArr

if __name__ == "__main__":
  readFile("./app/data.csv")

