#function below converts an int into a binary number
def toBinary(numb):
    for i in range(7, -1, -1):
        if 2**i <= numb:
            bin_num[i] = 1
            numb = numb - 2**i
    bin_num.reverse()
print("This program converts decimal numbers to binary numbers up to 8 bits")

while True:
    to_convert = input("Enter an integer:")
    if int(to_convert) > 255 or int(to_convert) < 0:
        print("Please enter a number less than 255 and greater than 0")
    else:
        break

bin_num = [0,0,0,0,0,0,0,0]

print(to_convert)
toBinary(int(to_convert))
print(bin_num)