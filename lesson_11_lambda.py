names = ['Ivan', 'Vika', 66, 88, 'vadim', 'yura', 'vita']
convert_to_str = map(lambda s: str(s), names)
print(list(convert_to_str))

numbers = [1, 4.6, 7, 8, 9, 5, 3, 'kkk', 4.6, 7.8, 9.7]
result = list(filter(lambda x: type(x) == int, numbers))
print(result)
