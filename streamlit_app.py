import streamlit as st
import pandas as pd
from io import BytesIO

# Titolo dell'applicazione
st.title('Keyword Target Position Matching')

# Introduzione e descrizione dell'applicazione
st.markdown("""
## 👉🏼 Description
Questa applicazione è stata progettata per facilitare l'identificazione delle corrispondenze tra un insieme definito di parole chiave target e un elenco di posizionamenti attuali estratti tramite Semrush e Ahrefs. Funziona analizzando un file di esportazione fornito da questi strumenti, che riporta in dettaglio le posizioni attuali di diverse parole chiave sui motori di ricerca. Gli utenti possono inserire un elenco di parole chiave di interesse e caricare il file di ranking per scoprire rapidamente se e dove queste parole chiave appaiono nella classifica.
""")

st.markdown("---")

# Campo di testo per inserire le parole chiave target, una per riga
keyword_input = st.text_area("Inserisci parole chiave target (una per riga):")

# Converti l'input dell'utente in una lista di parole chiave
keywords = [keyword.strip().lower() for keyword in keyword_input.split('\n') if keyword]

# Widget di caricamento file
uploaded_file = st.file_uploader("Carica il file di ranking:", type=['xlsx', 'csv'])

# Seleziona la codifica del file
encoding_option = st.selectbox("Seleziona la codifica del file:", ['Auto', 'utf-8', 'utf-16le'], index=0)

# Seleziona il separatore di campo
sep_option = st.selectbox("Seleziona il separatore di campo:", ['Auto', ',', ';', '\t'], index=0)

def load_file(uploaded_file, encoding='Auto', sep='Auto'):
    if encoding == 'Auto':
        encoding = None
    if sep == 'Auto':
        sep = None
    
    try:
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, encoding=encoding, sep=sep)
        else:
            st.error("Formato file non supportato.")
            return None
    except Exception as e:
        st.error(f"Errore nel caricamento del file: {e}")
        return None
    return df

if uploaded_file and keywords:
    df = load_file(uploaded_file, encoding_option, sep_option)
    if df is not None:
        def search_keywords(df, keywords):
            results = {}
            for keyword in keywords:
                matched_rows = df[df['Keyword'].str.lower() == keyword].sort_values(by='Position')
                if not matched_rows.empty:
                    row = matched_rows.iloc[0]
                    results[keyword] = {"Keyword": keyword, "Position": row['Position'], "URL": row.get('URL', '-')}
                else:
                    results[keyword] = {"Keyword": keyword, "Position": "-", "URL": "-"}
            return list(results.values())

        # Esegui la ricerca delle parole chiave
        results = search_keywords(df, keywords)
        
        # Mostra i risultati in una tabella
        results_df = pd.DataFrame(results)
        st.write("Risultati della ricerca:")
        st.table(results_df)
        
        # Funzione per convertire il DataFrame in un file Excel
        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Risultati')
                writer.close()  # Chiudere correttamente il writer
            processed_data = output.getvalue()
            return processed_data
        
        # Genera il file Excel e mostra il pulsante di download
        excel_data = to_excel(results_df)
        st.download_button(label='Scarica risultati in formato Excel',
                           data=excel_data,
                           file_name='risultati_keywords.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

else:
    st.write("Per favore, inserisci le parole chiave e carica un file per procedere.")
