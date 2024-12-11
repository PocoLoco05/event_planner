
from django.shortcuts import render

def index(request):
    return render(request, 'events/index.html' )


from django.shortcuts import render, redirect
from .forms import EventForm

def event_create_view(request):
    if request.method == 'POST' and 'theme' in request.POST:
        theme = request.POST.get('theme', 'light')
        language = request.POST.get('language', 'en')
        response = redirect('event-create')
        response.set_cookie('theme', theme, max_age=365 * 24 * 60 * 60)
        response.set_cookie('language', language, max_age=365 * 24 * 60 * 60)
        return response

    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'en')

    if request.method == 'POST' and 'event' in request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'events/index.html', {
        'form': form,
        'theme': theme,
        'language': language,
    })

