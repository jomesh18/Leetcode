n, q = map(int,input().split())
A = list(map(int,input().split()))
Q = []    # список на вывод
size = 1
while size < n:
    size *= 2

C = [[0, [0]*40] for i in range(2*size-1)]
#print(C)

def numb_inv(A,B):
    '''считает количество инверсий при объединении двух списков. Возвращает список'''
    C = []
    s = 0
    s += A[0] + B[0]
    D = [0] * 40
    f = 0
    for i in range(len(A[1])):
        #s += A[1][i]*sum(B[1][:i])
        s += A[1][i]*f
        f += B[1][i]
        D[i] = A[1][i] + B[1][i]
    C.append(s)
    C.append(D)
    return C

def set_numb(A,index,v,lx,rx,q):
    '''устанавливает по индексу новое значение и пеерсчитывает до корня'''
    if rx-lx == 1:
        A[q][0] = 0
        A[q][1] = [0]*40
        A[q][1][v-1] = 1
        return
    m = int((lx+rx)/2)
    if index < m:
        set_numb(A, index, v, lx, m, 2*q+1)
    else:
        set_numb(A, index, v, m, rx, 2 * q + 2)
    A[q] = numb_inv(A[2*q+1],A[2*q+2])
    return

for j in range(len(A)):
    set_numb(C, j, A[j], 0, size, 0)

#print(C)

def inv(A,l,r,lx,rx,q):
    '''число инверсий на отрзезке l до r-1'''
    global M
    if r <= lx or l >= rx:
        return
    elif lx >= l and rx <= r:
        M = numb_inv(M,A[q])
        return M[0]
    m = int((lx+rx)/2)
    inv(A, l, r, lx, m, 2*q+1)
    inv(A, l, r, m, rx, 2*q+2)
    return M[0]

for i in range(q):
    B = list(map(int,input().split()))
    if B[0] == 1:  # определить число инвесрсий на отрезке
        M = [0,[0]*40]
        Q.append(inv(C,B[1]-1,B[2],0,size,0))
    elif B[0] == 2:   # Заменить элемент
        set_numb(C, B[1]-1, B[2], 0, size, 0)

print(*Q, sep='\n')
