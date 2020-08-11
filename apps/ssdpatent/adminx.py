# _*_ coding: utf-8 _*_
# import pymysql as pymysql
from django.http import HttpResponseRedirect
from django.template.base import logger
from xlrd import open_workbook


import xadmin
from django.apps import apps

from .models import SSDPatent


class SSDPatentAdmin(object):
    list_display = [ 'id','tio', 'tic', 'tie','if_success', 'absc', 'abse',  'inc', 'agc',  'ano',  'ans','abso',
                    'ino', 'ine',  'exo', 'pd', 'asc', 'ipc', 'ase', 'aso', 'exc', 'pK', 'sfpns', 'lssc', 'vu',
                    'crc', 'pdfexist', 'ape', 'apc', 'cri', 'apo', 'cro', 'pdt', 'pns', 'pid', 'pno', 'depc', 'ad',
                    'ago', 'pdf', 'age', 'lc', 'debeo', 'debec', 'cre', 'debee', 'note', 'shop_status',
                    'if_show']
    search_fields = ['abso', 'tie', 'absc', 'abse', 'tio', 'inc', 'agc',  'ano', 'tic', 'ans',
                    'ino', 'ine',  'exo', 'pd', 'asc', 'ipc', 'ase', 'aso', 'exc', 'pK', 'sfpns', 'lssc', 'vu',
                    'crc', 'pdfexist', 'ape', 'apc', 'cri', 'apo', 'cro', 'pdt', 'pns', 'pid', 'pno', 'depc', 'ad',
                    'ago', 'pdf', 'age', 'lc', 'debeo', 'debec', 'cre', 'debee', 'note',]
    list_filter = ['abso', 'tie', 'absc', 'abse', 'tio', 'inc', 'agc',  'ano', 'tic', 'ans',
                    'ino', 'ine',  'exo', 'pd', 'asc', 'ipc', 'ase', 'aso', 'exc', 'pK', 'sfpns', 'lssc', 'vu',
                    'crc', 'pdfexist', 'ape', 'apc', 'cri', 'apo', 'cro', 'pdt', 'pns', 'pid', 'pno', 'depc', 'ad',
                    'ago', 'pdf', 'age', 'lc', 'debeo', 'debec', 'cre', 'debee', 'note',]
    list_editable = ['note', 'if_success', 'shop_status', 'if_show']
    refresh_times = [3, 5]
    # 富文本
    # style_fields = {"detail": "ueditor"}

    import_excel = True  # 控制开关

    # def queryset(self):
    #     qs = super(SSDPatentAdmin, self).queryset()
    #     qs = qs.filter(is_banner=False)
    #     return qs
    #
    # def save_models(self):
    #     # 在保存课程是后统计课程的课程数
    #     obj = self.new_obj
    #     obj.save()
    #     if obj.course_org is not None:
    #         course_org = obj.course_org
    #         course_org.courses = Course.objects.filter(course_org=course_org).count()
    #         course_org.save()

    # 定义重载post方法来获取excel表格中的数据
    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            execl_file = request.FILES.get('excel')
            files = open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            excel_into_model('ssdpatent', 'SSDPatent', excel_file=files)
            return HttpResponseRedirect('/admin/ssdpatent/ssdpatent/')
        return super(SSDPatentAdmin, self).post(request, *args, **kwargs)

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

def excel_into_model(appname, model_name, excel_file):
    try:
        appname_ = apps.get_model(appname, model_name)
        logger.info(appname + 'and' + model_name + 'model_name and appname is this')
        fields = appname_._meta.fields
        # 导入model,动态导入
        exec('from %s.models import %s' % (appname, model_name))
    except:
        logger.info('model_name and appname is not exist')
    field_name = []
    # 只导入第一个sheet中的数据
    table = excel_file.sheet_by_index(0)
    nrows = table.nrows
    table_header = table.row_values(0)
    print('table_header', table_header)
    # for cell in table_header:
    #     # for name in fields:
    #         # if cell in name.verbose_name.__str__():
    #         # if cell in name.name.__str__():
    #         #     field_name.append(name.name)
    #     for name in fields:
    #         if cell == name.name.__str__():
    #             field_name.append(name.name)
    field_name = table_header
    print('field_name', field_name)
    if 'pk' in field_name:
        field_name.remove('add_time')
    for x in range(1, nrows):
        # 行的数据,创建对象,进行报错数据
        exec_line = 'obj' + '=%s()' % model_name
        exec('obj' + '=%s()' % model_name)
        print(len(field_name))
        for y in range(len(field_name)):
            # exec_line = 'obj.%s' % field_name[y] + '="%s"' % (pymysql.escape_string(table.cell_value(x, y)))
            exec("obj.%s" % field_name[y] + "='''%s'''" % (table.cell_value(x, y)))
        exec('obj.save()')


xadmin.site.register(SSDPatent, SSDPatentAdmin)
