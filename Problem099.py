from math import log10


# Convert a string 'a,b' to b * log(a)
def str_base_exp_to_log(be):
    be = be.split(',')
    return int(be[1]) * log10(int(be[0]))


# Finding which line number of a text file has the greatest numerical value
def max_base_exp(be_list):
    be_list = list(map(str_base_exp_to_log, be_list))
    return be_list.index(max(be_list)) + 1


with open('p099_base_exp.txt') as f:
    base_exp_list = f.read()
base_exp_list = base_exp_list.split('\n')
print(max_base_exp(base_exp_list))
