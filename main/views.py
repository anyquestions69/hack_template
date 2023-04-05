from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render
from .models import User, Member, Orders, Category
from .filters import MemberFilter, ShortFilter
from django.core.exceptions import ObjectDoesNotExist




class Api():
    def register(request):
        if request.method == "POST":
            person = User()
            person.login = request.POST.get("login")
            person.email = request.POST.get("email")
            person.password = request.POST.get("password")
            person.save()
            response = HttpResponseRedirect("/")
            request.session['UUID'] = person.id
        return response

    def login(request):
        if request.method != 'POST':
            raise Http404('Только POST запросы')
        try:
            m = User.objects.get(login=request.POST['login'])
            print(m.password)
            print(request.POST['password'])
            if m.password == request.POST['password']:
                request.session['UUID'] = m.id
                print(request.session['UUID'])
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("неверный пароль")
        except User.DoesNotExist:
            return HttpResponse("Логин и пароль не совпадают")
        
    def logout(request):
        try:
            del request.session['UUID']
        except KeyError:
            pass
        return HttpResponseRedirect("/login")
    def filter(request):
        name = request.GET.get('name', '')
        inn = request.GET.get('inn', '')
        users = Member.objects.filter(inn__contains=inn)
        users = Member.objects.order_by("name", "age")
        print(users)
        return JsonResponse(users, safe=False)

    
    
class View():
    def index(request):
        users = Member.objects.all()
        filter = MemberFilter(request.GET, queryset=users)
        filter_short = ShortFilter(request.GET, queryset=users)
        if filter:
            users = filter.qs
        else:
            users = filter_short.qs
        return render(request, 'index.html', {"members": users, "filter":filter, "short":filter_short})
    def orders(request, pkid):
        member = Member.objects.get(id=pkid)
        orders = Orders.objects.filter(seller=pkid) |  Orders.objects.filter(buyer=pkid)
        return render(request, 'user.html', {"user":member, "orders":orders})
    def users(request):
        
        users = Member.objects.all()
        return render(request, 'index.html', {"members": users})