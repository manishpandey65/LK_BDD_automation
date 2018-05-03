from behave import *
import time
from selenium.webdriver.common.keys import Keys



@Given("PSL Network Cuscholar")
def step_impl(context):
    context.browser.get( "http://cuscholar15i.lkqa02.com/loans/new")

@When("Eligibility Page")
def step_impl(context):
    context.browser.find_element_by_xpath("//INPUT[@id='student_eligibility_test_requested_amount']").send_keys('25000')
    context.browser.find_element_by_xpath("//LABEL[@class='collection_radio_buttons'][text()='Graduate']").click()
	""""
    context.browser.find_element_by_xpath("//INPUT[@id='student_eligibility_test_requested_amount']").send_keys("25000")
    context.browser.find_element_by_xpath("//LABEL[@class='collection_radio_buttons'][text()='Graduate']").click()
    context.browser.find_element_by_xpath("//SPAN[@class='filter-option pull-left'][text()='Select a School']").click()
    time.sleep(3)
    context.browser.find_element_by_xpath("//SPAN[@class='text'][text()='Adelphi University']").click()
    context.browser.find_element_by_xpath("//*[@id='student_eligibility_test_graduation_date_2i']/option[13]").click()
    context.browser.find_element_by_xpath("//*[@id='student_eligibility_test_graduation_date_1i']/option[6]").click()
    context.browser.find_element_by_xpath("//*[@id='student_eligibility_test_academic_period_start_date_2i']/option[1]").click()
    context.browser.find_element_by_xpath("//*[@id='student_eligibility_test_academic_period_start_date_1i']/option[2]").click()
    context.browser.find_element_by_xpath("//*[@id='student_eligibility_test_academic_period_end_date_2i']/option[7]").click()
    context.browser.find_element_by_xpath("//*[@id='student_eligibility_test_academic_period_end_date_1i']/option[2]").click()
    context.browser.find_element_by_xpath("//*[@id='student_eligibility_test_class_standing']/option[5]").click()
    context.browser.find_element_by_xpath("//*[@id='student_eligibility_test_gpa_range']/option[5]").click()
    context.browser.find_element_by_xpath("//SPAN[@class='filter-option pull-left'][text()='Choose a Major']").click()
    context.browser.find_element_by_xpath("// SPAN[ @class ='text'][text()='Applied Mathematics']").click()
    context.browser.find_element_by_xpath("//INPUT[@id='student_eligibility_test_full_time_full-time']").click()
    context.browser.find_element_by_xpath("//LABEL[@class='collection_radio_buttons'][text()='Permanent Resident']").click()
    context.browser.find_element_by_xpath("//LABEL[@class='collection_radio_buttons'][text()='Apply without a Cosigner']").click()
    context.browser.find_element_by_xpath("//INPUT[@id='student_eligibility_test_email']").send_keys("test0329_1@lendkey.com")
    context.browser.find_element_by_xpath("//INPUT[@id='eligibility_test_submit']").click()
"""
    time.sleep(5)

@Then("Application Page")
def step_impl(context):
    #context.browser
    print("Thanks")

@Given("open the loan from Daphne")
def step_impl(context):
    main_window = context.browser.current_window_handle
    context.browser.get("http://ops.lkqa02.com/access/LKA-7563/login?return=%2Floans%2FLKA-7563")
    context.browser.find_element_by_xpath("//INPUT[@id='email']").send_keys("manish.pandey@lendkey.net")
    context.browser.find_element_by_xpath("//INPUT[@id='password']").send_keys("CompactSmith1234")
    context.browser.find_element_by_xpath("//INPUT[@type='submit']").click()
    time.sleep(6)
    context.browser.find_element_by_xpath("//*[@id='action_select']/option[3]").click()
    context.browser.find_element_by_xpath("//A[@id='action_link_to_trigger']").send_keys(Keys.CONTROL + Keys.ENTER)
    #time.sleep(3)
    context.browser.switch_to_window(context.browser.window_handles[1])
    time.sleep(10)

@When("Application Page")
def step_impl(context):
    #PDF extraction
    """
    r = requests.get ( 'http://cuscholar15i.lkqa02.com/loans/LKA-7563/inline_verification_pdf#toolbar=0&statusbar=0&messages=0&navpanes=0' ,stream=True )
    f = io.BytesIO ( r.content )
    reader = PdfFileReader ( f )
    contents = reader.getPage ( 1 ).extractText ( ).split ( '\n' )
    print(contents)
    f.close ( )
    """
    #context.browser.switch_to_window(context.browser.window_handles[0])
    #time.sleep(10)
    context.browser.find_element_by_xpath ( "//INPUT[@id='petition_for_student_borrower_borrower_attributes_first_name']" ).send_keys("shaun")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_middle_initial']").send_keys("")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_last_name']").send_keys("davis")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_social_security_number']").send_keys("878543214")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_date_of_birth']").send_keys("03/13/1996")
    #context.browser.find_element_by_xpath("//H3[@class='lk-subheading'][text()='Permanent Address ']").click()
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_address_attributes_street_address']").send_keys("123 street dr")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_address_attributes_secondary_address']").send_keys("")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_address_attributes_city']").send_keys("New York")
    context.browser.find_element_by_xpath("//*[@id='petition_for_student_borrower_borrower_attributes_address_attributes_state_id']/optgroup[1]/option[4]").click()
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_address_attributes_zip_code']").send_keys("10001")
    context.browser.find_element_by_xpath("//*[@id='petition_for_student_borrower_borrower_attributes_preferred_phone']/option[3]").click()
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_primary_phone']").send_keys("1234567890")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_employment_attributes_annual_income']").send_keys("200000")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_password']").send_keys("CompactSmith1234")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_borrower_attributes_password_confirmation']").send_keys("CompactSmith1234")
    #from selenium.webdriver.support.select import Select
    #select_code = Select(context.browser.find_element_by_xpath("//OBJECT[@id='object_verification_pdf']"))
    #code=select_code.first_selected_option
    context.browser.find_element_by_xpath("//OBJECT[@id='object_verification_pdf']").click()
    context.browser.find_element_by_xpath("//OBJECT[@id='object_verification_pdf']").send_keys(Keys.CONTROL, "a")
    context.browser.find_element_by_xpath("//OBJECT[@id='object_verification_pdf']").send_keys(Keys.CONTROL, "c")
    context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_pdf_verification_attributes_code_confirmation']").send_keys(Keys.CONTROL,"v")
    code_value=context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_pdf_verification_attributes_code_confirmation']").get_attribute('value')
    code=code_value[0:3]
    context.browser.find_element_by_xpath(
        "//INPUT[@id='petition_for_student_borrower_pdf_verification_attributes_code_confirmation']").send_keys(
        Keys.CONTROL,"a")
    context.browser.find_element_by_xpath(
        "//INPUT[@id='petition_for_student_borrower_pdf_verification_attributes_code_confirmation']").send_keys(
        code)
    #context.browser.find_element_by_xpath("//BODY[@id='body_petitions']").click()
    time.sleep(15)
    #context.browser.find_element_by_xpath("//H3[@class='lk-subheading'][text()='Review Disclosures']").click()
    #time.sleep(3)
    context.browser.find_element_by_xpath("//*[@id='disclosures_dialog']/div/div/div[3]/button").click()
    context.browser.find_element_by_xpath("//INPUT[@id='h21_accept']").click()
    #context.browser.find_element_by_xpath("//INPUT[@id='petition_for_student_borrower_submit']").click()

@Then("Thanks")
def step_impl(context):
    print("thank you")

#KXR-3934