from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import requests

# Create your views here.

from .models import Member
from .models import Attendance


def member_data(request):
    url = ""
    m_list = []
    member_obj = Member.objects.all()
    for m in member_obj:
        m_data = {
            "member_id": m.member_id,
            "first_name": m.first_name,
            "middle_name": m.middle_name,
            "last_name": m.last_name,
            "gender": m.gender,
            "location": m.location,
            "phone_number_1": m.phone_number_1,
            "phone_number_2": m.phone_number_2,
            "visitor": m.visitor,
            "date_added": m.date_added,
            "date_updated": m.date_updated,
        }

        m_list.append(m_data)
    # data = m

    result = {"count": len(m_list), "status_code": 200, "data": m_list}

    return JsonResponse(result)


def save_membership_data(request):
    url = "http://gecapp.herokuapp.com/member_data"
    # url = "http://127.0.0.1:9000/member_data"
    # url_data = urlopen(url)
    req = requests.get(url)
    req_data = req.json()

    print(req_data["data"])
    # m_list = []
    # member_obj = Member.objects.all()
    count = 0
    try:
        for m in req_data["data"]:
            print(m["first_name"])
            obj = Member.objects.create(
                member_id=m["member_id"],
                first_name=m["first_name"],
                middle_name=m["middle_name"],
                last_name=m["last_name"],
                gender=m["gender"],
                location=m["location"],
                phone_number_1=m["phone_number_1"],
                phone_number_2=m["phone_number_2"],
                visitor=m["visitor"],
            )
            count += 1
        print(count)
    except Exception as e:
        print(e)
        raise e

    result = {"count": count, "status_code": 200, "message": f"{count} members saved"}

    return JsonResponse(result)


def attendance_data(request):
    url = ""
    a_list = []
    attendace_obj = Attendance.objects.all()
    for a in attendace_obj:
        a_data = {
            "date": a.date,
            "member_id": a.member.member_id,
            "present": a.present,
            "child": a.child,
            "temp_tens": a.temp_tens,
            "temp_ones": a.temp_ones,
            "temp_decimals": a.temp_decimals,
            "temperature": a.temperature,
            "service": a.service,
            "date_added": a.date_added,
            "date_updated": a.date_updated,
        }

        a_list.append(a_data)
    # data = m

    result = {"count": len(a_list), "status_code": 200, "data": a_list}

    return JsonResponse(result)


def save_attendance_data(request):
    # url = "http://gecapp.herokuapp.com/attendance_data"
    url = "http://127.0.0.1:9000/attendance_data"
    # url_data = urlopen(url)
    req = requests.get(url)
    req_data = req.json()

    print(req_data["data"])

    count = 0

    try:
        for a in req_data["data"]:
            print(a["date"])
            if Member.objects.filter(member_id=a["member_id"]).exists():
                obj = Attendance.objects.create(
                    date=a["date"],
                    member_id=a["member_id"],
                    present=a["present"],
                    child=a["child"],
                    temperature=a["temperature"],
                    service=a["service"],
                    date_added=a["date_added"],
                    date_updated=a["date_updated"],
                )
            count += 1
        print(count)
    except Exception as e:
        print(e)
        raise e

    result = {
        "count": count,
        "status_code": 200,
        "message": f"{count} Attendances saved"}

    return JsonResponse(result)


# def profile_data(request):
#     url = ""
#     p_list = []
#     profile_obj = profile.objects.all()
#     for p in profile_obj:
#         p_data = {
#             'passport pic': p.photo,
#             'member': p.member,
#             'present': p.present,
#             'child': p.child,
#             'location': p.location,
#             'contact': p.contact_ones,
#             'date_updated':  a.date_updated,
#         }

#         p_list.append(p_data)
#     # data = m

#     result = {
#         'count': len(p_list),
#         'status_code': 200,
#         'data': p_list
#     }

#     return JsonResponse(result)
