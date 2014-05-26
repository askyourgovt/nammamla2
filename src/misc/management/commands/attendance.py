from __future__ import absolute_import
import os
import re
from django.core.management.base import BaseCommand, CommandError

from datetime import datetime
from misc.models import Representative, Role, Party, Constituency, Assembly, Session, RepRole, Attendance, Department, Question, State

import csv
from datetime import datetime, date, time
from time import gmtime, strftime
import sys
import time

class Command(BaseCommand):
    args = '<file_name> ...'
    help = 'script to import keys from csv files'

    def handle(self, *args, **options):
        session = Session.objects.get(id=1)
        assembly = Assembly.objects.get(id=1)
        file_name ='/home/thej/Desktop/attendance.csv'
        first_row = True
        with open(file_name) as as_result_file:
                reader = csv.reader(as_result_file,delimiter=',',quotechar='"')
                for row in reader:
                    if first_row:
                        first_row = False
                        continue

                    rep_key = row[0]
                    rep = Representative.objects.get(key=rep_key)
                    #just make sure end is Not null
                    rep_role = RepRole.objects.get(representative=rep, role__key='mla')
                    session_date = datetime.strptime(str(row[1]), "%Y-%m-%d") 

                    
                    attendance = row[2]
                    if attendance == 'p':
                        attendance = 'Present'
                    elif attendance == 'a':
                        attendance = 'Absent'
                    else:
                        attendance = 'N.A'

                    b2 = Attendance(representative=rep, session=session, date=session_date, repRole=rep_role, attendance=attendance)
                    b2.save()            


        print "I am done"