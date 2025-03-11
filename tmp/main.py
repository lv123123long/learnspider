my_dict = {'a': 1, 'b': 2, 'c': 3}

it_keys = iter(my_dict)      # 迭代键

it_values = iter(my_dict.values())   # 迭代值

it_items = iter(my_dict.items())    # 迭代键值对

print(it_keys.__next__())   #   a

print(it_values.__next__())  # 1

print(it_items.__next__())   # ('a', 1)