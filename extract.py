import requests
import csv
from bs4 import BeautifulSoup
import re
import transform_data as tr_data
import tool_box as tb

"""
Extracts and returns the product title from the HTML given as a parameter, or None if not found.
"""
def extract_title(html):
    if html:
        parser = BeautifulSoup(html, "html.parser")
        title = parser.find('div', class_='col-sm-6 product_main').find('h1')
        if title:
            return(title.text)
        else:
            return None


"""
Extracts products informations from the HTML given as a parameter.
Returns a list containing extracted product details.
"""
def extract_product_information(html):
    list_info = []
    if html:
        parser = BeautifulSoup(html, "html.parser")
        info_product = parser.find_all("td")
        compteur = 0

        for index in info_product:
            match compteur:
                case 0:     # extract UPC
                    list_info.append(index.text)
                    compteur += 1
                case 1:     # pass product type
                    compteur += 1
                    continue       
                case 2:     # extract price(excluding tax)
                    matches = re.search(r'£([\d.]+)', index.text)
                    list_info.append(matches.group(1))
                    compteur += 1
                case 3:     # extract price(including tax)
                    matches = re.search(r'£([\d.]+)', index.text)
                    list_info.append(matches.group(1))
                    compteur += 1
                case 4:     # pass tax
                    compteur += 1
                    continue
                case 5:     # extract availability
                    matches = re.search(r'In stock \((\d+) available\)', index.text)
                    list_info.append(matches.group(1))
                    compteur += 1
                case 6:     # extract number of reviews
                    list_info.append(index.text)
                    compteur += 1
        return(list_info)


"""
Extracts and returns the product description from the HTML given as a parameter, or None if not found.
"""
def extract_product_description(html):
    if html:
        parser = BeautifulSoup(html, "html.parser")
        desc = parser.find("p", class_=None)
        if desc:
            return(desc.text)
        else:
            return None


"""
Extracts and returns the image URL from the HTML given as a parameter, or None if not found.
"""
def extract_image_url(html):
    if html:
        parser = BeautifulSoup(html, "html.parser")
        img_url = parser.find("div", class_='item active').find('img').get('src')
        if img_url:
            return(tb.concatenate_url(img_url, 'https://books.toscrape.com/'))
        else:
            return None


"""
Extracts the URLs and titles of categories from the given HTML content.
Returns two lists:
- list_url_category: Full URLs of each category.
- list_title_category: Titles of each category.
"""
def extract_url_category(html, base_url):
    list_url_category = []
    list_title_category = []
    if html:
        parser = BeautifulSoup(html, "html.parser")
        category_url = parser.find("ul", class_="nav nav-list").find('ul').find_all('a')
        for index in category_url:
            container_url = index.get('href')
            container_title = index.text
            list_test = ' '.join(container_title.split())
            list_title_category.append(list_test)
            list_url_category.append(base_url + container_url)
        return (list_url_category, list_title_category)


"""
Extracts and returns a list of book URLs from a category page, including all pages.
Starts with the first page and iterates through each page.
- For each page:
- Sends a GET request to the page URL and checks for errors.
- Parses the HTML content to find book URLs.
- Appends the full book URLs to the list.
- Updates the URL to the next page.
- Stops if a request error occurs.
"""
def extract_url_books(url_category):
    list_url_book = []
    current_page = 1
    nb_page = tb.get_number_pages(url_category)
    if nb_page == 0:
        nb_page = 1
    while current_page <= nb_page:
        try:
            reponse = requests.get(url_category)
            reponse.raise_for_status()
            parser = BeautifulSoup(reponse.content, "html.parser")
            book_urls = parser.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
            for book in book_urls:
                container_url = book.find('div', class_='image_container').find('a').get('href')
                stock_url = tb.concatenate_url(container_url, 'https://books.toscrape.com/catalogue/')
                list_url_book.append(stock_url)
            current_page += 1
            url_category = tb.remove_end_of_url(url_category) + f'/page-{current_page}.html'
        
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            break
    return (list_url_book)


"""
Scrapes data from a list of book URLs, extracting details and downloading images.
For each book in the list:
- Retrieves the HTML content.
- Extracts the title, product information, product description, and image URL.
- Appends these details along with the book URL and category title to a row.
- Flattens the row and adds it to the data list.
- Downloads the image associated with the book.
Returns the complete list of data rows.
"""
def scrape_books_data(list_book, title_category):
    data_list = []
    for book in list_book:
        content = tb.get_html_content(book)
        row = []
        title = extract_title(content)
        url_book = book
        product_info = extract_product_information(content)
        product_desc = extract_product_description(content)
        image_url = extract_image_url(content)
        row.append(title)
        row.append(url_book)
        row.append(product_info)
        row.append(product_desc)
        row.append(title_category)
        row.append(image_url)
        row = tb.flatten_list(row)
        data_list.append(row)
        tr_data.download_image(image_url, title_category, title)
    return(data_list)


"""
Iterates through a list of categories and scrapes data for each.
For each category in the list:
- Extracts the list of book URLs in the category.
- Scrapes the data for each book and stores it in a list.
- Transforms the scraped data into a CSV file named after the category title.
Increments the count to move to the next category.
"""
def iterate_category(list_category, list_title_category, input_data):
    count = 0
    if input_data is not None:
        input_index = int(input_data)
    else:
        input_index = None
    for category in list_category:
        print('category en cour de scrap == ', list_title_category[count])
        list_url_book = extract_url_books(category)
        data_list = scrape_books_data(list_url_book, list_title_category[count])
        tr_data.transform_to_csv(list_title_category[count], data_list)
        if input_index is not None and count == input_index:
            break
        count += 1
