import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL of the website you want to scrape
url = "https://emeenentdev.vercel.app"

# Step 2: Send a GET request to the website
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 5: Find specific elements (e.g., all <h2> tags for article titles)
    titles = soup.find_all("h2")
    lines = soup.find_all("p")

    # Step 6: Print the extracted titles
    for title in titles:
        print(title.get_text())
else:
    print("Failed to fetch the webpage:", response.status_code)
