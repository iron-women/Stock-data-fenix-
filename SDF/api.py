from django.http import JsonResponse


def get_code(request):
    if request.method == 'GET':
        # 获取查询参数
        phonenum = request.GET.get('phonenum', None)
        return JsonResponse({'code': 100, 'msg': '只允许GET请求'})
    return JsonResponse({'code':100, 'msg': '只允许GET请求'})