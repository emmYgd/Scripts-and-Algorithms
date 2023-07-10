from typing import Any, List, TypeVar

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
def countArithmeticMeans(array: List[int]) -> int:
    '''This performs the nearest neighbor mean task..'''

    #Mean type:
    IntOrFloat = TypeVar("Choosable", int, float)

    #init event count:
    event_count: int = 0

    #init step count:
    step_count: int = 0
    
    for array_elem in array:
        
        #base case: first element count: 
        if array_elem == array[0] :
            #pass
            add: int = 0 + array[1]
            mean: IntOrFloat = add/2
            #print("First Mean: ", mean)

        #last case: last element count: 
        elif array_elem == array[-1] :
            #pass
            add: int = 0 + array[-2]
            mean: IntOrFloat = add/2
            #print("Last Mean: ", mean)
            
        #other case scenerio'''   
        else:
            add: int = array[step_count  - 1] + array[step_count  + 1]
            mean: IntOrFloat = add/2
            #print("Other Mean:", mean)        

        #print(mean)
        if mean == array[step_count]:
            event_count = event_count + 1
            #print("Event Count: ", event_count)

        step_count = step_count + 1

    return event_count

#main funiction:
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
    
    event_count = countArithmeticMeans(integer_array)
    print("Result: ", event_count)

#run the main event:
if __name__ == "__main__":
    main()


        
