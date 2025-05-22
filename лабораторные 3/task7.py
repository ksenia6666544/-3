def find_common_participants(group1, group2, separator=','):
    """
    Находит общих участников между двумя группами.

    :param group1: Строка с фамилиями первой группы, разделёнными разделителем
    :param group2: Строка с фамилиями второй группы, разделёнными разделителем
    :param separator: Символ-разделитель (по умолчанию ",")
    :return: Отсортированный список общих участников
    """
    # Преобразуем строки в множества уникальных фамилий
    set1 = set(group1.split(separator))
    set2 = set(group2.split(separator))

    # Находим пересечение множеств
    common_participants = sorted(set1 & set2)

    return common_participants


# Проверим работу функции
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)  # Выведет ["Петров", "Сидоров"]

# Другой пример с другим разделителем
group_a = "Сергеев-Семенов-Козлов"
group_b = "Семенов-Козлов-Иванов"

result = find_common_participants(group_a, group_b, '-')
print(result)  # Выведет ["Козлов", "Семенов"]

