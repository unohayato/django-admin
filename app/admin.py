from django.contrib import admin


from .models import Author, Book, Publisher

#ここでモデル(管理画面上の)ごとの制限などをかけたい場合はModelAdminをオーバーライドした独自のクラスを定義して以下のAdminSiteクラスのregisterメソッドの第二引数に渡す


"""
デコレータを使わない場合

class BookAdmin(admin.ModelAdmin): 
  pass #何もしない場合

admin.site.register(Book, BookAdmin)
"""






@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'price', 'user_id')
    ordering = ('-price',)
    def save_model(self, request, obj, form, change):
        # update_dateを現在時刻に更新
        obj.user_id = request.user.id
        # save_model関数をオーバーライドしてデータベースに変更を反映
        super(BookModelAdmin, self).save_model(request, obj, form, change)


admin.site.register(Publisher)
admin.site.register(Author)

