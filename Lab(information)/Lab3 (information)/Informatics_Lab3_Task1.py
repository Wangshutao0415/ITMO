# Author = [Ван Шутао]
# Group = P3113
# Date = 11.11.2025

import re


def find_haiku_words(text):
    """
    找到包含两个连续元音且后接不超过3个辅音单词的单词
    Найдите слова, содержащие две последовательные гласные и за которыми следует не более трёх согласных.
    """
    # 定义元音和辅音
    vowels = 'аеёиоуыэюяaeiou'  # 俄语和英语元音;Русские и английские гласные
    consonants = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz'  # 俄语和英语辅音;Русские и английские согласные

    # 匹配单词的模式（包含字母、连字符、撇号）;Шаблон для сопоставления слов (включая буквы, дефисы и апострофы)
    words = re.findall(r"[\w'-]+", text, re.IGNORECASE)

    result = []

    for i in range(len(words) - 1):
        current_word = words[i].lower()
        next_word = words[i + 1].lower()

        # 检查当前单词是否有两个连续元音;Проверьте, есть ли в текущем слове две последовательные гласные.
        has_double_vowel = False
        for j in range(len(current_word) - 1):
            if (current_word[j] in vowels and
                    current_word[j + 1] in vowels):
                has_double_vowel = True
                break

        # 计算下一个单词的辅音数量;Посчитать количество согласных в следующем слове
        consonant_count = 0
        for char in next_word:
            if char in consonants:
                consonant_count += 1

        # 如果满足条件，添加到结果;Если условие выполнено, добавить в результат
        if has_double_vowel and consonant_count <= 3:
            result.append(words[i])

    return result


# 测试用例
test_cases = [
    "Кривошеее существо гуляет по парку",
    "Красивое дерево стоит в лесу",
    "Синее море глубокое и широкое",
    "Большое яблоко лежит на столе",
    "Зеленое поле простирается до горизонта"
]

print("Результаты теста задачи 1:")
for i, test in enumerate(test_cases, 1):
    result = find_haiku_words(test)
    print(f"тест {i}: '{test}'")
    print(f"результат: {result}")
    print()