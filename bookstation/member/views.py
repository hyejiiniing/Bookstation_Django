from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse # reverse 함수 임포트
from . models import Member # Member 테이블 정보 불러옴
from django.http import HttpResponse, HttpResponseRedirect # 응답, 페이지 이동 클래스
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def main(request):
    # response.sendRedirect("member/main.html");
    return render(request,'member/main.html') # 메인 페이지 이동

def logout(request):
    auth.logout(request) # 로그아웃 -> session.invalidate()
    return HttpResponseRedirect("../login/") # 로그인폼 /member/login/

def login(request):
    if request.method != 'POST':  # GET 요청일 때
        return render(request, 'member/login.html')  # 로그인 폼 이동
    else:  # POST 요청일 때 (로그인 시도)
        member_id = request.POST['member_id']
        member_password = request.POST['member_password']
        
        try:
            member = Member.objects.get(member_id=member_id)
            if member.member_password == member_password:
                request.session['login'] = member_id  # 로그인 정보 session에 저장
                return HttpResponseRedirect("../main/")  # 메인 페이지로 리디렉션 (로그인 상태)
            else:
                context = {"msg": "비밀번호가 틀립니다.", "url": "../login/"}
                return render(request, 'main.html', context)
        except Member.DoesNotExist:
            return render(request, 'member/login.html', {"errormsg": "아이디가 틀립니다."})

def registerSuccess(request, member_name):
    return render(request, 'member/registerSuccess.html', {'member_name': member_name})

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

def pwChange(request, member_id):
    # 비밀번호 변경 로직을 여기에 추가
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
                member.member_password = new_password  # 비밀번호를 평문으로 저장
                member.save()
                messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
                return redirect('login')
            except Member.DoesNotExist:
                messages.error(request, '회원 정보를 찾을 수 없습니다.')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
    return redirect('pwChange', member_id=member_id)


# 아이디 체크 
def check_id(request):
    member_id = request.GET.get('member_id', '')
    data = {
        'is_taken': Member.objects.filter(member_id=member_id).exists()
    }
    return JsonResponse(data)

# 메인
def index(request):
    weekly = []  # 주간 베스트 책 목록
    yesterday = []  # 어제 베스트 책 목록
    monthly = []  # 월간 베스트 책 목록
    steady = []  # 스테디셀러 책 목록
    discountBest = []  # 할인 베스트 책 목록
    newNovel = []  # 새로운 소설 책 목록
    newEssay = []  # 새로운 시/에세이 책 목록
    newEconomy = []  # 새로운 경제/경영 책 목록
    newComics = []  # 새로운 만화 책 목록

    context = {
        'weekly': weekly,
        'yesterday': yesterday,
        'monthly': monthly,
        'steady': steady,
        'discountBest': discountBest,
        'newNovel': newNovel,
        'newEssay': newEssay,
        'newEconomy': newEconomy,
        'newComics': newComics,
    }
    return render(request, 'index.html', context)






def info(request,id): # request은 자체 내장에서 전달받은 것임. 이것외에 전달받은 매개변수명은 처리
    try:
        # request.session['login'] => 로그인한 사람의 정보를 꺼내온다.
        login=request.session['login'] # request.session['회원id키명']
    except:
        login="" # 로그인이 안된경우
    if login!="": # 로그인한 상태라면
        member=Member.objects.get(id=id) # id에 해당하는
        # 1.요청객체 2.경로 포함해서 이동할 페이지명 3.dic객체 형태로 전달 {"키명 전달할 객체명(VO)"}
        return render(request,'member/info.html',{"mem":member})
    else: # 다른 사용자의 정보를 조회 -> 해킹소지
        context={"msg":"본인 정보만 조회 가능합니다.","url":"../../main/"} # templates/member/main
        return render(request, 'alert.html',context) # 에러메세지 전달

