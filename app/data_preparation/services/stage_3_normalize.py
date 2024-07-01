import logging
import pandas as pd


logger = logging.getLogger(__name__)


def normalize_dataframe(dataframe, actions, logger = logger):
    """
    Normalization runner: run a list of corrections over a dataframe
    - all the actions have the same interface
    - all the actions are applied over the result of the previous action (pipeline pattern)
    - each action returns a new dataframe with the result of the application
    """
    try:
        processed_dataframe = dataframe
        for action in actions:
            processed_dataframe = action(processed_dataframe, logger)
        return processed_dataframe
    except Exception as e:
        # Anything to do here...?
        raise e


# Normalizations

def remove_negative_priced_and_wrongly_sized_items(dataframe, logger = logger):
    # INFO: this could/should be splitted - keeping it here as in the original notebook for simplicity
    result = dataframe[(dataframe.x * dataframe.y * dataframe.z != 0) & (dataframe.price > 0)]
    logger.info(f"remove_negative_priced_and_wrongly_sized_items: {result}")
    return result

def drop_useless_columns(dataframe, logger = logger):
    result = dataframe.drop(columns=['depth', 'table', 'y', 'z'])
    return result

def create_dummy_variables(dataframe, logger = logger):
    result = pd.get_dummies(dataframe, columns=['cut', 'color', 'clarity'], drop_first=True)
    return result