import logging
import time
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.db.models import Q
from django.db.models import Avg, Count, Min, Sum
from category.models import Category
from utils.category_utils import (
  scan_categories,
  scan_categories_by_re,
  repaire_category_balance
)


logger = logging.getLogger(__name__)


def check_category_by_file_job():
  # Your job processing logic here...
  print('==== run check_category_by_file_job.')
  scan_categories()
  return


def check_category_by_re_job():
  # Your job processing logic here...
  print('==== run check_category_by_re_job.')
  scan_categories_by_re()
  return

def check_category_balance():
  # Your job processing logic here...
  print('==== run check_category_balance.')
  categories = Category.objects.all()
  for cat in categories:
    repaire_category_balance(cat)
    time.sleep(1)
  return


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after our job has run.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
  """
  This job deletes APScheduler job execution entries older than `max_age` from the database.
  It helps to prevent the database from filling up with old historical records that are no
  longer useful.
  
  :param max_age: The maximum length of time to retain historical job execution records.
                  Defaults to 7 days.
  """
  DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
  help = "Runs APScheduler."

  def handle(self, *args, **options):
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
      check_category_by_file_job,
      trigger=CronTrigger(hour="*/8"),  # Every 2 hours
      id="check_category_by_file_job",  # The `id` assigned to each job MUST be unique
      max_instances=1,
      replace_existing=True,
    )
    logger.info("Added job 'check_category_by_file_job'.")

    scheduler.add_job(
      check_category_by_re_job,
      trigger=CronTrigger(hour="*/12"),
      id="check_category_by_re_job",
      max_instances=1,
      replace_existing=True,
    )
    logger.info("Added job 'check_category_by_re_job'.")

    check_category_balance
    scheduler.add_job(
      check_category_balance,
      trigger=CronTrigger(hour="*/1"),
      id="check_category_balance",  # The `id` assigned to each job MUST be unique
      max_instances=1,
      replace_existing=True,
    )
    logger.info("Added job 'check_category_balance'.")

    scheduler.add_job(
      delete_old_job_executions,
      trigger=CronTrigger(
          hour="23", minute="00"
      ),  # Midnight on Monday, before start of the next work week.
      id="delete_old_job_executions",
      max_instances=1,
      replace_existing=True,
    )
    logger.info(
      "Added daily job: 'delete_old_job_executions'."
    )

    try:
      logger.info("Starting scheduler...")
      scheduler.start()
    except KeyboardInterrupt:
      logger.info("Stopping scheduler...")
      scheduler.shutdown()
      logger.info("Scheduler shut down successfully!")
