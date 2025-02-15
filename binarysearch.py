# example program for the binary search for finding the elements in the list 
# O(log n)
# sorted_list =[2,4,6,8,10,12,14,16,18,20]   #length=10
#target = 12

def binary_search(sorted_list , target):
    low=0     # start of the list 
    high=len(sorted_list) - 1      #  high =9 end of the list

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]

        print(f" Searching between indices {low} and {high} -> mid = {mid} (value = {mid_value})")

        if mid_value == target:
            return mid    # target found
        elif mid_value > target :
            low = mid + 1       # discard the left half 
        else:
            high = mid -1    # discard the right half

    return -1   # target not found

# Example use case 

if __name__ == "__main__":
    sorted_list =[2,4,6,8,10,12,14,16,18,20]
    target = 12

    print(f"sorted list : {sorted_list}")
    print(f"target is : {target}")

    result = binary_search(sorted_list,target)

    if result !=1:
        print(f"target Found {target} at index {result}")
    else :
        print(f"target not found")


    
