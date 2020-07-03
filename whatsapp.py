from selenium import webdriver
PATH = "C:\WebDriver\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")
name = input("Enter the name of the user or group :")
msg = input("Enter the message you want to send :")
count = int(input("Enter the number of times you want to send the message :"))
input("Enter anything after scanning the QR code")
user = driver.find_element_by_xpath('//*[@id="pane-side"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name("_3uMse")
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_1U1xa")
    button.click()