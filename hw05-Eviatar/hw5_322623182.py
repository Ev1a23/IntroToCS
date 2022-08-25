# Skeleton file for HW5 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw5_ID.py).

import random
import math

##############
# QUESTION 2 #
##############

 
def is_sorted(lst):
    ''' returns True if lst is sorted, and False otherwise '''
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True


def modpower(a, b, c):
    ''' computes a**b modulo c, using iterated squaring '''
    result = 1
    while b > 0:  # while b is nonzero
        if b % 2 == 1:  # b is odd
            result = (result * a) % c
        a = (a * a) % c
        b = b // 2
    return result


def is_prime(m):
    ''' probabilistic test for m's compositeness '''''
    for i in range(0, 100):
        a = random.randint(1, m - 1)  # a is a random integer in [1...m-1]
        if modpower(a, m - 1, m) != 1:
            return False
    return True


class FactoredInteger:

    def __init__(self, factors, verify=True):
        ''' Represents an integer by its prime factorization '''
        if verify:
            assert is_sorted(factors)
        number = 1
        for p in factors:
            if verify:
                assert (is_prime(p))
            number *= p
        self.number = number
        self.factors = factors

    # 2b
    def __repr__(self):
        '''
        Represent a Factored Integer object
        Time complexity: O(k), k = len(self.factors)
        '''
        if len(self.factors) == 0: #if the number is 1(one has no prime factors)
            return "<1:>"
        str1 = "<"
        str1+= str(self.number) +":"
        for i in range(len(self.factors)-1):
            str1+= str(self.factors[i])+"*"
        str1+=str(self.factors[-1]) +">"
        return str1

    def __eq__(self, other):
        '''
        Define how to check if 2 FactoredInteger Objects are equal
        Time complexity: O(1)
        '''
        return self.number == other.number #equality of 2 Factored integer is determined if the number itself is equal because the list of factors is unique to each number
    def __mul__(self,other):
        '''
        Define how to multiply 2 FactoredInteger Objects
        Time complexity: O(k+m), k = len(self.factors), m = len(self.factors)
        '''
        if len(self.factors) == 0: #self == 1
            return FactoredInteger(other.factors,False)
        if len(other.factors) == 0: #other == 1
            return FactoredInteger(self.factors,False)
        i,j = 0,0
        merged = []
        for k in range(len(self.factors)+len(other.factors)): #iterate simultanousley through self.factors and other.factors
            if(self.factors[i]<=other.factors[j]):
                merged.append(self.factors[i])
                i+=1
                if i>=len(self.factors): #we finished iterating through each of self.factors objects
                    merged +=other.factors[j:] #need to add to merged the rest of other.factors
                    break
            else:
                merged.append(other.factors[j])
                j+=1
                if j>=len(other.factors): #we finished iterating through each of other.factors objects
                    merged +=self.factors[i:] #need to add to merged the rest of self.factors
                    break
        return FactoredInteger(merged,False)


    def __pow__(self, other):
        '''
        We can add each factor in self x times to lst, and x is other.number
        Time complexity: O(k*other.number), k = len(self.factors)
        '''
        lst = []
        for num in self.factors:
            for r in range(other.number):
                lst.append(num)
        return FactoredInteger(lst,False)
        
        

    # 2c
    def gcd(self, other):
        '''
        Eucled's method isn't answering the time complexity requirements
        Furthermore, we already have the factors of each number
        We will iterate simoultanousley through both of factors list
        if the current factors in both of the list is equal, we will add it to lst, and add 1 to each of the pointers
        Otherwise, we will add 1 to the pointer of the smallest factor
        This way, we match to the question time complexity requirements: O(n+m) n = len of self.factors, m = len of other.factors
        '''
        lst = []
        i,j = 0,0
        while i <len(other.factors) and j<len(self.factors): 
            if self.factors[j] == other.factors[i]:
                lst.append(self.factors[j])
                i+=1
                j+=1
            elif self.factors[j] > other.factors[i]:
                i+=1
            else:
                j+=1
        return FactoredInteger(lst,False)
                
    # 2d
    def lcm(self, others):
        my_set = set()
        lists = [self.factors] + [x.factors for x in others]
        f_i_d = [{f: 0 for f in x} for x in lists]
        for i in range(len(lists)):
            for f in lists[i]:
                my_set.add(f)
                f_i_d[i][f] += 1
        f_m_d = {x: 0 for x in my_set}
        for f_d in f_i_d:
            for f in f_d.keys():
                if f_d[f] > f_m_d[f]:
                    f_m_d[f] = f_d[f]
        result = []
        for k, v in f_m_d.items():
            result += [k] * v
        return FactoredInteger(result, verify=False)


