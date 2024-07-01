import logging

from data_preparation.services.stage_1_import import import_csv_in_dataframe
from data_preparation.services.stage_2_check import (run_checks_on_dataframe,
                                                     check_for_missing_values,
                                                     check_for_negative_prices,
                                                     check_for_zero_dimensional_stones,)
from data_preparation.services.stage_3_normalize import (normalize_dataframe,
                                                         remove_negative_priced_and_wrongly_sized_items,
                                                         drop_useless_columns,
                                                         create_dummy_variables,)


logger = logging.getLogger(__name__)


def pipeline_1(dataset_path):
    logger.info("Starting pipeline number 1")

    # Retrieve dataframe
    dataframe = import_csv_in_dataframe(dataset_path)

    # Execute checks
    checks = [
        check_for_missing_values,
        check_for_zero_dimensional_stones,
        check_for_negative_prices,
    ]
    run_checks_on_dataframe(dataframe, checks, False)

    # Normalize data
    actions = [
        remove_negative_priced_and_wrongly_sized_items,
        drop_useless_columns,
        create_dummy_variables,
    ]
    processed_dataframe = normalize_dataframe(dataframe, actions)

    # Model training
    # TODO: import the appropriate model training from the model_training app