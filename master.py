
# Lecture2HelloWorldAndExpressions.py
print('Hello, world!')
print('Hello 1')
print('Hello 2')
print('Hello 3')
print('Hello, world!')
print(Hello, world!)
print(Hello, world!) # Intentionally creates an error!
print(1)         # Technically an expression
print(1+2)       # Two operands and an operator make an expression
print(10*(10+1)) # The expression (10+1) acting as an operand
print(3 + 8 / 2)  # What do you predict?
print(4 * 2 + 3 + 5 * 2)  # And this one?
print('Hello', 'world', '!')
print(max(2,5,7))
print(max(2,7) + max(3,9)) # Using function calls as operands
print(max(2,7) + max(3,9)) # Calc 7, calc 9, then add
1
2
3
max(2,7)
None
print(2) + 2
print('Hello, world!')
max(2 ** 8, 3 ** 6, 5 ** 3)
1.0000000000000001 - 1
print(type(-100)) # int
print(type(10.1)) # float
print(type('A'))  # str
print(type(True)) # bool
print(type('10')) # str
print(type(10))   # int
print(type(10.0)) # float
print(type(True)) # bool
0.1 + 0.1 + 0.1
'Hello ' + 1111
'Hello ' + 'world' + '!'
'Hello ' + str(1111)
20 * 9/5 + 32
print('Temp: 68.0 F')
print('Temp: ' + 20 * 9/5 + 32 + ' F')
print('Temp: ' + str(20 * 9/5 + 32) + ' F')
# Lecture3VariablesAndConditions.py
two_to_the_eighth = 2 ** 8
print(two_to_the_eighth)
two_to_the_eighth * 2
pay_per_hour = 18
pay_per_hour = 20  # Pay raise!
print(pay_per_hour)
counter = 0
counter = counter + 1 # It's an instruction, not an equality!
print(counter)
counter = counter + 1
print(counter)
pay_per_hour = 20
hours = 40
total_pay = pay_per_hour * hours
print(total_pay)
Pay_Per_Hour = 15   # please avoid this capitalization style!
print(pay_per_hour) # remembers the lowercase value
silent_assignment = 0
20 = pay_per_hour
print(undefined_var + 7)
color = input('What is your favorite color? ')
print('Yeah, ' + color + ' is pretty great!')
to_square_str = input('What should I square? ')
print(int(to_square_str) ** 2)
city = input('What city are we in? ')
print(city == 'Boston')
    
answer = input('What is 2+2? ')
print(answer == 4) # not going to work
answer == '4'   # but this works
int(answer) == 4 # or this
float(answer) == 4 # or even this
print(1 < 1)
print(1 > 1)
print(1 != 1)
print(1 <= 1)
print(1 >= 1)
print('aardvark' < 'zebra')
print('capitalized' == 'Capitalized')
2 + 5 > 7 - 4  # 5 > 7 would be false, but (2+5) > (7-4) is True
total = 0
value_str = input('Enter a value: ')
value_int = int(value_str)
if value_int < 0:
    print('Sorry, that was a negative value.')
else:
    total = total + value_int
print(total)
if condition:
    statement_if_true1
    statement_if_true2
    statement_if_true3
    ...
else:
    statement_if_false1
    statement_if_false2
    ...
statement_regardless1
statement_regardless2
...
value = int(input('Enter an integer:'))
if value < 0:
    print('Negative')
else:
    print('Positive')
print('Done')
password = input('Enter the password: ')
if password == '1234':
    print('Correct!')
    print('Your account has $1000000 in it.')
else:
    print('Incorrect.')
print('Have a nice day.')
num1_str = input('Enter an integer: ')
num2_str = input('Enter a different integer: ')
num1_int = int(num1_str)
num2_int = int(num2_str)
if num1_str == num2_str:
    print('The numbers were supposed to be different...')
    print('But you entered ' + num1_str + ' twice!')
else:
    print(num2_str + ' divided by ' + num1_str + ' is...')
    print(num2_int / num1_int)  # Divide by zero would be error, btw
print('Done...')
language = input('What is your favorite language? ')
if language == 'Python':
    print('Mine too!')
print('But there sure are a lot of languages out there....')
value = int(input('Enter an integer between 0 and 100: '))
if value < 0:
    print('No negative numbers!')
elif value > 100:
    print('That value is too large!')
elif value == 42:
    print('That was the number I was thinking of!')
else:
    print('Guess again.')
    
value = int(input('Enter an integer between 0 and 100: '))
if value < 0:
    print('No negative numbers!')
elif value > 100:
    print('That value is too large!')
elif value >= 50:
    print('Big!')
else:
    print('Small!')
value = int(input('Enter an integer between 0 and 100: '))
if value < 0:
    print('No negative numbers!')
else:
    if value > 100:
        print('That value is too large!')
    else:
        if value >= 50:
            print('Big!')
        else:
            print('Small!')
age = int(input('Enter your age: '))
if age < 18:
    if age < 5:
        print('Just a toddler, then.')
    elif age < 12:
        print('Not quite a teenager, then.')
    else:
        print('Teenage years ... a difficult time!')
else:
    print('An adult, then.')
    if age >= 55:
        print('And a senior citizen, too!')
num1 = int(input('First number: '))
num2 = int(input('Second number: '))
num3 = int(input('Third number: '))
my_max = max(num1, num2, num3)
my_min = min(num1, num2, num3)
my_mean = (num1+num2+num3)/3  # Note importance of parens!
print('Min: ' + str(my_min))
print('Max: ' + str(my_max))
print('Mean: ' + str(my_mean))
if num1 == num2:
    print(str(num1) + ' was repeated')
elif num2 == num3:
    print(str(num2) + ' was repeated')
elif num1 == num3:
    print(str(num3) + ' was repeated')
else:
    print('The numbers were unique')
# Lecture4WhileAndLists.py
string = input('Enter a number: ')
while string != 'stop':
    print(string + ' squared is ' + str(int(string) ** 2))
    string = input('Enter a number: ')
print('Done.')
counter = 0
while counter < 21:
    print(counter)
    counter = counter + 1
print(counter)
counter = 1
print('We will now iterate three times...')
while counter < 4:
    print('Iteration ' + str(counter))
    counter = counter + 1
total = 0
count = 0
value_str = input('Enter a number, or "done" if done: ')
while value_str != 'done':
    count = count + 1
    value_int = int(value_str)
    total = total + value_int
    value_str = input('Enter a number, or "done" if done: ')
if count > 0:
    print('The average is ' + str(total/count))
total = 0
count = 0
value_str = input('Enter a number, or "done" if done: ')
while value_str != 'done':
    count += 1
    value_int = int(value_str)
    total += value_int
    value_str = input('Enter a number, or "done" if done: ')
if count > 0:
    print('The average is ' + str(total/count))
while(True):
    input('Enter any input to get a compliment: ')
    print('That is so clever of you!')
my_list = ['duck', 'duck', 'goose']  # A list with 3 items
print(my_list[0])
print(my_list[1])
print(my_list[2])
my_list = ['duck', 'duck', 'goose']
my_list[2] = 'bear'
print(my_list)
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # my_list has changed...
print(my_list.append(5))
print(my_list)
shopping_list = []
item = input('Add an item to the shopping list (or "done"): ')
while item.lower() != 'done':
    shopping_list.append(item)
    item = input('Add an item to the shopping list (or "done"): ')
print('Okay, so that was: ')
print(shopping_list)
[1, 2, 3] + [4, 5, 6]
print(len('Hello'))
print(len([1, 2, 3]))
my_items = ['eggs', 'flour', 'milk']
print(len(my_items), 'items')
print(my_items[2])
print(my_items[len(my_items)-1])
planet_diameter_km = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2377]
planet_diameter_km.sort()
planet_diameter_km
my_list1 = [3, 2, 1]
my_list2 = my_list1
my_list1.sort()
print(my_list1)
print(my_list2)
my_list1 = [3, 2, 1]
my_list2 = my_list1.copy()
my_list1.sort()
print(my_list1)
print(my_list2)
honors = ['Albert', 'Berenice', 'Chen', 'Dominique']
mentioned_honors = []
nonhonors = []
student = input('Enter a name (or "done"): ')
while (student != 'done'):
    if student in honors:
        print('Honors!')
        mentioned_honors.append(student)
    else:
        print('Not honors...')
        nonhonors.append(student)
    student = input('Enter a name (or "done"): ')
print('Honors mentioned: ' + str(mentioned_honors))
print('Nonhonors mentioned: ' + str(nonhonors))
# Lecture5MorePower.py
percent = input('Enter a percentage between 0 and 100:')
if float(percent) >= 0 and float(percent) <= 100:
    if float(percent) >= 10:
        print('A decent return on investment....')
    else:
        print('Not a great return on investment....')
else:
    print('That is not in the requested range!')
vip = False
spent = 10
if vip or spent >= 10000:
    print('Send this person a loyalty reward!')
else:
    print('This person deserves nothing!')
vip = False
if not vip:
    print('Have you considered signing up to join the VIP program?')
else:
    print('Welcome back, VIP customer!')
vip = False
spent = 0
if not vip or spent < 10000:  # "not" applied to vip before "or"
    print('Please spend more')
else:
    print('Hello, valued patron!')
vip = False
spent = 0
if not (vip or spent < 10000): # within parens evaluates to True
    print('Please spend more')
else:
    print('Hello, valued patron!')
my_list = [1,2,3]
my_list2 = [7,8,9]
if not 4 in my_list and not 4 in my_list2:
    print('No 4 found')
my_list = [1,2,3]
my_list2 = [7,8,9]
if 4 not in my_list and not in my_list2:
    print('This will actually cause an error - not how "in" works')
