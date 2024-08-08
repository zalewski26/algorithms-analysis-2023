
counter = 0

def f(n):
    s = 0;
    if n == 0:
        return 1
    else:
        for i in range(n):
            s += f(i)
            global counter
            counter += 1
        return s

val_list = [0, 1]    

print("i: counter vs 3a_{n-1} - 2a_{n-2}")
print("---------------------------------")
for i in range(30):
    counter = 0
    f(i)
    expected = 3*val_list[-1] - 2*val_list[-2] if i >= 2 else val_list[i]
    val_list.append(expected)
    print(f"{i}: {counter} vs {expected}")
