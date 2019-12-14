# module scope m8
import functools

columCount = 0
lineCount = 0

def getMatrix ():
  matrix = []
  global columCount
  global lineCount
  with open("data.csv", "r") as file:
    for line in file:
      if line.startswith('#'):
        continue
      lineValues = list(map(int, line.split(',')))
      if lineCount == 0 :
        columCount = len(lineValues)
      lineCount += 1
      if len(lineValues) != columCount:
        return -1
      matrix.append(lineValues)

  if (columCount != lineCount):
    return -1
  return matrix

def printMatrix (matrix):
  global columCount
  global lineCount
  print (f"| ** |", end='')
  for i in range(columCount):
    print (f"\tC{i}", end='')
  print()

  print (f"| ** |", end='')
  for i in range(columCount):
    print ("--------", end='')
  print()

  for row in matrix:
    print (f"| C{matrix.index(row)} |", end='')
    for column in row:
      print (f"\t{column}", end='')
    print()

def getRecall (i, matrix):
  # sum the row
  sum = functools.reduce (lambda a,b: a + b, matrix[i])
  # divied first Major of the matrix by the sum
  return (matrix[i][i] / sum) * 100

def getF1 (r, p):
  return ((r * p)/(r + p) * 2)

def getPrecision (i, matrix):
  # sum the column
  falsePositive = 0
  for j in range(columCount):
    falsePositive += matrix[j][i]
  return (matrix[i][i] / falsePositive) * 100


def getSpecificity (i, matrix):
  global lineCount
  # get true negative
  trueNegative = 0
  for j in range (lineCount):
    trueNegative += matrix[j][j]
  trueNegative - matrix[0][0] # true negative
  falsePositive = 0
  for j in range (lineCount):
    falsePositive += matrix[j][i]
  falsePositive -= matrix[i][i]
  return (trueNegative / (trueNegative + falsePositive)) * 100

def getAccuracy (matrix):
  d = 0
  for i in range(lineCount):
    d+=matrix[i][i]
  # roller coaster code bellow.... Wheeeeeeeeeeeee!!!!
  return (d / functools.reduce(lambda a,b: a + b, list(map(lambda c: functools.reduce(lambda e,f: e + f, c), matrix)))) * 100


def getMetrics (i, matrix):
  recall = getRecall(i, matrix)
  specificity = getSpecificity(i, matrix)
  precision = getPrecision(i, matrix)
  f1 = getF1(recall, precision)

  metrics = {
    "recall": recall,
    "specificity": specificity,
    "precision": precision,
    "f1": f1
  }
  return metrics

def printMetrics (d):
  print (f"\n recall: {d['recall']}\n spec: {d['specificity']}\n precision: {d['precision']}\n f1: {d['f1']}")

def getWeighOfClass (i, matrix):
  return functools.reduce(lambda a,b: a+b, matrix[i]) / functools.reduce(lambda a,b: a + b, list(map(lambda c: functools.reduce(lambda e,f: e + f, c), matrix)))

def getWeightedMetrics(d, matrix):
  w_recall = 0
  w_precision = 0
  w_f1 = 0
  for i in range (lineCount):
    w_recall += d[f"C{i}"]["recall"] * getWeighOfClass(i, matrix)
    w_precision += d[f"C{i}"]["precision"] * getWeighOfClass(i, matrix)
    w_f1 += d[f"C{i}"]["f1"] * getWeighOfClass(i, matrix)
  print (f"W-Recall: {w_recall}")
  print (f"W-Precision: {w_precision}")
  print (f"W-F1: {w_f1}")