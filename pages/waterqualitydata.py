import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

import os
import openai
import streamlit as st
from openai import OpenAI

st.title("Water Quality Data For Locations in San Jose :material/chart_data:")
st.divider()

data = pd.read_csv('pages/data/san_jose_water_quality_data.csv')

st.write(data.head())
openai.api_key = os.environ

client = OpenAI()

locations_ph = data.groupby('Location')['pH Level'].mean().nlargest(5)
locations_oxygen = data.groupby('Location')['Dissolved Oxygen (mg/L)'].mean().nlargest(5)
locations_turbidity = data.groupby('Location')['Turbidity (NTU)'].mean().nlargest(5)
locations_nitrate = data.groupby('Location')['Nitrate Levels (mg/L)'].mean().nlargest(5)
locations_phosphate = data.groupby('Location')['Phosphate Levels (mg/L)'].mean().nlargest(5)

sns.barplot(x=locations_ph.index, y=locations_ph.values)
plt.title('Average pH')
plt.ylabel('pH Level')
plt.xlabel('Location')
plt.xticks(rotation=45)

sns.barplot(x=locations_oxygen.index, y=locations_oxygen.values)
plt.title('Average Dissolved Oxygen Levels')
plt.ylabel('Dissolved Oxygen (mg/L)')
plt.xlabel('Location')
plt.xticks(rotation=45)

sns.barplot(x=locations_turbidity.index, y=locations_turbidity.values)
plt.title('Average Turbidity')
plt.ylabel('Turbidity (NTU)')
plt.xlabel('Location')
plt.xticks(rotation=45)

sns.barplot(x=locations_nitrate.index, y=locations_nitrate.values)
plt.title('Average Nitrate Levels')
plt.ylabel('Nitrate Levels (mg/L)')
plt.xlabel('Location')
plt.xticks(rotation=45)

sns.barplot(x=locations_phosphate.index, y=locations_phosphate.values)
plt.title('Average Phosphate Levels')
plt.ylabel('Phosphate Levels (mg/L)')
plt.xlabel('Location')
plt.xticks(rotation=45)


st.subheader("Average pH Level Bar Chart")
st.bar_chart(locations_ph, use_container_width=True)
st.subheader("Average Dissolved Oxygen Bar Chart")
st.bar_chart(locations_oxygen, use_container_width=True)
st.subheader("Average Turbidity Bar Chart")
st.bar_chart(locations_turbidity, use_container_width=True)
st.subheader("Average Nitrate Level Bar Chart")
st.bar_chart(locations_nitrate, use_container_width=True)
st.subheader("Average Phosphate Level Bar Chart")
st.bar_chart(locations_phosphate, use_container_width=True)

st.divider()
st.subheader("What Could This Data Mean?")
prompt = (
    f"The location with the highest average level of ph, dissolved oxygen, turbidity, nitrate, and phosphate are: "
    f"{', '.join(locations_ph.index)}. "
    f"{', '.join(locations_oxygen.index)}. "
    f"{', '.join(locations_turbidity.index)}. "
    f"{', '.join(locations_nitrate.index)}. "
    f"{', '.join(locations_phosphate.index)}. "
    "What could be the contributing factors to these levels of ph, dissolved oxygen, turbidity, nitrate, and phosphate. "
    "and its implications on the quality of the water for humans?"
)

def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": prompt},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

st.write(get_completion(prompt))