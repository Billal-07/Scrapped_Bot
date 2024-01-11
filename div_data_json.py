import requests
from bs4 import BeautifulSoup
import json

def extract_and_save_class_data(url, class_name, output_filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the specified class
        class_elements = soup.find_all(class_=class_name)

        # Initialize a list to store extracted data
        data_list = []

        # Extract information from each element
        for element in class_elements:
            article_url = element.find('a', class_='post-card-img')['href']
            title = element.find('h4').text.strip()

            # Check if the author elements exist before trying to access their properties
            author_url_elem = element.find('a', class_='post-card-author-img')
            author_name_elem = element.find('a', class_='post-card-author-name')
            date_time_elem = author_name_elem.find_next('div') if author_name_elem else None

            # Extract data only if the necessary elements are found
            if author_url_elem and author_name_elem and date_time_elem:
                author_url = author_url_elem['href']
                author_name = author_name_elem.text.strip()
                date_time = date_time_elem.text.split('⋅')[0].strip() if date_time_elem else ""

                # Create a dictionary for each entry
                entry = {
                    "article_url": article_url,
                    "title": title,
                    "author_website": author_url,
                    "author_name": author_name,
                    "date_time": date_time
                }

                # Append the entry to the data list
                data_list.append(entry)

        # Save the data as JSON to the specified file
        with open(output_filename, "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, ensure_ascii=False, indent=2)

        print(f"Data from class '{class_name}' saved to {output_filename}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Read URLs from the "wajid.txt" file
with open("wajid.txt", "r") as file:
    urls = file.read().splitlines()

# Perform extraction for each URL
for url in urls:
    class_to_extract = "post-card"
    output_file_name = f"saved_data_{url.split('/')[-2]}.json"  # Create a unique output file for each URL
    extract_and_save_class_data(url, class_to_extract, output_file_name)
