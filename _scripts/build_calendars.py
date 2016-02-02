from datetime import datetime, timedelta
import icalendar as cal
from glob import glob
import pytz
import yaml


c = cal.Calendar()

c.add('prodid', '-//KnoxGearhead Calendar//knoxgearhead.com//')
c.add('version', '0.0.1')

for f in glob('_posts/*.markdown'):
    e = cal.Event()

    with open(f, 'r') as txtfile:
        txt = txtfile.read()

    info = yaml.load(txt.split('---')[1])

    e.add('summary', info['title'])
    e.add('dtstart', info['date'].replace(tzinfo=pytz.timezone('US/Eastern')))
    e.add('dtend', info['date'].replace(tzinfo=(pytz.timezone('US/Eastern')))+timedelta(hours=1))

    organizer = cal.vCalAddress('MAILTO:knoxgearhead@knoxgearhead.com')
    organizer.params['cn'] = cal.vText('KnoxGearhead')
    e.add('organizer', organizer)
    e['uid'] = str(info['date']) + '/' + info['title']

    c.add_component(e)


with open('calendars/tmp.ics', 'w') as f:
    f.write(c.to_ical())