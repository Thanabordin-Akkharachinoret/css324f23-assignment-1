def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == (4,4,0)

def successors(s):
    a, b, c = s
    return []
