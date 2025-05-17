
#TODO------------------ [ MODUS PONENS ] ----------------#
#variables
p = True   # "It is raining"
q = True  # "The ground is wet"


#!---------------------- [ METHODS ] --------------------#
# p -> q
def conditional_proposition(p, q):
    return (not p) or q

# p
# p -> q
# ... q
def modus_ponens(p_then_q, p):
    if p_then_q and p:
        return True 
    else:
        return False 






#?------------ public static void main {} ---------------#
# Check if implication holds
p_implies_q = conditional_proposition(p, q)

# Apply modus ponens
result = modus_ponens(p_implies_q, p)

print(" ")
print("--------------- [ OUTPUT] ---------------")
print(f"P is {p}, Q is {q}")
print(f"P → Q is {p_implies_q}")
print(f"Modus Ponens conclusion: Q is {result}")