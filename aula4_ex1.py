def do_twice (f, x): 
    f (x) 
    f (x)

def print_twice (x): 
    print(x) 

do_twice (print_twice, 'spam')

def do_four (g, y): 
    do_twice(g, y) 
    do_twice(g, y) 

def print_four (y): 
    print(y)

do_four (print_four, 'string')

