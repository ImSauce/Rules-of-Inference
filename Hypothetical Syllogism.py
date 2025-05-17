
#TODO------------------ [ HYPOTHETICAL SYLLOGISM ] ----------------#
# Propositions as booleans
p = True   # "I study"
q = True   # "I pass the test"
r = True   # "I graduate"


#!---------------------- [ METHODS ] --------------------#
# Logical implication function
def conditional_proposition(x, y):
    return (not x) or y

# Hypothetical Syllogism:
# From (P → Q) and (Q → R), infer (P → R)
def hypothetical_syllogism(p_to_q, q_to_r):
    return p_to_q and q_to_r



#?------------ public static void main {} ---------------#
# Compute the two implications
p_to_q = conditional_proposition(p, q)     # If I study then I pass
q_to_r = conditional_proposition(q, r)     # If I pass then I graduate

# Chain them
p_to_r = hypothetical_syllogism(p_to_q, q_to_r)

# Output
print("--------------- [ OUTPUT ] ---------------")
print(f"P is {p}   # I study")
print(f"Q is {q}   # I pass the test")
print(f"R is {r}   # I graduate\n")
print(f"P → Q is {p_to_q}")
print(f"Q → R is {q_to_r}")
print(f"P → R (by Hypothetical Syllogism) is {p_to_r}")