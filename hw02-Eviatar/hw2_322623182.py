# Skeleton file for HW2 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw2_ID.py).

import random  # loads python's random module in order to use random.random() in question 2

##############
# QUESTION 1 #
##############

# 1a
def print_rectangle(length, width):
    '''
    Define how a row in the middle(not first or last) should look like, iterate through it and return final string
    '''
    assert (length >=3 and length <=100)
    assert (width >=3 and width <=100)
    part_row = "*"+(width-2)*" "+"*"+"\n"
    str1 = width*"*"+"\n"
    for i in range(length-2):
        str1+=part_row

    str1+= width*"*"
    return(str1)



# 1b
def x_o_winner(board):
    '''
    Define a list with all the options to define a winner
    Create a string of the board
    for each set, we will check if there is a winner which isn't e
    If so, return it,
    If there is no winner after all the sets, means we don't have a winner
    '''
    lst = [(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6),(0,1,2),(3,4,5),(6,7,8)]
    s1 = ""
    for item in board:
        for i in range(len(item)):
            s1+=item[i]
    for s in lst:
        x1,x2,x3 = s
        if(s1[x1]==s1[x2] and s1[x2] == s1[x3] and s1[x1]!="e"):
            return s1[x1]
    return "no winner"



# 1c
def valid_braces(s):
    '''
    Define list of all braces
    Define dictionary for each open and close type of brace
    Extract all the braces from s
    If the length of the list isn't even, we know the braces aren't valid
    We will iterate through lst1
    If there is no match between the first and last, We will return False
    '''
    braces = ["[","]","{","}","(",")"]
    dict1 = {"[":"]","(":")","{":"}"}
    lst1 = [c for c in s if c in braces]
    if(len(lst1) % 2 == 1):
        return False
    while len(lst1) >0:
        if(lst1[0] == "}" or lst1[0] == ")" or lst1[0] == "]"):
            return False
        if dict1[lst1[0]] == lst1[-1]:
            lst1.pop(0)
            lst1.pop()
        elif dict1[lst1[0]] == lst1[1]:
            lst1.pop(1)
            lst1.pop(0)
        else:
            return False
    return True


##############
# QUESTION 2 #
##############


# 2a
def coin():
    '''
    if the random.random() return number <0.5, The output will be False, Otherwise True
    '''
    return random.random()>=0.5  


# 2b
def roll_dice(d):
    '''
    To return a value between 1 and d using only random.random(), we have to multiply the value in random.random() by the input d,
    than add 1 so we won't get 0 as a output. To return a netural number, we return the int of this number/
    '''
    return int(d*random.random()+1)


# 2c
def roulette(bet_size, parity):
    '''
    Define a game of roulette according to the rules on HW
    '''
    dice = roll_dice(37)-1
    if dice == 0:
        return 0
    int_parity = 0
    if parity == "odd":
        int_parity =1
    if dice %2 == int_parity:
        return bet_size*2
    else:
        return 0


# 2d
def roulette_repeat(bet_size, n):
    '''
    Repeat roulette game n times
    '''
    money = 0
    for i in range(n):
        if coin() == True:
            parity = "odd"
        else:
            parity = "even"
        money += roulette(bet_size,parity) - bet_size
    return money


# 2e
def shuffle_list(lst):
    '''
    Shuffle a list using roll_dice
    '''
    copy_lst = [c for c in lst]
    for i in range(len(lst)):
        lst.pop()
    for i in range(len(copy_lst)):
        index = roll_dice(len(copy_lst))-1
        lst.append(copy_lst[index])
        del copy_lst[index]
    return lst

# 2f
def count_steps(d):
    '''
    Random walk on 1d until we reach d
    '''
    loc = 0
    cnt = 0
    while True:
        step = coin()
        if step:
            step = 1
        else:
            step = -1
        loc += step
        cnt+=1
        if(loc == d or loc == -d):
            return cnt
            

def avg_count_steps(d):
    '''
    Random walk 10000 times to find the avg length of walk
    '''
    sum1 = 0
    for i in range(10000):
        sum1 += count_steps(d)
    avg = (sum1/10000)
    return avg


