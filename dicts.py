def merge_dicts(dict1, dict2):
    # Create a copy of the first dictionary to avoid modifying the original
    merged_dict = dict1.copy()
    
    # Iterate through the second dictionary
    for key, value in dict2.items():
        # If the key exists in the first dictionary, sum the values
        if key in merged_dict:
            merged_dict[key] += value
        else:
            # if not, just add the key-value pair to the merged dictionary
            merged_dict[key] = value
    
    return merged_dict

#this how it would look like
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 2, 'd': 1}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)
