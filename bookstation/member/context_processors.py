def login_session(request):
    return {
        'login_id': request.session.get('login_id'),
        'login_point': request.session.get('login_point'),
        'login_grade': request.session.get('login_grade'),
    }