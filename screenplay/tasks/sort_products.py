import allure
from screenplay.interactions.select_option import SelectOption

class SortProducts:
    # Task to sort products
    SORT_DROPDOWN = "[data-test='product-sort-container']"

    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Value to sort is required and cannot be empty.")
        self._value = value

    def perform_as(self, actor) -> None:
        with allure.step(f"Sort products by {self._value}"):
            actor.attempts_to(
                SelectOption(self.SORT_DROPDOWN, self._value),
            )
        