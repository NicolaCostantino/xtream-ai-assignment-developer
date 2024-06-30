import logging

from ..exceptions import (MissingValues,
                         ZeroDimensionalStonesFound,
                         NegativePricesFound,)


logger = logging.getLogger(__name__)


def run_checks_on_dataframe(dataframe, checks, pass_on_failure=False, logger = logger):
    """
    Checks runner: run a list of tests over a dataframe
    - all the tests have the same interface
    - each test raises a specific domain exception (which can be only logged or re-raised)
    """
    try:
        for check in checks:
            check(dataframe, logger)
    except Exception as e:
        if pass_on_failure == True:
            pass
        else:
            raise e


# Checks

def check_for_missing_values(dataframe, logger = logger):
    result = dataframe.isna().sum()
    logger.info(f"check_for_missing_value: {result}")
    try:
        assertion_text = "Missing values found"
        assertion = (result == 0).all()
        logger.info(f"{assertion_text}: {assertion}")
        assert assertion, assertion_text
    except AssertionError as e:
        raise MissingValues(assertion_text)

def check_for_zero_dimensional_stones(dataframe, logger = logger):
    result = dataframe[dataframe.x * dataframe.y * dataframe.z == 0]
    logger.info(f"check_for_zero_dimensional_stones: {result}")
    try:
        assertion_text = "Zero dimensional stones found"
        assertion = result.empty
        logger.info(f"{assertion_text}: {assertion}")
        assert assertion, assertion_text
    except AssertionError as e:
        raise ZeroDimensionalStonesFound(assertion_text)

def check_for_negative_prices(dataframe, logger = logger):
    result = dataframe[dataframe.price <= 0]
    logger.info(f"check_for_negative_prices: {result}")
    try:
        assertion_text = "Negative prices found"
        assertion = result.empty
        logger.info(f"{assertion_text}: {assertion}")
        assert assertion, assertion_text
    except AssertionError as e:
        raise NegativePricesFound(assertion_text)
