from math import factorial, pow, exp
from scipy.special import comb
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import random
from tqdm import tqdm


def subscript_func(q, n):
    return pow(q / (1-q), n)


def nakamoto(q, n):
    p = 1-q
    l = n * (q / p)
    s = sum([exp(-l) * pow(l, k) * (1 - subscript_func(q, n-k)) / factorial(k) for k in range(n)])
    return 1 - s


def grunspan(q, n):
    p = 1-q
    s = sum([(pow(p, n) * pow(q, k) - pow(q, n) * pow(p, k)) * comb(k + n - 1, k) for k in range(n)])
    return 1 - s


def double_spending_attack(q, n, rounds=1000):
    legit = 0
    adversary = 0
    for _ in range(rounds):
        if random.random() < q:
            adversary += 1
        else:
            legit += 1
        if legit < n:
            continue
        if adversary >= legit:
            return True
    return False


def dsa_monte_carlo(q, n, it=10000):
    result = 0
    for _ in range(it):
        result += double_spending_attack(q, n)
    return result / it
        
        
def find_best_n(q, variant, prob):
    n = 1
    while variant(q, n) >= prob:
        n += 1
    return n

    
def get_df_compare_n(variant, n_arr, q_arr):
    return pd.DataFrame([[n, q, variant(q, n)] for q, n in itertools.product(q_arr, n_arr)], columns=['n', 'q', 'prob'])


def get_df_find_n(variant, probs, q_arr):
    return pd.DataFrame([[find_best_n(q, variant, prob), q, prob] for q, prob in itertools.product(q_arr, probs)], columns=['n', 'q', 'prob'])


def compare_for_n():
    n_arr = [1, 3, 6, 12, 24, 48]
    q_arr = [i / 100 for i in range(50)]
    
    df_nakamoto = get_df_compare_n(nakamoto, n_arr, q_arr)
    df_grunspan = get_df_compare_n(grunspan, n_arr, q_arr)
    df_mc = get_df_compare_n(dsa_monte_carlo, n_arr, q_arr)
    
    for n in n_arr:
        nakamoto_data = df_nakamoto.loc[df_nakamoto['n'] == n]
        grunspan_data = df_grunspan.loc[df_grunspan['n'] == n]
        mc_data = df_mc.loc[df_mc['n'] == n]
    
        plt.title(f"n = {n}")
        plt.xlabel("q")
        plt.ylabel("P(n,q)")
        plt.scatter(nakamoto_data['q'], nakamoto_data['prob'], label='Nakamoto', s=10)
        plt.scatter(grunspan_data['q'], grunspan_data['prob'], label='Grunspan', s=10)
        plt.scatter(mc_data['q'], mc_data['prob'], label='Monte Carlo', s=10)
        plt.legend(loc="best")
        plt.savefig(f"ex1/n={n}.png")
        plt.clf()


def fit_right_n():
    probs = [0.1, 0.01, 0.001]
    q_arr = [i / 100 for i in range(43)]
    
    df_nakamoto = get_df_find_n(nakamoto, probs, q_arr)
    df_grunspan = get_df_find_n(grunspan, probs, q_arr)
    
    for prob in probs:
        nakamoto_data = df_nakamoto.loc[df_nakamoto['prob'] == prob]
        grunspan_data = df_grunspan.loc[df_grunspan['prob'] == prob]
    
        plt.title(f"P(n,q) = {prob}")
        plt.xlabel("q")
        plt.ylabel("n")
        plt.scatter(nakamoto_data['q'], nakamoto_data['n'], label='Nakamoto', s=10)
        plt.scatter(grunspan_data['q'], grunspan_data['n'], label='Grunspan', s=10)
        plt.legend(loc="best")
        plt.savefig(f"ex2/P={prob}.png")
        plt.clf()
        

compare_for_n()
fit_right_n()