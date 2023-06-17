from django.shortcuts import render

def custom_404_view(request,exception):
    return render(request, '404-min.html', status=404)

def custom_500_view(request):
    return render(request, '404-min.html', status=404)

