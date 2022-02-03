def single_row(char, N):
    return(char * N)


def print_square(char, N):
    for i in range(N):
        print(single_row(char,N))
print_square("@", 3)
print()
print_square("#", 2)
print()
print_square("*", 5)
