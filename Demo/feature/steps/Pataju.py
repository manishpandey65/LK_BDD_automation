from behave import *
from time import sleep
#from selenium.webdriver.common.keys import Keys
import sys
sys.path.append('../feature/lib')
from cust_lib import *
#from feature.lib.cust_lib import *
from locator import *


@Given("open pataju")
def step_impl(context):
    context.browser.maximize_window()
    context.browser.get("http://myaccount.lkqa02.com")

@When("user enter valid credentials")
def step_impl(context):
    context.browser.find_element_by_name('email').send_keys("test0424_1@lendkey.com")
    context.browser.find_element_by_id('password').send_keys("CompactSmith1234")
    context.browser.find_element_by_xpath("//*[@data-test='login_button']").click()
    print("Login successfully")


@Then("summary page")
def step_impl(context):
    actual_data=context.browser.find_element_by_xpath("//*[@class='col-md-12']//h1").text
    expected_data="Account Summary"
    if(actual_data==expected_data):
        True

@When("User is on change payment option")
def step_impl(context):
    #click_payment_tab
    context.browser.find_element_by_xpath(locator_payment_tab).click()
    #context.browser.find_element_by_xpath("(//A[@data-toggle='dropdown'])[2]").click()           # click Payment Tab under myaccount
    sleep(2)
    #click_on_setup_automatic_payment
    context.browser.find_element_by_xpath(locator_setup_ach).click()
    #click_change_payment_options
    context.browser.find_element_by_xpath(locator_change_payment_options).click()

@When("User Select Checking Account")
def step_impl(context):
    sleep(2)
    context.browser.find_element_by_xpath("(//INPUT[@name='loan_payment_method[checking_account_id]'])[2]").click()
    sleep(2)
    context.browser.find_element_by_xpath(
        "(//A[@class='btn btn-primary'][text()='Continue'][text()='Continue'])[1]").click()
    sleep(2)

@When("User select Pay By Check")
def step_impl(context):
    context.browser.find_element_by_xpath("//INPUT[@id='loan_payment_method_checking_account_id_check']").click()
    context.browser.find_element_by_xpath(
        "(//INPUT[@class='button btn btn-primary'])[1]").click()

@When("User select Minimum monthly balance")
def step_impl(context):
    context.browser.find_element_by_xpath("//INPUT[@id='loan_payment_method_payment_type_monthly_payment']").click()
    context.browser.find_element_by_xpath(
        "(//A[@class='btn btn-primary'][text()='Continue'][text()='Continue'])[2]").click()

@When("User adds minimum amount")
def step_impl(context):
    context.browser.find_element_by_xpath(
        "//INPUT[ @ id = 'loan_payment_method_payment_type_monthly_payment_plus_additional']").click()
    context.browser.find_element_by_xpath("//INPUT[@id='loan_payment_method_additional_payment_amount']").clear()
    context.browser.find_element_by_xpath("//INPUT[@id='loan_payment_method_additional_payment_amount']").send_keys(
        "1001")
    context.browser.find_element_by_xpath(
        "(//A[@class='btn btn-primary'][text()='Continue'][text()='Continue'])[2]").click()

@When("User accept ACH authorization")
def step_impl(context):
    context.browser.find_element_by_xpath("//INPUT[@id='loan_payment_method_ach_authorization']").click()
    context.browser.find_element_by_xpath("(//INPUT[@class='button btn btn-primary'])[2]").click()


@Then("Payment method updated successfully")
def step_impl(context):
    context.browser.find_element_by_xpath("// P[text() = 'Payment method has been updated!']")
    #context.driver.find_element_by_xpath("//TD[text()='Minimum Monthly Balance Due + $1,001.00']")

@When("User enter's $0 as amount")
def step_impl(context):
    context.browser.find_element_by_xpath("//INPUT[@id='loan_payment_method_additional_payment_amount']").clear()
    sleep(2)
    context.browser.find_element_by_xpath("//INPUT[@id='loan_payment_method_additional_payment_amount']").send_keys("0")
    sleep(2)
    context.browser.find_element_by_xpath(
        "(//A[@class='btn btn-primary'][text()='Continue'][text()='Continue'])[2]").click()

@when("User Add new Account")
def step_impl(context):
    context.browser.find_element_by_xpath("//A[@href='/bank_account_verifications/new']\
    [text()='Add a new payment account']").click()
    add_ach(locator_nickname,locator_institution_name,locator_first_name,locator_last_name,locator_routing_number, \
            locator_account_number,locator_confirmation_account,locator_account_type, \
            locator_create_account,context)

@Then("Account Added Successfully")
def step_impl(context):
    #text_message=driver.find_element_by_xpath("(//P)[1]").get_text()
    print("thanks")

@Then("User should prompt message for valid amount")
def step_impl(context):
    expectedMessage="Value must be greator than or equal to 1"
    #context.driver.assertTrue(expectedMessage.isDisplayed())
    #self.assertTrue(self.driver.is_text_present(expectedMessage))
    #alertmessage=context.driver.switch_to_alert().getText()
    #print(alertmessage)

@When("user add amount and account  details")
def step_impl(context):
    context.browser.find_element_by_xpath("//A[@href='/loans/adhoc_payments'][text()='Make a one-time payment']").click()
    context.browser.find_element_by_xpath("//A[@href='/loans/VZD-3226/adhoc_payments/new'][text()='Make a Payment']").click()
    #context.browser.find_element_by_xpath("//INPUT[@id='adhoc_payment_date_to_process']").send_keys("2018-05-17")
    context.browser.find_element_by_xpath("//INPUT[@id='adhoc_payment_amount']").send_keys("1000")
    #context.browser.find_element_by_xpath("//SELECT[@id='adhoc_payment_checking_account_id_selected_for_ad_hoc_payment']").click()
    context.browser.find_element_by_xpath("//*[@id='adhoc_payment_checking_account_id_selected_for_ad_hoc_payment']/option[2]").click()

    context.browser.find_element_by_xpath("//*[@id='new_adhoc_payment']/button").click()
    sleep ( 5 )
    context.browser.find_element_by_xpath("//*[@id='affectScheduleNotice']/div/div/div[3]/button[1]").click()

@When("Confirm adhoc payment")
def step_impl(context):
    context.browser.find_element_by_xpath("//INPUT[@class='btn btn-primary pull-right']").click()

@Then("payment submitted")
def step_impl(context):
    context.browser.find_element_by_xpath("//H1[text()='Payment Submitted. Thank you!']")