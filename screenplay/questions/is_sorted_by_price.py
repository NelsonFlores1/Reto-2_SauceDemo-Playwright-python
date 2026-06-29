import allure

class IsSortedByPrice:
    """Question: What are the numerical prices of the displayed products?"""

    def answered_by(self, actor) -> list[float]:
        with allure.step("Get the list of displayed product prices"):
            page = actor.ability.page
            locator = page.locator("[data-test='inventory-item-price']")
            locator.first.wait_for(state = "visible")

            raw_prices = locator.all_inner_texts()

            numerical_prices = [float(price.replace("$", "")) for price in raw_prices]

            return numerical_prices
    