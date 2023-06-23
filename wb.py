# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of "F" greater than or equal to 2 returns "Outage", anything below returns "Power"
# Example Input: [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"

# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints
    # Determine a Logical way to solve the problem
        #Write each step out english
        #Write each step out in Python-esse
    # Invoke and Test Your Function


def streetLights(l_street):
    count_list = 0
    #Look at every letter in the list
    #Look how many Ts and Fs are in the list
    #if it is a total number of F >= 2 then it is a outage
    #Anything other than that is power
    for light in l_street:
        if light == 'F':
               count_list += 1
    if count_list >= 2:
        return "Outage"
    else:
        return "Power"
    
print(streetLights([ 'T', 'T', 'T', 'F' ]))

        





