import streamlit as st

bot_page = st.Page(
    page="pages/waterqualityqnabot.py",
    title="Water Quality Q&A Bot",
    icon=":material/robot_2:",
    default=True,
)
data_page = st.Page(
    page="pages/waterqualitydata.py",
    title="Water Quality Data",
    icon=":material/chart_data:"
)
testing_page = st.Page(
    page="pages/watertestmap.py",
    title="At Home Water Quality Testing And Map",
    icon=":material/map:"
)

st.logo("images/icon2.png")

pg = st.navigation(pages=[bot_page, data_page, testing_page])

pg.run()