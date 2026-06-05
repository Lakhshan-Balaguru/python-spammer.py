def spammer(usermessage, userno):
    print("time to spam")
    
    for i in range(userno):
        print (usermessage)
        
    print ("phwew done spamming")
   
print ("what word would u like to spam")
usermessage= input()

print ("how many times do u want to spam?")
userno = int(input())
spammer(usermessage, userno)