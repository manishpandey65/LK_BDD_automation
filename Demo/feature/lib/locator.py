requested_loan_amount="//INPUT[@id='student_eligibility_test_requested_amount']"
degree_type_graduate="//LABEL[@class='collection_radio_buttons'][text()='Graduate']"
degree_type_undergraduate="//LABEL[@class='collection_radio_buttons'][text()='Undergraduate']"
school_list="//SPAN[@class='filter-option pull-left'][text()='Select a School']"
select_school="//SPAN[@class='text'][text()='Adelphi University']"
expected_graduation_month="//*[@id='student_eligibility_test_graduation_date_2i']/option[13]"
expected_graduation_year="//*[@id='student_eligibility_test_graduation_date_1i']/option[6]"
academic_start_month="//*[@id='student_eligibility_test_academic_period_start_date_2i']/option[1]"
academic_start_year="//*[@id='student_eligibility_test_academic_period_start_date_1i']/option[2]"
academic_end_month="//*[@id='student_eligibility_test_academic_period_end_date_2i']/option[7]"
academic_end_year="//*[@id='student_eligibility_test_academic_period_end_date_1i']/option[2]"
class_standing="//*[@id='student_eligibility_test_class_standing']/option[5]"
GPA_range="//*[@id='student_eligibility_test_gpa_range']/option[5]"
click_subject="//SPAN[@class='filter-option pull-left'][text()='Choose a Major']"
choose_subject="// SPAN[ @class ='text'][text()='Applied Mathematics']"




###########---------Pataju--------------------############################

# Login to application
locator_login_email="//INPUT[@id='email']"
locator_login_password="//INPUT[@id='password']"
locator_login_submit="//*[@data-test='login_button']"

# Change in Payment
locator_payment_tab="(//A[@data-toggle='dropdown'])[2]"
locator_setup_ach="// A[ @ href = '/loans/setup_payment_accounts'][text() = 'Setup Automatic Payments']"
locator_change_payment_options ="(//a[text()='Change Payment Options'])[1]"

# Adding new account
locator_nickname="//INPUT[@id='bank_account_verification_nickname']"
locator_institution_name="//INPUT[@id='bank_account_verification_institution_name']"
locator_first_name="//INPUT[@id='bank_account_verification_account_holder_first_name']"
locator_last_name="//INPUT[@id='bank_account_verification_account_holder_last_name']"
locator_routing_number="//INPUT[ @ id = 'bank_account_verification_routing_number']"
locator_account_number="//INPUT[@id='bank_account_verification_account_number']"
locator_confirmation_account="//INPUT[@id='bank_account_verification_account_number_confirmation']"
locator_account_type="//SELECT[@id='bank_account_verification_account_type']//option[1]"
locator_create_account="//*[@data-test='create_account_button']"