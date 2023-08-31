from django.contrib import admin
from .models import Member,Meal,MoneyDeposit,Fine,BazarCost,BazarList



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
    list_display = ["member","morning","launch","dinner","date","created_at"]
    list_filter=["member","date"]
    search_fields=["member","date"]



@admin.register(MoneyDeposit)
class MoneyDepositAdmin(admin.ModelAdmin):
    list_display = ["member","deposit","date"]


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Fine._meta.fields]
    


@admin.register(BazarCost)
class BazarCostAdmin(admin.ModelAdmin):
    list_display = ["member","total_cost","date"]



@admin.register(BazarList)
class BazarListAdmin(admin.ModelAdmin):
    list_display = ["member","is_bazar_done",
                "bazar_done_status","bazar_date",]
    list_editable=["is_bazar_done"]
