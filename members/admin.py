from django.contrib import admin
from .models import Member,Meal,MoneyDeposit,Fine,BazarCost,BazarList,MealRequestClose


class MealTabularInline(admin.TabularInline):
    model = Meal
    extra = 1 

class MoneyDepositTabularInline(admin.TabularInline):
    model = MoneyDeposit
    extra = 1

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    inlines=[MoneyDepositTabularInline,MealTabularInline]
    list_display = ["name","total_meal","is_bazar_done","ordering"]
    list_editable=["ordering"]


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ["member","breakfast","launch","dinner","date","already_added","is_continue"]
    list_filter=["member","date"]
    date_hierarchy="date"
    search_fields=["member__name","date"]
    list_editable=["is_continue"]



@admin.register(MoneyDeposit)
class MoneyDepositAdmin(admin.ModelAdmin):
    list_display = ["member","deposit","date"]


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Fine._meta.fields]
    


@admin.register(BazarCost)
class BazarCostAdmin(admin.ModelAdmin):
    list_display = ["member","get_description","total_cost","date"]



@admin.register(BazarList)
class BazarListAdmin(admin.ModelAdmin):
    list_display = ["member","bazar_date","bazar_done_status","is_bazar_done"]
    date_hierarchy="bazar_date"           
    list_editable=["is_bazar_done"]
    list_filter=["bazar_date"]




@admin.register(MealRequestClose)
class MealRequestCloseAdmin(admin.ModelAdmin):
    list_display=["id","time"]
    list_editable=["time"]