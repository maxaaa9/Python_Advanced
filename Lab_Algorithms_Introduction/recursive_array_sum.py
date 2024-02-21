def recursive_sum(data, index=0):

    if index == len(data) - 1:
        return data[index]
    return data[index] + recursive_sum(data, index + 1)


print(recursive_sum([int(x) for x in input().split()]))