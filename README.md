# ![logo1](https://user-images.githubusercontent.com/90889155/163949077-046b55ab-af67-492c-8f95-049dd1aa39a3.png)

💊시각 지능을 활용한 안면인식 Medi-Penser
## 조원
> 안나현 윤진우 정건희 정경수 천유진
> 
# 목차 

- [선정배경 및 기대효과](#선정배경-및-기대효과)

- [서비스 FLOW](#서비스-flow)

- [기능 FLOW](#기능-flow)

- [작업환경](#작업환경)

- [ERD](#erd)

- [Architecture](#architecture)

- [UI/UX](#ui-ux)

## 선정배경 및 기대효과

1. 치매환자, 지적장애인(보호가 필요한 분들)의 올바른 약 복용 지도
2. 간병인/요양보호사 등에게 업무효율화 지원
3. KT B2B+DIGICO 사업 비중 확대에 이바지

## 서비스 FLOW
![big project service flow](https://user-images.githubusercontent.com/42240751/164355370-c89f4473-6ac1-417b-819d-c72b85e32a00.jpg)

## 기능 Flow
![기능](https://user-images.githubusercontent.com/90889155/167329955-8ea883ee-bc1c-4ef6-90c4-1f1bce145fc7.PNG)

## 작업환경
![작업](https://user-images.githubusercontent.com/90889155/167336536-2bead010-65c2-472b-b64b-674f88359d07.PNG)

## ERD
![erd](https://user-images.githubusercontent.com/90889155/167344017-314fd66d-65b0-42f4-86c6-206da4f5bd6f.png)

## Architecture
## UI UX
- 메인 페이지
![127 0 0 1_8000_ (1)](https://user-images.githubusercontent.com/90889155/167337450-3ef8d319-29ff-4e6d-ac95-b7ae33461a74.png)

## 인식할 얼굴의 data set 만들기
![OpenCV - Webcam Capture](https://user-images.githubusercontent.com/85106442/165012056-c7a9ad83-9ffe-43cf-88ca-be2a3c083576.jpg)   
   
cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 흑백으로   
minSize=(20,20) # 얼굴 최소 크기


## 얼굴 검출하기
![Face Detecting](https://user-images.githubusercontent.com/85106442/165013243-437f7427-19b0-4ddc-9dd8-322243a59449.png)

## 하드웨어 설계
![hardware](https://user-images.githubusercontent.com/85106442/166610878-f2529531-eca6-4b89-a5a7-d60b41e9e488.png)
