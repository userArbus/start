import random 
x= random.randint(1,55)
while True:
            print("guess a number: ")
            y=int(input())
            if x>y:
                        print("try something bigger")
            if x<y:
                         print("try something smaller")
            if x==y:
                         print("congo u guessed the right number "+ y )
                         break
