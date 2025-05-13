def find_first_occurrence(items_list, item):
    try:
        return items_list.index(item)
    except ValueError:
        return None

# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Поиск индексов для разных товаров
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_occurrence(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

