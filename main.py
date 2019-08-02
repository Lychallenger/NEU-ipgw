from selenium import webdriver
import time

def login(username, password):
    url='https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D1'
    driver = webdriver.PhantomJS()#or Chrome 火狐浏览器
    driver.get(url)
    # print driver.title
    name_input = driver.find_element_by_id('un')
    pass_input = driver.find_element_by_id('pd')
    login_button = driver.find_element_by_id('index_login_btn')

    name_input.clear()
    name_input.send_keys(username)  # 填写用户名
    time.sleep(0.2)
    pass_input.clear()
    pass_input.send_keys(password)  # 填写密码
    time.sleep(0.2)
    login_button.click()            # 点击登录

    time.sleep(0.2)
    print(driver.get_cookies())

    time.sleep(2)
    print(driver.title)
    driver.close()
    print('login success')

if __name__ == "__main__":
    user = "1801789"
    pw = "12345678"
    login(user, pw)
