from __future__ import absolute_import
import os
import re
from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
from datetime import datetime
from models import Representative, Session, Constituency

import csv
from datetime import datetime, date, time
from time import gmtime, strftime
import sys
import time
session = Session.objects.get(id=1)

with open(file_name) as as_result_file:
        reader = csv.reader(as_result_file,delimiter=',',quotechar='"')
        for row in reader:
            rep_key = row[0]
            constituency_key = row[4]
            role_key = row[1]
            party_key = row[5]
            ec_affidavits = row[6]
            start = row[2]
            end = row[3]

            rep = Representative.objects.get(key=rep_key)
            constituency = Constituency.objects.get(key=constituency_key)

            



print "I am done"