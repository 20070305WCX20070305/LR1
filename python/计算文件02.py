"""
    有两个整数a和b，他们的和是两个数字相同的两位数，他们的乘积是三个数字相同的三位数，求a和b的值。
"""

def find_numbers():
    result = []
    for a in range(10, 100):
        for b in range(10, 100):
            if (a + b) % 11 == 0 and (a * b) % 111 == 0 and (a + b) < 100 and (a * b) < 1000 and (a, b) not in result and (b, a) not in result:
                result.append((a, b))
    return result

result = find_numbers()
if result:
    for res in result:
        print(f"找到的结果是: a = {res[0]}, b = {res[1]}")
else:
    print("没有找到符合条件的结果。")