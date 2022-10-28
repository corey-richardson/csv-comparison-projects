# csv-projects
Collection of projects involving CSV manipulation and plotting

Iterations:
1 - csv-2-graphs
2 - sample-every-nth-from-csv
  - compare-csvs-with-graphs (added gui to csv-2-graphs)
3 - compare-similar-csvs-on-same-graph

Originally created to convert .csv data from technical flight sim testing at my YINI placement. I would often be given flight test data which I would have to plot individual graphs of time against each column on Excel; this was boring.

Therefore, I used Codecademy's [Visualise Data with Python Skill Course](https://www.codecademy.com/profiles/corey-richardson/certificates/5d24b4845808221825fadca1) to learn packages such as Pandas, matplotlib and seaborn in order to take in a .csv file as input and convert this into a dataframe. The program would then iterate through each column of the dataframe and plot against the first column - in these cases, time.

This was fine until I was then asked to do the same for simulated flight sim data and compare against the real data.

The in-house tool we used to generate the trajectory data accepted upto 1000 waypoints, however the real data had 93,998. To resolve this I created "sample-every-nth-row-from-csv" which originally took every 100th row and put it into a text document in the required format. The data this produced would be jittery and the way I fixed this was to decrease the number of rows before each sample down to 1 every 1800.

The outputted data would then be put through "compare-csvs-with-graphs" which would instead plot the corresponding plots onto the same figure rather than having to run the program on each seperate csv file. That being said, there was still improvement to be made.

This is where I added a simple Tkinter GUI that would open a file explorer allowing the user to set the input files in a more intuitive way than the previous of entering the input file names into the source code each, in the same file directory as the script every time you want to run the program.

Next, I made the third iteration - "compare-similar-csvs-on-same-graph". This version didn't just plot the graphs on the same figure, but onto the same plot. This allowed for the easiest comparison. The issue that arose this time was not due to script, but instead the data I was using. The technical data I was inputting to comapare was not the same length. 

The real data still had the 93,998 rows whereas the sim data, despite being derived directly from the real data, had much less. This caused issues with the graphs not showing at the same scales and as such I didn't flesh out this version with a GUI and simply left it as a proof of concept which I can go back to as a reference in the future.
