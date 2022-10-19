# #help("TUPLES")
# a = 4+5j


def my_crappy_range(N):
    i = 0
    while i < N:
        yield i
        i += 1
        
    return i
        
