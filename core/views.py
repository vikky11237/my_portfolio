from django.shortcuts import render
from .models import Project, Skill, Contact

def home(request):
    return render(request, 'core/home.html')

def about(request):
    context = {
        'cloud_skills': ['AWS', 'Lambda', 'Glue', 'EventBridge', 'S3', 'Redshift', 'EMR', 'Athena'],
        'big_data_skills': ['Hadoop', 'PySpark', 'Kafka', 'Spark Streaming', 'Databricks', 'Data Engineering', 'ETL', 'Data Architecture'],
        'programming_skills': ['Python', 'Django', 'Flask', 'React', 'Terraform', 'DBT', 'Unix Shell', 'GenAI'],
        'database_skills': ['MongoDB', 'MySQL', 'SQLite', 'SQL', 'Power BI', 'Slate', 'Palantir Foundry'],
        'core_skills': ['System Design', 'Performance Tuning', 'Automation', 'Big Data']
    }
    return render(request, 'core/about.html', context)

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'core/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('contact_success')
    return render(request, 'core/contact.html')
