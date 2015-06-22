# Problem 1

    # My solution

x = 0
while (x <= 10):
    x += 2
    print x
print 'Goodbye!'

    # Best practice

num = 2
while num < 11:
    print num
    num += 2
print "Goodbye!"

# Problem 2

print "Hello!"

num = 10
while num > 0:
    print num  # print the num first
    num -= 2

# Problem 3

total = 0
current = 1

while current <= end:

    total += current # total = total + current, 1
    current += 1 # 1st, current = 2

print total

# Finding the cube root of some number

x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
  
  # problem 1 to 3

myStr = '6.00x'

for char in myStr:
    print char

print 'done' 

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print letter 
    print letter # this line means the letter will get printed anyway

print 'done'

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons) 


count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count 

# Compare to this one:

num = 10
for var in range(5):
    print var
print num 

for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!' 
        
# L3 PROBLEM 5A

# 1

for var in range(2, 12, 2):
    print var
print 'Goodbye!'

# 2

print 'Hello!'
for var in reversed(range(2, 12, 2)):
    print var
    
# 3

# Example:

total = 0
current = 1

while current <= end:

    total += current # total = total + current, 1
    current += 1 # 1st, current = 2

print total

total = 0
for var in range(1,end+1):
    total += var
    # print total this is printing total in the for loop
print total # this is printing total at the end for once. 

# L3 PROBLEM 6

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1 # count get added for each letter in the string hello world
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 
    
iteration = 0
while iteration < 5:
    count = 0 # This reset count back to 0 at the begining of every interation
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 
    
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 
    
    
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
        break
        
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print "Iteration " + str(iteration) + "; count is: " + str(count)

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)

# Finding the sqrt of a num

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)
    
# L3 PROBLEM 9

print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)/2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))