# 수정할 데이터를 화면에 출력시킬 함수 update함수 작성
def update(request,id): # request은 자체 내장에서 전달받은 것임. 이것외에 전달받은 매개변수명은 처리
    try:
        # request.session['login'] => 로그인한 사람의 정보를 꺼내온다.
        login=request.session['login'] # request.session['회원id키명']
    except:
        login="" # 로그인이 안된경우
    if login!="": # 로그인한 상태라면
        # 전달받은 id와 동일한지 체크
        if login==id: # 수정할 대상자가 내id인지 확인
            return update_rtn(request,id) # 회원수정 해주는 함수 호출
        else:
            context = {"msg": "본인 정보만 조회 가능합니다.", "url": "../../main/"}  # 로그인 화면으로 이동
            return render(request, 'alert.html', context)  # 에러메세지 전달
    else: # 로그아웃 상태
        context={"msg":"먼저 로그인하세요.","url":"../../login/"} # 로그인 화면으로 이동
        return render(request, 'alert.html',context) # 에러메세지 전달

# 실질적인 회원수정 함수 ( 회원수정 == 회원가입 소스코드가 같다.(sql구문만 다르고) 장고에서는 같다.)
def update_rtn(request,id): # 회원가입과 동일
    if request.method != 'POST':  # get방식으로 요청했다면
        # 전달받은 id값에 해당하는 데이터를 꺼내와서 updateform.html에 전달
        member=Member.objects.get(id=id) # (필드명 = 수정하고자 하는 내id)
        return render(request, 'member/updateform.html',{"mem":member})
    else:  # post방식
        # 본인인지 아닌지를 확인
        member=Member.objects.get(id=id)
        if member.pass1 == request.POST['pass']:

            member = Member(id=request.POST['id'],
                            pass1=request.POST['pass'],
                            name=request.POST['name'],
                            gender=request.POST['gender'],
                            tel=request.POST['tel'],
                            email=request.POST['email'],
                            picture=request.POST['picture'])
            member.save()  # 테이블에 저장하라(update ~ sql대신 처리해주는 함수)
            # 수정한 데이터를 확인하기 위해서 회원상세 화면으로 전환 + id 값을 같이 전송
            return HttpResponseRedirect("../../info/"+id+"/")
        else: # 수정 암호가 틀린경우
            context = {"msg": "회원정보 수정 실패.\\n비밀번호 오류입니다.",
                       "url": "../../update/"+id+"/"}  # 다시 수정화면으로 이동
            return render(request, 'alert.html', context)

# delete 함수 작성
def delete(request,id):
    try:
        login=request.session['login']
    except:
        login=""
    if login!="":
        if login==id: # 대상자가 내 id인지 확인
            return delete_rtn(request,id) # 회원탈퇴 해주는 함수 호출
        else:
            context = {"msg": "본인만 탈퇴 가능합니다.", "url": "../../main/"}
            return render(request, 'alert.html', context)
    else: # 로그아웃 상태
        context={"msg":"먼저 로그인하세요.","url":"../../login/"}
        return render(request, 'alert.html',context)

# 실질적인 탈퇴처리 해주는 함수
def delete_rtn(request,id):
    if request.method != 'POST':  # 탈퇴폼으로 이동하라
        return render(request, 'member/deleteform.html',{"id":id})
    else:
        member=Member.objects.get(id=id) # select * from member where id='nup'
        if member.pass1 == request.POST['pass']:
            member.delete() # 테이블에서 삭제하라(insert, update(save()), delete (delete())
            context={"msg":"회원님 탈퇴처리가 완료되었습니다.",
                     "url":"../../login/"} # 정보확인창 이동 자동(현재창 종료)
            return render(request,'alert.html',context) # 암호창 전환
        else: # 비밀번호가 틀린 경우
            context = {"msg": "비밀번호 오류입니다.",
                       "url": "../../delete/"+id+"/"}  # 다시 현재창 그대로 유지
            return render(request, 'alert.html', context)

# 회원리스트 => 관리자로 로그인 했을 경우 -> 1.로그인 상태 OK 2.모든 회원정보를 불러오기 3. 관리자만 조회 가능
def list(request):
    try:
        login=request.session['login'] # String login=(String)session.getAttribute("login")
    except:
        login=""
    if login!="":
        if login=='admin': # 관리자로 로그인 했다면
            member=Member.objects.all() # select * from member_member와 동일한 효과
            return render(request,'member/list.html',{"mlist":member})
        else:
            context = {"msg": "관리자만 조회 가능합니다.", "url": "../main/"} # ../main
            return render(request, 'alert.html', context)
    else: # 로그아웃 상태
        context={"msg":"먼저 로그인하세요.","url":"../login/"}
        return render(request, 'alert.html',context)