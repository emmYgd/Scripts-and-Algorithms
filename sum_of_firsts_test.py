from typing import TypeVar, Optional, Any, List
import sys

#impose constraints with decorators:

def array_struct_constraint(func: Any) -> Any:
    '''Constraint: 1 <= a.length <= 10**3'''
    def inner(array:List[int]):
        
        first_condition : bool = (len(array) <= 10**3)
        second_condition : bool = (len(array) >= 1)
        
        if not(first_condition) and not(second_condition) :
            print("Constraint broken! Please supply array that will obey the constraint boundaries!")
            return
        
        return func(array)
    
    return inner

def array_args_constraint(func: Any) -> Any:
    '''Constraint: 0 <= a[i] <= 10**6'''
    def inner(array:List[int]):
        
        for array_elem in array:
            first_condition : bool = (array_elem <= 0)
            second_condition : bool = (array_elem <= 10**6)
        
            if not(first_condition) and not(second_condition) :
                print("Constraint broken! Please supply array elements that will obey the constraint boundaries!")
                return
        
        return func(array)
    
    return inner
            
    
#to the target function:
@array_struct_constraint
@array_args_constraint
def sumOfFirsts(array: List[int])-> int:
    """This is used for the algorithmic solution"""
    
    #init:
    work_array = array 
    array_count: int  = 0
    non_zero_value_sum: int = 0
       
    for each_elem in work_array:
        
        #print("Work Array : ", work_array)
        if work_array[array_count] == 0:
            #skip
            continue
        else:
            #the value:
            non_zero_value = work_array[array_count]
                
            #the modified list: use list comprehension to step through the array:
            modified_list = [(each_elem - non_zero_value) for each_elem in work_array if each_elem >= non_zero_value]
            print("Modified Array : ", modified_list)
            
        #set this as the latest array to work on :
        work_array = modified_list
        print("New Array : ", work_array)
                
        #the sum:
        non_zero_value_sum =  non_zero_value_sum + non_zero_value               
            
        array_count = array_count + 1

    return non_zero_value_sum
            
    
def main()->None:
     #init Integer List:
    integer_array: List[int] = []
    
    #add element to the list:
    array_length = int(input("Enter the length of the array you have in mind. Start counting from 1 : "))
    
    for index in range(array_length):
        array_elem: int = int(input("Enter each array element : "))
        #add to array:
        integer_array.append(array_elem)

    print("Array: ", integer_array)
    
    non_zero_value_sum = sumOfFirsts(integer_array)
    print("Result: ", non_zero_value_sum)

#run the main event:
if __name__ == "__main__":
    main()
