import streamlit as st

# --- Session State Initialization ---
if "page" not in st.session_state:
    st.session_state.page = 0

if "history" not in st.session_state:
    st.session_state.history = []  # Tracks visited pages

if "selected_year" not in st.session_state:
    st.session_state.selected_year = None

if "selected_persons" not in st.session_state:
    st.session_state.selected_persons = None

if "selected_digital_option" not in st.session_state:
    st.session_state.selected_digital_option = None

if "selected_content" not in st.session_state:
    st.session_state.selected_content = []

if "selected_storage" not in st.session_state:
    st.session_state.selected_storage = None

if "selected_cover" not in st.session_state:
    st.session_state.selected_cover = None

if "selected_format" not in st.session_state:
    st.session_state.selected_format = None


# --- Navigation Functions ---
def go_to_page(new_page):
    """Handles page navigation and stores history for the back button."""
    if st.session_state.page != new_page:
        st.session_state.history.append(st.session_state.page)
        st.session_state.page = new_page
        st.rerun()


def go_back():
    """Moves back to the last visited page."""
    if st.session_state.history:
        st.session_state.page = st.session_state.history.pop()
        st.rerun()


# --- UI Pages ---
st.title("Mein Digitales Abibuch")

# --- Page 0: Start Page ---
if st.session_state.page == 0:
    st.image("bildname.png", width=300)
    st.title("Berechne den Preis deines Abibuchs in einer Minute!")
    st.button("Los geht's!", on_click=lambda: go_to_page(1))

# --- Page 1: Select Year ---
elif st.session_state.page == 1:
    st.subheader("Für welches Jahr ist dein Abibuch?")
    current_year = 2025
    years = [current_year - 1, current_year, current_year, current_year + 1, current_year + 2]

    st.session_state.selected_year = st.radio("Jahr auswählen:", years, on_change=lambda: go_to_page(2))

    st.button("Zurück", on_click=go_back)

# --- Page 2: Select Number of People ---
elif st.session_state.page == 2:
    st.subheader("Wie viele Personen sollen ein Abibuch bekommen?")
    st.session_state.selected_persons = st.radio(
        "Anzahl der Personen:",
        ["50-60", "61-70", "71-80", "81-90", "91-100", "101-110", "111-120", "120+"],
        on_change=lambda: go_to_page(3),
    )

    st.markdown("ℹ️ **Hinweis:** Wie groß ist dein Jahrgang? Sollen Lehrer oder weitere Personen ebenfalls ein Abibuch erhalten?")
    st.button("Zurück", on_click=go_back)

# --- Page 3: Digital Version Selection ---
elif st.session_state.page == 3:
    st.subheader("Willst du eine digitale Version deines Abibuchs?")
    st.session_state.selected_digital_option = st.radio(
        "Digitale Version?",
        ["Ja", "Nein", "Ich will ausschließlich eine digitale Version"],
        on_change=lambda: go_to_page(4),
    )

    st.button("Zurück", on_click=go_back)

# --- Page 4: Select Content (Checkboxes) ---
elif st.session_state.page == 4:
    st.subheader("Welche Inhalte sollen in deinem Abibuch sein?")

    options = ["Schüler-Steckbriefe", "Lehrer-Steckbriefe", "lustige Zitate", "Videos",
               "Sprachmemos", "Fotos", "Schüler-Rankings", "Lehrer-Rankings", "Klassenlisten"]

    disabled_options = ["Videos", "Sprachmemos"] if st.session_state.selected_digital_option == "Nein" else []

    selected_content = []
    for option in options:
        disabled = option in disabled_options
        col1, col2 = st.columns([8, 1])
        with col1:
            if st.checkbox(option, key=option, disabled=disabled):
                selected_content.append(option)
        with col2:
            if disabled:
                st.markdown("❌")
                st.markdown("<span title='Nur bei digitaler Version verfügbar'>ℹ️</span>", unsafe_allow_html=True)

    st.session_state.selected_content = selected_content

    next_page = 5 if st.session_state.selected_digital_option in ["Ja", "Ich will ausschließlich eine digitale Version"] else 6
    st.button("Weiter", on_click=lambda: go_to_page(next_page))
    st.button("Zurück", on_click=go_back)

# --- Page 5: Select Storage (Only if Digital is Chosen) ---
elif st.session_state.page == 5:
    st.subheader("Wie viel Speicherplatz benötigst du?")
    st.session_state.selected_storage = st.radio(
        "Speicherplatz wählen:",
        ["32GB", "64GB", "124GB", "248GB"],
        on_change=lambda: go_to_page(6 if st.session_state.selected_digital_option == "Ja" else 8),
    )

    st.button("Zurück", on_click=go_back)

# --- Page 6: Select Cover (Only for Print Versions) ---
elif st.session_state.page == 6:
    st.subheader("Welches Cover soll dein Abibuch haben?")
    st.session_state.selected_cover = st.radio(
        "Cover wählen:",
        ["Hard-Cover", "Soft-Cover"],
        on_change=lambda: go_to_page(7),
    )

    st.button("Zurück", on_click=go_back)

# --- Page 7: Select Format (Only for Print Versions) ---
elif st.session_state.page == 7:
    st.subheader("Welches Format soll dein Abibuch haben?")
    st.session_state.selected_format = st.radio(
        "Format wählen:",
        ["DIN A4 (210x297 mm)", "Buchformat (170x240 mm)"],
        on_change=lambda: go_to_page(8),
    )

    st.button("Zurück", on_click=go_back)

# --- Page 8: Summary Page ---
elif st.session_state.page == 8:
    st.subheader("Meine Auswahl")
    st.write(f"**Jahr:** {st.session_state.selected_year}")
    st.write(f"**Anzahl Personen:** {st.session_state.selected_persons}")
    st.write(f"**Digitale Version:** {st.session_state.selected_digital_option}")
    st.write(f"**Inhalte:** {', '.join(st.session_state.selected_content)}")
    if st.session_state.selected_digital_option in ["Ja", "Ich will ausschließlich eine digitale Version"]:
        st.write(f"**Speicherplatz:** {st.session_state.selected_storage}")
    if st.session_state.selected_digital_option != "Ich will ausschließlich eine digitale Version":
        st.write(f"**Cover:** {st.session_state.selected_cover}")
        st.write(f"**Format:** {st.session_state.selected_format}")

    st.button("Zurück", on_click=go_back)
    st.button("Bestätigen", on_click=lambda: st.success("Vielen Dank für deine Auswahl!"))