import math
math.sqrt(2)
import math as m
m.sqrt(2)
from math import sqrt as my_sqrt
my_sqrt(2)
get_ipython().system('python3 -m ensurepip --upgrade')
get_ipython().system('pip install seaborn')
import seaborn as sns
df = sns.load_dataset("penguins") # Load a dataset about penguins
sns.jointplot(data=df, x="flipper_length_mm", y="bill_length_mm", hue="species")
import statistics
statistics.median([1, 2, 3, 4])
import statistics
statistics.median([1, 2, 3, 4])
total = 0
count = 0
value_str = input('Enter a number, or "done" if done: ')
while value_str != 'done':
    count = count + 1
    value_int = int(value_str)
    total = total + value_int
    value_str = input('Enter a number, or "done" if done: ')
if count > 0:
    print('The average is ' + str(total/count))
total = 0
count = 0
value_str = input('Enter a non-negative integer, or "done" if done: ')
while value_str != 'done':
    if not value_str.isdigit():
        print('Non-negative integers only!')
    else:
        count = count + 1
        value_int = int(value_str)
        total = total + value_int
    value_str = input('Enter a non-negative integer, or "done" if done: ')
if count > 0:
    print('The average is ' + str(total/count))
total = 0
count = 0
value_str = input('Enter a number, or "done" if done: ')
while value_str != 'done':
    count = count + 1
    value_int = int(value_str)
    total = total + value_int
    print(value_str)
if count > 0:
    print('The average is ' + str(total/count))
3 = my_list
total = 0
count = 0
value_str = input('Enter a number, or "done" if done: ')
count = count + 1
value_int = int(value_str)
total = total + value_int
if count > 0:
    print('The average is ' + str(total/count))
# Lecture6and7Iteration.py
people = ['Alice', 'Bob', 'Che']
index = 0
while index < len(people):
    person = people[index]
    print('Hooray for ' + person + '!')
    index += 1
people = ['Alice', 'Bob', 'Che']
for person in people:
    print('Hooray for ' + person + '!')
running_total = 0
numbers = [1,2,3,4,10]
for n in numbers:
    running_total = running_total + n  # Could be abbreviated running_total += n
    print('Sum so far: ' + str(running_total))
print('Sum: ' + str(running_total))
my_grades = [4, 3, 2, 3, 4]
letter_grades = []
for g in my_grades:
    if g == 4:
        letter_grades.append('A')
    elif g == 3:
        letter_grades.append('B')
    elif g == 2:
        letter_grades.append('C')
print(letter_grades)
temps_f = [36, 39, 45, 56, 66, 76, 81, 80, 72, 61, 51, 41] # Jan through Dec
temps_c = []
for t in temps_f:
    degrees_c = (t - 32)*5/9
    temps_c.append(round(degrees_c, 2)) # Round to 2 decimal places
temps_c
my_car = ("Honda Fit", 2010, 30, 10000)
print(my_car)
car_type, year, mpg, price = my_car
print(mpg)
print(my_car[0] + ' prints successfully')  # OK
my_car[0] = 'bad value' # Not OK, trying to change the tuple
my_movies = [("No", 4), ("Rogue One", 4.5), ("Casablanca", 5)]
for moviename, stars in my_movies:  # Notice the two variable names
    print ('I would rate ' + moviename + ' ' + str(stars) + ' stars')
my_movies = [("No", 4), ("Rogue One", 4.5), ("Casablanca", 5)]
best_rating = 0 # Initialize with a value that is definitely beat
best_movie = "none"
for movie, rating in my_movies:
    if rating > best_rating:
        best_rating = rating
        best_movie = movie
print("Best movie: " + best_movie + "...rating = " + str(best_rating))
movies = ['Fall Guy', 'Free Guy', 'Cable Guy']
ratings = [5, 4, 3]
for movie, rating in zip(movies, ratings):
    print("I'd rate " + movie + " a " + str(rating))
sw_movies = [('The Phantom Menace', 52),
('Attack of the Clones', 65),
('Revenge of the Sith', 80),
('Rogue One', 84),
('Solo', 70),
('Star Wars', 92),
('The Empire Strikes Back',94),
('Return of the Jedi', 82),
('The Force Awakens', 93),
('The Last Jedi', 90),
('The Rise of Skywalker', 51)]
my_list = []
for movie, score in sw_movies:
  if score >= 80:
    my_list.append(movie)
print(my_list)
for i in range(5):
  print ("Iteration " + str(i))
for i in range(1,6):
    print(i)
my_itinerary = ['Boston', 'Atlanta', 'LA', 'Seattle']
for idx in range(len(my_itinerary)-1):  # Avoid indexing out of bounds
    print(my_itinerary[idx] + '-' + my_itinerary[idx+1])
names = ['Alice', 'Bob', 'Charlie', 'Dora']
for number, name in enumerate(names):
    print(name + ' ' + str(number))
for movie, rating in sw_movies:
    print('Looking at ' + movie)
    if movie == 'Rogue One':
        print('The rating of Rogue One is ' + str(rating))
        break  # We don't need to look at any other entries
print('Done')
my_two_stock_histories = [[40.1, 40.2, 39.9, 40.2],
                         [100.2, 99.9, 100.0, 103.1]]
my_two_stock_histories = [[40.1, 40.2, 39.9, 40.2],
                         [100.2, 99.9, 100.0, 103.1]]
my_two_stock_histories[1]
my_two_stock_histories = [[40.1, 40.2, 39.9, 40.2],
                         [100.2, 99.9, 100.0, 103.1]]
my_two_stock_histories[1][2]
my_stock_histories = my_two_stock_histories.copy()
my_stock_histories.append([5.0, 9.0, 6.0, 7.0])
print(my_stock_histories)
print('Stock 0 closing prices: ')
for price in my_stock_histories[0]:
    print(price)
print('Starting prices for all stocks:')
for stock_list in my_stock_histories:
    print(stock_list[0])
letters = ['a', 'b', 'c','d','e','f','g','h','i','j']
print('All possible coordinates in Battleship:')
for l in letters:
    for n in range(1,11):
        print(l + str(n))
bills = [[1, 2, 3], [4,5,6], [7,8,9]]
my_totals = [] # empty list
for l in bills:
  print('new list')
  listsum = 0
  for l2 in l: # iterating over the list we got from the outer foreach
    print('adding ' + str(l2))
    listsum += l2
  my_totals.append(listsum)
print('Bill sums:' + str(my_totals))
print('Possible matchups:')
players = ['Alice', 'Bobby', 'Caspar', 'Dmitri', 'Eve']
for white_player in players:
  for black_player in players:
    print("White: " + white_player + "; Black player: " + black_player)
print('Possible matchups:')
players = ['Alice', 'Bobby', 'Caspar', 'Dmitri', 'Eve']
for white_player in players:
  for black_player in players:
    if not white_player == black_player:
        print("White: " + white_player + "; Black player: " + black_player)
my_multiples_of_3 = [v * 3 for v in range(5)]
my_multiples_of_3
unrounded = [1.9, 5.3, 9.9]
rounded  = [round(i,0) for i in unrounded]
rounded
unrounded = [1.9, 5.3, 9.9]
rounded = []
for item in unrounded:
    rounded.append(round(item,0))
print(rounded)
temps_f = [36, 39, 45, 56, 66, 76, 81, 80, 72, 61, 51, 41] # Jan through Dec
temps_c = [round((t-32)*5/9,2) for t in temps_f]
temps_c
times = [(2,30), (4,10), (1, 30), (0,40), (0, 20)]
minutes = [t[0]*60 + t[1] for t in times]
minutes
# Lecture8and9Functions.py
def add_an_s(string):
    new_string = string + 's'
    return new_string
add_an_s('example') + '!'
records = read_customer_data('input.csv')
sales = 0
purchase_counts = []
s_names = []
for record in records:
    name, purchase_list, sale_info = parse_record(record)
    s_names.append(standardize_name(name))
    sales = update_total_sales(sales, sale_info)
    update_purchase_counts(purchase_counts, purchase_list)
write_to_file(s_names, purchase_counts, sales, 'output.csv')
def add_two(my_number):
  # Adds two to the argument.
  return my_number + 2
add_two(2)
def count_matches(to_match, my_list):
  # Counts how many times to_match appears in my_list
  count = 0
  for m in my_list:
    if to_match == m:
      count += 1
  return count
print(count_matches(5, [5, 6, 7, 5]))
print(count_matches("foo", ["foo","bar","baz"]))
def percent_gain(start, finish):
    return (finish-start)/start * 100
print(percent_gain(36585.06, 33147.25))
print(percent_gain(4796.56, 3839.50))
print(percent_gain(15832.80, 10466.48))
def get_rating(movie_tuple):
    # More readable way to access a movie rating
    return movie_tuple[1]
get_rating(('Portrait of a Lady on Fire', 5))
def with_tax(price, tax):
    return round(price * (1 + tax * .01), 2)
with_tax(1,8.6)
from datetime import date
def greet_user():
  print("Hello, user!")
  print("Today's date is " + str(date.today()))
greet_user()
def greet_user():
  print("Hello, user!")
  print("Today's date is " + str(date.today()))
  return
print(greet_user())
def longest_customer_name(list_of_names):
    # Find the longest customer name, and how long it is
    # (maybe so we can display the names nicely later)
    longest_len = 0
    longest_name = ""
    for n in list_of_names:
        if len(n) > longest_len:
            longest_len = len(n)
            longest_name = n
    return longest_name, longest_len
name, length = longest_customer_name(['Alice', 'Bob', 'Cassia'])
print(name)
print(length)
from statistics import mean
def min_mean_max(L):
    return min(L), mean(L), max(L)
