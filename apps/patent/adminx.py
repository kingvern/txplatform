# _*_ coding: utf-8 _*_

import xadmin

from .models import Patent




class PatentAdmin(object):
    list_display = ['id', 'name', 'seller', 'patent_id', 'patent_category', 'price', 'keyword', 'click_num', 'fav_num',
                    'if_show', 'shop_status', 'note']
    search_fields = ['id', 'name', 'seller__username', 'seller__mobile', 'detail', 'patent_id', 'note']
    list_filter = ['id', 'name', 'seller', 'patent_id', 'patent_category', 'price', 'click_num', 'fav_num',
                   'shop_status', 'note']
    list_editable = ['note', 'shop_status', 'if_show']
    refresh_times = [3, 5]
    # 富文本
    style_fields = {"detail": "ueditor"}

    import_excel = True  # 控制开关

    # def save_models(self):
    #     obj = self.new_obj
    #     if obj.shop_status == '1':
    #         obj.if_show = True
    #     else:
    #         obj.if_show = False
    #     super.save_models()
    # obj.save()
    # self.new_obj.area_company = Group.objects.get(user=self.request.user)
    # super().save_models()

    # def save_models(self):
    #     it = self
    #     obj = self.new_obj
    #     if obj.shop_status:
    #         obj.if_show = True
    #     obj.save()


xadmin.site.register(Patent, PatentAdmin)
