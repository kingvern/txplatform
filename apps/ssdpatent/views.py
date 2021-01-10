# _*_ coding: utf-8 _*_
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect

from ssdpatent.adminx import SSDPatentAdmin
from .models import SSDPatent
from .forms import AddSSDPatentForm, ModifySSDPatentForm
from operation.models import UserFavorite, PatentComments


# Create your views here.
class SavePatentView(View):
    def get(self, request):
        all_patent = SSDPatent.objects.all()
        i = 0
        imgtitle_list = []
        for patent in all_patent:
            i += 0
            imgtitle_list.append(patent.imgtitle)
            if i >= 10:
                break
        # return HttpResponse('{"status":"fail", "msg":"fuck"}', content_type='application/json')
        return HttpResponse('{"status":"success", "msg":"{imgtitle_list}"}'.format(imgtitle_list=imgtitle_list), content_type='application/json')


class SSDPatentListView(View):
    def get(self, request):
        all_patent = SSDPatent.objects.all().filter(if_show=True)
        # all_patent = SSDPatent.objects.filter(if_show=True)
        field_category = request.GET.get('field_category', '')
        patent_category = request.GET.get('patent_category', '')
        success_category = request.GET.get('success_category', '')

        price_down = request.GET.get('price_down', '')
        price_up = request.GET.get('price_up', '')

        # newest_patent = all_patent.order_by('-add_time')[:10]
        newest_patent = SSDPatent.objects.all().filter(shop_status='3')[:10]


        FIELD = (
            ('0', '未分类'), ('1', '太赫兹'), ('2', '遥感成像'), ('3', '高可靠嵌入式'), ('4', '智能识别'),
            ('5', '化学化工'), ('6', '新能源'), ('7', '机械'), ('8', '环保和资源'), ('9', '交通运输'),
            ('21', '教育'), ('11', '仪器仪表'), ('12', '新型材料'), ('13', '电子信息'),
            ('14', '生物科学'), ('15', '农林牧业'),
            ('19', '电气自动化'),
            ('23', '安全防护'))

        # field_categorys_array = []
        # for field_category in field_categorys:
        #     field_categorys_array.append({'key': field_category[0], 'value': FIELD[field_category[0]]})

        patent_categorys = all_patent.values_list('tio').distinct()
        # PATENT = {
        #     'fmzl': u'发明专利', 'syxxzl': u'实用新型专利', 'wgzl': '外观专利'
        # }
        PATENT = (('发明', u'发明'), ('实用新型', u'实用新型'), ('外观设计', u'外观设计'))
        # patent_categorys_array = []
        # for patent_category in patent_categorys:
        #     patent_categorys_array.append({'key': patent_category[0], 'value': PATENT[patent_category[0]]})

        # FIELD_set = set()
        # asc_patents = all_patent.order_by('asc')
        # asc_patents = asc_patents.values('asc').distinct()
        # for asc_patent in asc_patents:
        #     FIELD_set |= (set(asc_patent['asc'].split(';')))
        # FIELD = list(FIELD_set)

        if field_category:
            all_patent = all_patent.filter(category=field_category)
        if patent_category:
            all_patent = all_patent.filter(pdt=patent_category)
        if success_category == '1':
            all_patent = all_patent.filter(shop_status='3')
        elif success_category == '0':
            all_patent = all_patent.filter(~Q(shop_status='3'))


        if price_down:
            all_patent = all_patent.filter(price__gte=price_down)
        if price_up:
            all_patent = all_patent.filter(price__lte=price_up)

        asc_patents = all_patent.order_by('asc')
        asc_patents = asc_patents.values('asc').distinct()
        # FIELD_set = set()
        # for asc_patent in asc_patents:
        #     FIELD_set |= (set(asc_patent['asc'].split(';')))
        # FIELD = list(FIELD_set)
        SUCCESS = (('0', u'上架专利'), ('1', u'成功案例'))




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
            # if not request.user.is_authenticated:
            patent_.has_fav = False
            if request.user.is_authenticated:
                if UserFavorite.objects.filter(user=request.user, fav_id=patent_.id, fav_type=1):
                    patent_.has_fav = True
        #     patents_.append(patent_)
        #
        # patent.object_list = patents_

        return render(request, 'patent-list.html', {
            'newest_patent': newest_patent,
            'all_patent': patent,
            'patent_nums': patent_nums,
            'field_category_id': field_category,
            'patent_category_id': patent_category,
            'success_category_id': success_category,
            'price_down': price_down,
            'price_up': price_up,
            'field_categorys': FIELD,
            'patent_categorys': PATENT,
            'success_categorys': SUCCESS
        })
    

