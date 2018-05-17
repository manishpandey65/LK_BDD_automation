from selenium import webdriver



#driver=webbrowser
#driver=webcontext.browser.Chrome()                                #webcontext.browser.Chrome()
#context.browser.maximize_window()

# Login to any account, include - Daphne, clavel, kamala, bucare, pataju

def acc_login(locator_login_email,locator_login_password,locator_login_submit,data_login_email,data_login_password,context):
    #data_import(daphne)
    context.browser.find_element_by_xpath(locator_login_email).send_keys(data_login_email)
    context.browser.find_element_by_xpath(locator_login_password).send_keys(data_login_password)
    context.browser.find_element_by_xpath(locator_login_submit).click()

# Selecting payment option

#click_payment_tab=context.browser.find_element_by_xpath(locator_payment_tab).click()
#click_on_setup_automatic_payment=context.browser.find_element_by_xpath(locator_setup_ach).click()
#click_change_payment_options=context.browser.find_element_by_xpath(locator_change_payment_options).click()

# Adding Checking Account for user

#click_add_new_account=context.browser.find_element_by_xpath("//A[@href='/bank_account_verifications/new'][text()='Add a new payment account']").click()


def add_ach(nickname,institution_name,first_name,\
            last_name,routing_number,account_number,\
            confirmation_account,account_type,create_account,context):
    context.browser.find_element_by_xpath ( nickname ).send_keys ( "Glen" )
    context.browser.find_element_by_xpath ( institution_name ).send_keys ( "fedec" )
    context.browser.find_element_by_xpath ( first_name ).send_keys ( "Glen" )
    context.browser.find_element_by_xpath ( last_name ).send_keys ( "Jones" )
    context.browser.find_element_by_xpath ( routing_number ).send_keys ( "021000021" )
    context.browser.find_element_by_xpath ( account_number ).send_keys ( "156465461412" )
    context.browser.find_element_by_xpath ( confirmation_account ).send_keys (
        "156465456412" )
    context.browser.find_element_by_xpath ( account_type ).click ( )
    context.browser.find_element_by_xpath ( create_account ).click ( )

