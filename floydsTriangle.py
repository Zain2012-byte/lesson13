rows=int(input("Enter the number of rows:"))

number = 1 #initialise by 1

print("Floyd`s` triangle")

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(number, end=' ')
        number+=1
    print()