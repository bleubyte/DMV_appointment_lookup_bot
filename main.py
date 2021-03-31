#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.dirname(__file__)
	return os.path.join(base_path, relative_path)

def fBrowser():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--window-size=800x600")
	#chrome_options.add_argument("user-data-dir=selenium")
	chrome_options.add_argument('--no-sandbox')
	#chrome_options.add_argument('--headless')
	chrome_options.add_argument('--ignore-certificate-errors')
	driver = webdriver.Chrome(options=chrome_options, executable_path=resource_path("c:\\chromedriver.exe"))
	driver.get('https://www.dmv.virginia.gov/onlineservices/appointments.aspx')
	action = ActionChains(driver)
	# Clicks https://www.geeksforgeeks.org/send_keys-method-action-chains-in-selenium-python/
	element = driver.find_element_by_xpath('//*[@id="apptForm"]/div[1]/label[4]')
	action.click(on_element = element)
	action.send_keys("Arrays")
	action.perform()

	elems = driver.find_elements_by_xpath('//*[@id="apptLocation"]/option')

	location_centers = {}

	for elem in elems:
		if elem.text == '': # Its picking up other hrefs for other services, a short filter
			pass
		else:
			value = elem.get_attribute("value")
			text = elem.text
			location_centers[text] = value

	del location_centers['Select a location']

	for key in location_centers:
		#open tab
		driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
		driver.get(value)
		time.sleep(10)
		#close tab
		driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
fBrowser()






