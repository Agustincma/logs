from django import forms

class LogAnalyzerForm(forms.Form):
    datetime = forms.CharField(label='Hora (HH:MM:SS)', max_length=20, required=False)
    log_file = forms.FileField(label='Cargar Log', required=False)
    reset = forms.BooleanField(label='Resetear', required=False)
    keywords = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple, required=False)

    def analyze_log(self):
        # Lógica de análisis de logs aquí
        results = []
        # ...
        return results
