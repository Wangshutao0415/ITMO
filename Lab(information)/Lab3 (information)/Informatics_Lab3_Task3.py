# Author = [Ван Шутао]
# Group = P3113
# Date = 11.11.2025

import re


def validate_cron_expression(cron_str):
    """
    验证cron表达式的格式正确性
    Проверить правильность формата cron-выражения
    """
    # 定义每个字段的正则表达式模式;Определить шаблон регулярного выражения для каждого поля
    minute_pattern = r'(\*|(\*/\d+)|(\d+-\d+)|\d+)'
    hour_pattern = r'(\*|(\*/\d+)|(\d+-\d+)|\d+)'
    day_of_month_pattern = r'(\*|(\*/\d+)|(\d+-\d+)|\d+)'
    month_pattern = r'(\*|(\*/\d+)|(\d+-\d+)|\d+)'
    day_of_week_pattern = r'(\*|(\*/\d+)|(\d+-\d+)|\d+)'

    # 完整的cron表达式模式;Полный шаблон выражения cron,cron,будильник


    # Cron是类Unix系统中的一个守护进程，用于在预定时间自动执行命令或脚本。它通过cron表达式来定义任务执行的时间规则。
    cron_pattern = f'^{minute_pattern} {hour_pattern} {day_of_month_pattern} {month_pattern} {day_of_week_pattern}$'

    # 检查格式;Проверить формат
    if not re.match(cron_pattern, cron_str):
        return False, "Ошибка формата,格式错误"

    # 分割字段;разделённое поле
    fields = cron_str.split()

    # 验证每个字段的范围;Проверить диапазон каждого поля
    ranges = [
        (0, 59, "минута"),  # 分钟
        (0, 23, "час"),  # 小时
        (1, 31, "Дата"),  # 月份中的日期
        (1, 12, "месяц"),  # 月份
        (0, 6, "неделя")  # 星期几
    ]

    for i, field in enumerate(fields):
        min_val, max_val, field_name = ranges[i]

        # 如果是星号，通过;Если это звездочка, пройти
        if field == '*':
            continue

        # 如果是 */数字;Если это */число
        if field.startswith('*/'):
            try:
                num = int(field[2:])
                if num <= 0 or num > (max_val - min_val + 1):
                    return False, f"{field_name}Значение шага поля выходит за пределы допустимого диапазона/字段步长值超出范围"
            except ValueError:
                return False, f"{field_name}Неверный формат поля/字段格式错误"

        # 如果是数字范围;Если это числовой диапазон
        elif '-' in field:
            try:
                start, end = map(int, field.split('-'))
                if start < min_val or end > max_val or start > end:
                    return False, f"{field_name}Ошибка диапазона поля/字段范围错误"
            except ValueError:
                return False, f"{field_name}Неверный формат диапазона поля/字段范围格式错误"

        # 如果是单个数字;Если это одна цифра
        else:
            try:
                num = int(field)
                if num < min_val or num > max_val:
                    return False, f"{field_name}Значение поля выходит за пределы допустимого диапазона/字段值超出范围"
            except ValueError:
                return False, f"{field_name}Неверный формат поля/字段格式错误"

    return True, "格式正确/Формат правильный"


# 测试用例;тестовый пример
test_cases = [
    "30 9 * * *",  # 正确,Правильный
    "*/5 * * * *",  # 正确,Правильный
    "0 0 1 1 *",  # 正确,Правильный
    "60 14 * * *",  # 错误 - 分钟超出范围,ошибка - Минуты вне допустимого диапазона
    "30 24 * * *",  # 错误 - 小时超出范围,ошибка -Часы вышли за пределы диапазона     разбуди
    "30 14 32 * *",  # 错误 - 日期超出范围,ошибка -Дата вне диапазона
    "30 14 * 13 *",  # 错误 - 月份超出范围,ошибка -Месяц вне диапазона
    "30 14 * * 7",  # 错误 - 星期超出范围,ошибка -Недопустимый день недели
    "30 14 * *",  # 错误 - 字段数量不足,ошибка -Недостаточное количество полей
    "30 14 * * * *",  # 错误 - 字段数量过多,ошибка -Слишком много полей
]

print("Результаты теста задачи 3:")
for i, test in enumerate(test_cases, 1):
    is_valid, message = validate_cron_expression(test)
    status = "Правильный" if is_valid else "ошибка"
    print(f"тест {i}: '{test}' - {status} ({message})")
    # Cron — это демон в системах, похожих на Unix,
    # используемый для автоматического выполнения команд или скриптов в запланированное время.
    # Он определяет правила выполнения задач с помощью cron-выражений.