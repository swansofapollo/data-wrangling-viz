import requests
import pandas as pd
import numpy as np
import streamlit as st
import bokeh
import plotly.express as px

yellow_df = pd.read_parquet("yellow_data.parquet")

col1, col2 = st.columns(2)

yellow_df.dropna(inplace=True)
print(len(yellow_df))
yellow_df.drop(['VendorID', 'RatecodeID', 'store_and_fwd_flag', 'PULocationID', 'DOLocationID','payment_type', 'extra','mta_tax', 'tolls_amount', 'improvement_surcharge','congestion_surcharge', 'airport_fee'], axis=1, inplace=True)
# yellow_df.head()

df = yellow_df.sample(n = 10000)
with col1:
    st.dataframe(yellow_df)
    st.write('Random sample of initial data. 19 columns x 10000 rows')
# df.head()



df['hours'] = df.tpep_pickup_datetime.dt.hour
df['day'] = df.tpep_pickup_datetime.dt.dayofweek
# df.head()

data = {"day": ["Mon", "Tue", 'Wed' , "Thu", "Fri", "Sat", 'Sun'], "12AM": [0, 0, 0,0,0,0,0], "1AM": [0, 0, 0,0,0,0,0], "2AM": [0, 0, 0,0,0,0,0], "3AM": [0, 0, 0,0,0,0,0], "4AM": [0, 0, 0,0,0,0,0], "5AM": [0, 0, 0,0,0,0,0], "6AM": [0, 0, 0,0,0,0,0], "7AM": [0, 0, 0,0,0,0,0], "8AM": [0, 0, 0,0,0,0,0], "9AM": [0, 0, 0,0,0,0,0], "10AM": [0, 0, 0,0,0,0,0], "11AM": [0, 0, 0,0,0,0,0], "12PM": [0, 0, 0,0,0,0,0], "1PM": [0, 0, 0,0,0,0,0], "2PM": [0, 0, 0,0,0,0,0], "3PM": [0, 0, 0,0,0,0,0], "4PM": [0, 0, 0,0,0,0,0], "5PM": [0, 0, 0,0,0,0,0], "6PM": [0, 0, 0,0,0,0,0], "7PM": [0, 0, 0,0,0,0,0], "8PM": [0, 0, 0,0,0,0,0], "9PM": [0, 0, 0,0,0,0,0], "10PM": [0, 0, 0,0,0,0,0], "11PM": [0, 0, 0,0,0,0,0]}
df_sum = pd.DataFrame(data)
df_sum.set_index('day', inplace=True)
df_count = pd.DataFrame(data)
df_count.set_index('day', inplace=True)


for i in range(len(df)):
    if float(df.iat[i, 6]) != 0:
        percent = abs(float(df.iat[i, 5])*100/float(df.iat[i, 6]))
        df_sum.iat[df.iat[i, 8]%7,df.iat[i,7]] += percent
        df_count.iat[df.iat[i, 8]%7,df.iat[i,7]] += 1
# print(df_sum)
# print(df_count) 
for i in range(len(df_sum)):
    for j in range(len(df_sum.columns)):
        if (float(df_sum.iat[i,j]) != 0) and (df_sum.iat[i,j] is not np.nan):
            # print(df_sum.columns[i], j, df_sum.iat[i,j], df_count.iat[i, j])
            df_sum.iat[i,j] = float(df_sum.iat[i,j])/int(df_count.iat[i,j])
        # else: 
        #     print(i, j, float(df_sum.iat[i,j]))
    
# print(df_sum)

# st.bokeh_chart(df_sum)
with col2:
    with st.container():
        fig = px.imshow(df_sum)
        st.plotly_chart(fig)
        st.write("Heatmap that shows correlation between time of the day and percentage of the tip leaved")
    with st.container():
        fig = px.imshow(df_count)
        st.plotly_chart(fig)
        st.write("Heatmap that shows correlation between time of the day and amount of ordering a taxi")