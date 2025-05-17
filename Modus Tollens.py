
#TODO------------------ [ MODUS TOLLENS ] ----------------#
# variables
p = True   # "It is raining"
q = True   # "The ground is wet"

#!---------------------- [ METHODS ] --------------------#
# p -> q
def conditional_proposition(p, q):
    return (not p) or q

# Modus Tollens:
# If (P → Q) is true and Q is false, then P must be false.
def modus_tollens(p_implies_q, q):
    if p_implies_q and not q:
        return True   # meaning "not P" is True
    else:
        return False  # cannot conclude "not P"

#?------------ public static void main {} ---------------#
p_implies_q = conditional_proposition(p, q)
not_p = modus_tollens(p_implies_q, q)

print("\n--------------- [ OUTPUT ] ---------------")
print(f"P is {p}, Q is {q}")
print(f"P → Q is {p_implies_q}")
print(f"Modus Tollens conclusion: not P is {not_p}")