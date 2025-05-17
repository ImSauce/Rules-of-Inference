
#TODO------------------ [ MODUS PONENS ] ----------------#
#variables
p = True   # "It is raining"
q = True  # "The ground is wet"


#!---------------------- [ METHODS ] --------------------#
# p -> q
def if_p_then_q(p,q):
    return (not p) or q


def modus_tollens(if_p_then_q, q):
    if if_p_then_q and not q:
        return True
    else:
        return False


#?------------ public static void main {} ---------------#
p_implies_q = if_p_then_q(p, q)

# Apply modus ponens
result = modus_tollens(p_implies_q, q)

print(" ")
print("--------------- [ OUTPUT] ---------------")
print(f"P is {p}, Q is {q}")
print(f"P → Q is {p_implies_q}")
print(f"Modus Tollens conclusion: not P is {result}")