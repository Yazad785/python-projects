start = int(input("Enter the start if the range:  "))
end = int(input("Enter the end of the range:  "))
for num in range(start, end + 1):
    if num >= 0:
        print(num, end = " ")
