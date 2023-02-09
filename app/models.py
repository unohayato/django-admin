from django.db import models

# Create your models here.
class Book(models.Model):
  class Meta:
    db_table = 'book' #テーブル名の変更、指定
    verbose_name = '本' #モデル単数の場合の名前
    verbose_name_plural = '本たち' #モデル複数の場合の名前
    
  title = models.CharField(verbose_name='タイトル', max_length=255)
  
  # ポストしたモデル一つ一つの管理サイト上での表示名
  def __str__(self):
    return self.title