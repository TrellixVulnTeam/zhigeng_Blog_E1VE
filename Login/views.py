from django.shortcuts import render, redirect
from user.models import User
from .forms import UserForm, RegisterForm


def index(request):
    context = {

    }
    return render(request, 'index.html', context)


def write(request):
    if request.session.get('is_login', False):
        return render(request, 'editor.html')
    else:
        return redirect('/login/')


def login(request):
    if request.session.get('is_login', False):
        return redirect('/write/')

    if request.method == "POST":
        message = "请检查填写的内容！"
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        try:
            user = User.objects.get(name=username)
            print(user)
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_email'] = user.email
                request.session['user_phone'] = user.phone
                request.session['user_signature'] = user.signature
                request.session.set_expiry(300)
                return redirect('/index/')
            else:
                message = "密码不正确！"
        except:
            message = "用户不存在！"
    return render(request, 'login.html', locals())


# # login_form = UserForm()
# return render(request, 'login.html', locals())

def toregister(request):
    return render(request, 'register.html')


def register(request):
    if request.session.get('is_login', False):
        return redirect("/index/")
    if request.method == "POST":
        message = "请检查填写的内容！"
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        sex = request.POST.get('gender')
        User.objects.create(name=username, sex=sex, password=password, email=email)
    return render(request, 'login.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")
