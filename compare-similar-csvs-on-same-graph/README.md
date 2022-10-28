# CompareSimilarCSVsSameGraph

Similar: same data headers but can be from different sources, like for like

Plots corresponding data from similar data frames onto a single graph even if the timestamps are different.
HOWEVER, the time STEPS do have to be the same for the graphs to be comparable.

Originally made this as a idea to improve [CompareCSVsWithGraphs](https://github.com/corey-richardson/Compare-CSVs-With-Graphs) however the time steps between the customers real flight data and the in-house simulated flight test was not the same and so I did not fully flesh it out. (93,000+ values vs 900+ values)

That being said, it does work to compare FlightRadar24 data and so I have attached telemetry data from BY6700 and BY6701, EXT <--> ACE, 9/10/22 and 16/10/22

![altitude](https://github.com/corey-richardson/CompareSimilarCSVsSameGraph/blob/main/Output/Altitude.png "Altitude")
![speed](https://github.com/corey-richardson/CompareSimilarCSVsSameGraph/blob/main/Output/Speed.png "Speed")

