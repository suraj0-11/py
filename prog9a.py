import os
import requests
os.makedirs("xkcd_comics", exist_ok=True)
comic_number = 1
while True:
    comic_url = f"https://xkcd.com/{comic_number}/"
    response = requests.get(comic_url)
    if response.status_code == 404:
        break
    img_url = f"https://xkcd.com/{comic_number}/info.0.json"
    img_response = requests.get(img_url)

    if img_response.status_code == 200:
        comic_data = img_response.json()
        img_url = comic_data["img"]
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            filename = f"xkcd_comics/{comic_data['title']}.png"
            with open(filename, "wb") as img_file:
                img_file.write(img_response.content)
            print(f"Downloaded: {comic_data['title']}")
    comic_number += 1
print("All XKCD comics downloaded successfully!")
