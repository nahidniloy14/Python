for row_1 in range(5):
    for column in range(5-row_1-1):
        print(' ',end=" ")
    for column in range(row_1*2+1):
        print('*',end=" ")
    print('\n')
for row_2 in range(5):
    for column in range(row_2 + 1):
        print(' ', end=" ")
    for column in range(5- row_2*2+2):
        print('*',end=" ")
    for column in range(row_2 + 1):
        print(' ',end=" ")
    print('\n')

#   0 1 2 3 4 5 6 7 8
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
8