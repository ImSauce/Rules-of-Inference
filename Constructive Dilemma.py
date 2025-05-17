
#TODO------------------ [ CONSTRUCTIVE DILEMMA ] ----------------#

# variables
p = True   # "I study"
q = True   # "I pass the test"
r = True   # "I graduate"
s = True   # "I get a girlfriend"
#!-------------------------- [ METHODS ] -------------------------#
def conditional_proposition(p, q):
    return (not p) or q

def conjunction(p,q):
    return p and q

def disjunction(p,q):
    return p or q



#?----------------- main logic -------------------#
p_then_q = conditional_proposition(p, q)
r_then_s = conditional_proposition(r, s)
pq_and_rs = conjunction(p_then_q,r_then_s)
p_or_r= disjunction(p,r)
q_or_s=disjunction(q,s)


# Output
print(" ")
print("\n--------------- [ OUTPUT ] ---------------")
print(f"( P -> Q [{p_then_q}] ) and ( R -> S [{r_then_s}] ) is [{pq_and_rs}]")
print(f"P or R [{p_or_r}]")
print(f"------------------")
print(f"Q or S [{q_or_s}]")

