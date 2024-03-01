def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   temp = user_val1
   user_val1 = user_val2
   user_val2 = temp
   temp = user_val3
   user_val3 = user_val4
   user_val4 = temp
   # 10 23 swap using 3rd variable 
   # swap using only given varaibles 
   return user_val1, user_val2, user_val3, user_val4



if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   print(swap_values(user_input1, user_input2, user_input3, user_input4))
   #print those output

 