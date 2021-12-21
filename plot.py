import argparse
import pandas as pd
from genetic_algorithm import *
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Input Product Description')
parser.add_argument('file_name', metavar='N', type=str,
                    help='enter file name')
args = parser.parse_args()
print(args.file_name)

# load the data
df = pd.read_excel("./data/test.xlsx",
                   header=[0, 1], sheet_name=args.file_name, engine='openpyxl')


# stores final objects
S = []

# store filters for different products 
AC = ["Std. AutoCall", "Fixed Coupon AC",
      "Phoenix AC with Memory", "Phoenix AC Wo Memory"]
PC1 = ["Fixed Coupon AC"]
PC2 = [" Phoenix AC with Memory", "Phoenix AC Wo Memory"]
YE1 = ["YC_Fixed Unconditional"]
YE2 = ["YC_Cond with Memory", "YC_Cond Wo Memory"]


for i in range(len(df["General Terms"]["Format"])):
    ac = True if args.file_name in AC else False
    pc1 = True if args.file_name in PC1 else False
    pc2 = True if args.file_name in PC2 else False
    ye1 = True if args.file_name in YE1 else False
    ye2 = True if args.file_name in YE2 else False

    # general tags
    st = df["General Terms"]["Solve For"][i]+","+df["General Terms"]["Public/Private"][i] + \
        ","+df["Dates"]["Strike Shift"][i]+"," + \
        df["Dates"]["Issue Date Offset"][i]+","
    a, pc, ye = ",,,,", ",,,", ",,,"

    # autocall tags
    if ac:
        a = df["AutoCall"]["Type"][i]+","+df["AutoCall"]["Autocall Freq. "][i] + \
            ","+df["AutoCall"]["AC From"][i]+"," + \
            df["AutoCall Coupon"]["Type"][i]+","
    
    # phoenix tags
    if pc1:
        pc = df["Periodic Coupon"]["Coupon Type"][i] + \
            ",,"+df["Periodic Coupon"]["Coupon Freq"][i]+","
    
    # phoenix tags    
    if pc2:
        pc = df["Periodic Coupon"]["Coupon Type"][i]+"," + \
            df["Periodic Coupon"]["Coupon Barrier Type"][i] + \
            ","+df["Periodic Coupon"]["Coupon Freq"][i]+","
    
    # yield enchancement tags
    if ye1:
        ye = df["Yield Enhancement"]["Coupon Type"][i] + \
            ",,"+df["Yield Enhancement"]["Coupon Freq"][i]+","
    
    # yield enchancement tags
    if ye2:
        ye = df["Yield Enhancement"]["Coupon Type"][i]+"," + \
            df["Yield Enhancement"]["Coupon Barrier Type"][i] + \
            ","+df["Yield Enhancement"]["Coupon Freq"][i]+","

    st = st+a+pc+ye
    st += df["Payoff at Maturity"]["Prot. Type"][i]

    s = Object(st)
    S.append(s)


# define the total iterations
n_iter = 1000
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9

# store results
best_scores = []
best_populations = []

for obj in range(10, 50, 5):
    # mutation rate
    r_mut = 0.5 / float(obj)
    print("Objects in a Population: ", obj)

    # perform the genetic algorithm search
    best, score = genetic_algorithm(
        objective, obj, n_iter, n_pop, r_cross, r_mut, S)
    best_scores.append(score)
    best_populations.append(best)

with open('result.txt', 'w') as f:
    for i, best_pop in enumerate(best_populations):
        f.write("Bucket Size: "+str(10+5*i)+"\n")
        f.write("Best Score: "+str(best_scores[i])+"\n")
        for p in best_pop:
            f.write(p.str+"\n")

x = list(range(5, 45, 5))

plt.plot(x, best_scores)
plt.title("Variation of KL-Divergence with Basket Size")
plt.xlabel("Basket Size")
plt.ylabel("KL-Divergence Score")
plt.show()