min_mean_max([1,2,3,4,5])
def count_items(lst):
    # Count items but warn if the list is empty
    if (len(lst) == 0):
        print('Warning: empty list passed to count_items!')
        return 0
    print("We don't get here with an empty list")
    return len(lst)
count_items([])
def is_prime(n):
    for i in range(2, n): # Look for a divisor
        if n % i == 0:    # i divides n evenly, no remainder
            return False
    return True           # didn't find a divisor
print(is_prime(11))
print(is_prime(4))
def longest_customer_name(list_of_names):
    # Find the longest customer name, and how long it is
    # (maybe so we can display the names nicely later)
    longest_len = 0
    longest_name = ""
    for n in list_of_names:
        if len(n) > longest_len:
            longest_len = len(n)
            longest_name = n
    return longest_name, longest_len
def count_matches(to_match, my_list):
  # Counts how many times to_match appears in my_list
  count = 0
  for m in my_list:
    if to_match == m:
      count += 1
  return count
def count_longest_name(list_of_names):
    # Count how many times the longest name appears in the list
    # Makes use of functions defined above
    word, length = longest_customer_name(list_of_names)
    return count_matches(word,list_of_names)
count_longest_name(['Alice','Bob','Catherine','Catherine'])
def all_names_short_enough1(names, limit):
    for name in names:
        if len(name) > limit:
            return False
    return True
print(all_names_short_enough1(['Alice', 'Bob'], 3))
print(all_names_short_enough1(['Alice', 'Bob'], 5))
def all_names_short_enough2(names, limit):
    name, length = longest_customer_name(names)
    return length <= limit
print(all_names_short_enough2(['Alice', 'Bob'], 3))
print(all_names_short_enough2(['Alice', 'Bob'], 5))
def add5(arg):
    b = arg + 5
    return b
add5(7) # Return 12
def pattern_a(price, tax):
  return price * (1 + 0.01 * tax)  # Everything we need is in the arguments - good
tax = 20 # Global variable - this is worse style
def pattern_b(price):
  return price * (1 + 0.01 * tax) # Works, but less flexible, hard to debug
print(pattern_a(100,20))
print(pattern_b(100))
def add_two(my_number):
  a = my_number + 2 # Shadows outer "a", now we have two a's and see this one
  print("a is " + str(a) + " inside add_two")
  return a
a = 5
print("add_two(2) is " + str(add_two(2)))
print("a is " + str(a) + " outside add_two")
my_list = ['a','b','c']
def concatenate_all(my_list):
    out = ''
    for item in my_list:
        out += item
    return out
print(concatenate_all(['d','e'])) # ['d','e'] is called my_list in the function
print(concatenate_all(my_list))  # my_list is still a,b,c
names = ["Catherine", "Donovan", "alice", "BOB"]
standardized_names = []
for name in names:
    name = name.capitalize() # Capitalize first letter, lc others
    standardized_names.append(name) 
    standardized_names.sort()    
jobs = ['Pilot', 'teacheR', 'firefighter', 'LIBRARIAN']
standardized_jobs = []
for job in jobs:
    job = job.capitalize()
    standardized_jobs.append(job)
    standardized_jobs.sort()
print(standardized_names)
print(standardized_jobs)
names = ["Catherine", "Donovan", "alice", "BOB"]
jobs = ['Pilot', 'teacheR', 'firefighter', 'LIBRARIAN']
def standardize_strings(string_list):
    out = []
    for s in string_list:
        s = s.capitalize()
        out.append(s)
    out.sort()
    return out
standard_names = standardize_strings(names)
standard_jobs = standardize_strings(jobs)
print(standard_names)
print(standard_jobs)
def get_first_letter(word):
  """ Returns the first letter of a string.
  word (str):  The string to get the letter from.
  A simple function just for demo purposes.  Probably
  not useful since get_first_letter takes more characters
  to type than string[0].
  """
  return word[0]
get_ipython().run_line_magic('pinfo', 'get_first_letter')
print(get_first_letter("Shibboleth") == "S")
print(pattern_a(100,20) == 120)
print(pattern_a(0, 20) == 0)
print(count_matches("A",[]) == 0)
print(count_matches("A", ["A","A","A"]) == 3)
# Lecture10Hashes.py
my_menu_dict = {
    "Salmon": 25,
    "Steak": 30,
    "Mac and cheese" : 18
}
print(my_menu_dict["Salmon"])
my_menu_dict = {} # empty dictionary
my_menu_dict["Salmon"] = 25
my_menu_dict["Steak"] = 30
my_menu_dict["Mac and cheese"] = 18
print(my_menu_dict["Salmon"])
my_dict = {}
my_dict.get('sushi', 0)
two_cities = """It was the best of times, it was the worst of times,
 it was the age of wisdom, it was the age of foolishness, it was the epoch of belief,
 it was the epoch of incredulity, it was the season of light, it was the season of darkness,
 it was the spring of hope, it was the winter of despair."""
worddict = {}
wordlist = two_cities.split()
for word in wordlist:
  if word in worddict:  # Check for presence of key
    worddict[word] += 1
  else:
    worddict[word] = 1
print(worddict["age"])
print(worddict["of"])
for word, count in worddict.items():
  print(word + ":" + str(count))
def word_prob(word, worddict):
    numerator = worddict.get(word, 0)
    denominator = 0
    for word, count in worddict.items():
        denominator += count
    return numerator / denominator
print(word_prob('winter', worddict))  # Should be 1/60 = 0.0167 or so
print(word_prob('season', worddict))  # Should be 2/60 = 0.0333 or so
print(word_prob('Pokemon', worddict))  # Should be 0 with no errors
bigIPs = {"209.85.231.104", "207.46.170.123", "72.30.2.43"}
bigIPs.add("208.80.152.2")
len(bigIPs)
newset = set()
newset.add("First item")
print("First item" in newset)
myset = set(range(123456789))   # {0, 1, 2, ...}
mylist = list(range(123456789)) # [0, 1, 2, ...]
12345678 in myset  # Fast, uses hash
12345678 in mylist # Slower, check each item
two_cities_extended = """It was the best of times,
it was the worst of times, it was the age of wisdom,
it was the age of foolishness, it was the epoch of belief,
it was the epoch of incredulity, it was the season of Light,
it was the season of Darkness, it was the spring of hope,
it was the winter of despair, we had everything before us,
we had nothing before us, we were all going direct to Heaven,
we were all going direct the other way--in short, the period was
so far like the present period that some of its noisiest authorities
insisted on its being received, for good or for evil, in the superlative
degree of comparison only.
There were a king with a large jaw and a queen with a plain face,
on the throne of England; there were a king with a large jaw and a
queen with a fair face, on the throne of France. In both countries
it was clearer than crystal to the lords of the State preserves of
loaves and fishes, that things in general were settled for ever.
It was the year of Our Lord one thousand seven hundred and seventy-five.
Spiritual revelations were conceded to England at that favoured period,
as at this. Mrs. Southcott had recently attained her five-and-twentieth
blessed birthday, of whom a prophetic private in the Life Guards had heralded
the sublime appearance by announcing that arrangements were made for the
swallowing up of London and Westminster. Even the Cock-lane ghost had been
laid only a round dozen of years, after rapping out its messages, as the
spirits of this very year last past (supernaturally deficient in originality)
rapped out theirs. Mere messages in the earthly order of events had lately
come to the English Crown and People, from a congress of British subjects
in America: which, strange to relate, have proved more important to the human
race than any communications yet received through any of the chickens of the
Cock-lane brood. 
"""
wordlist = two_cities_extended.split()
def find_by_list(wordlist):
  for word in wordlist:
    if word in wordlist:
        continue # Move on to next loop
get_ipython().run_line_magic('time', 'find_by_list(wordlist)')
worddict = {}
for word in wordlist:
  if word in worddict:
    worddict[word] += 1
  else:
    worddict[word] = 1
def find_by_dict(wordlist, dict):
  for word in wordlist:
    if word in dict:
      continue # Move on to next iteration of the for loop
get_ipython().run_line_magic('time', 'find_by_dict(wordlist,worddict)')
mydict = {"a":1000}
dict2 = mydict # gets the address, so any changes are permanent to the original
dict2["b"] = 500
print(mydict)
print(dict2)
dict3 = dict2.copy()
dict3["c"] = 40
print(dict2)
print(dict3)
from string import ascii_lowercase
myset = set()
for i in range(len(two_cities_extended)):
  myset.add(two_cities_extended[i].lower())
def checkletters(myset):
  for c in ascii_lowercase:
    # TODO check whether this letter appeared in myset, maybe return a value
    if c not in myset:
      print("Missing: " + c)
      return False
  print("All found")
  return True
checkletters(myset)
# Lecture11and12NumpyMatplotlib.py
import numpy as np
v = np.array([1, 2 ,3])
print(v)
A = np.array([[1, 0, 0],
              [0 ,2, 0],
              [0, 0, 3]])  # 3x3 with 1,2,3 along the diagonal
print(A)
print(A.shape)  # Tuples: like lists, but use () instead of [] 
print(v.shape)  # 1d outputs a comma to indicate it's still a tuple
v1 = v
print(v1)
v2 = np.array([4, 5, 6])
print(v2)
print("Adding 1D arrays: ",  v1 + v2)
print("Subtracting 1D arrays: ",  v1 - v2)
print("Multiplying 1D arrays: ", v1 * v2)
print("Dividing 1D arrays: ", v1 / v2)
print(v1)
print("Adding by a constant: ", v1 + 2)
print("Subtracting by a constant: ", v1 - 2)
print("Multiplying by a constant: ", v1 * 2)
print("Dividing by a constant: ", v1 / 2)
my_array = np.array([[1,2,3], 
                     [4,5,6]])
