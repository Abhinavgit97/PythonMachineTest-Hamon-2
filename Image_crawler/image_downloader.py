from selenium import webdriver
import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_image(img_url, save_path):
    response = requests.get(img_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as img_file:
            for chunk in response.iter_content(1024):
                img_file.write(chunk)
        return True
    return False


def scrape_images(url, save_path, limit):
    # Set up the web driver - chrome driver
    driver = webdriver.Chrome()

    # Open url
    driver.get(url)

    # Wait for the images to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))

    # Get image elements
    img_elements = driver.find_elements(By.TAG_NAME, "img")
    
    # Create the a folder to save images if not exist
    os.makedirs(save_path, exist_ok=True)
    count = 0
    for i, img_element in enumerate(img_elements):
        if count>limit:
            break
        try:
            # Get the URL of the image
            img_url = img_element.get_attribute("src")
            if img_url:
                print(f"Downloading image {i + 1}: {img_url}")
                
                # Extract the filename from the URL
                img_name = os.path.basename(img_url).split('?')[0]
                img_name, img_extension = os.path.splitext(img_name)
                
                # Ensure unique filename
                original_img_name = img_name
                counter = 1
                while os.path.exists(os.path.join(save_path, f"{img_name}{img_extension}")):
                    img_name = f"{original_img_name}_{counter}"
                    counter += 1
                
                unique_img_name = f"{img_name}{img_extension}"
                img_path = os.path.join(save_path, unique_img_name)

                # Downloading image
                if download_image(img_url, img_path):
                    count += 1
                else:
                    print(f"Failed to download image {count + 1}")
        except Exception as e:
            print(f"Failed to download image {i+1}: {e}")
    print(f"Downloaded {count} images successfully in the {save_path} folder")
    driver.quit()

# if __name__ == '__main__':
#     url = "https://www.gettyimages.in/photos/aamir-khan-actor"
#     save_path = "images"
#     limit = 60
#     scrape_images(url, save_path, limit)
