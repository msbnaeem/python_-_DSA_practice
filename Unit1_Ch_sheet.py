# split method

# Example 1: Split along whitespace
s = 'Never gonna give you up'
split = s.split()
# print(split) # Prints ['Never', 'gonna', 'give', 'you', 'up']

# Example 2: Split along specified separator
s = 'Never-gonna-let-you-down'
split = s.split("-", 1)
# print(split) # Prints ['Never', 'gonna', 'let', 'you', 'down']


my_string = 'code'
for index, char in enumerate(my_string):
#   print(index, char)
    pass

# two pointer
lst = [1,8,9,6,7,5,4]

left_pointer = 0
right_pointer = len(lst) - 1

while left_pointer < right_pointer:
    temp = lst[left_pointer]
    lst[left_pointer] = lst[right_pointer]
    lst[right_pointer] = temp
    
    left_pointer +=1
    right_pointer -=1

print(lst)




