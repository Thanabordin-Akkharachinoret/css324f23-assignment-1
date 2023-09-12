def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == (4,4,0)

def successors(s):
    a, b, c = s
    new_a, new_b = a-5, b+5
    new_b, new_c = b-3, c+3
    new_a, new_c = a+3, c-3
    new_b, new_c = b-2, c+2
    new_a, new_b = a-5, b+5
    new_b, new_c = b-1, c+1
    new_a, new_c = a+3, c-3
    return (4,4,0)
