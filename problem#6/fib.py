'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def fibonacci(n):
    #write your code here
    if n == 0:
        return(0)
    if n == 1:
        return(1)  #end of base case
    answer = fibonacci(n-2)+fibonacci(n-1)
    return(answer)
    

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')