import numpy as np


n = 6
P = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0.5, 0, 0.5, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0.5, 0, 0, 0.5, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    ])
P_mod = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0.5, 0, 0, 0.5, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    ])
J = np.ones((n, n))

# pi * M = pi  <=>  M^T * pi^T = pi^T
print("First:")
for alpha in [0, 0.15, 0.5, 1]:
    M = (1-alpha)*P + alpha/n * J
    eigval, eigvec = np.linalg.eig(np.transpose(M))
    indexes = np.where(np.isclose(eigval, 1))[0]
    result = np.zeros(n)
    print(f"\talpha = {alpha}:")
    for index in indexes:
        pi = np.abs(np.real(np.transpose(eigvec[:, index])))
        pi /= sum(pi)
        result += pi
        print(f"\t\tpi = {pi}")
    result /= sum(result)
    print(f"\t\tresult = {result}")

print("Modified:")
for alpha in [0, 0.15, 0.5, 1]:
    M = (1-alpha)*P_mod + alpha/n * J
    eigval, eigvec = np.linalg.eig(np.transpose(M))
    indexes = np.where(np.isclose(eigval, 1))[0]
    result = np.zeros(n)
    print(f"\talpha = {alpha}:")
    for index in indexes:
        pi = np.abs(np.real(np.transpose(eigvec[:, index])))
        pi /= sum(pi)
        result += pi
        print(f"\t\tpi = {pi}")
    result /= sum(result)
    print(f"\t\tresult = {result}")