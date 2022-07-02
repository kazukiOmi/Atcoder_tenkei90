import math
import functools
from itertools import permutations


def binary_search(numbers, value):
    """2分探索，みつかったらそのインデックス，見つからなかったら入るべきインデックス"""
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    if numbers[mid] < value:
        return mid+1
    else:
        return mid


def make_cumSum(list: list) -> list:
    """累積和作成"""
    cum_sum = []
    cum_sum.append(list[0])
    for a in list[1:]:
        cum_sum.append(a+cum_sum[-1])
    return cum_sum


def get_gcd(numbers: list) -> int:
    gcd = functools.reduce(math.gcd, numbers)
    return gcd


def make_junretsu(n: int):
    for comb in permutations(range(n)):
        print(comb)


def exp_cal(v, n, mod=None):
    """
    exponentiation calculation (高速累乗計算)
    Returns:
        int: v**n % mod
    """
    return pow(v, n, mod)


def factorization(n):
    """
    factarization (高速素因数分解)
    Returns:
        list: [[素因数1,累乗1],[素因数2,累乗2],...]
    """
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def combination(n, r):
    if(n < r):
        return 0
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def updateCombinationIndex(lastIndex, start, repetition=False):
    result = lastIndex[:start]
    x = lastIndex[start] + 1
    for i in range(start, len(lastIndex)):
        result.append(x)
        if(repetition == False):
            x += 1
    return result


def getComginationIndex(length, r, lastIndex):
    result = []
    for i in range(r):
        if(len(lastIndex) == 0):
            result.append(i)
        elif(lastIndex[i] >= length - r + i):
            result = updateCombinationIndex(lastIndex, i - 1, False)
            break
        elif(i == r - 1):
            result = updateCombinationIndex(lastIndex, i, False)
    return result


def getListElements(lis, indices):
    """listからindicesで示される要素の組を返す"""
    return [lis[i] for i in indices]


def combinationList(data, r):
    """dataからr個選ぶ組み合わせを全て出力する"""
    length = len(data)
    total = combination(length, r)
    result = []
    lastIndex = []
    for i in range(total):
        lastIndex = getComginationIndex(length, r, lastIndex)
        result.append(getListElements(data, lastIndex))
    return result
