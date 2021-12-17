import pandas as pd
from object import *

# load the data
df = pd.read_excel("./data/autocall_testcase.xlsx",
                   sheet_name='Sheet1', engine='openpyxl')

# convert the data into input format
# save into list of objects created by input
S = []

for i in range(len(df["Format"])):
    s = Object(df["Solve For"][i]+","+df["Public/Private"][i]+","+df["Strike Shift"][i]+","+df["Issue Date Offset"][i]+","+df["AutoCall Type"][i]+","+df["Autocall Freq."][i]+","+df["AC From"][i]+","+df["AutoCall Coupon Type"][i]+","+df["Prot. Type"][i])
    S.append(s)
