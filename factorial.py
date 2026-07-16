num = int(input("Enter a non-negative integer: "))
if num < 0:
	print("Invalid input")
else:
	fact = 1
	for i in range(2, num + 1):
		fact *= i
	print(f"{num}! = {fact}")

