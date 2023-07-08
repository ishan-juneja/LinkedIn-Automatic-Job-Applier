import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

linkedin_email = "ishanj101@gmail.com"
linkedin_password = "Balderdash2004"

chrome_driver_path = "/Users/ishanjuneja/Development/chromedriver_mac64"
# linkedin_job_path = input("Enter the linkedIn link you wish to apply through using Easy Apply: ")
linkedin_job_path = "https://www.linkedin.com/jobs/search/?currentJobId=3645477451&f_AL=true&f_E=1%2C2&f_JT=P%2CI&geoId=103644278&keywords=python%20developer&location=United%20States&refresh=true&sortBy=R"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(linkedin_job_path)
driver.maximize_window()

# Signing into Linkedin
Sign_In_Button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
Sign_In_Button.click()

Email_Input = driver.find_element(By.ID, "username")
Email_Input.send_keys(linkedin_email)
time.sleep(random.randint(2, 4))
Password_Input = driver.find_element(By.ID, "password")
Password_Input.send_keys(linkedin_password)
time.sleep((random.randint(2, 4)))
Password_Input.send_keys(Keys.RETURN)

Job_List = []

time.sleep(15)
print("done")

all_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

# Clicking every next listing every 0.1 sec so it scrolls down the search list and registers every newfound element
for listing in all_listings:
	time.sleep(1)
	driver.execute_script("arguments[0].click();", listing)

	listing.click()
	time.sleep(1)

final_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
print("-----------------------------")

counter = 0
for listing in final_listings:
	# clicking on element and retrieving the easy apply button
	time.sleep(6)

	listing.click()
	counter += 1
	time.sleep(2)
	easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
	print(easy_apply_button.text)
	print("hiiiiiiii")
	if easy_apply_button.text == "Easy Apply":
		driver.execute_script("arguments[0].click();", easy_apply_button)

		# Retrieving the number bar
		time.sleep(1)
		bars = driver.find_elements(By.CSS_SELECTOR, "input.artdeco-text-input--input")
		for bar in bars:
			if bar.get_attribute('value') == "":
				# Enter your number here
				bar.send_keys("4089962669")
				break

		# Get past entering number
		time.sleep(1)
		Skip_Job = False
		try:
			next_button = driver.find_element(By.XPATH,
			                                  "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
		except NoSuchElementException:
			Skip_Job = True
			submit_button = driver.find_element(By.XPATH,
			                                    "/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button")
		# driver.execute_script("arguments[0].click();", submit_button)

		if Skip_Job == False:
			driver.execute_script("arguments[0].click();", next_button)

			# Get past Resume Question
			time.sleep(1)
			next_button = driver.find_element(By.XPATH,
			                                  "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")

			# Checking if any further questions will be required from the posting
			# If so the user has the option to enter the info manually by using a sleep method until then but for now the code will
			# Skip past such a posting
			if (next_button.text == "Review"):
				# sending the application through once on the resume page
				driver.execute_script("arguments[0].click();", next_button)

				finalize_button = driver.find_element(By.XPATH,
				                                      "/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]/span")

				# Send our application through

				# UNCOMMENT OUT THIS LINE TO SEND YOUR CODE
				# driver.execute_script("arguments[0].click();", finalize_button)
				print(f"Sending your application in for: \n{listing.text}\n\n")
			elif (next_button.text == "Submit application"):
				# Send our application through
				# driver.execute_script("arguments[0].click();", next_button)
				print(f"Sending your application in for: \n{listing.text}\n\n")

		# Exit out of application
		time.sleep(0.1)
		x_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
		driver.execute_script("arguments[0].click();", x_button)

		time.sleep(0.1)
		confirm_exit_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]")
		driver.execute_script("arguments[0].click();", confirm_exit_button)

while True:
	pass
