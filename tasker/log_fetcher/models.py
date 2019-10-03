from django.db import models

# Create your models here.


class Fetcher(models.Model):
    APP_NAME = (
        ('api_1', 'api_1'),
        ('erp_1', 'erp_1'),
    )
    app_name = models.CharField(
        max_length=10,
        choices=APP_NAME,
        blank=True,
    )

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    file_path = models.CharField(
        'log path',
        max_length=100,
        blank=True,
        editable=False,
    )

    TASK_STATE = (
        ('R', 'running'),
        ('D', 'done'),
        ('F', 'failed'),
    )
    task_status = models.CharField(
        max_length=10,
        choices=TASK_STATE,
        blank=True,
        editable=False,
    )

    def __str__(self):
        return '{0} {1} {2}'.format(self.app_name, self.start_date,
                                    self.end_date)