##############
# QUESTION 3 #
##############

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = math.sqrt(x ** 2 + y ** 2)
        self.theta = math.atan2(y, x)
        if self.theta < 0:
            self.theta += 2 * math.pi

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    # 3a_i
    def angle_between_points(self, other):
        '''
        Return the angle between 2 points
        Time complexity: O(1)
        '''
        if self.theta == other.theta:
            return 0
        elif self.theta<other.theta:
            return other.theta-self.theta
        return 2*math.pi +other.theta-self.theta

def merge(A,B):
    ''' merging two lists into a sorted list
    A and B must be sorted!
    Time complexity: O(n+m)
    '''
    n = len(A)
    m = len(B)
    C = [None for i in range(n+m)]

    a=0; b=0; c=0
    while  a<n  and  b<m: #more element in both A and B
        if A[a].theta < B[b].theta:
            C[c] = A[a]
            a+=1
        else:
            C[c] = B[b]
            b+=1
        c+=1

    C[c:] = A[a:] + B[b:] #append remaining elements (one of those is empty)

    return C
def mergesort(lst):
    ''' recursive mergesort '''
    n = len(lst)
    if n<=1: 
        return lst
    else:            #two recursive calls, then merge
        return merge(mergesort(lst[0:n//2]),mergesort(lst[n//2:n]))

def find_optimal_angle(trees, alpha):
    '''
    Find the angle in which in our eyesight, we will see max number of trees.
    We will generate 2 pointers to our list and check the angle between them until the first pointer finished checking all of the trees
    We will count the steps we made and if the current count is bigger than the current max, we will make the current counter the max
    Will return the optimal angle to see the max trees in our alpha eyesight
    Time complexity: O(nlogn)
    '''
    if len(trees) == 0:
        return 0
    if(len(trees)) == 1:
        return trees[0].theta
    lst = mergesort(trees) #O(nlogn)
    max_t = 0 #max trees
    optimal = lst[0].theta
    i = 0 #current index
    j = 1 #next index
    cnt = 1 #count how many trees on the current check
    loop =False
    while (i!= len(lst)):
        if i == j:
            if loop == False:
                j+=1
                cnt = 1
            else:
                optimal = lst[i].theta
                return optimal
        if j == len(lst):
            loop = True
            j=0
        angle = lst[i].angle_between_points(lst[j])
        if angle<=alpha:
            cnt+=1
            j+=1
        else:
            if cnt> max_t:
                optimal = lst[i].theta
                max_t = cnt
            i+=1
            cnt = j-i
    return optimal
    
    if cnt>max_t:
        optimal = angle
    return optimal
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        # return str(self.value)
        # This shows pointers as well for educational purposes:
        return "(" + str(self.value) + ", next: " + str(id(self.next)) + ")"


class Linked_list:
    def __init__(self, seq=None):
        self.head = None
        self.len = 0
        if seq != None:
            for x in seq[::-1]:
                self.add_at_start(x)

    def __repr__(self):
        out = ""
        p = self.head
        while p != None:
            out += str(p) + ", "  # str(p) invokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"

    def __len__(self):
        ''' called when using Python's len() '''
        return self.len

    def add_at_start(self, val):
        ''' add node with value val at the list head '''
        tmp = self.head
        self.head = Node(val)
        self.head.next = tmp
        self.len += 1

    def find(self, val):
        ''' find (first) node with value val in list '''
        p = self.head
        # loc = 0     # in case we want to return the location
        while p != None:
            if p.value == val:
                return p
            else:
                p = p.next
                # loc=loc+1   # in case we want to return the location
        return None

    def __getitem__(self, loc):
        ''' called when using L[i] for reading
            return node at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        p = self.head
        for i in range(0, loc):
            p = p.next
        return p

    def __setitem__(self, loc, val):
        ''' called when using L[loc]=val for writing
            assigns val to node at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        p = self.head
        for i in range(0, loc):
            p = p.next
        p.value = val
        return None

    def insert(self, loc, val):
        ''' add node with value val after location 0<=loc<len of the list '''
        assert 0 <= loc <= len(self)
        if loc == 0:
            self.add_at_start(val)
        else:
            p = self.head
            for i in range(0, loc - 1):
                p = p.next
            tmp = p.next
            p.next = Node(val)
            p.next.next = tmp
            self.len += 1

    def delete(self, loc):
        ''' delete element at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        if loc == 0:
            self.head = self.head.next
        else:
            p = self.head
            for i in range(0, loc - 1):
                p = p.next
            # p is the element BEFORE loc
            p.next = p.next.next
        self.len -= 1


class Segment:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    def intersecting(self, other):
        if (self.point1.x - self.point2.x) == 0:
            return False
        if (other.point1.x - other.point2.x) == 0:
            return False
        self_incline = (self.point1.y - self.point2.y) / (self.point1.x - self.point2.x)
        other_incline = (other.point1.y - other.point2.y) / (other.point1.x - other.point2.x)
        self_b = self.point1.y - self_incline * self.point1.x
        other_b = other.point1.y - other_incline * other.point1.x
        if (self_incline - other_incline) == 0:
            return False
        intersecting_x = (other_b - self_b) / (self_incline - other_incline)
        if ((intersecting_x <= max(min(self.point1.x, self.point2.x), min(other.point1.x, other.point2.x))) or
                (intersecting_x >= min(max(self.point1.x, self.point2.x), max(other.point1.x, other.point2.x)))):
            return False
        else:
            return True


# for 3b_ii
def calculate_angle(p1, p2, p3):
    ang = math.degrees(math.atan2(p3.y - p2.y, p3.x - p2.x) - math.atan2(p1.y - p2.y, p1.x - p2.x))
    return ang + 360 if ang < 0 else ang


class Polygon:
    def __init__(self, llist):
        self.points_list = llist
        self.point_head = llist.head

    # 3b_ii
    def edges(self):
        '''
        The list of points is a linked list. We will calculate all the angles from second point until the one before the last one
        Then, we will calculate the last one
        Lastly, we will calculate the first one, using the pointer of the last point
        Time Complexity: O(n)
        '''
        lst = []
        prev = self.point_head #loc 0
        cur = self.point_head.next
        while cur.next != None:
            angle = calculate_angle(prev.value,cur.value,cur.next.value)
            if angle>180:
                angle= 360-angle
            lst.append(angle)
            prev = cur
            cur = cur.next
        angle = calculate_angle(prev.value,cur.value,self.point_head.value)
        if angle>180:
            angle = 360-angle
        lst.append(angle)
        angle = calculate_angle(cur.value,self.point_head.value,self.point_head.next.value)
        if angle >180:
            angle = 360-angle
        lst.insert(0,angle) #O(n)
        return lst

            

    # 3b_iii
    def simple(self):
        '''
        We will determine if the poligon is simple
        For doing so, we will check for each 2 pairs of segments if they are intersecting
        If all of them aren't, we can determine the polygon is simple
        Time complexity: O(n^2)
        '''
        prev = self.point_head
        cur = self.point_head.next
        lst = []
        while cur!= None:
            lst.append(Segment(prev.value,cur.value))
            prev = cur
            cur = cur.next
        lst.append(Segment(prev.value,self.point_head.value))
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if lst[i].intersecting(lst[j]):
                    return False
        return True

##############
# QUESTION 4 #
##############

def printree(t, bykey=True):
    '''Print a textual representation of t
    bykey=True: show keys instead of values'''
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    '''Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values'''
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    '''Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings'''

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    '''helper for conc'''
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    '''helper for conc'''
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class Binary_search_tree():

    def __init__(self):
        self.root = None

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    def inorder(self):
        result = []

        def inorder_rec(root):
            if root:
                inorder_rec(root.left)
                result.append((root.key, root.val))
                inorder_rec(root.right)

        inorder_rec(self.root)
        return result

    def lookup(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root == None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)


    # 4a
    def diam(self):
        '''
        We will call recursively each left and right of the current node
        for each left, right, we will calculate the depth of it, and the diameter of this node
        Then, we will return a tuple of 2 elements, 1 is the maximum between left diameter, right diameter and the left depth + right depth +1, and the maximum +1 between left depth and right depth
        Time complexity: O(n)
        '''
        def diam_rec(tree):
            if tree==None:
                return 0,0
            l_diam,l_depth = diam_rec(tree.left)
            r_diam,r_depth = diam_rec(tree.right)
            return (max(l_diam,r_diam,l_depth+r_depth+1),max(l_depth,r_depth)+1)
        if self.root == None:
            return 0
        check = diam_rec(self.root)
        return max(check[0],check[1])

    # 4b
    def cumsum(self):
        '''
        We will call recursively left, with a key variable.
        If the left call added anything to key, we will change the value of tree.key to left + current value.
        With the new value of tree.key, we will call the right side of tree.
        Time complexity: O(n)
        '''
        def cumsum_rec(tree,key):
            if tree== None:
                return key
            left = cumsum_rec(tree.left,key)
            if tree.key != left:
                tree.key = left + tree.key
            right = cumsum_rec(tree.right,tree.key)
            return right
            
        if self.root == None:
            return None
        cumsum_rec(self.root,"")
        return None


############
# QUESTION 5
############

# 5a
def prefix_suffix_overlap(lst, k):
    '''
    We will iterate through the list.
    Then, we will check if reisha of length k of string i equals the seifa or length k of string j, and check
    if i!=j, we aren't intrested in strings that there reisha equals their seifa.
    Time complexity: O(n^2 * k)
    '''
    output = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i!=j:
                if lst[i][:k] == lst[j][-k:]:
                    output.append((i,j))
    return output


# 5c
class Dict:
    def __init__(self, m, hash_func=hash):
        ''' initial hash table, m empty entries '''
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        ''' insert key,value into table
            Allow repetitions of keys '''
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):
        ''' returns ALL values of key as a list, empty list if none
        We find which table our key should be, according to the hash function
        Then, we will check for each item in the list, if its key is equal to our key
        If so, we will add it's value to our list
        Time complexity: O(k) when k is the length of the list we should check according to our hash function
        '''
        lst = []
        i = self.hash_mod(key)
        for j in range (len(self.table[i])):
            if self.table[i][j][0] == key:
                lst.append(self.table[i][j][1])
        return lst


# 5d
def prefix_suffix_overlap_hash1(lst, k):
    '''
    We will use Dict class of q5c
    We will insert to the Dict each of reisha's with length k
    After that, we will check for each seifa with length k if there is a matching seifa for it in the Dict. If so,we will check if the index of both is differnt.
    If so, we will insert it to the output list
    Time complexity: O(n*k)
    '''
    output = []
    dic = Dict(len(lst))
    for i in range(len(lst)):
        dic.insert(lst[i][:k],i)
    for i in range(len(lst)):
        check = dic.find(lst[i][-k:])
        for t in check:
            if i != t:
                output.append((t,i))
    return output
        


##########
# TESTER #
##########

def test():
    ##############
    # QUESTION 2 #
    #   TESTER   #
    ##############

    # 2b
    n1 = FactoredInteger([2, 3])  # n1.number = 6
    n2 = FactoredInteger([2, 5])  # n2.number = 10
    n3 = FactoredInteger([2, 2, 3, 5])  # n3.number = 60
    if str(n3) != "<60:2*2*3*5>":
        print("2b - error in __repr__")
    if n1 != FactoredInteger([2, 3]):
        print("2b - error in __eq__")
    if n1 * n2 != n3:
        print("2b - error in __mult__")
    if n1 ** n2 != FactoredInteger([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]):
        print("2b - error in __pow__")

    # 2c
    n4 = FactoredInteger([2, 2, 3])  # n4.number = 12
    n5 = FactoredInteger([2, 2, 2])  # n5.number = 8
    n6 = FactoredInteger([2, 2])  # n6.number = 4
    if n4.gcd(n5) != n6:
        print("2c - error in gcd")

    n7 = FactoredInteger([2, 3])  # n7.number = 6
    n8 = FactoredInteger([5, 7])  # n8.number = 35
    n9 = FactoredInteger([])  # represents 1
    if n7.gcd(n8) != n9:
        print("2c - error in gcd")

    ##############
    # QUESTION 3 #
    #   TESTER   #
    ##############

    # 3a
    p1 = Point(1, 1)  # theta = pi / 4
    p2 = Point(0, 3)  # theta = pi / 2
    if Point.angle_between_points(p1, p2) != 0.25 * math.pi or \
            Point.angle_between_points(p2, p1) != 1.75 * math.pi:
        print("3a_i - error in angle_between_points")

    trees = [Point(2, 1), Point(-1, 1), Point(-1, -1), Point(0, 3), Point(0, -5), Point(-1, 3)]
    if find_optimal_angle(trees, 0.25 * math.pi) != 0.5 * math.pi:
        print("3a_ii - error in find_optimal_angle")

    # 3b
    def test_angles(target, output):
        if len(target) != len(output):
            print("3a_ii - error in Polygon.edges")
        for i in range(len(target)):
            if abs(target[i] - output[i]) >= 0.1:  # dealing with floats
                print("3a_ii - error in Polygon.edges")

    parallelogram = Polygon(Linked_list([Point(1, 1), Point(4, 4), Point(8, 4),Point(5, 1)]))
    test_angles(parallelogram.edges(), [45.0, 135.0, 45.0, 135.0])
    other_poly = Polygon(Linked_list([Point(1, 1), Point(1, 3), Point(2, 3), Point(3, 1)]))
    test_angles(other_poly.edges(), [90.0, 90.0, 116.5, 63.4])
    not_simple = Polygon(Linked_list([Point(1, 1),Point(8, 4),Point(4, 4),Point(5, 1)]))

    if not_simple.simple():
        print("3a_iii - error in Polygon.simple")
    if not parallelogram.simple():
        print("3a_iii - error in Polygon.simple")
    if not other_poly.simple():
        print("3a_iii - error in Polygon.simple")

    ##############
    # QUESTION 4 #
    #   TESTER   #
    ##############

  

    # 4a
    t2 = Binary_search_tree()
    t2.insert('c', 10)
    t2.insert('a', 10)
    t2.insert('b', 10)
    t2.insert('g', 10)
    t2.insert('e', 10)
    t2.insert('d', 10)
    t2.insert('f', 10)
    t2.insert('h', 10)
    if t2.diam() != 6:
        print("4a - error in diam")

    t3 = Binary_search_tree()
    t3.insert('c', 1)
    t3.insert('g', 3)
    t3.insert('e', 5)
    t3.insert('d', 7)
    t3.insert('f', 8)
    t3.insert('h', 6)
    t3.insert('z', 6)
    if t3.diam() != 5:
        print("4a - error in diam")

    # 4b
    t3.cumsum()
    if str(t3.inorder()) != "[('c', 1), ('cd', 7), ('cde', 5), ('cdef', 8), ('cdefg', 3), ('cdefgh', 6), ('cdefghz', 6)]":
        print("4b - error in cumsum")
    t2.cumsum()
    if str(t2.inorder()) != "[('a', 10), ('ab', 10), ('abc', 10), ('abcd', 10), ('abcde', 10), ('abcdef', 10), ('abcdefg', 10), ('abcdefgh', 10)]":
        print("4b - error in cumsum")

    ##############
    # QUESTION 5 #
    #   TESTER   #
    ##############
    # 5a
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("error in prefix_suffix_overlap")

    # 5c
    d = Dict(3)
    d.insert("a", 56)
    d.insert("a", 34)
    if sorted(d.find("a")) != sorted([56, 34]) or d.find("b") != []:
        print("error in Dict.find")

    # 5d
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap_hash1(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("error in prefix_suffix_overlap_hash1")
