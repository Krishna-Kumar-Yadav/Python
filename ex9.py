import csv

def calculate(filepath):
  column = 7
  total = 0
  i = 0
  with open(filepath,'r') as file:
    csvFile = csv.reader(file)
    for row in csvFile:
      if i > 0:
        total = total + int(row[column])
      else:
        i = i + 1

    print(total)      



calculate('StudentOutstandingReport.csv')
