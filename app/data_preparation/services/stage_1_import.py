import logging
import pandas as pd


logger = logging.getLogger(__name__)


def import_csv_in_dataframe(csv_path: str, logger = logger):
    dataframe = pd.read_csv(csv_path)
    logger.info(f"{dataframe.head()}")
    return dataframe