def login(driver, username, password):
    # Navigate to the Fidelity Homepage

    # Find the Username box, send the Username

    # Find the password box, send the Password

    # Find the login button, and click it

    # Raise an error if we didn't make it to the management page

    pass


def get_account_information(driver):
    # Find each investment account, and summarize their assets

    return []


# Python modules can either be imported or run directly. This block will run
# whenever you run the script directly, for example with the command:
#  $ python fidelity_wrapper.py
if __name__ == '__main__':
    # See https://github.com/SergeyPirogov/webdriver_manager to get the proper
    # driver for automating your browser
    driver = None

    from getpass import getpass
    username = input("Username: ")
    password = getpass()

    login(driver, username, password)
    info = get_account_information(driver, username, password)

    print(f"Found info: {info}")