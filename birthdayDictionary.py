birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
     print("type name of the person u need to find birthday of: (blank space for exit.)")
     name = input()
     if name=="":
           break
     
     if name in birthdays:
           print(birthdays[name])
     
     else :
            print("our data dont have this birthday if you have than pls help us upgrade")
   
            date=input()

            if date == "":
                  print("thanks for not helping us ")
                             
            else:
                  birthdays[name] =date
                  print("thank you for helping us !!! Have a good day !!!")
                  break
print(birthdays)
