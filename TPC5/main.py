import re

exit = True
running = False
moneyc = 0
moneye = 0

# def that decrements the balance with the value received in arg
def decrement(dece,decc):
    global moneyc
    global moneye
    if moneyc > decc:
        moneyc -= decc
    else:
        rest = decc - moneyc
        print(rest)
        n = int(rest/100)
        print(n)
        moneye -= (n+1)
        rest = rest - n*100
        print(rest)
        moneyc = 100 - rest
    moneye -= dece

# def that increments the balance with the value received in arg
# 100 cents is equal to 1 euro
def increment(incc):
    global moneyc
    global moneye
    rest = 100 - moneyc
    if incc >= rest:
        incc -= rest
        moneye += 1
        if incc > 0:
            n = int(incc/100)
            moneye += n
            incc -= n*100
        moneyc = incc
    else:
        moneyc += incc

def troco():
    global moneyc
    global moneye
    res = "Troco= "

    coin2euros = int(moneye/2) # coin2euros retorno de moedas de 2 euros
    if coin2euros > 0:
        res += coin2euros + "x2e, "
        moneye -= coin2euros*2
    if moneye > 0:
        res += str(moneye) + "x1e, "

    coin50cent = int(moneyc/50)
    if coin50cent > 0:
        res += str(coin50cent) + "x50c, "
        moneyc -= coin50cent*50

    coin20cent = int(moneyc/20)
    if coin20cent > 0:
        res += str(coin20cent) + "x20c, "
        moneyc -= coin20cent*20

    coin10cent = int(moneyc/10)
    if coin10cent > 0:
        res += str(coin10cent) + "x10c, "
        moneyc -= coin10cent*10

    coin5cent = int(moneyc/5)
    if coin5cent > 0:
        res += str(coin5cent) + "x5c, "
        moneyc -= coin5cent*5

    coin2cent = int(moneyc/2)
    if coin2cent > 0:
        res += str(coin2cent) + "x2c, "
        moneyc -= coin2cent*2

    if moneyc > 0:
       res += str(moneyc) + "x1c, "

    res = res[:-2]

    return(res)

# def that treats the case when the user puts money
def moneyFunc(user_input):
    global moneyc
    global moneye
    money = re.split(r' ',user_input)
    res = ""
    # to each coin received, checks if they are euros or cents and if the coin exists
    for i in range(1,len(money)):
        cents = re.match(r"(\d+)c",money[i])
        euros = re.match(r"(\d+)e",money[i])
        if cents and not re.match(r"^[1|2|5|10|20|50]c$",cents.group(1)):
            # the coin is not valid
            res += cents.group(1) + "c - moeda inválida; "
        elif cents:
            increment(int(cents.group(1)))
        if euros and not re.match(r"^[1|2]e$",euros.group(1)):
            res += cents.group(1) + "c - moeda inválida; "
        elif euros:
            moneye += int(euros.group(1))
    print(res + "Saldo = " + str(moneye) + "e" + str(moneyc) + "c")

# def that treats the case of the user that puts a phone number
def teleFunc(user_input):
    tele = re.split(r'=',user_input)
    num = tele[1]
    # the number has to have nove numbers to be a valid phone number
    if len(num) == 9:
        if re.match(r'^601\d+',num) or re.match(r'641\d+',num):
            # treats the cases where the call is blocked
            print("Esse número não é permitido neste telefone. Queira discar novo número!")
        elif re.match(r'^00\d+',num):
            # the phone call is international, checks if the user has 1,5 euros
            if (moneye==1 and moneyc>=50) or moneye>1:
                decrement(1,50)
                print("Saldo = " + str(moneye) + "e" + str(moneyc) + "c")
            else:
                print("Saldo insuficiente :(")
        elif re.match(r'^2\d+',num):
            # the phone call is national, checks if the user has 25 cents
            if moneyc>=25 or moneye>=1:
                decrement(0,25)
                print("Saldo = " + str(moneye) + "e" + str(moneyc) + "c")
            else:
                print("Saldo insuficiente :(")
        elif re.match(r'^800\d+',num):
            # its a green call, its free
            print("Saldo = " + str(moneye) + "e" + str(moneyc) + "c")
        elif re.match(r'^808\d+',num):
            # its a blue call
            if moneyc>=10 or moneye>=1:
                decrement(0,10)
                print("Saldo = " + str(moneye) + "e" + str(moneyc) + "c")
            else:
                print("Saldo insuficiente :(")
    elif re.match(r'^00\d+',num):
        # the phone call is international, it can have less then nove numbers
        # checks if the user has 1,5 euros
        if (moneye==1 and moneyc>=50) or moneye>1:
            decrement(1,50)
            print("Saldo = " + str(moneye) + "e" + str(moneyc) + "c")
        else:
            print("Saldo insuficiente :(")
    else:
        print("Não é possível efetuar a operação :(")

# checks the commands and runs the respectives operations
# runs as long as there is no interrupt
while exit:
    try:
        user_input = input("Indica o comando: ")
        if re.match(r'^LEVANTAR$',user_input):
            print("Introduza moedas.")
            running=True
        elif running and re.match(r'^POUSAR$',user_input):
            print(troco() + "; Volte sempre!")
            moneyc = 0
            moneye = 0
            running = False
        elif running and re.match(r'^ABORTAR$',user_input):
            print("Retorna " + str(moneye) + "e" + str(moneyc) + "c; Volta sempre!")
        elif running and re.search(r'^MOEDA',user_input):
            moneyFunc(user_input)
        elif running and re.search(r'^T=',user_input):
            teleFunc(user_input)
        else:
            print("Não é possível efetuar a operação :(")       
    except KeyboardInterrupt:
        # end the loop when the user types "Ctrl+D" or "Ctrl+C"
        exit = False
    except EOFError:
        exit = False