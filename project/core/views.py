from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import LogAnalyzerForm

def log_analyzer(request):
    if request.method == 'POST':
        form = LogAnalyzerForm(request.POST)
        if form.is_valid():
            # Lógica de análisis de logs aquí
            results = form.analyze_log()
            return render(request, 'index.html', {'form': form, 'results': results})
    else:
        form = LogAnalyzerForm()

    return render(request, 'index.html', {'form': form})
