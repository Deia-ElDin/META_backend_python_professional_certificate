str = 'race1car'

def is_palindrome(str):
    return str == str[::-1]

# def is_palindrome(str):
#     start_idx = 0
#     end_idx = len(str) - 1

#     for i in range(len(str) // 2):
#         print("i ", i, "start_idx ", start_idx, "end_idx ", end_idx)

#         if str[start_idx] != str[end_idx]:
            
#             return False
#         # start_idx += 1
#         # end_idx -= 1
#     return True

print("\n--------------------------------\n")

'''
    Exercise: Make a cup of coffee
        Introduction
        In this exercise, you will practice the use of an algorithm to make a cup of instant coffee. The purpose is to lay out the steps required in order to get the final product. 

        Instructions
        Step 1: Start with the inputs - what is needed to make a cup of instant coffee?

        Step 2: Think about all the steps required in the physical aspect of making a cup of instant coffee.

        Step 3: Consider the edge cases of optional things like milk or sugar, some people may want it. 

        Step 4: The algorithm when complete should have as its final result a cup of coffee.

        Tips: Planning is key with any algorithm. Make sure you have all the steps neatly laid out. 

        Resources

    Make a cup of coffee - solution
        Solution algorithm

        Input 
            Ingredients required:
                Cup
                Hot water
                Coffee granules

        Optional:
            Milk
            Cream 
            Sugar

        Output
            A cup of coffee.

        Steps
            1. Add drinking water to an electric kettle. 
            2. Put the kettle on to boil water.
            3. While waiting, prepare coffee.
            4. Add coffee granules to the cup.
            5. If water is boiled, pour water into a cup, else continue to wait.
            6. If milk or cream is required, add and stir.
            7. If sugar is required, add and stir.
            8. Return coffee.
'''