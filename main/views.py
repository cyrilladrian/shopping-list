from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Cyrill Adrian Wicaksono',
        'class': 'PBP KI'
    }

    return render(request, 'main.html', context)
# Create your views here.
