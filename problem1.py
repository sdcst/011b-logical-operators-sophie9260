#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "true" if it is
divisible by 6, but not divisible by 8.
State whether the number is "true" 
(2 marks)

Inputs:
a number

Outputs:
xx is true
xx is not true

example:
Enter a number: 48
48 is not true

Enter a number: 36
36 is true

Enter a number: 16
16 is not true
"""
n = input("Enter a number of your choice.")
n = float(n)

six = n/6
six = round(six)
check = six*6

eight = n/8
eight = round(eight)
verify = eight*8

if n == check and n != verify:
    print(f"{n} is true")
else:
    print(f"{n} is not true")

