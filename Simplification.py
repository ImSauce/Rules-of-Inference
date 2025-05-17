
#TODO------------------ [ SIMPLIFICATION ] ----------------#

# variables
p = True   # "I study"
q = True   # "I pass the test"

#!-------------------------- [ METHODS ] -------------------------#
def conjunction(p, q):
    return p and q

def simplification(p_and_q):
    # From P ∧ Q, infer P
    if p_and_q:
        return True    # we know P must be true
    else:
        return False   # can't conclude P

#?----------------- main logic -------------------#
p_and_q = conjunction(p, q)
p_inferred = simplification(p_and_q)

# Output
print(" ")
print("\n--------------- [ OUTPUT ] ---------------")
print(f"P ∧ Q is {p_and_q}   # True ∧ True → True")
print(f"P (by Simplification) is {p_inferred}")