import dateutil.relativedelta as drel
import icalendar as cal
from glob import glob
import pytz
import yaml


# Build the calendar for all events
c = cal.Calendar()
c.add("prodid", "-//KnoxGearhead Calendar//knoxgearhead.com//")
c.add("version", "0.0.1")

# Build the calendar for drag racing events
c_drag = cal.Calendar()
c_drag.add(
    "prodid", "-//KnoxGearhead Carshow and Cruise-In Calendar//knoxgearhead.com//"
)
c_drag.add("version", "0.0.1")

# Build the calendar for car shows and cruise ins
c_showcruise = cal.Calendar()
c_showcruise.add("prodid", "-//KnoxGearhead Drag Racing Calendar//knoxgearhead.com//")
c_showcruise.add("version", "0.0.1")

# Iterate over all events
for f in glob("_posts/*.markdown"):
    # Create a new event
    e = cal.Event()

    # Load the event data
    with open(f, "r") as txtfile:
        txt = txtfile.read()
    info = yaml.safe_load(txt.split("---")[1])

    # Add the event data
    e.add("summary", info["title"])
    e.add("dtstart", info["date"].replace(tzinfo=pytz.timezone("US/Eastern")))

    # Calculate the end date
    if "end_date" in info:
        end_time = info["end_date"]
    elif "rec_end" in info:
        end_time = info["date"] + drel.relativedelta(hour=info["rec_end"].hour)
    else:
        end_time = info["date"] + drel.relativedelta(hours=4)
    e.add("dtend", end_time.replace(tzinfo=(pytz.timezone("US/Eastern"))))

    # Add metadata to the event
    organizer = cal.vCalAddress("MAILTO:knoxgearhead@knoxgearhead.com")
    organizer.params["cn"] = cal.vText("KnoxGearhead")
    e.add("organizer", organizer)
    e["uid"] = str(info["date"]) + "/" + info["title"]
    e["location"] = cal.vText(info["address"])
    e["description"] = cal.vText(
        "http://www.knoxgearhead.com \nWebsite: {}\n Location: {}\n\n{}".format(
            info["website"], info["location"], txt.split("---")[-1]
        )
    )

    # Add the event to the calendar(s)
    c.add_component(e)
    if "drag" in info["categories"]:
        c_drag.add_component(e)
    elif "carshow" in info["categories"] or "cruisein" in info["categories"]:
        c_showcruise.add_component(e)

# Write the calendars to files
with open("calendars/all_events.ics", "wb") as f:
    f.write(c.to_ical())
with open("calendars/drag_races.ics", "wb") as f:
    f.write(c_drag.to_ical())
with open("calendars/carshows.ics", "wb") as f:
    f.write(c_showcruise.to_ical())

exit()
# CAR SHOWS
c = cal.Calendar()

c.add("prodid", "-//KnoxGearhead Carshow Calendar//knoxgearhead.com//")
c.add("version", "0.0.1")

for f in glob("_posts/*.markdown"):

    with open(f, "r") as txtfile:
        txt = txtfile.read()
    info = yaml.safe_load(txt.split("---")[1])

    if "carshow" in info["categories"] or "cruisein" in info["categories"]:

        e = cal.Event()

        e.add("summary", info["title"])
        e.add("dtstart", info["date"].replace(tzinfo=pytz.timezone("US/Eastern")))

        if "end_date" in info:
            end_time = info["end_date"]
        elif "rec_end" in info:
            end_time = info["date"] + drel.relativedelta(hour=info["rec_end"].hour)
        else:
            end_time = info["date"] + drel.relativedelta(hours=4)

        e.add("dtend", end_time.replace(tzinfo=(pytz.timezone("US/Eastern"))))

        organizer = cal.vCalAddress("MAILTO:knoxgearhead@knoxgearhead.com")
        organizer.params["cn"] = cal.vText("KnoxGearhead")
        e.add("organizer", organizer)
        e["uid"] = str(info["date"]) + "/" + info["title"]
        e["location"] = cal.vText(info["address"])
        e["description"] = cal.vText(
            "http://www.knoxgearhead.com \nWebsite: {}\n Location: {}\n\n{}".format(
                info["website"], info["location"], txt.split("---")[-1]
            )
        )

        c.add_component(e)


with open("calendars/carshows.ics", "wb") as f:
    f.write(c.to_ical())


# DRAG RACES
c = cal.Calendar()

c.add("prodid", "-//KnoxGearhead Carshow Calendar//knoxgearhead.com//")
c.add("version", "0.0.1")

for f in glob("_posts/*.markdown"):

    with open(f, "r") as txtfile:
        txt = txtfile.read()
    info = yaml.safe_load(txt.split("---")[1])

    if "drag" in info["categories"]:

        e = cal.Event()

        e.add("summary", info["title"])
        e.add("dtstart", info["date"].replace(tzinfo=pytz.timezone("US/Eastern")))

        if "end_date" in info:
            end_time = info["end_date"]
        elif "rec_end" in info:
            end_time = info["date"] + drel.relativedelta(hour=info["rec_end"].hour)
        else:
            end_time = info["date"] + drel.relativedelta(hours=4)

        e.add("dtend", end_time.replace(tzinfo=(pytz.timezone("US/Eastern"))))

        organizer = cal.vCalAddress("MAILTO:knoxgearhead@knoxgearhead.com")
        organizer.params["cn"] = cal.vText("KnoxGearhead")
        e.add("organizer", organizer)
        e["uid"] = str(info["date"]) + "/" + info["title"]
        e["location"] = cal.vText(info["address"])
        e["description"] = cal.vText(
            "http://www.knoxgearhead.com \nWebsite: {}\n Location: {}\n\n{}".format(
                info["website"], info["location"], txt.split("---")[-1]
            )
        )

        c.add_component(e)


with open("calendars/drag_races.ics", "wb") as f:
    f.write(c.to_ical())
