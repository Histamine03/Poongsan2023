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
    <td><img src=".images\DataSet\RAW\forest (1).png" alt="RAW_test" width="350"/></td>
    <td><img src=".images\DataSet\RAW\forest (77).png" alt="RAW_test" width="350"/></td>
  </tr>
</table>

### GAN 증강
<p> 데이터셋 예시
<table>
  <tr>
    <td><img src=".mages\DataSet\GAN\GAN_forest (38).png" alt="GAN_test" width="350"/></td>
    <td><img src=".images\DataSet\GAN\seed0635.png" alt="GAN_test" width="350"/></td>
  </tr>
</table>

### 작은 객체 증강
<p> 데이터셋 예시
<table>
  <tr>
    <td><img src=".images\DataSet\SMALL\img (1).png" alt="SMALL_test" width="350"/></td>
    <td><img src=".images\DataSet\SMALL\img.png" alt="SMALL_test" width="350"/></td>
  </tr>
</table>

### 기하학적 증강
<p> 데이터셋 예시
<table>
  <tr>
    <td><img src=".images\DataSet\AUG\forest (1).png" alt="SMALL_test" width="233"/></td>
    <td><img src=".\images\DataSet\AUG\forest (1)_blurred.png" alt="SMALL_test" width="233"/></td>
    <td><img src=".\images\DataSet\AUG\forest (1)_flipped.png" alt="SMALL_test" width="233"/></td>
  </tr>
</table>

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


