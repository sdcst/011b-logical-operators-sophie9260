#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple (a**2 + b**2 = c**2)
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""


i = input("Enter an integer.")
i = int(i)
ii = input("Enter another integer.")
ii = int(ii)
iii = input("Enter another integer.")
iii = int(iii)

BN = max(i,ii,iii)
print(BN)

SN = min(i,ii,iii)
print(SN)

mn = (BN**2) - (SN**2)
MN = mn**0.5
print(MN)

OG = BN + SN
t = i + ii + iii
middle = t - OG

if MN == i or MN == ii or MN == iii:
    print(f"{SN}, {MN}, {BN} form a Pythagorean triple.")
elif MN != i or MN != ii or MN != iii:
    print(f"{SN}, {middle}, {BN} do not form a Pythagorean triple.")


"""
2 4 5            2+4+5=11  11-max=6
2 5 4            2+5+4=11  11-max=6   
"""