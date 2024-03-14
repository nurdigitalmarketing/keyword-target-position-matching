
# Keyword Target Position Matching

## 👉🏼 Description
This application is designed to facilitate the identification of matches between a defined set of target keywords and a list of current placements extracted through Semrush. It works by analyzing an export file provided by Semrush, which details the current positions of several keywords on search engines. Users can enter a list of keywords of interest and upload the ranking file to quickly find out if and where these keywords appear in the ranking list.

## 👉🏼 Features
- Interactive interface for uploading Excel files and entering target keywords.
- Accurate search functionality to find exact matches of keywords in the uploaded file.
- Display of search results including keyword, position, and URL in a user-friendly table format.

## 👉🏼 How to Use
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Install all dependencies from `requirements.txt` by running the command:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Streamlit application using the command:
   ```bash
   streamlit run app.py
   ```
5. Through the application interface, upload your Excel file and enter the keywords you want to search for, separated by commas.
6. The application will process the file and display a table with the keywords, their positions, and URLs if present.

## 👉🏼 Technologies Used
- `streamlit`: An open-source app framework for Machine Learning and Data Science projects.
- `pandas`: A fast, powerful, flexible and easy to use open-source data analysis and manipulation tool.
- `openpyxl`: A Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

## 👉🏼 Installation
To set up the project environment, run the following command to install necessary dependencies:
```bash
pip install -r requirements.txt
```

## 👉🏼 Credits
This application was inspired by the need to streamline the process of keyword analysis in large datasets. It's built to support professionals in fields such as digital marketing, SEO, and data analysis by providing a quick and efficient means to extract and analyze keyword data from Excel files.

For more information on Streamlit, visit [Streamlit Documentation](https://docs.streamlit.io/).
