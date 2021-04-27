"""
Given a, b, and c, return d such that
For each bit of c: if the bit is a 1, choose the corresponding bit from a.  
If it's a 0, choose the corresponding bit from b.
"""


def select(a, b, c):
    # Truth tables:
    
    # c a a1
    # 0 0  0
    # 0 1  0
    # 1 0  0
    # 1 1  1
    # c and a
    
    # c b b1
    # 0 0 0
    # 0 1 1
    # 1 0 0
    # 1 1 0
    #
    # (not c) and a
    
    

    # a1 = a0aaa0
    # b1 = 0b000b
    #a1|b1=abaaab

    return (c & a) | (~c & b) 