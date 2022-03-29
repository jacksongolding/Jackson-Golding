def createMatrix(matrix):
  for row in matrix:
    for col in row:
      print(col, end=" ")
    print()

def matrixTest():
  numPad = [[1,2,3],
            [4,5,6],
            [7,8,9],
            [" ",0," "]]

  matrix = [["Numpad", numPad]]

  for title, matrix in matrix:
    print(title)
    createMatrix(matrix)
    print()
