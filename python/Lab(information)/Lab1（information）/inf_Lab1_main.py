# 简单进制转换程序
# 输入：一个 C 进制下的数
# 输出：对应的 B 进制下的数

def to_base(n, base):
    """把十进制整数 n 转换成 base 进制字符串"""
    #Преобразовать десятичное целое число n в строку в системе счисления base
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res

# 示例：把 "30242" 从 5 进制转到 15 进制
#пример
num_str = "30242"
#输入A项
base_C = 5   # 源进制 C
#输入C
base_B = 15  # 目标进制 B
#输入B

# 先转成十进制整数
num_decimal = int(num_str, base_C)
print("十进制值:", num_decimal)
#Сначала преобразуйте в десятичную систему

# 再转成 B 进制
result = to_base(num_decimal, base_B)
print(f"{num_str} (base {base_C}) = {result} (base {base_B})")
#А потом перевести в систему счисления B
