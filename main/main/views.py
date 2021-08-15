import calendar
from datetime import date, datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from stuff.forms import UserUploadForm
from stuff.models import (RandomCombination, UserProgress, UserUpload,
                          create_combi)


def index(request):
    form = UserUploadForm()
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

    if request.user and request.user.is_authenticated:
        month_year = date.today().strftime('%m%Y')
        q = UserProgress.objects.filter(month_year=month_year)

        if len(q):
            progress = set(q[0].days.split(';'))
        else:
            progress = set()
    else:
        progress = set()

    cal = calendar.HTMLCalendar().formatmonth(today.year, today.month)
    cal = cal.split('<tr>')[3:]
    month = []
    
    for week in cal:
        week = week.split('</td>')
        month.append([])
        
        for day in range(7):
            day = week[day].split('>')[1]

            if day == '&nbsp;':
                month[-1].append('')
            elif day not in progress:
                month[-1].append(day)
            else:
                month[-1].append(f'<span class="text-success">{day}</span>')
            
    uploads = UserUpload.objects.filter(created=today)
    return render(request, 'index.html', {
        'month_and_year': month_and_year,
        'month': month,
        'combi1': combi1,
        'combi2': combi2,
        'time_left': time_left,
        'form': form,
        'uploads': uploads,
    })


@login_required()
def upload_creation(request):
    if request.method == 'POST':
        form = UserUploadForm(request.POST or None, files=request.FILES or None)
        # print(request.FILES, form.is_valid(), form.errors)
        if ('story' in request.POST and request.POST['story'] or request.FILES) and form.is_valid():
            print('good')
            upload = form.save(commit=False)
            upload.author = request.user
            upload.save()
            return redirect('done_today')

    return redirect('index')


@login_required()
def done_today(request):
    today = date.today()
    month_year = today.strftime('%m%Y')
    q = UserProgress.objects.filter(month_year=month_year)
    day = f'{today.day}'

    if len(q) == 0:
        progress = UserProgress.objects.create(user=request.user, month_year=month_year, days=day)
    else:
        progress = q[0]

        if progress.days[-len(day):] != day:
            progress.days += f';{day}'
    
    progress.save()

    return redirect('index')
