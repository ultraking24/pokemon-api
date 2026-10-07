#handles what the user sees
import streamlit as st
from main import get_poke

st.set_page_config(
    page_title = "Pokemon Retriever",
    page_icon="⚡",
    layout="wide"

)

if "search_history" not in st.session_state:
    st.session_state.search_history = []
if "current_pokemon" not in st.session_state:
    st.session_state.current_pokemon = []



st.title("POKEMON RETRIEVER")
st.header("Search")
with st.form("pokemon-search"):
    pokemon = st.text_input(
        "Enter a pokemon. See the data.",
        placeholder = "e.g pikachu"
    )
    submitted = st.form_submit_button("Search")
if submitted:
    pokemon_name = pokemon.strip().lower()
    if not pokemon_name:
        st.warning("Please enter a pokemon name.")
    else:
        with st.spinner("Searching for pokemon..."):
            data = get_poke(pokemon_name)

        if data:
            st.session_state.current_event = data
            if pokemon_name not in st.session_state.search_history:
                st.session_state.search_history.append(pokemon_name)
            st.subheader("Pokemon Information")
            tab1, tab2 = st.tabs([
                "Overview",
                "Types and Abilities",
                
            ])
            with tab1:
                st.image(data["sprites"]["front_default"])
                column1, column2, column3, column4 = st.columns(4, border = True)
                with column1:
                    st.metric("Name", data["name"].title())
                with column2:
                    st.metric("ID", data["id"])
                with column3:
                    st.metric("Height", data["height"])
                with column4:
                    st.metric("Weight", data["weight"])
            with tab2:
                type_column, ability_column = st.columns(2, border = True)
                with type_column:
                    st.subheader("Types")
                    for pokemon_type in data["types"]:
                        st.write(pokemon_type["type"]["name"].title())
                with ability_column:
                    st.subheader("Abilities")
                    for ability in data["abilities"]:
                        st.write(ability["ability"]["name"])
            

            

        else:
            st.error("Pokemon not found.")

with st.sidebar:
    st.header("Search History")
    for pokemon in st.session_state.search_history:
        st.write(pokemon.title())
    if st.button("Clear History"):
        st.write("History Cleared!")
        st.session_state.search_history.clear()
        st.rerun()




    



