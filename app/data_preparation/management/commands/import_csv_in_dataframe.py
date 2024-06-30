import logging
from django.core.management.base import BaseCommand

from ...services import (import_csv_in_dataframe,
                         run_checks_on_dataframe,
                         check_for_missing_values,
                         check_for_zero_dimensional_stones,
                         check_for_negative_prices,)


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    mapping = {
        "csv_path": "csv_path"
    }

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(self.mapping["csv_path"], nargs=1, type=str)

    def handle(self, *args, **options):
        csv_path = options[self.mapping["csv_path"]][0]
        logger.info(f"csv_path: {csv_path}")
        dataframe = import_csv_in_dataframe(csv_path, logger)
        checks = [
            check_for_missing_values,
            check_for_zero_dimensional_stones,
            check_for_negative_prices,
        ]
        pass_on_failure = False
        run_checks_on_dataframe(dataframe, checks, pass_on_failure, logger)