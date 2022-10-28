# CompareCSVsWithGraphs
Compares similar data from different sources, e.g. FlightRadar24 flight data, and graphs on corresponding subplots

Uses Pythons Pandas, Matplotlib.PyPlot and Seaborn libraries to plot similiar data on the same subplots, and exports as png.

I initially made this to compare data from real customer flight tests and simulated in-house flight tests to look for discrepencies.

~~How could I improve this?~~
~~- GUI~~
~~- add tkinter functionality that lets user select the input files from gui, as well as drop down menu to select output format (defaults to png)~~
~~- This would allow me to export the script as a distributable executable file, without the prerequsites of needing each user to have Python/Anaconda and appropriate libraries installed.~~

UPDATED: Added Tkinter GUI for easier file selection
Added a Tkinter GUI which allows for easier file navigation as opposed to the previous variables "input_one" and "input_two" which the user had to change each time in the source code.
