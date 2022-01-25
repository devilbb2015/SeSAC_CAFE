from django.db import IntegrityError
from django.shortcuts import render, redirect


# Create your views here.
from sign.models import CafeUser

## 로그인 페이지
def login(request):


    context = {

    }

    return render(request, 'sign/login.html', context)

## 로그인
def login2(request):
    print("login2 호출 됨")
    data = request.POST
    email = data.get('inputEmail')
    pw = data.get('inputPassword')
    qs = CafeUser.objects.filter(email=email)
    print("qsssssssssss >> ", qs)
    # print(qs[0].email)
    try :
        ## 비밀번호가 맞으면 로그인 성공 후 메인화면
        if qs[0].password == pw :
            print("222222222")
            return redirect('/main')
        ## qs 가 값이 없으면 error 를 넘기고 로그인 페이지로...
        elif qs is None:
            print("444444444")
            context = {
                "e": "error",
            }
            return render(request, 'sign/login.html', context)
        ## 입력받은 pw 를 넘기고 로그인 페이지로...
        else:
            print("3333333333")
            context = {
                "error" : pw
            }
            return render(request, 'sign/login.html', context)
    ## IndexError 발생시 error 메시지를 넘기고 로그인 페이지로...
    except IndexError as e:
        context = {
            "e" : e,
        }
        print("1111111111")
        return render(request, 'sign/login.html', context)


## 페이지 이동
def register(request):

    context = {

    }

    return render(request, 'sign/register.html', context)

## 회원등록
def register2(request):
    print("register2 호출 됨")
    data = request.POST
    ## 입력받은 회원가입 내용을 DB에 저장, 입력받은 이름을 넘기고 로그인 페이지로...
    try :
        new_post = CafeUser(name=data.get('inputName'), email=data.get('inputEmail'), password=data.get('inputPassword'))
        print(new_post)
        new_post.save()
        context = {
            'name' : data.get('inputName'),
        }
        return render(request, '/sign', context)
    ## 이메일 중복시 에러 발생하며 회원가입 페이지로..
    except IntegrityError as e:
        context = {
            'error' : e
        }
        return render(request, 'sign/register.html', context)

