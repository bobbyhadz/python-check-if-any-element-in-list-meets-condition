# Check if ANY element in a list meets a condition in Python

my_list = [1, 3, 5, 15]

if any(item > 10 for item in my_list):
    # 👇️ this runs
    print('There is an item greater than 10')
else:
    print('No items in the list are greater than 10')

# 👇️ True
print(any(item > 10 for item in my_list))

# 👇️ False
print(any(item > 50 for item in my_list))