Userik=['Maks']
Passik=['123']
a = ''
print('Hello user!')
def newacc():
    log=input('Write your login: ')
    if log in Userik:
        print('This Login exists.')
        newacc()
    else:
        b=int(input('U want to create own pass or random? 1-own, 2-random: '))
        if b==1:
            passw= input('Create password: ')
        if b==2:
            import random
            str0=".,:;!_*-+()/#¤%&"
            str1 = '0123456789'
            str2 = 'qwertyuiopasdfghjklzxcvbnm'
            str3 = str2.upper()
            str4 = str0+str1+str2+str3
            ls = list(str4)
            random.shuffle(ls)
            passw = ''.join([random.choice(ls) for x in range(12)])
            print('You are welcome',passw)
        Userik.append(log)
        Passik.append(passw)
        print(f'Welcome back, {log}!')
def oldacc():
    login = input('Your login: ')
    passw = input('Your password: ')
    if login in Userik and passw in Passik:
        print(f'Welcome back, {login}!')
    else:
        print('Incorect login or password, try one more time!')
        oldacc()
a=input('Are u our member? yes or no ? or if u want to quit, type: QUIT ===  ')
if a=='Yes' or a=='yes':
    oldacc()
elif a=='No' or a=='no':
    newacc()
elif a=='QUIT':
    quit()