class SearchView(View):
    def get(self, request):
        patent = SSDPatent.objects.all()

        newest_patent = SSDPatent.objects.order_by('-add_time')[:10]

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            patent = patent.filter(Q(tic__icontains=search_keywords) | Q(tie__icontains=search_keywords))
        pubDate = request.GET.get('pubDate', "")
        click_num = request.GET.get('click_num', "")
        if pubDate:
            patent = patent.order_by("-add_time")
        if click_num:
            patent = patent.order_by("-click_num")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(patent, 15, request=request)
        patent_data = p.page(page)

        for patent_ in patent_data.object_list:
            patent_.has_fav = False
            if request.user.is_authenticated:
                if UserFavorite.objects.filter(user=request.user, fav_id=patent_.id, fav_type=0):
                    patent_.has_fav = True
        return render(request, 'patent-search.html', {
            'newest_patent': newest_patent,
            'keywords': search_keywords,
            'pubDate': pubDate,
            'click_num': click_num,
            'all_patent': patent_data,
        })


class SSDPatentDetailView(View):
    def get(self, request, patent_id):
        # 此处的id为表默认为我们添加的值。
        patent = SSDPatent.objects.get(id=int(patent_id))
        # 增加专利点击数
        patent.click_num += 1
        patent.save()

        # 是否收藏
        patent.has_fav = False

        patent.available = True

        comments = PatentComments.objects.filter(patent=patent).order_by("-add_time")

        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=patent.id, fav_type=1):
                patent.has_fav = True
            if request.user == patent.seller:
                patent.available = False

        # 取出标签找到标签相同的patent
        cro = patent.cro
        # relate_patents = SSDPatent.objects.filter(field_category=patent.field_category)
        relate_patents = SSDPatent.objects.all()
        if cro:
            # 从1开始否则会推荐自己
            relate_patents = relate_patents.filter(Q(cro=cro) & ~Q(id=patent.id))[0:2]
        else:
            relate_patents = relate_patents.filter(~Q(id=patent.id))[0:2]
        return render(request, "patent-detail.html", {
            "patent": patent,
            "comments": comments,
            "relate_patents": relate_patents,
        })


class AddSSDPatentView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'next'

    def post(self, request, *args, **kwargs):
        # if 'excel' in request.FILES:
        #     print('get excel files!')
        #     return super(SSDPatentAdmin, self).post(request, args, kwargs)
        add_patent_form = AddSSDPatentForm(request.POST, request.FILES)
        if add_patent_form.is_valid():
            patent = add_patent_form.save(commit=False)
            patent.seller = request.user
            patent.hire = patent.price * 0.1
            patent.shop_status = 0
            patent.save()
            return HttpResponseRedirect(reverse('users:mypublish'))
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return render(request, 'usercenter-publish-patent.html', {'patent_form': add_patent_form})

    def get(self, request):
        add_patent_form = AddSSDPatentForm()
        return render(request, 'usercenter-publish-patent.html', {'patent_form': add_patent_form})


class ModifyView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'next'

    def post(self, request, patent_id):
        # patent_id = request.POST.get('id', 0)
        patent = SSDPatent.objects.get(id=int(patent_id))
        modify_patent_form = ModifySSDPatentForm(request.POST, request.FILES, instance=patent)
        if modify_patent_form.is_valid():
            modify_patent_form.save()
            return HttpResponseRedirect(reverse('users:mypublish'))
        else:
            # 通过json的dumps方法把字典转换为json字符串
            return render(request, 'usercenter-publish-patent.html', {'patent_form': modify_patent_form})

    def get(self, request, patent_id):
        # 此处的id为表默认为我们添加的值。
        patent = SSDPatent.objects.get(id=int(patent_id))
        modify_patent_form = ModifySSDPatentForm(instance=patent)
        return render(request, "usercenter-publish-patent.html", {
            "type": "patent:modify",
            "patent": patent,
            'patent_form': modify_patent_form
        })

