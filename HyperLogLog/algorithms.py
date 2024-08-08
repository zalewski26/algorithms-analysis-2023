from struct import unpack
from math import log


def min_count(multiset, hash_func, k):
    M = [1] * k
    for item in multiset:
        hash_item = get_hash(hash_func, item) / 2**32
        if hash_item < M[k-1] and hash_item not in M:
            M[k-1] = hash_item
            M.sort()
    if M[k-1] == 1:
        return sum(1 for i in M if i != 1)
    return (k-1)/M[k-1]

def hyperloglog(multiset, hash_func, b, alpha):
    m = 2**b
    R = [0] * m
    for item in multiset:
        hash_item = get_hash(hash_func, item)
        rest = hash_item >> b
        reg_id = hash_item ^ (rest << b)
        R[reg_id] = max(R[reg_id], leftmost_one_index(rest, 32-b))
    mean = 0
    for i in range(m):
        mean += 2**(-R[i])
    result = alpha*(m**2)/mean
    if result <= 2.5 * m:
        zero_regs = sum([1 for r in R if r == 0])
        if (zero_regs != 0):
            result = m * log(float(m) / zero_regs)
    elif result > (1/30) * 2**32:
        result = -2**32 * log(1-(float(result)/(2**32)))
    return result


def leftmost_one_index(number, size):
    binary_str = bin(number)[2:].zfill(size)
    try:
        return binary_str.index('1') + 1
    except:
        return size + 1


def get_hash(h, m):
    b = m.encode(encoding="utf-8")
    return unpack('L', h(b).digest()[:8])[0] >> 32

