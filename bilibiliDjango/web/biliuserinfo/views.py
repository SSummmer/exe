from django.shortcuts import render
from django.http import HttpResponse
from .models import BiliUser
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    all_userinfo = BiliUser.objects.all()
    page = request.GET.get('page')  # 获取前端传来的page参数的数据
    if page:
        page = int(page)
    else:
        page = 1
    paginator = Paginator(all_userinfo, 10)  # 实例化一个分页对象，每页显示10条
    page_num = paginator.num_pages  # 总页数
    page_user_list = paginator.page(page)  # 此page上的对象列表
    if page_user_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_user_list.has_previous():
        pre_page = page - 1
    else:
        pre_page = page
    if len(range(1, page_num)) < 5:  # 若总页数小于5，页码数列表即其本身
        page_num = range(1, page_num)
    else:
        if page > 4:  # 若请求的页数大于4，页码数列表改变
            page_num = range(page - 1, page + 5)
        else:  # 若总页数为6，页码数列表即其本身
            page_num = range(1, 7)
    top10_user_list = BiliUser.objects.order_by('-follower')[:10]  # 粉丝数排名前十的用户列表
    context = {
        'user_list': page_user_list,
        'page_num': page_num,
        'curr_page': page,
        'next_page': next_page,
        'pre_page': pre_page,
        'top10_user_list': top10_user_list,
    }
    return render(request, 'biliuserinfo/index.html', context=context)


def detail(request, id):
    user_quaryset = BiliUser.objects.filter(mid=id)
    if len(user_quaryset) != 1:
        return HttpResponse("用户不存在")
    else:
        next_user = BiliUser.objects.filter(mid__gt=id).order_by("mid")[:1]
        if len(next_user) != 0:
            next = {
                'next_mid': next_user[0].mid,
                'next_name': next_user[0].name,
            }
        else:
            next = {
                'next_mid': '#',
                'next_name': "无下一个用户",
            }
        pre_user = BiliUser.objects.filter(mid__lt=id).order_by("-mid")[:1]
        if len(pre_user) != 0:
            pre = {
                'pre_mid': pre_user[0].mid,
                'pre_name': pre_user[0].name,
            }
        else:
            pre = {
                'pre_mid': "#",
                'pre_name': "无上一位用户",
            }
        context = {
            'user': user_quaryset[0],
            'next': next,
            'pre': pre,
        }
        return render(request, 'biliuserinfo/detail.html', context=context)


def png(request):
    return render(request, 'biliuserinfo/png.html')
