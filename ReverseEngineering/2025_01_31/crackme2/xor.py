# Given key values
key_values = [67, 72, 67, 95, 56, 101, 95, 57, 73, 86, 49, 110, 103, 95, 
              97, 110, 95, 101, 97, 83, 89, 95, 84, 73, 109, 101]

# XOR each value with 3 and store the decimal results
xor_decimals = [c ^ 3 for c in key_values]

# Print the result
print(xor_decimals)
