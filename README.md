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

To summarize, the following tasks were made to help Britta clean the data and perform an ETL:

1. Create a function to read in the three files and give it a name.
2. Open the Wikipedia JSON file and use the json.load() function to convert the JSON data to raw data.
3. Read in the raw Wikipedia movie data as a Pandas DataFrame.
4. Create a path to the Wikipedia data, the Kaggle metadata, and the MovieLens rating data files.
5. Convert all three files to a DataFrame.
6. Write a list comprehension to iterate through the cleaned wiki movies list.
7. Write a try-except block that will catch errors while extracting the IMDb IDs with a regular expression string and dropping any imdb_id duplicates. If there is an error, capture and print the exception.
8. Write a list comprehension to keep the columns that have non-null values from the DataFrame, then create a wiki_movies_df DataFrame from the list.
9. Create a variable that will hold all the non-null values from the "Box office" column.
10. Convert the box office data created to string values using the lambda and join functions.
11. Write a regular expression to match the six elements of form_one and form_two of the box office data.
12. Add the code that cleans the box office column in the wiki_movies_df DataFrame using the form_one and form_two lists.
13. Add code that cleans the "budget" column in the wiki_movies_df DataFrame.
14. Add code that cleans the "release" column in the wiki_movies_df DataFrame.
15. Add code that cleans the "running time" column in the wiki_movies_df DataFrame.
16. Use the variables provided to create a path to the Wikipedia data, the Kaggle metadata, and the MovieLens rating data files.
17. Set the wiki_movies_df equal to the wiki_file variable.
18. Merge the wiki_movies_df DataFrame and the kaggle_metadata DataFrames, then name the new DataFrame, movies_df.
19. Drop unnecessary columns from the movies_df DataFrame.
20. Add the fill_missing_kaggle_data() function that fills in the missing Kaggle data on the movies_df DataFrame.
21. Call the fill_missing_kaggle_data() function with the movies_df DataFrame and the Kaggle and Wikipedia columns to be cleaned as the arguments.
22. Filter the movies_df DataFrame to keep the necessary columns.
23. Rename the columns in the movies_df DataFrame.
24. Transform and merge the ratings DataFrame with the movies_df DataFrame, name the new DataFrame movies_with_ratings_df, then clean the movies_with_ratings_df DataFrame.
25. Use the variables provided to create a path to the Wikipedia data, the Kaggle metadata, and the MovieLens rating data files.
26. Add the code to create the connection to the PostgreSQL database, then add the movies_df DataFrame to a SQL database.
27. Add the code that prints out the elapsed time to import each row.
28. Run the program.
29. After the program has finished, run a query on the PostgreSQL database that retreives the number of rows for the movies and ratings tables.
