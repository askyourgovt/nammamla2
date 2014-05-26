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
        file_name ='/home/thej/Desktop/rep_role.csv'
        first_row = True
        with open(file_name) as as_result_file:
                reader = csv.reader(as_result_file,delimiter=',',quotechar='"')
                for row in reader:
                    if first_row:
                        first_row = False
                        continue
                    rep_key = row[0]
                    print rep_key
                    role_key = row[1]
                    print str(row[2])
                    start = datetime.strptime(str(row[2]), "%Y-%m-%d") 
                    end = None
                    constituency_key = row[4]
                    party_key = row[5]
                    ec_affidavits = row[6]

                    rep = Representative.objects.get(key=rep_key)
                    constituency = Constituency.objects.get(key=constituency_key)
                    role = Role.objects.get(key=role_key)
                    party = Party.objects.get(key=str(party_key).lower())
                    b2 = RepRole(representative=rep,constituency=constituency,party=party,has_ec_affidavit=ec_affidavits,role=role, start=start, end=end,assembly=assembly)
                    b2.save()            



print "I am done"