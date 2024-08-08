import math

k = 400
alpha = 0.05

def f_k(x: float):
    return math.exp(x * k) * pow((1.0 - x), k)

def chernoff(delta):
    eps1 = delta/(1+delta)
    eps2 = delta/(1-delta)

    return f_k(eps1) + f_k(-eps2)

def main():
    left = 0.0
    right = 1.0
    
    while (left <= right - 0.00000001):
        mid = (left + right) / 2
        result = chernoff(mid)
        if result > alpha:
            left = mid
        else:
            right = mid
    
    print(left)


if __name__ == '__main__':
    main() 
    

# 0.005 = 0.18274402618408203
# 0.01 = 0.1697627380490303
# 0.05 = 0.1381368190050125