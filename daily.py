import random
from datetime import datetime

import jinja2
from granary import microformats2, rss
import os

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = "."
# OUTPUT_DIR = "/var/www/jamesg.blog/oblique-strategies/"

with open(os.path.join(FILE_DIR, "strategies.txt"), "r") as f:
    strategies = f.read().splitlines()

with open(os.path.join(FILE_DIR, "template.html"), "r") as f:
    template_file = f.read()

template = jinja2.Template(template_file)

strategy = "Intentions -credibility of -nobility of -humility of" # random.sample(strategies, 1)[0]
if strategy.count(" -") > 1:
    strategy = strategy.replace(" -", "<br> -")

rendered_template = template.render(
    strategy=strategy,
    date=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
)

with open(os.path.join(OUTPUT_DIR, "index.html"), "w") as f:
    f.write(rendered_template)

with open(os.path.join(FILE_DIR, "pwa.html"), "r") as f:
    template_file = f.read()

template = jinja2.Template(template_file)

rendered_template = template.render(
    strategy=strategy,
    date=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
)

with open(os.path.join(OUTPUT_DIR, "pwa_out.html"), "w") as f:
    f.write(rendered_template)

rss = rss.from_activities(
    microformats2.html_to_activities(rendered_template),
    feed_url="https://jamesg.blog/oblique-strategies",
    title="Oblique Strategies RSS",
)

with open(os.path.join(OUTPUT_DIR, "rss.xml"), "w") as f:
    f.write(rss)