print(np.min(my_array, axis=0))
print(np.mean(my_array, axis=1))
B = np.array([[3, 2], 
              [4, -1]])
w = np.array([1, -1])
z = B @ w
print(z)
my_array = np.array([8, 6, 7, 5, 3, 0, 9])
print(my_array[1:3]) # prints index 1 and 2, not 3
print(my_array)
print(my_array[1:])
my_array[:3]
my_matrix = np.array([[42.3, 71.1, 92],
                      [40.7, 70.0, 85],
                      [47.6, 122.0, 82]])
print(my_matrix)
two_by_two_square = my_matrix[1:, :2]
print(two_by_two_square)
no_last_column = my_matrix[:, :2] # no temperature
print(no_last_column)
import numpy as np
a = np.array([0, 1, 2, 3, 4, 5])
print(a)
b = a[1:3]
print(b)
b[1] = 100 # modify the slice...
print(a) # ...and see the original change
print(np.zeros(3)) #create an array of zeros with length 3
print(np.zeros((2, 3))) # create a 2x3 matrix of zeros
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [1, 4, 9]
plt.plot(x, y)
plt.show()
import numpy as np
my_points = np.array([[2, 1], 
                      [3, 4], 
                      [5, 6]]) # Each list is a point
print(my_points)
plt.plot(my_points[:, 0], my_points[:,1])    # Slice to get x values separate from y values
plt.show()
plt.plot(my_points[:, 0], my_points[:, 1], 'ro') # 'r' is for red, 'o' is for circles
plt.show()
distances_millions_miles = [35, 67, 93, 142, 484, 889, 1790, 2880]
plt.plot(np.arange(1, 9), distances_millions_miles, 'o')
plt.show()
np.arange(1,9)
xpoints = np.linspace(0, 10, 100)
ypoints = xpoints ** 2 + 1
plt.plot(xpoints, ypoints)
plt.show()
plt.plot(my_points[:, 0], my_points[:, 1], 'ro')
myfit_x = np.linspace(1, 5, 100)
myfit_y = np.linspace(1.5, 5.5, 100) # Same y/x slope for all segments - so, a line
plt.plot(myfit_x,myfit_y)
plt.show()
import matplotlib.pyplot as plt
x = [1, 2, 3]
y1 = [1, 2, 3]
y2 = [3, 2, 1]
plt.plot(x, y1, label='Sales')
plt.plot(x, y2, label='Quality')
plt.legend()
plt.title('Trends')
plt.grid(True)
customers = ['Oliver', 'Sophia', 'Liam', 'Arielle', 'Noah']
total_purchases = [56, 73, 24, 48, 88]
plt.bar(customers, total_purchases)
plt.xlabel("Customer name", fontsize=14)
plt.ylabel("Total purchases", fontsize=14)
plt.title("Total purchases for 5 Amazon customers", fontsize=16)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.show()
# Lecture13BiggerPrograms.py
    """
    Compute f-measure for each item in a list.
    
    Argument: stats_list (list):  a list of tuples of four ints, (tp, fp, tn, fn)
               (these stand for true positive, false positive, etc)
    Returns:  a list of floats, the f-measures.
    """
    """
    Compute the f-measure, a performance measure that ignores true negatives.
    
    Arguments:  tp (int):  the count of true positives
                fp (int):  the count of false negatives
                tn (int):  the count of true negatives
                fn (int):  the count of false negatives
    Returns: a float, the f-measure.
    """
def f_measures(stats_list):
    """
    Compute f-measure for each item in a list.
    
    Argument: stats_list (list):  a list of tuples of four ints, (tp, fp, tn, fn)
               (these stand for true positive, false positive, etc)
    Returns:  a list of floats, the f-measures.
    """
    for tp, fp, tn, fn in stats_list:
        f = f_measure(tp, fp, tn, fn)
def f_measures(stats_list):
    """
    Compute f-measure for each item in a list.
    
    Argument: stats_list (list):  a list of tuples of four ints, (tp, fp, tn, fn)
               (these stand for true positive, false positive, etc)
    Returns:  a list of floats, the f-measures.
    """
    out = []
    for tp, fp, tn, fn in stats_list:
        f = f_measure(tp, fp, tn, fn)
        out.append(f)
    return f
def f_measure(tp, fp, tn, fn):
    """
    Compute the f-measure, a performance measure that ignores true negatives.
    
    Arguments:  tp (int):  the count of true positives
                fp (int):  the count of false negatives
                tn (int):  the count of true negatives
                fn (int):  the count of false negatives
    Returns: a float, the f-measure.
    """
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    return (2 * precision * recall)/(precision + recall)
def f_measure(precision, recall):
    """
    Compute the f-measure, a performance measure that ignores true negatives.
    
    Arguments:  precision (float):  proportion of positive classifications that are correct
                recall (float):  proportion of positive examples that were found
    Returns: a float, the f-measure.
    """
    return (2 * precision * recall)/(precision + recall)
def precision(tp, fp):
    return tp/(tp + fp)
def recall(tp, fn):
    tp/(tp + fn)
    
def f_measures(stats_list):
    """
    Compute f-measure for each item in a list.
    
    Argument: stats_list (list):  a list of tuples of four ints, (tp, fp, tn, fn)
               (these stand for true positive, false positive, etc)
    Returns:  a list of floats, the f-measures.
    """
    out = []
    for tp, fp, tn, fn in stats_list:
        f = f_measure(precision(tp, fp), recall(tp, fn))
        out.append(f)
    return f
print(precision(4,4)) # Expect 0.5
print(recall(4,4)) # Expect 0.5
print(f_measure(1, 1)) # Expect 1
def recall(tp, fn):
    print(tp/(tp + fn))
    
recall(4,4)
def recall(tp, fn):
    print(tp/(tp + fn))
    return tp/(tp + fn)
    
recall(4,4)
def f_measure(precision, recall):
    """
    Compute the f-measure, a performance measure that ignores true negatives.
    
    Arguments:  precision (float):  proportion of positive classifications that are correct
                recall (float):  proportion of positive examples that were found
    Returns: a float, the f-measure.
    """
    return (2 * precision * recall)/(precision + recall)
def precision(tp, fp):
    return tp/(tp + fp)
def recall(tp, fn):
    return tp/(tp + fn)
    
def f_measures(stats_list):
    """
    Compute f-measure for each item in a list.
    
    Argument: stats_list (list):  a list of tuples of four ints, (tp, fp, tn, fn)
               (these stand for true positive, false positive, etc)
    Returns:  a list of floats, the f-measures.
    """
    out = []
    for tp, fp, tn, fn in stats_list:
        f = f_measure(precision(tp, fp), recall(tp, fn))
        out.append(f)
    return f
print(precision(4,4)) # Expect 0.5
print(recall(4,4)) # Expect 0.5
print(f_measure(1, 1)) # Expect 1
print(precision(0, 4)) # Expect 0
print(precision(0, 0)) # Expect ... oh, I guess we didn't think about this.  0?
print(precision(4, 0)) # Expect 1
print(recall(0, 4)) # Expect 0
print(recall(0, 0)) # Similarly to precision, let's return 0
print(recall(4, 0)) # Expect 1
print(f_measure(0, 0)) # Expect 0
print(f_measure(0.5, 0.5)) # Expect 0.5
def f_measure(precision, recall):
    """
    Compute the f-measure, a performance measure that ignores true negatives.
    
    Arguments:  precision (float):  proportion of positive classifications that are correct
                recall (float):  proportion of positive examples that were found
    Returns: a float, the f-measure.
    """
    return (2 * precision * recall)/(precision + recall)
def precision(tp, fp):
    if tp + fp == 0:
        return 0
    return tp/(tp + fp)
def recall(tp, fn):
    if tp + fn == 0:
        return 0
    return tp/(tp + fn)
    
def f_measures(stats_list):
    """
    Compute f-measure for each item in a list.
    
    Argument: stats_list (list):  a list of tuples of four ints, (tp, fp, tn, fn)
               (these stand for true positive, false positive, etc)
    Returns:  a list of floats, the f-measures.
    """
    out = []
    for tp, fp, tn, fn in stats_list:
        f = f_measure(precision(tp, fp), recall(tp, fn))
        out.append(f)
    return f
print(precision(4,4)) # Expect 0.5
print(recall(4,4)) # Expect 0.5
print(f_measure(1, 1)) # Expect 1
print(precision(0, 4)) # Expect 0
print(precision(0, 0)) # Expect 0
print(precision(4, 0)) # Expect 1
print(recall(0, 4)) # Expect 0
print(recall(0, 0)) # Similarly to precision, let's return 0
print(recall(4, 0)) # Expect 1
print(f_measure(0, 0)) # Expect 0
print(f_measure(0.5, 0.5)) # Expect 0.5
def f_measure(precision, recall):
    """
    Compute the f-measure, a performance measure that ignores true negatives.
    
    Arguments:  precision (float):  proportion of positive classifications that are correct
                recall (float):  proportion of positive examples that were found
    Returns: a float, the f-measure.
    """
    if precision + recall == 0:
        return 0
    return (2 * precision * recall)/(precision + recall)
def precision(tp, fp):
    if tp + fp == 0:
        return 0
    return tp/(tp + fp)
def recall(tp, fn):
    if tp + fn == 0:
        return 0
    return tp/(tp + fn)
    
def f_measures(stats_list):
    """
    Compute f-measure for each item in a list.
    
    Argument: stats_list (list):  a list of tuples of four ints, (tp, fp, tn, fn)
               (these stand for true positive, false positive, etc)
    Returns:  a list of floats, the f-measures.
    """
    out = []
    for tp, fp, tn, fn in stats_list:
        f = f_measure(precision(tp, fp), recall(tp, fn))
        out.append(f)
    return f
