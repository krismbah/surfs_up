# surfs_up

## Overview

The purpose of this analysis is  to provide W. Avy with more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round. The following tasks are to be completed: 

1. Determine the Summary Statistics for June.
2. Determine the Summary Statistics for December.
3. A written report for the statistical analysis.

## Results

***Deliverable 1: Determine the Summary Statistics for June***
Using Python, Pandas functions and methods, and SQLAlchemy, filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June. Then, convert those temperatures to a list, create a DataFrame from the list, and generate the summary statistics.
- Filter the date column from the Measurement table to retrieve all the temperatures for the month of June.
- Convert the June temperatures to a list.
- Create a DataFrame from the list of temperatures for the month of June (Figure 1).
- Generate the summary statistics for the June temperatures DataFrame (Figure 2).

Figure 1:

![June_DF](https://raw.githubusercontent.com/krismbah/surfs_up/main/June_DF.png)

Figure 2:

![June_DF_Stat](https://raw.githubusercontent.com/krismbah/surfs_up/main/June_DF_Stat.png)



***Deliverable 2: Determine the Summary Statistics for December***
Using Python, Pandas functions and methods, and SQLAlchemy, filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of December. Then, convert those temperatures to a list, create a DataFrame from the list, and generate the summary statistics.
- Filter the date column from the Measurement table to retrieve all the temperatures for the month of June.
- Convert the June temperatures to a list.
- Create a DataFrame from the list of temperatures for the month of December (Figure 3).
- Generate the summary statistics for the December temperatures DataFrame (Figure 4).

Figure 3:

![Dec_DF](https://raw.githubusercontent.com/krismbah/surfs_up/main/Dec_DF.png)

Figure 4:

![Dec_DF_Stat](https://raw.githubusercontent.com/krismbah/surfs_up/main/Dec_DF_Stat.png)




## Summary

To summarize, the following temperature observations were made from the Oahu site:

1. For June, 1700 temperature observations were made with a mean average of 74 degrees and a standard deviation of 3.26 degrees.
2. For June, the minimum and maximum temperatures observed ranged from 64 to 85 degrees, respectively.
3. For June, 75 percent of all data points observed were 73 degrees and above.
4. The temparature range for June provides for great surfing with minimal need for a wetsuit.
5. For December, 1517 temperature observations were made with a mean average of 71 degrees and a standard deviation of 3.75 degrees.
6. For December, the minimum and maximum temperatures observed ranged from 56 to 83 degrees, respectively.
7. For December, 50 percent of all data points observed were 71 degrees and above.
8. The temparature range for December provides for great surfing. However, thicker wetsuits may be needed for half the month which should provide more revenue for the surf shop.
