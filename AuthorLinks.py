import requests
from bs4 import BeautifulSoup
import json

def scrape_and_save_data(url, output_filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the div with id "Author Hero"
        author_hero_div = soup.find('div', id='author-hero')

        if author_hero_div:
            # Find the span tag with id "author-links" within the "Author Hero" div
            author_links_span = author_hero_div.find('span', id='author-links')

            if author_links_span:
                # Find all <a> tags within the "author-links" span
                author_links_a_tags = author_links_span.find_all('a')

                # Extract the href and text content of each <a> tag
                author_links_data = [{"href": a['href'], "text": a.text.strip()} for a in author_links_a_tags]

                # Create a dictionary for the extracted data
                data = {"author_links": author_links_data}

                # Save the data as JSON to the specified file
                with open(output_filename, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=2)

                print(f"Data from <a> tags in span with id 'author-links' saved to {output_filename}")
            else:
                print("Span tag with id 'author-links' not found.")
        else:
            print("Div with id 'Author Hero' not found.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage:
url_to_scrape = "https://blog.logrocket.com/author/pratikjoglekar/"  # Replace with the actual URL
output_file_name = "author_links_data.json"
scrape_and_save_data(url_to_scrape, output_file_name)


# import requests
# from bs4 import BeautifulSoup
# import json

# def scrape_and_save_data(json_file_path, output_filename):
#     # Read the JSON file to get the list of URLs
#     with open(json_file_path, "r", encoding="utf-8") as json_file:
#         data = json.load(json_file)
#         urls_to_scrape = data.get("urls", [])

#     if not urls_to_scrape:
#         print("No URLs found in the JSON file.")
#         return

#     # Initialize a list to store the extracted author website URLs
#     author_website_urls = []

#     for url_to_scrape in urls_to_scrape:
#         # Send a GET request to the URL
#         response = requests.get(url_to_scrape)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Parse the HTML content of the page
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Find the div with id "Author Hero"
#             author_hero_div = soup.find('div', id='Author Hero')

#             if author_hero_div:
#                 # Find the span tag with id "author-website" within the "Author Hero" div
#                 author_website_span = author_hero_div.find('span', id='author-website')

#                 if author_website_span:
#                     # Extract the text content of the span tag (assuming it contains the author website URL)
#                     author_website_url = author_website_span.text.strip()

#                     # Append the URL to the list
#                     author_website_urls.append(author_website_url)
#                 else:
#                     print(f"Span tag with id 'author-website' not found in URL: {url_to_scrape}")
#             else:
#                 print(f"Div with id 'Author Hero' not found in URL: {url_to_scrape}")
#         else:
#             print(f"Failed to retrieve the webpage. Status code: {response.status_code} for URL: {url_to_scrape}")

#     # Create a dictionary for the extracted data
#     data = {"author_website_urls": author_website_urls}

#     # Save the data as JSON to the specified file
#     with open(output_filename, "w", encoding="utf-8") as json_file:
#         json.dump(data, json_file, ensure_ascii=False, indent=2)

#     print(f"Author website URLs saved to {output_filename}")

# # Example usage:
# json_file_path = "saved_data_all_urls.json"  # Replace with the actual JSON file path
# output_file_name = "author_website_urls.json"
# scrape_and_save_data(json_file_path, output_file_name)
