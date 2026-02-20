@app.route('/test/status')
def test_status():
    """시스템 상태 확인 페이지"""
    try:
        status = {
            'app_name': app.name,
            'routes_count': len(list(app.url_map.iter_rules())),
            'database_tables': [],
            'features': {
                'email': False,
                'portfolio': False,
                'qa': False,
                'login': False
            }
        }
        
        # 데이터베이스 테이블 확인
        try:
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            status['database_tables'] = inspector.get_table_names()
        except:
            pass
        
        # 기능 확인
        routes = list(app.url_map.iter_rules())
        for route in routes:
            endpoint = route.endpoint.lower()
            if 'login' in endpoint:
                status['features']['login'] = True
            if 'portfolio' in endpoint:
                status['features']['portfolio'] = True
            if 'qa' in endpoint or 'question' in endpoint:
                status['features']['qa'] = True
            if 'email' in endpoint or 'send' in endpoint:
                status['features']['email'] = True
        
        return jsonify({
            'success': True,
            'status': status,
            'message': '시스템이 정상적으로 작동 중입니다.'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
