from django.shortcuts import render
from django.http import HttpResponse

from test_app.models import TestModel


def test_page(request):
    tm = TestModel.objects.all().order_by('value')
    return render(request,
                  'test_app/test_page.html',     # 使用するテンプレート
                  {'data': tm})         # テンプレートに渡すデータ
