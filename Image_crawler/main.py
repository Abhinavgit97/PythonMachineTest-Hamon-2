# main.py
from image_downloader import scrape_images

if __name__ == '__main__':
    url = "https://www.gettyimages.in/photos/aamir-khan-actor"
    save_path = "images"
    limit = 60
    scrape_images(url, save_path, limit)

    