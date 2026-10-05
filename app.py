#handles what the user sees
import streamlit as st
from main import get_poke

st.title("POKEMON RETRIEVER")
st.header("Search")
pokemon = st.text_input("Enter a pokemon. See the data.")



if st.button("Search"):
    data = get_poke(pokemon.lower())
    if data:
        st.subheader("Pokemon Information")
        column1, column2, column3, column4, column5 = st.columns(5, border = True)
        with column1:
            st.write(f'Name: {data["name"]}')
        with column2:
            st.write(f'ID: {data["id"]}')
        with column3:
            st.write(f'Height: {data["height"]}')
        with column4:
            st.write(f'Weight: {data["weight"]}')
        with column5:
            with st.container():
                st.write("Types:")
                for pokemon_type in data["types"]:
                    st.write(pokemon_type["type"]["name"])
                st.divider()
                st.write("Abilities:")
                for ability in data["abilities"]:
                    st.write(ability["ability"]["name"])

    else:
        st.error("Pokemon not found.")




    



