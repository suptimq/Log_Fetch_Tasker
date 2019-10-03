import time
import subprocess
from threading import Thread


def fetch_log(instance, path_pattern):
    app_name = instance.app_name
    start_date = instance.start_date.strftime('%Y-%m-%d %H:%M')
    end_date = instance.end_date.strftime('%Y-%m-%d %H:%M')
    instance.task_status = 'R'
    instance.save(update_fields=['task_status'])

    proc = subprocess.run(
        ['/usr/local/bin/tsle', app_name, start_date, end_date],
        stdout=subprocess.PIPE)
    proc_stdout = proc.stdout.decode('utf-8')
    file_path = path_pattern.search(proc_stdout).group()
    instance.file_path = file_path
    instance.task_status = 'D'
    instance.save(update_fields=['file_path', 'task_status'])
