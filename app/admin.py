from django.contrib import admin
from .models import Book
# Register your models here.

#ここでモデル(管理画面上の)ごとの制限などをかけたい場合はModelAdminをオーバーライドした独自のクラスを定義して以下のAdminSiteクラスのregisterメソッドの第二引数に渡す


"""
デコレータを使わない場合

class BookAdmin(admin.ModelAdmin): 
  pass #何もしない場合

admin.site.register(Book, BookAdmin)
"""


#デコレータを使う場合
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  pass
