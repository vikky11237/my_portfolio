from django.core.management.base import BaseCommand
from core.models import Skill, Project
import requests

class Command(BaseCommand):
    help = 'Loads initial skill data and GitHub projects'

    def handle(self, *args, **kwargs):
        skills_data = [
            {"name": "AWS Glue", "proficiency": 90},
            {"name": "AWS Lambda", "proficiency": 85},
            {"name": "Apache Spark", "proficiency": 90},
            {"name": "Python", "proficiency": 85},
            {"name": "AWS Redshift", "proficiency": 85},
            {"name": "Data Pipeline Design", "proficiency": 90},
            {"name": "ETL Development", "proficiency": 90},
            {"name": "AWS EMR", "proficiency": 85},
            {"name": "Terraform", "proficiency": 80},
            {"name": "Apache Kafka", "proficiency": 80},
        ]

        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"proficiency": skill_data["proficiency"]}
            )
        
        # Fetch GitHub projects
        github_username = "vikky11237"
        api_url = f"https://api.github.com/users/{github_username}/repos"
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                repos = response.json()
                for repo in repos:
                    if not repo['fork']:  # Only include non-forked repositories
                        Project.objects.get_or_create(
                            title=repo['name'],
                            defaults={
                                'description': repo['description'] or 'No description available',
                                'tech_stack': repo['language'] or 'Not specified',
                                'github_link': repo['html_url'],
                                'live_demo_link': repo.get('homepage') or repo['html_url']  # Use GitHub URL as fallback
                            }
                        )
                self.stdout.write(self.style.SUCCESS('Successfully loaded GitHub projects'))
            else:
                self.stdout.write(self.style.WARNING('Failed to fetch GitHub projects'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error fetching GitHub projects: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded all initial data'))