print(precision(4,4)) # Expect 0.5
print(recall(4,4)) # Expect 0.5
print(f_measure(1, 1)) # Expect 1
print(precision(0, 4)) # Expect 0
print(precision(0, 0)) # Expect 0
print(precision(4, 0)) # Expect 1
print(recall(0, 4)) # Expect 0
print(recall(0, 0)) # Similarly to precision, let's return 0
print(recall(4, 0)) # Expect 1
print(f_measure(0, 0)) # Expect 0
print(f_measure(0.5, 0.5)) # Expect 0.5
# Lecture14Pandas.py
import pandas as pd
import numpy as np
s1 = pd.Series([-3, -1, 1, 3, 5])
print(s1)
print(s1.index)
s1[:2] # First 2 elements
print(s1[[2,1,0]])  # Elements out of order
type(s1)
s1[s1 > 0]
s2 = pd.Series(np.random.rand(5), index=['a', 'b', 'c', 'd', 'e'])
print(s2)
print(s2.index)
print(s2['a'])
data = {'pi': 3.14159, 'e': 2.71828}  # dictionary
print(data)
s3 = pd.Series(data)
print(s3)
my_array = s3.values
print(my_array)
import numpy as np
my_data = np.array([[5, 5, 4], 
                    [2, 3, 4]])
hotels = pd.DataFrame(my_data, index = ["Alice rating", "Bob rating"],
                   columns = ["Hilton", "Marriott", "Four Seasons"])
hotels
from google.colab import files
uploaded = files.upload() # pick starbucks_drinkMenu_expanded.csv
get_ipython().system('ls')
import pandas as pd
df = pd.read_csv('starbucks_drinkMenu_expanded.csv', index_col = 'Beverage')
df.head()
sorted_df = df.sort_values(by = "Calories", ascending=False)
sorted_df.head()
hotels
hotels['Hilton']
sum = 0
for i in hotels['Hilton']:
    sum += i
print('Average Hilton Rating: ' + str(sum/len(hotels['Hilton'])))
hotels.loc['Bob rating']
hotels.loc['Bob rating', 'Marriott']
hotels.iloc[1, 1]
print(hotels.iloc[0, 1:2])
print(hotels.loc['Bob rating', ['Marriott', 'Hilton']])
(df['Calories'] > 300)
df[df['Calories'] > 300].head()
df[(df['Calories'] > 300) & (df['Beverage_prep'] == 'Soymilk')].head()
df['bad_fat'] = df['Trans_Fat_g'] + df['Saturated_Fat_g']
df.head()
size_ounces_dict = {'Short': 8, 'Tall': 12, 'Grande': 16, 'Venti': 20}
ounces_list = []
for drink in df['Beverage_prep']:
    ounces_list.append(size_ounces_dict.get(drink, -1))
df['ounces'] = ounces_list
df.head()
def size_to_ml(size_name):
    size_ounces_dict = {'Short': 8, 'Tall': 12, 'Grande': 16, 'Venti': 20}
    return size_ounces_dict.get(size_name,0) * 29.5735
ml = df['Beverage_prep'].map(size_to_ml)
print(ml)
# Lecture15Pandas.py
import pandas as pd
df = pd.read_csv('starbucks_drinkMenu_expanded.csv', index_col = 'Beverage')
df.head()
print(df.loc[:, "Protein_g"].mean())
print(df.loc[:, "Protein_g"].max())
print(df.loc[:, "Protein_g"].idxmax()) # "argmax," gives index with biggest value
df.describe()
df.corr(numeric_only=True)  # New to pandas 2.0.0: chokes on strings without added arg
df.columns
df.dtypes
string = 'string'
string[:-1]
df['Vitamin_A'] = df['Vitamin_A'].str[0:-1] # Remove the % at the end
df['Vitamin_A']
df['Vitamin_A'] = pd.to_numeric(df['Vitamin_A'])
df.dtypes
df['Vitamin_A'] = df['Vitamin_A'].astype('float64')
df.dtypes
df.corr(numeric_only=True)
df.isnull().sum()
df = df.dropna(axis=0, how="any") # Remove the offending row
df.isnull().sum()
calorie_max = 0
best_name = ""
for index, row in df.iterrows():
  if row['Calories'] > calorie_max:
    calorie_max = row['Calories']
    best_name = index
print(best_name)
protein = df.loc[:, "Protein_g"]
protein.hist(bins=20); # Create a histogram with 20 equally spaced bins for the data
subplot = df[["Protein_g", "Vitamin_A"]] # Notice another way to get desired columns
subplot.boxplot(); # Boxplots give median value, middle 50% of data, and range of non-outliers
from google.colab import files
uploaded = files.upload() # pick titanic.csv
df = pd.read_csv('titanic.csv', index_col = 'PassengerId')
df.head()
df.columns
df.dtypes
df.describe()
df.corr(numeric_only=True)
males = df[df['Sex'] == 'male']
males.head()
males.describe()
females = df[df['Sex'] == 'female']
females.describe()
df['sex_numeric'] = df['Sex'] == 'female'
df.corr(numeric_only=True)
third_class = df[df['Pclass'] == 3]
second_class = df[df['Pclass'] == 2]
first_class = df[df['Pclass'] == 1]
third_class['Survived'].hist();
second_class['Survived'].hist();
first_class['Survived'].hist();
# Lecture16Strings.py
my_cost = 12.95821
print(f'The total cost was {my_cost} dollars')
print(f'The total cost was {my_cost:.2f} dollars')
groceries = "milk,eggs,yogurt"
grocerieslist = groceries.split(',')
print(grocerieslist)
','.join(['milk', 'eggs', 'yogurt'])
'     milk,eggs,yogurt     '.strip()
lines = "SERVANT: Sir, there are ten thousand--\nMACBETH: Geese, villain?"
linelist = lines.splitlines()  # A shortcut for split('\n')
for line in linelist:
  if line.startswith("MACBETH"):
    print(line.split(": ")[1])
print('Wow\n\twow!')
print("foo" in "food")
print("foodfood".replace("foo", "ra"))
import numpy as np
import pandas as pd
my_data = np.array([["Excellent", "   Okay   ", "   Okay"], ["Great    ", "   Good", "   Good"]])
df = pd.DataFrame(my_data, columns = ["Hilton", "Marriott", "Four Seasons"], index = ["Alice", "Bob"])
df
marriott = df['Marriott']
for s in marriott:
    print(s)
print('---')
for s in marriott.str.strip():
    print(s)  # Look, no extra whitespace
marriott.str.match("\s*Okay\s*")
import re
pattern = '02143'
longstring = 'Somerville, MA 02143'
result = re.search(pattern, longstring)
if result:  # (if it's not None)
    print(result.group())
longstring = '0132428190214200'
pattern2 = '02143'
result2 = re.search(pattern2, longstring)
print(result2)
pattern3 = '\d\d\d\d\d'
longstring = 'Somerville, MA 02143'
result3 = re.search(pattern3, longstring)
if result3:
    print(result3.group())
longstring = 'My phone number is 5555555'
pattern4 = 'phone number is \d+'
result4 = re.search(pattern4, longstring)
if result4:
    print(result4.group())
longstring = 'Call me at 555-5555'
pattern5 = '\d\d\d-?\d\d\d\d'
result5 = re.search(pattern5, longstring)
if result5:
    print(result5.group())
longstring = "Call me at 1-800-555-5555."
pattern = "(\d-)?(\d\d\d-)?\d\d\d-?\d\d\d\d"
result = re.search(pattern, longstring)
if result:
    print(result.group())
longstring2 = "Call me at 555-5555."
result = re.search(pattern, longstring2)
if result:
    print(result.group())
pattern = "Somerville, (MA|NJ)"
longstring = "Somerville, NJ 02143"
result = re.search(pattern, longstring)
if result:
    print(result.group())
longstring = "States with a Somerville:  AL, IN, ME, MA, NJ, OH, TN, TX"
pattern = "[A-Z][A-Z]"  # Get capital letters within A-Z range
result = re.findall(pattern, longstring)
print(result)
longstring = "The stock NVDA went down 4.54 points"
pattern = "stock (\w+) went down (\d+\.\d+) points"
result = re.search(pattern, longstring)
if result:
    print(result.group())
    print(result.group(1))  # Subgroup 1, the first () in the pattern
    print(result.group(2))
import re
longstring = "We paid $100 for those shoes"
pattern = '\$\d+'
result = re.search(pattern, longstring)
print(result.group())
# Lecture18Objects.py
class Car:
    pass
car1 = Car()
car2 = Car()
car3 = Car()
print(isinstance(car1,Car))
car1.year = 2010
car1.make = "Honda"
car1.model = "Fit"
car1.color = "blue"
car2.year = 2013
car2.make = "Toyota"
car2.model = "Camry"
car2.color = "silver"
print(f"This car is a {car1.year} {car1.color} {car1.make} {car1.model}")
my_car = (2010, 'Honda', 'Fit', 'blue')
print(f"This car is a {my_car[0]} {my_car[3]} {my_car[1]} {my_car[2]}")
class Car:
    def print_facts(self):
        print(f"This car is a {self.year} {self.color} {self.make} {self.model}")
car1 = Car()
car2 = Car()        
car1.year = 2010
car1.make = "Honda"
car1.model = "Fit"
car1.color = "blue"
car2.year = 2013
car2.make = "Toyota"
car2.model = "Camry"
car2.color = "silver"
car1.print_facts()
car2.print_facts()
class Car:
    def __init__(self, year, make, model, color):
        # It's common for the constructor's arguments
        # to have similar or identical names to the attributes they set
        # (but we still have to say one should be set to the other)
        self.year = year
        self.make = make
        self.model = model
        self.color = color
    
    def print_facts(self):
        print(f"This car is a {self.year} {self.color} {self.make} {self.model}")
