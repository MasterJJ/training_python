is_even = lambda x: x % 2 == 0
print(is_even(3))
print(is_even(2))

# filter
input_raw_data = [0, 1, 2, 3, 4, 5,]
get_filter_data = list(filter(lambda a: a % 2 == 0, input_raw_data))

print(get_filter_data)
