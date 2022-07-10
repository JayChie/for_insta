# Create by JaaayC 20220511 Ver. 8.0 bata
# Auto likes for instagram
# selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from IG_Document import *

import undetected_chromedriver as uc
import random
import time

print('開始自動操作...')
for IG_Account in IG_Accounts:
    try:
        options = uc.ChromeOptions()
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_setting_values.notifications": 2,
            },
        )
        # block pop-up and notifications:
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument('--no-first-run')
        options.add_argument('--no-service-autorun')
        options.add_argument('--no-default-browser-check')
        options.add_argument('--password-store=basic')
        driver = uc.Chrome(options=options, use_subprocess=True)

    #for IG_Account in IG_Accounts:
        driver.get("https://www.instagram.com")
        time.sleep(random.randint(4, 15))

        assert "Instagram" in driver.title
        time.sleep(random.randint(2, 5))
        driver.find_element_by_xpath('//*[@name="username"]').send_keys(IG_Account['IDa'])
        time.sleep(random.randint(1, 3))
        driver.find_element_by_xpath('//*[@name="password"]').send_keys(IG_Account['PAs'])
        time.sleep(random.randint(2, 5))
        # 登入
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        time.sleep(random.randint(6, 8))

        print('-Success-' * 10)
        print('已順利登入:',(IG_Account['IDa']))
        # 滾動頁面
        for i in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # chance to likes
        chance_to_likes = int(IG_Account['chance_to_like'])
        # 開始操作 到不同的tag去按讚
        for tags in IG_Account['Tas']:
            driver.get("https://www.instagram.com/explore/tags/" + tags)  # 切換到該tag
            print('執行:', tags)
            # 等待圖片出現後點選圖片
            try:
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_aanc")))
            except:
                time.sleep(random.randint(3, 8))

            driver.find_elements_by_class_name('_aa8k')[9].click()  # 點選圖片(選擇最新發的)

            for i in range(random.randint(10, 15)):

                time.sleep(random.randint(8, 16))

                # 檢查有沒有按過讚
                if len(driver.find_elements_by_xpath('//*[@aria-label="Unlike"]')) != 0 :
                    print('互動過跳出')
                    break
                else:
                    # Random chance of commenting
                    do_i_like = randint(1, chance_to_likes)
                    if do_i_like == 1:
                        time.sleep(random.randint(10, 16))
                        try:
                            # like
                            driver.find_element_by_class_name('_aamw').click()
                            print('click')
                        except:
                            print('圖片沒跑出來，直接下一頁')
                    else:
                        print('沒按到')
                # NEXT PAGE
                try:
                    time.sleep(random.randint(8, 12))
                    driver.find_element_by_xpath('//*[@aria-label="下一步"]').click()
                    print('下一篇')
                except:
                    print('下一頁')

            print(tags + ' 全部按完')
            time.sleep(random.randint(7, 15))  # 隨機數字 模仿真人休息

        print('已完成，自動關閉網頁')
        time.sleep(3)
        driver.quit()
        print('關閉瀏覽器')
        time.sleep(random.randint(8, 12))
    except:
        driver.save_screenshot("錯誤截圖報告.png")
        print('有誤，已截圖')
        time.sleep(3)
        driver.quit()

time.sleep(3)
print('已全部完成，自動關閉網頁')