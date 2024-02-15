# Create a function that takes a list of strings and returns the list sorted alphabetically

str_list = ['Orange', "cucumber", 'Chocolate', 'apple', 'Pie', 'papaya']

def sort_string(sl):
    sl.sort()
    return sl
                                    
print(sort_string(str_list))