def distances_from_average(test_list):
    
    total = sum(test_list)  # Calculate the sum of all elements in the array
    avg = total / len(test_list)  # Calculate the average
    
    # Calculate the distance from the average for each element and round it to 2 decimal places
    result = [round(avg - x, 2) for x in test_list]
    
    return result