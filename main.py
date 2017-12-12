#main

#값을 비교하는 함수 switch
def switch(x) :
    return {
    1 : "category", 
    2 : "shape",
    3 : "sentence",
    4 : "add"
}.get(x, 0)

#사전의 기능 여부
print("수어 사전을 시작합니다.")
while True:
    print("수어에 대한 내용이면 S, 농문화에 대한 내용이면 D를 눌러주세요.")
    f=input("")
    print()
    
    if f=="S":
        print("수어를 검색하기 위해 분류를 제공합니다. 원하면 Y, 원치 않으시면 N를 눌러주세요.")
        tp=input("")
        
        if tp=="Y":
            print("수어의 카테고리를 통해 찾고자 하는 경우는 1, 수어의 형태를 통해 찾고자 하는 경우는 2, 수어의 문장 분석을 하고자 하는 경우는 3, 새로운 수어 단어를 추가하고자 하는 경우는 4를 눌러주세요")
            case=int(input(""))
            switch(case)
        #1번의 경우 사전 내 분류기준
        #2번의 경우 이미지 파일을 불러 원하는 경우를 탐색, switch문 사용
        #3번의 경우 KoNLPy 이용한 형태소 분석 이후 단어 검색
        #4번의 경우 사전의 정보를 충족할 수 있도록 조건적인 접근 허용
        
        elif tp=="N":
            print("검색할 단어를 입력해주세요.")
            search=input("")
        #Naver API와 연동하여 검색한 단어와 유사한 단어들을 나열
        #수어 사전 목록 중에 단어가 있는 지를 분석하여 결과 제공 - 수어 단어의 부족성 때문에!
            
        else :
            print("잘못된 입력입니다. 시작 화면으로 돌아갑니다.")
            continue

    elif f=="D":
        print("아직 개발중인 내용입니다. 시작 화면으로 돌아갑니다.")
        print()

    else:
        print("잘못된 입력입니다. 시작 화면으로 돌아갑니다.")
        print()
