import hashlib
from algorithms import min_count, hyperloglog
import matplotlib.pyplot as plt
from tqdm import tqdm
from pathlib import Path

# alpha: (m*(integral (log2((2+u)/(1+u)))^m from 0 to inf))^(-1)
alpha = {
    3  : 0.62560871093725783198500641115,
    4  : 0.67310202386766599233548265739,
    5  : 0.69712263380102416804875375530,
    6  : 0.70920845287002329682833053248,
    7  : 0.71527118996133942147695553096,
    8  : 0.71830763819181383227618018595,
    9  : 0.71982714782040011202713737966,
    10 : 0.72058722597645269495707971678,
    11 : 0.72096734613621909810824869710,
    12 : 0.72115742651737845487667069838
}


def main():
    compare()
    # min_vs_hyper()


# 32k = 5 * 2^b  =>    k = 5/32 * 2^b
def min_vs_hyper():
    length = 10000
    S = [[] for _ in range(length)]
    hash_func = hashlib.sha1
    b = [5, 6, 7, 8]
    k = [5, 10, 20, 40]
    results_min = [[] for _ in range(len(b))]
    results_hyper = [[] for _ in range(len(b))]
    
    cnt = 1
    temp = 1
    while (cnt <= length):
        S[cnt-1] = [str(i) for i in range(temp, temp+cnt)]
        temp = temp+cnt
        cnt += 1
    
    for i in tqdm(range(len(b))):
        results_min[i] = [min_count(s, hash_func, k[i]) / len(s) for s in S]
        results_hyper[i] = [hyperloglog(s, hash_func, b[i], alpha[b[i]]) / len(s) for s in S]
    
    result_dir = 'hyper_vs_min'
    Path(result_dir).mkdir(parents=True, exist_ok=True)
    for i in range(len(b)):
        plt.title(f"Hyperloglog vs Min count\nb = {b[i]} k = {k[i]}")
        plt.xlabel("n")
        plt.ylabel("n^/n")
        plt.scatter(range(1, length+1), results_min[i], label=f"min_count", s=10)
        plt.scatter(range(1, length+1), results_hyper[i], label=f"hyperloglog", s=10)
        plt.legend(loc="best")
        plt.savefig(f"{result_dir}/b={b[i]}_k={k[i]}.png")
        plt.clf()

def compare():
    length = 10000
    S = [[] for _ in range(length)]
    hash_func = hashlib.blake2s
    b = range(4, 12+1)
    results = [[] for _ in range(len(b))]
    
    cnt = 1
    temp = 1
    while (cnt <= length):
        S[cnt-1] = [str(i) for i in range(temp, temp+cnt)]
        temp = temp+cnt
        cnt += 1
    
    for i in tqdm(range(len(b))):
        results[i] = [hyperloglog(s, hash_func, b[i], alpha[b[i]]) / len(s) for s in S]
    
    result_dir = 'compare_blake2s'
    Path(result_dir).mkdir(parents=True, exist_ok=True)
    for i in range(len(b)):
        plt.title(f"Hyperloglog, b = {b[i]}")
        plt.xlabel("n")
        plt.ylabel("n^/n")
        plt.scatter(range(1, length+1), results[i], color='gray', label=f"b = {b[i]}", s=10)
        plt.savefig(f"{result_dir}/b={b[i]}.png")
        plt.clf()
    plt.title("Hyperloglog")
    plt.xlabel("n")
    plt.ylabel("n^/n")
    for i in range(len(b)):
        plt.scatter(range(1, length+1), results[i], label=f"b = {b[i]}", s=10)
    plt.legend(loc="best")
    plt.savefig(f"{result_dir}/all.png")
    plt.clf()


if __name__ == '__main__':
    main()
    
    
    
# b = 6 => m = 64 każdy po 5 bitów
# k po 32 bity

# 32k = 5 * 2^b
# k = 10