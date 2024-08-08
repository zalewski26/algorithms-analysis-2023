from itertools import product
from tqdm import tqdm


def is_legal(config):
    result = 0
    if config[0] == config[-1]:
        result += 1
    for i in range(1, len(config)):
        if (config[i] != config[i-1]):
            result += 1
    return result == 1


def count_max_steps(config, visited_dict):
    result = 0
    def count_steps(config, counter=0):
        nonlocal result
        if is_legal(config):
            if counter > result:
                result = counter
            return 0
        max_dist_to_end = 0
        if tuple(config) in visited_dict:
            max_dist_to_end = counter + visited_dict[tuple(config)]
            if max_dist_to_end > result:
                result = max_dist_to_end
            return visited_dict[tuple(config)]
        if config[0] == config[-1]:
            new_config = config[:]
            new_config[0] = (new_config[0] + 1) % (len(new_config) + 1)
            max_dist_to_end = max(max_dist_to_end, count_steps(new_config, counter+1) + 1)
        for i in range(1, len(config)):
            if (config[i] != config[i-1]):
                new_config = config[:]
                new_config[i] = new_config[i-1]
                max_dist_to_end = max(max_dist_to_end, count_steps(new_config, counter+1) + 1)
        visited_dict[tuple(config)] = max_dist_to_end
        return max_dist_to_end
    count_steps(config)
    return result


# n = 3 => 2
# n = 4 => 13
# n = 5 => 24
# n = 6 => 38
# n = 7 => 55
# n = 8 => 75
def main():
    n = 7
    configurations = product(range(n+1), repeat=n)
    visited_dict = {}
    results = []
    for c in tqdm(configurations, total=pow(n+1, n)):
        results.append(count_max_steps(list(c), visited_dict))
    print(max(results))
    


if __name__ == '__main__':
    main()