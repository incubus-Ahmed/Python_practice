#This program can +,-,* and / any two numbers

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Enter the operation you want to perform (add, subtract, multiply, divide): ").strip().lower()

if operation == "add":
	result = first_number + second_number
	op_text = "addition"
elif operation == "subtract":
	result = first_number - second_number
	op_text = "subtraction"
elif operation == "multiply":
	result = first_number * second_number
	op_text = "multiplication"
elif operation == "divide":
	if second_number != 0:
		result = first_number / second_number
		op_text = "division"
	else:
		print("Error: Cannot divide by zero.")
		result = None
		op_text = "division"
else:
	print("Invalid operation selected.")
	result = None
	op_text = operation

if result is not None:
	print(f"The {op_text} for {first_number} and {second_number} is {result}")
