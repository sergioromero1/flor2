from django.shortcuts import render

# Create your views here.
def load_index(request):
    return render(request,"orders/index.html")

def load_error_404(request, exception):
    return render(request,"orders/error-404.html",status=404)