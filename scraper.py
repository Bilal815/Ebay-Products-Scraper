from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
# URl to web scrap from.
# in this we web scrape ebay's product page
page_url = "https://www.ebay.co.uk/b/Definite-Purpose-Industrial-Electric-Motors/181731/bn_16568098"
# opens the connection and downloads html page from url
uClient = uReq(page_url)
# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

page_header =  page_soup.h1.span
# finds each product from the store page
containers = page_soup.find_all("div", {"class": "s-item__wrapper"})
# name the output file to write to local disk
out_filename = "Products.csv"
# header of csv file to be written
headers = "Title, product_price, shipping \n"
# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)
# loops over each product and grabs attributes about
# each product
for container in containers:

    make_rating_sp = container.find_all("h3", {"class": "s-item__title"})[0].text
    # Grabs the title from the image title attribute
    # Then does proper casing using .title()
    Title = make_rating_sp
    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    product_price = container.find_all("span", {"class": "s-item__price"})[0].text
    # Grabs the product shipping information by searching
    # all lists with the class "price-ship".
    # Then cleans the text of white space with strip()
    # Cleans the strip of "Shipping $" if it exists to just get number
    shipping = container.find_all("span", {"class": "s-item__shipping"})[0].text
    # prints the dataset to console
    print("Title: " + Title + "\n")
    print("product_price: " + product_price + "\n")
    print("shipping: " + shipping + "\n")
    # writes the dataset to file
    f.write(Title.replace(",", "|") + ", " + product_price.replace(",", "|") + ", " + shipping.replace(",", "|") + "\n")
f.close()  # Close the file