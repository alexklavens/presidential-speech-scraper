from datetime import datetime
import math

def printEstimatedCompletionTime(lastTime,currentTime,remainingIterations):
    interval = currentTime - lastTime
    duration_in_s = interval.total_seconds()      # Total number of seconds between dates

    timeLeft = remainingIterations * duration_in_s

    minutes = timeLeft//60
    seconds = timeLeft%60
    print("This should take about",int(minutes),"minutes and",int(seconds),"seconds.")

def _formatDate(dateString):
    month_lst = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']

    month = dateString.split()
    for m in month_lst:
        if month[0].lower() in m:
            return str(datetime.strptime(('{} {}, {}'.format(m.title(),month[1][:-1],month[2])),'%B %d, %Y'))
