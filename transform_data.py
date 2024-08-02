import csv
import os
import requests
import tool_box as tb

en_tete = ['title', 'product_page_url', 'universal_ product_code', 'price_excluding_tax', 'price_including_tax', 'number_available', 'review_rating', 'product_description', 'category', 'image_url']


"""
Saves the provided data to a CSV file named after the given category.
Creates necessary directories if they do not exist and writes the data to a CSV file.
The first row of the CSV file contains headers, followed by the data rows of the category.
"""
def transform_to_csv(category, data_book):
    directory = 'Fichier_csv'
    path = os.path.join('Data', directory)
    if not os.path.exists(path):
        os.makedirs(path)
    path_file = os.path.join(path, category)
    with open(f'{path_file}.csv', 'w', newline='', encoding='utf-8') as my_file:
        writer = csv.writer(my_file, delimiter=',')
        writer.writerow(en_tete)
        for index in data_book:
            writer.writerow(index)


"""
Downloads an image from the given URL and saves it to a specified directory.
The function creates necessary directories if they do not exist, cleans the filename, and saves the image with a `.jpg` extension.
If the download fails, an error message is printed.
"""
def download_image(url, title_category, title_book):
    directory = 'Image'
    count = 0
    stock = tb.clean_filename(title_book)
    if not os.path.exists('Data'):
        os.makedirs('Data')
    path = os.path.join('Data', directory, title_category)
    if not os.path.exists(path):
        os.makedirs(path)
    path_file = os.path.join(path, stock)
    path_file += '.jpg'
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(path_file, 'wb') as my_file:
            my_file.write(response.content)
        count += 1
    except requests.exceptions.RequestException as e:
        print(f"Échec du téléchargement de l'image depuis {url}. Erreur : {e}")