from apscheduler.schedulers.background import BackgroundScheduler
from cita.update import update_somthing, sms_remminder

from apscheduler.triggers.cron import CronTrigger
trigger = CronTrigger(hour='12', minute='00')

trigger2 = CronTrigger(hour='6', minute='15')

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_somthing, trigger, replace_existing=True, max_instances=1, id='reminder1')
    scheduler.add_job(sms_remminder, trigger2, replace_existing=True, max_instances=1, id='reminder2')
    scheduler.start()
