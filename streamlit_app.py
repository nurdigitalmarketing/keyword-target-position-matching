import streamlit as st
import pandas as pd

# Titolo dell'applicazione
st.title('Keyword Target Position Matching')

# Introduzione e descrizione dell'applicazione
st.markdown("""
## 👉🏼 Description
This application is designed to facilitate the identification of matches between a defined set of target keywords and a list of current placements extracted through Semrush and Ahrefs. It works by analyzing an export file provided by these tools, which details the current positions of several keywords on search engines. Users can enter a list of keywords of interest and upload the ranking file to quickly find out if and where these keywords appear in the ranking list.
""")

st.markdown("---")

# Campo di testo per inserire le parole chiave target, una per riga
keyword_input = st.text_area("Inserisci parole chiave target (una per riga):")

# Converti l'input dell'utente in una lista di parole chiave
keywords = [keyword.strip() for keyword in keyword_input.split('\n') if keyword]

# Widget di caricamento file
uploaded_file = st.file_uploader("Carica il file di ranking:", type=['xlsx', 'csv'])

if uploaded_file is not None and keywords:
    # Determina il tipo di file e leggi il contenuto in un DataFrame
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        st.write("Formato file non supportato.")
        st.stop()

    # Adatta la funzione di ricerca per gestire i file di Semrush e Ahrefs
    def search_keywords(df, keywords):
        results = {}
        for keyword in keywords:
            # La colonna 'Keyword' potrebbe necessitare di normalizzazione nel nome per alcuni file
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
    st.write("Per favore, inserisci le parole chiave e carica un file per procedere.")
