
#TODO------------------ [ RESOLUTION ] ----------------#

# variables
p = True   # "I study"
q = True   # "I pass the test"
r = True   # "I graduate"
#!-------------------------- [ METHODS ] -------------------------#
def disjunction(p, q):
    return p or q


#?----------------- main logic -------------------#
p_or_q       = disjunction(p, q)         # P ∨ Q
not_p        = not p                     # ¬P
not_p_or_r   = disjunction(not_p, r)   

q_or_r = disjunction(q, r)


# Output
print(" ")
print("\n--------------- [ OUTPUT ] ---------------")
print(f"P or Q is {p_or_q}   ")
print(f"-P or R is {not_p_or_r} ")
print(f"------------------")
print(f"Q or R is {q_or_r}")
