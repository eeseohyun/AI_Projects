from flask import Flask, render_template
import corona19_data
from datetime import date, timedelta   #현재날짜,시간차 참조

#app 생성
app = Flask(__name__)

#url router
@app.route('/')
def index():
    now = date.today()
    now_string = now.strftime("%Y%m%d")  #2021-10-11 -> 20211011 string형태로 변환
    print(now_string)

    data = corona19_data.get_corona19_data(now_string, now_string)
    print(data)

    #data가 없는 경우, 하루 전날 데이터 불러오기 요청
    if not data :
        yesterday = now - timedelta(days=1)
        yesterday_string = yesterday.strftime("%Y%m%d")
        print(yesterday_string)

        data = corona19_data.get_corona19_data(now_string, now_string)
        print(data)

    
    return render_template('index.html', data = data[1:])


#main
if __name__ == '__main__':
    app.run(debug=True)  #수정가능

