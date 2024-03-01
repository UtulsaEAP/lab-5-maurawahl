'''
Name: Maura Wahl
Time: Thursdays at 2
'''

def int_to_reverse_binary(user_input):
    num1 = user_input
    binary_val = ''
#write your while loop here
    while num1 > 0:
        #write your code
        binary_val += str(num1%2)
        num1 = int(num1 // 2)

    return binary_val  

def string_reverse(input_string): 
    reverse_input = ''
    
   #write your for loop here
    for i in range(len(input_string)-1,-1,-1):
        reverse_input += input_string[i]
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)

    #def reverse_binary():
    #user_num = int(input())
    #first_output = 0
    # YOUR CODE HERE
    #s=""
    #while user_num >0:
    #    first_output = user_num%2
    #    s += str(first_output)
    #    user_num = int(user_num/2)
    #print(s)
#if __name__ == "__main__":
#    reverse_binary()