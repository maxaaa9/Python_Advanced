def negatives(nums):
    n_result = sum(int(x) for x in nums if int(x) < 0)
    print(n_result)
    return n_result


def positives(nums):
    p_result = sum(int(x) for x in nums if int(x) > 0)
    print(p_result)
    return p_result


def result(pos_sum, neg_sum):
    if abs(neg_sum) > pos_sum:
        return "The negatives are stronger than the positives"

    return "The positives are stronger than the negatives"


numbers = input().split()
negative_sum = negatives(numbers)
positive_sum = positives(numbers)

print(result(positive_sum, negative_sum))