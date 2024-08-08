import numpy as np
import matplotlib.pyplot as plt
import hashlib

def min_count(multiset, hash_func, k):
    M = [1 for _ in range(k)]
    for s in multiset:
        temp_hash = hash_func(s)
        if (temp_hash < M[k-1] and temp_hash not in M):
            M[k-1] = temp_hash
            M.sort()
    if (M[k-1] == 1):
        return sum([1 for i in range(k) if M[i] != 1])
    return (k-1)/M[k-1] 


def ex5():
    length = 1000
    S = [[] for _ in range(length)]
    k = [2, 3, 10, 100, 400]
    results = [[] for _ in range(len(k))]
    # hash_func = lambda x: zlib.crc32(bytes(x, encoding='utf-8')) / 2**32
    # hash_func = lambda x: int(hashlib.sha256(bytes(x, encoding='utf-8')).hexdigest()[:8], 16) / 2**32
    hash_func = lambda x: int(hashlib.sha1(bytes(x, encoding='utf-8')).hexdigest()[:8], 16) / 2**32
    # hash_func = lambda x: int(hashlib.shake_128(bytes(x, encoding='utf-8')).hexdigest(1), 16) / 2**8
    # hash_func = lambda x: int(hashlib.shake_128(bytes(x, encoding='utf-8')).hexdigest(2), 16) / 2**16
    
    cnt = 1
    temp = 1
    while (cnt <= length):
        S[cnt-1] = [str(i) for i in range(temp, temp+cnt)]
        temp = temp+cnt
        cnt += 1
    
    for i in range(len(k)):
        results[i] = [min_count(s, hash_func, k[i]) / len(s) for s in S]
    
    for i in range(len(k)):
        plt.title(f"Min Count, k = {k[i]}")
        plt.xlabel("n")
        plt.ylabel("n^/n")
        plt.plot(range(1, length+1), results[i], color='gray', label=f"k = {k[i]}")
        plt.savefig(f"ex5_k={k[i]}.png")
        plt.clf()
    plt.title("Min Count")
    plt.xlabel("n")
    plt.ylabel("n^/n")
    plt.plot(range(1, length+1), results[0], color='gray', label=f"k = {k[0]}")
    plt.plot(range(1, length+1), results[1], color='blue', label=f"k = {k[1]}")
    plt.plot(range(1, length+1), results[2], color='green', label=f"k = {k[2]}")
    plt.plot(range(1, length+1), results[3], color='yellow', label=f"k = {k[3]}")
    plt.plot(range(1, length+1), results[4], color='red', label=f"k = {k[4]}")
    plt.legend(loc="best")
    plt.savefig(f"ex5.png")
    plt.clf()


def ex7():
    length = 10000
    S = [[] for _ in range(length)]
    k = 400
    hash_func = lambda x: int(hashlib.sha1(bytes(x, encoding='utf-8')).hexdigest()[:8], 16) / 2**32
    alphas = [0.05, 0.01, 0.005]
    
    cnt = 1
    temp = 1
    while (cnt <= length):
        S[cnt-1] = [str(i) for i in range(temp, temp+cnt)]
        temp = temp+cnt
        cnt += 1
    results = []
    abs_list = []
    for s in S:
        temp_result = min_count(s, hash_func, k) / len(s)
        results.append(temp_result)
        abs_list.append(abs(1 - temp_result))
    abs_list.sort()
    
    for alpha in alphas:
        delta_id = int((1-alpha)*len(abs_list))
        delta = abs_list[delta_id]
        plt.title(f"Zadanie 7, ograniczenia, alpha = {alpha}")
        plt.xlabel("n")
        plt.ylabel("n^/n")
        plt.scatter(range(1, length+1), results, color='blue')
        chebyshev = np.sqrt((length - k + 1) / (length * (k - 2))) / np.sqrt(alpha)
        chernoff = {
            0.005: 0.18274402618408203,
            0.01: 0.1697627380490303,
            0.05: 0.1381368190050125,
        }
        plt.plot(range(1, length+1), [1 - delta for _ in range(length)], linestyle='dashed', color='black', label=f'delta={delta:.3f}')
        plt.plot(range(1, length+1), [1 + delta for _ in range(length)], linestyle='dashed', color='black')
        plt.plot(range(1, length+1), [1 - chernoff[alpha] for _ in range(length)], linestyle='dashed', color='green', label=f'chernoff, delta={chernoff[alpha]:.3f}')
        plt.plot(range(1, length+1), [1 + chernoff[alpha] for _ in range(length)], linestyle='dashed', color='green')
        plt.plot(range(1, length+1), [1 - chebyshev for _ in range(length)], linestyle='dashed', color='red', label=f'chebyshev, delta={chebyshev:.3f}')
        plt.plot(range(1, length+1), [1 + chebyshev for _ in range(length)], linestyle='dashed', color='red')
        plt.legend(loc="upper left")
        plt.savefig(f"ex7_{alpha}.png")
        plt.clf()
    

def main():
    # ex5()
    ex7()



if __name__=='__main__':
    main()