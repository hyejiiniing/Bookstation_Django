from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),  # 메인 
    path('register/', views.register, name='register'), # 회원가입
    path('registerSuccess/<str:member_name>/', views.registerSuccess, name='registerSuccess'), # 회원가입 성공
    path('login/', views.login, name='login'), # 로그인
    path('logout/', views.logout, name='logout'), # 로그아웃
    path('memberFind/', views.memberFind, name='memberFind'), # 아이디찾기
    path('idSearch/<str:member_name>/<str:member_id>/<str:reg_date>/', views.idSearch, name='idSearch'), # 아이디확인
    path('pwChange/<str:member_id>/', views.pwChange, name='pwChange'), # 비밀번호찾기
    path('update_password/', views.update_password, name='update_password'), # 비밀번호 재설정
    path('adminMember/', views.adminMember, name='adminMember'), # 회원관리
    path('adminDetail/<str:member_id>/', views.adminDetail, name='adminDetail'), # 회원정보
    path('delete_member/', views.delete_member, name='delete_member'), # 회원 삭제
    path('userInfoChange/', views.userInfoChange, name='userInfoChange'), # 회원 정보 수정
]

