'''
    str[start:stop:step]
    start: index of the first character to include
    stop: index of the first character to exclude
    step: index of the character to include
'''

trial = "reversal"

new_trial = trial[::-1]
print ("Reversal of 'reversal' is using slicing: ", new_trial)

print("\n--------------------------------\n")

def reverse_string_recursive(str):
    if len(str) == 0:
        return str
    else:
        # 1st method
        # len_str = len(str) - 1
        # last_char =  str[len_str]
        # return last_char + reverse_string_recursive(str[:len_str])

        # 2nd method
        # return str[-1] + reverse_string_recursive(str[:-1])

        # 3rd method
        return reverse_string_recursive(str[1:]) + str[0]
    
print ("Reversal of 'reversal' is using recursion: ", reverse_string_recursive("reversal"))

print("\n--------------------------------\n")



