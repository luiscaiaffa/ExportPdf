from django.shortcuts import render
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

from weasyprint import HTML, CSS

class ExportPdf(View):
	def get(self, request):
		context = {}
		html_string = render_to_string('base_pdf.html', context)

		html = HTML(string=html_string, base_url=request.build_absolute_uri())
		html.write_pdf(target='/tmp/mypdf.pdf',stylesheets=[CSS(settings.STATIC_ROOT +  '/css/main.css')]);

		fs = FileSystemStorage('/tmp')
		with fs.open('mypdf.pdf') as pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
			return response

		return response
		return render(request, 'pdf.html', context)
