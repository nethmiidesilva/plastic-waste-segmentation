import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    "./views/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
plastic_waste_segmentation_page = st.Page(
    "./views/plastic_waste_segmentation.py",
    title="Plastic Waste Segmentation",
    icon="🗑️",
)
realtime_plastic_waste_segmentation_page = st.Page(
    "./views/realtime_plastic_waste_segmentation.py",
    title="Real-time Plastic Waste Segmentation",
    icon="🌊",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [home_page],
        "Analysis": [plastic_waste_segmentation_page, realtime_plastic_waste_segmentation_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("./assets/omdena_jaipur_chapter.jpeg")
st.sidebar.image("./assets/omdena_logo.png")
st.sidebar.markdown("Made with ❤️ by Omdena Community")


# --- RUN NAVIGATION ---
pg.run()
