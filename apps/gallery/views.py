# _*_ coding: utf-8 _*_
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from gallery.models import Gallery
from operation.models import UserFavorite, UserJoin


# Create your views here.

class ListView(View):
    def get(self, request):

        all_gallery = Gallery.objects.all()
        latest_gallery = Gallery.objects.order_by('-time_end')[:2]

        type = request.GET.get('type', '')

        keywords = request.GET.get('keywords', '')
        if keywords:
            all_gallery = all_gallery.filter(Q(name__icontains=keywords) | Q(descs__icontains=keywords))

        if type:
            all_gallery = all_gallery.filter(type=type)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_gallery, 10, request=request)

        gallery = p.page(page)

        return render(request, 'gallery-list.html', {
            'keywords': keywords,
            'gallery': gallery,
            'type': type,
            'latest_gallery': latest_gallery
        })


class DetailView(View):
    def get(self, request, gallery_id):
        gallery = Gallery.objects.get(id=int(gallery_id))
        has_join = False
        has_fav = False
        has_zan = False
        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserJoin.objects.filter(user=request.user, join_id=gallery.id, join_type=3):
                has_join = True

            if UserFavorite.objects.filter(user=request.user, fav_id=gallery.id, fav_type=7):
                has_zan = True
            if UserFavorite.objects.filter(user=request.user, fav_id=gallery.id, fav_type=6):
                has_fav = True

        return render(request, "gallery-detail.html", {
            "gallery": gallery,
            "has_fav": has_fav,
            "has_zan": has_zan,
            "has_join": has_join
        })
