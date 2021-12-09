matrix = []
file = open("2021/day9/input.txt","r")
for line in file.readlines():
    row = []
    for num in line.strip():
        row.append(int(num))
    matrix.append(row)

def is_low_point(row,col,matrix):
    max_row = len(matrix)-1
    max_col = len(matrix[0]) -1
    is_low = 1
    #left
    if(col != 0):
        if(matrix[row][col-1] <= matrix[row][col]):
            is_low = 0
    #right
    if(col != max_col):
        if(matrix[row][col+1] <= matrix[row][col]):
            is_low = 0
    # top
    if(row != 0):
        if(matrix[row-1][col] <= matrix[row][col]):
            is_low = 0
    # bottom
    if(row != max_row):
        if(matrix[row+1][col] <= matrix[row][col]):
            is_low = 0 
    return is_low

final_arr = []
def recursive_growth_of_basins(row,col,matrix):
    global final_arr
    max_row = len(matrix)-1
    max_col = len(matrix[0]) -1  
    if([row,col] not in final_arr):
        final_arr.append([row,col])
    #left
    if(col != 0):
        if(matrix[row][col-1] != 9):
            if([row,col-1] not in final_arr):
                recursive_growth_of_basins(row,col-1,matrix)
    #right
    if(col != max_col):
        if(matrix[row][col+1] != 9):
            if([row,col+1] not in final_arr):
                recursive_growth_of_basins(row,col+1,matrix)
    # top
    if(row != 0):
        if(matrix[row-1][col] != 9):
            if([row-1,col] not in final_arr):
                recursive_growth_of_basins(row-1,col,matrix)
    # bottom
    if(row != max_row):
        if(matrix[row+1][col] != 9):
            if([row+1,col] not in final_arr):
                recursive_growth_of_basins(row+1,col,matrix)


all_low_points = []
lol = []

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if(is_low_point(row,col,matrix)):
            final_arr = []
            recursive_growth_of_basins(row,col,matrix)
            lol.append(len(final_arr))

lol.sort()

print(lol[-1]*lol[-2]*lol[-3])