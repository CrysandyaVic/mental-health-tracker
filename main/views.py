from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306165622',
        'name': 'Crysandya Vic Rajendra',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
# Create your views here.
