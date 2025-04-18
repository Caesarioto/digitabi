import streamlit as st
from datetime import datetime

# --- Initialisieren ---
def init_state():
    for key, value in {
        "page": 1,
        "history": [],
        "selected_year": None,
        "selected_persons": None,
        "selected_digital_option": None,
        "selected_content": [],
        "selected_storage": None,
        "selected_cover": None,
        "selected_format": None,
    }.items():
        if key not in st.session_state:
            st.session_state[key] = value

# --- Navigation ---
def go_to_page(page):
    if st.session_state.page != page:
        st.session_state.history.append(st.session_state.page)
        st.session_state.page = page
        st.session_state._rerun = True

        # Workaround to trigger rerun after session state update
        st.experimental_rerun()

def go_back():
    if st.session_state.history:
        st.session_state.page = st.session_state.history.pop()
        st.experimental_rerun()

# --- Banner ---
def show_banner():
    st.markdown("<h1 style='text-align:center;'>\U0001F4D8 Mein Digitales Abibuch</h1><hr>", unsafe_allow_html=True)

# --- Seiten ---
def page_1():
    st.title("Berechne den Preis deines Abibuchs in einer Minute!")
    st.markdown("\n" * 3)
    if st.button("Los geht's!"):
        go_to_page(2)

def page_2():
    st.header("Für welches Jahr ist dein Abibuch?")
    current = datetime.now().year
    options = [current - 1, current, current + 1, current + 2]
    choice = st.radio("", options, key="year")
    if choice is not None:
        st.session_state.selected_year = choice
        go_to_page(3)
    st.button("Zurück", on_click=go_back)

def page_3():
    st.header("Wie viele Personen sollen ein Abibuch bekommen?")
    options = ["50-60", "61-70", "71-80", "81-90", "91-100", "101-110", "111-120", "120+"]
    choice = st.radio("", options, key="persons")
    st.info("Hinweis: Wie groß ist dein Jahrgang? Sollen Lehrer oder weitere Personen ebenfalls ein Abibuch erhalten?")
    if choice is not None:
        st.session_state.selected_persons = choice
        go_to_page(4)
    st.button("Zurück", on_click=go_back)

def page_4():
    st.header("Willst du eine digitale Version deines Abibuchs?")
    options = ["Ja", "Nein", "Ich will ausschließlich eine digitale Version"]
    choice = st.radio("", options, key="digital_option")
    if choice is not None:
        st.session_state.selected_digital_option = choice
        go_to_page(5)
    st.button("Zurück", on_click=go_back)

def page_5():
    st.header("Welche Inhalte sollen in deinem Abibuch sein?")
    opts = ["Schüler-Steckbriefe", "Lehrer-Steckbriefe", "lustige Zitate", "Videos",
            "Sprachmemos", "Fotos", "Schüler-Rankings", "Lehrer-Rankings", "Klassenlisten"]
    disabled = ["Videos", "Sprachmemos"] if st.session_state.selected_digital_option == "Nein" else []
    selected = []
    for o in opts:
        cols = st.columns([0.9, 0.1])
        with cols[0]:
            if st.checkbox(o, key=o, disabled=o in disabled):
                selected.append(o)
        with cols[1]:
            if o in disabled:
                st.markdown("❌")
                st.markdown("<span title='Nur bei digitaler Version verfügbar'>ℹ️</span>", unsafe_allow_html=True)
    st.session_state.selected_content = selected
    if st.button("Weiter"):
        if st.session_state.selected_digital_option in ["Ja", "Ich will ausschließlich eine digitale Version"]:
            go_to_page(6)
        else:
            go_to_page(7)
    st.button("Zurück", on_click=go_back)

def page_6():
    st.header("Wie viel Speicherplatz benötigst du?")
    options = ["32 GB", "64 GB", "124 GB", "248 GB"]
    choice = st.radio("", options, key="storage")
    if choice is not None:
        st.session_state.selected_storage = choice
        if st.session_state.selected_digital_option == "Ich will ausschließlich eine digitale Version":
            go_to_page(9)
        else:
            go_to_page(7)
    st.button("Zurück", on_click=go_back)

def page_7():
    st.header("Welches Cover soll dein Abibuch haben?")
    choice = st.radio("", ["Hard-Cover", "Soft-Cover"], key="cover")
    if choice is not None:
        st.session_state.selected_cover = choice
        go_to_page(8)
    st.button("Zurück", on_click=go_back)

def page_8():
    st.header("Welches Format soll dein Abibuch haben?")
    choice = st.radio("", ["DIN A4 (210x297 mm)", "Buchformat (170x240 mm)"], key="format")
    if choice is not None:
        st.session_state.selected_format = choice
        go_to_page(9)
    st.button("Zurück", on_click=go_back)

def page_9():
    st.header("Meine Auswahl")
    st.write(f"**Jahr:** {st.session_state.selected_year}")
    st.write(f"**Personenzahl:** {st.session_state.selected_persons}")
    st.write(f"**Digitaloption:** {st.session_state.selected_digital_option}")
    st.write(f"**Inhalte:** {', '.join(st.session_state.selected_content)}")
    if st.session_state.selected_digital_option in ["Ja", "Ich will ausschließlich eine digitale Version"]:
        st.write(f"**Speicherplatz:** {st.session_state.selected_storage}")
    if st.session_state.selected_digital_option != "Ich will ausschließlich eine digitale Version":
        st.write(f"**Cover:** {st.session_state.selected_cover}")
        st.write(f"**Format:** {st.session_state.selected_format}")
    st.success("Bitte überprüfe deine Angaben.")
    st.button("Zurück", on_click=go_back)

# --- Main ---
init_state()
show_banner()
page = st.session_state.page

pages = {
    1: page_1,
    2: page_2,
    3: page_3,
    4: page_4,
    5: page_5,
    6: page_6,
    7: page_7,
    8: page_8,
    9: page_9
}

if page in pages:
    pages[page]()

