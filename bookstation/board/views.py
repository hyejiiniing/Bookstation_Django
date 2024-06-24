from django.shortcuts import render # 페이지 전환(이동시킬 페이지명, 전달할 매개변수명)

# Create your views here.

from django.http import HttpResponseRedirect # 페이지 전환(요청명령어를 이용) ex) redirect:/명령어
from.models import Board # 테이블과 관련된 Board클래스 불러온다.
from django.utils import timezone # 게시판의 글작성 날짜

# 페이징 처리
from django.core.paginator import Paginator # 페이징처리 해주는 클래스

def handle_upload(f):
    with open("file/board/"+f.name,"wb+") as destination:
        for ch in f.chunks():
            destination.write(ch)

def write(request):
    if request.method!='POST': # Get방식
        return render(request,'board/writeform.html') # response역할
    else: # post
        try:
            # 파일업로드할 파일명
            filename=request.FILES["file1"].name
            print('업로드할 파일명(filename)=>',filename) # System.out.println(~)
            handle_upload(request.FILES["file1"])
        except:
            filename="" # 업로드한 파일이 없는 경우
        b=Board(name=request.POST['name'],
                pass1=request.POST['pass'],
                subject=request.POST['subject'],
                content=request.POST['content'],
                regdate=timezone.now(), readcnt=0, file1=filename)
        b.save() # insert, update -> save(), delete -> delete()
        return HttpResponseRedirect("../list/") # 글목록보기 /board/list/ -> list.html

def list(request):
    # String pagenum=request.getParameter("pageNum") if pageNum==null pageNum="1"
    # 기본페이지가 1 int pageNum=Integer.parseInt(request.getParameter("pageNum")) "1" -> 1
    pageNum=int(request.GET.get('pageNum',1)) # pageNum의 값을 1로 설정
    print('pageNum=>',pageNum) # 1
    # select * from board order by num desc; # 형식) order_by('-필드명') 내림차순
    all_boards=Board.objects.all().order_by("-num") # 모든 레코드를 가져오는데 게시물의 내림차순 순서
    paginator=Paginator(all_boards,3) # 1.화면에 출력할 모든 레코드객체 2.numPerPage
    board_list=paginator.get_page(pageNum) # get_page(화면에 출력할 페이지번호)
    print('board_list=>',board_list)
    # 총레코드 갯수
    listcount=Board.objects.count() # Board.objects.all(), Board.object.get(필드명=값)
    return render(request,'board/list.html',
                  {'board':board_list,'listcount':listcount})

# 자료실 상세보기
def info(request,num):
    # select * from board_board where num=11
    board=Board.objects.get(num=num)
    # update board_board set readcnt=readcnt+1 where num=11
    board.readcnt+=1 # 조회수 증가 board.readcnt=board.readcnt+1
    board.save() # insert, update => save(), delete -> delete() 함수 사용
    return render(request,'board/info.html',{'b':board}) # {'board':board}

# 글수정 -> 글쓰기와 로직이 동일(코딩이 동일하다)
def update(request,num):
    if request.method!='POST': # Get방식
        board = Board.objects.get(num=num)
        context={'b':board}
        return render(request,'board/updateform.html',context)
    else: # post
        try: # 자료실 수정
            # 파일업로드할 파일명
            handle_upload(request.FILES["file1"])
            filename = request.FILES["file1"].name
            print('업로드할 파일명(filename)=>',filename)
        except:
            filename="" # 업로드한 파일이 없는 경우
        # 업로드 변경
        if filename=="":
            filename=request.POST['file2'] # 기존의 업로드한 파일전송받음.

        b=Board(num=request.POST['num'], # 자료실 수정하는 경우에는 반드시 자료실 번호를 전달받을것.
                name=request.POST['name'],
                pass1=request.POST['pass'],
                subject=request.POST['subject'],
                content=request.POST['content'],
                regdate=timezone.now(), readcnt=0, file1=filename)
        b.save() # insert, update -> save(), delete -> delete()
        return HttpResponseRedirect("../../list/")

# 자료실 삭제
def delete(request,num): # 요청명령어에 연결되어서 동적으로 매개변수를 전달하는 경우
    if request.method!='POST': # Get방식
        return render(request,'board/deleteform.html', {"num":num})
    else: # post
        board=Board.objects.get(num=num)
        pass1=request.POST['pass'] # 암호 전달 받음
        if board.pass1 == pass1: # 암호가 맞다면
            board.delete()
            return HttpResponseRedirect("../../list/")
        else:
            return render(request,'board/deleteform.html',{"num":num})