from datetime import datetime
import dateutil.relativedelta as drel
from glob import glob
import os
import yaml


for eventfile in glob("_posts/*.markdown"):

    with open(eventfile, 'r') as txt:
        content = txt.read()

    info = yaml.load(content.split("---")[1])

    if 'end_date' in info:
        d = info['end_date']
    else:
        d = info['date']

    if datetime.now() > ( d + drel.relativedelta(days=1) ):
        print("Archived: {}".format(eventfile))
        os.rename(eventfile, eventfile.replace("_posts", "_archive"))
