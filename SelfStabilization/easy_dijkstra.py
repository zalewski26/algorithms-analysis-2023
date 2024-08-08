from itertools import product
from multiprocessing import Pool
from tqdm import tqdm


def is_legal(config):
    result = 0
    if config[0] == config[-1]:
        result += 1
    for i in range(1, len(config)):
        if (config[i] != config[i-1]):
            result += 1
    return result == 1


def count_max_steps(config):
    result = 0
    def count_steps(config, counter=0):
        nonlocal result
        if is_legal(config):
            if counter > result:
                result = counter
            return
        if config[0] == config[-1]:
            new_config = config[:]
            new_config[0] = (new_config[0] + 1) % (len(new_config) + 1)
            count_steps(new_config, counter+1)
        for i in range(1, len(config)):
            if (config[i] != config[i-1]):
                new_config = config[:]
                new_config[i] = new_config[i-1]
                count_steps(new_config, counter+1)
    count_steps(config)
    return result


def process_config(config):
    return config, count_max_steps(list(config))


# n = 3 => 2
# n = 4 => 13
# n = 5 => 24
def main():
    n = 5
    configurations = product(range(n+1), repeat=n)
    pool = Pool()
    results = []

    for c, result in pool.map(process_config, configurations):
        print(f"{c} -> {result}")
        results.append(result)
    print(max(results))
    


if __name__ == '__main__':
    main()