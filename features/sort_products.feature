Feature: Sort products in Product page

Scenario: Sort products by name and price
    Given the user wants to access the store from login page
    And he logs in with username "standard_user" and password "secret_sauce"
    When he sorts the products by "Name (Z to A)"
    Then the product should be sorted by "Name (Z to A)"
    
    When he sorts the products by "Price (low to high)"
    Then the product should be sorted by "Price (low to high)"
    When he sorts the products by "Price (high to low)"
    Then the product should be sorted by "Price (high to low)"
    When he sorts the products by "Name (A to Z)"
    Then the product should be sorted by "Name (A to Z)"
