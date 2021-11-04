from datetime import datetime
import dateutil.relativedelta as drel
from glob import glob
import os
import yaml

# Ensure _archive directory exists
os.makedirs("_archive", exist_ok=True)

# Iterate over all events in the events directory
for eventfile in glob("_posts/*.markdown"):

    # Load the event file
    with open(eventfile, "r") as txt:
        content = txt.read()

    # Load the YAML frontmatter
    info = yaml.safe_load(content.split("---")[1])

    # Get the date of the event
    if "end_date" in info:
        d = info["end_date"]
    else:
        d = info["date"]

    # Move the event to the archive directory if occured greater than a day ago
    if datetime.now() > (d + drel.relativedelta(days=1)):
        print("Archived: {}".format(eventfile))
        os.rename(eventfile, eventfile.replace("_posts", "_archive"))
