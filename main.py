import streamlit as st 

# --- Globale Session State Variablen ---
defaults = {
    "page": 0,
    "selected_year": None,
    "selected_persons": 85,
    "selected_digital_option": None,
    "selected_content": [],
    "selected_storage": None,
    "selected_size": None,
    "selected_cover": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --- Helper Funktionen ---
def show_header():
    """Zeigt das allgemeine Header-Bild und ein optionales Titelbild."""
    st.image("bildname.png", width=300)

def next_page():
    """Wechselt zur nächsten Seite, berücksichtigt 'Nur digital'- oder 'Nein'-Option."""
    if st.session_state.page == 4 and st.session_state.selected_digital_option == "Nein":
        st.session_state.page = 6  # Überspringe Speicherplatz bei "Nein"
    elif st.session_state.page == 5 and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 8  # Überspringe Format & Cover bei "Nur digital"
    else:
        st.session_state.page += 1


def prev_page():
    """Geht zur vorherigen Seite, berücksichtigt 'Nur digital'-Option."""
    if st.session_state.page == 8 and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 5  
    elif st.session_state.page == 6 and st.session_state.selected_digital_option == "Nur digital":
        st.session_state.page = 5  
    else:
        st.session_state.page = max(0, st.session_state.page - 1)

# --- Seiteninhalt ---
show_header()
progress = st.progress(st.session_state.page / 8)  # Fortschrittsanzeige

if st.session_state.page == 0:
    st.title("Berechne in unter 1 Minute wie viel dein Abibuch kostet!")
    st.button("Los geht's!", on_click=next_page)

elif st.session_state.page == 1:
    st.title("Mein Digitales Abibuch")
    st.subheader("Für welches Jahr ist dein Abibuch?")
    years = [2024, 2025, 2026, 2027]
    st.session_state.selected_year = st.radio("Jahr auswählen", years)
    st.button("Weiter", on_click=next_page)

elif st.session_state.page == 2:
    st.title("Wie viele Personen sollen ein Abibuch bekommen?")
    st.session_state.selected_persons = st.slider("Anzahl Personen", 1, 170, 85)
    st.button("Weiter", on_click=next_page)

elif st.session_state.page == 3:
    st.title("Möchtest du eine digitale Version deines Abibuchs?")
    st.session_state.selected_digital_option = st.radio("Digitale Version?", ["Ja", "Nein", "Nur digital"])
    st.button("Weiter", on_click=next_page)

elif st.session_state.page == 4:
    st.title("Welche Inhalte möchtest du in deinem Abibuch?")

    all_options = ["Lehrer-Steckbriefe", "Schüler-Steckbriefe", "Videos", "Sprachmemos",
                   "Fotos", "Schüler-Rankings", "Lehrer-Rankings", "Klassenlisten"]

    # Wenn "Nein" bei digital gewählt wurde → keine Videos & Sprachmemos
    if st.session_state.selected_digital_option == "Nein":
        options = [opt for opt in all_options if opt not in ["Videos", "Sprachmemos"]]
    else:
        options = all_options

    st.session_state.selected_content = st.multiselect("Wähle Inhalte aus:", options)
    st.button("Weiter", on_click=next_page)


elif st.session_state.page == 5:
    st.title("Wie viel Speicherplatz benötigst du für deine digitale Version?")
    st.session_state.selected_storage = st.radio("Speicherplatz wählen:", ["32GB", "64GB", "128GB"])
    st.button("Weiter", on_click=next_page)

elif st.session_state.page == 6 and st.session_state.selected_digital_option != "Nur digital":
    st.title("Welche Maße soll dein Abibuch haben?")
    st.session_state.selected_size = st.radio("Buchgröße wählen:", ["DIN A4 (210x297 mm)", "Buchformat (170x210 mm)"])
    st.button("Weiter", on_click=next_page)

elif st.session_state.page == 7 and st.session_state.selected_digital_option != "Nur digital":
    st.title("Welche Art von Cover soll dein Abibuch haben?")
    st.session_state.selected_cover = st.radio("Cover wählen:", ["Hard-Cover", "Soft-Cover"])
    st.button("Weiter", on_click=next_page)

elif st.session_state.page == 8:
    st.title("Meine Auswahl")
    st.write(f"**Jahr:** {st.session_state.selected_year}")
    st.write(f"**Anzahl Personen:** {st.session_state.selected_persons}")
    st.write(f"**Digitale Version:** {st.session_state.selected_digital_option}")
    st.write(f"**Inhalte:** {', '.join(st.session_state.selected_content) if st.session_state.selected_content else 'Keine Auswahl'}")
    st.write(f"**Speicherplatz:** {st.session_state.selected_storage if st.session_state.selected_storage else 'Keine Auswahl'}")
    if st.session_state.selected_digital_option != "Nur digital":
        st.write(f"**Buchgröße:** {st.session_state.selected_size if st.session_state.selected_size else 'Keine Auswahl'}")
        st.write(f"**Cover:** {st.session_state.selected_cover if st.session_state.selected_cover else 'Keine Auswahl'}")
    st.button("Bestätigen", on_click=lambda: st.success("Vielen Dank für deine Auswahl!"))
