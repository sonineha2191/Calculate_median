def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    if len(numbers)%2:
        # %2 gives remainder, if 0 its even---false---else, if not 0 then odd---true--if condition satisfy
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]    
    else:  
        # if 0 its even---false---else
        middle_left = int((len(numbers)/2)-1)
        middle_right = int(len(numbers)/2)
        return (numbers[middle_left] + numbers[middle_right])/2

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))
