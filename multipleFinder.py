mult_find = input("Please enter a number to find it's multiples")

count = 0

check = 2

other_factor = 0

mult_find = int(mult_find)


while True:
    count = count + 1

    if (mult_find % check) != 0:
        check = check + 1
    else:
        break
other_factor = mult_find / check
print("Number of iterations:" + str(count))
print("The multiples are: " + str(int(other_factor)) + " and " + str(check))
