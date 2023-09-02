from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse
from .models import MealRequestClose,Meal
import time
from datetime import datetime ,timedelta
# import schedule
# import threading


# class MyThread(threading.Thread):
#     def __init__(self, delay=1):
#         super().__init__()
#         self.delay = delay

#     def run(self):
#         while True: 
#             job()
#             print("called")
#             time.sleep(self.delay)

# def job():
#     next_day=datetime.now().date()+timedelta(days=1)
#     continue_meal=Meal.objects.filter(is_continue=True,date=datetime.now().date())

#     desired_time = "23:01"

#     # close=MealRequestClose.objects.last()
#     # if close:
#     #     desired_time=close.time 
#     current_time = time.strftime("%H:%M")
#     print(current_time)
#     if current_time == desired_time:
#         for meal in continue_meal:
#                 Meal.objects.create(
#                     member=meal.member,
#                     breakfast=meal.breakfast,
#                     launch=meal.launch,
#                     dinner=meal.dinner,
#                     is_continue=meal.is_continue,
#                     date=next_day
#                 )
#         print("created")
    
    

# schedule.every(1).seconds.do(job)

class MealRequestView(View):
    def get(self,request):
        return render(request,"members/index.html")
    
    def post(self,request):
        # reader=MyThread(1)
        # reader.start()
        return JsonResponse({"data":"ok"})



