from termcolor import cprint

for i in range(0,8):
    for j in range(0,8):
        if (i+j)%2==0:
            cprint(("B", "black", "on_black"), end="")

        else:
            cprint(("W", "white", "on_white"), end="")
            
    print()