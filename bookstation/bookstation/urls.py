"""
URL configuration for study1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include # 함수1,함수2,,
# 추가(setting.py에 설정된 static,file폴더를 인식시키기위해서 -> 요청명령어와 연결시켜서 적용)
from django.conf.urls.static import static # static함수(사진 업로드때문에 필요) (경로)
from django.conf import settings # 사진업로드 경로때문에

urlpatterns = [
    path("admin/", admin.site.urls),
    # 추가 member/login, member/logout, member/main
    path('member/',include('member.urls')), # 위임처리 (프로필 사진)
    path('board/',include('board.urls')),
    # path('sangpum/',include('sangpum.urls')) # 상품이미지를 업로드
]
# 파일업로드를 위한 설정(settings.py의 MEDIA_URL(실질적인 폴더경로),MEDIA_ROOT(전체경로) 추가)
# 1.실질적인 업로드경로(/file) 2.전체경로(업로드 경로까지 포함된)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
