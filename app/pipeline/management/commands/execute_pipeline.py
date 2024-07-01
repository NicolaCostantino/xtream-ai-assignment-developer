import logging
from django.core.management.base import BaseCommand

from ...services import pipeline_1


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    # Mapping the args allow to change the internal and external name for each (e.g. verbose outside, shorter inside)
    mapping = {
        "pipeline_n": "pipeline_number",
        "dataset_path": "dataset_path",
    }

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(self.mapping["pipeline_n"], nargs=1, type=int)
        parser.add_argument(self.mapping["dataset_path"], nargs=1, type=str)

    def handle(self, *args, **options):
        pipeline_n = options[self.mapping["pipeline_n"]][0]
        logger.info(f"Selected pipeline number: {pipeline_n}")
        dataset_path = options[self.mapping["dataset_path"]][0]
        logger.info(f"Selected pipeline number: {dataset_path}")
        
        if pipeline_n == 1:
            pipeline_1(dataset_path)
        else:
            raise Exception(f"Pipeline {pipeline_n} not found")