#2g
def count_steps_2dim(d):
    '''
    Random walk on 2d, using coin
    '''
    locx = 0
    locy = 0
    cnt = 0
    
    while True:
        if coin() == True:
            if coin() == True:
                locx += 1
            else:
                locx -= 1
        else:
            if coin() == True:
                locy += 1
            else:
                locy -= 1
        cnt += 1
        if d == (locx**2+locy**2)**0.5:
            break

    return cnt
        


##############
# QUESTION 3 #
##############


# 3a
def inc(binary):
    '''
    Add 1 to inputed binary number in string
    '''
    new_num = ""
    carried_digit = 1
    for num in binary[::-1]:
        if carried_digit == 1:
            if num == "0":
                new_num = "1" + new_num
                carried_digit = 0
            else:
                new_num = "0" + new_num
        else:
            if num == "0":
                new_num = "0" + new_num
            else:
                new_num = "1" + new_num
    if carried_digit == 1:
        new_num = "1" + new_num
    return new_num


# 3b
def add(bin1, bin2):
    '''
    Define a method to add 2 binary numbers
    We will put the "longer" one in bin 1, and add in each index the 2 numbers, withoud forgetting the carried digit
    '''
    new_num = ""
    carried_digit = 0
    flag = False #to store if len of two number is equal
    if(len(bin1) != len (bin2)):
        flag = True
        if(len(bin2) > len(bin1)):
            bin1,bin2 = bin2,bin1
    for i in range(len(bin2)):
        num1 = bin1[-1-i]
        num2 = bin2[-1-i]
        if carried_digit == 0:
            if num1 == num2 and num2 == "0":
                new_num = "0" + new_num
            elif num1 == num2 and num2 == "1":
                new_num = "0" + new_num
                carried_digit = 1
            else:
                new_num = "1" + new_num
        elif carried_digit == 1:
            if num1 == num2 and num2 == "0":
                  new_num = "1" + new_num
                  carried_digit = 0
            elif num1 == num2 and num2 == "1":
                new_num = "1" + new_num
            else:
                new_num = "0" + new_num
                carried_digit = 1
    
    if flag:
        for i in range(len(bin2),len(bin1)):
            num1 = bin1[-1-i]
            if carried_digit == 0:
                 if num1 =="0":
                    new_num = "0" + new_num
                 else:
                    new_num = "1" + new_num
            elif carried_digit == 1:
                if num1 == "0":
                    new_num = "1"+ new_num
                    carried_digit = 0
                else:
                    new_num = "0" + new_num
    if carried_digit ==1:
        new_num = "1" + new_num
    return new_num

# 3c
def pow_two(binary, power):
    '''
    Compute binary **power using add method from 3b
    '''
    num = binary
    for i in range(2**power-1):
        num = add(num, binary)
    return num


# 3d
def div_two(binary, power):
    '''
    Compute binary/(2**power)
    '''
    cnt_keep = len(binary)- power
    if cnt_keep > 0:
        return binary[0:cnt_keep]
    else:
        return "0"
        

# 3e
def leq(bin1, bin2):
    '''
    Return True if bin1<=bin2, False otherwise
    '''
    if len(bin1) != len(bin2):
        if len(bin2) > len(bin1):
            return True
        elif len(bin1) > len(bin2):
            return False
    for i in range(len(bin1)):
        b1 = bin1[i]
        b2 = bin2[i]
        if(b1 != b2):
            if b1>b2:
                return False
            elif b2>b1:
                return True
        continue
    
    return True
    
# 3f
def to_decimal(binary):
    '''
    Convert binary to decimal
    '''
    num = 0
    lst = [c for c in binary]
    lst.reverse()
    for i in range(len(lst)):
        num += int(lst[i]) * 2**i
    return num


##############
# QUESTION 5 #
##############


# 5a
def divisors(n):
    '''
    Create and return a list of all the dividors of n from 1 till n-1 using list comprehension
    '''
    return [num for num in range(1,n) if n % num == 0]


