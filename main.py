import streamlit as st

# --- Globale Session State Variablen ---
if "page" not in st.session_state:
    st.session_state.page = 0

if "selected_year" not in st.session_state:
    st.session_state.selected_year = None

if "selected_persons" not in st.session_state:
    st.session_state.selected_persons = 85

if "selected_digital_option" not in st.session_state:
    st.session_state.selected_digital_option = None

if "selected_content" not in st.session_state:
    st.session_state.selected_content = []

if "selected_storage" not in st.session_state:
    st.session_state.selected_storage = None

if "selected_size" not in st.session_state:
    st.session_state.selected_size = None

if "selected_cover" not in st.session_state:
    st.session_state.selected_cover = None


# --- Navigation zwischen den Seiten ---
def next_page():
    """Navigates to the next page and skips Format & Cover pages if 'Nur digital' is selected."""
    
    if st.session_state.page == 3:
        if st.session_state.selected_digital_option == "Nur digital":
            st.session_state.page = 5  # Skip pages 4 and 5
        else:
            st.session_state.page += 1

    elif st.session_state.page == 5:
        if st.session_state.selected_digital_option == "Nur digital":
            st.session_state.page = 8  # Skip pages 6 and 7
        else:
            st.session_state.page += 1

    elif st.session_state.page in [6, 7] and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 8  # Ensure direct jump if user somehow lands here

    else:
        st.session_state.page += 1

    st.experimental_rerun()  # 🔹 Forces Streamlit to refresh immediately after a page change


def prev_page():
    """Navigates to the previous page while considering 'Nur digital' selection."""
    
    if st.session_state.page == 8 and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 5  # Jump back to Speicherplatz selection

    elif st.session_state.page in [7, 6] and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 5  # Skip back to Speicherplatz page

    else:
        st.session_state.page -= 1

    st.experimental_rerun()  # 🔹 Forces Streamlit to refresh immediately after a page change


# --- Seiteninhalt ---
if st.session_state.page == 0:
    st.image("bildname.png", width=300)
    st.title("Berechne in unter 1 Minute wie viel dein Abibuch kostet!")
    st.button("Los geht's!", on_click=next_page)

elif st.session_state.page == 1:
    st.image("bildname.png", width=300)
    st.title("Mein Digitales Abibuch")
    st.subheader("Für welches Jahr ist dein Abibuch?")
    
    current_year = 2025
    years = [current_year - 1, current_year, current_year + 1, current_year + 2]
    
    st.session_state.selected_year = st.radio("Jahr auswählen", years)

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Weiter", on_click=next_page)

elif st.session_state.page == 2:
    st.image("bildname.png", width=300)
    st.title("Wie viele Personen sollen ein Abibuch bekommen?")

    st.session_state.selected_persons = st.slider("Anzahl Personen", min_value=1, max_value=170, value=85)
    st.write(f"**Anzahl Personen:** {st.session_state.selected_persons}")

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Weiter", on_click=next_page)

elif st.session_state.page == 3:
    st.image("bildname.png", width=300)
    st.title("Möchtest du eine digitale Version deines Abibuchs?")

    selected_option = st.radio("Digitale Version?", ["Ja", "Nein", "Nur digital"], 
                               index=["Ja", "Nein", "Nur digital"].index(st.session_state.selected_digital_option) 
                               if st.session_state.selected_digital_option else 0)

    # Update session state before proceeding
    if selected_option != st.session_state.selected_digital_option:
        st.session_state.selected_digital_option = selected_option  

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Weiter", on_click=next_page)

elif st.session_state.page == 4:
    st.image("bildname.png", width=300)
    st.title("Welche Inhalte möchtest du in deinem Abibuch?")
    
    options = ["Lehrer-Steckbriefe", "Schüler-Steckbriefe", "Videos", "Sprachmemos", 
               "Fotos", "Schüler-Rankings", "Lehrer-Rankings", "Klassenlisten"]
    
    st.session_state.selected_content = st.multiselect("Wähle Inhalte aus:", options)

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Weiter", on_click=next_page)

elif st.session_state.page == 5:
    st.image("bildname.png", width=300)
    st.title("Wie viel Speicherplatz benötigst du für deine digitale Version?")
    
    st.session_state.selected_storage = st.radio(
        "Speicherplatz wählen:", ["32GB", "64GB", "128GB"]
    )

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Weiter", on_click=next_page)

elif st.session_state.page == 6:
    st.image("bildname.png", width=300)
    st.title("Welche Maße soll dein Abibuch haben?")
    
    st.session_state.selected_size = st.radio(
        "Buchgröße wählen:", ["DIN A4 (210x297 mm)", "Buchformat (170x210 mm)"]
    )

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Weiter", on_click=next_page)

elif st.session_state.page == 7:
    st.image("bildname.png", width=300)
    st.title("Welche Art von Cover soll dein Abibuch haben?")

    st.session_state.selected_cover = st.radio(
        "Cover wählen:", ["Hard-Cover", "Soft-Cover"]
    )

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Weiter", on_click=next_page)

elif st.session_state.page == 8:
    st.image("bildname.png", width=300)
    st.title("Meine Auswahl")

    st.write(f"**Jahr:** {st.session_state.selected_year}")
    st.write(f"**Anzahl Personen:** {st.session_state.selected_persons}")
    st.write(f"**Digitale Version:** {st.session_state.selected_digital_option}")
    st.write(f"**Speicherplatz:** {st.session_state.selected_storage}")

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Bestätigen", on_click=lambda: st.success("Vielen Dank für deine Auswahl!"))

