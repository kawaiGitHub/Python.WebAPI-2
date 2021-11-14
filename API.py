import requests

def main():
    api_url ="https://dog.ceo/api/breeds/image/random"

    r = requests.get(api_url)

    print(r.json())
    data = r.json()

    image_url =data["message"]
    print(image_url)

    download_image(url=image_url, file_path="images/dog.jpg")

if __name__=="__main__":
    main()