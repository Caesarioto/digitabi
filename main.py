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
    """ Wechselt zur nächsten Seite und überspringt Format & Cover, falls 'Nur digital' gewählt wurde. """
    if st.session_state.page == 5 and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 8  # Springt direkt zur Zusammenfassung
    else:
        st.session_state.page += 1


def prev_page():
    """ Geht zur vorherigen Seite und berücksichtigt, ob 'Nur digital' gewählt wurde. """
    if st.session_state.page == 8 and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 5  # Springt zurück zur Speicherplatz-Seite
    elif st.session_state.page == 6 and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 5  # Falls Nutzer zurückgeht, springt er direkt zur Speicherplatz-Seite
    else:
        st.session_state.page -= 1


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
    
    st.session_state.selected_digital_option = st.radio(
        "Digitale Version?", ["Ja", "Nein", "Nur digital"]
    )

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

# Falls "Nur digital" gewählt wurde, wird Seite 6 & 7 übersprungen!
elif st.session_state.page == 6 and st.session_state.selected_digital_option != "Nur digital":
    st.image("bildname.png", width=300)
    st.title("Welche Maße soll dein Abibuch haben?")
    
    st.session_state.selected_size = st.radio(
        "Buchgröße wählen:", ["DIN A4 (210x297 mm)", "Buchformat (170x210 mm)"]
    )

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Weiter", on_click=next_page)

elif st.session_state.page == 7 and st.session_state.selected_digital_option != "Nur digital":
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
    st.write(f"**Ausgewählte Inhalte:** {', '.join(st.session_state.selected_content) if st.session_state.selected_content else 'Keine Auswahl'}")
    st.write(f"**Speicherplatz:** {st.session_state.selected_storage if st.session_state.selected_storage else 'Keine Auswahl'}")

    if st.session_state.selected_digital_option != "Nur digital":
        st.write(f"**Buchgröße:** {st.session_state.selected_size if st.session_state.selected_size else 'Keine Auswahl'}")
        st.write(f"**Cover:** {st.session_state.selected_cover if st.session_state.selected_cover else 'Keine Auswahl'}")

    col1, col2 = st.columns(2)
    col1.button("Zurück", on_click=prev_page)
    col2.button("Bestätigen", on_click=lambda: st.success("Vielen Dank für deine Auswahl!"))
