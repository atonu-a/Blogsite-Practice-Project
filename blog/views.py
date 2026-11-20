from django.shortcuts import render


def post_list_view(request):
    try:
        a = 1/0
        print(a)
    
    except Exception as e :
        return render(request, 'error.html', {'error':e})
# Create your views here.
