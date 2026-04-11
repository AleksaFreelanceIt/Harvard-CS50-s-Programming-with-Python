#Unpacking a dictionary
#def total(eur, usd, rsd):
#    return(eur*117 + usd*110 + rsd)
#
#coins={"eur": 100, "usd":50, "rsd":25}
#
#print(total(**coins),"RSD") #** unpacks a dictionary


#kwargs, allows the function to optionaly take multiple args
def f(*args, **kwargs): #kwargs makes the arguments an dictionary
    print("Named:",kwargs)

f(eur = 100,usd = 50,rsd = 25) 