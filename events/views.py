from django.shortcuts import render

def index():
        return render(request, "templates/admin/events/change_list.html")