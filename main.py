import requests
import csv
from bs4 import BeautifulSoup
import extract 
import tool_box as tb

base_url = 'https://books.toscrape.com/'

def main():
    input_data = tb.get_input_user()
    content = tb.get_html_content(base_url)
    data_url_category, data_title_category = extract.extract_url_category(content, base_url)
    extract.iterate_category(data_url_category, data_title_category, input_data)

if __name__== "__main__":
    main()