# 5b
def perfect_numbers(n):
    '''
    Return a list of n perfect numbers(number which the sum of his divisors is the number)
    '''
    count = 0
    lst = []
    num = 1
    while count < n:
        if sum(divisors(num)) == num:
            count +=1
            lst.append(num)
        num+=1
    return lst


# 5c
def abundant_density(n):
    '''
    Compute the density of all the numbers between 1 and n
    '''
    count = 0
    for num in range(n+1):
        if sum(divisors(num)) > num:
            count+=1
    return count/n


# 5e
def semi_perfect_3(n):
    '''
    A number is semi perfect if sum of 3 different dividors of his equals the number
    '''
    lst_divisors = divisors(n)
    len1 = len(lst_divisors)
    for i in range(len1):
        for j in range(i+1,len1):
            for k in range(j+1, len1):
                if lst_divisors[i] +lst_divisors[j] + lst_divisors[k] ==n:
                    return [lst_divisors[c] for c in [i,j,k]]
    return None

##########
# Tester #
##########

def test():
    if print_rectangle(4, 5) != "*****\n*   *\n*   *\n*****" or \
       print_rectangle(3, 3) != "***\n* *\n***" or \
       print_rectangle(5, 4) != '****\n*  *\n*  *\n*  *\n****':
        print("#1a - error in print_rectangle")

    if x_o_winner(["eee", "xxx", "eoo"]) != "x" or \
       x_o_winner(["xee", "oxo", "eex"]) != "x" or \
       x_o_winner(["eex", "oxe", "xoe"]) != "x" or \
       x_o_winner(["oee", "oxx", "oeo"]) != "o" or \
       x_o_winner(["eee", "eee", "eeo"]) != "no winner":
        print("#1b - error in x_o_winner")

    if valid_braces("(ab{cd}ef)") is not True or \
       valid_braces("{this(is]wrong") is not False or \
       valid_braces("{1:(a,b),2:[c,d)}") is not False:
        print("#1c - error in valid_braces")

    for i in range(10):
        if coin() not in {True, False}:
            print("#2a - error in coin")
            break

    for i in range(10):
        if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
            print("2b - error in roll_dice")
            break

    for i in range(10):
        if (roulette(100, "even") not in {0, 200}) or (roulette(100, "odd") not in {0, 200}):
            print("2c - error in roulette")
            break

    if shuffle_list([1, 2, 3, 4]) == [1, 2, 3, 4] or \
       shuffle_list(["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"] or \
       shuffle_list([(1, 2), (3, 4), ("a", "b")]) == [(1, 2), (3, 4), ("a", "b")]:
        print("2e - error in shuffle_list")

    if not 24 < avg_count_steps(5) < 26:  # very low probability that a good implementation will be out of this range
        print("2f - error in avg_count_steps")

    if count_steps_2dim(5) < 5:  # can't reach d in less than d steps
        print("2g - error in count_steps_2dim")

    if inc("0") != "1" or \
       inc("1") != "10" or \
       inc("101") != "110" or \
       inc("111") != "1000" or \
       inc(inc("111")) != "1001":
        print("3a - error in inc")

    if add("0", "1") != "1" or \
       add("1", "1") != "10" or \
       add("110", "11") != "1001" or \
       add("111", "111") != "1110":
        print("3b - error in add")

    if pow_two("10", 2) != "1000" or \
       pow_two("111", 3) != "111000" or \
       pow_two("101", 1) != "1010":
        print("3c - error in pow_two")

    if div_two("10", 1) != "1" or \
       div_two("101", 1) != "10" or \
       div_two("1010", 2) != "10" or \
       div_two("101010", 3) != "101":
        print("3c - error in div_two")

    if not leq("1010", "1010") or \
           leq("1010", "0") or \
           leq("1011", "1010"):
        print("3d - error in leq")

    if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
        print("5a - error in divisors")

    if perfect_numbers(2) != [6, 28]:
        print("5b - error in perfect_numbers")

    if abundant_density(20) != 0.15:
        print("5c - error in adundant_density")

    if semi_perfect_3(18) != [3, 6, 9] or semi_perfect_3(20) is not None:
        print("5e - error in semi_perfect_3")
