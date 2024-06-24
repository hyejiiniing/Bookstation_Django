# 게시판의 요청명령어 등록해서 처리해주는 함수목록리스트 작성용

from django.urls import path # path 함수
from . import views # 요청명령어에 따른 함수 호출

urlpatterns=[
    path('write/', views.write, name='write'), # 글수정과 동일
    path('list/', views.list, name='list'), # 페이징 처리
    # 추가
    path('info/<int:num>/', views.info, name='info'),
    # 수정, 삭제
    path('update/<int:num>/', views.update, name='update'),
    path('delete/<int:num>/', views.delete, name='delete'),
]