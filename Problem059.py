# XOR operator
def xor(x,  y):
    return x ^ y


# Finding the most common element in a list
def most_common(lst):
    return max(set(lst), key=lst.count)


# Finding the cipher key when the length k is known and the words
# can be assumed to be separated by spaces
def get_cypher(text, k):
    return ''.join([str(chr(xor(ord(' '), most_common(text[i::k])))) for i in range(k)])


# Just for fun, decypher a text given key length k
def decypher(text, k):
    key = get_cypher(text, k)
    return ''.join([str(chr(xor(text[i], ord(key[i % k])))) for i in range(len(text))])


# Finding the sum of the ASCII values of a text
def sum_ascii(text):
    return sum([ord(i) for i in text])


with open('p059_cipher.txt') as f:
    cipher = f.read()
codes = [int(c) for c in cipher.split(',')]
print(sum_ascii(decypher(codes, 3)))
