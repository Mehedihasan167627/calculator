from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse
from .models import MealRequestClose,Meal
import time
from datetime import datetime ,timedelta
import schedule


def job():
    continue_meal=Meal.objects.filter(is_continue=True)
    next_day=datetime.now().date()+timedelta(days=1)
    desired_time = "21:30"
    close=MealRequestClose.objects.last()
    if close:
        desired_time=close.time 
    current_time = time.strftime("%H:%M")
    if current_time == desired_time:
        check=Meal.objects.filter(date=next_day)
        if not check:
            for meal in continue_meal:
                Meal.objects.create(
                    member=meal.member,
                    breakfast=meal.breakfast,
                    launch=meal.launch,
                    dinner=meal.dinner,
                    is_continue=meal.is_continue,
                    date=next_day
                )
    

schedule.every(1).seconds.do(job)

class MealRequestView(View):
    def get(self,request):
        return render(request,"members/index.html")
    
    def post(self,request):
        while True:    
            schedule.run_pending()
            time.sleep(1) 


