def k_knight(p):
    column = ord(p[0]) - ord('a') + 1
    row = int(p[1])
    steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), 
             (2,1), (1,2), (-1,2), (-2,1)]
    result = 0

    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_row <= 8:
            result = result + 1 

    return result
