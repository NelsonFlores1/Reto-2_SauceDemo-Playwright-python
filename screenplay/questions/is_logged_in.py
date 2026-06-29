import allure


class IsLoggedIn:
    """Question: Is the user currently logged in?"""

    def answered_by(self, actor) -> bool:
        with allure.step("Check if user is logged in"):
            page = actor.ability.page
            if page.locator("data-test='title'").is_visible():
                return True
            return page.locator("class='app_logo'").first.is_visible()