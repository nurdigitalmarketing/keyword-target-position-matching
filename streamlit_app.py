import streamlit as st
import pandas as pd

# Titolo dell'applicazione
st.title('Keyword Search Streamlit Application')

# Introduzione e descrizione dell'applicazione
st.markdown("""
## 👉🏼 Description
This Streamlit application is designed to facilitate the search for specific keywords within an Excel file, providing a simple yet powerful tool for analyzing and extracting data based on user-defined keywords.
""")

# Campo di testo per inserire le parole chiave target, una per riga
keyword_input = st.text_area("Inserisci parole chiave target (una per riga):")

# Converti l'input dell'utente in una lista di parole chiave
keywords = [keyword.strip() for keyword in keyword_input.split('\n') if keyword]

# Widget di caricamento file
uploaded_file = st.file_uploader("Carica il file Excel:", type=['xlsx'])

if uploaded_file is not None and keywords:
    # Leggi il contenuto del file Excel in un DataFrame
    df = pd.read_excel(uploaded_file)

    # Funzione per cercare le corrispondenze esatte delle parole chiave e ottenere posizioni e URL
    # Assicurati che ogni parola chiave venga riportata una sola volta con la posizione più alta
    def search_keywords(df, keywords):
        results = {}
        for keyword in keywords:
            matched_rows = df[df['Keyword'].str.lower() == keyword.lower()].sort_values(by='Position')
            if not matched_rows.empty:
                # Prendi solo la prima riga (posizione più alta)
                row = matched_rows.iloc[0]
                results[keyword] = {"Keyword": keyword, "Position": row['Position'], "URL": row.get('URL', '-')}
            else:
                if keyword not in results:
                    results[keyword] = {"Keyword": keyword, "Position": "-", "URL": "-"}
        return list(results.values())
    
    # Esegui la ricerca delle parole chiave
    results = search_keywords(df, keywords)
    
    # Mostra i risultati in una tabella
    results_df = pd.DataFrame(results)
    st.write("Risultati della ricerca:")
    st.table(results_df)
else:
    st.write("Per favore, inserisci le parole chiave e carica un file Excel per procedere.")
