import streamlit as st
from datetime import datetime

# --- Session State Initialization ---
defaults = {
    "page": 1,
    "history": [],
    "selected_year": None,
    "selected_persons": None,
    "selected_digital_option": None,
    "selected_content": [],
    "selected_storage": None,
    "selected_cover": None,
    "selected_format": None,
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- Navigation ---
def go_to_page(new_page):
    if st.session_state.page != new_page:
        st.session_state.history.append(st.session_state.page)
        st.session_state.page = new_page
        st.rerun()

def go_back():
    if st.session_state.history:
        st.session_state.page = st.session_state.history.pop()
        st.rerun()

# --- Banner ---
st.markdown("<h1 style='text-align:center;'>📘 Mein Digitales Abibuch</h1><hr>", unsafe_allow_html=True)

# --- Seite 1 ---
if st.session_state.page == 1:
    st.title("Berechne den Preis deines Abibuchs in einer Minute!")
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.button("Los geht’s!", on_click=lambda: go_to_page(2))
    st.markdown("</div>", unsafe_allow_html=True)

# --- Seite 2: Jahr ---
elif st.session_state.page == 2:
    st.header("Für welches Jahr ist dein Abibuch?")
    current_year = datetime.now().year
    years = [current_year - 1, current_year, current_year + 1, current_year + 2]
    st.session_state.selected_year = st.radio("Wähle das Jahr:", years)
    if st.session_state.selected_year:
        go_to_page(3)
    st.button("Zurück", on_click=go_back)

# --- Seite 3: Personenanzahl ---
elif st.session_state.page == 3:
    st.header("Wie viele Personen sollen ein Abibuch bekommen?")
    st.session_state.selected_persons = st.radio(
        "Anzahl wählen:",
        ["50-60", "61-70", "71-80", "81-90", "91-100", "101-110", "111-120", "120+"]
    )
    st.info("Hinweis: Wie groß ist dein Jahrgang? Sollen Lehrer oder weitere Personen ebenfalls ein Abibuch erhalten?")
    if st.session_state.selected_persons:
        go_to_page(4)
    st.button("Zurück", on_click=go_back)

# --- Seite 4: Digital-Version ---
elif st.session_state.page == 4:
    st.header("Willst du eine digitale Version deines Abibuchs?")
    st.session_state.selected_digital_option = st.radio(
        "Digitale Version?",
        ["Ja", "Nein", "Ich will ausschließlich eine digitale Version"]
    )
    if st.session_state.selected_digital_option:
        go_to_page(5)
    st.button("Zurück", on_click=go_back)

# --- Seite 5: Inhalte ---
elif st.session_state.page == 5:
    st.header("Welche Inhalte sollen in deinem Abibuch sein?")
    options = [
        "Schüler-Steckbriefe", "Lehrer-Steckbriefe", "lustige Zitate", "Videos",
        "Sprachmemos", "Fotos", "Schüler-Rankings", "Lehrer-Rankings", "Klassenlisten"
    ]

    disabled = []
    if st.session_state.selected_digital_option == "Nein":
        disabled = ["Videos", "Sprachmemos"]

    selected = []
    for opt in options:
        cols = st.columns([0.9, 0.1])
        with cols[0]:
            if st.checkbox(opt, key=opt, disabled=opt in disabled):
                selected.append(opt)
        with cols[1]:
            if opt in disabled:
                st.markdown("❌")
                st.markdown(
                    "<span title='Nur bei digitaler Version verfügbar'>ℹ️</span>",
                    unsafe_allow_html=True,
                )
    st.session_state.selected_content = selected

    if st.button("Weiter"):
        if st.session_state.selected_digital_option in ["Ja", "Ich will ausschließlich eine digitale Version"]:
            go_to_page(6)
        else:
            go_to_page(7)
    st.button("Zurück", on_click=go_back)

# --- Seite 6: Speicherplatz ---
elif st.session_state.page == 6:
    st.header("Wie viel Speicherplatz benötigst du?")
    st.session_state.selected_storage = st.radio(
        "Speicher wählen:",
        ["32 GB", "64 GB", "124 GB", "248 GB"]
    )
    if st.session_state.selected_storage:
        if st.session_state.selected_digital_option == "Ja":
            go_to_page(7)
        else:
            go_to_page(9)
    st.button("Zurück", on_click=go_back)

# --- Seite 7: Cover ---
elif st.session_state.page == 7:
    st.header("Welches Cover soll dein Abibuch haben?")
    st.session_state.selected_cover = st.radio("Cover wählen:", ["Hard-Cover", "Soft-Cover"])
    if st.session_state.selected_cover:
        go_to_page(8)
    st.button("Zurück", on_click=go_back)

# --- Seite 8: Format ---
elif st.session_state.page == 8:
    st.header("Welches Format soll dein Abibuch haben?")
    st.session_state.selected_format = st.radio(
        "Format wählen:",
        ["DIN A4 (210x297 mm)", "Buchformat (170x240 mm)"]
    )
    if st.session_state.selected_format:
        go_to_page(9)
    st.button("Zurück", on_click=go_back)

# --- Seite 9: Zusammenfassung ---
elif st.session_state.page == 9:
    st.header("Meine Auswahl")
    st.write(f"**Jahr:** {st.session_state.selected_year}")
    st.write(f"**Personenzahl:** {st.session_state.selected_persons}")
    st.write(f"**Digitaloption:** {st.session_state.selected_digital_option}")
    st.write(f"**Inhalte:** {', '.join(st.session_state.selected_content)}")
    if st.session_state.selected_digital_option in ["Ja", "Ich will ausschließlich eine digitale Version"]:
        st.write(f"**Speicher:** {st.session_state.selected_storage}")
    if st.session_state.selected_digital_option != "Ich will ausschließlich eine digitale Version":
        st.write(f"**Cover:** {st.session_state.selected_cover}")
        st.write(f"**Format:** {st.session_state.selected_format}")
    st.success("Bitte überprüfe deine Angaben.")
    st.button("Zurück", on_click=go_back)


