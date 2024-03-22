from django.core.management import BaseCommand

from task_app.consuming import KafkaConsumer


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Running task_tracker consumer...')
        KafkaConsumer().consume()
        print('Consumer disconnected')
