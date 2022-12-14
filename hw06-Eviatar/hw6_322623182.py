# Skeleton file for HW6 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw6_ID.py).
from PIL import Image  # need to install PIL/PILLOW

# Q1b
def sets_concat(s1, s2):
    s = set()
    for x in s1:
        for y in s2:
            s.add(x+y)
    return s


def generate_language(rule_dict, start_var, k):
    mem = dict()
    return generate_language_rec(rule_dict, start_var, k, mem)


def generate_language_rec(rule_dict, var, k, mem):
    if (var, k) in mem:
        return mem[(var, k)]

    s = set()
    if k == 0:
        if "" in rule_dict[var]:
            s.add("")
        mem[(var, k)] = s
        return s

    if k == 1:
        for x in rule_dict[var]:
            if len(x) == 1:
                s.add(x)
        mem[(var, k)] = s
        return s

    for var_rule in rule_dict[var]:
        if len(var_rule) == 2:
            X, Y = var_rule[0], var_rule[1]
            for j in range(1, k):
                 s1 = generate_language_rec(rule_dict,X,j,mem)
                 s2 = generate_language_rec(rule_dict,Y,k-j,mem)
                 s.update(sets_concat(s1,s2))
    mem[(var, k)] = s
    return s

# Q1c
def what(rule_dict, start_var, k):
    mem = dict()
    return what_rec(rule_dict, start_var, k, mem)


def what_rec(rule_dict, var, k, mem):
    if (var, k) in mem:
        return mem[(var, k)]

    cnt = 0
    if k == 0:
        if "" in rule_dict[var]:
            cnt += 1
        mem[(var, k)] = cnt
        return cnt

    if k == 1:
        for x in rule_dict[var]:
            if len(x) == 1:
                cnt += 1
        mem[(var, k)] = cnt
        return cnt

    for var_rule in rule_dict[var]:
        if len(var_rule) == 2:
            X, Y = var_rule[0], var_rule[1]
            for j in range(1, k):
                cnt += what_rec(rule_dict, X, j, mem) * what_rec(rule_dict, Y, k - j, mem)
    mem[(var, k)] = cnt
    return cnt


# Q2a
def get_next_sum(gen):
    n1 = 0 #to collect sum
    n2 = 1 #to store all numbers gen generates
    while True:
        n2 *= next(gen)
        n1+= 1/n2
        yield n1


# Q2b
def gen_sequence():
    yield 1
    i=1
    while True:
        yield i
        i+=1


# Q6a
def right_left(img):
    w, h = img.size
    mat = img.load()
    new_img = img.copy()
    new_mat = new_img.load()
    for x in range(w):
        for y in range(h):
            new_mat[x,y] = mat[w-x-1,y]
    return new_img


# Q6b
def what2(img):
    w, h = img.size
    mat = img.load()
    new_img = img.copy()
    new_mat = new_img.load()
    for y in range(h):
        lst = []
        for x in range(w):
            lst.append(new_mat[x,y])
        lst.sort()
        for x in range(w):
            new_mat[x,y] = lst[x]
    new_img.show()
    return new_img

############
#  TESTER  #
############
def test():
    # Q1b
    rule_dict = {"S": {"AB", "BC"}, "A": {"BA", "a"}, "B": {"CC", "b"}, "C": {"AB", "a"}}
    res = generate_language(rule_dict, "S", 5)
    if ("baaba" not in res) or ("baab" in res) or ("babab" in res):
        print("Error in Q1b - generate_language")

    # Q2
    import math
    gen1 = gen_sequence()
    gen2 = get_next_sum(gen1)
    for i in range(20):
        next(gen2)
    if abs(math.e - next(gen2)) > 0.00001:
        print("Error in Q2 - get_next_sum or gen_sequence")

