from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import csv

def extract_linkedin_data(first_name, last_name):
    # Alright, let's fire up Chromedriver. Buckle up!
    driver_path = "*******chromedriver.exe"

    # Setting up the ChromeDriver service, because we like to serve Chrome.
    service = Service(driver_path)

    # Initiating the Chrome browser. Time to surf the web!
    driver = webdriver.Chrome(service=service)

    # Heading straight to LinkedIn. Time to socialize!
    driver.get("https://www.linkedin.com")

    # Time to spill the beans! Logging in with our super secret credentials.
    username = "khushikhari03@gmail.com"
    password = "lalalalalal@123"

    driver.find_element_by_id("session_key").send_keys(username)
    driver.find_element_by_id("session_password").send_keys(password)
    driver.find_element_by_class_name("sign-in-form__submit-button").click()

    time.sleep(2)  # Just a quick breather while the page loads.

    # Let's go on a scavenger hunt! Searching for our prey based on first and last names.
    search_query = f"{first_name} {last_name} site:linkedin.com/in"
    driver.get(f"https://www.google.com/search?q={search_query}")

    time.sleep(2)  # Holding our breath while the search results pop up.

    # Time to play detective! Extracting intel from the search results.
    user_profiles = driver.find_elements_by_css_selector(".tF2Cxc")

    users = []
    for profile in user_profiles[:5]:  # Grabbing data from the first 5 search results
        name = profile.find_element_by_css_selector(".DKV0Md").text
        profile_url = profile.find_element_by_css_selector("a").get_attribute("href")
        users.append({"name": name, "profile_url": profile_url})

    # Mission accomplished! Closing the browser before anyone suspects a thing.
    driver.quit()

    return users

# Example usage
first_name = "dr. meredith"
last_name = "grey"
users = extract_linkedin_data(first_name, last_name)

# Time to stash our loot in a top-secret CSV file.
with open("linkedin_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "profile_url"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for user in users:
        writer.writerow(user)
