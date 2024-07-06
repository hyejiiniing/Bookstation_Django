from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse # reverse 함수 임포트
from . models import Member # Member 테이블 정보
from django.http import HttpResponse, HttpResponseRedirect # 응답, 페이지 이동
from django.http import JsonResponse # JSON 응답을 위해 JsonResponse 클래스 임포트
from django.contrib import messages # 알림 메시지 표시
from django.contrib import auth # 로그인 인증 모듈
from django.shortcuts import get_object_or_404 # 특정 객체가 존재하지 않을 때 404 에러 반환
from django.core.paginator import Paginator # 페이징 처리
# views.py

# 메인
def main(request):
    return render(request,' main.html') # 메인 페이지 이동

# 로그인
def login(request):
    if request.method != 'POST':
        return render(request, 'member/login.html')  # 로그인 폼 이동
    else: 
        member_id = request.POST['member_id']
        member_password = request.POST['member_password']
        
        try:
            member = Member.objects.get(member_id=member_id)
            if member.member_password == member_password:
                request.session['login_id'] = member.member_id  # 로그인 정보 session에 저장
                request.session['login_point'] = member.member_point
                request.session['login_grade'] = member.grade_name 
                return HttpResponseRedirect("/")  # 메인 페이지로 리디렉션 (로그인 상태)
            else:
                context = {"msg": "비밀번호가 틀립니다.", "url": "../login/"}
                messages.error(request, '비밀번호가 틀렸습니다.')
                return render(request, 'member/login.html', context)
        except Member.DoesNotExist:
            messages.error(request, '아이디가 틀렸습니다.')
            return render(request, 'member/login.html', {"errormsg": "아이디가 틀립니다."})

# 로그아웃
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("../login/")

# 회원가입
def register(request):
    if request.method == 'POST':
        member_id = request.POST['member_id']
        member_password = request.POST['member_password']
        member_name = request.POST['member_name']
        member_gender = request.POST['member_gender']
        member_phone = request.POST['member_phone']
        member_email = request.POST['member_email']
        member_zipcode = request.POST['member_zipcode']
        member_address1 = request.POST['member_address1']
        member_address2 = request.POST['member_address2']
        member_birthday = request.POST['member_birthday']

        member = Member(
            member_id=member_id,
            member_password=member_password,
            member_name=member_name,
            member_gender=member_gender,
            member_phone=member_phone,
            member_email=member_email,
            member_zipcode=member_zipcode,
            member_address1=member_address1,
            member_address2=member_address2,
            member_birthday=member_birthday,
            reg_date=timezone.now()
        )
        member.save()

        return redirect(reverse('registerSuccess', kwargs={'member_name': member_name}))
    else:
        return render(request, 'member/register.html')
    
# 회원가입 성공 
def registerSuccess(request, member_name):
    return render(request, 'member/registerSuccess.html', {'member_name': member_name})

# 아이디 찾기   
def memberFind(request):
    if request.method == 'POST':
        member_name = request.POST['member_name']
        member_email = request.POST['member_email']
        
        members = Member.objects.filter(member_name=member_name, member_email=member_email)
        
        if members.exists():
            member = members.first()
            reg_date = member.reg_date.strftime('%Y-%m-%d')
            return redirect('idSearch', member_name=member.member_name, member_id=member.member_id, reg_date=reg_date)
        else:
            messages.error(request, '아이디를 찾을 수 없습니다.')
            return redirect('memberFind')
    return render(request, 'member/memberFind.html')

# 아이디 확인
def idSearch(request, member_name, member_id, reg_date):
    context = {
        'member_name': member_name,
        'member_id': member_id,
        'reg_date': reg_date
    }
    return render(request, 'member/idSearch.html', context)

# 비밀번호 찾기
def pwChange(request, member_id):
    return render(request, 'member/pwChange.html', {'member_id': member_id})

# 비밀번호 변경
def update_password(request):
    if request.method == 'POST':
        member_id = request.POST['member_id']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        if new_password == confirm_password:
            try:
                member = Member.objects.get(member_id=member_id)
                member.member_password = new_password 
                member.save()
                messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
                return redirect('login')
            except Member.DoesNotExist:
                messages.error(request, '회원 정보를 찾을 수 없습니다.')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
    return redirect('pwChange', member_id=member_id)

# 회원관리  
def adminMember(request):
    login_id = request.session.get('login_id', "")
    
    alert_message = ""
    if login_id != "admin":
        alert_message = "관리자만 사용할 수 있습니다."
    
    allMemList = Member.objects.all()
    sort = request.GET.get('sort', 'all')
    
    # 페이징 처리 
    paginator = Paginator(allMemList, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'member/adminMember.html', {
        'page_obj': page_obj,
        'sort': sort,
        'alert_message': alert_message  
    })
    
# 회원 수정
def adminDetail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'member/adminDetail.html', {'member': member})

# 회원 정보 변경
def userInfoChange(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        member_name = request.POST.get('member_name')
        member_email = request.POST.get('member_email')
        member_zipcode = request.POST.get('member_zipcode')
        member_address1 = request.POST.get('member_address1')
        member_address2 = request.POST.get('member_address2')
        member_phone = request.POST.get('member_phone')

        member = get_object_or_404(Member, member_id=member_id)
        member.member_name = member_name
        member.member_email = member_email
        member.member_zipcode = member_zipcode
        member.member_address1 = member_address1
        member.member_address2 = member_address2
        member.member_phone = member_phone
        member.save()
        
        return redirect('adminDetail', member_id=member.member_id) 

    return render(request, 'member/adminDetail.html')

# 회원 삭제 
def delete_member(request):
    member_id = request.POST.get('member_id')
    member = get_object_or_404(Member, pk=member_id)
    member.delete()
    return redirect('adminMember') 