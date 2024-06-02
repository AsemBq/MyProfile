from django.shortcuts import render
from . import models
import telebot



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
        bot = telebot.TeleBot('7008384349:AAHiFpu3vwi310YOQrTQBMlsEf34cjVoQ48')
        bot.send_message(149539081, 'You have New Ticket')
    return render(request, 'home/index.html', context={'header': header, 'aboutMe': aboutMe, 'socialMedia': socialMedia,
                                                       'technologys': technologys, 'tools': tools,
                                                       'otherSkills': otherSkills,'projects':projects})
