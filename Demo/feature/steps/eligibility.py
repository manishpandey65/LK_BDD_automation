from selenium import webdriver

# Url
Eligibility_PSL_network="http://cuscholar15i.lkqa02.com/loans/new"
Amount="find_element_by_xpath('//INPUT[@id='student_eligibility_test_requested_amount']').send_keys('25000')"
"""
    find_element_by_xpath("//LABEL[@class='collection_radio_buttons'][text()='Graduate']").click()
    find_element_by_xpath("//SPAN[@class='filter-option pull-left'][text()='Select a School']").click()
    time.sleep(3)
    find_element_by_xpath("//SPAN[@class='text'][text()='Adelphi University']").click()
    find_element_by_xpath("//*[@id='student_eligibility_test_graduation_date_2i']/option[13]").click()
    find_element_by_xpath("//*[@id='student_eligibility_test_graduation_date_1i']/option[6]").click()
    find_element_by_xpath("//*[@id='student_eligibility_test_academic_period_start_date_2i']/option[1]").click()
    find_element_by_xpath("//*[@id='student_eligibility_test_academic_period_start_date_1i']/option[2]").click()
    find_element_by_xpath("//*[@id='student_eligibility_test_academic_period_end_date_2i']/option[7]").click()
    find_element_by_xpath("//*[@id='student_eligibility_test_academic_period_end_date_1i']/option[2]").click()
    find_element_by_xpath("//*[@id='student_eligibility_test_class_standing']/option[5]").click()
    find_element_by_xpath("//*[@id='student_eligibility_test_gpa_range']/option[5]").click()
    find_element_by_xpath("//SPAN[@class='filter-option pull-left'][text()='Choose a Major']").click()
    find_element_by_xpath("// SPAN[ @class ='text'][text()='Applied Mathematics']").click()
    find_element_by_xpath("//INPUT[@id='student_eligibility_test_full_time_full-time']").click()
    find_element_by_xpath("//LABEL[@class='collection_radio_buttons'][text()='Permanent Resident']").click()
    find_element_by_xpath("//LABEL[@class='collection_radio_buttons'][text()='Apply without a Cosigner']").click()
    find_element_by_xpath("//INPUT[@id='student_eligibility_test_email']").send_keys("test0329_1@lendkey.com")
    find_element_by_xpath("//INPUT[@id='eligibility_test_submit']").click()
    time.sleep(15)
"""