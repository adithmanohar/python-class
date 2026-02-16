#Print the following pattern using nested loops:
"""
    2
   2 4
  2 4 6
 2 4 6 8
 """
rows = 4  
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(2 * k, end=" ")
    print()
