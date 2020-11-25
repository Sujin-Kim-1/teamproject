from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Linux 서버에서는 GUI Browser를 구동할 수 없기 때문에 Headless Mode로 사용해야 한다.
chrome_options = webdriver.ChromeOptions()
# # 크롬 헤드리스 모드 사용 위해 disable-gpu setting
chrome_options.add_argument('--disable-gpu')
# # 크롬 헤드리스 모드 사용 위해 headless setting
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(BASE_DIR / 'products/chromedriver', options=chrome_options)
driver.implicitly_wait(1)
driver.get('https://store.musinsa.com/app/')

search_input = driver.find_element_by_id('search_query')
search_input.send_keys('아우터')
search_input.send_keys(Keys.RETURN)


# 스크롤다운
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(1)

listimages = driver.find_elements_by_css_selector('#searchList > li.li_box > div.li_inner > div.list_img > a > img')

for listimage in listimages:
   listimage_link = listimage.get_attribute('data-original')
   print(listimage_link)



# 이미지를 저장하는 크롤링
#if not os.path.exists('./images'):
#    os.mkdir('./images')

#for index, image in enumerate(images):
#    image_src = image.get_attribute('data-original')

#    # gif / base64 가 아닌 jpg 이미지만 다운로드
#    if 'https' in image_src and '.jpg' in image_src:
#        extension = image_src.split('.')[-1]
#        print(f'{index}: {image_src}')
#        urllib.request.urlretrieve(image_src, f'./images/outer-{index}.jpg')




# 코드 실행을 잠시 멈춘다.
time.sleep(2)

# 사용을 마치면 드라이버를 종료시킨다.
driver.quit()