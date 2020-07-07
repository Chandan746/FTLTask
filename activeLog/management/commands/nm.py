from django.core.management.base import BaseCommand, CommandError
from activeLog.models import Profile,activity_periods
from django.contrib.auth.models import User
import datetime
class Command(BaseCommand):
    help = 'enter activity periods'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=str, help='Username')
        parser.add_argument("start_time",help="start_time")
        parser.add_argument("end_time",help="end_time") 
    def handle(self, *args,**kwargs):
        user_id = kwargs['user_id']
        start_time = kwargs['start_time']
        start_time = datetime.datetime.strptime(start_time, "%b-%d-%Y-%I:%M-%p")
        end_time = kwargs['end_time']
        end_time = datetime.datetime.strptime(end_time, "%b-%d-%Y-%I:%M-%p")
        if user_id:
            # print(user_id,"++",start_time,'++',end_time)
            try:
                user = User.objects.get(id=int(user_id))
                # print(user)
                profile = Profile.objects.get(user = user)
                # print(profile)
            except:
                raise CommandError('User does not exist')
            if start_time and end_time :
                m1 = activity_periods.objects.create(start_time=start_time,end_time=end_time)
                m1.save()
                profile.activity_periods.add(m1)
                profile.save()

                self.stdout.write('updated')
