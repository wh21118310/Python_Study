from selenium import webdriver
fp1 = webdriver.FirefoxProfile()
fp1.set_preference("javascript.enabled", False)
driver = webdriver.Firefox(firefox_profile=fp1)
driver.get('https://zh.airbnb.com/s/Shenzhen--China/all?refinement_paths%5B%5D=%2Ffor_you')
rent_list = driver.find_elements_by_css_selector('div._v72lrv')
    # 对于每一个出租房
for eachhouse in rent_list:
        # 找到评论数量
        try:
            comment = eachhouse.find_element_by_css_selector('span._1u3ih39j')
            comment = comment.text
        except:
            comment = 0
        # 找到价格
        price = eachhouse.find_element_by_css_selector('span._9nurmxj')
        price = price.text[4:]
        # 找到名称
        name = eachhouse.find_element_by_css_selector('div._vbshb6')
        name = name.text
        # 找到房屋类型，大小
        details = eachhouse.find_elements_by_css_selector('span._14ksqu3j')
        print(comment, price, name, details)