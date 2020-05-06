def _string_hash(word):
    # A variable-length version of Python's builtin hash
    if word == "":
        return 0
    else:
        x = ord(word[0]) << 7
        print(x)
        m = 1000003
        mask = 2 ** 128 - 1
        for c in word:
            x = ((x * m) ^ ord(c)) & mask
        x ^= len(word)
        if x == -1:
            x = -2
        print(x)
        print(str(bin(x)))
        print(len(str(bin(x))))


def hamming_distance(hash1, hash2):
    x = (hash1 ^ hash2) & ((1 << 128) - 1)
    tot = 0
    while x:
        tot += 1
        x &= x-1
    return tot


print(bin(2305915360917275473), bin(2377943372515183779))
print(len(bin(2305915360917275473)), len(bin(2377943372515183779)))
print(hamming_distance(2305915360917275473, 2377943372515183779))


_string_hash('微博')
_string_hash('博客')
_string_hash('北京')
