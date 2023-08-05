from pprint import pprint
from time import sleep
from bs4 import BeautifulSoup

ACCT_ID='Z08484714'

def slow_send_keys(element, string):
    for character in string:
        element.send_keys([character])
        sleep(0.1)

def login(driver, username, password):
    driver.get('https://fidelity.com')

    login_field = driver.find_element('id', 'userId-input')
    password_field = driver.find_element('id', 'password')
    login_button = driver.find_element('id', 'fs-login-button')

    slow_send_keys(login_field, username)
    slow_send_keys(password_field, password)
    sleep(2)

    login_button.click()

    # Raise an error if we didn't make it to the management page

def get_account_list(driver):
    soup = BeautifulSoup(
        driver.page_source,
        'html.parser'
    )

    acct_nav = soup.find('nav', {'aria-label': 'Account selector'})
    acct_divs = acct_nav.find_all('div', {'class': 'acct-selector__acct-content'})

    def parse_acct_entry(acct):
        name_div = acct.find('div', {'class': 'acct-selector__acct-name'})
        id_div = acct.find('span', {'class': 'acct-selector__acct-num'})
        return {
            'name': name_div.text.strip(),
            'id': id_div.text.strip()
        }

    return [parse_acct_entry(div) for div in acct_divs]

def get_account_information(driver, acct_id=ACCT_ID):
    # Find each investment account, and summarize their assets
    soup = BeautifulSoup(
        driver.page_source,
        features='lxml',
    )

    acct_nav = soup.find('nav', {'aria-label': 'Account selector'})

    return []


# Python modules can either be imported or run directly. This block will run
# whenever you run the script directly, for example with the command:
#  $ python fidelity_wrapper.py
if __name__ == '__main__':
    # from selenium.webdriver.firefox.options import Options as FirefoxOptions
    # from selenium import webdriver
    # options = FirefoxOptions()
    # options.headless = True
    # driver = webdriver.Firefox(options=options)
    import undetected_chromedriver as uc
    driver = uc.Chrome(
        driver_executable_path="/home/mitch/.local/bin/chromedriver-alt"
    )
    # from selenium.webdriver.chrome.options import Options as ChromeOptions
    # from selenium import webdriver
    # options = ChromeOptions()
    # driver = webdriver.Chrome(options=options)

    from getpass import getpass
    username = input("Username: ")
    password = getpass()

    login(driver, username, password)
    info = get_account_information(driver)

    sleep(10)

    print(f"Found info: {info}")
