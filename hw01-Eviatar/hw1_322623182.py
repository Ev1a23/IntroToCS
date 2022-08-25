#Skeleton file for HW1 - Spring 2021 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.
#you can add new functions if needed.

#Change the name of the file to include your ID number (hw1_ID.py).


#Question 4a
def num_different_letters(text):
    chars = "abcdefghijklmnopqrstuvwxyz"
    cnt = 0 #counter
    lst1 = [c for c in chars] #list that every object in it is a char in chars ['a','b',...,'z']
    for char in text: #iterate through every char in text
        if(char in lst1): #if char is within lst1
            cnt+=1 #add 1 to the counter
            lst1.remove(char) #remove the char from lst1, so if char is found again in the string, it won't be counted
    return cnt
        
        

#Question 4b
def replace_char(text, old, new):
    str1 = "" #new string that will be returned
    for char in text: #iterate through every char in text
        if (char == old): #if the current char equals to the value we want to replace
            str1+= new #add to returned string the new char
        else:
            str1+= char #add to returned string the current char
    return str1
#Question 4c
def longest_word(text):
    lst1 = text.split() #list of every word in text
    long = 0 #variable to save the length of the longest word
    for word in lst1: #iterate through every word in lst1
        if(len(word) > long): #if the length of current word is longer than the current longest word
            long = len(word) #put the length of the current word in the long variable
    return long

#Question 4d
def to_upper(text):
    '''
    We know that for every lower letter in english, there is a upper one.
    My solution will use the index of the lower letter to put the upper letter in the returned string
    '''
    
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lst_lower = [c for c in lower] #list of every lower letter
    lst_upper = [c for c in upper] #list of every upper letter
    str1 = "" #returned string
    for char in text: #iterate through every char in text
        if(char not in lst_lower): #if the char isn't a lower letter
            str1+=char #add the not lower char to the returned string
            continue # we don't want to execute the rest of this current itteration if char isn't a lower letter, so we use continue
        str1+= lst_upper[lst_lower.index(char)] #we search the index of char in lst_lower, and add to the returned string the letter in the same index in lst_upper
    return str1
    

#Question 5
def calc(expression):
    if expression == "":
        return ""
    lst = expression.split("'") #split the expression into list, and the split sign is "'"
    for exp in lst:
        if exp =="":
            lst.remove(exp) #remove every blank cell in lst
    str1 = str(lst.pop(0)) #assign into str1 the first object in lst, and remove it from lst
    for i in range(0,len(lst)-1,2): #iterate through every 2 cells in lst
        if(lst[i] == "*"): #if the operator is *
            str1 *= int(lst[i+1]) #mupltiply str1 the amount of times in lst[i+1]
        elif(lst[i] == "+"): #if the operator is +
            str1 += lst[i+1] #add to str the string in lst[i+1]
    return str1 #at the end of iterations, return the final string str1
    
    
    

########
# Tester
########

def test():
    #testing Q4
    if num_different_letters("aa bb cccc dd ee fghijklmnopqrstuvwxyz") != 26:
        print("error in num_different_letters - 1")
    if num_different_letters("aaa98765432100000000") != 1:
        print("error in num_different_letters - 2")

    if replace_char("abcdabcde", "a", "x") != "xbcdxbcde":
        print("error in replace_char - 1")
    if replace_char("abcd123", "1", "x") != "abcdx23":
        print("error in replace_char - 2")
        
    if longest_word("a bb ccc 4444 e") != 4:
        print("error in longest_word - 1")
    if longest_word("a bb ccc 4444 eeeee fffff") != 5:
        print("error in longest_word - 2")

    if to_upper("abc") != "ABC":
        print("error in to_upper - 1")
    if to_upper("123") != "123":
        print("error in to_upper - 2")

    #testing Q5
    if calc("'123321'*'2'") != "123321123321":
        print("error in calc - 1")
    if calc("'Hi there '*'3'+'you2'") != "Hi there Hi there Hi there you2":
        print("error in calc - 2")
    if calc("'hi+fi'*'2'*'2'") != "hi+fihi+fihi+fihi+fi":
        print("error in calc - 3")
    if calc("'a'*'2'+'b'*'2'") != "aabaab":
        print("error in calc - 4")

