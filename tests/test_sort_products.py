from pytest_bdd import scenarios

# Import step definitions so pytest-bdd can discover them
from steps.login_steps import *  # noqa: F401, F403
from steps.sort_products_steps import *  # noqa: F401, F403

# Load all scenarios from the feature file
scenarios("sort_products.feature")