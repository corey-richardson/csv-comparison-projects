import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import time

# ------------------------------------------------- #
# Change input file to the CSV file you want to plot
# Must be in the same directory
input_file="BY6701_2ddc965e.csv"
# Set Number of columns per subplot and Number of
# rows per subplot here
columns = 2
rows = 3
# Set output format
output_format = ".png"
# ------------------------------------------------- #

# Timer
start_time = time.time()

# Panda reads the CSV and sets it to the dataframe 'df'
encoder = "mbcs"
df = pd.read_csv(input_file,encoding=encoder)

# Input sanitisation for later use
input_file = input_file.replace(".csv","")
# iterate through each column of df
# every row*column plots, save the png
# increment format_check
# if format check = row*column
# save fig

 

# Counter, format Counter (if format_counter == row*column: savefig)
count = 1
format_counter=1

# Set up a subplot of size 10*8 inches
plt.subplots(figsize=(columns*6,rows*4))

# Iterates through each column of df and plots it against "Time (s)"
# Increments count
# When count = row*columns,
# - Assign the output file name and format
# - Save the figure to output_file
# - Increment the format_counter so the next save doesn't overwrite
# - Reset count to 1
# - Clear the figure

 

for i in df.columns:
    print("%i/%i" % (count,rows*columns),end="\r")
    plt.subplot(rows,columns,count)
    ax = sns.lineplot(data = df, x=df.iloc[:, 0],y=df[i])

 

    if count == rows*columns:
        output_file = "Output/" + input_file + "_" + str(format_counter) + output_format
        plt.savefig(output_file,dpi=300)
        print(output_file.replace("Output/",""))
        format_counter+=1
        # print("format count %i" % format_counter)
        count=1
        plt.clf()
    else:
        count+=1

 
# Saves the last figure in case count < rows*columns
output_file = "Output/" + input_file + "_" + str(format_counter) + output_format
try:
    plt.savefig(output_file,dpi=300)
except:
    print("Please make a file called \"Output\" in the same file directory as the .py file.")
print(output_file.replace("Output/",""))
plt.clf()

print("Time taken: %s" % (time.time()-start_time))