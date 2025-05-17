
#TODO------------------ [ DISJUNCTIVE SYLLOGISM ] ----------------#
p =  False   # "I do not study"
q = True   # "I pass the test"
#!-------------------------- [ METHODS ] -------------------------#

def p_or_q(p, q):
    return p or q


def disjunctive_syllogism(p_or_q_val, p):
    # From P ∨ Q and ¬P, infer Q
    return p_or_q_val and not p

#?----------------- public static void main {} -------------------#

if_p_or_q = p_or_q(p, q)
result     = disjunctive_syllogism(if_p_or_q, p)

print("\n--------------- [ OUTPUT ] ---------------")
print(f"P is {p}   # I did not study")
print(f"Q is {q}   # I pass the test")
print(f"P ∨ Q is {if_p_or_q}")
print(f"Q (by Disjunctive Syllogism) is {result}")