
#TODO------------------ [ ABSORPTION ] ----------------#

# variables
p = True   # "I study"
q = True   # "I pass the test"
#!-------------------------- [ METHODS ] -------------------------#
def conditional_proposition(p, q):
    return (not p) or q

def conjunction(p,q):
    return p and q

def absorption (p, p_and_q):
    return (not p) or p_and_q



#?----------------- main logic -------------------#
p_then_q = conditional_proposition(p, q) 
p_and_q = conjunction(p,q)    
p_then_p_and_q = absorption(p, p_and_q)


# Output
print(" ")
print("\n--------------- [ OUTPUT ] ---------------")
print(f"P -> Q is {p_then_q}")
print(f"------------------")
print(f"p -> (p and q is {p_and_q}) is {p_then_p_and_q}")
