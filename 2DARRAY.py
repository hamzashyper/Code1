
def build_matrix(rows, cols):
    matrix = []

    for r in range(0, rows):           
        if r == 0:
            matrix.append([1 for c in range(0,cols)])
            
        else:
            matrix.append([0 for c in range(0,cols)])
            

    return matrix


v= build_matrix(5, 12)

for a in range (0,5):
    for b in range (0,12):
        print(v[a][b], end = " ")
    print(" ")
