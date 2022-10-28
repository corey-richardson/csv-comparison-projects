# SampleEveryNthFromCSV

I was asked to sample ~1000 data values for Longitude, Latitude, Speed and Altitude from a flight test sim consisting of over 93,000 rows.
To do this by hand would have taken... a while.
As such I used Pythons Pandas library to read the .csv file and File I/O to format this data into the required format in a txt file.
The program will also output the number of rows sampled - waypoints - so the user can check it is below 1000 and use this in the required tools.

The attached example csv file is flight data from FlightRadar24 representing a TUI flight from Lanzarote (ACE) to Exeter (EXT) on 16/10/2022.

How I could improve this?
- GUI allowing you to select input file path and set the formatting variables

17/10/2022
