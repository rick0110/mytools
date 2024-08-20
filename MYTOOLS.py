PI_INT = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
E_INT = 7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
def pi_real(n):
    pi = 3 + PI_INT/10**100
    return f'{pi:.{n}f}'

def e_real(n):
    e = 2 + E_INT/10**100
    return f'{e:.{n}f}'

print(type(e_real(9)))