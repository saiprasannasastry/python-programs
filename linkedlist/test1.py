# def GCD(A,B):
#     if B==0:
#         return A
#     else:
#         return GCD(B,A%B)
# print(GCD(357,234))

def LCM(A,B):
    if B==0:
        return A
    else:
        return LCM(A,A%B)
print(LCM(6,8))