# ![logo1](https://user-images.githubusercontent.com/90889155/163949077-046b55ab-af67-492c-8f95-049dd1aa39a3.png)

💊시각 지능을 활용한 안면인식 Medi-Penser
## 조원
> 안나현 윤진우 정건희 정경수 천유진
## 실행방법
```
> git clone https://github.com/AIVLE-School-first-Big-Project/Medi-Penser.git
> cd Medi-Penser
> pip install -r requirements.txt
> python manage.py makemigrations(최초실행시)
> python manage.py migrate(최초실행시)
> python manage.py runserver
```
# 목차 

- [선정배경 및 기대효과](#선정배경-및-기대효과)

- [서비스 FLOW](#서비스-flow)

- [기능 FLOW](#기능-flow)

- [작업환경](#작업환경)

- [ERD](#erd)

- [Architecture](#architecture)

- [UI/UX](#ui-ux)
- [얼굴인식 데이터셋](#인식할-얼굴의-data-set-만들기)
- [얼굴 검출](#얼굴-검출하기)
- [하드웨어 설계](#하드웨어-설계)



## 선정배경 및 기대효과

> **선정배경**
>>치매 환자, 지적장애인들은 복용해야 하는 약을 헷갈릴 수 있다.  
>>누군가가 도와준다면 맞는 약을 복용할 수 있지만
>>보호자가 하루 종일 붙어있기는 쉽지 않다.  
>>약의 오남용을 방지하고 보호자에게 여유를 제공할 수 있는 방법이 무엇일지 생각해보았고,    
>>얼굴인식을 통해 올바른 약을 공급하는 서비스에 대한 아이디어를 도출 할 수 있었다.



> **기대효과**
>> 1. 치매환자, 지적장애인(보호가 필요한 분들)의 올바른 약 복용 지도
>> 2. 간병인/요양보호사 등에게 업무효율화 지원
>> 3. KT B2B+DIGICO 사업 비중 확대에 이바지

## 서비스 FLOW
![big project service flow](https://user-images.githubusercontent.com/42240751/164355370-c89f4473-6ac1-417b-819d-c72b85e32a00.jpg)

## 기능 Flow
![기능](https://user-images.githubusercontent.com/90889155/167329955-8ea883ee-bc1c-4ef6-90c4-1f1bce145fc7.PNG)

## 작업환경
![작업](https://user-images.githubusercontent.com/90889155/167336536-2bead010-65c2-472b-b64b-674f88359d07.PNG)

## ERD
![erd](https://user-images.githubusercontent.com/90889155/167431283-8bb696ce-35d3-4a9b-88fb-9f9b1a5057ca.PNG)

## Architecture
![arc](https://user-images.githubusercontent.com/90889155/167430614-82109d19-9e90-4874-9df8-8f0c082301ba.PNG)
## UI UX
- 메인 페이지
![127 0 0 1_8000_ (1)](https://user-images.githubusercontent.com/90889155/167337450-3ef8d319-29ff-4e6d-ac95-b7ae33461a74.png)

- 로그인,회원가입
![login](https://user-images.githubusercontent.com/90889155/167346333-155600de-c606-42eb-974f-266557446a96.png)

- 게시판
![게시판2](https://user-images.githubusercontent.com/90889155/167348425-f80547c1-22fa-46b6-a654-2992e8dba927.PNG)

- 게시글
![게시판](https://user-images.githubusercontent.com/90889155/167348335-834af48a-0127-4123-a3eb-323f08605d59.PNG)


## 인식할 얼굴의 data set 만들기
![OpenCV - Webcam Capture](https://user-images.githubusercontent.com/85106442/165012056-c7a9ad83-9ffe-43cf-88ca-be2a3c083576.jpg)   
   
cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 흑백으로   
minSize=(20,20) # 얼굴 최소 크기


## 얼굴 검출하기
![Face Detecting](https://user-images.githubusercontent.com/42240751/167565215-081b5eef-5211-49af-9e4c-fefca8251c28.png)

## 하드웨어 설계
![hardware](https://user-images.githubusercontent.com/42240751/167565955-97236825-ba37-4370-b277-b85fbaae94e2.png)
