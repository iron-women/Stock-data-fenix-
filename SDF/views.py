from django.shortcuts import render, redirect
from SDF.api import get_code
from SDF.forms import UserForm


def show_log(request):
    return render(request, 'SDF_login.html')


def show_reg(request):
    if request.method == 'GET':
        return render(request, 'SDF_register.html')

    # 处理post请求
    form = UserForm(request.POST)  # 将数据传入到Form类
    # 验证数据的完整性
    if form.is_valid():
        code = get_code(form.cleaned_data.get('phonenum'))
        if code.decode() == form.cleaned_data.get('code'):
            form.save()  # 无错时，则保存数据
            return redirect('/sdf/index/')
        else:
            return render(request, 'SDF_register.html', {'errors': '<h4>验证码验证失败!</h4>'})

    errors = form.errors  # 默认情况是html的错误信息
    return render(request, 'SDF_register.html', locals())

def show_index(request):
    return render(request, 'SDF_article.html')
