import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

# Create your views here.
@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template = "contact_upload.html"

    prompt = {
        'order': 'Follw ordering guidelines per google sheet'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=',', quotechar=""):
        _, created = Class.objects.update_or_create(
            prefix = col[0],
            ID = col[1],
            name = col[2],
            description = col[3],
            HI = col[4],
            CI = col[5],
            DI = col[6],
            fall = col[7],
            spring = col[8],
            summer = col[9],
            pathway = col[10]
        )
    
    
    context = {}
    return render(request, template, context)