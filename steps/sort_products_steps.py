import allure
from pytest_bdd import given, when, then, parsers

from screenplay.actors.actor import Actor
from screenplay.tasks.sort_products import SortProducts
from screenplay.questions.is_sorted_by_price import IsSortedByPrice
from screenplay.questions.is_sorted_by_product_name import IsSortedByProductName

@when(parsers.parse("he sorts the products by '{sort_option}'"))
def sort_products(actor: Actor, sort_option: str):
    actor.attempts_to(
        SortProducts(sort_option)  
    )

@then(parsers.parse("the product should be sorted by '{sort_order}'"))
def verify_product_sorting(actor: Actor, sort_order: str):
    
    if "Name" in sort_order:
        actual_list = actor.asks_about(IsSortedByProductName())

        if sort_order == "Name (A to Z)":
            expected_list = sorted(actual_list)
        elif sort_order == "Name (Z to A)":
            expected_list = sorted(actual_list, reverse=True)
        
    elif "Price" in sort_order:
        actual_list = actor.asks_about(IsSortedByPrice())

        if sort_order == "Price (low to high)":
            expected_list = sorted(actual_list)
        elif sort_order == "Price (high to low)":
            expected_list = sorted(actual_list, reverse=True)

    else: 
        raise ValueError(f"Sort option '{sort_order}' is not supported")
    
    error_message = (
        f"Sorting failed for '{sort_order}'.\n"
        f"Expected: {expected_list}\n"
        f"Actual:   {actual_list}"
    )

    assert actual_list == expected_list, error_message