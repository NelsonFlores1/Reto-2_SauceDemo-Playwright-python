import allure


class IsLoginFailed:
    """Question: Is login failed?"""

    def answered_by(self, actor) -> str:
        with allure.step("Get the login error message text"):
            page = actor.ability.page
            
            locator = page.locator("[data-test='error']")
            locator.wait_for(state='visible')

            return locator.inner_text()