from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='student1@example.com', name='Student One', age=16),
            User(email='student2@example.com', name='Student Two', age=17),
            User(email='student3@example.com', name='Student Three', age=15),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Team Alpha')
        team2 = Team(name='Team Beta')
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, date=datetime.now().date()),
            Activity(user=users[1], type='Cycling', duration=45, date=datetime.now().date()),
            Activity(user=users[2], type='Swimming', duration=60, date=datetime.now().date()),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, points=100),
            Leaderboard(team=team2, points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Morning Run', description='A quick morning run', duration=30),
            Workout(name='Evening Yoga', description='Relaxing yoga session', duration=60),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
