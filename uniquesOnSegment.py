from typing import TypeVar, Optional, Any, List
import sys

def sub_arr_count(sub_array:List[int] , k: int)->int:
    #init:
    sub_array_count:int = 0
    
    #convert new list to set (to test for uniqueness):
    sub_array = set(sub_array)
    if len(sub_array) >= k :
        sub_array_count = sub_array_count + 1
    else:
        sub_array_count = sub_array_count

    return  sub_array_count
    

def uniquesOnSegment(numbers: List[int] , k: int ):
    """This is used for the algorithmic solution"""
    
    #init:
    for i in numbers:
        #get ranges based on the given solution:

        #init:
        from_value: int = 0
        to_value: int = k
        shuffled_sub_list: List[int] = []
        sub_array_count: int = 0
        
        #base instance:
        shuffled_sub_list = numbers[from_value : to_value]
        #to_value = to_value + 1
        sub_array_count = sub_arr_count(shuffled_sub_list , k)
        print("Base SubList: ", shuffled_sub_list)
        print("Count:", sub_array_count)

        for i in numbers:
            
            to_value = to_value + 1
            shuffled_sub_list = numbers[from_value : to_value]
            sub_array_count = sub_arr_count(shuffled_sub_list , k)
            print("Other SubList: ", shuffled_sub_list)
            print("Count:", sub_array_count)
            
            if to_value == len(numbers):
                #reset base positions:
                from_value = from_value + 1
                shuffled_sub_list = numbers[from_value : to_value]
                sub_array_count = sub_arr_count(shuffled_sub_list , k)
                print("Other SubList: ", shuffled_sub_list)
                print("Count:", sub_array_count)
                
    return sub_array_count

        

            
                


                
        
