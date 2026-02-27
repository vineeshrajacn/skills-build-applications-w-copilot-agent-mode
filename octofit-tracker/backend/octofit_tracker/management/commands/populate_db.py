from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='cap@marvel.com', name='Captain America', team='marvel'),
            User(email='thor@marvel.com', name='Thor', team='marvel'),
            User(email='hulk@marvel.com', name='Hulk', team='marvel'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
            User(email='flash@dc.com', name='Flash', team='dc'),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-02-27')
        Activity.objects.create(user='Superman', type='swim', duration=45, date='2026-02-27')
        Activity.objects.create(user='Batman', type='cycle', duration=60, date='2026-02-27')
        Activity.objects.create(user='Thor', type='lift', duration=50, date='2026-02-27')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=200)
        Leaderboard.objects.create(team='dc', points=180)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='medium')
        Workout.objects.create(name='Deadlift', description='Do deadlifts', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
