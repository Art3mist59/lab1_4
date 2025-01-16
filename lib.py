def count_common_elements(*lists):
    """Функция, которая принимает N списков и возвращает количество одинаковых элементов в них."""
    if not lists:
        return 0

    # Используем множество для хранения уникальных элементов из первого списка
    common_elements = set(lists[0])

    # Перебираем остальные списки и обновляем множество
    for lst in lists[1:]:
        common_elements.intersection_update(lst)

    return len(common_elements)

if __name__ == "__main__":
    # Пример использования функции
    n = int(input("Введите количество списков: "))
    lists = []

    for i in range(n):
        lst = input(f"Введите элементы списка {i + 1} через пробел: ").split()
        lists.append(lst)

    result = count_common_elements(*lists)
    print(f"Количество одинаковых элементов в списках: {result}")