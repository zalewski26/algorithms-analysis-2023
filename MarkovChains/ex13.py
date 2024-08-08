import numpy as np


n = 4
P = np.array([
    [0, 0.3, 0.1, 0.6],
    [0.1, 0.1, 0.7, 0.1],
    [0.1, 0.7, 0.1, 0.1],
    [0.9, 0.1, 0, 0],
    ])

# pi * P = pi  <=>  P^T * pi^T = pi^T
eigval, eigvec = np.linalg.eig(np.transpose(P))
index = np.where(np.isclose(eigval, 1))[0][0]
pi = np.real(np.transpose(eigvec[:, index]))
pi = np.abs(pi) / sum(np.abs(pi))
print(f"Stationary: {pi}")

# prob of 0 -> 3  after 32 steps
result1 = np.linalg.matrix_power(P, 32)[0][3]
print(f"Probability of 0->3 after 32 steps: {result1}")

# prob of _ -> 3  after 128 steps
prob = np.linalg.matrix_power(P, 128)
result2 = sum([prob[i, 3] for i in range(n)]) / n 
print(f"Probability of _->3 after 128 steps: {result2}")

# min t  max_s |(P_0,s)^t - pi_s| <= eps
for eps in [0.1, 0.01, 0.001]:
    print(f"eps = {eps}:")
    t = 1
    result = 1
    P_temp = P
    while True:
        result = max(abs(P_temp[0] - pi))
        if (result <= eps):
            break
        t += 1
        P_temp = np.dot(P, P_temp)
    print(f"\tt = {t}")