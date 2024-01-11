import requests
from bs4 import BeautifulSoup

def scrape_and_save_html(url, filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the raw HTML content
        html_content = response.text

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove all script tags
        for script_tag in soup.find_all('script'):
            script_tag.decompose()

        for meta_tag in soup.find_all('meta'):
                meta_tag.decompose()    

        for link_tag in soup.find_all('link'):
                link_tag.decompose()      

        for style_tag in soup.find_all('stlye'):
                style_tag.decompose()      

        for head_tag in soup.find_all('head'):
                head_tag.decompose()                    

        # Get the modified HTML content
        modified_html = str(soup)

        # Save the modified HTML content to a file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(modified_html)

        print(f"HTML content saved to {filename}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage:
url_to_scrape = "https://blog.logrocket.com/"
file_name = "data.html"
scrape_and_save_html(url_to_scrape, file_name)
