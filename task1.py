numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_=numbers.index(None)
sum_without_none = sum(x for x in numbers if x is not None)
total_count = len(numbers)
a = sum_without_none / total_count
numbers[index_] = a
print("Измененный список:", numbers)
