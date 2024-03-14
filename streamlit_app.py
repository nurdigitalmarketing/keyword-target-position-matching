import streamlit as st
import pandas as pd

# Titolo dell'applicazione
st.title('Keyword Search Streamlit Application')

# Introduzione e descrizione dell'applicazione
st.markdown("""
## 👉🏼 Description
This Streamlit application is designed to facilitate the search for specific keywords within an Excel file, providing a simple yet powerful tool for analyzing and extracting data based on user-defined keywords. It allows users to upload an Excel file and enter a set of target keywords, then searches for these keywords within the file to display their occurrences, positions, and associated URLs if available. This tool is particularly useful for content managers, SEO specialists, and data analysts looking to quickly assess the presence and distribution of keywords across large datasets.
""")

# Campo di testo per inserire le parole chiave target, separate da virgole
keyword_input = st.text_area("Inserisci parole chiave target (separate da virgole):")

# Converti l'input dell'utente in una lista di parole chiave
keywords = [keyword.strip() for keyword in keyword_input.split(',') if keyword]

# Widget di caricamento file
uploaded_file = st.file_uploader("Carica il file Excel:", type=['xlsx'])

if uploaded_file is not None and keywords:
    # Leggi il contenuto del file Excel in un DataFrame
    df = pd.read_excel(uploaded_file)

    # Funzione per cercare le corrispondenze esatte delle parole chiave e ottenere posizioni e URL
    def search_keywords(df, keywords):
        results = []
        for keyword in keywords:
            matched_rows = df[df['Keyword'].str.lower() == keyword.lower()]
            if not matched_rows.empty:
                for _, row in matched_rows.iterrows():
                    results.append({"Keyword": keyword, "Position": row['Position'], "URL": row.get('URL', '-')})
            else:
                results.append({"Keyword": keyword, "Position": "-", "URL": "-"})
        return results
    
    # Esegui la ricerca delle parole chiave
    results = search_keywords(df, keywords)
    
    # Mostra i risultati in una tabella
    results_df = pd.DataFrame(results)
    st.write("Risultati della ricerca:")
    st.table(results_df)
else:
    st.write("Per favore, inserisci le parole chiave e carica un file Excel per procedere.")
