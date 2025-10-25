import streamlit as st

st.sidebar.title("Calcolatore Cartamodelli")
st.sidebar.header("Inserisci le misure")

# Input per pantaloni
st.sidebar.subheader("Pantaloni")
circonferenza_vita = st.sidebar.number_input("Circonferenza vita (cm)", min_value=50, max_value=150, step=1)
circonferenza_fianchi = st.sidebar.number_input("Circonferenza fianchi (cm)", min_value=50, max_value=150, step=1)
lunghezza_gamba = st.sidebar.number_input("Lunghezza gamba esterna (cm)", min_value=50, max_value=120, step=1)

# Calcoli (esempio semplice)
larghezza_vita = circonferenza_vita / 4 + 2  # Aggiungi margine
larghezza_fianchi = circonferenza_fianchi / 4 + 2

st.write("### Risultati per il cartamodello dei pantaloni")
st.write(f"Larghezza vita: {larghezza_vita} cm")
st.write(f"Larghezza fianchi: {larghezza_fianchi} cm")