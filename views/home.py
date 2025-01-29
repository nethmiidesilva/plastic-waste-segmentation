import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- MAIN TITLE ---
st.title("Omdena Jaipur Chapter", anchor=False)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
with col1:
    st.image("./assets/omdena_jaipur_chapter.jpeg", use_container_width=True)

with col2:
    st.write("### Protect Ganges River with Artificial Intelligence 🌊")
    st.write(
        """
        Welcome to the Jaipur Chapter of Omdena, where we leverage AI to protect 
        the Ganges River by intercepting as much  plastic wastes as possible. Join us in making a difference with cutting-edge technology and teamwork.
        """
    )
    if st.button("✉️ Contact Us"):
        show_contact_form()

