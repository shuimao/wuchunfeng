import xadmin
from .models import *
xadmin.site.register(Category)
xadmin.site.register(Tag)
# xadmin.site.register(Article)
xadmin.site.register(Ads)

class ArticleAdmin:
    style_fields = {"body":"ueditor"}

xadmin.site.register(Article, ArticleAdmin)