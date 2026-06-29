"""Shared login step definitions using Screenplay Pattern"""

import allure
from pytest_bdd import given, when, then, parsers

from screenplay.actors.actor import Actor
from screenplay.interactions.navigate_to import NavigateTo
from screenplay.tasks.login import Login
from screenplay.questions.is_logged_in import IsLoggedIn

@allure.feature("Authentication")
@given("the user wants to access the store from login page")
def navigate_to_login_page(actor: Actor):
    """Navigate the browser to the Saucedemo login page"""
    actor.attempts_to("https://www.saucedemo.com")

@when(
    parsers.parse('he logs in with username "{username}" and password "{password}"'),
    target_fixture = "login_result",
)
def enter_credentials(actor: Actor, username: str, password: str):
    """Fill in credentials and submit the login form."""
    actor.attempts_to(Login(username, password))

@then("he should see the inventory page")
def verify_dashboard_displayed(actor: Actor):
    """Assert that the user is logged in and the product page is visible"""
    assert actor.asks_about(IsLoggedIn()), (
        "Login failed: the product page is not displayed."
    )