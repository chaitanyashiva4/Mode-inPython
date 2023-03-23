list_a = list(map(int,input().split(","))) #reads input and splits it into a list of integers using int and map functions.
max_num = 0  #assign 0, to find the highest frequency of num in the list
mode = 0  #assign 0, to find the number with the highest frequency
for num in list_a : #iterates over each num in the list
    count = list_a.count(num) #used to count the frequency of the number
    if count > max_num : #check the current maximum frequency of the number using this condition
        max_num = count #assign count if max_num is less than count
        mode = num #assign the num with maximum frequency 
print(mode) 
