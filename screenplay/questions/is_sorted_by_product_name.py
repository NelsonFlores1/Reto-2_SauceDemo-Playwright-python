import allure

class IsSortedByProductName:
    # Question: Are products sorted by name?

    def answered_by(self, actor) -> list[str]:
        with allure.step("Get the list of displayed product names"):
            page = actor.ability.page
            
            locator = page.locator("[data-test='inventory-item-name']")
            locator.first.wait_for(state="visible")

            return locator.all_inner_texts()