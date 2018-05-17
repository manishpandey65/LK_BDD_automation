Feature: Testing My Account
  Scenario: User successfully login
    Given open pataju
    When user enter valid credentials
    Then summary page


  Scenario: Perform Adhoc Payment
    When user add amount and account  details
    When Confirm adhoc payment
    Then payment submitted

  Scenario: user add checking account
    When User Add new Account
    Then Account Added Successfully


"""
User is on change payment option
User Select Checking Account
User select Pay By Check
User select Minimum monthly balance
User adds minimum amount
User accept ACH authorization
Payment method updated successfully
User enter's $0 as amount
User Add new Account
Account Added Successfully
User should prompt message for valid amount
"""