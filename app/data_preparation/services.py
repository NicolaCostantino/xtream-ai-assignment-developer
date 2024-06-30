import logging
import pandas as pd


logger = logging.getLogger(__name__)


def import_csv_in_dataframe(csv_path: str, logger = logger):
    dataframe = pd.read_csv(csv_path)
    logger.info(f"{dataframe.head()}")
    return dataframe

def check_dataframe(dataframe, logger = logger):
    checks = [
        _check_for_missing_values,
        _check_for_zero_dimensional_stones,
        _check_for_negative_prices,
    ]
    for check in checks:
        check(dataframe, logger)

# Checks

def _check_for_missing_values(dataframe, logger = logger):
    result = dataframe.isna().sum()
    logger.info(f"_check_for_missing_value: {result}")
    assertion_text = "Missing values found"
    assertion = (result == 0).all()
    logger.info(f"{assertion_text}: {assertion}")
    assert assertion, assertion_text

def _check_for_zero_dimensional_stones(dataframe, logger = logger):
    result = dataframe[dataframe.x * dataframe.y * dataframe.z == 0]
    logger.info(f"{result}")
    assertion_text = "Zero dimensional stones found"
    assertion = result.empty
    logger.info(f"{assertion_text}: {assertion}")
    assert assertion, assertion_text

def _check_for_negative_prices(dataframe, logger = logger):
    result = dataframe[dataframe.price <= 0]
    logger.info(f"{result}")
    assertion_text = "Negative prices found"
    assertion = result.empty
    logger.info(f"{assertion_text}: {assertion}")
    assert assertion, assertion_text