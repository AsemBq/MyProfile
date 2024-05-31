from django.shortcuts import render
from . import models


def home(request):
    header = models.Header.objects.last()
    aboutMe = models.AboutMe.objects.last()
    socialMedia = models.SocialMedia.objects.last()
    technologys = models.Technology.objects.all()
    projects=models.Project.objects.all()
    tools = models.Tools.objects.all()
    otherSkills = models.OtherSkills.objects.all()

    if request.method=="POST":
        name=request.POST.get('fullName')
        email=request.POST.get('email')
        message=request.POST.get('message')
        models.Ticket.objects.create(name=name,email=email,message=message)
    return render(request, 'home/index.html', context={'header': header, 'aboutMe': aboutMe, 'socialMedia': socialMedia,
                                                       'technologys': technologys, 'tools': tools,
                                                       'otherSkills': otherSkills,'projects':projects})
