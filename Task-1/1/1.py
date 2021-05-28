file = input("Enter the filename(with file extension): ")
with open(file,'r') as cf:
    content = cf.readlines()
numbers = []
for i in range(len(content)):
    word = ""
    j=0
    while content[i][j] !='\n':
        word += content[i][j]
        j+=1
        if j == len(content[i]):
            break
    numbers.append(float(word)) #= float(word)
    # print(numbers[i])    
small = numbers[0]
large = numbers[0]
total = 0
for i in range(len(numbers)):
    if(numbers[i]>large):
        large = numbers[i]
    elif(numbers[i]<small):
        small = numbers[i]

    total += numbers[i]
print("Minimum: " + str(small))
print("Maximum: " + str(large))
print("Average: " + str(total/len(numbers)))