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

    with open(eventfile, 'r') as txt:
        content = txt.read()

    info = yaml.load(content.split("---")[1])

    # start = dp.parse(info['rec_start'])
    # end = dp.parse(info['rec_end'])

    start = info['rec_start']
    end = info['rec_end']

    if "week" in info['rec_period']:
        rr = dr.rrule(dr.WEEKLY,byweekday=DAYS[info['rec_day']])
    else:
        print "Error: this recurring type not supported"

    dates = rr.between(start, end)

    for d in dates:
        formatted_date = str(d)
        c = content.replace("DATEc", formatted_date)
        filename = "_posts/" + formatted_date.split(" ")[0] + '-' + eventfile.split("/")[-1]
        with open(filename, "w") as outfile:
            outfile.write(c)