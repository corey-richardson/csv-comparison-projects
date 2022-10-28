import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df1 = pd.read_csv("BY6700_EXT_ACE.csv")
df2 = pd.read_csv("BY6701_ACE_EXT.csv")

# Creates a new column called "index" containing data:
# 1, 2, 3, 4, n, n+1, n+2, etc...
df1["index"] = [i for i in range(len(df1))]
df2["index"] = [i for i in range(len(df2))]

plt.subplots(figsize=(6,4))
for i in df1.columns:
    ax1 = sns.lineplot(data=df1,x=df1["index"],y=df1[i])
    ax2 = sns.lineplot(data=df2,x=df2["index"],y=df2[i])
    plt.legend([ax1,ax2],labels=["BY6700","BY6701"])
    plt.savefig("Output/" + str(i) + ".png")
    plt.clf()    

# Plots the corresponding data onto the same graph
# This wouldn't work (without modification) for the customer flight test and flight sim data
# due to the differing lengths --> 900 vs 90,000 rows, as such the data would not be comparable,
# even with the set index without a multiplication of ratios
# 100Hz vs 25Hz
# 900... seconds vs 300... seconds
