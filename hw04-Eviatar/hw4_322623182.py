# Skeleton file for HW4 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).
def winnable_mem(board):
    d = {}
    return winnable_mem_rec(board, d)

# 1c
def winnable_mem_rec(board, d):
    '''
    Define a munch game function with memoization
    '''
    if (sum(board)==0):
        return True
    m = len(board)
    for i in range(m):
        for j in range(board[i]):
            munched_board = board[0:i] +[min(board[k],j) for k in range(i,m)]
            if tuple(munched_board) not in d:
                res = winnable_mem_rec(munched_board,d)
                d[tuple(munched_board)] = res
            if not d[tuple(munched_board)]:
                return True
    return False

# 2a
def H_local(n, i, j):
    '''
    Return the M in index(i,j) in hadmard matrix of size 2^n * 2^n
    Time complexity: O(n^2)
    '''
    num = pow(2,n)
    if (n==0):
        return 0
    if(i>=num//2 and j>=num//2):
        if(H_local(n-1,i-num//2,j-num//2) ==1):
            return 0
        return 1
    if i>=num/2:
        i = i-num//2
    if j>=num//2:
        j = j-num//2
    return H_local(n-1,i,j)
    
# 2c
    '''
    Create a list with a full hamdmard matrix of size 2^n * 2^n
    '''
H_complete = lambda n: [[H_local(n,i,j) for j in range(pow(2,n))]for i in range(pow(2,n))]


# 3a
def can_create_once(s, L):
    '''
    Can create sum s using L objects, using each object exactly one time.
    Time complexity: O(2^n)
    '''
    def q3a_rec(s,L,i):
        if i == len(L) and s==0:
            return True
        elif i== len(L):
            return False
        return q3a_rec(s+L[i],L, i+1) or q3a_rec(s-L[i], L, i+1)

    return q3a_rec(s,L,0)


# 3b
def can_create_twice(s, L):
    '''
    Can create sum s using L objects, using each object 0/1/2 time.
    Time complexity: O(5^n)
    '''
    def q3b_rec(s,L,i):
        if i == len(L) and s==0:
            return True
        elif i == len(L):
            return False
        return q3b_rec(s+L[i],L, i+1) or q3b_rec(s+2*L[i],L, i+1) or q3b_rec(s-L[i], L, i+1) or q3b_rec(s-2*L[i], L, i+1) or q3b_rec(s,L, i+1)

    return q3b_rec(s,L,0)

# 3c
def valid_braces_placement(s, L):
    '''
    Given sum s and L objects, can we put braces on L objects to write a math expression valued s
    Time complexity: O(n!)
    '''
    if(len(L)<=3):
        if len(L) ==0:
            return s==0
        elif len(L) == 1:
            return s == L[0]
        else:
            return s == eval(str(L[0])+(L[1])+str(L[2]))
    for i in range(0,len(L)-2,2):
        res = eval(str(L[i]) + str(L[i+1]) + str(L[i+2]))
        lst = []
        j=0
        while j<i:
            lst.append(L[j])
            j+=1
        lst.append(res)
        j+=3
        while j< len(L):
            lst.append(L[j])
            j+=1
        if valid_braces_placement(s,lst):
            return True
    return False
        
# 4a
def grid_escape1(B):
    '''
    Given matrix B of size n*n, starting from B[0][0], can we move to B[n][n] using the values of the matrix?
    We can move up or right. Number of steps for each move is the matrix value at our current position.
    '''
    
    def q4a_rec(B,i,j):
        a,b = False,False
        if i == j and i == len(B)-1:
            return True
        if(B[i][j] == 0):
            return False
        if(i+B[i][j] <= len(B)-1):
            a = q4a_rec(B,i+B[i][j],j)    
        if(j+B[i][j] <=len(B)-1):
            b = q4a_rec(B,i,j+B[i][j])
        return a or b
    if len(B) ==0:
        return True
    return q4a_rec(B,0,0)

# 4b
def grid_escape2(B):
    '''
    Given matrix B of size n*n, starting from B[0][0], can we move to B[n][n] using the values of the matrix?
    We can move up, down, left, right. Number of steps for each move is the matrix value at our current position.
    We uses memoization to avoid infinite loop, and improve our runtime.
    '''
    def q4b_rec(B,i,j,dic):
        a,b,c,d = False,False,False,False
        if i == j and i == len(B)-1:
            return True
        if(B[i][j] == 0):
            return False
        if(i+B[i][j] <= len(B)-1 and (i+B[i][j],j) not in dic):
            dic[(i+B[i][j],j)] = 1
            a = q4b_rec(B,i+B[i][j],j,dic)    
        if(j+B[i][j] <=len(B)-1 and (i,j+B[i][j]) not in dic):
            dic[(i,j+B[i][j])] = 1
            b = q4b_rec(B,i,j+B[i][j],dic) 
        if(i-B[i][j] >= 0 and (i-B[i][j],j) not in dic):
            dic[(i-B[i][j],j)] = 1
            c = q4b_rec(B,i-B[i][j],j,dic)
        if(j-B[i][j] >= 0 and (i,j-B[i][j]) not in dic):
            dic[(i,j-B[i][j])] = 1
            d = q4b_rec(B,i,j-B[i][j],dic)
        return a or b or c or d
    if (len(B) == 0):
        return True
    return q4b_rec(B,0,0,{})


##########
# Tester #
##########
def test():
    # 1c
    if winnable_mem([5, 5, 3]) or not winnable_mem([5, 5, 5]):
        print("error in winnable_mem")
    # 2a
    if H_local(2,2,2) != 1:
        print("error in H_local")
    # 2c
    if H_complete(1) != [[0,0],[0,1]]:
        print("error in H_complete")
    # 3a
    if not can_create_once(6, [5, 2, 3]) or not can_create_once(-10, [5, 2, 3]) \
            or can_create_once(9, [5, 2, 3]) or can_create_once(7, [5, 2, 3]):
        print("error in can_create_once")
    # 3b
    if not can_create_twice(6, [5, 2, 3]) or not can_create_twice(9, [5, 2, 3]) \
        or not can_create_twice(7, [5, 2, 3]) or can_create_once(19, [5, 2, 3]):
        print("error in can_create_twice")
    # 3c
    L  = [6, '-', 4, '*', 2, '+', 3]
    if not valid_braces_placement(10, L) or not valid_braces_placement(1, L) or valid_braces_placement(5, L):
        print("error in valid_braces_placement")

    B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
    B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]
    B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]

    # 4a
    if grid_escape1(B1) is False:
        print("error in grid_escape1 - B1")
    if grid_escape1(B2) is True:
        print("error in grid_escape1 - B2")
    if grid_escape1(B3) is True:
        print("error in grid_escape1 - B3")

    # 4b
    if grid_escape2(B1) is False:
        print("error in grid_escape2 - B1")
    if grid_escape2(B2) is False:
        print("error in grid_escape2 - B2")
    if grid_escape2(B3) is True:
        print("error in grid_escape2 - B3")
