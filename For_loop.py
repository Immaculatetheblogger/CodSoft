text = "Hello"
for i in text
reverse.text()

 Example 1: counts the number of vowels in a word
word = "Animal".lower()
word = "I am a student".lower()

word = str(input("Enter a statement:")).lower()
count = 0
for i in word:
	if i not in ("aeiou"):
		print(i, end=' ')
		count = count + 1
		#print( i)
print(f"\n {count}")
		
		
number = range(1,11)

Example 2: Nested loops - Pyramid pattern
n = 5
for i in range(n):
    for j in range(i + 1):
        print('*', end=" ")
    print()


 Example 3: Fibonacci Sequence
n = 10
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b
    
    
Example 4: add all numbers in a list
def total_num(n):
 	total_sum = 0
 	for i in n:
 		total_sum = total_sum + i
 	return total_sum
 	
total_num((8, 5, 12, 6.5, 30))


Example 5: add all numbers in n range
def sum_of_num(n):
	sum_total = 0
	for i in range(1, n):
		sum_total = sum_total + i
	return sum_total
	

 Example 6: Print the multiplication of a given number 'n'' from 1 to 12 using a 'for' loop

n = 8
num = range(1,13)
for i in num:
	#prod = n * i
	print(f"{n} * {i} == {n*i}")
	
 Example 7: Print the multiplication of a given number 'n'' from 1 to 12 using a 'while' loop
n = 8
i = 0
while i < 13:
		#i = i + 1
		print(f"{n} * {i} == {n*i}")
		i += 1

Example 8: Write a for loop that takes a string as input and prints it in reverse order
Reverse a string:
	
text = "Python programming is fun"
reversed_text = ""
for char in text:
	reversed_text = char + reversed_text
print(reversed_text)


Checks whether a number is a prime:
def prime_num(num):
	if num <= 1:
		return False
	else:
		for x in range(2, num):
			if num % x == 0:
				return False
			return False
			
print(prime_num(11))


"More efforts on this nested function"
def prime_num(num):
	def num_prime(num):
		    if num <= 1:
		    	return False
		    else:
		           for x in range(2, num):
			              if num % x == 0:
				                 return False
				   #return True
		    return num_prime(num)

num_prime(num)	
print(prime_num(56))

Finding prime numbers: Using CHAT-GPT
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num)


name = "Amaka"
new_name = reversed(name)
print(new_name)	

	    
