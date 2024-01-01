import os, datetime, shutil, subprocess, time, csv
#os.system("pip install easyocr")
import easyocr
import requests

def fetch_images(api_url, max_retries=3, retry_timeout=5):
    for retry in range(max_retries):
        try:
            response = requests.get(api_url, timeout=15)
            if response.status_code == 200:
                data = response.json()
                if (
                    "result" in data
                    and "result" in data["result"]
                    and "images" in data["result"]["result"]
                ):
                    return data["result"]["result"]["images"]
            print(f"Retrying ({retry+1}/{max_retries}) to fetch images...")
            time.sleep(retry_timeout)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {str(e)}")
            print(f"Retrying ({retry+1}/{max_retries}) to fetch images...")
            time.sleep(retry_timeout)
    return []

def download_images(images, folder_path):
    os.makedirs(folder_path, exist_ok=True)
    for i, image_link in enumerate(images):
        output_filename = os.path.join(folder_path, f"{i}.jpg")
        try:
            subprocess.run(["curl", image_link, "-o", output_filename])
            print(f"Image {i} downloaded as {output_filename}")
        except Exception as e:
            print(f"Failed to download image {i}: {str(e)}")

def perform_ocr(folder_path, confidence_threshold=0.82):
    reader = easyocr.Reader(['en'])
    text_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            result = reader.readtext(image_path)
            for detection in result:
                _, text, confidence = detection
                if confidence >= confidence_threshold:
                    text_list.append(text)
    return text_list

def main():
    if os.path.exists("links.txt"):
        with open("links.txt", "r", encoding="utf-8") as links_file:
            links = [line.strip() for line in links_file.readlines()]
    else:
        print("links.txt is not provided.")
        links = []

    csv_data = [["extracted_text"]]

    for idx, tiktok_url in enumerate(links, start=1):
        if tiktok_url.endswith("/"):
            tiktok_id = tiktok_url.split("/")[-2]
        else:
            tiktok_id = tiktok_url.split("/")[-1]

        api_url = f"https://tiktok-api-dbs8.onrender.com/{tiktok_id}"
        images = fetch_images(api_url, max_retries=3, retry_timeout=5)

        if images:
            folder_index = idx
            if not os.path.exists(".temp"):
                os.mkdir(".temp")
            while os.path.exists(f".temp/_Post_{folder_index}"):
                folder_index += 1
            folder_path = f".temp/_Post_{folder_index}"
            download_images(images, folder_path)
            extracted_text = perform_ocr(folder_path)
            if extracted_text:
                for text in extracted_text:
                    lines = text.split('\n')
                    for line in lines:
                        csv_data.append([line])
                print(extracted_text)

    if csv_data:
        with open(
            f"canva_import_{datetime.datetime.now().strftime('%d_%m_%H_%M_%S')}.csv",
            "w",newline="",
            encoding="utf-8",
        ) as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(csv_data)

if __name__ == "__main__":
    main()
    shutil.rmtree(".temp")
