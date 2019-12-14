from lib import helper

print ("######################################################################################################")
print ("Welcome to confusion matrix program and ML measurement calculator")
print ("The default file to be read is 'data.csv' and should be structured as follows:")
print ("Numbers of rows should be equal to number of columns. Each row is entry in the table")
print ("Lines starting with '#' will be ignored")
print ("Each column is calcification class and diagonal of the table is CORRECT classification")
print ("Real classes are parsed as rows and predicted classes are parsed as columns. Classes are named as 'C[i]\nWhere 'i' is index")

print ("Press ENTER key to start the file processing")

# input()

print ("Here we go!\n\n")

matrix = helper.getMatrix()

helper.printMatrix(matrix)
print (f"Acc: {helper.getAccuracy(matrix)}")

dic = {}
for i in range(len(matrix)):
  dic[f"C{i}"] = helper.getMetrics(i, matrix)
  print(f"C{i}: ", end='')
  helper.printMetrics(dic[f"C{i}"])

# weighted metrics
helper.getWeightedMetrics(dic, matrix)
