import logging
from django.core.management.base import BaseCommand
from ...services import import_csv_in_dataframe, check_dataframe


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
        dataframe = import_csv_in_dataframe(csv_path, logger)
        check_dataframe(dataframe, logger)