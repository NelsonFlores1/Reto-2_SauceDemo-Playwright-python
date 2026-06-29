Feature: Blocked user Authentication
    As a blocked customer
    I want to be prevented from logging into the store
    So that the system system displays an error message

    Scenario: Attempting to log in with a blocked account
        Given the user wants to access the store from login page
        When he logs in with username "locked_out_user" and password "secret_sauce"
        Then he should see an error message saying "Epic sadface: Sorry, this user has been locked out."
