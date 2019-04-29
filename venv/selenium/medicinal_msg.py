from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os,time,sys
from selenium.webdriver.common.keys import Keys


"""加载驱动"""
chrome_options = Options()
chrome_options.add_argument("--headless")  # 不显示浏览器
chrome_options.add_argument('--disable-gpu')  # 跳过GPU数据收集
chrome_options.add_argument('--disable-software-rasterizer')  # 禁用WebGL支持
chrome_options.add_argument('log-level=3')  # 屏蔽日志
# info(default) = 0
# warning = 1
# LOG_ERROR = 2
# LOG_FATAL = 3
# chrome_options.add_argument('--allow - running - insecure - content') #消除安全校验 可以直接无提示访问http网站
# chrome_options.add_argument('--silent') #
driver = webdriver.Chrome(chrome_options=chrome_options)  # 使用 chrome_options 选项

try:
    url = "http://jy.hbjycg.com/ProcureCatalogList1.aspx"
    driver.get(url)
    str_xpath = ' // *[ @ id = "gvwProduceCatalog"] / tbody'
    WebDriverWait(driver, 15, 0.1).until(
        EC.presence_of_element_located((By.XPATH, str_xpath)))  # 0.5秒查一次最大45秒直到出来
    tbodyXml = driver.find_element_by_xpath(str_xpath)  # 取 页面的 记录表体
    #print(type(tbodyXml))
    #print(str(tbodyXml))
    #print(tbodyXml.text)
    list1 = tbodyXml.find_elements_by_tag_name("tr")[0]
    col1 = list1.find_elements_by_tag_name("th")[0:]
    line1 = ''
    for col in col1:
        line1 = line1 + '"' + col.text + '",'
    line1 = line1[:-1]
    line1 = line1 + '\n'
    with open('page_msg.csv', 'a+', encoding='utf-8') as f1:  # 一次性安全写数据到文件
        f1.writelines(line1)

    num = 1
    while(num <3857):
        xpathStr = '//*[@id="AspNetPager1_input"]'
        page_input = driver.find_element_by_xpath(xpathStr)
        print(num)
        page_input.clear()
        page_input.send_keys(num)
        page_input.send_keys(Keys.ENTER)
        page_msg = ''
        WebDriverWait(driver, 15, 0.1).until(
            EC.presence_of_element_located((By.XPATH, str_xpath)))
        tbodyXml = driver.find_element_by_xpath(str_xpath)
        trList = tbodyXml.find_elements_by_tag_name("tr")[1:]  # 取 记录列表
        for tr in trList:
            collist = tr.find_elements_by_tag_name("td")[0:]
            lines_msg = ''
            for col in collist:
                lines_msg = lines_msg + '"' +col.text+ '",'
            lines_msg = lines_msg[:-1]
            #print(lines_msg)
            page_msg = page_msg + lines_msg +'\n'
        with open('page_msg.csv', 'a+', encoding='utf-8') as f1:  # 一次性安全写数据到文件
            f1.writelines(page_msg)

        num = num + int(1)

        time.sleep(1)

finally:
    driver.close()


# try:
#     driver.get("https://www.baidu.com")
#     input=driver.find_element_by_id("kw")
#     input.send_keys("Python")
#     input.send_keys(Keys.ENTER)
#     wait=WebDriverWait(driver,10)
#     wait.until(EC.presence_of_element_located((By.ID,"content_left")))
#     print(driver.current_url)
#     print(driver.get_cookies())
#     print(driver.page_source)
#     time.sleep(10)
# finally:
#     driver.close()
