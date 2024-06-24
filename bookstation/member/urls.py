from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'), # 회원가입
    path('registerSuccess/<str:member_name>/', views.registerSuccess, name='registerSuccess'), # 회원가입 성공
    # path('check_id/<str:member_id>/', views.check_id, name='check_id'),
    path('login/', views.login, name='login'), # 로그인
    path('logout/', views.logout, name='logout'), # 로그아웃
    path('memberFind/', views.memberFind, name='memberFind'), # 아이디찾기
    path('idSearch/<str:member_name>/<str:member_id>/<str:reg_date>/', views.idSearch, name='idSearch'), # 아이디확인
    path('pwChange/<str:member_id>/', views.pwChange, name='pwChange'), # 비밀번호찾기
    path('update_password/', views.update_password, name='update_password'), # 비밀번호 재설정
    path('main/', views.main, name='main'), # 메인페이지
    path('', views.index, name='index'), # 메인 2
    # 추가 ('요청명령어/<자료형(str or int,,):전달할 매개변수명>')
    path('info/<str:id>/', views.info, name='info'),
    path('update/<str:id>/', views.update, name='update'), # 회원수정하기 위해서 계정 id 전달됨
    # 회원탈퇴
    path('delete/<str:id>/', views.delete, name='delete'),
    # 회원리스트
    path('list/', views.list, name='list'),
]