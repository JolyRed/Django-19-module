from django.contrib import admin
from .models import Game, Buyer, News

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    search_fields = ('title', )
    list_filter = ('size', 'cost')
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('name', )
    list_per_page = 30

    readonly_fields = ('balance', )

admin.site.register(News)