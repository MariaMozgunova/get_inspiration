import calendar
from datetime import date, datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from stuff.forms import UserUploadForm
from stuff.models import RandomCombination, UserUpload, create_combi


def index(request):
    form = UserUpload()
    today = date.today()
    now = datetime.now()
    time_left = 24 * 60 * 60 - now.hour * 60 * 60 - now.minute * 60 - now.second
    hour = time_left // 3600
    minute = (time_left - hour * 3600) // 60
    second = (time_left - hour * 3600 - minute * 60)
    time_left = f'{hour:02}:{minute:02}:{second:02}'
    month_and_year = today.strftime('%B %Y')
    today_combi =  RandomCombination.objects.filter(created=today)

    if len(today_combi) == 0:
        combi1 = create_combi()
        combi2 = create_combi()
    else:
        combi1, combi2 = today_combi

    cal = calendar.HTMLCalendar().formatmonth(today.year, today.month)
    cal = cal.split('<tr>')[3:]
    month = []
    
    for week in cal:
        week = week.split('</td>')
        month.append([])
        
        for day in range(7):
            day = week[day].split('>')[1]
            month[-1].append('' if day == '&nbsp;' else day)
            
    # make calendar
    # get today`s combinations
    # form for upload
    # current time
    # uploads of other users
    return render(request, 'index.html', {
        'month_and_year': month_and_year,
        'month': month,
        'combi1': combi1,
        'combi2': combi2,
        'time_left': time_left,
        'form': form,
    })

@login_required()
def upload_creation(request):
    if request.method == 'POST':
        form = UserUploadForm(request.POST or None, files=request.FILES or None)
        
        if form.is_valid():
            upload = form.save(commit=False)
            upload.author = request.user
            upload.save()

    return redirect('index')
