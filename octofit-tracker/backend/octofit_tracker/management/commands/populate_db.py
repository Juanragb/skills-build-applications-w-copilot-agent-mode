from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many([
            {"email": "thundergod@mhigh.edu", "name": "Thor", "password": "password123"},
            {"email": "metalgeek@mhigh.edu", "name": "Tony Stark", "password": "password123"},
            {"email": "zerocool@mhigh.edu", "name": "Steve Rogers", "password": "password123"},
        ])

        db.teams.insert_one({"name": "Avengers", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu", "zerocool@mhigh.edu"]})

        db.activity.insert_many([
            {"user": "thundergod@mhigh.edu", "type": "Cycling", "duration": 60, "date": "2025-04-08"},
            {"user": "metalgeek@mhigh.edu", "type": "Running", "duration": 45, "date": "2025-04-08"},
        ])

        db.leaderboard.insert_one({"team": "Avengers", "points": 100})

        db.workouts.insert_many([
            {"name": "Cycling Training", "description": "Cycling for endurance"},
            {"name": "Running Training", "description": "Running for stamina"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
