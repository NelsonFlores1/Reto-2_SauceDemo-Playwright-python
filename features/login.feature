Feature: User Authentication in Saucedemo
    As a customer of the store
    I want to log in securely with my credentials
    So that I can browse and purchase products

    Scenario:
        Given the user wants to access the store from login page
        When he logs in with username "standard_user" and password "secret_sauce"
        Then he should see the inventory page
