import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparse;
import goggle_login
import naver_blogger
import html
from glob import glob
import io;







class myHandler(BaseHTTPRequestHandler):
# GET형식의 파라미터를 파싱한다.(url의 물음표(?) 이후의 값을 딕셔너리로 파싱한다.
    def __get_Parameter(self, key):
# 해당 클래스에 __param변수가 선언되었는지 확인한다.
        if hasattr(self,"_myHandler__param") == False:
            if "?" in self.path:
# url의 ?이후의 값을 파싱한다.
                self.__param = dict(urlparse.parse_qsl(self.path.split("?")[1], True));
            else :
# url의 ?가 없으면 빈 딕셔너리를 넣는다.
                self.__param = {};
        if key in self.__param:
            return self.__param[key];
        return None;
# POST형식의 form 데이터를 파싱한다.
    def __get_Post_Parameter(self, key):
# 해당 클래스에 __post_param변수가 선언되었는지 확인한다.
        if hasattr(self,"_myHandler__post_param") == False:
# 해더로 부터 formdata를 가져온다.
            data = self.rfile.read(int(self.headers['Content-Length']));
            data.decode("cp949")
            print(data)

            if data is not None:
                print(data)
                self.__post_param = dict(urlparse.parse_qs(data.decode('cp949')));
            else :
                self.__post_param = {};
        if key in self.__post_param:
            return self.__post_param[key][0];
        return None;
# http 프로토콜의 header 내용을 넣는다.
    def __set_Header(self, code):
# 응답 코드를 파라미터로 받아 응답한다.
        self.send_response(code);
        self.send_header('Content-type','text/html');
        self.end_headers();
# http 프로토콜의 body내용을 넣는다.
    def __set_Body(self, data):
# body 응답은 byte형식으로 넣어야 한다.(필요에 의해 주석 해제)
#response = io.BytesIO()
#response.write(b"<html><body><form method='post'><input type='text' name='test' value='hello'><input type='submit'></form></body></html>");
#self.wfile.write(response.getvalue());
# data(string)를 byte형식으로 변환해서 응답한다.
        self.wfile.write(data.encode('cp949'));
# POST 형식의 request일 때 호출된다.
    def do_GET(self):
# GET 방식의 파라미터의 data 값을 취득한다.
        data = self.__get_Parameter('data');
# response(응답)할 body내용이다.
        body = f"""
<!DOCTYPE html>
<meta charset="utf-8">
<html>
<head><title>python</title></head>
<body>
<form method='post'>
<input type='text' name='id' value='{data}'>
<input type='text' name='pw' value='{data}'>
<input type='text' name='title' value='{data}'>
<input type='text' name='main' value='{data}'>
<div>
  <input type="radio" id="google" name="type" value="google"
         checked>
  <label for="google">google</label>
</div>
<div>
  <input type="radio" id="naver" name="type" value="naver">
  <label for="naver">naver</label>
</div>
<input type='submit'>
</form>
</body>
</html>
""";
# response header code는 200(정상)으로 응답한다.
        self.__set_Header(200);
# response body는 위 html 코드 내용을 넣는다.
        self.__set_Body(body);
# POST 형식의 request일 때 호출된다.
    def do_POST(self):
# response header code는 200(정상)으로 응답한다.
        self.__set_Header(200);
# response body는 form으로 받은 test의 값으로 응답한다.

        id= (self.__get_Post_Parameter('id'))
        pw= (self.__get_Post_Parameter('pw'))
        title= (self.__get_Post_Parameter('title'))
        main= (self.__get_Post_Parameter('main'))
        type= (self.__get_post_parameter('type'))
        print(title)
        print(main)
        print(id)
        print(pw)
        if os.path.isfile("titlefile.txt"):
            os.remove("titlefile.txt")

        f = open("titlefile.txt", 'w')


        #encoded_title = title.encode("UTF-8")
        #decoded_title = encoded_title.decode('cp949')
        #title.decode("EUC-KR")
        #encoded_main = main.encode("UTF-8")
        #decoded_main = encoded_main.decode('euc-kr')
        #main.decode("EUC-KR")
        f.write(title)
        print("write over")
        f.close()
        if os.path.isfile("mainfile.txt"):
            os.remove("mainfile.txt")

        m = open("mainfile.txt")
        m.write(main)
        m.close()
        if type =='google':
            goggle_login.google_login(id,pw);
        elif type == 'naver':
            naver_blogger.naver_blog(id,pw);

# http server를 생성한다.
httpd = HTTPServer(('', 80), myHandler);
# 서버 중지(Ctrl + Break)가 나올때까지 message 루프를 돌린다.
httpd.serve_forever();

