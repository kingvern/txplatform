# _*_ coding: utf-8 _*_
import json

from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Patent
from .forms import AddPatentForm
from operation.models import UserFavorite


# Create your views here.

class PatentListView(View):
    def get(self, request):
        all_patent = Patent.objects.all()
        field_category = request.GET.get('field_category', '')
        patent_category = request.GET.get('patent_category', '')
        price_down = request.GET.get('price_down', '')
        price_up = request.GET.get('price_up', '')

        newest_patent = all_patent.order_by('-add_time')[:10]

        # field_categorys = all_patent.values_list('field_category').distinct()
        # FIELD = {
        #     '0': u'食品饮料', '1': u'建筑建材', '2': u'家居用品', '3': u'轻工纺织', '4': u'化学化工', '5': u'新能源', '6': u'机械',
        #     '7': u'环保和资源', '8': u'橡胶塑料', '9': u'仪器仪表', '10': u'新型材料', '11': u'电子信息', '12': u'医药与医疗',
        #     '13': u'农林牧业', '14': u'海洋开发', '15': u'航空航天', '16': u'采矿冶金', '17': u'电气自动化', '18': u'包装印刷',
        #     '19': u'教育休闲', '20': u'钒钛产业', '21': u'安全防护', '22': u'交通运输'
        # }
        FIELD = (
            ('0', u'食品饮料'), ('1', u'建筑建材'), ('2', u'家居用品'), ('3', u'轻工纺织'), ('4', u'化学化工'), ('5', u'新能源'),
            ('6', u'机械'),
            ('7', u'环保和资源'), ('8', u'橡胶塑料'), ('9', u'仪器仪表'), ('10', u'新型材料'), ('11', u'电子信息'), ('12', u'医药与医疗'),
            ('13', u'农林牧业'), ('14', u'海洋开发'), ('15', u'航空航天'), ('16', u'采矿冶金'), ('17', u'电气自动化'), ('18', u'包装印刷'),
            ('19', u'教育休闲'), ('20', u'钒钛产业'), ('21', u'安全防护'), ('22', u'交通运输'))

        # field_categorys_array = []
        # for field_category in field_categorys:
        #     field_categorys_array.append({'key': field_category[0], 'value': FIELD[field_category[0]]})

        patent_categorys = all_patent.values_list('patent_category').distinct()
        # PATENT = {
        #     'fmzl': u'发明专利', 'syxxzl': u'实用新型专利', 'wgzl': '外观专利'
        # }
        PATENT = (('fmzl', u'发明专利'), ('syxxzl', u'实用新型专利'), ('wgzl', '外观专利'))
        # patent_categorys_array = []
        # for patent_category in patent_categorys:
        #     patent_categorys_array.append({'key': patent_category[0], 'value': PATENT[patent_category[0]]})

        if field_category:
            all_patent = all_patent.filter(field_category=field_category)
        if patent_category:
            all_patent = all_patent.filter(patent_category=patent_category)
        if price_down:
            all_patent = all_patent.filter(price__gte=price_down)
        if price_up:
            all_patent = all_patent.filter(price__lte=price_up)

        patent_nums = all_patent.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_patent, 10, request=request)

        patent = p.page(page)

        # patents = patent.object_list
        # patents_=[]

        for patent_ in patent.object_list:
            patent_.has_fav = False
            if request.user.is_authenticated:
                if UserFavorite.objects.filter(user=request.user, fav_id=patent_.id, fav_type=1):
                    patent_.has_fav = True
        #     patents_.append(patent_)
        #
        # patent.object_list = patents_

        return render(request, 'patent-list.html', {
            'current_page': 'patent',
            'newest_patent': newest_patent,
            'all_patent': patent,
            'patent_nums': patent_nums,
            'field_category_id': field_category,
            'patent_category_id': patent_category,
            'price_down': price_down,
            'price_up': price_up,
            'field_categorys': FIELD,
            'patent_categorys': PATENT
        })


class PatentDetailView(View):
    def get(self, request, patent_id):
        # 此处的id为表默认为我们添加的值。
        patent = Patent.objects.get(id=int(patent_id))
        # 增加专利点击数
        patent.click_num += 1
        patent.save()

        # 是否收藏
        has_fav_patent = False

        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=patent.id, fav_type=1):
                has_fav_patent = True
        # 取出标签找到标签相同的patent
        keyword = patent.keyword
        if keyword:
            # 从1开始否则会推荐自己
            relate_patents = Patent.objects.filter(keyword=keyword)[1:2]
        else:
            relate_patents = []
        return render(request, "patent-detail.html", {
            'current_page': 'patent',
            "patent": patent,
            "relate_patents": relate_patents,
            "has_fav_patent": has_fav_patent,
        })


class AddPatentView(View):
    def post(self, request):
        add_patent_form = AddPatentForm(request.POST)
        if add_patent_form.is_valid():
            patent = add_patent_form.save(commit=False)
            patent.seller = request.user
            patent.save()
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return HttpResponse(
                json.dumps(
                    add_patent_form.errors),
                content_type='application/json')
            # patent = Patent()
            # patent.name = request.POST.get('name', '')
            # patent.seller = request.user
            # patent.patent_id = request.POST.get('patent_id', '')
            # patent.field_category = request.POST.get('field_category', '')
            # patent.patent_category = request.POST.get('patent_category', '')
            # patent.province = request.POST.get('province', '')
            # patent.patent_expired = request.POST.get('patent_expired', '')
            # patent.price = request.POST.get('price', '')
            # patent.bargain = request.POST.get('bargain', '')
            # patent.hire = request.POST.get('hire', '')
            # patent.status = request.POST.get('status', '')
            # patent.IPC_num = request.POST.get('IPC_num', '')
            # patent.application_date = request.POST.get('application_date', '')
            # patent.agent = request.POST.get('agent', '')
            # patent.agency = request.POST.get('agency', '')
            # patent.inventor = request.POST.get('inventor', '')
            # patent.applicant = request.POST.get('applicant', '')
            # patent.contact = request.POST.get('contact', '')
            # patent.contact_mobile = request.POST.get('contact_mobile', '')
            # patent.detail = request.POST.get('detail', '')
            # patent.save()
