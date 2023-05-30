from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MappingPoint_E, MappingPoint_I, ContactForm_E, ContactForm_I

import json
# Create your views here.

def index(request):
    return render(request, 'index.html')

def save_marker_data_E(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            latitude = data.get("latitude")
            longitude = data.get("longitude")
            name = data.get("name")

            # 데이터 처리 로직 수행
            try:
                # MappingPoint 모델을 이용하여 데이터 저장
                mapping_point = MappingPoint_E(latitude=latitude, longitude=longitude, name=name)
                mapping_point.save()

                # 응답 데이터 생성
                response_data = {
                    "message": "Data saved successfully."
                }
                return JsonResponse(response_data)
            
            except Exception as e:
                # 저장 중에 예외가 발생한 경우 처리
                response_data = {
                    "error": str(e)
                }
                return JsonResponse(response_data, status=500)

        except json.JSONDecodeError as e:
            # JSON 디코딩 중에 예외가 발생한 경우 처리
            response_data = {
                "error": "Invalid JSON format."
            }
            return JsonResponse(response_data, status=400)

    # POST 요청이 아닌 경우에 대한 처리
    return JsonResponse({"error": "Invalid request."})

def get_marker_data_E(request):
    if request.method == "GET":
        try:
            # MappingPoint 모델에서 데이터 조회
            marker_data = MappingPoint_E.objects.all().values()

            # 응답 데이터 생성
            response_data = {
                "marker_data": list(marker_data)
            }
            return JsonResponse(response_data)

        except Exception as e:
            # 조회 중에 예외가 발생한 경우 처리
            response_data = {
                "error": str(e)
            }
            return JsonResponse(response_data, status=500)

    # GET 요청이 아닌 경우에 대한 처리
    return JsonResponse({"error": "Invalid request."})

def save_marker_data_I(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            latitude = data.get("latitude")
            longitude = data.get("longitude")
            name = data.get("name")

            # 데이터 처리 로직 수행
            try:
                # MappingPoint 모델을 이용하여 데이터 저장
                mapping_point = MappingPoint_I(latitude=latitude, longitude=longitude, name=name)
                mapping_point.save()

                # 응답 데이터 생성
                response_data = {
                    "message": "Data saved successfully."
                }
                return JsonResponse(response_data)
            
            except Exception as e:
                # 저장 중에 예외가 발생한 경우 처리
                response_data = {
                    "error": str(e)
                }
                return JsonResponse(response_data, status=500)

        except json.JSONDecodeError as e:
            # JSON 디코딩 중에 예외가 발생한 경우 처리
            response_data = {
                "error": "Invalid JSON format."
            }
            return JsonResponse(response_data, status=400)

    # POST 요청이 아닌 경우에 대한 처리
    return JsonResponse({"error": "Invalid request."})

def get_marker_data_I(request):
    if request.method == "GET":
        try:
            # MappingPoint 모델에서 데이터 조회
            marker_data = MappingPoint_I.objects.all().values()

            # 응답 데이터 생성
            response_data = {
                "marker_data": list(marker_data)
            }
            return JsonResponse(response_data)

        except Exception as e:
            # 조회 중에 예외가 발생한 경우 처리
            response_data = {
                "error": str(e)
            }
            return JsonResponse(response_data, status=500)

    # GET 요청이 아닌 경우에 대한 처리
    return JsonResponse({"error": "Invalid request."})


def form_submit_E(request):
    if request.method == 'POST':
        mbti = request.POST.get('mbti')
        influence = request.POST.get('influence')
        comments = request.POST.get('comments')
        
        form = ContactForm_E(mbti=mbti, influence=influence, comments=comments)
        form.save()
        
        return render(request, 'index.html')
    
    return render(request, 'index.html')

def form_submit_I(request):
    if request.method == 'POST':
        mbti = request.POST.get('mbti')
        influence = request.POST.get('influence')
        comments = request.POST.get('comments')
        
        form = ContactForm_I(mbti=mbti, influence=influence, comments=comments)
        form.save()
        
        return render(request, 'index.html')
    
    return render(request, 'index.html')