import requests
from bs4 import BeautifulSoup
import math
import re

"""
Prompts the user to input the number of categories to retrieve.
Returns the user's input if it is a valid integer within the allowed range.
If the input is empty or exceeds the maximum allowed value, returns the default value of 50.
"""

def get_input_user():
    while True:
        input_data = input('Nombre de catégories a récupérer : ')
        if not input_data:
            return 50
        try:
            data = int(input_data)
            if data > 50:
                return 50
            return data
        except ValueError:
            print("Entrez un nombre entier ou appuyez sur 'Entrer'.")


"""
Fetches and returns the HTML content from the given URL.   
This function sends a GET request to the specified URL and returns the HTML content if the request is successful.
If an error occurs during the request, it returns None.
"""
def get_html_content(base_url):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.text
    except requests.RequestExceptions:
        return None


"""
Combines a base URL with a false URL to create a full URL.
It removes any leading `./` from the false URL and appends it to the base URL. 
The function returns the resulting full URL.
"""
def concatenate_url(false_url, base_url):
    cleaned_url = false_url.lstrip('./')
    true_url = base_url + cleaned_url

    return true_url


"""
Removes the last segment from the given URL by trimming everything after the last `/`. 
If no `/` is found, the function returns the original URL.
"""
def remove_end_of_url(false_url):
    index = false_url.rfind('/')
    if index == -1:
        return false_url
    return false_url[:index]

"""
Parses the HTML to find the pagination information and calculates the total number of pages.
Returns the total number of pages or 0 if the pagination info is not found or an error occurs.
"""
def get_number_pages(url_category):
    try:
        reponse = requests.get(url_category)
        reponse.raise_for_status()
        parser = BeautifulSoup(reponse.content, "html.parser")
        pager = parser.find('div', class_='col-sm-8 col-md-9').find('strong')
        
        if pager and pager.string:
            nb_page = int(pager.string)
            nb_page /= 20
            return math.ceil(nb_page)
        else:
            return 1
    except requests.RequestException:
        return 1


"""
Iterates through the input list and extends the result list with elements from any nested lists, or appends individual elements if they are not lists.
"""
def flatten_list(false_list):
    stock_list = []
    for index in false_list:
        if isinstance(index, list):
            stock_list.extend(index)
        else:
            stock_list.append(index)
    return stock_list


"""
Cleans and formats a filename by replacing invalid characters with underscores and truncating it to a maximum length of 190 characters.
Invalid characters include: < > : " / \\ | ? *
Multiple spaces are replaced with a single underscore.
"""
def clean_filename(filename):
    stock = re.sub(r'[<>:,"/\\|?*]', '_', filename)
    stock = re.sub(r'[\s]+', '_', stock)
    if len(stock) > 190:
        return stock[:190]
    return stock