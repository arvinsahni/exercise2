Step-by-Step Instructions

Once you have your EC2 instance running ( AMI used UCB W205 Spring Ex 2 Image ) , you can follow the below steps to get the application running

1. Start postgres using /data/start_postgres.sh

2. Create a new database called tcount by running the file db_create.py 

3. Create a new table  called tweetwordcount by running the file table_create.py

4. Login into postgres as postgres user to create a user-defined function up_in as shown in file  up_in.sql

5. Storm/Python Project tweetwordcount can now be run by changing directory from root to tweetwordcount and then executing sparse run .Twitter credentials have already been added to the files under the project .

6. Once the program is run, the table created earlier (tweetwordcount) would now be populated

7. You can run finalresults.py with or without any input word parameter. If no word is supplied , it gives all the words and their counts ordered alphabetically . If a word is specified, it shows only the record from the table for that word. In case the word doesn’t exist in the table, it will print a message to the user saying “not found in the table”

8. You can also run histogram.py by giving two input parameters k1 and k2. It will show all the words whose counts lie between k1 and k2. In case no such word doesn’t exist in the table, it will print a message to the user saying “not found in the table” .
If only one or no input parameters are provided, it will throw a message for the user saying “check the parameters passed”

9. top_twenty.py was used to create the bar chart for the top 20 words (by count) in the twitter stream. Plotly was used for this and if credentials are asked when viewing the bar chart on the plotly webpage, you may use the one provided in the top_twenty.py file as a comment.

Note: It is a known issue in plotly that bar charts cant be sorted and given that i used a dictionary in the code for storing the x -axis and y-axis values, sorting was not done at that step either.
Hence the top twenty may not be displayed in the right order amongst themselves

