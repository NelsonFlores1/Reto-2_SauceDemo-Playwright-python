import allure
from pytest_bdd import given, when, then, parsers

from screenplay.actors.actor import Actor
from screenplay.interactions.navigate_to import NavigateTo
from screenplay.tasks.login import Login
from screenplay.questions.is_login_failed import IsLoginFailed

# @allure.feature("Authentication")
# @given("the user wants to access the store from login page")
# def navigate_to_login_page(actor: Actor):
#     """Navigate the browser to the Saucedemo login page"""
#     actor.attempts_to("https://www.saucedemo.com")

# @when(
#     parsers.parse('he logs in with username "{username}" and password "{password}"'),
#     target_fixture = "login_result",
# )
# def enter_credentials(actor: Actor, username: str, password: str):
#     """Fill in credentials and submit the login form."""
#     actor.attempts_to(Login(username, password))

@then(parsers.parse("he should see an error message saying '{expected_error_message}'"))
def verify_error_message_displayed(actor: Actor, expected_error_message: str):
    """Assert that the error message is displayed."""
    actual_error = actor.asks_about(IsLoginFailed())

    assert actual_error == expected_error_message, \
    f"Login error mismatch.\nExpected: '{expected_error_message}'\nActual: '{actual_error}'"