# Print all integers from 0 to 150.
for x in range (150):
    print(x)

#Print all the multiples of 5 from 5 to 1,000
for x in range (5 , 1000 , 5):
    print(x)



# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
num = 0
for i in range(0,100):
    num+=1
    print(num)
    if num % 5 == 0:
        print("Coding")
    elif num % 10 ==0:
        print("Coding Dojo")

# Add odd integers from 0 to 500,000, and print the final sum.
odd_num = 0

for i in range(0, 500001):
    if(i % 2 != 0):
        print("{0}".format(i))
        odd_num = odd_num + i

print("sum of Odd Numbers from 1 to {0} = {1}".format(i, odd_num))

#Print positive numbers starting at 2018, counting down by fours

for i in range(2018 , 0 , -4):
    print(i)