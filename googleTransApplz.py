import sys
import re
import googletrans

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("UI/google_ui.ui")[0]  # 문자열 형식 - google_ui.ui를 불러오기


# 디자인한 외부 ui 불러와서 저장

class GoogleTrans(QMainWindow, form_class):  # 상속받기
    def __init__(self):
        super().__init__()  # 부모 클래스 생성자 호출 // super() 괄호 꼭 필요함
        self.setupUi(self)  # 불러온 ui파일 연결
# 어느 프로그램 만들던지 12줄과 13줄은 필수로 써야함. 이유는 부모를 불러오고 사용해야 하기 때문
        self.setWindowTitle("구글 한줄 번역기")  # 윈도우 타이플
        self.setWindowIcon(QIcon("icon/google.png"))  # 윈도우 아이콘
        self.statusBar().showMessage("Google Trans App v1.0 Made By Gyohincompany 구글 어플 버전 1.0")  # 윈도우 상태표시줄

        self.trans_btn.clicked.connect(self.trans_action)  # signal 시그널
        self.init_btn1.clicked.connect(self.init1_action)
        self.init_btn2.clicked.connect(self.init2_action)

#버튼이 눌리는 이벤트가 일어나면 트랜스 함수가 호출되는 함수 만들기

    # def trans_action(self):  # 번역 실행 함수 => Slot 함수
    #     korText = self.kor_input.text()  # 입력된 한글 텍스트 가져오기
    #     # 넣는건 set text 이고, 가져오는건 text
    #     trans = googletrans.Translator()  # 구글트랜스 모듈의 객체 선언

    def trans_action(self):  # 번역 실행 함수 => Slot 함수
        korText = self.kor_input.text()  # 입력된 한글 텍스트 가져오기
        reg = re.compile(r'[^가-힣]*$')  # 한글만 찾는 정규표현식

        if korText == "":
            print("공백입력!!")
            QMessageBox.warning(self, "입력오류", "한글입력란에 번역 할 내용을 넣어주세요")
        elif reg.match(korText):  #한글인지 아닌 여부 확인(숫자 또는 영어로만 입력시 경고창 출력)
            print("한글아닌 문자 입력!!")
            QMessageBox.warning(self, "입력오류", "한글입력란에는 한글만 넣어주세요")
        else:
            print("정상번역결과 출력!!")
            trans = googletrans.Translator()  # 구글트랜스 모듈의 객체 선언
            # print(googletrans.LANGUAGES) -> 번역 언어의 dest 약자 찾기

            engText = trans.translate(korText, dest="en")  # 영어 번역 결과
            japText = trans.translate(korText, dest="ja")  # 일본어 번역 결과
            chnText = trans.translate(korText, dest="zh-cn")  # 중국어 번역 결과

        self.eng_input.append(engText.text)  # engText를 찍겠다. 텍스트를 찍어야 하기 때문에 .text 추가로 기입
        # 번역된 영어 텍스트를 eng_input에 출력
        self.jap_input.append(japText.text)
        self.chn_input.append(chnText.text)

    def init2_action(self):  # 전체초기화 버튼 함수
        self.kor_input.clear()  # 입력 내용 지우기
        self.eng_input.clear()
        self.jap_input.clear()
        self.chn_input.clear()

    def init1_action(self):  # 입력초기화 버튼 함수
        self.kor_input.clear()  # 입력 내용 지우기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    googleWin = GoogleTrans()
    googleWin.show()
    sys.exit(app.exec_())



