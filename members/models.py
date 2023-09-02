from django.db import models
from django.utils.html import format_html
from datetime import datetime,timedelta
from ckeditor.fields import RichTextField


class BaseEntity(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True 

class Member(BaseEntity):
    name=models.CharField(max_length=255,unique=True)
    ordering=models.PositiveBigIntegerField(blank=True,null=True)
    is_bazar_done=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        ordering=["ordering"]
    
    @property
    def total_meal(self):
        obj=Meal.objects.prefetch_related("member").filter(member__id=self.id)
        details=""
        # single total 
        morning=0
        for m in obj.filter(breakfast__gt=0):
            morning+=m.breakfast
        launch=0
        for l in obj.filter(launch__gt=0):
            launch+=l.launch
        dinner=0
        for d in obj.filter(dinner__gt=0):
            dinner+=d.dinner

        r=morning+launch+dinner

        details+=f"<span style='margin-right:30px'>Total meal : <b>{r}</b> </span>"
        deposits=MoneyDeposit.objects.prefetch_related("member").filter(member__id=self.id)
        total=sum([obj.deposit for obj in deposits])
        details+=f"<span>Total Deposit:  <b>{total} tk</b></span></br></br>"
         


        meals=Meal.objects.prefetch_related("member").filter(date__month=datetime.now().date().month)
        total_cost=BazarCost.objects.prefetch_related("member").filter(date__month=datetime.now().date().month)
        morning,launch,dinner=0,0,0
        for m in meals.filter(breakfast__gt=0):
            morning+=m.breakfast
        for l in meals.filter(launch__gt=0):
            launch+=m.launch
        for d in meals.filter(dinner__gt=0):
            dinner+=m.dinner
        total_meal=morning+launch+dinner

        total_cost=float(sum([obj.total_cost for obj in total_cost]))
        try:
            meal_rate=total_cost/total_meal
        except:
            meal_rate=0
        
        single_cost=round(meal_rate*r,2)
        details+=f"<span style='margin-right:30px'>Total Cost : <b>{single_cost}</b> </span>"
        deposits=MoneyDeposit.objects.prefetch_related("member").filter(member__id=self.id,date__month=datetime.now().date().month)
        total=float(sum([obj.deposit for obj in deposits]))
        if round(total - float(single_cost),2) <1:
            details+=f"<span>Total Balance:  <b style='color:red;font-size:16px';>{round(total - float(single_cost),2)} tk</b></span></br>"
        else:
            details+=f"<span>Total Balance:  <b>{round(total - float(single_cost),2)} tk</b></span></br></br>"
            
        return format_html(details)
    


class Meal(BaseEntity):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    breakfast=models.DecimalField(max_digits=8,decimal_places=2,default=0.5,verbose_name="সকাল")
    launch=models.DecimalField(max_digits=8,decimal_places=2,default=1,verbose_name="দুপুর")
    dinner=models.DecimalField(max_digits=8,decimal_places=2,default=1,verbose_name="রাত")
    date=models.DateField(default=datetime.now().date()+timedelta(days=1))
    is_continue=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.member.name
    
    @property
    def already_added(self):
        if datetime.now().date()+timedelta(days=1)==self.date: 
            return format_html("<p style='color:green'>already added</p>")
        return format_html("<p style='color:red'>pending...</p>")


class BazarList(BaseEntity):
    member=models.OneToOneField(Member,on_delete=models.CASCADE)
    is_bazar_done=models.BooleanField(default=False) 
    bazar_date=models.DateField(blank=True,null=True) 
   
    def save(self,*args,**kwargs):
        if self.is_bazar_done:
            self.bazar_date=datetime.now().date()
            member=self.member
            member.is_bazar_done=True 
            member.save()
        return super().save(*args,**kwargs)
    
    @property
    def bazar_done_status(self):
        if self.is_bazar_done:
            return "Done"
        return "Pending..."
    

class MoneyDeposit(BaseEntity):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    deposit=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()
    def __str__(self) -> str:
        return self.member.name


class BazarCost(BaseEntity):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    description=RichTextField()
    total_cost=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()

    def __str__(self) -> str:
        return self.member.name
    

    def get_description(self):
        return format_html(self.description)




class Fine(BaseEntity):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    meal=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()

    def __str__(self) -> str:
        return self.member.name
    



class MealRequestClose(models.Model):
    time=models.CharField(max_length=255,help_text="10:20")

    def __str__(self) -> str:
        return self.time 