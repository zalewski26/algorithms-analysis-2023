import random


counter = 0

def f(n):
    global counter
    counter += 1
    if n >= 2:
        for i in range(1,n+1):
            if random.random() > 0.5:
                f(i)

val_list = [1, 1]  
iterations = 10000

print("i: counter vs 3*2^{n-2}: diff")
print("---------------------------------")
for i in range(30):
    counter = 0
    for j in range(iterations):
        f(i)
    counter /= iterations
    expected = 3*2**(i-2) if i >= 2 else val_list[i]
    val_list.append(expected)
    print(f"{i}: {counter} vs {expected}: \t{(abs(counter - expected) / expected * 100):.02f}%")