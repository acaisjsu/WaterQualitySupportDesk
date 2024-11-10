import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("How to Test Water at Home")
st.divider()
option = st.selectbox(
    "What kinds of water test would you like to know about?",
    ("Water Test Kits", "Boiling Test", "Smell and Look Test"),
)
if option == "Water Test Kits":
    st.write("Home water testing kits are readily available in stores and are used to test water for contaminants. They test for things like pH, hardness, chlorine, nitrates, and bacteria.")
if option == "Boiling Test":
    st.write("You can boil water for more than a minute to kill off most harmfull bacteria that may be in the water. Boiling won't get rid of heavy metals or chemical contaminants that may be in the water.")
if option == "Smell and Look Test":
    st.write("The smell and look of the water can be an indicator of quality. Cloudiness can show that the water has high mineral content or contamination. Rotten egg smell can indicate bacteria or hydrogen sulfide.")

st.divider()
# Define store locations with coordinates
locations = [
    {"name": "Blossom Hill Road Home Depot", "lat": 37.2442, "lon": -121.8378, "address": "920 Blossom Hill Rd, San Jose, CA 95123"},
    {"name": "Hillsdale Avenue Home Depot", "lat": 37.2731, "lon": -121.9236, "address": "1855 Hillsdale Ave, San Jose, CA 95124"},
    {"name": "Capitol Expressway Home Depot", "lat": 37.2777, "lon": -121.8602, "address": "635 W Capitol Expy, San Jose, CA 95136"},
    {"name": "Monterey Highway Home Depot", "lat": 37.3067, "lon": -121.8649, "address": "2181 Monterey Hwy, San Jose, CA 95125"},
    {"name": "De Anza Boulevard Home Depot", "lat": 37.3072, "lon": -122.0313, "address": "975 S De Anza Blvd, San Jose, CA 95129"},
    {"name": "Story Road Home Depot", "lat": 37.3542, "lon": -121.8204, "address": "2855 Story Rd, San Jose, CA 95127"},
    {"name": "Story Road Walmart", "lat": 37.3389, "lon": -121.8461, "address": "777 Story Rd, San Jose, CA 95122"},
    {"name": "Monterey Road Walmart", "lat": 37.3086, "lon": -121.8609, "address": "1450 Monterey Rd, San Jose, CA 95110"},
    {"name": "Stevens Creek Boulevard Walmart", "lat": 37.3235, "lon": -122.0004, "address": "4080 Stevens Creek Blvd, San Jose, CA 95129"},
    {"name": "Almaden Expressway Walmart", "lat": 37.2507, "lon": -121.8882, "address": "5095 Almaden Expy, San Jose, CA 95118"},
    {"name": "Evergreen Village Square Walmart", "lat": 37.3134, "lon": -121.7569, "address": "4055 Evergreen Village Square, San Jose, CA 95135"},
]

# Initialize the map centered around San Jose
m = folium.Map(location=[37.3, -121.86], zoom_start=11)

# Add red dot markers to the map
for store in locations:
    folium.CircleMarker(
        location=[store["lat"], store["lon"]],
        radius=5,                  # Size of the dot
        color='red',               # Border color of the circle
        fill=True,
        fill_color='red',          # Fill color of the circle
        fill_opacity=0.8,          # Transparency
        popup=folium.Popup(f"<b>{store['name']}</b><br>{store['address']}", max_width=250),
        tooltip=store["name"]
    ).add_to(m)

# Display the map in Streamlit
st.title("Store Locations That Sell Water Test Kits in San Jose :material/map:")
st_folium(m, width=725, height=500)