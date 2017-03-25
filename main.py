#coding=utf-8
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options)

driver.implicitly_wait(5)
#driver.set_page_load_timeout(3)
driver.get("http://www.juzimi.com")

#driver.find_element_by_id("ur").send_keys("15610537527")
#driver.find_element_by_id("pw").send_keys("15866584957")
#driver.find_element_by_class_name("loading_btn").click()
#向cookie 的name 和value 添加会话信息。
#driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
print "1、遍历所有cookie："
#遍历cookies 中的name 和value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print "%s:%s" % (cookie['name'], cookie['value'])
print "2、输出所有cookie："
# 获得全部cookie 信息
cookie= driver.get_cookies()
for item in cookie:
    print item
#将获得cookie 的信息打印
#print cookie
print "3、输出删除指定cookie的cookie："
# 删除一个特定的cookie
driver.delete_cookie("cookie_username")
for cookie in driver.get_cookies():
    print "%s:%s" % (cookie['name'], cookie['value'])
print "4、输出删除所有cookie的cookie："
# 删除所有cookie
driver.delete_all_cookies()
for cookie in driver.get_cookies():
    print "%s:%s" % (cookie['name'], cookie['value'])



time.sleep(2)
driver.quit()