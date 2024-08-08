import numpy as np
import matplotlib.pyplot as plt


n = 5
P = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    ], dtype=float)
J = np.ones((n, n))
pi_0 = (0.2, 0.2, 0.2, 0.2, 0.2)
alphas = [0, 0.25, 0.5, 0.75, 0.85, 1]
steps = 25


for i in range(len(P)):
    if all(element == 0 for element in P[i]):
        P[i] = [1] * len(P[i])
for i in range(len(P)):
    P[i] /= sum(P[i])
    

pi_val = {}
pi_diff = {}
for alpha in alphas:
    M = (1-alpha)*P + alpha/n * J
    eigval, eigvec = np.linalg.eig(np.transpose(M))
    indexes = np.where(np.isclose(eigval, 1))[0]
    stationary = np.zeros(n)
    for index in indexes:
        pi = np.abs(np.real(np.transpose(eigvec[:, index])))
        pi /= sum(pi)
        stationary += pi
    stationary /= sum(stationary)
    temp_pi = pi_0
    pi_val[alpha] = [temp_pi]
    pi_diff[alpha] = [sum([abs(temp_pi[i] - stationary[i]) for i in range(n)])]
    for _ in range(steps):
        temp_pi = np.dot(temp_pi, M)
        pi_val[alpha].append([temp_pi])
        pi_diff[alpha].extend([sum([abs(temp_pi[i] - stationary[i]) for i in range(n)])])

result_path = 'results'
for alpha, values in pi_diff.items():
    plt.plot(range(steps+1), values, label=f'Alpha = {alpha}')
plt.xlabel('Steps')
plt.ylabel('Diff')
plt.title('Difference between current and stationary')
plt.legend()
plt.savefig(f'{result_path}/diff.png')
plt.clf()

last_values = {alpha: values[-1] for alpha, values in pi_val.items()}
for alpha, values in last_values.items():
    for val in values:
        plt.bar(range(n), val)
    plt.grid()
    plt.xlabel('Page')
    plt.ylabel('Probability')
    plt.title(f'Distribution after 25 steps with alpha = {alpha}')
    plt.savefig(f'{result_path}/alpha_{alpha}.png')
    plt.clf()