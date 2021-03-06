from datetime import datetime, timedelta
import dateutil.relativedelta as drel
import icalendar as cal
from glob import glob
import pytz
import yaml



# ALL EVENTS
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

    if 'end_date' in info:
        end_time = info['end_date']
    elif 'rec_end' in info:
        end_time = info['date'] + drel.relativedelta(hour=info['rec_end'].hour)
    else:
        end_time = info['date'] + drel.relativedelta(hours=4)

    e.add('dtend', end_time.replace(tzinfo=(pytz.timezone('US/Eastern'))))

    organizer = cal.vCalAddress('MAILTO:knoxgearhead@knoxgearhead.com')
    organizer.params['cn'] = cal.vText('KnoxGearhead')
    e.add('organizer', organizer)
    e['uid'] = str(info['date']) + '/' + info['title']
    e['location'] = cal.vText(info['address'])
    e['description'] = cal.vText('http://www.knoxgearhead.com \nWebsite: {}\n Location: {}\n\n{}'.format(info['website'], info['location'], txt.split('---')[-1]))

    c.add_component(e)


with open('calendars/all_events.ics', 'w') as f:
    f.write(c.to_ical())
    
    
# CAR SHOWS
c = cal.Calendar()

c.add('prodid', '-//KnoxGearhead Carshow Calendar//knoxgearhead.com//')
c.add('version', '0.0.1')

for f in glob('_posts/*.markdown'):
    
    with open(f, 'r') as txtfile:
        txt = txtfile.read()
    info = yaml.load(txt.split('---')[1])
    
    if "carshow" in info['categories']:
    
        e = cal.Event()
    
    
        e.add('summary', info['title'])
        e.add('dtstart', info['date'].replace(tzinfo=pytz.timezone('US/Eastern')))
    
        if 'end_date' in info:
            end_time = info['end_date']
        elif 'rec_end' in info:
            end_time = info['date'] + drel.relativedelta(hour=info['rec_end'].hour)
        else:
            end_time = info['date'] + drel.relativedelta(hours=4)
    
        e.add('dtend', end_time.replace(tzinfo=(pytz.timezone('US/Eastern'))))
    
        organizer = cal.vCalAddress('MAILTO:knoxgearhead@knoxgearhead.com')
        organizer.params['cn'] = cal.vText('KnoxGearhead')
        e.add('organizer', organizer)
        e['uid'] = str(info['date']) + '/' + info['title']
        e['location'] = cal.vText(info['address'])
        e['description'] = cal.vText('http://www.knoxgearhead.com \nWebsite: {}\n Location: {}\n\n{}'.format(info['website'], info['location'], txt.split('---')[-1]))
    
        c.add_component(e)


with open('calendars/carshows.ics', 'w') as f:
    f.write(c.to_ical())
    
    
# DRAG RACES
c = cal.Calendar()

c.add('prodid', '-//KnoxGearhead Carshow Calendar//knoxgearhead.com//')
c.add('version', '0.0.1')

for f in glob('_posts/*.markdown'):
    
    with open(f, 'r') as txtfile:
        txt = txtfile.read()
    info = yaml.load(txt.split('---')[1])
    
    if "drag" in info['categories']:
    
        e = cal.Event()
    
    
        e.add('summary', info['title'])
        e.add('dtstart', info['date'].replace(tzinfo=pytz.timezone('US/Eastern')))
    
        if 'end_date' in info:
            end_time = info['end_date']
        elif 'rec_end' in info:
            end_time = info['date'] + drel.relativedelta(hour=info['rec_end'].hour)
        else:
            end_time = info['date'] + drel.relativedelta(hours=4)
    
        e.add('dtend', end_time.replace(tzinfo=(pytz.timezone('US/Eastern'))))
    
        organizer = cal.vCalAddress('MAILTO:knoxgearhead@knoxgearhead.com')
        organizer.params['cn'] = cal.vText('KnoxGearhead')
        e.add('organizer', organizer)
        e['uid'] = str(info['date']) + '/' + info['title']
        e['location'] = cal.vText(info['address'])
        e['description'] = cal.vText('http://www.knoxgearhead.com \nWebsite: {}\n Location: {}\n\n{}'.format(info['website'], info['location'], txt.split('---')[-1]))
    
        c.add_component(e)


with open('calendars/drag_races.ics', 'w') as f:
    f.write(c.to_ical())