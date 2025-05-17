
#TODO------------------ [ CONJUNCTION ] ----------------#

# variables
p = True   # "I study"
q = True   # "I pass the test"

#!-------------------------- [ METHODS ] -------------------------#
def conjunction(p, q):
    return p and q


#?----------------- main logic -------------------#
p_and_q = conjunction(p, q)

# Output
print(" ")
print("\n--------------- [ OUTPUT ] ---------------")
print(f"P is {p}   # I study")
print(f"Q is {q}   # I pass the test")
print(f"P ∧ Q (by Conjunction) is {p_and_q}")
