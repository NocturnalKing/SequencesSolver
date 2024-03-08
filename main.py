# Arithmetic
def arithmetic():
	diff = int(input("What is the common difference? "))
	termX = int(input("What is one of the numbers given to you? "))
	x = int(input("What was the index of that number? "))
	n = int(input("What is the index you want to solve for? "))
	termN = (n-x)*diff + termX
	print(f"The {n}th term of your sequence is", termN)

# Geometric
def geometric():
	num = float(input("What is the first number you know? "))
	xTerm = int(input("What term was that number? "))
	ratio = float(input("What is the common ratio? "))
	term = int(input("What term are you tring to solve for? ")) - xTerm
	print(f"The {term}th term of your sequence is", num*(ratio**term))

# Arithmetic Sum 
def arithSum():
	total = float(input("What is the first term of the series? "))
	inter = int(input("How many term are in this series? ")) + 1
	diff = float(input("What is the common difference? "))
	for i in range(1,inter):
		total += i*diff
		print("The sum is", total)

# Geometric Sum
def geoSum():
	start = float(input("What is the first term of the series? "))
	ratio = float(input("What is the common ratio? "))
	num = int(input("How many terms are in the series? "))
	a = start*(1-ratio**num)
	b = 1 - ratio
	c = a/b
	print("The sum is", c)

# Choice 
print("""
Do you want to: 
	a - Find a term in an arithmetic series
	b - Find a term in an geometric series
	c - Find the sum of an arithmetic series
	d - Find the sum of a geometic series""")
choice = input("Type a,b,c, or d: ").lower()
while choice not in ["a","b","c","d"]:
	choice = input("That wasn't a valid input. \nType a, b, c, or d: ").lower()
if choice == "a":
	arithmetic()
elif choice == "b":
	geometric()
elif choice == "c":
	arithSum()
elif choice == "d":
	geoSum()
