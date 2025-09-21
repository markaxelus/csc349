
def base3_list_to_base10(base3_list):
    base10_result = 0.0 
    # your code goes here and should calculate the base10 floating point value appropriately  
    n = len(base3_list)
    for i in range(n):
        power =  n - i - 1
        base10_result += (3 ** power) * base3_list[i]
    return base10_result 
    
     



