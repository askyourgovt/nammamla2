from __future__ import absolute_import
import os
import re
from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
from datetime import datetime
from models import Representative, Session

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
            rep = Representative.objects.get(key=rep_key)
            session = Session.objects.get(id=1)
            session_date = row[1]

            
            attendance = row[2]
            if attendance == 'p':
                attendance = 'Present'
            elif attendance == 'a':
                attendance = 'Absent'
            else:
                attendance = 'N.A'



print "I am done"