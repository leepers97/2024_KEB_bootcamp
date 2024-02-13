def factorial(number) -> int :
    if number == 1 :
        return 1
    else :
        return number * factorial(number - 1)

def nCr(n, r) -> int :
    '''
    조합함수
    :param n:
    :param r:
    :return:
    '''
    numerater = factorial(n)
    denominator = factorial(n - r) * factorial(r)
    return int(numerater / denominator)