car1 = Car(2010, "Honda", "Fit", "blue")
car2 = Car(2013, "Toyota", "Camry", "silver")        
car1.print_facts()
car2.print_facts()
def newest_car(list_of_cars):
    if not list_of_cars:  # ie, empty list
        return None
    best_year = list_of_cars[0].year
    best_car = list_of_cars[0]
    for car in list_of_cars:
        # This warning message could prevent a bug if we try
        # to hand this function the wrong list
        if not isinstance(car, Car):
            print('Warning, list had non-car items!')
        elif car.year > best_year:
            best_year = car.year
            best_car = car
    return best_car
newest_car([car1, car2]).print_facts()
class Bill:
  """ Represents a bill at a restaurant.
  _items (list of tuples):  list of (item name, cost) tuples
  """
  def __init__(self, items):
    self._items = items
  # "Getter"
  def items(self):
    return self._items
  # "Setter"
  def set_items(self, items):
    self._items = items
  
  def total_cost_pretax(self):
    total = 0
    for name, cost in self._items:
      total += cost
    return total
  def total_cost_with_tax(self, tax_rate):
    return round(self.total_cost_pretax() * (1 + tax_rate), 2)
my_lunch = [("Ham Sandwich", 9), ("Coke", 2)]
new_bill = Bill(my_lunch)
cost_with_tax = new_bill.total_cost_with_tax(0.08)
print(f"Total cost: {cost_with_tax}")
new_bill.items() # could have said new_bill._items, but we were told not to
class Bill:
  """ Represents a bill at a restaurant. 
  _item_names (list of strings):  list of items on bill
  _item_costs (list of ints): list of prices of items on bill
  _items is not here anymore! sorry anybody who wrote code that uses it, we warned you!
  """
  def __init__(self, items):
    self._item_names = [item[0] for item in items]
    self._item_costs = [item[1] for item in items]
  # "Getter"
  def items(self):
    # list(zip(a, b)) returns a list of tuples combining a and b
    return list(zip(self._item_names, self._item_costs))
  # "Setter"
  def set_items(self, items):
    self._item_names = [item[0] for item in items]
    self._item_costs = [item[1] for item in items]
  
  def total_cost_pretax(self):
    total = 0
    for name, cost in self._items:
      total += cost
    return total
  # Notice that we can call another method with this one
  def total_cost_with_tax(self, tax_rate):
    return round(self.total_cost_pretax() * (1 + tax_rate), 2)
my_lunch = [("Ham Sandwich", 9), ("Coke", 2)]
new_bill = Bill(my_lunch)
print(new_bill.items())  # this still works, but _items would have broken
class Circle:
  def __init__(self, radius):
    if radius < 0:
      raise ValueError("Can't have negative circle radius")
    self.radius=radius
Circle(-1)
class Circle2:
  def __init__(self,radius=2):
    self.radius = radius
Circle2().radius
class Student:
  def __init__(self, age, major, year):
    self.age = age
    self.major = major
    self.year = year
  
  def get_older(self, amount):
    self.age += amount
bob = Student(20,"Biology","Sophomore")
bob.get_older(2)
print(bob.age)
car1 = Car(2010, "Honda", "Fit", "blue")
car2 = car1
car2.color = "black"
car1.print_facts()  # It's black now
car2.print_facts()
import copy
car2 = copy.copy(car1)
car2.color = "white"
car1.print_facts()
car2.print_facts()
from google.colab import files
uploaded = files.upload() # import books.csv
import pandas as pd
df = pd.read_csv('books.csv', index_col = 'title')
df.head()
class Book:
    def __init__(self, title, author, average_rating):
        self.title = title
        self.author = author
        self.average_rating = average_rating
        # Could add more fields from the dataset if desired
    
class Publisher:
    def __init__(self, df, publisher_name):
        self.name = publisher_name
        self.books = []
        for row in df.itertuples():
            if row.publisher == publisher_name:
                self.books.append(Book(row.Index, row.authors, row.average_rating))
    
    def average_rating(self):
        total = 0
        for book in self.books:
            total += book.average_rating
        return total/len(self.books)
scholastic = Publisher(df,'Scholastic Inc.')
scholastic.average_rating()
# Lecture19MoreOO.py
class Client:  # both Faculty and Students
  def __init__(self, birthyear, uid):
    self.birthyear = birthyear
    self.uid = uid
  def get_uid(self):
    return self.uid
  
  def get_birthyear(self):
    return self.birthyear
class Student(Client):  # inherit from Client
  def __init__(self, birthyear, uid, gradyear):
    self.birthyear = birthyear
    self.uid = uid
    self.gradyear = gradyear
  def get_gradyear(self):
    return self.gradyear
    
class Faculty(Client):
  pass     # Nothing else we want to do for Faculty
   
alice = Student(2003, 123456789, 2024)
print(alice.get_birthyear()) # Inherited from Client
print(alice.get_uid())       # Inherited from Client
print(alice.get_gradyear())  # Specific to Student
person1 = Student(2000,123456,2025)
if not isinstance(person1, Faculty):
    print("Hey, this person doesn't have permission to do this!")
else:
    print("Welcome, Faculty number " + str(person1.uid) + "!")
student1 = Student(2000,123456,2025)
print(isinstance(student1,Student))
print(isinstance(student1,Client))
print(isinstance(student1,object)) # Every class inherits from object
class Student(Client):  # inherit from Client
  def __init__(self, birthyear, uid, gradyear):
    super().__init__(birthyear, uid)
    self.gradyear = gradyear
  def get_gradyear():
    return self.gradyear
bob = Student(2002,987654321,2022)
print(bob.get_uid()) # inherited from Client
class Trip:
  def __init__(self,cost,start_date,end_date):
    self.cost = cost
    self.start_date = start_date
    self.end_date = end_date
    self.reimbursed = False
  def cost(self):
    return self.cost
  
  def reimburse(self):
    self.reimbursed = True
  
  def dates(self):
    return self.startDate, self.endDate
class EquipmentOrder:
  def __init__(self,cost,domestic_seller):
    self.cost = cost
    self.reimbursed = False
    self.domestic_seller = domestic_seller
  def cost(self):
    return self.cost
  
  def reimburse(self):
    self.reimbursed = True
  
  def domestic_seller(self):
    return self.domestic_seller
class Expense:
  def __init__(self,cost):
    self.cost = cost
    self.reimbursed = False
  
  def cost(self):
    return self.cost
  
  def reimburse(self):
    self.reimbursed = True
class Trip(Expense):
  def __init__(self,cost,start_date,end_date):
    super().__init__(cost)
    self.start_date = start_date
    self.end_date = end_date
  
  # inherit cost, reimburse
  def dates(self):
    return self.start_date, self.end_date
class EquipmentOrder(Expense):
  def __init__(self,cost,domestic_seller):
    super().__init__(cost)
    self.domestic_seller = domestic_seller
  # inherit cost, reimburse
  def domestic_seller(self):
    return self.domestic_seller
class Employee:
    def __init__(self, name, salary, title, years_of_service):
        self.name = name
        self.salary = salary
        self.title = title
        self.years_of_service = years_of_service
    
    def give_raise(self, raise_amount):
        self.salary += raise_amount
        
    def change_title(self, new_title):
        self.title = new_title
    
    def update_years_of_service(self, increase):
        self.years_of_service += increase
class Contractor:
    def __init__(self, name, salary, contract_duration):
        self.name = name
        self.salary = salary
        self.contract_duration = contract_duration
    
    def give_raise(self, raise_amount):
        self.salary += raise_amount
    
alice = Employee("Alice", 90000, "Manager", 7)
alice.give_raise(10000)
print(alice.salary)
bob = Contractor("Bob", 80000, 2)
bob.give_raise(10000)
print(bob.salary)
class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def give_raise(self, raise_amount):
        self.salary += raise_amount
    
class Employee(Worker):
    def __init__(self, name, salary, title, years_of_service):
        super().__init__(name, salary)
        self.title = title
        self.years_of_service = years_of_service
        
    def change_title(self, new_title):
        self.title = new_title
    
    def update_years_of_service(self, increase):
        self.years_of_service += increase
class Contractor(Worker):
    def __init__(self, name, salary, contract_duration):
        super().__init__(name, salary)
        self.contract_duration = contract_duration
        
alice = Employee("Alice", 90000, "Manager", 7)
alice.give_raise(10000)
print(alice.salary)
bob = Contractor("Bob", 80000, 2)
bob.give_raise(10000)
print(bob.salary)
class Gradyear:
  def __init__(self, year):
    self.year = year
year = Gradyear(2024)
print(year)
class Gradyear:
  def __init__(self, year):
    self.year = year
  def __str__(self):    # Our own implementation
    return str(self.year)
gradyear = Gradyear(2024)
print(gradyear)
gy1 = Gradyear(2024)
gy2 = Gradyear(2024)
print(gy1 == gy2)
myset = set()
myset.add(gy1)
myset.add(gy2)
len(myset)
class Gradyear:
  def __init__(self, year):
    self.year = year
  def __str__(self):    # Our own implementation
    return str(self.year)
  
  def __eq__(self, other):
    return self.year == other.year
  def __hash__(self):
    return self.year # Just store by number itself
gy1 = Gradyear(2024)
gy2 = Gradyear(2024)
print(gy1 == gy2)
myset = set()
myset.add(gy1)
myset.add(gy2)
len(myset)
# Lecture20Recursion.py
def bad_recursion():
  print("Bad!")
  bad_recursion()
