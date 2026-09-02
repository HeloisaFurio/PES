n = int(input("Até que número deseja contar?\n- "))

if n > 0:
    i = 0
    while i < n:
        i += 1
        print(i)

        
elif n < 0:
    j = 0
    while j > n:
        j-=1
        print(j)