# Data Wrangling and Visualization Assignment

1. Got the NYC Taxi Data from https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page using the requests library (Url: https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet).
2. Cleaned data by dropping extra columns and lines that contain any Nan (I had 3 million lines of data, I can legally do it). Data had the highest usability rating so it was no problem dealing with it.
3. Used the streamlit library for simple and beautiful visualization of the data. 

To launch the site and see for yourself, run 
streamlit run streamlit.py in the console and visit localhost:8501.

![Alt text](https://github.com/swansofapollo/data-wrangling-viz/blob/main/pic1.png)