# CSV2Graphs
Converts CSV files to graphs using Pythons Pandas, MatPlotLib and Seaborn libraries 

Originally created to convert .csv data from technical flight sim testing at my YINI placement.
This flight sim data had multiple .csv files for GPS / INS / Nav / etc data
Data can come from different .csv files with differing number of columns so I wanted to program this to be as dynamic as I could.
--> can be used to plot 6 graphs or 50 graphs.
As such, the number of columns and rows per subplot can be changed from variables at the top of the .py code.

Input file, output format (png/pdf), encoder, rows and columns can all be changed.

Iterates through each column in the dataframe, plots a lineplot and adds to a subplot. 
Then, either when the subplot is full or at the end of running, it saves the subplot figure as the set output format.

The attached example csv file is flight data from FlightRadar24 representing a TUI flight from Lanzarote (ACE) to Exeter (EXT) on 16/10/2022.

How I could improve this?
- GUI allowing you to select input file path and set the formatting variables
- Export the graphs to an Excel Spreadsheet allowing for easier data analysis compared to a static image file

7/10/2022
