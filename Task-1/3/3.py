file1 = "input1.txt" #input("Enter first file")
file2 = "input2.txt" #input("Enter second file")
with open(file1,'r') as rf1:
    with open(file2,'r') as rf2:
        with open("output1.txt",'w') as wf1:
            with open("output2.txt",'w') as wf2:
                numbers1 = rf1.readlines()
                numbers2 = rf2.readlines()
                for i in range(len(numbers1)):
                    if(i==len(numbers1)-1):
                        numbers1[i] = int(numbers1[i][:len(numbers1[i])])
                    else:
                        numbers1[i] = int(numbers1[i][:len(numbers1[i])-1])

                numbers1.sort()
                print("No. of elements in file1(input1.txt): ",len(numbers1),'\n')
                print("List1(input1.txt): ",numbers1,'\n')
                for i in range(len(numbers1)):
                    wf1.write(str(numbers1[i])+'\n')
                #     wf1.write(str(sorted(numbers1)[i])+'\n')
                for i in range(len(numbers2)):
                    numbers2[i] = int(numbers2[i][:len(numbers2[i])-1])
                numbers2.sort()
                print("No. of elements in file2(input2.txt): ",len(numbers2),'\n')
                print("List2(input2.txt):",numbers2)
                for i in range(len(numbers2)):
                    wf2.write(str(numbers2[i])+'\n')
                #wf1.writelines(str(numbers1))