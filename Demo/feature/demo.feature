Feature: Getting Experian Profile from dump
  Scenario: Eligibility
    Given PSL Network Cuscholar
    When Eligibility Page
    Then Application Page

"""
  Scenario: Application
    Given open the loan from Daphne
    When Application Page
    Then Thanks
"""

