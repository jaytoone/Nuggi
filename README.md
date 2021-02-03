## Mask_RCNN의 전이학습을 통한 육류 이미지 누끼따기



**Mask_RCNN : https://github.com/matterport/Mask_RCNN** 



## Description

* via_region_data.json : 누끼를 따기위해 학습시킬 이미지의 라벨을 위해 VGG Image Annotator (VIA)를 활용해 만든 json 데이터

* Make_model_gogi.ipynb : Mask_RCNN의 전이학습을 통한 육류 이미지 누끼따는 인공지능 모델 제작

* Detect gogi and save.ipynb : 제작된 인공지능 모델을 사용해 육류를 찾고 누끼를 따며 CNN모델에 학습시킬 이미지 데이터를 생산 

  * **육류만 누끼를 딴 결과 (후 작업을 위해 마스킹처리하였다.)**

    <img src="https://user-images.githubusercontent.com/50652715/80910282-27616c00-8d69-11ea-9261-c188169d04c3.png" alt="bbox" style="zoom: 25%;" /><img src="https://user-images.githubusercontent.com/50652715/80910284-2b8d8980-8d69-11ea-9401-0faa6a801b52.png" alt="bbox_multi" style="zoom: 25%;" />

* 아래 그림은 **CNN에 학습시킬 이미지 데이터**를 설명한다.

![example1](https://user-images.githubusercontent.com/50652715/80910120-5b885d00-8d68-11ea-8d38-700d33f37b46.png)

CNN에 학습시킬 **이미지 데이터의 정형화**를 위해 250 * 250 PIXEL의 크기로 지정하였고, 그림과 같이 Mask-RCNN을 통해 **누끼를 딴 상태에서 고기(마스킹)의 내부에 검은색 박스의 이미지 데이터만을 추출**한다. 과정과 결과는 아래 그림과 같다. (**우측 하단의 이미지가 CNN에 사용할 최종 데이터**)

![example2](https://user-images.githubusercontent.com/50652715/80910180-b752e600-8d68-11ea-8f90-dedf91c78941.png)



## Result

<img src="https://user-images.githubusercontent.com/50652715/80909640-d5b6e280-8d64-11ea-99b7-704270dccc23.png" alt="chagget_prediction" style="zoom:50%;" />

## Reference

Image Preprocessing : https://machinelearningmastery.com/how-to-manually-scale-image-pixel-data-for-deep-learning/