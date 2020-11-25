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
# chrome_options.add_argument('--disable-gpu')
# # 크롬 헤드리스 모드 사용 위해 headless setting
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(BASE_DIR / 'products/chromedriver', options=chrome_options)
driver.implicitly_wait(1)
driver.get('https://store.musinsa.com/app/goods/668822')

bigimages = driver.find_elements_by_css_selector('#bigimg.plus_cursor')
brandnames = driver.find_elements_by_css_selector('#product_order_info > div.explan_product.product_info_section > ul > li:nth-child(1) > p.product_article_contents > strong > a')


for bigimage in bigimages:
   bigimage_link = bigimage.get_attribute('src')
   print(bigimage_link)

for brandname in brandnames:
   brandname_text = brandname.text
   print(brandname_text)



# 이미지를 저장하는 크롤링
#if not os.path.exists('./detailimages'):
#    os.mkdir('./detailimages')

#for index, bigimage in enumerate(bigimages):
#    bigimage_src = bigimage.get_attribute('src')

# gif / base64 가 아닌 jpg 이미지만 다운로드
#    if 'https' in bigimage_src and '.jpg' in bigimage_src:
#        extension = bigimage_src.split('.')[-1]
#        print(f'{index}: {bigimage_src}')
#        urllib.request.urlretrieve(bigimage_src, f'./detailimages/detail-{index}.jpg')



# 코드 실행을 잠시 멈춘다.
time.sleep(2)

# 사용을 마치면 드라이버를 종료시킨다.
driver.quit()