bad_recursion()
def factorial(n):
  # Omitting checks to make sure we're a natural number, etc
  if n == 1:
    return 1
  return n * factorial(n-1)
print (factorial(4))
def factorial(n):
  # Omitting checks to make sure we're a natural number, etc
  print(f'Evaluating {n}!')
  if n == 1:
    print('Returning 1')
    return 1
  result = n * factorial(n-1)
  print(f'Returning {result}')
  return result
print (factorial(4))
def sum_m_to_n(m, n):
    if n == m:
        return m
    result = n + sum_m_to_n(m, n-1)
    return result
sum_m_to_n(3, 7) # 3 + 4 + 5 + 6 + 7 = 25
def sum_m_to_n(m, n):
    print(f'Evaluating sum from {m} to {n}')
    if n == m:
        print(f'Returning {m}')
        return m
    result = n + sum_m_to_n(m, n-1)
    print(f'Returning {result}')
    return result
sum_m_to_n(3, 7) # 3 + 4 + 5 + 6 + 7 = 25
def mypow(a, p):
    if p == 0:
        return 1
    result = a * mypow(a, p-1)
    return result
mypow(2,8)
def mypow(a, p):
    print(f'Evaluating {a}^{p}')
    if p == 0:
        print('Returning 1')
        return 1
    result = a * mypow(a, p-1)
    print(f'Returning {result}')
    return result
