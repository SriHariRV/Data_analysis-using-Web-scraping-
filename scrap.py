
from bs4 import BeautifulSoup
import openpyxl

def extract_product_info(product_div):
    product_name_elem = product_div.find('span', class_='a-size-medium a-color-base a-text-normal')
    product_name = product_name_elem.text.strip() if product_name_elem else " "

    product_price_elem = product_div.find('span', class_='a-price-whole')
    product_price = product_price_elem.text.strip() if product_price_elem else " "

    num_of_reviews_elem = product_div.find('span', class_='a-size-base s-underline-text')
    num_of_reviews = num_of_reviews_elem.text.strip() if num_of_reviews_elem else " "

    return product_name, product_price, num_of_reviews

with open('amazon.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')
product_divs = soup.find_all('div', class_='puisg-col-inner')

workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet.append(['Product Name', 'Product Price', 'Number of Reviews'])


for product_div in product_divs:
    product_name, product_price, num_of_reviews = extract_product_info(product_div)
    worksheet.append([product_name, product_price, num_of_reviews])

workbook.save('output.xlsx')
