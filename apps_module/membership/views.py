from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
# Create your views here.

from .models import Member
from .models import Attendance

def member_data(request):
    url = ""
    m_list = []
    member_obj = Member.objects.all()
    for m in member_obj:
        m_data = {
            'member_id': m.member_id,
            'first_name': m.first_name,
            'middle_name': m.middle_name,
            'last_name': m.last_name,
            'gender': m.gender,
            'location': m.location,
            'phone_number_1': m.phone_number_1,
            'phone_number_2': m.phone_number_2,
            'visitor': m.visitor,
            'date_added': m.date_added,
            'date_updated':  m.date_updated,
        }

        m_list.append(m_data)
    # data = m

    result = {
        'count': len(m_list),
        'status_code': 200,
        'data': m_list
    }

    return JsonResponse(result)




