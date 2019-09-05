n = int(input("Enter the length of the sequence: ")) # Do not change this line
int_list=[]
for i in range(1,n+1):
    if i <= 3:
        print (i)
        int_list.append(i)
    else:
        placeholder = int_list[-3]+int_list[-2]+int_list[-1]
        int_list.append(placeholder)
        print(placeholder)
        