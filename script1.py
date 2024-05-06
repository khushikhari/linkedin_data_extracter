import csv
import requests

# Here's the secret sauce! Your LinkedIn API access token. Use it wisely.
ACCESS_TOKEN = "nanannaanannan;)"

def retrieve_current_member_profile():
    # The URL where the magic happens! Accessing the LinkedIn Current Member's Profile API.
    url = "https://api.linkedin.com/v2/me"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Summoning the LinkedIn wizards! Making a GET request to the LinkedIn API.
    response = requests.get(url, headers=headers)

    # Checking if our owl returned successfully.
    if response.status_code == 200:
        data = response.json()
        profile_data = {
            "name": f"{data.get('firstName', {}).get('localized', {}).get('en_US', '')} {data.get('lastName', {}).get('localized', {}).get('en_US', '')}",
            "headline": data.get('headline', {}).get('localized', {}).get('en_US', ''),
            "vanityName": data.get('vanityName', ''),
            "profilePicture": data.get('profilePicture', {}).get('displayImage', ''),
            "id": data.get('id', '')
        }

        # Capturing the enchanting data in a mystical CSV file.
        with open("linkedin_current_member_profile.csv", "w", newline="") as csvfile:
            fieldnames = ["name", "headline", "vanityName", "profilePicture", "id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(profile_data)
        
        print("Voilà! The data has been successfully saved to linkedin_current_member_profile.csv.")
    else:
        print(f"Uh oh! Looks like our owl encountered a hiccup. Error code: {response.status_code}")

# Time to cast the spell and retrieve the current member's profile!
retrieve_current_member_profile()
