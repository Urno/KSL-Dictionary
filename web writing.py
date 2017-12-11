#한국수어사전 웹 크롤링
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

for x in range(100): #사전 단어 긁어오기 (수어사전의 단어 수가 약 23000개 정도)
    x=x+1
    x=str(x)
    url="http://sldict.korean.go.kr/front/sign/signContentsView.do?origin_no="+x
    
    try :
        html = urlopen(url)
        data=html.read().decode('utf-8')
        begin=data.find("<!-- 동영상 설명 start -->")
        end=data.find("<!--// 내용 보기 end -->")
        end+=len("<!--// 내용 보기 end -->") #내용 선별하기
        
        letter=data[begin:end].split()
        #print(letter) #실제 데이터 확인
        D={}
        
        for a in letter:
            if letter[letter.index(a)+1]=="사진</dt>" and a=='pointer;">수형':
                num=letter.index(a)+6
                image=letter[num][5:-2]
                letter.remove(a)#수어 사진
            if letter[letter.index(a)+1]=="설명</dt>" and a=='pointer;">수형':
                num=letter.index(a)+2
                exp=letter[num][4:]
                for x in range(num+1, len(letter)-1):
                    exp+=" "+letter[x]
                    if letter[x+1]=="<br/>":
                        exp=exp[:-5]
                        break #수어 동작 묘사
            if a=='그림)</dt>' :
                num=letter.index(a)+1
                inf=letter[num][4:]
                for x in range(num+1, len(letter)-1):
                    inf+=" "+letter[x]
                    if letter[x]=="<!--":
                        inf=inf[:-10]
                        break #수어 정보
            if a=='pointer;">한국어' and letter[letter.index(a)+1]=="정보</span></dt>":
                num=letter.index(a)+2
                name=letter[num][4:]
                for x in range(num+1, len(letter)-1):
                    name+=" "+letter[x]
                    if letter[x]=="</dd>":
                        name=name[:-5]
                        part=letter[x+2]
                        break #수어 단어, 품사
                num=letter.index(a)+7
                mean=letter[num]
                for x in range(num+1, len(letter)-1):
                    mean+=" "+letter[x]
                    if letter[x]=="<!--":
                        mean=mean[:-5]
                        break #단어 의미
    except:
        continue
    
    try : 
        f = open('dictionary.txt', 'a') # 파일 열기
        temp=name+"+"+image+"+"+exp+"+"+inf+"+"+part+"+"+mean
        print(temp, file=f)
    except:
        temp="" # 파일 저장하기, 가끔 오류나는 경우 존재 ex) x=30
                # 어느정도 숫자 이상부터는 D 저장X
        
f.close()
