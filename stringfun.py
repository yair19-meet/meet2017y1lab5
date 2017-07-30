def string_test(s):
    return (len(s) > 2 and s[0] == s[-1])
    


def add_x(s):
    s.append('x')
    s.reverse()
    s.append('x')
    s.reverse()
    
    return s
