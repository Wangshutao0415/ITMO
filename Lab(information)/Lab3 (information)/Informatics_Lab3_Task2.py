# Author = [Ван Шутао]
# Group = P3113
# Date = 11.11.2025

import re


def find_and_sort_words(text):
    """
    找到严格只含一个元音字母的单词，并按长度和字典序排序
    Найдите слова, содержащие ровно одну гласную букву, и отсортируйте их по длине и в алфавитном порядке
    """
    # 定义元音（俄语和英语）;Определение гласных (на русском и английском)
    vowels = 'аеёиоуыэюяaeiou'

    # 获取所有单词;Получить все слова
    words = re.findall(r"[\w'-]+", text)

    # 筛选只包含一个不同元音的单词;Выберите слова, содержащие только один различающийся гласный.
    filtered_words = []

    for word in words:
        # 找到单词中的所有不同元音;Найдите все разные гласные в слове
        found_vowels = set()
        for char in word.lower():
            if char in vowels:
                found_vowels.add(char)

        # 如果只有一个不同的元音;Если есть только один различный гласный
        if len(found_vowels) == 1:
            filtered_words.append(word)

    # 排序：先按长度，再按字典序;Сортировка: сначала по длине, затем по словарному порядку
    filtered_words.sort(key=lambda x: (len(x), x.lower()))

    return filtered_words


# 测试用例;тестовый пример
test_cases = [
    "Классное слово – обороноспособность, которое должно идти после слов: трава и молоко.",
    "Окно стол дом школа университет",
    "Мама мыла раму в комнате",
    "Большое красное яблоко лежит на столе",
    "Река течет медленно и спокойно"
]

print("Результаты теста задачи 2:")
for i, test in enumerate(test_cases, 1):
    result = find_and_sort_words(test)
    print(f"тест {i}: '{test}'")
    print(f"результат: {result}")
    print()