file1 = "input1.txt" #input("Enter first file")
file2 = "input2.txt" #input("Enter second file")
with open(file1,'r') as rf1:
    with open(file2,'r') as rf2:
        with open("output.txt",'w') as wf:
            numbers1 = rf1.readlines()
            numbers2 = rf2.readlines()
            for i in range(len(numbers1)):
                if(i==len(numbers1)-1):
                    numbers1[i] = int(numbers1[i][:len(numbers1[i])])
                else:
                    numbers1[i] = int(numbers1[i][:len(numbers1[i])-1])

            # numbers1.sort()
            print("No. of elements in file1(input1.txt): ",len(numbers1))
            print("List1(input1.txt): ",numbers1,'\n')
            
            for i in range(len(numbers2)):
                numbers2[i] = int(numbers2[i][:len(numbers2[i])-1])
            # numbers2.sort()
            print("No. of elements in file2(input2.txt): ",len(numbers2))
            print("List2(input2.txt): ",numbers2,'\n')
            numbers = numbers1 + numbers2
            numbers.sort()
            print("Sorted List: ",numbers)
            for i in range(len(numbers)):
                wf.write(str(numbers[i])+'\n')
            #     wf1.write(str(sorted(numbers1)[i])+'\n')