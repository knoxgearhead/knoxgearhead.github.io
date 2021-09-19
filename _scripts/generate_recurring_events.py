import dateutil.rrule as dr
import dateutil.parser as dp
import dateutil.relativedelta as drel
from glob import glob
import yaml

DAYS = {"monday": dr.MO,
        "tuesday":dr.TU,
        "wednesday":dr.WE,
        "thursday":dr.TH,
        "friday":dr.FR,
        "saturday":dr.SA,
        "sunday":dr.SU}


for eventfile in glob("_recurring/*.markdown"):
    print("Event: {}".format(eventfile))

    with open(eventfile, 'r') as txt:
        content = txt.read()

    info = yaml.load(content.split("---")[1])

    # start = dp.parse(info['rec_start'])
    # end = dp.parse(info['rec_end'])

    start = info['rec_start']
    end = info['rec_end']

    if "week" in info['rec_period']:
        rr = dr.rrule(dr.WEEKLY,byweekday=DAYS[info['rec_day']],dtstart=start)

    elif "month" in info['rec_period']:
        rr = dr.rrule(dr.MONTHLY, byweekday=DAYS[info['rec_day']](info['rec_instance']), dtstart=start)

    else:
        print("Error: this recurring type not supported")

    print(start)
    dates = rr.between(start, end)

    print(dates)

    if 'bi' in info['rec_period']:
        dates = dates[::2]


    if 'rec_skip' in info:
        skip_dates = info['rec_skip']
    else:
        skip_dates = []

    for d in dates:
        d_date = d.date() +  drel.relativedelta(hour=start.hour)

        if not( d_date in skip_dates):
            print("Date: {}".format(d))
            formatted_date = str(d)
            c = content.replace("DATE", formatted_date)
            filename = "_posts/" + formatted_date.split(" ")[0] + '-' + eventfile.split("/")[-1]
            with open(filename, "w") as outfile:
                outfile.write(c)
