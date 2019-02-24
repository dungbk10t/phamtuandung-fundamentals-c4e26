import ex9
even_list = ex9.get_even_list([1,2,5,9,-10,6])
if set(even_list) == set([2,-10,6]):
    print("Your funtion is correct")
else:
    print("Ooops, bugs dectecd")
        