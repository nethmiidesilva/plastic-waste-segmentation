import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    "C:/Users/Dell User/OneDrive/Desktop/JaipurIndia/JaipurIndia_GangesRiverPlasticInterceptor-main/views/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
plastic_waste_segmentation_page = st.Page(
    "C:/Users/Dell User/OneDrive/Desktop/JaipurIndia/JaipurIndia_GangesRiverPlasticInterceptor-main/views/plastic_waste_segmentation.py",
    title="Plastic Waste Segmentation",
    icon="🗑️",
)
realtime_plastic_waste_segmentation_page = st.Page(
    "C:/Users/Dell User/OneDrive/Desktop/JaipurIndia/JaipurIndia_GangesRiverPlasticInterceptor-main/views/realtime_plastic_waste_segmentation.py",
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
st.logo("C:/Users/Dell User/OneDrive/Desktop/JaipurIndia/JaipurIndia_GangesRiverPlasticInterceptor-main/assets/omdena_jaipur_chapter.jpeg")
st.sidebar.image("C:/Users/Dell User/OneDrive/Desktop/JaipurIndia/JaipurIndia_GangesRiverPlasticInterceptor-main/assets/omdena_logo.png")
st.sidebar.markdown("Made with ❤️ by Omdena Community")


# --- RUN NAVIGATION ---
pg.run()
