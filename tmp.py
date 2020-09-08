ri = 0      # sum i
rj = 1      # pred j
rk = 0      # sum k

for i in range(3, 9):
    print('i = ', i)
    for j in range(2, 6):
        print('j = ', j)
        for k in range(2, 8):
            print('k = ', k)
            rk  += (2*i + j + 2*k)
        rj *= rk
    ri += rj
print(ri) 
    