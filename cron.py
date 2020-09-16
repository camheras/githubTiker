from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command='python3 test.py')
job.minute.every(1)
cron.write()
