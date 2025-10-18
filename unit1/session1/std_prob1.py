# 1 hundred acre wood
def welcome():
    print("Welcome to The Hundred Acre Wood!")

# welcome()

# 2 greetings

def greetings(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# greetings('Mohammad')

# 3 catchcephrase
def print_catchphrase(character):

    phrases = {"Pooh":"Oh brother!", "Trigger":"TTFN: Ta-ta for now!", "Eeyore": "Thanks for noticing me.", 
               "Christopher Robin": "Silly old bear."}
    
    if character in phrases:
        print(phrases[character])
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

# print_catchphrase("Poo")

# 4 return item
def get_item(items, x):

    if x not in range(len(items)):
        return None
    return items[x]

items = ["Pnguin", 'horse', 'cat']
x = 2
# print(get_item(items, x))
result = get_item(items, x)
# print(result)
x = 4
result = get_item(items, x)
# print(result)

#  5 
'''
Total Honey
Winnie the Pooh wants to know how much honey he has. 
Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. 
Do not use the built-in function sum().
'''
def sum_honey(hunney_jars):
    summ = 0
    for i in hunney_jars:
        summ += i
    return summ

x = [1,2,2,1]
# for i in x:
#     summ += i
# print(sum_honey(x))

'''
Problem 6: Double Trouble
Help Winnie the Pooh double his honey! Write a function doubled() 
that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. 
Return the doubled list.
'''
def doubled(hunny_jars):
    doubled = [num * 2 for num in hunny_jars]
    return doubled

lst = [1,8,99,63]
# print(doubled(lst))

'''Problem 7: Poohsticks
Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. 
They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. 
count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.
'''
def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count

lst = [1,2,3,4,5,6,7,8]
# threshold = 5
# print(count_less_than(lst, threshold=8))

# Problem 8: Pooh's To Do's
def print_todo_list(task):
    print("Pooh's To Dos:")
    
# Problem 8: Pooh's To Do's

def print_todo_list(task):
	
    for number, task in enumerate(task):
        print(number, task)


# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

# task = []
# print_todo_list(task)

# Problem 9: Pairs
def can_pair(item_quantities):
    even = []
    for num in item_quantities:
        if num % 2 != 0:
            return False
        else:
            return True



    


'''
Problem 10: Split Haycorns
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. 
split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.
'''
def split_haycorns(quantity):
     splitted = []
     for i in quantity:
        if quantity % i == 0:
            splitted.append(quantity)
     return splitted

quantity = 6
# print(split_haycorns(quantity))