mypow(2,8)
def fib(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fib(n-1) + fib(n-2)
for i in range(10):
    print(fib(i))
def r_perm(r, n):
    if n == r+1:
        return n
    return n * r_perm(r,n-1)
r_perm(5,7)
def iter_factorial(n):
  running_fact = 1
  for i in range(1,n+1):
    running_fact *= i
  return running_fact
  
print(iter_factorial(4))
import numpy as np
def iter_fib(n):
    if n == 0 or n == 1:
        return n
    fibs = np.zeros(n+1)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2,n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return int(fibs[n])
for i in range(10):
    print(iter_fib(i))
def power_set(setstring):
    if len(setstring) == 0:
        return [""]
    subset_list = []
    # Recursive call gets all the subsets that don't involve the first character
    smaller_power_set = power_set(setstring[1:])
    # The starting character is either in the subset...
    for substring in smaller_power_set:
        subset_list.append(setstring[0] + substring)
    # ...or not.
    for substring in smaller_power_set:
        subset_list.append(substring)
    return subset_list
power_set("abcd")
def recursive_sum(lst):
    if not lst:  # empty list
        return 0
    return lst[0] + recursive_sum(lst[1:])
recursive_sum([1,2,3])
def recursive_filter(min_val, lst):
    if not lst:
        return []
    if lst[0] >= min_val:
        return [lst[0]] + recursive_filter(min_val, lst[1:])
    else:
        return recursive_filter(min_val, lst[1:])
recursive_filter(3, [1, 2, 3, 4, 5])
def recursive_index(item, lst, index):  # index tracks where we are in the list
    if not lst:
        return None   # not found
    if lst[0] == item:
        return index
    return recursive_index(item,lst[1:],index+1)
recursive_index(5, [0, 1, 2, 5], 0)
def recursive_skiplist(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    return [lst[0]] + recursive_skiplist(lst[2:])
recursive_skiplist([5,3,7,2,9])
# Lecture21DataStructures.py
class ll_node:
  def __init__(self, num):
    self.number = num
    self.next = None
  def append(self, num):
    if self.next == None:     # End of the list - add the node
      self.next = ll_node(num)
    else:
      self.next.append(num) # Recursively append to rest of list
    
  def contains(self, othernum):
    if self.number == othernum:  # We found it
      return True
    elif self.next == None:  # We reached the end, didn't find it
      return False
    # Not here, there's more list - so, keep looking (recursively)
    return self.next.contains(othernum)
  def __str__(self):
    if self.next == None:  # Last number
        return str(self.number)
    # Print this and print the rest (more recursion)
    return str(self.number) + ' ' + str(self.next)
mylist = ll_node(6)
mylist.append(1)
mylist.append(7)
print(mylist)
print('Contains 7: ' + str(mylist.contains(7)))
print('Contains 5: ' + str(mylist.contains(5)))
import numpy as np
class dynamic_array:  # Showing how Python lists work
  def __init__(self, initial_size):
    self.memory = np.zeros(initial_size)
    self.occupied = 0
    self.size = initial_size
  def __str__(self):
    return str(self.memory)
  
  def append(self, val):
    if self.occupied == self.size:
      print('Resizing...')
      new_memory = np.zeros(self.size*2)
      # A "hiccup" in running time as everything's copied
      for i in range(len(self.memory)): 
        new_memory[i] = self.memory[i] 
      self.memory = new_memory
      self.size = self.size*2
    print('Adding ' + str(val))
    self.memory[self.occupied] = val
    self.occupied += 1
my_array = dynamic_array(2)
print(my_array)
my_array.append(1)
my_array.append(1)
print(my_array)
my_array.append(1)
print(my_array)
my_array.append(1)
print(my_array)
class FolderTree:
  # binary left and right are its fields
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val
  
  def addLeft(self, node):
    self.left = node
  
  def addRight(self, node):
    self.right = node
  
  def find(self, v):
    if self.val == v:
      return True
    # "if self.left" is checking that self.left exists - 
    # else error when we run self.left.find()
    if self.left and self.left.find(v):
      return True
    if self.right and self.right.find(v):
      return True
    return False
leftleftchild = FolderTree("wow.exe")
leftrightchild = FolderTree("xls.exe")
rightleftchild = FolderTree("lec12.pdf")
rightrightchild = FolderTree("lec14.pdf")
leftparent = FolderTree("apps")
rightparent = FolderTree("lecs")
leftparent.addLeft(leftleftchild)
leftparent.addRight(leftrightchild)
rightparent.addLeft(rightleftchild)
rightparent.addRight(rightrightchild)
root = FolderTree("root")
root.addLeft(leftparent)
root.addRight(rightparent)
print(root.find("wow.exe"))
print(root.find("lec13.exe"))
def count_nodes(tree):
    if tree == None:
        return 0
    return 1 + count_nodes(tree.left) + count_nodes(tree.right)
count_nodes(root)
def calc_depth(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 0  # Leaf has depth 0 in its subtree
    return 1 + max(calc_depth(tree.left), calc_depth(tree.right))
calc_depth(root)
class BinarySearchTree:
  # binary left and right are its fields
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val
  
  def addLeft(self, node):
    self.left = node
  
  def addRight(self, node):
    self.right = node
  
  def find(self, v):
    if self.val == v:
      return True
    if v < self.val:
      if self.left:
        print("Going Left")
        return self.left.find(v)
      else:
        return False
    else:
      if self.right:
        print("Going Right")
        return self.right.find(v)
      else:
        return False
root = BinarySearchTree("m")
leftparent = BinarySearchTree("f")
rightparent = BinarySearchTree("q")
leftleftchild = BinarySearchTree("a")
leftrightchild = BinarySearchTree("h")
rightleftchild = BinarySearchTree("o")
rightrightchild = BinarySearchTree("u")
leftparent.addLeft(leftleftchild)
leftparent.addRight(leftrightchild)
rightparent.addLeft(rightleftchild)
rightparent.addRight(rightrightchild)
root.addLeft(leftparent)
root.addRight(rightparent)
print(root.find("h"))
print(root.find("d"))
class infect_tree:
    # name is a string, infects is a list of infect_tree's infected
    def __init__(self, name, infects):
        self.name = name
        self.infects = infects
jake = infect_tree('jake', [])
eric = infect_tree('eric', [])
fifi = infect_tree('fifi', [])
ged = infect_tree('ged', [])
hao = infect_tree('hao', [])
idris = infect_tree('idris', [jake])
bob = infect_tree('bob', [eric])
che = infect_tree('che', [])
daphne = infect_tree('daphne', [fifi, ged, hao, idris])
alice = infect_tree('alice', [bob, che, daphne])
def find_most_infections(my_tree):
    best_infects = len(my_tree.infects)
    best_name = my_tree.name
    for infect in my_tree.infects:
        name, infects = find_most_infections(infect) # Recursion...
        if infects > best_infects:
            best_infects = infects
            best_name = name
    return best_name, best_infects
find_most_infections(alice)
def find_all_descendants(my_tree):
    my_list = [my_tree.name]
    for infect in my_tree.infects:
        my_list += find_all_descendants(infect)  # More recursion
    return my_list
find_all_descendants(daphne)
# Lecture22ScikitLearn.py
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()
print(digits.data.shape) # Examples x 64 pixels
import matplotlib.pyplot as plt 
plt.gray() 
plt.matshow(digits.images[0]) # Notice images[0] is 2D
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
from sklearn.neighbors import KNeighborsClassifier
nbrs = KNeighborsClassifier(n_neighbors=3).fit(digits.data, digits.target)
nbrs.score(digits.data, digits.target) # Find accuracy on the training dataset
from sklearn.model_selection import train_test_split
data_train, data_test, label_train, label_test = train_test_split(digits.data, digits.target, test_size=0.2)
nbrs = KNeighborsClassifier(n_neighbors=3).fit(data_train, label_train)
nbrs.score(data_test,label_test)
print(nbrs.predict(data_test[0:3]))
def reshape_and_show(num, data_test):
    image = data_test[num].reshape(8,8)
    plt.matshow(image)
reshape_and_show(0,data_test)
reshape_and_show(1,data_test)
reshape_and_show(2,data_test)
from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people(min_faces_per_person = 100)
plt.imshow(faces.images[5], cmap="gray")
data_train, data_test, label_train, label_test = train_test_split(faces.data, faces.target, test_size=0.2)
nbrs = KNeighborsClassifier(n_neighbors=3).fit(data_train, label_train)
 
nbrs.score(data_test,label_test)
import random
random.seed(110)  # Set seed - comment this out to get different rolls
print(random.randint(1,8))  # Normally produces random integer 1-8
print(random.randint(1,8))
data_train, data_test, label_train, label_test = train_test_split(faces.data,
                                                                  faces.target, test_size=0.2,
                                                                  random_state=110) # Set the seed
nbrs = KNeighborsClassifier(n_neighbors=3).fit(data_train, label_train)
 
nbrs.score(data_test,label_test)
from sklearn.model_selection import cross_val_score
cross_val_score(nbrs, data_train, label_train)
import numpy as np
for i in range(1,10):
  nbrs = KNeighborsClassifier(n_neighbors=i)
  print(np.mean(cross_val_score(nbrs, data_train, label_train)))
# Lecture23DecisionTrees.py
import math
yes_branch_entropy = 0
no_branch_entropy = -0.2 * math.log(0.2,2) - 0.8 * math.log(0.8, 2)
pr_yes = 5/2005
pr_no = 2000/2005
print(pr_yes * yes_branch_entropy + pr_no * no_branch_entropy)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
iris = load_iris()
iris.feature_names
iris.target_names
iris.data[0]
features_train, features_test, labels_train, labels_test = \
train_test_split(iris.data, iris.target, test_size=0.1, random_state=110)
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
dtree = DecisionTreeClassifier(criterion="entropy", random_state=110)
dtree.fit(features_train, labels_train)
dtree.score(features_test, labels_test) # Gives accuracy
import matplotlib.pyplot as plt
from sklearn import tree
plt.figure(figsize=(14,10))
tree.plot_tree(dtree, feature_names = iris.feature_names, class_names = iris.target_names)
# Lecture24RandomForestsOnly.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
iris = load_iris()
iris["feature_names"]
features_train, features_test, labels_train, labels_test = \
  train_test_split(iris['data'], iris['target'],
                   test_size=0.1,random_state=110)
irisforest = RandomForestClassifier(n_estimators=200,criterion="entropy",random_state=110)
irisforest.fit(features_train, labels_train)
irisforest.score(features_test, labels_test)
irisforest.feature_importances_
# Lecture25Regression.py
import numpy as np
x = np.linspace(1984, 2016, 33)
y = [48.0, 47.3, 47.2, 47.4, 47.2, 46.7,
     49.7, 49.6, 46.4, 47.3, 47.7, 47.8, 47.3, 47.4, 50.4, 49.8, 
     47.5, 49.1, 49.4, 47.1, 47.6, 48.4, 50.1, 48.3, 48.6, 47.8,
     50.4, 49.7, 51.4, 48.8, 47.7, 48.5, 50.3]
import matplotlib.pyplot as plt
plt.plot(x,y,'o')
import sklearn.linear_model as lm
from sklearn.linear_model import LinearRegression
linear_model = LinearRegression()
x = x.reshape(-1,1)
linear_model.fit(x,y)
y_hat = linear_model.predict(x)
plt.plot(x,y,'o')
plt.plot(x,y_hat,'r')
print(f'The temperature is rising {linear_model.coef_[0]:.4f} degrees F per year')
print(f'{linear_model.intercept_:.2f}')
linear_model.score(x,y)
methane = np.array([12.81, 25.15, 38.06, 49.47, 60.24, 71.32,
     80.08, 94.14, 96.49, 100.32, 107.54, 111.50, 113.97, 120.26, 132.39, 134.82,
     133.30, 132.60, 135.91, 140.65, 135.76, 136.14, 138.11, 145.90, 152.41, 157.13,
     162.33, 167.15, 172.17, 177.86, 190.62, 200.65, 207.73])
mass_co = [84, 82.7, 84.9, 81.7, 81.9, 79.2, 79.9, 85.9, 84.3, 81.9,
           82.9, 82.8,83.7, 85, 83.6, 85, 77.1, 80.4, 77.2, 70.6,
           72.0, 68.1, 61.9, 65.7, 63.8, 65.6, 63.9]
y_from_90 = y[6:]  # From the last example, these are the temperatures
methane_from_90 = methane[6:]
x = np.transpose(np.array([mass_co, methane_from_90]))
x
temp_model = LinearRegression()
temp_model.fit(x,y_from_90)
print(temp_model.coef_)
print(temp_model.intercept_)
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import matplotlib.pyplot as plt
model = DecisionTreeRegressor() # no pruning of any kind, so expect overfitting
x = np.linspace(1984, 2016, 33)
x = x.reshape(-1,1)
y = [48.0, 47.3, 47.2, 47.4, 47.2, 46.7,
     49.7, 49.6, 46.4, 47.3, 47.7, 47.8, 47.3, 47.4, 50.4, 49.8, 
     47.5, 49.1, 49.4, 47.1, 47.6, 48.4, 50.1, 48.3, 48.6, 47.8,
     50.4, 49.7, 51.4, 48.8, 47.7, 48.5, 50.3]
xtrain = x[:30]
ytrain = y[:30]
model.fit(xtrain,ytrain)
yhat = model.predict(x)
plt.plot(x,y,'o')
plt.plot(x[:30],yhat[:30])
plt.plot(x[29:],yhat[29:],'r') # Plot line to test predictions in red
model = DecisionTreeRegressor(max_depth = 3) # maybe overdoing it on the pruning
x = np.linspace(1984, 2016, 33)
prev_value_features = [0] + y.copy()[:-1] # shift y values so we see the previous one; discard last
combined_features = np.array([x, prev_value_features]).transpose()
print(combined_features)
xtrain = combined_features[:30,:]
model.fit(xtrain,ytrain)
yhat = model.predict(combined_features)
plt.plot(x,y,'o')
plt.plot(x[:30],yhat[:30])
plt.plot(x[29:],yhat[29:],'r')
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(xtrain,ytrain) # xtrain has the matrix we made in the previous code box
yhat = model.predict(combined_features)
plt.plot(x,y,'o')
plt.plot(x[:30],yhat[:30])
plt.plot(x[29:],yhat[29:],'r')
from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=3)
model.fit(xtrain,ytrain) # xtrain has the matrix we made in the previous code box
yhat = model.predict(combined_features)
plt.plot(x,y,'o')
plt.plot(x[:30],yhat[:30])
plt.plot(x[29:],yhat[29:],'r')
# Lecture26ModernNLPandML.py
import pandas as pd
SST2_LOC = 'https://github.com/clairett/pytorch-sentiment-classification/raw/master/data/SST2/train.tsv'
df = pd.read_csv(SST2_LOC, delimiter='\t', header=None)
df
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt') # Name means 'period' in German; from Kiss and Strunk 2006
word_tokenize("I won't sell my cat for even $1,000,000,000.") 
def wordset(raw_text):
  tokenized = word_tokenize(raw_text.lower())
  return set(tokenized)
def all_words_set(df_column):
  set_of_all = set()
  dict_of_all = {}
  for row in df_column:
    textset = wordset(row)
    set_of_all = set_of_all.union(textset)
    dict_of_all[row] = textset
  return set_of_all, dict_of_all
def one_hot_columns(df_column):
  all_words, all_tokenizations = all_words_set(df_column)
  word_dict = {}
  for word in all_words:
    word_present_list = []
    for line_num in range(len(df_column)):
      if word in all_tokenizations[df_column[line_num]]:
        word_present_list.append(1)
      else:
        word_present_list.append(0)
    word_dict[word] = word_present_list
  # We can create a dataframe from a dictionary of column header
  # to list of column values
  return pd.DataFrame.from_dict(word_dict)
one_hot_cols = one_hot_columns(df.iloc[:,0])
one_hot_cols
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
labels = df[1]
features = one_hot_cols
X_train, X_test, y_train, y_test = train_test_split(features, labels, random_state=42)
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
one_hot_cols.sum()
import gensim.downloader as api
wv = api.load('word2vec-google-news-300')
wv['king']
print(wv.most_similar('king')) # Prints words and cosines of angles with 'king'
import numpy as np
def find_cosine(vec1, vec2):
  # Scale vectors to both have unit length
  unit_vec1 = vec1/np.linalg.norm(vec1)
  unit_vec2 = vec2/np.linalg.norm(vec2)
  # The dot product of unit vectors gives the cosine of their angle
  return np.dot(unit_vec1,unit_vec2)
print(find_cosine(wv['king'], wv['faucet']))
wv.similarity('king', 'faucet')
def find_avg_vector(txt, embedding):
  words = word_tokenize(txt)
  vec_sum = None
  count = 0
  for word in words:
    if word in embedding:
      count += 1
      if vec_sum is not None:
        vec_sum += embedding[word]
      else:
        # The embeddings are read-only unless you copy them
        vec_sum = embedding[word].copy()
  if vec_sum is None:
    return pd.Series(np.zeros((300,)))  # Treat no word found in embedding as zero vector
  return pd.Series(vec_sum/count)
find_avg_vector('Long live the king and queen!', wv)
df_embeddings = df[0].apply(lambda txt: find_avg_vector(txt, wv))
df_embeddings.rename(columns=lambda x: 'feature'+str(x), inplace=True)
df_augmented = pd.concat([df, df_embeddings], axis=1)
df_augmented
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
labels = df_augmented[1]
features = df_augmented.iloc[:,2:]
X_train, X_test, y_train, y_test = train_test_split(features, labels, random_state=42)
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train, y_train)
clf.score(X_test, y_test)