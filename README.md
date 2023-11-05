# Case study on application of intelligent technology to military drones

## 실험 결과
<img src="./images/result.png"  width="700" height="370">

<table>
  <tr>
    <td><b>[원본 데이터 (200장)]</b> <br><img src=".\runs\test\RAW_last\precision-recall_curve.png" alt="RAW_test" width="350"/></td>
    <td><b>[GAN 증강 (400장)]</b> <br><img src=".\runs\test\GAN_last\precision-recall_curve.png" alt="GAN_test" width="350"/></td>
  </tr>
  <tr>
    <td><b>[기하학적 증강 (600장)]</b> <br><img src=".\runs\test\AUG_last\precision-recall_curve.png" alt="Augmentation" width="350"> </td>
    <td><b>[작은 객체 증강(200장)]</b> <br><img src=".\runs\test\SMALL_last\precision-recall_curve.png" alt="Small objet Augmentation" width="350"/></td>
  </tr>
</table>

## 데이터셋

### 원본 데이터
<p> 데이터셋 예시
<table>
  <tr>
    <td><img src=".\images\DataSet\RAW\forest (1).png" alt="RAW_test" width="350"/></td>
    <td><img src=".\images\DataSet\RAW\tank (77).png" alt="RAW_test" width="350"/></td>
  </tr>
</table>
<ul>
  <li>UNITY 환경 내에서 다양한 각도와 객체 크기를 고려하여, 숲 배경(100장), 도시 배경(100장) 을 수집하였습니다.</li>
  <li><strong>데이터 규모: </strong>200장</li>
  <li><strong>객체 갯수: </strong>200개</li>
</ul>

### GAN 증강
<p> 데이터셋 예시
<table>
  <tr>
    <td><img src=".\images\DataSet\GAN\GAN_forest (38).png" alt="GAN_test" width="350"/></td>
    <td><img src=".\images\DataSet\GAN\seed0635.png" alt="GAN_test" width="350"/></td>
  </tr>
</table>

<ul>
  <li>원본 데이터를 기반으로 styleGAN3-ADA를 바탕으로 증강하였습니다.</li>
  <li><strong>데이터 규모: </strong>400장</li>
  <li><strong>객체 갯수: </strong>400개</li>
</ul>

### 작은 객체 증강
<p> 데이터셋 예시
<table>
  <tr>
    <td><img src=".\images\DataSet\SMALL\img (1).png" alt="SMALL_test" width="350"/></td>
    <td><img src=".\images\DataSet\SMALL\img.png" alt="SMALL_test" width="350"/></td>
  </tr>
</table>

<ul>
  <li>원본 데이터를 기반으로 <a href = "https://github.com/Histamine03/small_obj_augmentation">작은 객체 증강 GUI </a>을 이용하여 이미지 내에 객체 등장 횟수를 2번으로 조정하였습니다.</li>
  <li><strong>데이터 규모: </strong>200장</li>
  <li><strong>객체 갯수: </strong>400개</li>
</ul>


### 기하학적 증강
<p> 데이터셋 예시
<table>
  <tr>
    <td><img src=".\images\DataSet\AUG\forest (1).png" alt="SMALL_test" width="233"/></td>
    <td><img src=".\images\DataSet\AUG\forest (1)_blurred.png" alt="SMALL_test" width="233"/></td>
    <td><img src=".\images\DataSet\AUG\forest (1)_flipped.png" alt="SMALL_test" width="233"/></td>
  </tr>
</table>

<ul>
  <li>원본 데이터를 기반으로 가우시안 필터 증강과 이미지 반전을 써서 원본 데이터의 3배만큼 증강시켰습니다.</li>
  <li><strong>데이터 규모: </strong>600장</li>
  <li><strong>객체 갯수: </strong>600개</li>
</ul>
</ul>

### 테스트 데이터셋
<p> 데이터셋 예시
<table>
  <tr>
    <td><img src=".\images\DataSet\TEST\test_tank (4).png" alt="test" width="350"/></td>
    <td><img src=".\images\DataSet\TEST\test_tank (45).png" alt="test" width="350"/></td>
  </tr>
  <tr>
    <td><img src=".\images\DataSet\TEST\test_tank (33).png" alt="test" width="350"/></td>
    <td><img src=".\images\DataSet\TEST\test_tank (1).png"alt="test" width="350"/></td>
  </tr>
</table>

<ul>
  <li>보다 다양한 환경과 극한 환경에서 이미지를 수집하기 위해 노력하였습니다.</li>
  <li><strong>데이터 규모: </strong>50장</li>
</ul>


