
#TODO------------------ [ ADDITION ] ----------------#

# variables
p = True   # "I study"
q = True  # "I pass the test" (doesn't matter for the rule)

#!-------------------------- [ METHODS ] -------------------------#
def disjunction(p, q):
    # From p, infer p ∨ q
    return p or q

#?----------------- main logic -------------------#
p_or_q = disjunction(p, q)

# Output
print(" ")
print("\n--------------- [ OUTPUT ] ---------------")
print(f"P is {p}   # I study")
print(f"Q is {q}   # I pass the test")
print(f"P ∨ Q (by Addition) is {p_or_q}")