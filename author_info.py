import requests
from bs4 import BeautifulSoup

def remove_unwanted_elements(soup):
    # Remove div elements with specified classes
    for class_name in ["content-max-width", "grofile-hash-map-9ab4e30e3aab3b8228474dc25ec42dad",
                       "jp-carousel-loading-overlay", "jp-carousel-container"]:
        for div_tag in soup.find_all('div', class_=class_name):
            div_tag.extract()

    # Remove style tags
    for style_tag in soup.find_all('style'):
        style_tag.extract()

    # Remove script tags
    for script_tag in soup.find_all('script'):
        script_tag.extract()
        
    for head_tag in soup.find_all('head'):
        head_tag.extract()    

def extract_and_save_html(url, output_filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove unwanted elements
        remove_unwanted_elements(soup)

        # Extract the modified HTML content
        html_content = str(soup)

        # Save the HTML content to the specified file
        with open(output_filename, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)

        print(f"HTML content from {url} saved to {output_filename} (unwanted elements removed)")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage:
url_to_scrape = "https://blog.logrocket.com/author/emmanuelodioko/"
output_file_name = "author.html"
extract_and_save_html(url_to_scrape, output_file_name)
