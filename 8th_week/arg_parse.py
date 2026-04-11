import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n",default= 1, help = "number of times to meow", type= int) #calling -h shows help 
args = parser.parse_args() #parser calls the sys library to work with command line args

for _ in range(int(args.n)):
    print("meow")