'''
用0到9十个数字各一次，组成四位数，三位数，两位数，一位数各一个，四个数字两两互质，已知
四位数是1860，求其他三个数
'''

from itertools import permutations
from math import gcd

def are_all_coprime(nums):
    """检查列表里所有数是否两两互质"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if gcd(nums[i], nums[j]) != 1:
                return False
    return True

def solve_without_1860():
    results = []
    # 对 0-9 十个数字进行全排列
    for p in permutations(range(10)):
        # ----- 关键剪枝：排除前导零和一位数为0的情况 -----
        # 四位数 p[0] 不能为0；三位数 p[4] 不能为0；两位数 p[7] 不能为0；一位数 p[9] 不能为0
        if p[0] == 0 or p[4] == 0 or p[7] == 0 or p[9] == 0:
            continue

        # 构造四个数
        four_digit = p[0]*1000 + p[1]*100 + p[2]*10 + p[3]
        three_digit = p[4]*100 + p[5]*10 + p[6]
        two_digit = p[7]*10 + p[8]
        one_digit = p[9]

        # 检查是否两两互质
        if are_all_coprime([four_digit, three_digit, two_digit, one_digit]) and one_digit != 1:
            results.append((four_digit, three_digit, two_digit, one_digit))

    return results

# 运行
results = solve_without_1860()
print(f"共有 {len(results)} 组解：")
for i, (a, b, c, d) in enumerate(results, 1):
    print(f"第{i}组: 四位数={a}, 三位数={b}, 两位数={c}, 一位数={d}")