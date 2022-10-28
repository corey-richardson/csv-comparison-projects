import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Set encoder variable
encoder = "mbcs"

# TO IMPROVE: add tkinter functionality that lets user select the input files from gui, as well as drop down menu to select output format (defaults to png)
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *

# Tk head
# Initialises a new window of size 700x350
root = tk.Tk()
root.geometry("700x350")
# Sets window title
root.title("CSV file to graph comparison")
# Displays a message to the window with guide instructions
label = ttk.Label(text="Select first CSV file. \nSelect second CSV file. \nSelect output directory. \nSet filetype. \nSet output format.")
label.pack(fill=tk.X, padx=5, pady=5)
# Tk body

# Defines a function which allows the user to set the input files in file explorer
def set_inputs():
    from tkinter import filedialog as fd
    input_file = fd.askopenfilename()
    label = ttk.Label(text=input_file)
    label.pack(fill=tk.X, padx=5, pady=5)
    return input_file

input_one = set_inputs()
input_two = set_inputs() 

# Opens file explorer allowing user to select output directory, then displays the file path to screen
output_location = fd.askdirectory()
label = ttk.Label(text=output_location)
label.pack(fill=tk.X, padx=5, pady=5)

# Set output format
label = ttk.Label(text="Set the output format:")
label.pack(fill=tk.X,padx=5,pady=5)
selected_format = tk.StringVar()
format_select = ttk.Combobox(textvariable=selected_format)
format_select["values"] = (".png",".pdf",".svg")
# Commented out next line due to issue where cmb_form_changed() would not update if the box was left 
# as it's default setting, and would therefore be an empty value
# format_select.set(".png")
format_select["state"] = "readonly"
format_select.pack(fill=tk.X, padx=5, pady=5)

# Defines a function that runs when the  combobox is changed
# Sets the current combobox value to the relevant variable
format_output = ""
def cmb_form_changed(event):
    global format_output
    format_output = selected_format.get()
        
format_select.bind('<<ComboboxSelected>>', cmb_form_changed)

Button(root,text="Plot",command=root.destroy).pack()
root.mainloop()

COLUMNS = 1
ROWS = 2

# Pandas read the csv files and save them to dataframes
df1 = pd.read_csv(input_one,encoding=encoder)
df2 = pd.read_csv(input_two,encoding=encoder)

# Sets up a subplot/figure with dynamic size
plt.subplots(figsize=(COLUMNS*6,ROWS*4)) 

# Counts the number of columns in the dataframe
# This value is later used as a check to prevent the plotting to overrun the amount of data
num_cols = 0
for i in df1.columns:
    num_cols+=1
    
# Initialise variables
name_count = 1
count = 1
for i in df1.columns:
    # Checks if the current plotting column is out of range
    # If it is, it will break from the for loop and end program
    if name_count == num_cols:
       break
    print("%i/%i" % (name_count,num_cols-1))
    plt.subplot(ROWS,COLUMNS,count)
    ax1 = sns.lineplot(data=df1,x=df1.iloc[:,0],y=df1[i])
    count+=1
    plt.subplot(ROWS,COLUMNS,count)
    ax2 = sns.lineplot(data=df2,x=df2.iloc[:,0],y=df2[i])
    plt.savefig(output_location + "/" + str(name_count) + format_output ,dpi=300)
    plt.clf()
    count=1
    name_count += 1

# Advantages over previous method
# - Plotting each column through excel is time consuming, as opposed to this script which can take
# -- less than a minute
# Disadvantages over previous method
# - Plots are not interactive and so don't allow for in-depth analysis, however they will show any obvious
# -- discrepencies allowing you to focus in on those areas with more in-depth methods
# - Also, with the amount of time this took me, I could have plotted hundreds of Excel graphs :)
