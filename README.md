# LinkedIn-Automatic-Job-Applier

This application creates a bot that applies for [Easy-To-Apply]("https://business.linkedin.com/talent-solutions/product-update/recruiting-and-candidate-search-tool/lever/easy-apply") jobs on LinkedIn. However, the bot will only apply for jobs that require your phone number and resume!

## Structure
- `main.py` runs the entirety of the program and applies for the jobs
- `safe_setting_main.py` runs a similar version of the program yet doesn't apply for any of the jobs and rather cancels out of each application

## Dependencies & Configurations
1. The [Selenium API](https://www.selenium.dev/documentation/webdriver/) is used for logging into LinkedIn and web scraping the jobs and applying for each posting
   - Retrieve your LinkedIn email and password and replace them at the top of the file
   - Enter your phone number into `bar.send_keys(os.environ["PHONE_NUMBER"])`
2. This application is only compatible with google chrome and requires you to have a [chrome_driver_path](https://chromedriver.chromium.org/downloads)
3. Lastly, the program will ask you to enter a LinkedIn link to which kinds of jobs you want to apply for. This link must be configured within LinkedIn itself by applying your desirable filters.
   
## Demo

Configuring my link within LinkedIn. Here, I am choosing to apply for Easy to Apply Python Developer jobs
![Screenshot 2023-07-10 at 11 52 15 AM](https://github.com/ishan-juneja/LinkedIn-Automatic-Job-Applier/assets/69048541/fc3b1b98-437f-412f-b201-ade0280e6b32)

Entering my link into the console
<img width="1405" alt="Screenshot 2023-07-10 at 11 52 39 AM" src="https://github.com/ishan-juneja/LinkedIn-Automatic-Job-Applier/assets/69048541/ba634e4b-17f5-49a3-9b29-4e003550507e">

Demo video of `safe_setting_main.py`

https://github.com/ishan-juneja/LinkedIn-Automatic-Job-Applier/assets/69048541/a4d007f6-a3c7-4edf-b05d-f605382098a8



## Future Improvements
1. Being able to apply for Easy-To-Apply Jobs that also take in your address and have more than just your resume and number fields.
2. Being able to apply for more jobs beyond Easy Apply.
