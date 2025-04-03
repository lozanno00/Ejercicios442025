def torre(n, torre1="1", torre2="2", torre3="3"):
    if n>0:
        torre(n-1, torre1, torre3, torre2)
        print(f"Mover disco de {torre1} a {torre3}")
        torre(n-1, torre2, torre1, torre3)

piedras=int(input("Cuantas piedras vas a usar:"))
torre(piedras)