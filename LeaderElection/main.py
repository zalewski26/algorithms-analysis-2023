from math import ceil, log2
from random import random
from tqdm import tqdm
import matplotlib.pyplot as plt
import statistics


def second_scenario(num_of_nodes):
    time = 0
    threshold = 1 / num_of_nodes
    count = 0
    while (count != 1):
        count = 0
        time += 1
        for _ in range(num_of_nodes):
            if random() < threshold:
                count += 1
    return time


def third_scenario(num_of_nodes, upper_bound):
    time = 0
    count = 0
    round_slots = ceil(log2(upper_bound))+1
    while (count != 1):
        count = 0
        for _ in range(num_of_nodes):
            if random() < 1/2**(time % round_slots + 1):
                count += 1
        time += 1
    return time


def second_simulation(n, iterations, output=None):
    results = []
    for _ in tqdm(range(iterations), desc=f"Scenario 2, n={n}", disable=not output):
        results.append(second_scenario(n))
    
    if output:
        plt.title(f'Scenario 2\nn={n}')
        plt.xlabel('Number of slots')
        plt.ylabel('Frequency')
        plt.hist(x=results, bins=range(1, max(results)), alpha=0.7, ec='black')
        plt.savefig(output)
        plt.clf()
    
    return statistics.mean(results), statistics.variance(results)


def third_simulation(n, u, iterations, output=None):
    results = []
    for _ in tqdm(range(iterations), desc=f"Scenario 3, n={n}, u={u}", disable=not output):
        results.append(third_scenario(n, u))

    round_slots = ceil(log2(u))+1
    if output:
        plt.title(f'Scenario 3\nn={n}, u={u}')
        plt.xlabel('Number of slots')
        plt.ylabel('Frequency')
        plt.hist(x=results, bins=range(1, max(results)), alpha=0.7, ec='black')
        for i in range(max(results) // round_slots):
            plt.axvline(i*round_slots + 1, linestyle='dashed', color='black', linewidth=0.5)
        plt.savefig(output)
        plt.clf()
    
    return len([i for i in results if i <= round_slots]) / len(results)


def ex2():
    n=1000
    iterations=1000
    
    second_simulation(n, iterations, 'ex2_sec.png')
    third_simulation(2, n, iterations, 'ex2_third_2.png')
    third_simulation(n//2, n, iterations, 'ex2_third_half.png')
    third_simulation(n, n, iterations, 'ex2_third_u.png')


def ex3():
    expected, variance, count = 0, 0, 0
    exp_dict, var_dict = {}, {}
    for n in tqdm(range(100, 3000, 100), desc="Estimation for scenario 2"):
        temp_expected, temp_variance = second_simulation(n, 1000)
        expected += temp_expected
        variance += temp_variance
        count +=1
        exp_dict[n] = temp_expected
        var_dict[n] = temp_variance
    expected = expected / count
    variance = variance / count
    
    plt.title(f'Scenario 2 estimation\nE[L] \u2248 {expected:.4f}, Var[L] \u2248 {variance:.4f}')
    plt.xlabel('n')
    plt.ylabel('Value')
    plt.plot(exp_dict.keys(), exp_dict.values(), color='green', label='Expected')
    plt.plot(var_dict.keys(), var_dict.values(), color='blue', label='Variance')
    plt.axhline(expected, linestyle='dashed', color='green', linewidth=0.5)
    plt.axhline(variance, linestyle='dashed', color='blue', linewidth=0.5)
    plt.legend(loc="best")
    plt.savefig("ex3.png")
    plt.clf()


def ex4():
    prob_2, prob_half, prob_u, count = 0, 0, 0, 0
    prob_2_dict, prob_half_dict, prob_u_dict = {}, {}, {}
    for u in tqdm(range(100, 1000, 50), desc="Estimation for scenario 3"):
        temp_prob_2 = third_simulation(2, u, 1000)
        temp_prob_half = third_simulation(u//2, u, 1000)
        temp_prob_u = third_simulation(u, u, 1000)
        prob_2 += temp_prob_2
        prob_half += temp_prob_half
        prob_u += temp_prob_u
        count += 1
        prob_2_dict[u] = temp_prob_2
        prob_half_dict[u] = temp_prob_half
        prob_u_dict[u] = temp_prob_u
    prob = (prob_2 + prob_half + prob_u) / (3 * count)
    
    plt.title(f'Scenario 3 estimation\nPr[S] \u2248 {prob:.4f}')
    plt.xlabel('u')
    plt.ylabel('Value')
    plt.plot(prob_2_dict.keys(), prob_2_dict.values(), color='green', label='n=2')
    plt.plot(prob_half_dict.keys(), prob_half_dict.values(), color='blue', label='n=u/2')
    plt.plot(prob_u_dict.keys(), prob_u_dict.values(), color='red', label='n=u')
    plt.axhline(prob_2/count, linestyle='dashed', color='green', linewidth=0.5)
    plt.axhline(prob_half/count, linestyle='dashed', color='blue', linewidth=0.5)
    plt.axhline(prob_u/count, linestyle='dashed', color='red', linewidth=0.5)
    plt.legend(loc="best")
    plt.savefig("ex4.png")
    plt.clf()
    

# Expected value ≈ 2.7048620689655167
# Variance ≈ 4.641512305408857
# Probability ≈ 0.7275789473684208
def main():
    ex2()
    ex3()
    ex4()



if __name__ == "__main__":
    main()