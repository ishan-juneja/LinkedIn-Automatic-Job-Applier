# LinkedIn-Automatic-Job-Applier

This application creates a bot that applies for [Easy-To-Apply]("https://business.linkedin.com/talent-solutions/product-update/recruiting-and-candidate-search-tool/lever/easy-apply") jobs on LinkedIn. However, the bot will only apply for jobs that require your phone number and resume!


## Structure
- `main.py` runs the entirety of the program and applies for the jobs
- `safe_setting_main.py` runs a similar version of the program yet doesn't apply for any of the jobs, and rather cancels out of each application

## Dependencies & Configurations
1. The [Selenium API](https://www.selenium.dev/documentation/webdriver/) used for logging into LinkedIn and web scraping the jobs and applying for each posting
2. The [Tequila Kiwi API](https://tequila.kiwi.com/) to find all our flight info.
   - Retrieve your **API_KEY** & **AFFIL_ID** once you create your account
   - Add to `flight_search.py`
3. The [Twilio API](https://www.twilio.com/docs) to message ourselves our details of the flight.
   - Retrieve your **ACCOUNT_SID** & **AUTH_TOKEN** once you create your account
   - Add to `notification_class.py`
   - Change the phone numbers to your Twilio Assigned Number and your personal phone number within the `notification_class.py` in the `notify` method

## Demo
The spreadsheet with our desired prices and locations. The program automatically fills in the IATA codes for you!
![Screenshot 2023-07-04 at 11 43 21 PM](https://github.com/ishan-juneja/Personal-Flight-Club/assets/69048541/d35e7a4f-90d0-49ed-ad28-e9ce995d6d55)

The programs sifts through the API data to retrieve us the relevant prices we want and compares them to what we had previously specified. 
<img width="1402" alt="Screenshot 2023-07-04 at 11 46 53 PM" src="https://github.com/ishan-juneja/Personal-Flight-Club/assets/69048541/e03230d4-cdee-402b-abb9-28c61a9d4c49">

If the program has found a match, then we recieve an email and text message!
![Screenshot 2023-07-04 at 11 48 05 PM](https://github.com/ishan-juneja/Personal-Flight-Club/assets/69048541/5777d90d-5e9d-43e3-a40c-a9e9469867b3)

![IMG_8822](https://github.com/ishan-juneja/Personal-Flight-Club/assets/69048541/aa90803f-aeff-4c8b-b856-c82f5562eeea)
