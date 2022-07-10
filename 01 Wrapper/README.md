# Fidelity API Wrapper

This is where the Fidelity API Wrapper lives. The goal of this part of the
program is to automate the login procedure to Fidelity's asset management portal
and extract asset positions and other account information.

## Dependencies
You will need to install the following libraries with Pip, Python's package manager.

 * [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/getting_started/), to automate your browser.

 * [Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager), to download the proper drivers for your browser

 * [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), for extracting information from web pages

## Getting started

Run the Fidelity API file with `python fidelity_api.py`

Eventually, the output should look something like [wrapper_output.json](wrapper_output.json).