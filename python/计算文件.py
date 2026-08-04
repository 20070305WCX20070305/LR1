'''
用0到9十个数字各一次，组成四位数，三位数，两位数，一位数各一个，四个数字两两互质，已知
四位数是1860，求其他三个数
'''

import tqdm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1

def find_numbers():
    possible_numbers = []
    i = 1860  # 四位数固定为1860
    for j in tqdm.tqdm(range(100, 1000)):
        for k in range(10, 100):
            for l in range(1, 10):
                if len(list(set(str(i) + str(j) + str(k) + str(l)))) == 10:
                    if are_coprime(i, j) and are_coprime(i, k) and are_coprime(i, l) and are_coprime(j, k) and are_coprime(j, l) and are_coprime(k, l):
                        possible_numbers.append((i, j, k, l))
                            
    return possible_numbers

results = find_numbers()
print(f"可能的答案有{len(results)}组")
for i in range(len(results)):
    print(f"第{i+1}组: \n四位数: {results[i][0]}\n三位数: {results[i][1]}\n两位数: {results[i][2]}\n一位数: {results[i][3]}")