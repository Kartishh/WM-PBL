from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import track

scheduler = BlockingScheduler()

# run every 10 minutes (change as needed)
scheduler.add_job(track, "interval", minutes=1)

print("Scheduler started... Ctrl+C to stop")
scheduler.start()
