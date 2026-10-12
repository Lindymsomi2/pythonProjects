# Python Data Structures and Slicing Challenge

# Given Data:
my_list = [10, 20, 30, 40, 50]
my_tuple = (5, 15, 25, 35, 45)
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# 1. Print the third element from the list.
third_element_list = my_list[2]
print(third_element_list)
# 2. Print the last element from the tuple.
last_element_tuple = my_tuple[-1]
print(last_element_tuple)
# 3. Print the value associated with the key 'age' from the dictionary.
age_value_dict = my_dict["age"]
print(age_value_dict)
# 4. Use slicing to print the first three elements from the list.
sliced_list = my_list[ : 3:]
print(sliced_list)
# 5. Use negative indexing to print the last two elements from the tuple.
last_two_elements_tuple = my_tuple[-2::1]
print(last_two_elements_tuple)