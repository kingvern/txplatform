from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

from operation.models import BuyerPatent, BuyerProject
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Delete objects older than 24 hours'

    def handle(self, *args, **options):
        outdate_orders = BuyerPatent.objects.filter(
            Q(step_time__gte=datetime.now() - timedelta(seconds=10)) & Q(step='0'))
        for outdate_order in outdate_orders:
            outdate_order.step = '-1'
        self.stdout.write('Deleted objects older than 24 hours')
