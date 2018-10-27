# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Project
from operation.models import UserFavorite


# Create your views here.

class ProjectListView(View):
    def get(self, request):
        all_project = Project.objects.all()
        field_category = request.GET.get('field_category', '')
        project_step = request.GET.get('project_step', '')
        cooperation = request.GET.get('cooperation', '')
        price_down = request.GET.get('price_down', '')
        price_up = request.GET.get('price_up', '')

        FIELD = (
            ('0', u'食品饮料'), ('1', u'建筑建材'), ('2', u'家居用品'), ('3', u'轻工纺织'), ('4', u'化学化工'), ('5', u'新能源'),
            ('6', u'机械'),
            ('7', u'环保和资源'), ('8', u'橡胶塑料'), ('9', u'仪器仪表'), ('10', u'新型材料'), ('11', u'电子信息'), ('12', u'医药与医疗'),
            ('13', u'农林牧业'), ('14', u'海洋开发'), ('15', u'航空航天'), ('16', u'采矿冶金'), ('17', u'电气自动化'), ('18', u'包装印刷'),
            ('19', u'教育休闲'), ('20', u'钒钛产业'), ('21', u'安全防护'), ('22', u'交通运输'))

        STEP = (
            ('0', u'未知'), ('1', u'实验室阶段'), ('2', u'样品阶段'), ('3', u'小试阶段'),
            ('4', u'中试阶段'),
            ('5', u'量产阶段'))
        CORP = (
            ('0', u'股权投资'), ('1', u'技术转让'), ('2', u'许可使用'), ('3', '合作开发'), ('4', u'合作兴办新企业'),
            ('5', u'其他'))
        if field_category:
            all_project = all_project.filter(field_category=field_category)
        if project_step:
            all_project = all_project.filter(project_step=project_step)
        if cooperation:
            all_project = all_project.filter(cooperation=cooperation)
        if price_down:
            all_project = all_project.filter(price__gte=price_down)
        if price_up:
            all_project = all_project.filter(price__lte=price_up)

        project_nums = all_project.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_project, 1, request=request)

        project = p.page(page)

        return render(request, 'project-list.html', {
            'all_project': project,
            'project_nums': project_nums,
            'field_category_id': field_category,
            'project_step_id': project_step,
            'cooperation_id': cooperation,
            'price_down': price_down,
            'price_up': price_up,
            'field_categorys': FIELD,
            'project_steps': STEP,
            'cooperations': CORP

        })


class ProjectDetailView(View):
    def get(self, request, project_id):
        # 此处的id为表默认为我们添加的值。
        project = Project.objects.get(id=int(project_id))
        # 增加专利点击数
        # project.click_nums += 1
        project.save()

        # 是否收藏
        has_fav_project = False

        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=project.id, fav_type=1):
                has_fav_project = True
        # 取出标签找到标签相同的project
        keyword = project.keyword
        if keyword:
            # 从1开始否则会推荐自己
            relate_projects = Project.objects.filter(keyword=keyword)[1:2]
        else:
            relate_projects = []
        return render(request, "project-detail.html", {
            "project": project,
            "relate_projects": relate_projects,
            "has_fav_project": has_fav_project,
        })
