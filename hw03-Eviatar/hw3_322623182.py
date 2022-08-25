# Skeleton file for HW3 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).
import math
import random

# Q2 - C
def bin_to_fraction(binary):
    sum1 = 0
    for i in range(len(binary)):
        if binary[i]=="1":
            sum1+=2**-(int(i)+1)
    return sum1

# Q2 - D
bin_to_float = lambda binary: (int(-1)**int(binary[0]))*(2**(int(binary[1:9],2)-127))*(1+(bin_to_fraction(binary[9:])))

# Q2 - E
def is_greater_equal(bin1, bin2):
    if(bin1[0]!=bin2[0]): #Check if the sign is not the same(+ and - or - and +)
       if(bin1[0]=="0"):
           return True
       return False
    for i in range(1,32):
        if(bin1[i]!=bin2[i]):
            if(bin1[i]=="1"):
                if(bin1[0] == "0"):
                    return True
                else:
                    return False
            else:
                if(bin1[0] == "0"):
                    return False
                else:
                    return True
    return True


# Q3 - A
def approx_root(x, e):
    lst1 = []
    sum1 = 0
    i = 1
    while True:
        if (1/(i*i))<=x:
            lst1.append(i)
            sum1+=1/i
            break
        i+=1
    i = lst1[0]
    while(x >= (e+sum1)*(e+sum1)):
            if (sum1+1/(math.prod(lst1)*i))*(sum1+1/(math.prod(lst1)*i))<=x:
                sum1+= 1/(math.prod(lst1)*i)
                lst1.append(i)
            else:
                i+=1
    return (lst1,sum1)
            
        
                


# Q3 - B
def single_e_approx():
    sum1 = 0
    cnt = 0
    while sum1 < 1:
        sum1+=random.random()
        cnt+=1
    return cnt
def approx_e(N):
    cnt = 0
    for game in range(N):
        cnt += single_e_approx()
    return cnt/N

# Q4 - A
def find(lst, s):
    if(len(lst)<=1):
        if len(lst) ==1:
            if(lst[0]) == s:
                return 0
        else:
            return None
    n = len(lst)
    left = 0
    right = n-1

    while left <= right and right-left>=3:
        mid = (right-left)//2
        if s == lst[mid-1] or s == lst[mid] or s == lst[mid+1]:
            if s== lst[mid-1]:
                return mid-1
            elif s== lst[mid]:
                return mid
            else:
                return mid+1
        elif  s < lst[mid-1]:
            right = mid-2
        else :
            left = mid+2
    if(s == lst[left]):
        return left
    elif (s == lst[right]):
        return right
    elif (s == lst[(right+left)//2]):
        return (right+left)//2
    elif ( s== lst[(right+left)//2 +1]):
        return (right+left)//2 + 1
        
    return None


# Q4 - B
def sort_from_almost(lst):
    if (len(lst) <= 1):
        return lst
    tmp =0
    
    i = 0
    while i+1<len(lst):
        if(lst[i] > lst[i+1]):
          tmp = lst[i+1]
          lst[i+1] = lst[i]
          lst[i] = tmp
        i+=1
    return lst
# Q4 - C
def find_local_min(lst):
    if (len(lst) == 1):
        return 0
    if(lst[0] <= lst[1]):
        return 0
    i = 1
    while i+1 < len(lst):
        if(lst[i] <= lst[i-1] and lst[i] <= lst[i+1]):
           return i
        i+=1           
    if lst[-1] <= lst[-2]:
        return (len(lst)-1)
    return None

# Q5 - A
def string_to_int(s):
    dict1 = {"a":0, "b":1, "c":2, "d":3,"e":4}
    rslt = 0
    k = len(s)-1
    for char in s:
        rslt += dict1[char] * (5**k)
        k-=1
    return rslt
#Q5 - B
def int_to_string(k, n):
    dict1 = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e"}
    lst = [None for c in range(k)]
    for i in range(1,k+1):
        lst[k-i] = dict1[n%5]
        n//=5
    return "".join(lst)

# Q5 - C
def sort_strings1(lst, k):
    num = 0
    lst1 = [None for c in range(5**k)]
    for s in lst:
        num = string_to_int(s)
        if lst1[num] == None :
            lst1[num] = [s]
        else:
            lst1[num].append(s)
    lst_out = []
    
    for item in lst1:
        if item != None:
            lst_out.append(item)
    lst_out = [item for sub in lst_out for item in sub]
    
    return lst_out
            
    
# Q5 - E
def sort_strings2(lst, k):
    lst_out = []
    num = 0
    for i in range(5**k):
        for item in lst:
           num = string_to_int(item)
           if i==num:
               lst_out.append(item)
           if len(lst_out) == len(lst):
               break
    return lst_out
        
    



##########
# Tester #
##########
def test():
    # Q2 - C
    if bin_to_fraction('01101') != 0.40625 or bin_to_fraction('1010000') != 0.625:
        print('error in bin_to_fraction')
    # Q2 - D
    if bin_to_float('00111110001000000000000000000000') != 0.15625:
        print("error in bin_to_float")

    # Q2 - E
    if is_greater_equal('00111110001000000000000000000000', '00111111001000000000000000000000') == True or \
       is_greater_equal('00111110001000000000000000000000', '00111110001000000000000000000000') == False:
        print("error in is_greater_equal")
  # Q3 - A
    if approx_root(2, 0.1) != ([1, 3], 1 + 1/3):
        print("error in approx_root (1)")
    if approx_root(2, 0.02) != ([1, 3, 5], 1 + 1/3 + 1/15):
        print("error in approx_root (2)")
    if approx_root(2, 0.001) != ([1, 3, 5, 5], 1 + 1/3 + 1/15 + 1/75):
        print("error in approx_root (3)")

    # Q3 - B
    if abs(approx_e(1000000) - math.e) > 0.01:
        print("MOST LIKELY there's an error in approx_e (this is a probabilistic test)")

    # Q4 - A
    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
    if find(almost_sorted_lst, 5) != 3:
        print("error in find")
    if find(almost_sorted_lst, 50) != None:
        print("error in find")
    
    # Q4 - B
    if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst):
        print("error in sort_from_almost")

    # Q4 - C
    lst = [5, 6, 7, 5, 1, 1, 99, 100]
    pos = find_local_min(lst)
    if pos not in (0, 4, 5):
        print("error in find_local_min")

    # Q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if string_to_int(s) != i:
            print("error in int_to_string and/or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")
        
