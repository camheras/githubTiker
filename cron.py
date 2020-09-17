from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command='python3 main.py --repo username/repo --token your_github_token --fb_username your_fb_username --fb_password your_fb_password --fb_group your_fb_group')
job.minute.every(1)
cron.write()
