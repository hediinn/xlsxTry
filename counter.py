import msvcrt,sys

i =0

class counter:

    while True:
    
        if msvcrt.kbhit():
            ch=ord(msvcrt.getch())
            if i ==10:
                i=0 
            if ch == 113:
                sys.exit()
            if ch == 32:
                i=i+1
                print(i)
    