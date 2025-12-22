def hamming_decode(bits):
    # 简单检查输入长度
    if len(bits) != 7:
        print("Пожалуйста, введите 7-битное двоичное число")
        return
    r1 = int(bits[0])
    r2 = int(bits[1])
    i1 = int(bits[2])
    r3 = int(bits[3])
    i2 = int(bits[4])
    i3 = int(bits[5])
    i4 = int(bits[6])

    s1 = r1 ^ i1 ^ i2 ^ i4
    s2 = r2 ^ i1 ^ i3 ^ i4
    s3 = r3 ^ i2 ^ i3 ^ i4

    syndrome = (s3 << 2) | (s2 << 1) | s1

    error_pos = syndrome
    if error_pos != 0:
        print(f"Ошибка в бите №{error_pos}")
        if error_pos == 1:
            r1 ^= 1
        elif error_pos == 2:
            r2 ^= 1
        elif error_pos == 3:
            i1 ^= 1
        elif error_pos == 4:
            r3 ^= 1
        elif error_pos == 5:
            i2 ^= 1
        elif error_pos == 6:
            i3 ^= 1
        elif error_pos == 7:
            i4 ^= 1
    else:
        print("Ошибок нет")

    corrected = [i1, i2, i3, i4]
    print(f"Правильное сообщение: {corrected}")

# Пример вызова:
hamming_decode("0001110")