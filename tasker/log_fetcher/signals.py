import re
import threading
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from log_fetcher.models import Fetcher
from log_fetcher.threads import fetch_log


@receiver(post_save, sender=Fetcher, dispatch_uid="save_query_info")
def save_query_info(sender, instance, created, **kwargs):
    if created:
        # match strings like /tmp/jboss_log_1542210082.tar.gz
        path_pattern = re.compile(r'/tmp/jboss_log_[0-9]+\.tar\.gz')

        thread = threading.Thread(
            target=fetch_log, args=(instance, path_pattern))
        thread.setDaemon = True
        thread.start()


@receiver(post_save, sender=Fetcher)
def debug_info(sender, **kwargs):
    print('Finish')
