# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
from . import asset_handler

@csrf_exempt
def report(request):
    # 通过csrf_exempt装饰器，跳过django的csrf安全机制，让post的数据能被接收
    if request.method == 'POST':
        asset_data = request.POST.get('asset_data')
        # print(asset_data)
        data = json.loads(asset_data)
        if not data:
            return HttpResponse('No data!')
        if not issubclass(dict, type(data)):
            return HttpResponse('数据必须为字典格式！')
        # 是否有关键的sn
        sn = data.get('sn', None)
        if sn:
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                #　已经上线的资产则更新数据
                update_asset = asset_handler.UpdateAsset(request, asset_obj[0], data)
                return HttpResponse('资产数据已经更新！')
            else:
                # 进入新资产待审批区
                obj = asset_handler.NewAsset(request, data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse('没有资产sn序列号，请检查数据格式是否正确！')


def index(request):
    assets = models.Asset.objects.all()
    return render(request, 'assets/index.html', locals())


def dashboard(request):
    total = models.Asset.objects.count()
    upline = models.Asset.objects.filter(status=0).count()
    offline = models.Asset.objects.filter(status=1).count()
    unknown = models.Asset.objects.filter(status=2).count()
    breakdown = models.Asset.objects.filter(status=3).count()
    backup = models.Asset.objects.filter(status=4).count()
    up_rate = round(upline / total * 100)
    o_rate = round(offline / total * 100)
    un_rate = round(unknown / total * 100)
    bd_rate = round(breakdown / total * 100)
    bu_rate = round(backup / total * 100)
    server_number = models.Server.objects.count()
    networkdevice_number = models.NetworkDevice.objects.count()
    storagedevice_number = models.StorageDevice.objects.count()
    securitydevice_number = models.SecurityDevice.objects.count()
    software_number = models.Software.objects.count()
    return render(request, 'assets/dashboard.html', locals())


def detail(request, asset_id):
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'assets/detail.html', locals())


