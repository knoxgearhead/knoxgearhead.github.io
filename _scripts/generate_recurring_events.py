import dateutil.rrule as dr
import dateutil.parser as dp
import dateutil.relativedelta as drel
from glob import glob
import yaml

# Map days of the week to their dateutil.rrule.weekday values
DAYS = {
    "monday": dr.MO,
    "tuesday": dr.TU,
    "wednesday": dr.WE,
    "thursday": dr.TH,
    "friday": dr.FR,
    "saturday": dr.SA,
    "sunday": dr.SU,
}

# Iterate over all recurring events
for eventfile in glob("_recurring/*.markdown"):
    print("Event: {}".format(eventfile))

    # Load the event
    with open(eventfile, "r") as txt:
        content = txt.read()
    info = yaml.safe_load(content.split("---")[1])

    # Get the start and end dates
    start = info["rec_start"]
    end = info["rec_end"]

    # Handle weekly events
    if "week" in info["rec_period"]:
        rr = dr.rrule(dr.WEEKLY, byweekday=DAYS[info["rec_day"]], dtstart=start)
    # Handle monthly events
    elif "month" in info["rec_period"]:
        rr = dr.rrule(
            dr.MONTHLY,
            byweekday=DAYS[info["rec_day"]](info["rec_instance"]),
            dtstart=start,
        )
    # Handle other events
    else:
        print("Error: this recurring type not supported")

    # Calculate all dates
    dates = rr.between(start, end)

    # Remove every other date if biweekly or bimonthly
    if "bi" in info["rec_period"]:
        dates = dates[::2]

    # Find dates to skip
    if "rec_skip" in info:
        skip_dates = info["rec_skip"]
    else:
        skip_dates = []

    # Iterate over all dates
    for d in dates:
        d_date = d.date() + drel.relativedelta(hour=start.hour)

        # Create event if not in skip list
        if not (d_date in skip_dates):
            print("Date: {}".format(d))
            formatted_date = str(d)
            c = content.replace("DATE", formatted_date)
            filename = (
                "_posts/"
                + formatted_date.split(" ")[0]
                + "-"
                + eventfile.split("/")[-1]
            )
            with open(filename, "w") as outfile:
                outfile.write(c)
