import bottle

@bottle.route('/')
def home_page():
    return "Hello World\n"

@bottle.route('/testpage')
def test_page():
    return "Test Page"

bottle.debug(True)
bottle.run(host='127.0.0.1',port=8080)