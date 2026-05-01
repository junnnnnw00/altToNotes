# CSED226 - _Data_Analytics__11_1__Bivariate_Data_Analysis_and_Visualization 상세 해설 노트 (음성 전사 포함)

> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다. Alt(altalt.io) 음성 전사 데이터를 함께 활용했습니다.

---

## Slide 1

**핵심 개념**
*   **Bivariate Visualization**: 두 가지 속성(변수) 간의 관계를 시각적으로 탐색하는 기법입니다. 단일 변수를 분석하는 것을 넘어, 두 변수가 서로 어떻게 영향을 주고받는지 이해하는 데 중점을 둡니다.
*   **Multivariate Visualization**: 세 가지 이상의 속성(변수) 간의 복합적인 관계를 시각적으로 분석하는 기법입니다. 데이터 내의 복잡한 패턴과 상호작용을 파악하는 데 활용됩니다.
*   **목표**: 데이터 내 두 개 이상의 변수 간의 복잡한 관계를 이해하기 위한 시각화 기술을 습득하는 것입니다.

**코드/수식 해설**
현재 슬라이드는 강의의 제목 슬라이드이므로, 해당되는 코드나 수식은 없습니다. 이후 슬라이드에서 각 시각화 기법과 관련된 Python 라이브러리(NumPy, pandas, matplotlib, scikit-learn 등) 코드가 다뤄질 예정입니다.

**구체적 예시**
*   **Univariate (단일 변수) 예시**: 학생들의 키 분포를 히스토그램으로 확인하는 경우 (키라는 단일 변수).
*   **Bivariate (두 변수) 예시**: 학생들의 키와 몸무게 간의 관계를 산점도(scatter plot)로 확인하여 키가 클수록 몸무게도 많이 나가는 경향이 있는지 파악하는 경우.
*   **Multivariate (다변수) 예시**: 학생들의 키, 몸무게, 나이, 학점 네 가지 변수 간의 관계를 동시에 시각화하여 특정 그룹에서 나타나는 복합적인 패턴을 찾는 경우. 예를 들어, 키와 몸무게는 양의 상관관계를 가지며, 나이가 많을수록 학점이 높은 경향이 있는지 등을 탐색할 수 있습니다.

**강의 내용**
교수님께서는 이번 강의가 기존에 학습했던 히스토그램과 같은 단일 변수(single variable) 시각화를 넘어, 두 개 또는 그 이상의 변수 간의 관계를 이해하기 위한 기술로 확장됨을 강조하셨습니다. 특히, 앞으로 다룰 내용의 로드맵으로 '관계형 플롯(relational plots)'과 '이변수 밀도 플롯(bivariate density plots)'을 첫 번째 주제로 언급하여, 강의의 큰 흐름을 제시했습니다.

**시험 포인트**
*   ⭐ **Bivariate와 Multivariate Visualization의 정의 및 차이점**을 명확히 이해하고 설명할 수 있어야 합니다. (변수의 개수에 따른 분류)
*   ⭐ 왜 단일 변수 시각화를 넘어 **다변수 시각화가 필요한지**, 그 목적을 설명할 수 있어야 합니다. (복잡한 관계 이해, 패턴 발견)

---
## Slide 2

**핵심 개념**
이 슬라이드는 데이터 분석 및 시각화에 사용될 다양한 플롯(Plot) 유형들을 개관하고 있습니다. 크게 7가지 범주로 나뉘며, 각 범주별로 주로 사용되는 시각화 기법과 해당 라이브러리 함수가 제시되어 있습니다.

1.  **Relational (X-Y) Plot**: 두 변수 간의 관계를 탐색하는 데 사용됩니다.
    *   **Scatter Plot**: 두 연속형 변수 간의 개별 데이터 포인트 분포를 보여줍니다.
    *   **Line Plot**: 시간에 따른 변화나 순서가 있는 데이터의 추세를 나타내는 데 적합합니다.
    *   **Regression / LOESS Plot**: 두 변수 간의 선형 또는 비선형 관계 및 추세선을 시각화합니다.
    *   **Figure-level faceting**: `relplot`과 같이 여러 서브플롯을 통해 복잡한 관계를 다양한 조건에서 분석할 수 있게 합니다.

2.  **Bivariate Density Plot**: 두 변수의 결합 분포(joint distribution) 밀도를 시각화합니다.
    *   **Hexbin / 2D Hist**: 2차원 공간에서의 데이터 밀도를 육각형 또는 사각형 격자를 사용하여 표현합니다.
    *   **2D KDE**: 2차원 커널 밀도 추정(Kernel Density Estimation)을 통해 두 변수의 밀도 분포를 부드러운 곡면으로 시각화합니다.

3.  **Distributions (by group) Plot**: 한 변수의 분포를 여러 그룹별로 비교하여 시각화합니다.
    *   **Hist/KDE**: 단일 변수의 분포를 히스토그램이나 커널 밀도 추정으로 보여줍니다. `displot`, `kdeplot` 함수가 사용됩니다.
    *   **ECDF Plot**: 경험적 누적 분포 함수(Empirical Cumulative Distribution Function)를 통해 데이터의 분포를 나타냅니다.
    *   **Box / Violin / Boxen Plot**: 데이터의 중앙값, 사분위수, 이상치 등을 요약하여 분포를 보여줍니다. 특히 `violinplot`은 데이터 밀도까지 함께 표현합니다.
    *   **Raw points**: `stripplot`이나 `swarmplot`을 사용하여 개별 데이터 포인트의 분포를 직접 보여줍니다.

4.  **Matrix / Structure Plot**: 데이터의 행렬 또는 구조적 관계를 시각화합니다.
    *   **Pair Plot**: 데이터프레임 내 모든 수치형 변수 쌍에 대한 산점도와 각 변수의 분포를 한눈에 보여줍니다.
    *   **Correlation Heatmap**: 변수 간의 상관관계를 색상 강도로 시각화합니다.
    *   **Clustered Heatmap**: 상관관계 또는 유사도에 따라 행과 열을 재정렬하여 패턴을 파악합니다.

5.  **Multivariate Projections**: 다변수 데이터를 저차원으로 투영하여 시각화합니다.
    *   **PCA scatter**: 주성분 분석(PCA)을 통해 차원을 축소한 후 산점도로 시각화합니다.
    *   **Parallel coordinates**: 각 변수를 평행한 축으로 표현하고 데이터 포인트를 이어서 다변수 데이터의 패턴을 시각화합니다.

6.  **Diagnostics Plot**: 주로 회귀 모델의 진단에 사용됩니다.
    *   **Residuals vs Fitted**: 잔차(residuals)와 예측값(fitted values)을 비교하여 모델의 가정 위반 여부를 확인합니다.

7.  **Faceting & Encodings**: 시각화에 추가적인 차원을 인코딩하는 방법들입니다.
    *   `hue`, `style`, `size`, `row`/`col`, `col_wrap` 등을 사용하여 색상, 모양, 크기, 행/열 분할 등으로 추가 정보를 표현합니다.

**코드/수식 해설**

*   **`scatterplot`**: 두 연속형 변수 $X$와 $Y$ 사이의 관계를 점으로 표현합니다.
    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt
    # 예시: 붓꽃 데이터의 꽃받침 길이와 너비 관계
    sns.scatterplot(x="sepal_length", y="sepal_width", data=iris_df)
    plt.show()
    ```
*   **`jointplot(kind="hex"/"hist"/"kde")`**: `kind` 인자에 따라 2변수 밀도 플롯의 종류를 지정합니다.
    *   `kind="hex"`: 육각형 구간에 따른 데이터 밀도를 보여줍니다.
    *   `kind="hist"`: 2차원 히스토그램으로 밀도를 나타냅니다.
    *   `kind="kde"`: 2차원 커널 밀도 추정으로 부드러운 밀도 곡선을 그립니다.
    ```python
    sns.jointplot(x="sepal_length", y="sepal_width", data=iris_df, kind="kde")
    plt.show()
    ```
*   **`displot`, `kdeplot`**: 단일 변수의 분포를 시각화합니다.
    *   `displot`은 히스토그램, KDE 플롯, ECDF 플롯 등을 유연하게 그릴 수 있는 Figure-level 함수입니다.
    *   `kdeplot`은 커널 밀도 추정만 그립니다.
    ```python
    sns.displot(data=iris_df, x="sepal_length", kind="hist", hue="species")
    plt.show()
    ```
*   **`boxplot`, `violinplot`, `boxenplot`**: 그룹별 분포를 비교하는 데 유용합니다.
    *   `boxplot`: 5가지 요약 통계량(최소, 1사분위, 중앙값, 3사분위, 최대)을 시각화합니다.
    *   `violinplot`: 박스 플롯에 커널 밀도 추정(KDE)을 추가하여 분포의 모양을 더 자세히 보여줍니다.
    *   `boxenplot`: 박스 플롯보다 더 많은 분위수를 표시하여 분포의 꼬리 부분을 더 자세히 보여줍니다.
    ```python
    sns.boxplot(x="species", y="sepal_length", data=iris_df)
    plt.show()
    ```

**구체적 예시**

`Distributions (by group)` 플롯의 예시로 붓꽃(Iris) 데이터셋을 생각해 봅시다. 붓꽃에는 'setosa', 'versicolor', 'virginica' 세 가지 종(species)이 있습니다.

만약 우리가 각 종별 'sepal length'(꽃받침 길이)의 분포를 비교하고 싶다면 다음과 같은 플롯을 사용할 수 있습니다.

*   **Box Plot**: 각 종의 꽃받침 길이 분포의 중앙값, 사분위수, 그리고 이상치를 빠르게 비교할 수 있습니다. 예를 들어, 'setosa' 종의 꽃받침 길이가 다른 두 종에 비해 평균적으로 짧고 분포의 폭도 좁다는 것을 한눈에 파악할 수 있습니다.
*   **Violin Plot**: 박스 플롯 정보와 함께 각 종의 꽃받침 길이 데이터 밀도 곡선을 보여주어, 'setosa'는 비교적 대칭적인 분포를 보이는 반면, 'virginica'는 약간 치우친 분포를 가질 수 있다는 등의 세부적인 분포 형태를 파악할 수 있습니다.
*   **Histogram/KDE by group**: `displot`에 `hue="species"`를 추가하여 각 종별로 히스토그램이나 KDE 플롯을 따로 그려 분포의 형태를 비교할 수 있습니다.

**강의 내용**
교수님은 특히 "Distributions (by group)" 섹션을 강조하셨습니다. `hist`, `histogram`, `KDE`, `ECDF`, `violin`, `box` 플롯 등은 원래 단일 속성(single attributes)의 분포를 보여주는 데 사용되지만, 이 슬라이드에서 다루는 방식은 **여러 그룹별로 분포를 비교**하는 데 초점을 맞춘다고 설명하셨습니다. 즉, 하나의 차트 안에 여러 그룹의 분포 플롯을 함께 그려서 한 개 이상의 속성(그룹 속성 포함)을 커버하여 비교 분석할 수 있음을 강조했습니다. 이어서 "metrics plot"이라는 표현으로 다음 섹션인 "Matrix / Structure" 플롯으로 넘어갈 것을 암시했습니다.

**시험 포인트**
*   ⭐ **각 플롯 유형의 목적과 사용 사례**: 주어진 데이터 특성(두 변수 관계, 밀도, 분포 비교 등)에 따라 적절한 시각화 방법을 선택할 수 있어야 합니다.
*   ⭐ **`Distributions (by group)`의 중요성**: 단일 속성 분포 플롯을 여러 그룹에 적용함으로써 그룹 간의 비교 분석이 가능하다는 점을 이해해야 합니다.
*   ⭐ **FacetGrid 및 Encoding의 활용**: `hue`, `style`, `size`, `row`/`col`과 같은 인자들이 시각화에 추가적인 차원(정보)을 어떻게 인코딩하고, 복잡한 데이터 분석에 어떻게 기여하는지 알아야 합니다.
*   ⭐ **주요 Seaborn 함수 이름과 그 기능 연결**: `scatterplot`, `lineplot`, `regplot`, `jointplot`, `displot`, `kdeplot`, `boxplot`, `violinplot`, `pairplot`, `heatmap` 등의 함수가 어떤 유형의 플롯을 그리는지 파악해야 합니다.

---
## Slide 3

### 핵심 개념: Scatter Plot (산점도)

*   **정의**: 두 변수 $x$와 $y$의 관계를 시각화하기 위해 각 데이터 포인트 $(x_i, y_i)$를 2차원 평면에 점으로 표현하는 그래프입니다.
*   **다변수 인코딩 (Optional Encodings)**:
    *   `hue` (색상): 범주형 변수를 색상으로 구분하여 나타냅니다. (예: 붓꽃 종)
    *   `size` (크기): 숫자형 변수를 점의 크기로 표현합니다. (예: 꽃잎 넓이)
    *   `style` (스타일): 마커의 모양(예: 원, 엑스, 사각형 등)으로 추가적인 범주형 정보를 인코딩할 수 있습니다.

### 사용 시점 및 해석 방법

*   **주요 사용 시점 (`Use when`)**:
    *   두 변수 간의 선형 또는 비선형 관계를 탐색할 때.
    *   데이터 내의 군집(clusters)을 식별할 때.
    *   이상치(outliers)를 찾아낼 때.
*   **해석 방법 (`How to read`)**:
    *   **기울기(Slope)와 형태(shape)**: 점들의 분포가 형성하는 기울기와 모양을 통해 변수 간의 관계(양의 상관관계, 음의 상관관계, 비선형 관계, 무관계 등)를 파악합니다.
    *   **띠의 두께 (분산, `band thickness (variance)`)**: 점들이 얼마나 퍼져 있는지를 통해 데이터의 분산 정도를 가늠합니다. 띠가 두꺼우면 분산이 크고, 얇으면 분산이 작습니다.
    *   **분리된 구름 (`separate clouds`)**: 점들이 여러 개의 뚜렷한 '구름'처럼 모여 있다면, 이는 데이터 내에 명확한 군집(clusters)이 존재함을 시사합니다.

### 코드/수식 해설

산점도를 그리는 가장 일반적인 방법은 `matplotlib`의 `plt.scatter` 또는 `seaborn`의 `sns.scatterplot`을 사용하는 것입니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris

# Iris 데이터셋 로드
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# 기본적인 산점도 예시: 꽃받침 길이와 너비 관계
plt.figure(figsize=(8, 6))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Basic Scatter Plot of Iris Data')
plt.grid(True)
plt.show()

# hue를 사용하여 붓꽃 종(species)별로 색상 구분
# size, alpha 등의 인자를 추가하여 과밀화(overplotting) 문제를 완화할 수 있습니다.
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='sepal length (cm)',
    y='sepal width (cm)',
    hue='species', # 종(species)에 따라 점의 색상 변경
    s=100,         # 점의 크기 조절
    alpha=0.7      # 점의 투명도 조절
)
plt.title('Scatter Plot of Iris Data with Species Hue')
plt.show()
```

데이터 포인트는 일반적으로 $(x_i, y_i)$로 표현되며, 여기서 $i$는 $1$부터 $n$까지의 데이터 인덱스를 나타냅니다. $n$은 전체 데이터 포인트의 개수입니다.

### 구체적 예시

붓꽃(Iris) 데이터셋을 예시로 들 수 있습니다. 붓꽃의 꽃받침 길이($x_i$)와 꽃받침 너비($y_i$)를 두 축으로 산점도를 그리면, 붓꽃의 세 가지 종(setosa, versicolor, virginica)이 서로 다른 영역에 군집을 이루는 것을 시각적으로 확인할 수 있습니다. 이때 `hue` 인자를 사용하여 각 종을 다른 색상으로 표시하면 군집이 더욱 명확해집니다. 이를 통해 각 종의 꽃받침 특성이 어떻게 다른지 한눈에 파악할 수 있습니다.

### 강의 내용

교수님은 이 슬라이드를 통해 다변량 시각화의 큰 그림을 설명하면서 산점도의 중요성을 강조하셨습니다.

*   **다변량 시각화의 강력한 도구**: `pair plot`, `correlation heat map`, `cluster heat map` 등은 한 번에 모든 특성(features)의 전체적인 그림을 볼 수 있는 매우 강력한 도구이며, 산점도는 특히 `pair plot`의 핵심 구성 요소입니다.
*   **고차원 데이터 시각화**: `PCA` (Principal Component Analysis)와 같은 다변량 투영(multivariate projections) 기법도 언급되었지만, 이 강의에서는 `parallel coordinates`를 통한 고차원 데이터 시각화와 모델 진단을 위한 `diagnostic plots`에 더 중점을 둘 예정이라고 하셨습니다.
*   **예시 데이터셋**: 지난주와 동일하게 붓꽃(Iris) 데이터셋과 와인 분류(wine classification) 데이터셋을 활용하여 실습 및 설명을 진행할 것임을 밝히셨습니다. 이는 산점도를 포함한 다양한 시각화 기법을 실제 데이터에 적용해 볼 기회가 될 것입니다.

### 시험 포인트

*   ⭐ **산점도의 정의 및 주요 용도**: 두 변수 간의 관계, 군집, 이상치 탐색에 사용된다는 점을 명확히 이해해야 합니다.
*   ⭐ **다변수 인코딩 방법**: `hue`, `size`, `style`을 사용하여 2차원 이상의 정보를 시각화하는 방법을 설명하고 예시를 들 수 있어야 합니다.
*   ⭐ **산점도 해석 방법**: 기울기/형태, 띠의 두께(분산), 분리된 군집의 의미를 파악하는 것이 중요합니다.
*   ⭐ **Overplotting 문제 및 해결책 (`Pitfalls`)**: 데이터 포인트 $n$이 많을 때 발생하는 과밀화(overplotting) 현상과 이를 완화하기 위한 투명도(`alpha`) 조절 또는 밀도 플롯(density plots) 사용법을 알아두세요.
*   ⭐ **Pair Plot과의 관계**: `pair plot`이 여러 산점도의 조합이라는 점을 인지하고, 이것이 여러 변수 간의 관계를 한 번에 파악하는 데 어떻게 도움이 되는지 이해해야 합니다.

---
## Slide 4

### 핵심 개념
산점도(Scatter Plot)는 두 개 이상의 변수 간의 관계를 시각적으로 파악하는 데 사용되는 가장 기본적인 플롯입니다.
*   **기본 원리**: 각 관측치 $ (x_i, y_i) $에 대해 2차원 평면 상에 하나의 점을 배치합니다. 여기서 $x_i$는 $x$축에 매핑될 변수의 값이고, $y_i$는 $y$축에 매핑될 변수의 값입니다.
*   **강력한 확장성**: 기본적인 $x, y$축 외에도 점의 `색상(hue)`, `크기(size)`, `모양(style)` 등 시각적 인코딩을 추가하여 범주형 또는 수치형 변수를 더 표현할 수 있습니다. 이를 통해 두 개를 초과하는 변수들의 관계를 동시에 파악하는 다변량 시각화가 가능해집니다.

### 코드/수식 해설

```python
import seaborn as sns
# Iris 데이터셋 로드 (seaborn에 내장되어 있음)
iris = sns.load_dataset("iris") 

# 산점도 생성 코드
sns.scatterplot(data=iris,
                x="petal length (cm)",
                y="petal width (cm)",
                hue="species",
                alpha=0.7)
```
*   `sns.scatterplot()`: `seaborn` 라이브러리에서 산점도를 그리는 함수입니다.
*   `data=iris`: 시각화에 사용할 데이터프레임으로, 여기서는 붓꽃(Iris) 데이터셋을 지정합니다.
*   `x="petal length (cm)"`: $x$축에 매핑할 변수를 지정합니다. 붓꽃의 꽃잎 길이(petal length)를 나타냅니다.
*   `y="petal width (cm)"`: $y$축에 매핑할 변수를 지정합니다. 붓꽃의 꽃잎 너비(petal width)를 나타냅니다.
*   `hue="species"`: `species` 변수(붓꽃의 종, 범주형)를 점의 `색상` 인코딩에 사용합니다. 이 인자를 통해 각 종별로 다른 색상의 점이 그려져 시각적으로 구분됩니다.
*   `alpha=0.7`: 점의 투명도를 설정합니다. $0$ (완전 투명)부터 $1$ (완전 불투명) 사이의 값을 가지며, 점들이 겹쳐 있을 때 밀집도를 파악하기 용이하고 오버플롯을 줄이는 데 도움이 됩니다.

### 구체적 예시
제공된 슬라이드의 예시는 `Iris` 데이터셋을 사용하여 붓꽃의 `꽃잎 길이(petal length)`와 `꽃잎 너비(petal width)` 간의 관계를 산점도로 시각화하고 있습니다.
*   $x$축은 꽃잎 길이, $y$축은 꽃잎 너비를 나타냅니다.
*   `hue="species"` 인자로 인해, 세 가지 붓꽃 종(`setosa`, `versicolor`, `virginica`)이 각각 주황색, 파란색, 녹색으로 구분되어 표시됩니다.
*   결과 그래프에서 `setosa` 종은 다른 두 종에 비해 꽃잎 길이가 짧고 너비도 좁은 영역에 집중되어 뚜렷하게 군집을 형성하는 것을 볼 수 있습니다. `versicolor`와 `virginica`는 꽃잎 크기가 더 크지만, 이 두 종 역시 특정 영역에 분포하여 구분되는 경향을 보입니다. 이처럼 산점도를 통해 여러 변수 간의 복합적인 관계와 데이터의 분포 특성을 한눈에 파악할 수 있습니다.

### 강의 내용
교수님께서는 산점도를 "가장 중요하고 기본적인(fundamental and simple)" 플롯이라고 강조하셨습니다.
*   "모든 관측치 $ (x_i, y_i) $에 대해 하나의 점을 배치한다"는 기본 원리를 설명하셨습니다.
*   산점도의 진정한 "힘(power)"은 "더 많은 인코딩(more encodings)"을 추가하는 데서 온다고 강조하셨습니다. 이는 단순히 두 변수만 시각화하는 것을 넘어, 범주형 변수를 `색상(hue)`으로, 수치형 변수를 `크기(size)`로, 또 다른 범주형 변수를 `스타일/모양(style)` 등으로 매핑하여 다차원 정보를 하나의 그래프에 담을 수 있음을 의미합니다.

### 시험 포인트
*   ⭐**산점도의 기본 용도**: 두 수치형 변수 간의 관계(패턴, 상관관계, 군집)를 시각적으로 파악하는 데 사용됩니다.
*   ⭐**다변량 시각화를 위한 인코딩**: `hue` (색상), `size` (크기), `style` (모양/스타일)과 같은 인자를 사용하여 산점도에 2개 이상의 변수 정보를 추가할 수 있다는 점을 이해하고 설명할 수 있어야 합니다.
*   ⭐`seaborn.scatterplot()` 함수의 주요 인자들 (`data`, `x`, `y`, `hue`, `alpha`)의 역할과 사용법을 정확히 알아두세요.
*   주어진 Iris 데이터셋 예시에서 각 `species`가 꽃잎 길이와 너비에 따라 어떻게 시각적으로 구분되는지 해석할 수 있어야 합니다. 이는 데이터 분석 결과 해석 능력의 기초가 됩니다.

---
## Slide 5

**핵심 개념**:
이 슬라이드는 **선 그래프(Line Plot)**의 정의, 사용 시점, 해석 방법 및 주의사항을 다룹니다. 선 그래프는 주로 $x$축에 순서(ordered $x$)가 있는 데이터를 시각화하여 변화의 추세나 패턴을 파악하는 데 사용됩니다.

*   **정의**: 시간(time)이나 용량(dose)과 같이 순서가 있는 $x$축을 따라 관측값들을 연결하여 데이터를 표현합니다. 연속적인 데이터 흐름을 보여주는 데 적합합니다.
*   **사용 시점**:
    *   시간에 따른 추세(Trends over time) 변화를 파악할 때 (예: 주가, 기온, 인구 변화).
    *   데이터의 진화 곡선(evolution curves)을 나타낼 때.
    *   불확실성 대역(uncertainty bands)을 포함한 평균값을 보여줄 때 (예: 신뢰구간).
*   **해석 방법**:
    *   **기울기(Slope)**: 데이터의 변화율(rate of change)을 나타냅니다. 기울기가 가파르면 변화 속도가 빠름을 의미합니다.
    *   **곡률(Curvature)**: 변화의 가속도(acceleration)를 나타냅니다. 곡선이 위로 볼록하거나 아래로 볼록한 정도를 통해 변화 속도의 변화를 파악합니다.
    *   **신뢰구간(CI, Confidence Interval) 대역의 폭**: 데이터의 안정성(stability) 또는 예측의 불확실성을 나타냅니다. 대역의 폭이 좁을수록 안정성이 높거나 불확실성이 낮음을 의미합니다.
*   **주의사항(Pitfalls)**:
    *   **순서가 없는 범주형 데이터는 연결하지 마세요.** 선으로 연결하는 행위 자체가 순서 관계를 가정하므로, 의미 없는 순서가 부여될 수 있습니다.
    *   **샘플링 간격이 일정하지 않을 경우** 시각화 해석에 주의해야 합니다. 불규칙한 간격은 실제 변화율을 왜곡하여 보여줄 수 있습니다.

**코드/수식 해설**:
선 그래프는 `matplotlib`와 같은 라이브러리를 사용하여 쉽게 그릴 수 있습니다. 특히 시계열 데이터를 다룰 때 유용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 가상의 시간 데이터 (x축)
time_points = np.arange(0, 10, 1)
# 가상의 측정 데이터 (y축, 시간에 따라 변화하는 값)
measured_values = np.sin(time_points / 2) * 5 + time_points + np.random.randn(len(time_points)) * 0.5

plt.figure(figsize=(10, 6))
plt.plot(time_points, measured_values, marker='o', linestyle='-', color='purple', label='Measured Value')
plt.title('Time-Series Data Visualization with Line Plot')
plt.xlabel('Time (Units)')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()
```

기울기는 두 연속된 데이터 포인트 $ (x_i, y_i) $와 $ (x_{i+1}, y_{i+1}) $ 사이의 변화율로 계산할 수 있습니다:
$$ \text{Slope} = \frac{\Delta y}{\Delta x} = \frac{y_{i+1} - y_i}{x_{i+1} - x_i} $$

**구체적 예시**:
*   **COVID-19 확진자 수 변화**: 매일 발표되는 신규 확진자 수를 날짜(시간)를 $x$축으로, 확진자 수를 $y$축으로 하여 선 그래프를 그리면 확산 추세(기울기)와 방역 정책의 효과(곡률 변화)를 시각적으로 파악할 수 있습니다.
*   **식물 성장 일지**: 식물의 키나 잎의 개수를 매주 측정하여 선 그래프로 나타내면 성장 속도(기울기)와 성장 패턴을 이해하는 데 도움이 됩니다.

**강의 내용**:
교수님께서는 이 슬라이드에 앞서 다변량 데이터 처리 방식에 대해 언급하며, **산점도(scatter plot)**를 이용해 두 **수치형 변수(numerical variables)** 간의 관계를 탐색하는 방법을 설명하셨습니다.
*   산점도를 분석할 때 주로 **기울기(slope)**와 **점 구름(point cloud)의 형태**를 주목해야 한다고 강조하셨습니다.
*   점들이 빽빽하게 띠를 이루는(tight band of points) 형태는 변수 간의 **강한 관계**를 시사하며, 점들이 넓게 퍼져 있는(diffuse cloud) 형태는 **약한 관계**를 의미합니다.
*   특히, 대규모 데이터셋(large data set)에서 산점도를 그릴 때 발생하는 주요 문제점으로 **오버플로팅(over-plotting)**을 지적하셨습니다. 오버플로팅은 너무 많은 점이 겹쳐 찍혀 데이터의 실제 분포나 관계를 제대로 파악하기 어렵게 만드는 현상입니다. 이는 투명도를 조절하거나, 샘플링 또는 핵밀도 추정(Kernel Density Estimation)과 같은 기법으로 완화할 수 있습니다.

**시험 포인트**:
*   ⭐ **선 그래프의 핵심 용도**: $x$축이 시간, 순서, 용량과 같이 순서가 있는 데이터의 추세나 변화율을 시각화할 때.
*   ⭐ **선 그래프 해석의 주요 요소**: 기울기(변화율), 곡률(가속도), 신뢰구간 대역의 폭(안정성/불확실성).
*   ⭐ **선 그래프 사용 시 반드시 피해야 할 경우**: $x$축에 순서가 없는 범주형 데이터를 연결하여 시각화하는 것.
*   ⭐ **(강의 내용 관련) 산점도 사용 시 대규모 데이터셋에서 발생하는 주요 문제점**: 오버플로팅 (over-plotting) 및 그 의미.

---
## Slide 6

---
### **핵심 개념**: 시계열 데이터 시각화와 신뢰 구간 (CI) 및 산점도 과밀화 문제

이 슬라이드는 주로 Seaborn 라이브러리를 사용하여 시계열 데이터를 시각화하는 `sns.lineplot`의 활용법과 데이터 생성 과정을 다룹니다. 특히, 여러 그룹의 시간에 따른 변화 추이를 보여주고, 데이터의 불확실성을 나타내는 신뢰 구간(Confidence Interval, CI)을 포함하는 방법을 강조합니다.

강의 음성에서는 대규모 산점도(scatter plot)에서 발생하는 과밀화(overplotting) 문제와 이를 해결하기 위한 투명도(`alpha`) 설정 및 `hue` 파라미터로 범주형 변수를 색상으로 인코딩하는 방법에 대해 설명합니다. 이는 다양한 시각화 기법이 각기 다른 데이터 특성 및 문제 상황에 어떻게 적용될 수 있는지를 보여줍니다.

### **코드/수식 해설**:

슬라이드의 코드는 두 부분으로 나뉩니다: 데이터 생성과 시각화.

```python
# Build df_long with repeated measures per time & group
rng = np.random.default_rng(42) # 재현 가능한 난수 생성기 설정
T, n_rep = 100, 30 # 시간(T) 100 스텝, 반복 횟수(n_rep) 30
time = np.arange(T) # 0부터 T-1까지의 시간 배열 생성
rows = []
for g, base, slope in [("A", 0.0, 0.03), ("B", 0.3, 0.02)]: # 두 그룹 (A, B) 설정
    for r in range(n_rep): # 각 그룹별로 n_rep만큼 반복
        # y 값 생성: 기본값 + 기울기 * 시간 + 사인파 + 정규 분포 노이즈
        y = base + slope*time + 0.4*np.sin(time/7.5) + rng.normal(0,0.15,T)
        rows.append(pd.DataFrame({"time":time, "value":y, "group":g, "rep":r}))
df_long = pd.concat(rows, ignore_index=True) # 생성된 데이터를 하나의 DataFrame으로 결합

sns.lineplot(data=df_long, x="time", y="value", hue="group", errorbar=("ci", 95))
```

1.  **데이터 생성 (`df_long`)**:
    *   `rng = np.random.default_rng(42)`: `np.random.default_rng()`을 사용하여 재현 가능한 난수 생성을 위한 시드를 42로 설정합니다.
    *   `T = 100`, `n_rep = 30`: `time` 축의 길이는 100, 각 그룹과 각 시간 스텝에 대해 30번의 반복 측정(repeated measures)을 수행합니다.
    *   `time = np.arange(T)`: 0부터 99까지의 정수 배열을 생성하여 시간 `t`를 나타냅니다.
    *   두 개의 그룹("A", "B")이 정의되며, 각 그룹은 서로 다른 `base` 값과 `slope` 값을 가집니다.
    *   중첩 루프를 통해 각 그룹(`g`)과 각 반복 측정(`r`)에 대해 `y` 값을 계산합니다.
    *   `y` 값은 다음과 같은 수식으로 생성됩니다:
        $$ y = \text{base} + \text{slope} \times \text{time} + 0.4 \times \sin(\text{time}/7.5) + \mathcal{N}(0, 0.15, \text{T}) $$
        여기서 `base`는 초기 값, `slope`는 시간에 따른 선형 증가 기울기, $0.4 \times \sin(\text{time}/7.5)$는 주기적인 패턴(사인파)을 추가하며, $\mathcal{N}(0, 0.15, \text{T})$는 평균이 0이고 표준편차가 0.15인 정규 분포에서 추출된 `T`개의 난수(노이즈)를 의미합니다. 이 노이즈는 데이터의 자연스러운 변동성을 모사합니다.
    *   생성된 `time`, `y`, `group`, `rep` 값을 `pd.DataFrame`으로 만들어 `rows` 리스트에 추가합니다.
    *   `df_long = pd.concat(rows, ignore_index=True)`: 모든 개별 DataFrame을 하나의 긴 형식(long format) DataFrame인 `df_long`으로 합칩니다.
2.  **시각화 (`sns.lineplot`)**:
    *   `sns.lineplot(data=df_long, x="time", y="value", hue="group", errorbar=("ci", 95))`: Seaborn의 `lineplot` 함수를 사용하여 선 그래프를 그립니다.
        *   `data=df_long`: 사용할 데이터프레임.
        *   `x="time"`: x축에 `time` 열의 값을 매핑.
        *   `y="value"`: y축에 `value` 열의 값을 매핑.
        *   `hue="group"`: `group` 열의 고유 값(예: "A", "B")에 따라 선의 색상을 다르게 설정하여 그룹별 추세를 구분.
        *   `errorbar=("ci", 95)`: 각 시간 스텝에서 `value`의 95% 신뢰 구간(confidence interval)을 음영 처리된 영역으로 표시합니다. 이는 데이터의 평균 주위에 불확실성 범위를 시각적으로 나타냅니다.

### **구체적 예시**:

*   **라인 플롯 예시 (슬라이드 내용 기반)**: 슬라이드 하단의 그래프는 "group A"와 "group B"라는 두 그룹의 시간에 따른 `value` 변화를 보여줍니다. 각 그룹은 시간에 따라 증가하는 추세와 주기적인 패턴을 보이며, 두 그룹의 추세선 주위에 옅은 색의 영역이 95% 신뢰 구간을 나타냅니다. 이를 통해 단순히 평균선만 보는 것이 아니라, 각 시점에서의 데이터 분포의 불확실성을 함께 파악할 수 있습니다. 예를 들어, 어떤 신약의 효과를 A그룹(대조군)과 B그룹(실험군)으로 나누어 시간에 따라 측정했을 때, 이러한 라인 플롯으로 신약 효과의 변화 추이와 통계적 유의미성(신뢰 구간이 겹치는지 여부 등)을 시각적으로 분석할 수 있습니다.
*   **산점도 예시 (강의 음성 기반)**: 만약 붓꽃(Iris) 데이터셋을 `sns.scatterplot`으로 시각화한다고 가정해 봅시다.
    ```python
    # (Iris 데이터 로드 가정)
    # import seaborn as sns
    # iris = sns.load_dataset("iris")
    # sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species", alpha=0.7)
    ```
    이 코드는 `sepal_length`를 x축에, `sepal_width`를 y축에 놓고, `species` (setosa, versicolor, virginica)에 따라 점의 색깔을 다르게 합니다. `alpha=0.7`은 각 점에 70%의 투명도를 적용하여, 겹쳐 있는 점들이 더 어둡게 보이면서 데이터의 밀집도를 시각적으로 파악할 수 있게 돕습니다.

### **강의 내용**:

교수님은 대규모 데이터를 단일 산점도에 그릴 때 발생하는 문제점을 먼저 언급합니다. 수백만 개의 점을 하나의 산점도에 그리면 점들이 너무 많이 겹쳐서 데이터의 패턴을 파악하기 어려워지는 "과밀화(overplotting)" 문제가 발생할 수 있습니다. 투명도(`alpha`)를 사용해도 모든 경우에 충분히 도움이 되지 않을 수 있으며, 이런 경우 밀도 플롯(density plot)과 같은 다른 시각화 방법을 고려할 수 있다고 설명합니다.

이어지는 설명에서 교수님은 Seaborn의 `scatterplot` API에 대한 구체적인 예시를 들었습니다. (현재 슬라이드의 이미지와는 다르게) "fatal length"를 x축에, "fatal width"를 y축에 매핑하는 산점도를 예로 들며, `hue` 파라미터의 중요성을 강조합니다. `hue`를 "species"로 설정하면 각 점이 붓꽃의 세 가지 종(species) 중 어느 것에 속하는지에 따라 색상이 다르게 인코딩되어, 종별 특징을 시각적으로 구분할 수 있게 됩니다. 또한, `alpha=0.7`을 설정하여 부분적인 투명도를 적용함으로써 겹치는 점들을 좀 더 명확하게 볼 수 있다고 설명합니다.

### **시험 포인트**:

*   ⭐ `sns.lineplot`에서 `hue` 파라미터가 어떤 역할을 하는지 (그룹별 시각화) 정확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ `errorbar=("ci", 95)`와 같이 신뢰 구간(Confidence Interval, CI)을 시각화하는 방법과, 95% CI가 무엇을 의미하는지 (반복 측정 시 참 평균이 해당 구간에 있을 확률 95%) 설명할 수 있어야 합니다.
*   ⭐ 산점도(scatter plot)에서 발생하는 과밀화(overplotting) 문제와 이를 해결하기 위한 방법들(예: `alpha`를 이용한 투명도 조절, 밀도 플롯)을 설명할 수 있어야 합니다. (강의 음성 내용)
*   ⭐ `hue` 파라미터가 산점도뿐만 아니라 다른 Seaborn 플롯에서도 범주형 변수를 색상으로 인코딩하여 그룹을 구분하는 데 활용될 수 있음을 이해해야 합니다. (강의 음성 내용)
*   ⭐ 주어진 코드처럼 시계열 데이터 또는 반복 측정 데이터를 생성하는 기본적인 Python/Pandas/NumPy 로직을 이해하는 것이 중요합니다.
---

---

## Slide 7

## 회귀분석 (OLS/LOESS) — 정의 및 활용법

### 핵심 개념
이 슬라이드는 회귀분석의 두 가지 주요 방법인 OLS(Ordinary Least Squares)와 LOESS(Locally Estimated Scatterplot Smoothing)의 정의, 사용 시점, 해석 방법, 그리고 한계점을 다룹니다.

*   **OLS (Ordinary Least Squares)**: 가장 기본적인 선형 회귀 방법으로, 관측된 데이터의 종속 변수 $Y$와 독립 변수 $X$ 사이의 선형 관계를 모델링합니다. 잔차(실제 값과 예측 값의 차이) 제곱의 합을 최소화하는 방식으로 최적의 회귀 계수를 추정합니다.
*   **LOESS (Locally Estimated Scatterplot Smoothing)**: 비모수적 회귀 방법으로, 데이터의 국소적인(locally) 부분에 가중치를 두어 다항식을 피팅하여 전역적인 선형 관계가 아닌 비선형적인 패턴이나 트렌드를 부드럽게(smoother) 추정합니다.

### 코드/수식 해설
*   **OLS 정의**:
    OLS는 조건부 기댓값 $E[Y|X]$를 독립 변수 $X$에 대한 선형 함수로 모델링합니다.
    $$E[Y|X] = \beta_0 + \beta_1 X$$
    여기서 $Y$는 종속 변수(예측하려는 값), $X$는 독립 변수(예측에 사용하는 값), $\beta_0$는 절편, $\beta_1$은 기울기를 나타내는 회귀 계수입니다. OLS는 이 $\beta_0$와 $\beta_1$을 추정하여 $Y$와 $X$ 사이의 최적의 선형 관계를 찾습니다.

*   **LOESS 정의**:
    LOESS는 특정한 수식으로 직접 표현하기보다는, 각 데이터 포인트 주변의 국소적인 데이터에 가중치를 부여하여 다항 회귀를 수행하고 이를 연결하여 부드러운 곡선을 생성하는 알고리즘입니다. 'locally weighted smoother'라는 표현에서 알 수 있듯이, 데이터의 전역적인(global) 패턴보다는 부분적인(local) 패턴을 강조합니다.

### 구체적 예시
*   **OLS 예시**:
    학생들의 공부 시간($X$)이 시험 점수($Y$)에 미치는 영향을 분석할 때 OLS를 사용할 수 있습니다. 만약 공부 시간이 늘어날수록 시험 점수가 대체로 선형적으로 증가한다면, OLS는 "공부 시간 1시간 증가당 시험 점수 N점 증가"와 같은 명확한 선형 관계를 제공합니다.
*   **LOESS 예시**:
    특정 지역의 월별 평균 기온 변화를 분석할 때 LOESS를 사용할 수 있습니다. 기온은 계절에 따라 비선형적인 패턴을 보일 수 있으며, LOESS는 이러한 계절적 추세나 단기적인 비선형 변동을 부드러운 곡선 형태로 시각화하여 보여줄 수 있습니다. 예를 들어, 특정 월에 이상 기온이 발생했더라도 LOESS는 국소적인 평균을 반영하여 전체적인 추세를 크게 왜곡하지 않으면서 이상점을 걸러낼 수 있습니다.

### 강의 내용
교수님께서는 이 슬라이드에 앞서 또는 이 슬라이드와 연관하여 데이터의 시각적 탐색의 중요성을 강조하신 것으로 보입니다. "And if this plot was all one color. we will be seeing a strong single positive relationship." 부분은 전체 데이터에서 단일한 강한 양의 상관관계를 볼 수 있음을 의미하며, 이는 OLS와 같은 선형 모델로 포착될 수 있는 특징입니다.

하지만 이어서 "But with hue, I mean we can see more richer kind of relationship and see that the setosa So those are species on a tight and completely separable cluster at the bottom left. and also the other two are also very distinctive from each other with the"라는 말씀은 데이터를 'hue'(색상)를 통해 그룹별로 시각화했을 때(예: 붓꽃(Iris) 데이터셋에서 종(species)별로 색상을 다르게 표시했을 때), 각 그룹(예: setosa 종)이 완전히 분리되는 독특한 군집(cluster)을 형성하며 서로 다른 관계를 보인다는 점을 설명하고 있습니다. 이는 단순한 하나의 OLS 선형 모델로는 전체 데이터의 복잡한 관계를 충분히 설명하기 어려울 수 있음을 시사합니다. 각 그룹별로 다른 회귀 관계가 존재하거나, 비선형적인 관계가 있을 수 있음을 시각적으로 확인하는 것이 중요함을 강조하는 부분입니다. 이러한 통찰은 단일 OLS 모델 대신 LOESS와 같이 국소적인 패턴을 따르는 모델을 고려하거나, 그룹별로 별도의 OLS 모델을 적용하는 등의 전략을 세우는 데 필수적인 기반이 됩니다.

### 시험 포인트
*   **OLS와 LOESS의 차이점**: OLS는 선형 관계를, LOESS는 비선형적인 국소적 트렌드를 추정합니다. ⭐
*   **OLS 사용 시기**: 중앙 추세 요약, 그룹별 기울기 비교 등에 사용.
*   **LOESS 사용 시기**: 데이터에 명확한 선형 관계가 없거나, 국소적인 패턴을 보고 싶을 때 유용합니다.
*   **회귀 분석 결과 해석 방법**:
    *   ⭐**기울기($\beta_1$)의 부호 및 크기**: 독립 변수 $X$가 종속 변수 $Y$에 미치는 영향의 방향(양의/음의)과 강도를 나타냅니다.
    *   **신뢰 구간 (CI envelope)**: 추정된 관계에 대한 불확실성 범위를 보여줍니다.
    *   **잔차 진단 (residual diagnostics)**: 모델의 적합성(fit quality)을 평가하는 데 사용됩니다.
*   **각 방법의 한계 (Pitfalls)**:
    *   ⭐**OLS는 이상치(outliers)에 매우 민감합니다.** 이상치가 있을 경우 회귀선이 크게 왜곡될 수 있습니다.
    *   ⭐**LOESS는 대역폭(bandwidth) 매개변수에 의해 부드러움(smoothness)이 제어됩니다.** 대역폭이 너무 작으면 과적합(overfitting)될 수 있고, 너무 크면 지나치게 평활(oversmoothing)되어 중요한 패턴을 놓칠 수 있습니다. 대역폭 선택은 LOESS의 성능에 결정적인 영향을 미칩니다.

---
## Slide 8

**핵심 개념**:
*   **회귀 분석 시각화 (Regression Visualization)**: 두 연속형 변수 간의 관계를 파악하고 시각적으로 모델을 적합시키는 방법입니다. 주로 `sns.regplot`과 `sns.lmplot`을 사용합니다.
*   **`sns.regplot`**: 산점도(scatter plot) 위에 선형 회귀선과 신뢰구간(confidence interval)을 함께 그리는 기본적인 회귀 플롯입니다.
*   **`sns.lmplot`**: `regplot`과 유사하게 선형 모델을 적합하지만, Faceting Grid를 지원하여 여러 서브플롯을 만들 수 있는 유연성을 제공합니다. 또한 `lowess` 파라미터를 통해 비선형적인 국소 평활화(Local Smoothing) 모델을 시각화할 수 있습니다.
*   **LOWESS (Locally Weighted Scatterplot Smoothing)**: 데이터의 국소적인 부분에 가중치를 두어 여러 개의 작은 회귀 모델을 만들고 이를 연결하여 부드러운 곡선을 생성하는 비모수적 회귀 방법입니다.

**코드/수식 해설**:
*   **기본 선형 회귀 플롯**:
    ```python
    sns.regplot(data=wine, x="alcohol", y="color_intensity")
    ```
    이 코드는 `wine` 데이터셋의 `alcohol` 컬럼을 x축으로, `color_intensity` 컬럼을 y축으로 하는 산점도를 그리고, 그 위에 OLS(Ordinary Least Squares) 방법을 이용한 선형 회귀선을 적합하여 함께 시각화합니다. 기본적으로 회귀선 주위에 95% 신뢰구간도 함께 표시됩니다.

*   **국소 평활화(Local Smoother) 플롯**:
    ```python
    # Local smoother
    sns.lmplot(data=wine, x="alcohol", y="color_intensity", lowess=True)
    ```
    이 코드는 `regplot`과 동일하게 `alcohol`과 `color_intensity` 간의 관계를 시각화하지만, `lowess=True` 옵션을 사용하여 데이터를 국소적으로 평활화한 비선형 회귀선을 그립니다. 이는 전역적인 선형 관계보다는 데이터의 지역적인 추세를 더 잘 반영하는 부드러운 곡선을 제공합니다. `lmplot`은 내부적으로 `regplot`을 사용하며, `lowess`를 포함한 다양한 옵션을 통해 더욱 유연한 시각화를 가능하게 합니다.

**구체적 예시**:
슬라이드에 첨부된 그래프는 와인 데이터에서 알코올 함량(`alcohol`)과 색상 강도(`color_intensity`) 사이의 관계를 보여줍니다. 각 'X' 표시는 개별 와인 샘플의 데이터 포인트이며, 주황색 직선은 이 데이터 포인트들을 가장 잘 설명하는 선형 회귀선입니다. 이 그래프를 통해 알코올 함량이 증가할수록 색상 강도도 증가하는 경향이 있음을 시각적으로 확인할 수 있습니다. 만약 `lowess=True` 옵션을 사용했다면, 이 직선 대신 데이터의 분포를 더 부드럽게 따라가는 곡선이 그려져 비선형적인 관계나 특정 구간에서의 변화를 더 잘 보여줄 수 있었을 것입니다.

**강의 내용**:
교수님은 슬라이드의 내용(회귀 플롯)과는 다소 다른 시각화 유형에 대해 설명하셨습니다.
*   이전 슬라이드나 내용에서 `hue` 파라미터를 사용하여 종(species)별로 데이터를 구분한 산점도에 대한 논의가 있었던 것으로 보입니다 (예: Virginica 품종의 `peitar length`와 `peitar width` 비교).
*   이어서 교수님은 **라인 플롯(line plot)**에 대해 설명하며, 라인 플롯이 산점도(scatter plot)와 종종 혼동되지만 근본적으로 다르다고 강조했습니다.
*   라인 플롯의 핵심은 "관측값을 **순서대로(in order)** 연결한다"는 점입니다.
*   특히, x축이 **정렬된(ordered)** 데이터를 가져야 한다고 여러 번 강조했습니다.
*   정렬된 x축의 예시로는 시간(`time`), 일(`days`), 월(`months`), 연도(`years`) 등 자연스럽고 논리적인 순서를 갖는 데이터를 들었습니다.
*   라인 플롯은 주로 시간에 따른 트렌드(trends over time)를 시각화하는 데 표준적으로 사용된다고 설명했습니다.

**시험 포인트**:
*   ⭐ `sns.regplot`과 `sns.lmplot`의 사용 목적 및 기본 파라미터(특히 `x`, `y`, `data`)를 이해하고 활용할 수 있는가?
*   ⭐ `lowess=True` 옵션이 `lmplot`에서 어떤 역할을 하며, 어떤 종류의 회귀선을 그리는지 설명할 수 있는가? (선형 vs. 국소 평활화)
*   ⭐ **(강의 내용 강조)** 라인 플롯(Line plot)과 산점도(Scatter plot)의 근본적인 차이점은 무엇이며, 라인 플롯에서 x축의 '순서(ordered)'가 왜 중요한지 설명할 수 있는가?
*   ⭐ **(강의 내용 강조)** 라인 플롯이 특히 효과적인 데이터 유형(예: 시계열 데이터)과 시각화 목적(예: 시간에 따른 트렌드)을 알고 있는가?

---
## Slide 9

**핵심 개념**:
*   **`relplot` 정의**: `relplot`은 `seaborn` 라이브러리에서 제공하는 Figure-level 함수로, `scatterplot` (산점도)과 `lineplot` (선 그래프)을 아우르는 상위 래퍼 함수입니다. `FacetGrid` 기능을 내장하여 `row` 또는 `col` 인자를 통해 데이터를 서브그룹으로 분할하고, 각각의 서브플롯(small multiples)에 일관된 크기와 범례로 시각화를 생성할 수 있습니다.
*   **주요 기능**: `kind` 인자를 `"scatter"` (산점도) 또는 `"line"` (선 그래프)로 지정하여 두 변수 간의 관계를 시각화합니다. 다양한 그룹별로 데이터의 관계를 한 번에 비교할 때 매우 유용합니다.

**코드/수식 해설**:
*   **`relplot` 기본 구조**:
    `relplot`은 `x`, `y`축에 매핑할 데이터 외에 `kind`, `data`, 그리고 `row`, `col`, `hue`, `style`, `size`와 같은 인자를 통해 여러 차원의 데이터를 효과적으로 시각화할 수 있습니다.
    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt

    # 예시 데이터 로드
    tips = sns.load_dataset("tips")

    # relplot 사용 예시: 요일별, 시간대별 팁과 총 지불액의 관계를 선 그래프로 시각화
    # col="time"은 'time' 컬럼의 고유 값별로 열을 나누고,
    # row="smoker"는 'smoker' 컬럼의 고유 값별로 행을 나눕니다.
    # hue="day"는 'day' 컬럼의 고유 값별로 선의 색상을 다르게 합니다.
    # kind="line"은 선 그래프를 생성합니다.
    sns.relplot(
        x="total_bill", y="tip",
        col="time", row="smoker",
        hue="day", kind="line",
        data=tips
    )
    plt.title("Tip vs Total Bill by Time, Smoker, and Day")
    plt.tight_layout() # 그래프 레이아웃 조정
    plt.show()
    ```
*   **불확실성 구간 (Confidence Interval)**: 선 그래프에서 주로 나타나는 음영 처리된 영역으로, 추정치(예: 평균)의 신뢰도를 나타냅니다. 예를 들어, 95% 신뢰 구간은 이 구간 안에 실제 모수 값이 존재할 확률이 95%임을 의미합니다. 수학적으로는 평균($\mu$)과 표준 오차(SE)를 이용하여 $\mu \pm z^* \cdot \text{SE}$ 또는 $\mu \pm t^* \cdot \text{SE}$와 같이 표현될 수 있습니다.

**구체적 예시**:
*   **시계열 데이터 분석**: 주식 가격 변동, 웹사이트 사용자 트래픽, 센서 데이터 등 시간에 따라 변화하는 데이터의 추세를 시각화할 때 `kind="line"`으로 `relplot`을 활용합니다. 예를 들어, 여러 지역별(facet) 웹사이트 트래픽(y축) 변화를 시간(x축)에 따라 보여주어, 각 지역의 트렌드를 동시에 비교할 수 있습니다.
*   **실험 결과 비교**: 다른 실험 조건(예: 약물 투여량)에 따른 피실험자의 측정값(예: 혈압) 변화를 시간에 따라 추적할 때 `relplot`을 사용합니다. 각 조건별로 그래프를 나누어(facet) 보여주면, 어떤 조건이 가장 효과적인지 시각적으로 쉽게 파악할 수 있습니다. 이때 불확실성 구간을 통해 각 추정치의 신뢰도도 함께 고려할 수 있습니다.

**강의 내용**:
*   교수님은 `relplot`이 **주식 가격, 웹사이트 트래픽, 실험 데이터**와 같이 **시간이나 순서가 있는 데이터**의 변화 추이를 시각화하는 데 매우 효과적이라고 강조하셨습니다.
*   주로 **평균 트렌드(mean trend)**를 시각화하며, 트렌드 주변에 나타나는 **음영 처리된 불확실성 구간(shaded uncertainty band)**은 추정치의 **안정성(stability)** 또는 **확실성(certainty)**을 나타낸다고 설명하셨습니다. 이 구간이 좁을수록 추정치가 더 신뢰할 수 있다는 의미입니다.
*   그래프를 읽는 방법과 관련하여:
    *   **기울기(slope)**: 데이터의 **변화율(rate of change)**을 보여줍니다. 기울기가 가파르면 변화율이 크고, 평평하면 변화율이 작다는 의미입니다.
    *   **곡률(curvature)**: **가속도(acceleration)**를 나타냅니다. 기울기의 변화율, 즉 변화의 속도가 얼마나 빨라지는지(또는 느려지는지)를 파악할 수 있습니다.
*   ⭐**가장 흔한 실수**: **순서가 없는(unordered) 범주형 데이터를 선으로 연결하는 것**은 잘못된 시각화라고 강력히 경고하셨습니다. 선 그래프는 데이터 포인트 간에 의미 있는 순서나 연속성이 있을 때만 사용해야 합니다.

**시험 포인트**:
*   ⭐`relplot`이 `scatterplot`과 `lineplot`의 상위 **Figure-level wrapper**이며, `FacetGrid`를 통해 `row`와 `col` 인자로 **서브그룹별 시각화(small multiples)**를 지원한다는 점을 이해해야 합니다.
*   ⭐`kind` 인자를 `"scatter"` 또는 `"line"`으로 설정하여 생성되는 그래프의 종류와 각 그래프가 적합한 데이터 유형 및 해석 방법을 구분할 수 있어야 합니다.
*   ⭐선 그래프에서 **기울기(rate of change)**, **곡률(acceleration)**, **불확실성 구간(stability/certainty)**이 각각 무엇을 의미하고 어떻게 해석해야 하는지 설명할 수 있어야 합니다.
*   ⭐선 그래프 사용 시 **순서가 없는 범주형 데이터**를 연결하는 것이 왜 **시각화의 오류**가 되는지 설명할 수 있어야 합니다. 이는 강의에서 특히 강조된 중요한 실수입니다.

---
## Slide 10

### **핵심 개념**

*   **`seaborn.relplot`**: `seaborn` 라이브러리에서 관계형 플롯(relational plots)을 그리는 데 사용되는 figure-level 함수입니다. `kind` 파라미터를 통해 산점도(scatter plot) 또는 선 그래프(line plot)를 그릴 수 있습니다.
*   **산점도(Scatter Plot)**: 두 연속형 변수 간의 관계를 점들을 사용하여 시각화하는 데 적합합니다. 각 점은 데이터셋의 한 관측치를 나타냅니다.
*   **패싯팅(Faceting) 또는 조건부 서브플롯**: 데이터셋의 범주형 변수를 기준으로 여러 개의 작은 서브플롯을 생성하는 기법입니다. 각 서브플롯은 특정 범주의 데이터를 보여주며, 여러 그룹 간의 패턴을 쉽게 비교할 수 있도록 돕습니다. 본 슬라이드에서는 붓꽃(Iris) 품종(`species`)별로 꽃받침 길이와 너비의 관계를 별도의 서브플롯으로 보여줍니다.

### **코드/수식 해설**

아래 코드는 `seaborn.relplot`을 사용하여 붓꽃(Iris) 데이터셋의 `sepal length (cm)`와 `sepal width (cm)` 간의 산점도를 그립니다. 이때, `species` 변수를 기준으로 패싯팅(분할)하고, 점의 색상도 `species`에 따라 다르게 지정합니다.

```python
sns.relplot(
    data=iris,
    x="sepal length (cm)",
    y="sepal width (cm)",
    hue="species",
    col="species",
    kind="scatter",
    col_wrap=3,
    height=3.0,
    aspect=1.05,
    alpha=0.75
)
```

*   `data=iris`: 시각화에 사용할 데이터프레임을 지정합니다. 여기서는 붓꽃 데이터셋을 사용합니다.
*   `x="sepal length (cm)"`: x축에 매핑할 컬럼을 지정합니다 (꽃받침 길이).
*   `y="sepal width (cm)"`: y축에 매핑할 컬럼을 지정합니다 (꽃받침 너비).
*   `hue="species"`: 점의 색상을 `species` 컬럼의 값에 따라 다르게 지정합니다. 이를 통해 각 품종을 시각적으로 구분할 수 있습니다.
*   `col="species"`: `species` 컬럼의 각 고유한 값에 따라 별도의 서브플롯(열)을 생성합니다. 이것이 패싯팅의 핵심적인 부분입니다.
*   `kind="scatter"`: 플롯의 종류를 산점도로 명시합니다. `relplot`은 `scatter` 또는 `line`을 지원합니다.
*   `col_wrap=3`: `col` 파라미터에 의해 생성된 서브플롯들을 한 줄에 최대 3개씩 배치하고 다음 줄로 넘어가도록 합니다. 여기서는 3가지 품종이므로 한 줄에 모두 배치됩니다.
*   `height=3.0`: 각 패싯(서브플롯)의 높이를 인치 단위로 지정합니다.
*   `aspect=1.05`: 각 패싯의 가로/세로 비율을 지정합니다 (`aspect = width / height`).
*   `alpha=0.75`: 점의 투명도를 설정합니다. 0 (완전 투명)에서 1 (완전 불투명) 사이의 값으로, 데이터 포인트가 겹칠 때 유용합니다.

### **구체적 예시**

슬라이드에 제시된 붓꽃 데이터 예시는 `relplot`의 강력한 시각화 기능을 잘 보여줍니다. `sepal length`와 `sepal width`의 관계를 단순히 하나의 산점도로 그리는 대신, `col="species"`를 통해 각 붓꽃 품종(`setosa`, `versicolor`, `virginica`)별로 별도의 서브플롯을 생성했습니다. 이처럼 패싯팅을 활용하면 각 품종 내에서의 특징적인 관계를 한눈에 비교할 수 있습니다. 예를 들어, `setosa`는 다른 두 품종에 비해 상대적으로 `sepal width`가 넓고 `sepal length`가 짧은 경향이 뚜렷하게 나타나는 것을 볼 수 있습니다.

교수님이 언급하신 라인 플롯 예시는 `relplot`의 또 다른 활용법을 설명합니다.
*   **부적절한 라인 플롯 사용 예**: "New York, London and Tokyo"와 같이 서로 독립적인 범주형 데이터를 선으로 연결하는 것은 논리적으로 타당하지 않습니다. 이러한 경우에는 각 범주의 값을 비교하는 막대 그래프(`bar chart`)가 더 적절합니다.
*   **적절한 라인 플롯 사용 예**: "synthetic time series data"의 경우처럼, 연속적인 시간(`time`) 흐름에 따른 값(`value`)의 변화를 시각화할 때 라인 플롯은 매우 유용합니다. "두 그룹 A, B에 대해 30회 반복, 100 타임 스텝" 데이터를 `x`축에 시간, `y`축에 값, `hue`에 그룹을 매핑하여 라인 플롯으로 그릴 수 있습니다. 이는 `sns.relplot(x='time', y='value', hue='group', kind='line', ...)`와 같은 방식으로 구현될 수 있습니다.

### **강의 내용**

교수님은 `relplot`이 제공하는 두 가지 주요 `kind`인 `scatter`와 `line` 중 특히 **라인 플롯의 올바른 사용법**에 대해 강조하셨습니다.

*   **라인 플롯 오용에 대한 경고**: "You must never use the line plot to connect data from New York, London and Tokyo." 이는 서로 연관성 없는 개별 범주형 데이터를 선으로 연결하는 것은 잘못된 시각적 해석을 유도할 수 있음을 강력히 경고한 것입니다. 이러한 경우 `bar chart`와 같은 다른 시각화 방식을 고려해야 합니다.
*   **라인 플롯의 적절한 사용 시기**: 라인 플롯은 `time series data`와 같이 **연속적인 순서가 있고, 그 순서에 따른 변화 추이를 보여줄 때** 사용해야 합니다.
*   **교수님의 라인 플롯 시연 예시**: 합성 시계열 데이터를 생성하여 이를 라인 플롯으로 시각화하는 과정을 설명하셨습니다.
    *   두 그룹 A와 B를 생성.
    *   각 그룹에 대해 30회 반복, 100 타임 스텝에 걸쳐 시뮬레이션된 데이터.
    *   `relplot`을 호출할 때 `time`을 `x`축에, `value`를 `y`축에, `group`을 `hue`에 매핑하여 사용. (여기서 `kind='line'`이 명시적으로 언급되지는 않았지만, 맥락상 라인 플롯임을 알 수 있습니다.)
*   이 슬라이드 이미지는 `kind="scatter"` 예시를 보여주고 있지만, 교수님의 강의 내용은 `relplot`의 또 다른 중요한 기능인 `kind="line"`의 올바른 활용법에 대한 일반적인 지침을 제공한 것으로 해석됩니다. `relplot`은 관계형 데이터를 시각화하는 포괄적인 함수이므로, 그 안에 포함된 여러 `kind`에 대한 이해가 중요합니다.

### **시험 포인트**

*   ⭐ **`seaborn.relplot`의 기능과 `kind` 파라미터(`scatter`, `line`)의 의미**: 각 `kind`가 어떤 종류의 데이터와 관계를 시각화하는 데 적합한지 명확히 이해해야 합니다.
*   ⭐ **라인 플롯의 올바른 사용과 오용 사례**:
    *   **오용**: "New York, London, Tokyo"와 같이 연속성이 없는 범주형 데이터를 연결하는 것은 잘못입니다. ⭐ 시험에서 이러한 오용 사례를 제시하고 올바른 대안(예: 막대 그래프)을 묻는 문제가 나올 수 있습니다.
    *   **올바른 사용**: 시계열 데이터와 같이 연속적인 변화 추이를 보여줄 때 사용합니다.
*   ⭐ **패싯팅(Faceting)의 개념과 활용**: `col`, `row`, `col_wrap`과 같은 파라미터를 사용하여 여러 범주형 그룹 간의 패턴을 비교하는 방법을 이해하고 실제 코드에 적용할 수 있어야 합니다. ⭐ 패싯팅이 왜 필요한지, 어떤 파라미터로 구현하는지 묻는 문제가 나올 수 있습니다.
*   ⭐ `relplot`의 주요 파라미터들(`data`, `x`, `y`, `hue`, `col`, `kind`, `height`, `aspect`, `alpha`) 각각의 역할과 기능.

---
## Slide 11

**핵심 개념**:
`seaborn.relplot`은 관계형 데이터를 시각화하는 유연한 함수로, 특히 `kind="line"`을 사용하여 시계열 데이터나 특정 변수에 대한 추이를 선 그래프로 나타낼 때 유용합니다. 이 슬라이드에서는 반복 측정(Repeated Measures) 데이터를 효과적으로 시각화하기 위해 각 시간 지점에서의 데이터 평균과 그 불확실성을 나타내는 신뢰 구간(Confidence Interval, CI)을 함께 표현하고, 여러 그룹의 데이터를 `faceting` 기법을 통해 분리하여 보여주는 방법을 다룹니다.

**코드/수식 해설**:
다음 Python 코드는 `seaborn` 라이브러리의 `relplot` 함수를 사용하여 반복 측정 데이터를 시각화합니다.

```python
sns.relplot(
    data=df_long,
    x="time", y="value",
    hue="group", col="group", col_wrap=2,
    kind="line", errorbar=("ci", 95),
    height=3.0, aspect=1.25
)
```
- `sns.relplot(...)`: `seaborn` 라이브러리의 관계형 플롯 함수를 호출합니다.
- `data=df_long`: 시각화에 사용할 데이터프레임입니다.
- `x="time"`, `y="value"`: x축에 `time` 컬럼을, y축에 `value` 컬럼을 매핑합니다.
- `hue="group"`: `group` 컬럼의 고유 값에 따라 색상을 다르게 합니다. (여기서는 `col="group"`으로 패싯이 분리되므로 주로 범례에 영향을 줍니다.)
- `col="group"`, `col_wrap=2`: `group` 컬럼의 고유 값에 따라 그래프를 열 방향으로 분리(faceting)하여 그립니다. `col_wrap=2`는 한 행에 최대 2개의 서브플롯을 배치하도록 합니다.
- `kind="line"`: 선 그래프(line plot)를 그리도록 지정합니다.
- `errorbar=("ci", 95)`: ⭐ 이 파라미터는 각 `x` 값에 대해 `y` 값의 통계적 요약(기본적으로 평균)과 함께 95% 신뢰 구간(Confidence Interval)을 음영 영역으로 표시하도록 지시합니다. 신뢰 구간은 기본적으로 부트스트랩(bootstrap) 방법을 통해 계산됩니다. 즉, $Y$ 값의 평균 $\bar{Y}$과 이에 대한 신뢰 구간을 보여줍니다.
- `height=3.0`, `aspect=1.25`: 각 서브플롯의 크기를 조절하는 파라미터입니다.

**구체적 예시**:
만약 특정 학습 프로그램의 효과를 평가하기 위해 두 그룹(Group A: 대조군, Group B: 실험군)에 대해 시간(time)에 따른 학습 성과(value)를 반복적으로 측정했다고 가정해봅시다. 각 그룹에서 30명의 학생이 참여했고, 각 학생의 성과가 시간에 따라 기록되었습니다.
이때 `sns.relplot` 함수를 사용하면, 각 그룹에 대한 30명의 학생 개개인의 성과 라인 30개를 모두 그리는 대신, 각 그룹 내 30명 학생의 평균 학습 성과 추이를 실선으로 나타내고, 그 평균의 95% 신뢰 구간을 음영 영역으로 표시함으로써 데이터의 핵심적인 트렌드와 그 통계적 신뢰도를 한눈에 파악할 수 있도록 해줍니다. 이렇게 하면 수많은 개별 선으로 인해 복잡해질 수 있는 그래프를 깔끔하고 해석하기 쉽게 만들 수 있습니다.

**강의 내용**:
교수님께서는 슬라이드의 두 개의 선 그래프가 각각 Group A와 Group B에 대한 데이터 추이를 나타낸다고 강조하셨습니다. 여기서 가장 중요한 파라미터는 `errorbar`로, 이는 데이터의 평균뿐만 아니라 그 평균에 대한 95% 신뢰 구간을 함께 표시하여 데이터의 변동성과 신뢰도를 시각적으로 전달합니다. 각 그룹에는 30회의 반복 측정 데이터가 있으며, `seaborn`은 개별적인 60개의 선(Group A 30개, Group B 30개)을 그리는 대신, 각 시간 지점마다 30회 반복 측정된 값들의 평균을 계산하고, 이 평균에 대한 부트스트랩 95% 신뢰 구간을 함께 시각화합니다. 결과적으로 생성된 플롯은 매우 깔끔하고 강력하며, 실선은 데이터의 평균적인 트렌드를, 음영 처리된 영역은 95% 신뢰 구간을 의미합니다. (음성에서 55% 신뢰 구간이 언급되었으나, 코드와 이어지는 설명에서 95% 신뢰 구간이 명확하므로 95%로 이해하는 것이 옳습니다.)

**시험 포인트**:
- ⭐ `seaborn.relplot`을 활용하여 반복 측정 데이터의 평균 추이와 불확실성(신뢰 구간)을 시각화하는 방법을 이해하고 설명할 수 있어야 합니다. 특히 `kind="line"`과 `errorbar=("ci", 95)` 파라미터의 역할을 정확히 알아두세요.
- ⭐ `errorbar` 파라미터가 왜 필요한지 (많은 개별 라인을 그리는 대신 데이터의 핵심 트렌드와 신뢰도를 한눈에 파악하기 위함) 그 장점을 설명할 수 있어야 합니다.
- ⭐ `col` 또는 `row` 파라미터를 이용한 Faceting 기법이 여러 그룹의 데이터를 효율적으로 비교하는 데 어떻게 사용되는지 이해하고 있어야 합니다.

---
## Slide 12

**핵심 개념**
이 슬라이드는 여러 그룹에 걸쳐 분포(Distribution)를 비교하는 방법에 대해 설명합니다. 데이터의 분포를 비교함으로써 각 그룹 간의 위치(location), 퍼짐(spread), 비대칭성(skewness), 꼬리(tails) 모양, 다봉성(multimodality) 등의 특성 차이를 파악하고, 전체 구성에 대한 이해를 돕습니다. 주로 `seaborn` 라이브러리의 `displot` (히스토그램 또는 KDE), `kdeplot`, `histplot`, `ecdfplot` 등의 시각화 도구가 활용됩니다.

**코드/수식 해설**
*   **분포 시각화 파라미터**:
    *   `stat="density"`: 여러 분포를 비교할 때, 각 분포의 히스토그램이나 KDE(Kernel Density Estimate)를 밀도(density)로 정규화하여 면적의 합이 1이 되도록 합니다. 이는 각 그룹의 데이터 크기가 다를 때도 공정한 비교를 가능하게 합니다.
    *   `common_norm=False`: 다중 분포를 그릴 때, 각 분포를 독립적으로 정규화하도록 설정합니다. 만약 `True`로 설정하면 모든 그룹의 데이터를 합산한 전체 데이터에 대해 정규화되므로, 그룹별 분포의 상대적인 모양을 파악하기 어려워질 수 있습니다.

*   **OLS (Ordinary Least Squares) 수식**:
    강의 음성에서 언급된 OLS는 회귀 분석에서 가장 널리 사용되는 방법으로, 실제 값과 모델이 예측한 값 사이의 오차 제곱합을 최소화하는 방식으로 회귀 계수를 추정합니다.
    선형 회귀 모델 $\hat{y}_i = \beta_0 + \beta_1 x_i$ 에 대해, OLS는 다음 오차 제곱합(Residual Sum of Squares, RSS)을 최소화하는 $\beta_0, \beta_1$을 찾습니다.
    $$ \text{RSS} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - (\beta_0 + \beta_1 x_i))^2 $$
    여기서 $y_i$는 실제 값, $\hat{y}_i$는 예측 값, $x_i$는 독립 변수, 그리고 $\beta_0, \beta_1$은 추정해야 할 회귀 계수입니다.

**구체적 예시**
*   **성별/연령대별 소득 분포 비교**: 성별 또는 연령대 그룹에 따라 소득 분포가 어떻게 다른지(`location` - 평균 소득, `spread` - 소득 격차, `skew` - 고소득자 비율)를 `displot`이나 `kdeplot`을 사용하여 시각적으로 비교할 수 있습니다. 예를 들어, 남성 그룹의 소득 분포와 여성 그룹의 소득 분포를 동시에 그려서 평균 소득의 차이와 분포의 형태를 한눈에 파악합니다.
*   **지역별 집값 분포 분석**: 특정 도시의 지역구별 아파트 평당 가격 분포를 비교하여, 어떤 지역이 평균 가격이 높고(shift), 가격 변동성이 큰지(spread), 또는 고가 아파트가 몰려있는지(tail) 등을 파악할 수 있습니다.

**강의 내용**
교수님께서는 슬라이드의 주제와는 다소 다르게 회귀 플롯(regression plot)에 대해 설명하며, 산점도(scatter plot)에 적합된 모델(주로 선형 모델)을 추가하여 추세(trend)를 요약하는 것이라고 말씀하셨습니다. 특히,
*   회귀 플롯에서 **55% 신뢰 구간(confidence interval)**이 음영 처리된 영역으로 표시된다고 언급하셨습니다.
*   가장 흔한 모델로 **OLS (Ordinary Least Squares)**를 강조하셨습니다. OLS는 오차를 최소화하는 단일 직선을 가장 잘 맞추는 방법이며, 선형 대수학 수업에서 배웠을 것이라고 덧붙이셨습니다.
*   OLS의 대안으로 **Loess (Local Smoother)**를 언급하셨습니다.

**시험 포인트**
*   ⭐ **다중 분포 비교의 목적**: 여러 그룹 간의 데이터 분포 특성(위치, 퍼짐, 비대칭성, 꼬리 등) 차이를 파악하는 목적을 이해해야 합니다.
*   ⭐ **정규화 옵션의 중요성**: `stat="density"`와 `common_norm=False` 파라미터가 다중 분포를 공정하게 비교하는 데 왜 중요한지, 그리고 이들을 사용하지 않을 경우 발생할 수 있는 문제점(예: 오해의 소지가 있는 면적 비교)을 설명할 수 있어야 합니다.
*   ⭐ **OLS (Ordinary Least Squares)**: OLS의 개념(오차 제곱합 최소화), 선형 회귀에서 OLS의 역할 및 수식을 정확히 이해하고 있어야 합니다. (선형 대수학과의 연관성 강조)
*   ⭐ **회귀 플롯**: 회귀 플롯이 산점도에 어떤 정보를 추가하여 데이터의 추세를 보여주는지, 그리고 신뢰 구간의 의미를 알아두세요.
*   ⭐ **Loess**: OLS의 대안으로서 Loess와 같은 지역 평활화(local smoother) 방법이 있다는 것을 기억하세요.

---
## Slide 13

**핵심 개념**
이 슬라이드는 `seaborn` 라이브러리의 `displot` 함수를 사용하여 여러 그룹의 데이터 분포를 하나의 그래프에 오버레이(겹쳐서) 히스토그램 형태로 시각화하는 방법을 설명합니다. 특히, `Iris` 데이터셋의 `petal length` (꽃잎 길이) 변수를 `species` (종)별로 구분하여 분포를 비교합니다. 이러한 시각화는 다른 그룹 간에 특정 변수의 분포가 어떻게 다른지 직관적으로 파악하는 데 매우 유용합니다.

**코드/수식 해설**

```python
sns.displot(
    data=iris,
    x="petal length (cm)", hue="species",
    kind="hist", bins=24,
    stat="density", common_norm=False,
    element="step" # outlines for clean overlays
)
```

*   `sns.displot()`: `seaborn`에서 단일 변수의 분포를 시각화하는 데 사용되는 유연한 함수입니다.
*   `data=iris`: 시각화에 사용할 데이터프레임으로 `iris` 데이터셋을 지정합니다.
*   `x="petal length (cm)"`: 히스토그램의 x축에 해당할 변수로 `petal length (cm)` 컬럼을 지정합니다.
*   `hue="species"`: `species` 컬럼의 고유한 값(예: setosa, versicolor, virginica)에 따라 데이터를 그룹화하고, 각 그룹을 다른 색상으로 구분하여 표시합니다. 이를 통해 그룹별 분포를 오버레이하여 볼 수 있습니다.
*   `kind="hist"`: 분포 시각화의 종류를 히스토그램(`hist`)으로 지정합니다. 다른 옵션으로는 커널 밀도 추정(`kde`), 경험적 누적 분포(`ecdf`) 등이 있습니다.
*   `bins=24`: 히스토그램의 막대(bin) 개수를 24개로 설정합니다. 이는 데이터를 24개의 구간으로 나누어 각 구간에 속하는 데이터의 빈도를 계산합니다.
*   `stat="density"`: y축의 통계량을 `count` (빈도) 대신 `density` (밀도)로 표시합니다. `density`는 각 막대의 높이를 전체 데이터의 합이 1이 되도록 정규화하여, 막대의 높이가 해당 구간에 데이터가 있을 확률 밀도를 나타내게 합니다.
*   `common_norm=False`: `hue` 파라미터로 여러 그룹을 나눴을 때, 각 그룹의 히스토그램을 개별적으로 정규화합니다. 즉, 각 종별 `petal length` 분포의 총 면적이 1이 되도록 합니다. `True`로 설정하면 모든 그룹의 데이터를 합친 전체 분포에 대해 정규화됩니다.
*   `element="step"`: 히스토그램의 막대를 채우는 대신, 막대의 윤곽선(outline)을 계단(`step`) 형태로 그려서 표시합니다. 이는 여러 히스토그램이 겹쳐질 때 각 분포를 더 명확하게 구분하고 깔끔하게 보이도록 합니다.

**구체적 예시**
첨부된 슬라이드의 하단 그래프는 `Iris` 데이터셋에서 `petal length`의 분포를 `setosa`, `versicolor`, `virginica` 세 종별로 오버레이하여 보여줍니다.
*   노란색 계단형 히스토그램(`setosa`)은 1cm에서 2cm 사이의 짧은 꽃잎 길이에 집중되어 있으며, 다른 두 종과는 명확하게 분리된 분포를 보입니다.
*   하늘색(`versicolor`)과 초록색(`virginica`) 히스토그램은 3cm에서 7cm 사이에서 분포하며, 서로 어느 정도 겹치는 구간이 있지만 `versicolor`는 3.5cm-5cm, `virginica`는 4.5cm-6.5cm 범위에 주로 분포하는 경향을 보여줍니다.
이처럼 `hue`와 `element="step"` 조합은 여러 범주형 그룹의 연속형 변수 분포를 한눈에 비교하고 각 그룹의 특징을 파악하는 데 효과적입니다.

**강의 내용**
교수님 음성 전사는 현재 슬라이드의 내용(그룹별 오버레이 히스토그램)과 직접적으로 일치하지 않습니다. 음성에서는 `OLS (Ordinary Least Squares)`, `Loess (Locally Estimated Scatterplot Smoothing)`와 같은 회귀 분석 기법, 산점도(scatterplot)에서의 `중심 경향 요약`, `55% 신뢰 구간` 및 `ESS`를 통한 `smoothness` 제어, 그리고 `wine` 데이터셋의 `alcohol` 변수를 플로팅하는 것에 대해 설명하고 있습니다. 이러한 내용은 일반적으로 데이터의 추세선(trend line)을 찾고 예측 모델을 구축할 때 사용되는 개념입니다. 이는 주로 산점도와 함께 회귀선을 시각화하는 맥락에서 다뤄집니다.

**시험 포인트**
*   ⭐ `seaborn.displot` 함수를 사용하여 여러 그룹의 단일 변수 분포를 효과적으로 시각화하는 방법을 이해해야 합니다.
*   ⭐ `kind` (hist, kde, ecdf), `stat` (count, density, probability), `common_norm` (True/False), `element` (bars, step, poly) 등 `displot`의 핵심 파라미터들이 시각화 결과에 미치는 영향을 설명하고 적절히 활용할 수 있어야 합니다.
*   ⭐ 특히, `hue` 파라미터를 사용하여 그룹별 오버레이를 구현하는 방법과, `stat="density"` 및 `element="step"`가 겹쳐진 히스토그램을 해석하는 데 어떻게 도움이 되는지 이해해야 합니다.
*   ⭐ 주어진 데이터셋에 대해 그룹별 분포 비교가 필요할 때 `displot`과 같은 시각화 기법을 언제, 왜 선택해야 하는지 설명할 수 있어야 합니다.

---

## Slide 14

**핵심 개념**
이 슬라이드는 `seaborn` 라이브러리의 `kdeplot` 함수를 사용하여 여러 범주형 그룹의 Kernel Density Estimate (KDE)를 `stacked` 또는 `filled` 형태로 시각화하는 방법을 설명합니다. KDE는 데이터의 확률 밀도 함수 (Probability Density Function, PDF)를 추정하여 분포의 형태를 부드러운 곡선으로 나타냅니다. `multiple="fill"` 옵션은 여러 KDE 곡선이 서로 겹치는 부분을 채워 넣고, 각 `x` 값에서 모든 범주의 비율이 100% (또는 1.0)가 되도록 정규화하여 표시합니다. 이는 특정 변수 값 범위에서 각 범주가 차지하는 상대적인 비중을 직관적으로 비교할 때 유용합니다.

**코드/수식 해설**

```python
sns.kdeplot(
    data=iris,
    x="petal length (cm)",
    hue="species",
    multiple="fill",
    common_norm=False,
    bw_adjust=0.9,
    alpha=0.9
)
```

*   `sns.kdeplot()`: `seaborn` 라이브러리의 KDE 플롯을 그리는 함수입니다.
*   `data=iris`: 플롯에 사용할 데이터를 지정합니다. 여기서는 `iris` 데이터셋을 사용합니다.
*   `x="petal length (cm)"`: X축에 표시할 변수를 지정합니다. 붓꽃의 꽃잎 길이(cm)입니다.
*   `hue="species"`: `species` (종) 변수에 따라 KDE를 나누어 그립니다. `setosa`, `versicolor`, `virginica` 세 가지 종별 분포를 보게 됩니다.
*   `multiple="fill"`: 이 옵션이 핵심입니다. 각 `hue` 그룹에 대한 KDE 곡선을 쌓아서(stack) 그릴 때, 곡선 아래 영역을 채워 넣습니다. 각 `x` 값에서 채워진 영역의 높이는 해당 지점에서 각 `hue` 그룹이 전체에서 차지하는 비율을 나타냅니다. Y축이 0.0부터 1.0까지의 `proportion`으로 표시되는 이유입니다.
*   `common_norm=False`: `multiple="fill"`과 함께 사용될 때, 각 개별 KDE 곡선이 자신의 면적 합이 1이 되도록 정규화됩니다. 이 설정은 스택된 플롯에서 각 `x` 값에서 모든 범주의 합이 1이 되도록 하는 데 필수적입니다.
*   `bw_adjust=0.9`: 대역폭(bandwidth) 조절 파라미터입니다. KDE 곡선의 부드러움을 결정하는 `h` 값을 조절합니다. 값이 작을수록 곡선이 데이터 포인트에 더 민감하게 반응하여 뾰족해지고, 값이 클수록 더 부드러워집니다. 여기서는 기본값(1.0)보다 약간 작은 0.9로 설정하여 살짝 더 상세한 분포를 보여줍니다.
*   `alpha=0.9`: 채워진 영역의 투명도를 설정합니다. 0 (완전 투명)에서 1 (완전 불투명) 사이의 값을 가집니다.

KDE의 기본 수식은 다음과 같습니다:
$$ \hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right) $$
여기서 $n$은 데이터 포인트 수, $h$는 대역폭(bandwidth), $K(\cdot)$는 커널 함수(예: 가우시안 커널), $x_i$는 개별 데이터 포인트입니다.

**구체적 예시**
첨부된 슬라이드의 `kdeplot`은 붓꽃(Iris) 데이터셋에서 `petal length (cm)`를 기준으로 `species`별 분포의 상대적 비중을 보여줍니다.
*   **`petal length`가 약 1.0 cm ~ 2.5 cm 사이**: 주황색 영역(`setosa`)이 거의 100%를 차지합니다. 이는 이 꽃잎 길이 범위에서는 거의 모든 붓꽃이 `setosa` 종임을 의미합니다.
*   **`petal length`가 약 2.5 cm ~ 5.0 cm 사이**: 하늘색 영역(`versicolor`)과 초록색 영역(`virginica`)이 함께 나타나며, 이들 두 종이 혼재되어 있음을 보여줍니다. `petal length`가 증가함에 따라 `versicolor`의 비율이 줄어들고 `virginica`의 비율이 점차 늘어나는 것을 확인할 수 있습니다.
*   **`petal length`가 약 5.5 cm 이상**: 초록색 영역(`virginica`)이 거의 100%를 차지합니다. 이 꽃잎 길이 범위에서는 대부분 `virginica` 종임을 알 수 있습니다.
이 플롯을 통해 `petal length`라는 단일 변수만으로도 붓꽃의 종을 상당 부분 구분할 수 있음을 시각적으로 파악할 수 있습니다.

**강의 내용**
교수님께서는 이 슬라이드가 시작되기 직전까지 `regplot`과 `lmplot`을 이용한 선형 회귀 적합(OLS) 및 로컬 가중치 회귀(LoESS) 곡선에 대한 설명을 마무리하고 계십니다. 특히, '알코올'과 '색상 강도(color intensity)' 변수 간의 강한 양의 선형 관계를 보여주는 예시를 언급하셨습니다. 음성 전사 마지막 부분의 "Okay, next plot is a real plot."이라는 발언은 이전 시각화(선형 회귀 플롯)에 대한 논의를 마치고, 현재 슬라이드에서 보여지는 새로운 유형의 시각화(`kdeplot`)로 넘어가는 전환점입니다. 이는 다양한 데이터 시각화 기법들을 순차적으로 학습하고 있음을 시사합니다.

**시험 포인트**
*   ⭐ `kdeplot`의 기본적인 기능(데이터 분포 시각화)과 `multiple="fill"` 옵션의 의미를 정확히 이해하고 있어야 합니다.
*   ⭐ `hue` 파라미터를 사용하여 여러 범주형 그룹별 분포를 비교하는 방법을 알아야 합니다.
*   ⭐ 스택/채워진 KDE 플롯을 보고, 특정 `x` 값 범위에서 각 범주가 전체에서 차지하는 상대적 '비율' 또는 '비중'을 해석하는 능력이 중요합니다.
*   ⭐ `bw_adjust`와 같은 대역폭(bandwidth) 관련 파라미터가 KDE 곡선의 형태와 부드러움에 어떻게 영향을 미치는지 설명할 수 있어야 합니다.
*   ⭐ `common_norm=False`가 `multiple="fill"`과 함께 사용될 때 어떤 역할을 하는지 이해해야 합니다.

---
## Slide 15

### 핵심 개념

`Pair Plot` (산점도 행렬, Scatter-Matrix)은 데이터셋 내의 모든 수치형 변수 쌍 간의 관계를 한눈에 파악하기 위한 강력한 시각화 도구입니다. 이는 여러 개의 산점도(`scatter plot`)를 격자 형태로 배열한 것으로, 각 변수의 분포 정보까지 함께 제공합니다.

*   **정의**: 데이터셋의 각 변수 쌍에 대한 산점도를 격자로 배열하고, 대각선에는 각 변수의 단일 변수 분포(예: 히스토그램 `hist` 또는 커널 밀도 추정 `kde`)를 표시하여 변수 간의 관계 행렬을 시각화합니다.
*   **활용 시점**:
    *   변수 간의 **쌍별 연관성(pairwise associations)**을 빠르게 탐색할 때.
    *   데이터 내의 **클러스터(clusters)**나 그룹을 시각적으로 식별할 때.
    *   특정 레이블(label)에 따라 데이터가 얼마나 **분리 가능한지(separability by label)** 확인할 때 유용합니다.

### 코드/수식 해설

`Pair Plot`은 주로 `seaborn` 라이브러리의 `pairplot()` 함수를 사용하여 생성합니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 로드
iris = sns.load_dataset("iris")

# 기본적인 Pair Plot 생성
sns.pairplot(iris)
plt.show()

# 특정 변수에 따라 색상 구분 (hue), 비대각선 플롯 종류 지정 (kind), 대각선 플롯 종류 지정 (diag_kind)
sns.pairplot(iris, hue="species", kind="scatter", diag_kind="kde")
plt.show()

# 중복 제거 (corner=True): 하삼각 행렬만 표시
sns.pairplot(iris, hue="species", kind="scatter", diag_kind="kde", corner=True)
plt.show()
```

*   **`kind` 인자**: 비대각선(off-diagonal)에 그려질 플롯의 유형을 지정합니다. 기본값은 `'scatter'`이며, `'reg'` (회귀선 포함), `'kde'` (2D 커널 밀도 추정) 등으로 설정할 수 있습니다.
*   **`diag_kind` 인자**: 대각선(diagonal)에 그려질 플롯의 유형을 지정합니다. 기본값은 `'hist'` (히스토그램)이며, `'kde'` (커널 밀도 추정) 등으로 설정할 수 있습니다.
*   **`hue` 인자**: 데이터 내의 범주형 변수를 지정하여, 해당 변수의 값에 따라 다른 색상으로 데이터를 구분하여 표시합니다. 이는 그룹별 패턴을 파악하는 데 매우 유용합니다.
*   **`corner=True` 인자**: 기본적으로 `pairplot`은 대칭적인 플롯 행렬을 그립니다 (예: X-Y 산점도와 Y-X 산점도는 서로 대칭). `corner=True`로 설정하면 중복되는 플롯을 제거하고, 아래쪽 삼각형 부분만 표시합니다.

**Pitfalls**:
데이터의 변수 개수 $d$가 많아질수록 생성되는 축(axes)의 개수는 $O(d^2)$에 비례하여 증가합니다.
$$ \text{플롯 개수} = d \times d $$
이는 데이터셋의 피처(feature) 개수가 많거나 전체 데이터($n$)의 크기가 클 경우, 플롯을 렌더링하는 데 시간이 오래 걸리거나 시각적으로 복잡해져 분석이 어려워질 수 있음을 의미합니다. 이 경우, 데이터 샘플링(downsample)을 고려해야 합니다.

### 구체적 예시

머신러닝에서 분류 모델을 구축하기 전에 `Pair Plot`은 데이터의 초기 탐색에 매우 유용합니다. 예를 들어, 붓꽃(Iris) 데이터셋을 사용하여 세 가지 붓꽃 품종(`species`)이 꽃잎(petal)과 꽃받침(sepal)의 길이(`length`)와 너비(`width`) 변수들을 기준으로 얼마나 잘 구분되는지 시각적으로 확인할 수 있습니다.

`pairplot(iris, hue="species")`를 그리면, 각 변수 쌍에 대한 산점도에서 품종별로 다른 색상의 점들이 어떻게 분포하는지 볼 수 있습니다. 만약 특정 변수 쌍에서 각 품종의 점들이 명확히 분리된 클러스터를 형성한다면, 해당 변수들이 품종 분류에 중요한 역할을 할 수 있음을 시사합니다. 예를 들어, `petal_length`와 `petal_width` 산점도에서 품종별로 뚜렷한 경계가 나타나는 것을 확인할 수 있습니다.

### 강의 내용

교수님께서는 `Pair Plot`이 완전히 새로운 유형의 플롯이라기보다는, `scatter plot`이나 `line plot`과 같은 기본적인 플롯들을 **피겨 레벨(figure level)에서 감싸서(wrapper)** 보여주는 역할을 한다고 설명하셨습니다. 이는 여러 플롯을 하나의 통합된 시각화로 구성하는 높은 수준의 추상화된 함수임을 의미합니다.

특히, 데이터를 **"small multiples"** 형태로 시각화할 때 `Pair Plot`이 매우 유용하다고 강조하셨습니다. "Small multiples"는 데이터를 하위 그룹으로 나누고, 각 하위 그룹에 대해 동일한 유형의 플롯을 그린 다음, 이를 그리드 형태로 배열하여 여러 조건에서의 패턴 변화를 비교하기 쉽게 만드는 기법입니다.

강의에서는 `kind` 인자를 `scatter` 또는 `line`으로 설정하여 플롯 유형을 지정할 수 있다고 언급하셨습니다. (참고: `pairplot`의 `kind`는 주로 `'scatter'`, `'reg'` 등을 지원하며, `line`은 `seaborn.relplot`과 같은 다른 피겨 레벨 함수에서 더 일반적으로 사용됩니다. 교수님의 말씀은 `pairplot`이 이러한 기본적인 관계형 플롯들을 조합하는 상위 개념임을 강조하신 것으로 이해할 수 있습니다.)

예를 들어, "세 가지 카테고리가 있을 때 세 가지 다른 산점도를 그린다"는 설명은 `hue` 인자를 사용하여 데이터를 범주별로 구분하고, 각 범주에 대해 개별적인 패턴을 한 그리드 안에서 비교하는 `Pair Plot`의 핵심적인 활용 사례를 설명한 것입니다.

### 시험 포인트

*   ⭐ `Pair Plot`의 **정의와 목적**: 여러 변수 간의 관계와 개별 변수의 분포를 동시에 탐색하기 위한 시각화 도구임을 이해해야 합니다.
*   ⭐ `Pair Plot`의 **구성 요소**: 비대각선(off-diagonal)은 변수 간의 관계(`kind` 인자), 대각선(diagonal)은 각 변수의 분포(`diag_kind` 인자)를 나타냄을 기억해야 합니다.
*   ⭐ 주요 `seaborn.pairplot()` **인자들의 역할**: `hue` (그룹별 색상), `kind` (비대각선 플롯 종류), `diag_kind` (대각선 플롯 종류), `corner=True` (중복 제거)의 기능을 명확히 알고 있어야 합니다.
*   ⭐ **"Small multiples"** 개념: 데이터를 서브그룹으로 나눠 동일한 플롯을 그리드에 배열하는 기법의 의미와 `Pair Plot`과의 연관성을 이해해야 합니다.
*   ⭐ `Pair Plot`의 **한계 (Pitfalls)**: 변수의 개수 $d$가 많아질수록 플롯의 개수가 $O(d^2)$로 증가하여 발생하는 성능 및 시각적 복잡성 문제, 그리고 이에 대한 해결책(다운샘플링)을 설명할 수 있어야 합니다.

---
## Slide 16

## Pair Plot — 코드 및 예시 (Iris)

### 핵심 개념
**Pair Plot**은 다변량 데이터셋의 모든 수치형 변수 쌍에 대한 관계를 한 번에 시각화하고, 각 변수의 단변량 분포를 대각선에 표시해주는 강력한 탐색적 데이터 분석(EDA) 도구입니다. `seaborn` 라이브러리의 `pairplot()` 함수를 사용하여 데이터의 전반적인 구조, 변수 간의 상관관계, 그리고 특정 그룹(범주)별 특성 차이를 시각적으로 쉽게 파악할 수 있습니다.

### 코드/수식 해설

```python
import seaborn as sns
import pandas as pd # 일반적으로 데이터프레임 사용

# iris 데이터셋 로드 (예시, 실제 코드에는 포함되지 않음)
# iris = sns.load_dataset("iris") 

sns.pairplot(
    iris,
    vars=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
    hue="species",
    corner=True,
    diag_kind="kde",
    plot_kws=dict(alpha=0.6, s=22)
)
```

*   `sns.pairplot(iris, ...)`: `iris` 데이터프레임을 입력받아 변수 쌍 간의 관계를 시각화합니다.
*   `vars=["..."]`: pair plot에 포함할 특정 변수(컬럼)들의 리스트를 지정합니다. 여기서는 붓꽃의 꽃받침(sepal)과 꽃잎(petal)의 길이 및 너비 변수를 사용했습니다.
*   `hue="species"`: `iris` 데이터프레임의 "species" 컬럼을 기준으로 데이터를 그룹화하고, 각 그룹(종)에 다른 색상을 할당하여 시각화합니다. 이를 통해 종별 특성 차이를 시각적으로 쉽게 파악할 수 있습니다.
*   `corner=True`: 전체 `N x N` 행렬 대신, 대각선(단변량 분포)과 하삼각 행렬(이변량 산점도)만 생성합니다. 상삼각 행렬은 하삼각 행렬과 대칭이므로, 중복을 피하고 플롯의 공간 효율성을 높이며 복잡성을 줄일 때 유용합니다.
*   `diag_kind="kde"`: 대각선에 위치하는 각 변수의 단변량 분포를 **Kernel Density Estimate (KDE)** 플롯으로 그립니다. KDE는 데이터 분포의 밀도를 부드러운 곡선 형태로 추정하여 보여줍니다.
    *   *참고*: 슬라이드의 결과 이미지는 대각선에 히스토그램이 표시되어 있어, 코드의 `diag_kind="kde"` 설정과 차이가 있습니다. `diag_kind="hist"`를 사용하면 히스토그램이 그려집니다.
*   `plot_kws=dict(alpha=0.6, s=22)`: 산점도(scatter plot)에 적용될 추가적인 키워드 인수를 딕셔너리 형태로 전달합니다.
    *   `alpha=0.6`: 점의 투명도를 $0.6$으로 설정하여 데이터 포인트가 겹쳐진 부분을 쉽게 구별할 수 있게 합니다.
    *   `s=22`: 각 점의 크기를 $22$로 설정합니다.

### 구체적 예시
Iris 데이터셋을 사용하여 `pairplot`을 생성하면, 붓꽃의 세 가지 종(setosa, versicolor, virginica)에 대한 4가지 수치형 변수(sepal length, sepal width, petal length, petal width) 간의 모든 쌍별 관계를 한눈에 볼 수 있습니다. 예를 들어, `sepal length`와 `sepal width` 간의 산점도를 보면 Setosa 종은 다른 종들과 확연히 구분되는 군집을 형성하며 특정 상관관계를 보이고, Versicolor와 Virginica 종 또한 서로 다른 분포 패턴을 보이는 것을 확인할 수 있습니다. `hue="species"` 덕분에 이러한 종별 차이가 색상으로 명확히 구분되어 데이터의 그룹별 특성을 쉽게 파악할 수 있습니다.

### 강의 내용
교수님께서는 Iris 데이터셋의 `pairplot`을 분석하며, 특히 붓꽃의 종(species)에 따른 `sepal length`와 `sepal width` 변수 간의 상관관계를 강조하여 설명하셨습니다.

*   **Setosa 종**: `sepal length`와 `sepal width` 사이에서 "명확한 양의 상관관계(clear positive correlation)"를 보인다고 언급하셨습니다. 즉, 꽃받침 길이가 길수록 꽃받침 너비도 길어지는 경향이 뚜렷함을 의미합니다.
*   **Versicolor 종**: "sepal length"와 "sepal width" 간에 "더 약한 상관관계(weaker correlation)"를 보인다고 설명하셨습니다. Setosa만큼 뚜렷한 경향성을 보이지 않는다는 의미입니다.
*   **Virginica 종**: Setosa와 유사하게 "양의 상관관계(positive correlation)"를 보인다고 설명하셨습니다.

이러한 종별 상관관계의 차이는 `hue` 파라미터로 색상 구분된 산점도를 통해 시각적으로 명확하게 드러나며, 붓꽃 종을 구분하는 중요한 특징이 될 수 있음을 시사합니다.

### 시험 포인트
*   ⭐ **`seaborn.pairplot`의 주요 목적**: 다변량 데이터에서 모든 수치형 변수 쌍 간의 관계(산점도) 및 각 변수의 단변량 분포(대각선)를 한 번에 시각화하여 데이터의 전반적인 구조와 변수 간의 상관관계를 탐색하는 데 사용됩니다.
*   ⭐ **주요 파라미터의 기능 및 활용**:
    *   `vars`: 시각화할 특정 변수들을 선택하는 데 사용됩니다.
    *   `hue`: 특정 범주형 변수를 기준으로 데이터를 색상으로 구분하여 그룹별 특성을 파악하는 데 필수적입니다 (예: `species`로 붓꽃 종별 차이 분석).
    *   `corner=True`: 플롯의 중복을 제거하고 필요한 정보만 표시하여 가독성을 높이는 데 활용됩니다.
    *   `diag_kind`: 대각선 플롯의 종류를 지정합니다 (`"kde"` 또는 `"hist"` 등). 이 파라미터를 통해 각 변수의 단변량 분포를 어떻게 표현할지 결정할 수 있습니다.
*   ⭐ **그래프 해석 능력**: `pairplot`의 산점도에서 점들의 분포를 보고 변수 간의 양의 상관관계, 음의 상관관계, 또는 상관관계 없음 등을 정확하게 파악하고 설명할 수 있어야 합니다 (예: Setosa의 sepal length/width 양의 상관관계).

---
## Slide 17

**핵심 개념**:
*   **클러스터맵 (Clustermap)**: 계층적 클러스터링(Hierarchical Clustering)을 적용한 히트맵입니다. 데이터의 행(rows)과 열(columns)을 유사도에 따라 재정렬하여 숨겨진 블록 구조(blocked structure)를 시각적으로 드러내는 데 사용됩니다. 이는 데이터 내의 유사한 특징 그룹이나 샘플 클러스터를 찾거나, 변수 간의 상관관계 블록을 탐색할 때 유용합니다.
*   **분포 비교 (Comparing Distributions)**: 하나의 수치형 변수(numerical variable)와 하나의 범주형 변수(categorical value)가 있을 때, 범주형 변수의 각 그룹에 따라 수치형 변수의 분포가 어떻게 다른지 비교하는 분석 기법입니다.

**코드/수식 해설**:
*   **클러스터맵 (Clustermap) 생성 예시 (Python, Seaborn 라이브러리)**:
    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    # 예시 데이터 생성: 50개의 샘플과 5개의 피처를 가진 데이터프레임
    # 실제 데이터셋에서는 이 데이터를 기반으로 유사성/상관 행렬을 생성합니다.
    df = pd.DataFrame(np.random.rand(50, 5), columns=[f'feature_{i}' for i in range(5)])
    
    # 피처 간의 상관 행렬 계산
    correlation_matrix = df.corr()

    # 클러스터맵 그리기
    plt.figure(figsize=(8, 7))
    sns.clustermap(correlation_matrix,
                   cmap='viridis',        # 색상 맵 (컬러 스케일) 설정
                   annot=True,            # 셀 내부에 숫자 값 표시 여부
                   fmt=".2f",             # 숫자 값의 형식 (소수점 둘째 자리까지)
                   linewidths=.5,         # 셀 경계선의 두께
                   cbar_pos=(0.02, 0.82, 0.03, 0.15)) # 컬러바의 위치 (left, bottom, width, height)
    plt.suptitle("Feature Correlation Clustermap", y=1.02) # 전체 제목
    plt.show()
    ```
    *설명*: `seaborn.clustermap` 함수는 입력된 데이터 행렬(여기서는 상관 행렬)에 계층적 클러스터링을 적용하고, 그 결과를 히트맵으로 시각화합니다. 행과 열이 클러스터링 결과에 따라 재정렬되며, 이는 덴드로그램으로 표현됩니다. `cmap`은 값의 크기에 따른 색상 변화를, `annot`은 각 셀에 실제 값을 표시할지 여부를 결정합니다.

**구체적 예시**:
*   **클러스터맵**: 금융 데이터 분석에서 여러 회사의 주가 수익률 데이터를 클러스터맵으로 시각화할 수 있습니다. 예를 들어, 금융주, 기술주, 제조업 등 산업별로 유사한 주가 변동 패턴을 보이는 회사들이 클러스터맵 상에서 가까이 묶여 블록 형태로 나타나게 됩니다. 이 블록들은 특정 산업 섹터 또는 시장 트렌드에 따라 움직이는 그룹을 시각적으로 보여줍니다. 덴드로그램(dendrogram)은 어떤 회사들이 서로 유사하여 먼저 묶이고, 어떤 그룹끼리 다시 묶이는지 그 계층적 관계를 보여줍니다.
*   **분포 비교**: 특정 제품의 판매량(수치형 변수)이 지역(범주형 변수: 서울, 부산, 대구 등)에 따라 어떻게 다른지 비교하는 경우를 예로 들 수 있습니다. 각 지역별로 판매량의 히스토그램이나 KDE 플롯을 그려보면, 특정 지역에서 판매량이 높고 분포가 좁게 집중되어 있는지, 혹은 판매량이 낮지만 넓게 퍼져있는지 등을 한눈에 비교할 수 있습니다.

**강의 내용**:
교수님께서는 슬라이드의 주된 내용인 '클러스터맵'에 대한 설명 직후 또는 직전에, **"다수의 분포 비교(comparing distributions, multiple distributions)"**라는 다음 주제로 넘어감을 명확히 언급하셨습니다.
*   **주제 전환**: "Let's move to our next kind of family called comparing distributions, multiple distributions." 라고 말씀하시며 주제 전환을 알렸습니다.
*   **분포 비교의 상황**: 이 비교는 **하나의 수치형 변수**와 **하나의 범주형 변수**가 있을 때, 이들을 서로 비교하는 상황에 적합하다고 설명하셨습니다.
*   **활용 도구**: 분포 비교를 위한 시각화 도구로 **히스토그램(histogram)**, **커널 밀도 추정(KDE, Kernel Density Estimate)**, **경험적 누적 분포 함수(ECDF, Empirical Cumulative Distribution Function)**를 언급하셨습니다.
*   **예시 플롯**: 강의에서는 `distribution plot`과 `histogram plot`을 활용한 예시를 다룰 것이라고 설명하셨습니다.

**시험 포인트**:
*   ⭐ **클러스터맵의 정의 및 활용 목적**: '계층적으로 클러스터링된 히트맵'으로서 '피처 그룹, 샘플 클러스터 찾기' 및 '상관관계 블록 탐색'에 사용됨을 정확히 이해해야 합니다.
*   ⭐ **클러스터맵 해석 방법**: '덴드로그램이 유사성을 나타내고, 대각선상의 블록이 모듈(유사한 그룹)을 시사한다'는 점을 숙지해야 합니다.
*   ⭐ **클러스터맵 사용 시 주의사항 (Pitfalls)**: '거리/연결 방식에 민감하며, 스케일이 다른 경우 표준화 필요, 과도한 레이블 사용 금지' 등의 실제 사용 시 유의할 점을 기억해야 합니다.
*   ⭐ **다수 분포 비교의 상황 및 주요 도구**: '하나의 수치형 변수와 하나의 범주형 변수를 비교할 때' 사용되며, 이를 위한 `히스토그램`, `KDE`, `ECDF` 등의 시각화 도구들을 알아두는 것이 중요합니다. (특히 `seaborn` 라이브러리의 관련 함수들)

---
## Slide 18

### 핵심 개념

`Clustermap`은 데이터셋 내 여러 변수 간의 관계(주로 상관계수)를 시각화하고, 이 변수들을 계층적 군집화(Hierarchical Clustering)를 통해 재정렬하여 유사한 특성을 가진 변수들을 묶어 보여주는 강력한 도구입니다. 이는 `Heatmap`의 확장 버전으로, 행과 열에 대한 덴드로그램(dendrogram)을 추가하여 시각적 패턴을 더욱 명확하게 파악할 수 있게 합니다. 특히, 상관관계 행렬(correlation matrix)과 같이 대칭적인 관계를 나타내는 데이터에 유용하며, 변수 간의 숨겨진 구조나 그룹을 발견하는 데 도움을 줍니다.

### 코드/수식 해설

슬라이드의 코드는 `seaborn` 라이브러리의 `clustermap` 함수를 사용하여 와인 데이터셋의 상관관계 행렬을 시각화하는 과정을 보여줍니다.

```python
1 num = wine.drop(columns=["class", "target"], errors="ignore")
2 corr = num.corr()
3 sns.clustermap(
4     corr, center=0, cmap="vlag",
5     linewidths=0.3, method="average", metric="euclidean"
6 )
```

1.  `num = wine.drop(columns=["class", "target"], errors="ignore")`:
    *   `wine` 데이터프레임에서 "class"와 "target"이라는 이름의 열(column)을 제거합니다. 이 열들은 일반적으로 분류 레이블이거나 분석 대상이 아닌 경우가 많습니다.
    *   `errors="ignore"`는 제거하려는 열이 없을 경우 오류를 발생시키지 않고 무시하도록 합니다.
2.  `corr = num.corr()`:
    *   `num` 데이터프레임의 모든 숫자형 변수 쌍 간의 피어슨 상관계수(Pearson Correlation Coefficient)를 계산하여 상관관계 행렬 `corr`를 생성합니다.
    *   피어슨 상관계수 $r$은 두 변수 $X$와 $Y$ 사이의 선형 관계 강도와 방향을 나타내며, 다음과 같이 계산됩니다:
        $$ r = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2 \sum (Y_i - \bar{Y})^2}} $$
        여기서 $\bar{X}$와 $\bar{Y}$는 각 변수의 평균입니다.
3.  `sns.clustermap(...)`:
    *   `seaborn` 라이브러리의 `clustermap` 함수를 호출하여 군집화된 히트맵을 생성합니다.
    *   `corr`: 시각화할 상관관계 행렬을 전달합니다.
    *   `center=0`: 컬러맵의 중심 값을 0으로 설정합니다. 상관관계 분석에서 0은 무상관을 의미하므로, 양의 상관관계와 음의 상관관계를 시각적으로 구분하는 데 유용합니다.
    *   `cmap="vlag"`: 사용할 컬러맵을 지정합니다. "vlag"는 파란색(-1)에서 흰색(0)을 거쳐 빨간색(+1)으로 변하는 발산형 컬러맵으로, 상관관계 시각화에 적합합니다.
    *   `linewidths=0.3`: 히트맵 셀 사이에 0.3의 두께를 가진 선을 추가하여 셀을 시각적으로 구분합니다.
    *   `method="average"`: 계층적 군집화 시 사용될 링키지(linkage) 방법을 지정합니다. "average"는 두 클러스터 간의 모든 개별 관측치 쌍의 평균 거리를 사용하여 클러스터 간 거리를 계산합니다.
    *   `metric="euclidean"`: 군집화 시 개체(여기서는 변수) 간의 거리를 측정하는 데 사용될 거리 측정법을 지정합니다. "euclidean"은 유클리드 거리(Euclidean distance)를 사용합니다.

### 구체적 예시

슬라이드 하단의 "Wine — Clustered Heatmap (order via linkage)" 이미지는 와인 데이터셋의 각 특성(예: ash, malic\_acid, alcohol, proline 등) 간의 상관관계를 `clustermap`으로 시각화한 결과입니다.

*   **색상 해석**:
    *   진한 노란색/연두색에 가까울수록 양의 상관관계(1에 가까움)가 강합니다. (예: `total_phenols`와 `flavanoids`)
    *   진한 보라색/파란색에 가까울수록 음의 상관관계(-1에 가까움)가 강합니다. (예: `malic_acid`와 `nonflavanoid_phenols` 주변)
    *   녹색/회색에 가까울수록 상관관계가 0에 가깝거나 약합니다.
*   **클러스터링 해석**:
    *   히트맵의 왼쪽과 상단에 있는 덴드로그램은 계층적 군집화 결과를 보여줍니다. 가지가 가깝게 연결될수록 해당 변수들은 서로 더 유사한 패턴을 보이며 강하게 연관되어 있다는 것을 의미합니다.
    *   예를 들어, `total_phenols`, `flavanoids`, `od280/od315_of_diluted_wines`는 서로 매우 강한 양의 상관관계를 보이며 하나의 클러스터를 형성하고 있습니다. 이는 이들 특성이 와인의 특정 품질에 함께 영향을 미칠 가능성이 높다는 것을 시사합니다.
    *   반대로, `malic_acid`와 `alcalinity_of_ash`는 `proline`과 같은 다른 특성들과는 다소 독립적인 클러스터를 형성하거나 약한 상관관계를 보일 수 있습니다.
*   **대각선**: 자기 자신과의 상관관계는 항상 1이므로 대각선은 진한 노란색으로 표시됩니다.

이 시각화를 통해 데이터 분석가는 어떤 특성들이 서로 강하게 연관되어 있는지, 어떤 특성들이 독립적인지 등을 한눈에 파악하여 데이터의 복잡한 구조를 이해하는 데 활용할 수 있습니다.

### 강의 내용

교수님의 음성 전사 내용은 현재 슬라이드의 `clustermap`과는 직접적으로 다른 시각화 기법, 즉 `seaborn.histplot` 또는 `seaborn.displot`을 활용한 **단변수/이변수 분포 시각화**에 대해 설명하고 있습니다. 이는 이 슬라이드 이전 단계에서 다루어졌거나, 관련 개념으로 잠시 언급되었을 가능성이 높습니다.

*   **Hue를 이용한 그룹별 히스토그램 오버레이**: "Hue is set to species, so that's why we have three histograms."는 `seaborn`에서 `hue` 파라미터를 사용하여 특정 범주형 변수(예: `species`)의 값(예: 3가지 종)에 따라 여러 개의 히스토그램을 한 차트 위에 겹쳐 그리는 것을 의미합니다. 이를 통해 각 그룹의 분포를 쉽게 비교할 수 있습니다.
*   **`displot`의 활용**: "Then you can use distribution plot."은 `seaborn.displot`을 언급하며, 이는 단변수(univariate) 또는 이변수(bivariate) 데이터의 분포를 히스토그램, KDE(커널 밀도 추정) 플롯 등으로 시각화하는 데 사용됩니다. 교수님께서는 특히 "distribution plot is related to bivariate data rather than univariate data"라고 언급했는데, `displot`은 단변수 분포도 시각화할 수 있지만 `hue`를 사용하거나, `kind='kde'` 등으로 이변수 분포를 시각화할 때도 활용됩니다.
*   **`stat='density'`의 중요성**: "And here the state is set to density, means the area under each histogram sums to one. And then this is essential for a fair comparison. Otherwise, group with more samples would just look bigger, right?"는 `histplot`에서 `stat='density'` 옵션의 중요성을 강조합니다. 이 옵션은 히스토그램의 Y축을 확률 밀도로 스케일링하여 각 막대 아래의 면적 합이 1이 되도록 합니다. 이는 표본 크기가 다른 그룹 간의 분포 모양을 공정하게 비교하기 위해 필수적입니다. 단순히 빈도수를 나타내면 표본이 많은 그룹의 히스토그램이 불필요하게 커 보여 왜곡된 판단을 할 수 있기 때문입니다.
*   **이변수 KDE Plot**: "The next one is KDE plot, but this is for the bivariate data."는 `seaborn.kdeplot`이 두 변수(이변수 데이터) 간의 결합 분포(joint distribution)를 등고선(contour) 형태로 시각화하는 데 사용될 수 있음을 설명합니다.

### 시험 포인트

*   ⭐ **Clustermap의 목적 및 해석**: Clustermap이 무엇이고, 왜 사용하며(상관관계 및 데이터 구조 파악), 히트맵 색상과 덴드로그램을 어떻게 해석해야 하는지 이해하는 것이 중요합니다. 특히, `center`, `cmap`, `method`, `metric`과 같은 주요 파라미터들이 시각화 결과에 어떤 영향을 미치는지 알아두세요.
*   ⭐ **상관관계 행렬의 의미**: `corr()` 메서드를 통해 얻는 상관관계 행렬의 각 값이 무엇을 의미하는지, 그리고 피어슨 상관계수의 개념을 알아야 합니다.
*   ⭐ **`seaborn` 분포 시각화(`displot`, `histplot`, `kdeplot`)**: 비록 슬라이드에 직접적인 코드는 없지만, 강의 음성에서 강조되었으므로, `seaborn`에서 분포를 시각화하는 다양한 방법(`displot`, `histplot`, `kdeplot`)과 각 함수의 주요 파라미터(특히 `hue`와 `stat='density'`)의 역할과 중요성을 숙지해야 합니다.
*   ⭐ **`stat='density'`의 필요성**: `stat='density'`를 사용하여 히스토그램의 면적을 정규화하는 이유, 즉 서로 다른 표본 크기를 가진 그룹 간의 분포를 공정하게 비교하기 위한 중요성을 설명할 수 있어야 합니다.

---
## Slide 19

**핵심 개념**
이 슬라이드는 두 변수 $(x, y)$ 간의 관계를 시각화하는 `Hexbin` 플롯과 `2D Histogram`에 대한 정의와 사용법을 다룹니다.
*   **정의**: 2D 도메인인 $(x, y)$ 공간을 육각형(`Hexbin`) 또는 직사각형(`2D Histogram`) 형태의 `bin`으로 분할한 후, 각 `bin`에 포함된 데이터 포인트의 수를 색상으로 인코딩하여 밀도를 표현하는 시각화 기법입니다. 색상의 진하기나 밝기가 해당 구간의 데이터 빈도(count)를 나타냅니다.
*   **사용 시점**: 일반적인 산점도(scatter plot)에서 데이터 포인트가 너무 밀집되어 과적합(overplotting)이 발생하여 개별 점을 구분하기 어려울 때, 데이터의 밀도 분포를 파악하는 데 유용합니다.
*   **해석 방법**: 색상이 진하거나 밝은 `bin` 영역(`Hotspots`)은 해당 $(x, y)$ 조합이 빈번하게 발생함을 의미합니다. `band shape` (띠 모양)은 두 변수 간의 관계 형태를 시각적으로 보여줍니다.
*   **주의사항 (Pitfalls)**: `Bin size` (구간의 크기)는 시각적 인식에 큰 영향을 미칩니다. 너무 작거나 크게 설정할 경우 데이터의 패턴을 왜곡할 수 있으므로, 여러 `bin size` 그리드를 비교하며 적절한 크기를 찾는 것이 중요합니다.

**코드/수식 해설**
Hexbin 및 2D Histogram에서 각 `bin`에 포함된 데이터의 개수는 색상 강도($C$)로 인코딩됩니다. 이는 기본적으로 다음과 같은 매핑 함수를 통해 이루어집니다.
$$ C = f(\text{count}) $$
여기서 $\text{count}$는 특정 `bin` 내의 데이터 포인트 수이며, $f$는 색상 스케일을 정의하는 함수입니다 (예: `viridis`, `plasma` 등의 컬러맵). `count`가 높을수록 $C$는 더 강한 색상(또는 밝기)을 나타내어 밀도가 높음을 시각적으로 표현합니다.

**구체적 예시**
*   **인구 밀도 지도**: 특정 도시의 지리적 좌표(위도 $x$, 경도 $y$)를 $(x, y)$로 하고, 해당 지역의 인구 밀도를 나타내는 2D Histogram이나 Hexbin 플롯을 만들 수 있습니다. 인구가 밀집된 지역은 더 진한 색상으로 표시되어 한눈에 밀집 지역을 파악할 수 있습니다.
*   **주식 시장 데이터 분석**: 주식의 특정 두 지표 (예: 거래량 $x$와 종가 변동률 $y$) 사이의 관계를 Hexbin 플롯으로 시각화할 수 있습니다. 거래량이 많으면서 변동률이 큰 구간이 어디인지 `hotspot`을 통해 파악하여 투자 전략에 활용할 수 있습니다.

**강의 내용**
교수님의 음성 전사는 현재 슬라이드의 Hexbin 및 2D Histogram 내용과 직접적으로 일치하지 않으며, `stacked area plot`에 대해 설명하고 있습니다. 음성 전사의 주요 내용은 다음과 같습니다:
*   `hue` 매개변수를 `species`로, `multiple` 매개변수를 `fill`로 설정하여 `stacked area plot`을 생성합니다.
*   이 플롯에서는 모든 $x$ 값에서 전체 높이가 $100\%$로 정규화됩니다.
*   이러한 `stacked area plot`은 개별 분포의 모양을 보여주기보다는, 특정 `x` 값(예: `petal length`)에서 `species`별 구성 또는 비율을 보여주는 데 중점을 둡니다.

**시험 포인트**
*   ⭐ **Hexbin과 2D Histogram의 기본 정의 및 차이점**: 육각형(`Hexbin`)과 직사각형(`2D Histogram`) `bin`의 특징을 명확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ **사용 목적**: 데이터 포인트가 너무 많아 산점도가 밀집되어 있을 때, 데이터 밀도를 효과적으로 시각화하는 데 사용된다는 점을 기억하세요.
*   ⭐ **플롯 해석**: 색상의 강도(intensity)가 데이터의 빈도(count)를 나타내며, `hotspots`가 무엇을 의미하는지 해석할 수 있어야 합니다.
*   ⭐ **`Bin size`의 중요성**: `bin size`가 시각화 결과에 미치는 영향과, 여러 `bin size`로 비교하는 것의 필요성을 알아두세요.
*   강의 음성에서 언급된 `stacked area plot`도 중요한 시각화 기법이므로, 해당 플롯의 특징(특히 $100\%$ 정규화 및 구성/비율 표시)을 별도로 학습해두는 것이 좋습니다.

---
## Slide 20

---
### **핵심 개념**
*   **Hexbin Plot 및 2D Histogram (2차원 밀도 플롯)**: 두 개의 연속형 변수 간의 관계와 데이터 밀도를 시각화하는 데 사용됩니다. 데이터 포인트가 너무 많아 겹쳐서 분포를 파악하기 어려울 때, 특정 영역에 데이터가 얼마나 밀집해 있는지 색상 농도로 표현하여 효과적으로 패턴을 보여줍니다.
    *   **Hexbin Plot (`kind="hex"`)**: 데이터를 육각형(hexagonal) 모양의 격자로 나누어 각 격자 내 데이터 포인트의 개수를 색상으로 표시합니다.
    *   **2D Histogram (`kind="hist"`)**: 데이터를 사각형 모양의 격자(bins)로 나누어 각 격자 내 데이터 포인트의 개수를 색상으로 표시합니다.
*   **Pair Plot (다변량 플롯)**: (교수님 강의 내용에 따르면) 여러 변수 간의 모든 가능한 쌍별 관계를 한 번에 시각화하여 데이터의 전반적인 구조와 패턴을 빠르게 파악하는 데 사용되는 강력한 도구입니다.

### **코드/수식 해설**
주어진 슬라이드는 `seaborn` 라이브러리의 `jointplot` 함수를 사용하여 Hexbin 및 2D Histogram을 생성하는 예시 코드를 보여줍니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Wine 데이터셋에 대한 Hexbin Plot
# sns.jointplot(data=wine, x="alcohol", y="malic_acid", kind="hex")

# Diabetes 데이터셋에 대한 2D Histogram
# sns.jointplot(data=diabetes, x="bmi", y="target", kind="hist")
```
*   `sns.jointplot()`: 두 변수 간의 관계를 시각화하는 함수로, 메인 플롯과 함께 각 변수의 단변량 분포(히스토그램 또는 KDE)를 주변에 함께 보여줄 수 있습니다 (슬라이드 이미지에는 메인 플롯만 나와있음).
    *   `data`: 시각화할 데이터프레임.
    *   `x`, `y`: 각각 x축, y축에 사용할 컬럼 이름을 문자열로 지정합니다.
    *   `kind="hex"`: Hexbin 플롯을 생성하도록 지정합니다.
    *   `kind="hist"`: 2D Histogram을 생성하도록 지정합니다.

### **구체적 예시**
*   **Wine — Hexbin (counts)**: Wine 데이터셋에서 `alcohol` (알코올 함량)과 `malic_acid` (말산 함량) 변수 간의 관계를 Hexbin 플롯으로 시각화한 것입니다. 플롯의 색상 농도가 짙을수록 해당 `alcohol` 및 `malic_acid` 범위에 더 많은 데이터 포인트가 존재함을 나타냅니다. 예를 들어, `alcohol`이 약 13.5이고 `malic_acid`가 약 1.5인 지점에 데이터가 가장 밀집되어 있음을 노란색으로 확인할 수 있습니다.
*   **Diabetes — 2D Histogram**: Diabetes 데이터셋에서 `bmi` (체질량지수)와 `target` (질병 진행 정도) 변수 간의 관계를 2D Histogram으로 시각화한 것입니다. 각 사각형 셀의 색상 농도는 해당 `bmi` 및 `target` 범위에 있는 데이터 포인트의 개수를 나타냅니다. `bmi`가 0에 가깝고 `target`이 약 75인 영역에 데이터가 비교적 밀집되어 있음을 확인할 수 있습니다.
*   **Pair Plot의 구조 (강의 내용 기반)**: 만약 3개의 변수($V_1, V_2, V_3$)가 있다면, pair plot은 $3 \times 3$ 그리드를 생성합니다.
    *   대각선 셀($V_1$ vs $V_1$, $V_2$ vs $V_2$, $V_3$ vs $V_3$)을 제외한 모든 셀에는 가능한 모든 쌍별 변수 관계($V_1$ vs $V_2$, $V_1$ vs $V_3$, $V_2$ vs $V_3$ 등)의 산점도(scatter plot)가 그려집니다.

### **강의 내용**
*   교수님은 이 슬라이드 구간 이전에 "petal length"와 관련된 x축 문제에 대한 수정 계획을 언급하셨습니다.
*   ⭐ 교수님은 **Pair Plot**을 "**가장 중요하며(The most important), 다변량(multi-variate) 데이터를 볼 때 반드시 시도해야 할(you should try with) 플롯**"이라고 강력하게 강조하셨습니다.
*   Pair Plot은 "무식하지만(brute force) 엄청나게 효과적인(incredibly effective) 플롯"이라고 설명하셨습니다.
*   Pair Plot은 데이터를 시각화하기 위해 그리드 또는 행렬 형태로 생성되며, **대각선을 제외한 모든 셀은 가능한 모든 변수 쌍 간의 관계를 보여주는 산점도(scatter plot)로 구성**된다고 설명하셨습니다.

### **시험 포인트**
*   ⭐ **Hexbin Plot과 2D Histogram의 사용 목적 및 차이점**: 두 변수 간의 밀도 분포를 시각화하는 데 효과적이며, 각각 어떤 `kind` 옵션(`"hex"`, `"hist"`)을 사용하는지, 그리고 육각형과 사각형 bin의 시각적 차이점을 설명할 수 있어야 합니다.
*   ⭐ **Pair Plot의 중요성 및 특징**: 왜 다변량 데이터 분석 시 Pair Plot을 먼저 시도해야 하는지, 그리고 Pair Plot이 그리드/행렬 형태로 모든 가능한 변수 쌍의 관계(주로 산점도)를 보여준다는 핵심 구조를 이해하고 설명할 수 있어야 합니다. 교수님이 "가장 중요"하다고 강조한 부분입니다.
---

---
## Slide 21

### 2D KDE (2차원 커널 밀도 추정)

**핵심 개념**:
2D KDE (Kernel Density Estimate)는 두 개의 연속형 변수 $x$와 $y$의 **결합 확률 밀도 함수 (Joint Probability Density Function)**를 추정하고 시각화하는 비모수적 방법입니다. 이는 데이터 포인트가 특정 2차원 공간에 얼마나 밀집되어 있는지를 부드러운 형태로 보여줍니다.

*   **사용 목적**: 데이터의 밀도 구조, 즉 데이터가 집중되어 있는 영역(모드, modes), 특정 방향으로 길게 늘어진 형태(릿지, ridges) 등을 파악하는 데 유용합니다.
*   **해석 방법**: 2D KDE 결과는 등고선(contour) 형태로 주로 표현되며, 등고선의 봉우리(peaks)는 데이터 밀도가 높은 영역을 나타냅니다. 등고선 간의 간격은 밀도의 변화 기울기(gradient)를 반영합니다. 간격이 좁을수록 밀도 변화가 급격하다는 의미입니다.
*   **주의 사항 (Pitfalls)**: KDE의 성능은 **대역폭 (bandwidth)** 선택에 매우 민감합니다. 대역폭이 너무 작으면 과적합(overfitting)되어 노이즈가 많고 뾰족한 밀도 추정치가 나오며, 너무 크면 과소적합(underfitting)되어 데이터의 중요한 구조를 놓치고 너무 부드러운 추정치가 나옵니다. 적절한 대역폭 조절(`bw_adjust`)이 필수적입니다.

**코드/수식 해설**:
2차원 커널 밀도 추정의 수식은 다음과 같습니다.
$$
\hat{f}(x, y) = \frac{1}{nh_x h_y} \sum K_x\left(\frac{x-x_i}{h_x}\right)K_y\left(\frac{y-y_i}{h_y}\right)
$$
*   $\hat{f}(x, y)$: 주어진 점 $(x, y)$에서의 추정된 확률 밀도 값입니다.
*   $n$: 데이터 포인트의 총 개수입니다.
*   $h_x$, $h_y$: 각각 $x$축과 $y$축 방향의 **대역폭 (bandwidth)**으로, 커널 함수의 너비를 결정하여 밀도 추정의 부드러움 정도를 조절합니다.
*   $K_x(\cdot)$, $K_y(\cdot)$: 각각 $x$와 $y$ 방향에 적용되는 **커널 함수 (kernel function)**입니다. 일반적으로 가우시안 커널 (Gaussian kernel)이 많이 사용됩니다. 각 데이터 포인트 $(x_i, y_i)$ 주변에 작은 "언덕"을 만드는 역할을 합니다.
*   $\sum$: 모든 데이터 포인트 $i$에 대해 커널 함수의 기여도를 합산합니다.

이 수식은 각 데이터 포인트에 커널 함수를 적용한 후, 이 모든 커널 함수의 합을 데이터 개수와 대역폭의 곱으로 정규화하여 전체적인 밀도 함수를 추정하는 과정을 나타냅니다.

**구체적 예시**:
*   **실생활 비유**: 등고선 지도와 유사합니다. 지도의 등고선이 밀집된 곳은 산이 가파르고, 등고선이 듬성듬성한 곳은 완만한 경사를 가지듯이, 2D KDE의 등고선이 밀집된 곳은 데이터 밀도가 높고, 듬성듬성한 곳은 밀도가 낮습니다. 봉우리는 데이터가 가장 많이 모여있는 지점입니다.
*   **데이터 분석 예시**: 학생들의 '수학 점수'와 '물리 점수' 두 변수 간의 관계를 2D KDE로 시각화할 수 있습니다. 이를 통해 두 점수대가 동시에 높은 학생들의 밀집도를 파악하거나, 특정 점수대에서 데이터가 어떻게 분포하는지 직관적으로 확인할 수 있습니다. 일반적인 산점도(scatter plot)만으로는 데이터 포인트가 너무 많거나 겹쳐서 밀도를 파악하기 어려울 때 2D KDE가 특히 유용합니다. `seaborn.kdeplot` 함수 등을 통해 쉽게 구현할 수 있습니다.

**강의 내용**:
강의 음성 전사는 이전 슬라이드에서 다루어졌을 것으로 추정되는 **Pair Plot (산점도 행렬)**에 대한 설명으로 시작합니다.
*   교수님은 'feature 1, feature 2, and feature 3'과 같이 세 가지 특성(변수)이 있을 때 '9 plot' (즉, $3 \times 3$ 행렬 형태의 차트)이 생성됨을 언급합니다.
*   여기서 'diagonal cells' (대각선 셀)은 각 특성($F_1, F_2, F_3$)의 **단변량 분포 (univariate distribution)**를 보여줍니다. 예를 들어, 교수님은 'this cell indicates the univariate distribution for feature one'이라고 설명하며 대각선 셀이 각 단일 특성의 분포를 나타냄을 강조합니다. (예: 히스토그램이나 1D KDE).
*   이 슬라이드에서 다루는 **2D KDE**는 이와 대조적으로 Pair Plot의 **비대각선 셀**에서 두 특성 간의 **이변량 분포 (bivariate distribution)**를 부드럽게 추정하고 시각화하는 데 사용되는 핵심 기법입니다. 즉, $F_1$과 $F_2$, $F_1$과 $F_3$ 등의 관계를 밀도 형태로 보여주는 데 2D KDE가 활용됩니다.

**시험 포인트**:
*   ⭐ **2D KDE의 정의와 목적**을 정확히 이해하고 설명할 수 있어야 합니다. (두 변수의 결합 확률 밀도 함수 추정)
*   ⭐ **2D KDE 수식의 각 항 (n, $h_x, h_y$, $K_x, K_y$)의 의미**를 설명할 수 있어야 합니다. 특히 **대역폭 (bandwidth)**의 역할과 중요성을 강조할 수 있어야 합니다.
*   ⭐ 2D KDE 결과물인 **등고선 플롯 (contour plot)의 해석 방법**을 숙지해야 합니다. (봉우리는 고밀도 영역, 등고선 간격은 기울기)
*   ⭐ **대역폭 선택의 중요성**과 잘못된 대역폭 선택(과소/과대적합)이 결과에 미치는 영향 (`bw_adjust`의 필요성)을 이해해야 합니다.
*   다변량 시각화에서 **단변량 분포와 이변량 분포의 차이**를 구분하고, 2D KDE가 어느 부분에 활용되는지 (예: Pair Plot의 비대각선 셀) 이해하는 것이 중요합니다.

---
## Slide 22

**핵심 개념**
*   **2D Kernel Density Estimation (KDE)**: 두 연속형 변수(이변량)의 결합 확률 밀도 함수(Joint Probability Density Function)를 추정하고 이를 등고선(contour) 형태로 시각화하는 통계적 기법입니다. 데이터 포인트가 밀집된 영역은 높은 밀도로, 희소한 영역은 낮은 밀도로 표현하여 데이터의 분포 패턴과 군집을 파악하는 데 사용됩니다.
*   **`seaborn.jointplot`**: `seaborn` 라이브러리의 강력한 시각화 함수로, 두 변수 간의 관계를 중앙에 그리고 각 변수의 개별 분포를 주변에 함께 보여줍니다. `kind` 인자를 통해 중앙 플롯의 유형을 지정할 수 있으며, `kind="kde"`는 2D KDE 등고선 플롯을 생성합니다.

**코드/수식 해설**
```python
sns.jointplot(data=iris, x="sepal length (cm)", y="sepal width (cm)", kind="kde")
```
*   `sns`: `seaborn` 라이브러리를 가져올 때 일반적으로 사용하는 별칭입니다.
*   `data=iris`: 시각화할 데이터셋을 지정합니다. 여기서는 붓꽃(iris) 데이터셋을 사용합니다.
*   `x="sepal length (cm)"`: x축에 매핑될 데이터셋의 컬럼 이름을 지정합니다. 'sepal length (cm)' 변수입니다.
*   `y="sepal width (cm)"`: y축에 매핑될 데이터셋의 컬럼 이름을 지정합니다. 'sepal width (cm)' 변수입니다.
*   `kind="kde"`: `jointplot`의 중심(joint) 부분에 2D KDE 플롯을 그리도록 지정합니다. 이 옵션은 산점도(scatter plot) 대신 두 변수의 결합 밀도 분포를 등고선 형태로 보여줍니다.

**KDE의 원리 (2차원 확장)**:
KDE는 각 데이터 포인트 주변에 커널 함수(예: 가우시안 커널)를 배치하고, 이 커널들의 합을 통해 전체 데이터의 밀도를 추정합니다. 2차원 KDE에서는 2차원 커널 함수를 사용하며, 각 데이터 포인트 $(x_i, y_i)$가 해당 위치의 밀도에 기여합니다. 추정된 밀도 함수는 다음과 같이 표현될 수 있습니다:
$$ \hat{f}(x, y) = \frac{1}{n h_x h_y} \sum_{i=1}^n K\left(\frac{x - x_i}{h_x}, \frac{y - y_i}{h_y}\right) $$
여기서 $n$은 데이터 포인트의 개수, $K$는 2차원 커널 함수, $h_x$와 $h_y$는 각각 x축과 y축 방향의 대역폭(bandwidth)입니다.

**구체적 예시**
*   슬라이드에 표시된 "Iris — 2D KDE (contours)" 플롯은 아이리스 데이터셋의 'sepal length'와 'sepal width' 간의 결합 밀도 분포를 보여줍니다.
*   **등고선 해석**: 컨투어 라인(등고선)은 동일한 밀도를 가진 지점들을 연결한 것입니다. 플롯에서 숫자가 라벨링된 등고선들은 추정된 밀도 값을 나타냅니다 (예: $0.050$, $0.100$, $0.150$, ...). 밀도 값이 높은 영역일수록 데이터 포인트들이 더 많이 집중되어 있음을 의미하며, 일반적으로 더 짙거나 따뜻한 색상(초록색, 노란색)으로 표현됩니다.
*   **군집 식별**: 이 플롯을 보면 'sepal length'와 'sepal width'의 조합에서 데이터가 크게 두 개의 뚜렷한 밀집 영역, 즉 두 개의 군집으로 나뉘어 분포하고 있음을 명확히 확인할 수 있습니다. 하나는 'sepal length'가 작고 'sepal width'가 큰 영역(좌측 상단), 다른 하나는 'sepal length'가 크고 'sepal width'가 작은 영역(우측 하단)입니다.

**강의 내용**
*   교수님은 이러한 플롯을 데이터 분석의 시작 단계에서 "all pairwise associations"를 빠르게 스캔하고 "clusters"를 찾기 위해 사용한다고 강조했습니다.
*   특히, 이 2D KDE 플롯을 통해 "which features are best at separating your label data"를 파악할 수 있다고 설명했습니다. 즉, 어떤 특징들의 조합이 데이터를 효과적으로 분류하는 데 도움이 되는지 시각적으로 확인할 수 있다는 것입니다.
*   강의에서는 'sepal length'와 'sepal width'의 조합이 데이터를 "into the two" (두 개의 그룹)으로 "very clear"하게 분리할 수 있는 "good combination of features"라고 명확히 언급했습니다. 이는 슬라이드의 2D KDE 플롯에서 두 개의 뚜렷한 밀도 군집이 나타나는 것과 직접적으로 연결됩니다. 이러한 시각적 분리는 머신러닝 모델링 시 특징 선택(feature selection)의 중요한 근거가 될 수 있습니다.

**시험 포인트**
*   ⭐ **2D KDE의 핵심 목적**: 두 변수의 결합 분포에서 데이터의 밀집 영역과 군집을 시각적으로 파악하는 데 사용됨을 이해해야 합니다.
*   ⭐ **`jointplot`의 `kind="kde"` 옵션**: `seaborn.jointplot`에서 `kind` 인자를 `kde`로 설정할 때 어떤 종류의 시각화가 생성되는지, 그리고 그 특징(등고선)을 알고 있어야 합니다.
*   ⭐ **2D KDE 플롯 해석 능력**: 플롯에 나타난 등고선이 무엇을 의미하는지(밀도), 밀도 차이가 어떻게 데이터의 군집을 보여주는지 해석할 수 있어야 합니다.
*   ⭐ **탐색적 데이터 분석(EDA)에서의 활용**: 2D KDE와 같은 시각화가 데이터의 특징(feature) 조합이 레이블 데이터를 얼마나 잘 분리할 수 있는지(예: 아이리스 종 분류)를 직관적으로 파악하는 데 어떻게 기여하는지 중요하게 다뤄질 수 있습니다.

---
## Slide 23

## 데이터분석 입문 (CSED226) 강의 노트: 버블 플롯 & 클러스터맵

### 핵심 개념

*   **버블 플롯 (Bubble Plot)**
    *   **정의**: 두 개의 수치형 변수($X$, $Y$) 간의 관계를 산점도(scatter plot)로 표현하되, 각 마커(점)의 **크기(size)**를 이용해 **세 번째 수치형 변수**를 인코딩하는 시각화 기법입니다. 필요에 따라 **색상(hue)**을 사용하여 범주형 변수를 표현할 수도 있습니다.
    *   **사용 시점**: 두 변수 $X, Y$의 관계를 보여주면서 동시에 각 데이터 포인트의 **크기(magnitude)**를 비교하고자 할 때 유용합니다.
*   **클러스터맵 (ClusterMap)**
    *   **정의**: 일반적인 히트맵(heatmap)보다 발전된 형태로, 행(row)과 열(column)에 **계층적 클러스터링(hierarchical clustering)** 알고리즘을 적용하여 유사성에 따라 데이터를 재정렬한 후 그리는 히트맵입니다.
    *   **목적**: 데이터 내에 숨겨진 **"블록(blocks)" 또는 "모듈(modules)"**과 같은 패턴이나 구조를 파악하고자 할 때 사용됩니다.

### 코드/수식 해설

*   **버블 플롯 구현 (Python, `seaborn` 예시)**
    버블 플롯은 주로 `matplotlib`의 `scatter` 함수나 `seaborn`의 `scatterplot` 또는 `relplot` 함수를 사용하여 구현합니다. 특히 `size` 인자를 통해 세 번째 변수를 마커 크기에 매핑합니다.

    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    # 예시 데이터 생성
    data = {
        'X_variable': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Y_variable': [10, 8, 6, 7, 5, 3, 4, 2, 1, 0],
        'Size_variable': [100, 200, 300, 250, 150, 400, 50, 350, 280, 120],
        'Category_variable': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C']
    }
    df = pd.DataFrame(data)

    # seaborn을 이용한 버블 플롯
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x='X_variable',
        y='Y_variable',
        size='Size_variable',  # 세 번째 변수를 마커 크기로 인코딩
        hue='Category_variable', # 범주형 변수를 색상으로 인코딩 (선택 사항)
        sizes=(20, 1000),      # 마커 크기 범위 설정
        alpha=0.7,             # 투명도 설정
        legend='full',         # 범례 표시
        data=df
    )
    plt.title('Bubble Plot Example')
    plt.xlabel('X Variable')
    plt.ylabel('Y Variable')
    plt.show()
    ```

*   **클러스터맵의 계층적 클러스터링 개념**:
    클러스터맵은 행과 열에 독립적으로 계층적 클러스터링을 적용합니다. 이는 데이터를 재배열하여 유사한 행(예: 유사한 특성을 가진 샘플)과 유사한 열(예: 유사한 패턴을 보이는 변수)이 서로 옆에 오도록 합니다. 계층적 클러스터링은 다음과 같은 단계를 거칩니다.
    1.  각 데이터 포인트를 하나의 클러스터로 간주합니다.
    2.  가장 가까운 두 클러스터를 병합합니다. (가까움의 기준은 거리 측정 방법: 유클리드 거리, 코사인 유사도 등)
    3.  모든 데이터 포인트가 하나의 클러스터로 병합될 때까지 2단계를 반복합니다.
    4.  이 병합 과정을 덴드로그램(dendrogram)으로 시각화하며, 이를 바탕으로 히트맵의 행과 열을 재정렬합니다.

### 구체적 예시

*   **버블 플롯 예시**:
    세계 각국의 **GDP ($X$)**, **기대 수명 ($Y$)**, 그리고 **인구 수 ($Size$)** 간의 관계를 시각화할 때 버블 플롯을 사용할 수 있습니다. 각 국가를 하나의 버블로 표현하고, 버블의 $X$축 위치는 GDP, $Y$축 위치는 기대 수명, 버블의 크기는 인구 수를 나타내게 됩니다. 추가적으로 대륙별로 버블의 색상을 다르게 할 수도 있습니다. 이를 통해 GDP가 높을수록 기대 수명도 높은 경향이 있는지, 그리고 인구가 많은 국가들의 특징은 무엇인지 등을 한눈에 파악할 수 있습니다.

*   **클러스터맵 예시**:
    유전자 발현(gene expression) 데이터에서 클러스터맵이 유용하게 사용됩니다. 행은 유전자, 열은 다른 샘플(환자 또는 조직)을 나타내고, 각 셀은 특정 유전자의 발현 수준을 나타냅니다. 클러스터맵은 유사한 발현 패턴을 보이는 유전자들(행 클러스터링)과 유사한 발현 특징을 가진 샘플들(열 클러스터링)을 자동으로 묶어줍니다. 이를 통해 특정 질병과 관련된 유전자 그룹이나 질병의 아형(subtype)을 발견하는 데 도움을 줄 수 있습니다. 예를 들어, 특정 유전자 그룹이 특정 환자 그룹에서 함께 높은 발현을 보이는 "블록" 패턴을 시각적으로 확인할 수 있습니다.

### 강의 내용

*   교수님께서는 슬라이드의 주요 내용인 버블 플롯과 관련하여, 사람이 면적을 인식하는 방식이 비선형적(nonlinear)이므로, 버블 플롯 사용 시 **범례(legend)를 반드시 포함**하고 **크기 범위가 너무 크지 않도록 주의**해야 한다고 강조하셨습니다. (Pitfalls 부분)

*   이번 슬라이드 구간에서는 데이터 시각화 기법 중 **클러스터맵(ClusterMap)**에 대해서도 상세히 설명해주셨습니다.
    *   클러스터맵은 일반적인 히트맵보다 "더 똑똑한(smarter)" 히트맵이라고 언급하셨습니다.
    *   일반 히트맵은 숫자의 행렬을 있는 그대로 플롯하지만, 클러스터맵은 먼저 **행과 열 모두에 계층적 클러스터링 알고리즘을 실행**하여 유사성을 기반으로 행과 열을 **재정렬**합니다.
    *   이러한 재정렬을 통해 유사한 열과 유사한 행이 서로 옆에 배치되게 하여, 데이터 내에 숨겨진 **"블록(blocks)" 또는 "모듈(modules)"을 의심할 때** 유용하다고 설명하셨습니다. 이는 데이터의 패턴과 구조를 직관적으로 파악하는 데 큰 도움을 줍니다.

*   클러스터맵 설명 전에 데이터의 **두 클래스 분류**와 **페어 플롯(pair plot)**에 대해서도 잠시 언급하셨는데, 이는 다양한 다변량 시각화 기법들을 상기시키거나 클러스터맵의 맥락을 제공하기 위함으로 보입니다.

### 시험 포인트

*   ⭐ **버블 플롯의 3가지 인코딩 요소**를 정확히 이해하고 설명할 수 있어야 합니다: 위치($x, y$), 크기(세 번째 값), 색상(그룹).
*   ⭐ 버블 플롯 사용 시 **주의해야 할 점(Pitfalls)**: 사람의 면적 인식 비선형성, 범례 포함의 중요성, 과도한 크기 범위 회피.
*   ⭐ **클러스터맵이 일반 히트맵과 다른 점**은 무엇이며, 어떤 과정을 통해 데이터 내의 "숨겨진 블록이나 모듈"을 찾아내는지 (계층적 클러스터링 및 재정렬) 설명할 수 있어야 합니다.
*   ⭐ **클러스터맵의 주요 목적**: 데이터 내의 유사성 기반 패턴, 그룹, 모듈 등을 발견하는 데 활용됨.

---
## Slide 24

- **핵심 개념**:
    *   **버블 플롯 (Bubble Plot)**: 일반적인 산점도(scatter plot)의 확장으로, 두 개의 수치형 변수 간의 관계를 $x$축과 $y$축으로 표현하는 동시에, 세 번째 수치형 변수의 값을 각 점의 크기(`size`)로 나타내어 3차원 정보를 2차원 평면에 시각화하는 기법입니다. 여기에 추가적으로 네 번째 변수(주로 범주형)를 색상(`hue`)으로 나타내어 다차원 데이터를 한 번에 탐색할 수 있도록 돕습니다. 이는 데이터 내 여러 변수 간의 복합적인 관계나 특정 그룹의 패턴을 파악하는 데 매우 유용합니다.

- **코드/수식 해설**:
    *   `seaborn` 라이브러리의 `scatterplot` 함수를 사용하여 버블 플롯을 생성하는 코드입니다.
    ```python
    import seaborn as sns

    sns.scatterplot(data=wine, x="alcohol", y="malic_acid",
                    size="proline", hue="class", alpha=0.6)
    ```
    *   `data=wine`: 시각화에 사용할 데이터프레임을 지정합니다. 여기서는 `wine` 데이터셋을 사용합니다.
    *   `x="alcohol"`: $x$축에 매핑할 변수로, 와인의 `alcohol` (알코올 함량) 특성을 사용합니다.
    *   `y="malic_acid"`: $y$축에 매핑할 변수로, 와인의 `malic_acid` (말산 함량) 특성을 사용합니다.
    *   `size="proline"`: 각 점의 크기를 결정하는 변수로, 와인의 `proline` (프롤린 함량) 특성을 사용합니다. `proline` 값이 클수록 해당 점의 크기가 커집니다.
    *   `hue="class"`: 각 점의 색상을 결정하는 변수로, 와인의 `class` (와인 종류) 특성을 사용합니다. 이를 통해 각 `class`별로 다른 색상으로 표현되어 시각적으로 구분됩니다.
    *   `alpha=0.6`: 점의 투명도를 설정합니다. `0.6`은 점들이 겹쳐 보일 때 뒤쪽 점을 어느 정도 볼 수 있도록 하여 밀집도를 파악하는 데 도움을 줍니다.

- **구체적 예시**:
    *   첨부된 슬라이드의 플롯은 와인 데이터셋에서 `alcohol` (알코올 함량)과 `malic_acid` (말산 함량)의 관계를 보여주면서, 동시에 `proline` (프롤린 함량)을 점의 크기로, `class` (와인 종류)를 색상으로 나타내고 있습니다.
    *   예를 들어, `class_0` (주황색 'x' 표시)에 속하는 와인들은 `alcohol` 함량이 비교적 높고 `malic_acid` 함량은 다양한 분포를 보이며, `proline` 함량(점의 크기)도 크게 나타나는 경향이 있음을 한눈에 파악할 수 있습니다. 반면 `class_1` (하늘색 'x' 표시) 와인들은 `alcohol` 함량이 낮고 `proline` 함량(점의 크기)도 작은 경향을 보입니다. 이처럼 버블 플롯을 통해 와인 종류별로 `alcohol`, `malic_acid`, `proline` 세 가지 특성의 복합적인 관계와 패턴을 효과적으로 탐색할 수 있습니다.

- **강의 내용**:
    *   교수님은 이러한 시각화 기법이 "함께 움직이는 특성 그룹이나 유사한 프로필 또는 상관관계를 가진 샘플 그룹을 찾는 데 매우 유용하다"고 강조했습니다. 이는 다변량 데이터를 분석하여 숨겨진 패턴이나 군집을 발견하는 데 시각화가 핵심적인 역할을 한다는 점을 나타냅니다.
    *   이어서 교수님은 데이터 내 유사성을 찾는 또 다른 방법으로 **덴드로그램(dendrogram)**과 **상관관계 행렬(correlation matrix)**을 언급했습니다. 특히, 상관관계를 계산하기 위해서는 모든 특성(feature)이 반드시 **수치형(numerical)**이어야 하며, 이를 위해 상관계수를 계산하기 전에 **범주형(categorical) 특성들은 반드시 제외(drop)해야 한다**는 중요한 전처리 단계를 강조했습니다. 이는 데이터 분석 시 데이터 타입에 대한 정확한 이해와 적절한 전처리의 중요성을 시사합니다.

- **시험 포인트**:
    *   ⭐ **버블 플롯의 다변량 시각화 원리**: `x`, `y`, `size`, `hue` 등 `sns.scatterplot` 함수의 다양한 인자들이 각각 어떤 변수를 시각화하는 데 사용되는지 정확히 이해하고 설명할 수 있어야 합니다. 특히, `size`와 `hue` 인자를 통해 추가적인 차원을 시각화하는 방법을 아는 것이 중요합니다.
    *   ⭐ **상관관계 분석을 위한 데이터 전처리**: 상관계수를 계산할 때 **범주형 변수를 제외하고 오직 수치형 변수만 사용해야 하는 이유**를 명확히 설명할 수 있어야 합니다. 이는 데이터 분석의 기본적인 전처리 지식입니다.
    *   ⭐ 다변량 데이터에서 특성(feature)이나 샘플(sample) 간의 **유사성(similarity) 또는 상관관계(correlation)를 탐색하는 것의 중요성**을 이해하고, 이를 위한 시각화 및 분석 기법(예: 버블 플롯, 덴드로그램, 상관관계 행렬)의 기본적인 개념을 파악해야 합니다.

---
## Slide 25

## Box Plot: 정의 및 활용

### 핵심 개념
이 슬라이드는 **Box Plot (상자 수염 그림)**의 정의와 활용법, 그리고 그 한계점을 설명합니다. Box Plot은 데이터의 분포와 주요 통계량을 시각화하여 여러 그룹 간의 비교를 용이하게 하는 데 사용됩니다.

*   **정의**:
    *   **중앙선 (Median line)**: 데이터의 중앙값($Q_2$)을 나타냅니다.
    *   **상자 (Box)**: 1사분위수($Q_1$)부터 3사분위수($Q_3$)까지의 범위를 나타내며, 이는 **사분위 범위(IQR: InterQuartile Range)**와 같습니다.
    *   **수염 (Whiskers)**: 일반적으로 $Q_1 - 1.5 \times \text{IQR}$부터 $Q_3 + 1.5 \times \text{IQR}$까지의 범위 내에 있는 데이터의 최소/최대값을 나타냅니다.
    *   **이상치 (Outliers)**: 수염의 범위를 벗어나는 개별 데이터 포인트들을 나타냅니다.

*   **언제 사용하는가 (Use when)**: 위치(중앙값)와 퍼짐(IQR)에 대한 견고한 그룹 비교가 필요할 때 사용됩니다.
*   **읽는 방법 (How to read)**:
    *   중앙선(Median)의 위치 변화: 그룹 간 중앙값의 차이를 파악합니다.
    *   상자(IQR)의 너비: 그룹 간 데이터의 퍼짐(분산) 정도를 비교합니다.
    *   이상치 개수: 비정상적인 데이터 포인트의 존재 여부와 그 수를 확인합니다.
*   **주의할 점 (Pitfalls)**:
    *   다봉성(multimodality) 분포를 숨길 수 있습니다. (예: 두 개 이상의 봉우리가 있는 분포를 하나의 상자로 표현)
    *   사용된 수염 규칙을 명확히 문서화해야 합니다 (예: $1.5 \times \text{IQR}$ 규칙).

### 코드/수식 해설
*   **IQR (InterQuartile Range)**: 데이터의 3사분위수($Q_3$)와 1사분위수($Q_1$)의 차이로 정의됩니다.
    $$ \text{IQR} = Q_3 - Q_1 $$
*   **수염 (Whiskers)**의 일반적인 범위는 다음과 같습니다.
    *   상한선: $\min(\text{최대값}, Q_3 + 1.5 \times \text{IQR})$
    *   하한선: $\max(\text{최소값}, Q_1 - 1.5 \times \text{IQR})$

**예시 코드 (Python Matplotlib)**:
```python
import matplotlib.pyplot as plt
import numpy as np

# 가상의 데이터 생성
data_group1 = np.random.normal(0, 1, 100)
data_group2 = np.random.normal(2, 1.5, 100) + np.random.normal(5, 0.5, 20) # 다봉성 예시

plt.boxplot([data_group1, data_group2], labels=['Group 1', 'Group 2'])
plt.title('Box Plot Example')
plt.ylabel('Value')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

### 구체적 예시
어떤 반 학생들의 중간고사 점수를 비교하는 상황을 가정해 봅시다.
*   **A반 점수**: [60, 65, 70, 75, 80, 85, 90, 95, 100]
*   **B반 점수**: [40, 50, 60, 70, 80, 90, 100, 110(이상치)]

A반의 Box Plot은 중앙값이 80점 근처, IQR은 20점 정도이고 이상치가 없습니다.
B반의 Box Plot은 중앙값이 75점 근처, IQR은 40점 정도로 A반보다 넓으며, 110점이라는 이상치가 명확히 표시될 것입니다. 이를 통해 B반은 A반보다 점수 분포가 넓고 고득점 이상치가 있다는 것을 한눈에 파악할 수 있습니다.

### 강의 내용
교수님께서는 슬라이드의 Box Plot 설명 이후, 다음 내용으로 넘어가시며 다른 시각화 기법에 대해 언급하셨습니다. (강의 음성 전사 내용은 현재 슬라이드 이미지와는 다른 주제를 다루고 있습니다.)

1.  **Cluster Map**: "이것을 클러스터 맵이라고 부를 것입니다. 그리고 이 속성들은 유사성을 기반으로 재정렬됩니다. X축도 마찬가지입니다."
    *   이는 일반적으로 **히트맵(Heatmap)**에 **계층적 클러스터링(Hierarchical Clustering)**을 적용하여 행과 열을 유사성에 따라 재배열함으로써 패턴을 더 쉽게 식별할 수 있도록 하는 시각화 기법을 지칭합니다.

2.  **Hex Bin 및 2D Histogram**: "Hex bin과 2D histogram으로 넘어갑시다. 산점도를 사용하면 오버플로팅(over plotting) 문제가 발생합니다. 예를 들어, 100,000개의 점이 있다면 어떨까요? 개별 점을 그리는 대신 2D 비닝(beaming, 즉 binning)을 사용할 수 있습니다. 이것을 2D 히스토그램이라고 합니다. 우리는 $xy$ 평면을 육각형 또는 직사각형 모양의 빈(bin) 격자로 분할합니다."
    *   **오버플로팅 문제**: 산점도(scatterplot)에서 데이터 포인트의 수가 매우 많을 때 (예: 100,000개), 점들이 서로 겹쳐져 데이터의 밀도나 패턴을 파악하기 어려워지는 문제입니다.
    *   **해결책 (2D 비닝/2D 히스토그램)**: 개별 점을 그리는 대신, $xy$ 평면을 일정한 크기의 격자(grid of bins)로 나누고, 각 격자 안에 포함된 데이터 포인트의 수를 색상이나 음영으로 표현하여 데이터 밀도를 시각화합니다. 이 격자는 육각형(hex bin)이 될 수도 있고 직사각형(2D histogram)이 될 수도 있습니다.

### 시험 포인트
*   ⭐ **Box Plot의 구성 요소 (중앙값, IQR, 수염, 이상치)를 정확히 정의하고 설명할 수 있어야 합니다.** 특히 IQR과 수염의 $1.5 \times \text{IQR}$ 규칙은 중요합니다.
*   ⭐ **Box Plot이 언제 유용하게 사용되는지 (그룹 간 위치/퍼짐 비교) 이해하고, 어떤 한계점(다봉성 숨김)이 있는지 알아야 합니다.**
*   ⭐ **산점도의 '오버플로팅 문제'가 무엇이며, 이를 해결하기 위한 '2D 히스토그램' 또는 'Hex Bin'의 원리를 설명할 수 있어야 합니다.**

---
## Slide 26

---

### **핵심 개념**
이 슬라이드는 **박스 플롯(Box Plot)**을 사용하여 범주형 변수에 따른 연속형 변수의 분포를 시각화하는 방법을 설명합니다. 박스 플롯은 데이터의 중앙값, 사분위수, 데이터의 퍼짐 정도(산포), 그리고 이상치(outliers)를 한눈에 파악할 수 있게 해주는 강력한 도구입니다.

### **코드/수식 해설**

**1. `sns.boxplot()` 코드:**
```python
sns.boxplot(data=wine, x="class", y="alcohol", showfliers=True, whis=1.5)
```
*   `sns.boxplot()`: Seaborn 라이브러리의 박스 플롯을 그리는 함수입니다.
*   `data=wine`: 시각화에 사용할 데이터셋을 지정합니다. 여기서는 `wine` 데이터프레임을 사용합니다.
*   `x="class"`: x축에 해당하는 변수입니다. 범주형 변수인 와인의 `class` (예: `class_0`, `class_1`, `class_2`)를 나타냅니다. 각 클래스별로 박스 플롯이 그려집니다.
*   `y="alcohol"`: y축에 해당하는 변수입니다. 연속형 변수인 와인의 `alcohol` (알코올 함량)을 나타냅니다. 각 클래스별 알코올 함량의 분포가 이 변수를 통해 시각화됩니다.
*   `showfliers=True`: 이상치(outliers)를 점으로 표시할지 여부를 지정합니다. `True`로 설정하면 이상치가 그래프에 나타납니다.
*   `whis=1.5`: 이상치를 결정하는 기준이 되는 '위스커(whisker)'의 길이를 설정합니다. 기본값으로 1.5를 많이 사용합니다. 이 값은 사분위 범위(InterQuartile Range, IQR)의 몇 배를 위스커의 최댓값/최솟값으로 설정할지 정합니다.

**2. 박스 플롯의 주요 구성 요소 및 수식:**
박스 플롯은 다음과 같은 5가지 주요 통계량(five-number summary)을 시각적으로 나타냅니다.
*   **중앙값 (Median, $Q2$)**: 상자 안의 선으로 표시되며, 데이터를 오름차순으로 정렬했을 때 중앙에 위치하는 값입니다. 50번째 백분위수입니다.
*   **하위 사분위수 (First Quartile, $Q1$)**: 상자의 아랫부분입니다. 데이터의 25번째 백분위수입니다.
*   **상위 사분위수 (Third Quartile, $Q3$)**: 상자의 윗부분입니다. 데이터의 75번째 백분위수입니다.
*   **사분위 범위 (InterQuartile Range, IQR)**: 상자의 높이로, $Q3 - Q1$ 값입니다. 데이터의 중간 50%가 분포하는 범위입니다.
    $$ IQR = Q3 - Q1 $$
*   **위스커 (Whiskers)**: 상자에서 뻗어 나가는 선으로, 이상치가 아닌 데이터의 최대/최소 범위를 나타냅니다.
    *   상위 위스커의 끝: $\min(Q3 + \text{whis} \times IQR, \text{데이터 중 } Q3 + \text{whis} \times IQR \text{보다 작은 최댓값})$
    *   하위 위스커의 끝: $\max(Q1 - \text{whis} \times IQR, \text{데이터 중 } Q1 - \text{whis} \times IQR \text{보다 큰 최솟값})$
*   **이상치 (Outliers)**: 위스커 바깥에 있는 개별 데이터 포인트들로 점으로 표시됩니다. `whis=1.5`일 경우, $Q3 + 1.5 \times IQR$보다 크거나 $Q1 - 1.5 \times IQR$보다 작은 값들이 해당됩니다.

### **구체적 예시**
슬라이드의 그림은 `wine` 데이터셋의 세 가지 `class` (`class_0`, `class_1`, `class_2`) 각각에 대한 `alcohol` 함량의 분포를 박스 플롯으로 보여줍니다.
*   **`class_0`**: 알코올 함량의 중앙값과 전체적인 분포가 세 클래스 중 가장 높은 편입니다. 박스의 크기(IQR)는 중간 정도입니다.
*   **`class_1`**: 알코올 함량의 중앙값과 분포가 세 클래스 중 가장 낮은 편입니다. 또한, 상위 위스커 위에 여러 개의 이상치(동그란 점들)가 관찰됩니다. 이는 `class_1` 와인 중 알코올 함량이 매우 높은 몇몇 예외적인 경우가 있음을 나타냅니다.
*   **`class_2`**: 알코올 함량 분포가 `class_0`과 `class_1`의 중간 정도이며, 박스의 크기는 세 클래스 중 가장 작아 데이터의 분포가 비교적 좁다는 것을 알 수 있습니다.

이처럼 박스 플롯을 통해 각 와인 클래스별 알코올 함량의 중심 경향, 산포, 그리고 특이점들을 쉽게 비교하고 해석할 수 있습니다.

### **강의 내용**
교수님의 음성 전사 내용은 현재 슬라이드에 제시된 **박스 플롯과는 다른 시각화 기법**인 **2D 밀도 맵(density map) 또는 헥스빈 플롯(hexbin plot)**에 대한 설명으로 보입니다. 이는 조밀한 산점도(dense scatterplot)에서 데이터 분포를 시각화하는 데 유용합니다.

음성에서 강조된 내용은 다음과 같습니다:
*   **조밀한 산점도의 문제 해결**: 데이터 포인트가 너무 많아 겹쳐 보일 때 (overplotting), 각 영역에 얼마나 많은 포인트가 밀집되어 있는지 시각화하기 위해 사용됩니다. 이는 산점도의 한계를 극복하는 직접적인 해결책입니다.
*   **2D 밀도 맵 생성 원리**: 그래프 영역을 여러 개의 '빈(bin)' 또는 '그리드(grid)'로 나눕니다. 각 빈에 속하는 데이터 포인트의 수를 계산하고, 이 개수를 **색상 강도(color intensity)**로 표현합니다. 포인트 수가 많을수록 색상이 더 진하게 표시되어 밀집도를 나타냅니다.
*   **"Hot Spots" 파악**: 가장 어둡거나 강렬한 색상을 가진 빈(hex bean)은 데이터가 가장 많이 집중된 영역, 즉 "핫 스팟(hot spots)"을 의미합니다. 이를 통해 데이터의 핵심 분포 지역을 시각적으로 쉽게 식별할 수 있습니다.
*   **⭐빈 크기(Bin Size) 또는 그리드 크기(Grid Size)의 중요성**: 2D 밀도 맵의 시각화 결과는 빈 또는 그리드의 크기에 매우 민감하게 반응합니다.
    *   **빈 크기가 너무 작으면**: 데이터의 노이즈가 강조되어 전반적인 패턴을 파악하기 어려울 수 있습니다.
    *   **빈 크기가 너무 크면**: 중요한 미세한 패턴이나 특징을 놓칠 수 있습니다.
    적절한 빈 크기 선택이 데이터의 실제 분포를 정확하고 효과적으로 나타내는 데 중요합니다.

이러한 2D 밀도 맵은 `matplotlib.pyplot.hexbin`이나 `seaborn.jointplot(kind='hex')` 등 다양한 라이브러리 함수를 통해 구현할 수 있습니다.

### **시험 포인트**
*   ⭐**박스 플롯의 구성 요소 (중앙값, 사분위수, 위스커, 이상치)와 각각이 의미하는 통계적 개념을 정확히 설명할 수 있어야 합니다.** 특히 $IQR$과 이상치 판단 기준 (예: $Q3 + 1.5 \times IQR$)을 이해하는 것이 중요합니다.
*   ⭐`sns.boxplot()` 함수의 `x`, `y`, `showfliers`, `whis` 인자가 그래프에 어떤 영향을 미치는지 코드를 보고 설명하거나 직접 구현할 수 있어야 합니다.
*   ⭐(음성 전사 내용 관련) 데이터 포인트가 매우 조밀한 산점도에서 발생하는 과밀화(overplotting) 문제를 해결하기 위해 **2D 밀도 맵 (헥스빈 플롯 등)이 사용되는 이유와 기본적인 작동 원리 (빈 카운트 및 색상 강도)**를 설명할 수 있어야 합니다.
*   ⭐**2D 밀도 맵에서 빈 크기(bin size)가 시각화 결과에 미치는 영향**에 대해 설명하고, 적절한 빈 크기 설정의 중요성을 강조할 수 있어야 합니다.

---
## Slide 27

**핵심 개념**:
*   **바이올린 플롯(Violin Plot)**: 데이터의 분포를 시각화하는 방법 중 하나입니다. 커널 밀도 추정(KDE, Kernel Density Estimation) 결과를 중앙선을 기준으로 대칭적으로 표현한 엔벨로프(envelope) 형태를 가집니다. 엔벨로프 내부에는 사분위수(quartiles) 또는 중앙값(median)을 나타내는 마크(선)가 포함될 수 있습니다.
*   **사용 시점**: 그룹별 데이터 분포의 **형태(shape)**, 즉 왜도(skew), 꼬리(tails), 다봉성(multimodality) 등을 시각적으로 명확하게 파악하고자 할 때 유용합니다.
*   **해석 방법**: 플롯의 **너비는 데이터 밀도에 비례($\text{Width} \propto \text{density}$)**합니다. 즉, 너비가 넓은 구간은 해당 값 범위에 더 많은 데이터 포인트가 존재함을 의미합니다. 여러 바이올린 플롯을 나란히 배치하여 각 그룹의 분포 너비를 비교함으로써 분포의 차이를 파악할 수 있습니다.
*   **주의사항**: KDE의 대역폭(bandwidth) 선택이 매우 중요하며, 데이터 포인트 수($n$)가 적을 때는 플롯 상의 작은 봉우리(bumps)를 과해석하지 않도록 유의해야 합니다.

**강의 내용**:
교수님께서는 바이올린 플롯의 내용과 더불어, 데이터 시각화 전반에 걸쳐 **빈(bin) 크기**의 중요성을 강조하셨습니다.
*   **빈 크기 조절의 중요성**: "빈이 너무 크면 모든 세부 정보를 잃게 되고, 너무 작으면 플롯이 듬성듬성하고 노이즈처럼 보일 수 있습니다."라고 언급하며, 적절한 빈 크기 설정이 데이터의 실제 분포 특성을 왜곡 없이 보여주는 데 필수적임을 강조하셨습니다.
*   **헥스 빈 플롯(Hex Bin Plot) 언급**: 특정 슬라이드 내용을 지칭하는 것이 아닐 수 있으나, 교수님께서는 헥스 빈 플롯을 예시로 들며 2차원 분포 시각화에 대해 언급하셨습니다. 헥스 빈 플롯은 데이터를 육각형(hexagon) 모양의 셀로 나누어 각 셀에 해당하는 데이터의 밀도를 색상 농도로 표현하는 방식입니다.
*   `jointplot` 활용: `seaborn` 라이브러리의 `jointplot` 함수에서 `kind='hex'` 또는 `kind='hist'` 옵션을 사용하여 2차원 데이터를 시각화할 수 있음을 설명하셨습니다. 현재 슬라이드가 2차원 플롯이나 헥스 빈 플롯을 직접적으로 다루지 않아 다소 혼란스러울 수 있다는 점도 덧붙이셨습니다.

**코드/수식 해설**:
바이올린 플롯의 기반이 되는 커널 밀도 추정(KDE)의 일반적인 수식은 다음과 같습니다.
$$\hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right)$$
여기서 $\hat{f}_h(x)$는 $x$에서의 밀도 추정치, $n$은 데이터 포인트의 수, $h$는 대역폭(bandwidth) 또는 스무딩(smoothing) 매개변수, 그리고 $K$는 커널 함수(예: 가우시안 커널)를 나타냅니다. 바이올린 플롯은 이 KDE 결과를 중앙값을 기준으로 대칭적으로 표현합니다.

강의에서 언급된 `seaborn.jointplot`을 사용하여 헥스 빈 플롯을 생성하는 예시는 다음과 같습니다.
```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 예시 데이터 생성
np.random.seed(42)
x = np.random.randn(1000)
y = np.random.randn(1000) + x * 0.5 # x와 y 간의 약한 상관관계 부여

# jointplot을 사용하여 hex bin plot 생성
sns.jointplot(x=x, y=y, kind='hex', height=6, ratio=5, cmap='Blues')
plt.suptitle("Hex Bin Plot Example (kind='hex')", y=1.02)
plt.show()

# jointplot을 사용하여 2D 히스토그램 (marginal histograms) 예시
# sns.jointplot(x=x, y=y, kind='hist', height=6, ratio=5, cmap='viridis')
# plt.suptitle("2D Histogram (jointplot kind='hist')", y=1.02)
# plt.show()
```
`jointplot`의 `kind='hex'`는 중앙에 2차원 헥스 빈 플롯을, 주변에는 각 변수의 히스토그램을 표시하여 두 변수 간의 관계와 각 변수의 분포를 동시에 볼 수 있게 합니다.

**구체적 예시**:
*   **바이올린 플롯**: 특정 약물 투여 전후 환자들의 혈압 변화 분포를 비교할 때 사용할 수 있습니다. 단순히 평균 혈압이 얼마나 변했는지뿐만 아니라, 약물 투여 후 혈압 분포가 한 방향으로 치우치는지(skewed), 여러 개의 정점(multimodal)을 가지는지 등 분포의 미묘한 변화를 시각적으로 파악하는 데 매우 효과적입니다. 예를 들어, 어떤 약물은 혈압을 전반적으로 낮추지만, 특정 소그룹에서는 효과가 없거나 오히려 높아지는 양봉 분포를 보일 수도 있습니다.
*   **헥스 빈 플롯**: 인구 밀집도가 높은 도시 지역에서 상점들의 위치와 매출액 데이터를 시각화할 때 활용할 수 있습니다. 상점들의 $x, y$ 좌표를 매출액과 함께 헥스 빈 플롯으로 표현하면, 특정 지역의 상점 밀도와 해당 지역의 평균 매출액 추세를 동시에 파악하여 잠재적 상권 분석에 활용할 수 있습니다. 산점도에서 점들이 너무 많아 겹쳐 보일 때 밀집도를 파악하는 데 특히 유용합니다.

**시험 포인트**:
*   ⭐ **바이올린 플롯의 정의**: KDE 엔벨로프와 내부 사분위수/중앙값 표시를 포함하여 정확하게 설명할 수 있어야 합니다.
*   ⭐ **바이올린 플롯의 활용 목적**: 그룹 간 분포의 **형태(shape, 왜도, 꼬리, 다봉성)** 비교에 적합함을 이해해야 합니다.
*   ⭐ **바이올린 플롯 해석 방법**: 너비가 **밀도에 비례($\text{Width} \propto \text{density}$)**한다는 원리를 숙지하고, 이를 통해 분포를 해석할 수 있어야 합니다.
*   ⭐ **대역폭(bandwidth) 선택의 중요성** 및 작은 $n$에서 봉우리를 과해석하지 않아야 하는 **주의사항**을 기억해야 합니다.
*   ⭐ 강의에서 강조된 **빈(bin) 크기 조절의 중요성**과 그 이유를 설명할 수 있어야 합니다. (너무 크거나 작을 때의 문제점)
*   ⭐ `seaborn.jointplot`을 이용한 2차원 데이터 시각화에서 `kind='hex'` 또는 `kind='hist'` 파라미터의 기능과 차이점을 이해해야 합니다.

---
## Slide 28

---
### **핵심 개념**

*   **Violin Plot (바이올린 플롯)**: 데이터의 분포를 시각화하는 강력한 도구입니다. 기본적인 박스 플롯에 데이터의 **커널 밀도 추정(Kernel Density Estimation, KDE)** 결과를 더하여, 단순히 사분위수뿐만 아니라 데이터가 특정 값 주변에 얼마나 밀집해 있는지, 여러 개의 봉우리(peaks)를 갖는지 등 상세한 밀도 분포를 함께 보여줍니다. 주로 범주형 변수에 따른 연속형 변수의 분포를 비교할 때 유용하게 사용됩니다.

### **코드/수식 해설**

*   **Violin Plot 코드**:
    ```python
    sns.violinplot(data=wine, x="class", y="flavanoids", inner="quartile", cut=0, bw_adjust=1.0)
    ```
    *   `data=wine`: 시각화에 사용할 데이터프레임입니다. 여기서는 `wine` 데이터셋을 사용합니다.
    *   `x="class"`: x축에 표시할 범주형 변수입니다. `wine` 데이터셋의 `class` 변수(와인 종류)를 기준으로 분포를 나눕니다.
    *   `y="flavanoids"`: y축에 표시할 연속형 변수입니다. `flavanoids` 함량의 분포를 각 `class`별로 시각화합니다.
    *   `inner="quartile"`: 바이올린 플롯 내부에 사분위수(Q1, 중앙값, Q3)를 가로선으로 표시합니다. `inner` 파라미터는 `"box"`, `None` 등의 다른 옵션도 가질 수 있습니다.
    *   `cut=0`: 바이올린 곡선이 데이터의 실제 최소/최대 범위 밖으로 확장되는 것을 제한합니다. `0`으로 설정하면 데이터 범위 내에서만 그려집니다.
    *   `bw_adjust=1.0`: 대역폭(bandwidth)을 조절하는 파라미터입니다. KDE의 평활화 정도를 조절하며, 값이 클수록 곡선이 더 부드러워집니다.

*   **KDE (Kernel Density Estimation) 수식 (1차원)**:
    바이올린 플롯의 형태를 만드는 기본 원리인 1차원 KDE는 다음과 같이 정의됩니다.
    $$ \hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right) $$
    여기서:
    *   $\hat{f}_h(x)$는 지점 $x$에서의 추정된 확률 밀도입니다.
    *   $n$은 데이터 포인트의 총 개수입니다.
    *   $h$는 대역폭(bandwidth)으로, 평활화 정도를 결정합니다.
    *   $K$는 커널 함수(kernel function)로, 일반적으로 가우시안 커널(Gaussian kernel)이 사용됩니다.
    *   $x_i$는 $i$번째 데이터 포인트의 값입니다.

### **구체적 예시**

슬라이드의 예시는 `wine` 데이터셋에서 와인의 `class` (종류)에 따라 `flavanoids` (플라바노이드 함량)의 분포를 바이올린 플롯으로 시각화한 것입니다.

*   `class_0`, `class_1`, `class_2` 세 가지 와인 종류별로 플라바노이드 함량의 밀도 분포를 바이올린 형태로 보여줍니다.
*   `class_0`은 비교적 좁고 중간 정도의 플라바노이드 함량 분포를 가지며, 중앙값은 약 3에 위치합니다.
*   `class_1`은 가장 넓은 범위의 플라바노이드 함량 분포를 보여주며, 낮은 값과 중앙값 부근에 밀도가 집중된 것처럼 보입니다. 중앙값은 약 2에 위치합니다.
*   `class_2`는 가장 낮은 플라바노이드 함량 분포를 가지며, 밀도가 1보다 낮은 값에 집중되어 있습니다.
*   `inner="quartile"` 설정 덕분에 각 바이올린 내부의 가로선을 통해 각 클래스별 플라바노이드 함량의 25th, 50th(중앙값), 75th 백분위수를 명확하게 확인할 수 있습니다.

### **강의 내용**

교수님께서는 이어서 **2D KDE (2차원 커널 밀도 추정)**에 대해 설명하셨습니다.

*   **2D KDE**: 기존 1차원 KDE의 개념을 두 개의 속성(변수)으로 확장한 것입니다. 각 개별 데이터 포인트 위에 작은 2차원 벨 커브(종종 2차원 가우시안 커브)를 배치합니다.
*   **작동 방식**: 이 모든 개별 커브들을 합산하여 데이터의 부드럽고 연속적인 표면을 생성합니다. 이 표면은 두 변수의 결합된 추정 확률 밀도를 나타냅니다.
*   **사용 시점**: 데이터의 부드러운 밀도 구조나 두 변수 간의 관계를 연속적인 관점에서 보고 싶을 때 유용합니다.
*   **연관성**: 이전에 다루었던 `jointplot`과 같이 두 변수의 관계를 시각화하는 플롯에서 2D KDE를 활용하여 데이터가 어디에 밀집해 있는지를 밀도 표면으로 표현할 수 있습니다. 바이올린 플롯이 단일 변수의 조건부 밀도 분포를 보여준다면, 2D KDE는 두 변수의 결합 밀도 분포를 보여주는 데 사용됩니다.

### **시험 포인트**

*   ⭐ **Violin Plot의 해석**: 바이올린 플롯이 데이터의 밀도 분포(shape), 중앙값, 사분위수 등의 정보를 어떻게 보여주는지 정확히 이해하고 해석할 수 있어야 합니다. 특히 박스 플롯과의 시각적 차이점과 추가 정보를 파악하는 능력이 중요합니다.
*   ⭐ **KDE (Kernel Density Estimation)**: 바이올린 플롯의 기본 원리이자 2D KDE의 핵심 개념입니다. KDE가 데이터 포인트로부터 밀도 분포를 추정하는 방법임을 숙지해야 합니다.
*   ⭐ **1D KDE와 2D KDE의 차이**: 바이올린 플롯에서 사용되는 1차원 KDE(단일 변수의 분포 추정)와 교수님께서 강조하신 2차원 KDE(두 변수의 결합 분포 추정)의 개념적 차이점을 명확히 구분할 수 있어야 합니다.
*   `bw_adjust`와 같은 파라미터가 플롯의 부드러움에 어떤 영향을 미치는지 이해하는 것이 좋습니다.

---
## Slide 29

**핵심 개념**:
이 슬라이드 구간에서는 커널 밀도 추정(KDE)을 활용하여 데이터의 밀도 분포를 시각화하고, 특히 두 변수 간의 결합 밀도 분포에서 주요 모드(peaks)나 윤곽선(contours)을 식별하는 방법에 대해 다룹니다. `seaborn` 라이브러리의 `jointplot`을 사용하여 2차원 밀도 등고선을 그리고, 대역폭(bandwidth) 조절의 중요성을 강조합니다.

**코드/수식 해설**:
두 변수의 결합 분포를 KDE로 시각화하기 위해 `seaborn.jointplot` 함수를 사용합니다. `kind` 인자를 `'kde'`로 설정하여 중앙 플롯에 2D 밀도 등고선을 표시합니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 예시 데이터 로드 (seaborn 내장 iris 데이터셋)
iris = sns.load_dataset("iris")

# 'sepal_length'와 'sepal_width' 두 변수의 2D KDE 플롯 생성
# kind='kde'로 설정하여 중앙에 밀도 등고선 표시
# bw_adjust를 사용하여 대역폭 조절 (기본값의 0.5배)
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="kde", bw_adjust=0.5)
plt.suptitle("2D KDE Plot of Sepal Length vs. Sepal Width", y=1.02) # 전체 플롯 제목
plt.show()
```
`bw_adjust` 속성은 커널 밀도 추정에서 대역폭(bandwidth)을 조절하는 데 사용됩니다. 대역폭은 각 데이터 포인트 주변에 사용되는 커널(kernel)의 너비나 부드러움 정도를 결정합니다.
*   `bw_adjust` 값이 작을수록 커널이 좁아져 추정된 밀도 곡선이 데이터 포인트에 더 민감하게 반응하여 뾰족하거나 세밀한 형태를 띠게 됩니다. 이는 데이터의 미세한 구조나 여러 개의 작은 모드를 강조할 때 유용할 수 있습니다.
*   `bw_adjust` 값이 클수록 커널이 넓어져 추정된 밀도 곡선이 더 부드러워지고 일반화됩니다. 이는 데이터의 전반적인 추세나 큰 모드를 식별할 때 적합합니다.

수학적으로, KDE는 각 데이터 포인트 $x_i$에 커널 함수 $K$를 적용하여 밀도를 추정합니다. 2차원 KDE의 경우, 밀도 함수 $f(x, y)$는 대략 다음과 같이 표현될 수 있습니다:
$$ \hat{f}(x, y) = \frac{1}{n h_x h_y} \sum_{i=1}^n K\left(\frac{x - x_i}{h_x}, \frac{y - y_i}{h_y}\right) $$
여기서 $n$은 데이터 포인트의 개수, $h_x$와 $h_y$는 각 차원($x, y$)의 대역폭입니다. `bw_adjust`는 이 대역폭 $h$를 조절하는 역할을 합니다.

**구체적 예시**:
아이리스(Iris) 데이터셋을 예로 들어보면, `sepal_length`와 `sepal_width` 두 변수 간의 결합 분포를 시각화할 수 있습니다. `jointplot(..., kind="kde")`를 사용하면 중앙에 이 두 변수의 2차원 밀도 등고선이 그려지고, 각 축에는 해당 변수의 단변량 KDE 플롯이 함께 나타납니다.

만약 `jointplot`을 통해 `sepal_length`와 `sepal_width`의 2D KDE 플롯을 그렸을 때, 특정 `sepal_length`와 `sepal_width` 값 주변에서 등고선이 가장 밀집되어 있다면, 그 지점이 데이터 밀도가 가장 높은 '피크 모드'가 됩니다. 예를 들어, `sepal_length`가 약 5.0cm이고 `sepal_width`가 약 3.4cm인 지점에서 등고선이 가장 조밀하게 나타난다면, 해당 특성을 가진 붓꽃의 개체가 가장 많다는 것을 의미합니다. `bw_adjust` 값을 변경하며 여러 플롯을 그려보면, 밀도 등고선의 세부적인 모양이 어떻게 달라지는지 확인하여 데이터의 숨겨진 구조를 탐색할 수 있습니다.

**강의 내용**:
교수님께서는 특히 데이터 밀도의 '모드(modes)', 즉 '피크(peaks)' 또는 '윤곽선(contours)'을 식별하는 것에 특별히 관심을 두라고 강조하셨습니다.
*   단변량(univariate) KDE와 마찬가지로 2차원 KDE에서도 **대역폭(bandwidth)이 매우 중요**하다고 언급하셨습니다. 이는 커널의 '크기'를 결정하며, `bw_adjust` 속성을 통해 조절할 수 있습니다.
*   `jointplot` 함수를 사용하고 `kind` 인자를 `KDE`로 설정해야 2차원 밀도 등고선을 시각화할 수 있음을 명확히 하셨습니다.
*   중앙의 플롯이 2차원 밀도 등고선을 보여주며, 이를 통해 데이터의 **하나 이상의 주요 피크 모드**를 식별할 수 있다고 설명했습니다.
*   "centered around the separate length of"라는 언급은 특정 변수(예: `sepal_length`)의 특정 값 주변에 주요 피크 모드가 형성되어 있음을 시사하며, 이는 해당 변수가 데이터 분포에서 중요한 군집을 형성하는 데 기여함을 나타낼 수 있습니다.

**시험 포인트**:
*   ⭐ **KDE (Kernel Density Estimation)의 개념**: 데이터 밀도 분포를 추정하는 비모수적 방법이며, 주로 데이터의 분포 형태와 모드를 파악하는 데 사용됨을 이해해야 합니다. 특히 2D KDE는 두 변수 간의 결합 분포를 시각화하는 데 유용합니다.
*   ⭐ **`seaborn.jointplot`과 `kind='kde'`**: `jointplot`을 사용하여 두 변수의 결합 밀도 분포를 2D 등고선 형태로 시각화하는 방법을 알아야 합니다. 이 플롯의 각 부분(중앙의 2D KDE, 주변의 단변량 KDE)을 설명할 수 있어야 합니다.
*   ⭐ **`bw_adjust` 속성의 역할 및 중요성**: KDE에서 대역폭(bandwidth)이 무엇을 의미하며, `bw_adjust` 파라미터를 통해 밀도 추정의 부드러움(smoothing)이나 세밀함(detail)을 어떻게 조절할 수 있는지 설명할 수 있어야 합니다. 작은 값과 큰 값이 시각화에 미치는 영향(예: 과도한 평활화 또는 노이즈 강조)을 비교하여 설명할 수 있어야 합니다.
*   ⭐ **2D 밀도 등고선 해석**: 플롯에서 밀도가 높은 영역(모드/피크)을 식별하고, 이것이 데이터셋에서 무엇을 의미하는지 해석하는 능력. 여러 모드가 나타날 경우, 각 모드가 서로 다른 데이터 군집을 나타낼 수 있음을 이해해야 합니다.

---
## Slide 30

### **핵심 개념**
이 슬라이드는 `seaborn` 라이브러리의 `boxenplot` (또는 `letter-value plot`) 함수를 사용하여 데이터의 분포를 시각화하는 코드 예시를 보여줍니다. `boxenplot`은 기존 `boxplot`의 확장된 형태로, 특히 데이터의 꼬리 부분(tail of the distribution)과 아웃라이어를 더 세밀하게 보여주는 데 강점이 있습니다. 이는 데이터의 중앙 집중 경향뿐만 아니라 분포의 밀도 변화까지 시각적으로 파악할 수 있게 돕습니다.

### **코드/수식 해설**
주어진 코드는 `wine` 데이터셋을 활용하여 `class`별 `flavanoids`의 분포를 `boxenplot`으로 그리는 예시입니다.

```python
sns.boxenplot(data=wine, x="class", y="flavanoids",
              k_depth="trustworthy", width_method="linear",
              showfliers=True, outlier_prop=0.01)
```
*   `sns.boxenplot()`: `seaborn` 라이브러리에서 `boxenplot`을 생성하는 함수입니다.
*   `data=wine`: 시각화에 사용할 데이터프레임입니다. 여기서는 `wine` 데이터셋을 사용합니다.
*   `x="class"`: x축에 매핑될 변수입니다. `class` 변수는 보통 범주형으로, 와인의 종류나 등급을 나타냅니다.
*   `y="flavanoids"`: y축에 매핑될 수치형 변수입니다. 여기서는 와인의 `flavanoids` 함량을 나타냅니다.
*   `k_depth="trustworthy"`: `boxenplot`의 각 박스 깊이를 결정하는 방법입니다. `"trustworthy"`는 각 깊이에서 가장 신뢰할 수 있는 통계량(예: 중앙값)을 사용하여 박스 경계를 계산합니다. 이는 특히 데이터의 꼬리 부분을 더 견고하게 표현하는 데 도움을 줍니다.
*   `width_method="linear"`: 각 박스의 너비를 결정하는 방법입니다. `"linear"`는 박스의 너비를 선형적으로 조절하여 분포의 밀도를 시각적으로 나타낼 수 있습니다.
*   `showfliers=True`: 아웃라이어(이상치)를 플롯에 표시할지 여부를 결정합니다. `True`로 설정하면 아웃라이어가 점으로 표시됩니다.
*   `outlier_prop=0.01`: `showfliers=True`일 때, 데이터의 상위 $1\%$와 하위 $1\%$에 해당하는 값을 아웃라이어로 간주하여 표시합니다. 즉, 전체 데이터의 $2\%$를 아웃라이어로 간주할 수 있습니다.

### **구체적 예시**
이 코드를 실행하면, `wine` 데이터셋의 각 `class` (예: 와인 등급 1, 2, 3)별 `flavanoids` 함량 분포를 여러 겹의 박스로 시각화한 그래프가 생성됩니다. 각 박스의 계층은 데이터 분포의 특정 사분위수(quartile) 또는 다른 퀀타일(quantile)을 나타내어, 데이터의 중앙값, 사분위수 범위뿐만 아니라 분포의 꼬리 부분에 있는 값들의 밀도까지 상세하게 보여줍니다. 예를 들어, 특정 `class`의 `flavanoids` 분포가 다른 `class`에 비해 훨씬 넓거나 좁은지, 혹은 아웃라이어가 많은지를 한눈에 파악할 수 있습니다.

### **강의 내용**
교수님은 해당 슬라이드 구간에서 `boxenplot` 코드와는 별개로 "버블 차트(bubble chart)"에 대해 설명하셨습니다.
*   **버블 차트의 정의**: 버블 차트는 기본적으로 특별한 형태의 스캐터플롯(scatter plot)입니다.
*   **3차원 변수 매핑**: 일반적인 스캐터플롯이 두 개의 수치형 변수를 x, y 축에 매핑하는 반면, 버블 차트는 "마커의 크기(size of markers)가 세 번째 수치형 변수(third numerical variable)에 매핑"되는 특징을 가집니다.
*   **`hue` 대신 `size` 사용**: 색상(`hue`)으로 범주형 변수를 표현하는 대신, 마커의 크기(`size`)를 사용하여 수치형 변수의 값을 시각적으로 나타냅니다.
*   **예시**: "pruroline" (아마도 `proline` 변수의 오타)과 같은 수치형 변수의 값이 클수록 마커의 크기가 커지도록 시각화하여, 세 변수 간의 관계를 동시에 파악할 수 있습니다.

### **시험 포인트**
*   ⭐ `boxenplot`의 개념과 `boxplot`과의 차이점 (특히 데이터 분포의 꼬리 부분을 더 상세하게 보여준다는 점).
*   ⭐ `sns.boxenplot` 함수 사용 시 `x`, `y` 매개변수가 각각 어떤 변수를 나타내는지, 그리고 `k_depth`, `showfliers`, `outlier_prop`과 같은 주요 파라미터의 역할을 설명할 수 있어야 합니다.
*   ⭐ 버블 차트가 무엇이며, 일반적인 스캐터플롯과 어떤 차이가 있는지, 즉 **마커의 크기를 사용하여 세 번째 수치형 변수를 시각화하는 방법**을 설명할 수 있어야 합니다.

---
## Slide 31

---

### 핵심 개념

이 슬라이드는 **Strip Plot**과 **Swarm Plot**의 정의와 사용 목적을 설명합니다. 두 플롯 모두 범주형 변수별로 1차원 산점도를 보여주는 방식입니다.

*   **Strip Plot**: 각 데이터 포인트를 1차원 공간에 점으로 표시합니다. 점들이 겹쳐 보일 수 있으므로, 보통 `jitter` 기능을 사용하여 점들의 위치를 약간 무작위로 분산시켜 겹침을 줄이고 모든 개별 관측치를 볼 수 있도록 합니다.
*   **Swarm Plot**: Strip Plot과 유사하게 개별 관측치를 보여주지만, 점들이 서로 겹치지 않도록 자동으로 위치를 조정하여 분포의 밀도를 시각적으로 더 명확하게 보여줍니다. 'non-overlapping packing' 방식으로 점들을 배열합니다.
*   **사용 시점**: 요약 통계량(예: 평균, 중앙값)과 함께 원본 데이터의 개별 관측치를 보고자 할 때 유용합니다. 특히 Box Plot이나 Violin Plot과 함께 사용하여 요약된 분포 정보와 개별 데이터 포인트의 실제 위치를 동시에 파악할 수 있습니다.
*   **해석 방법**: 데이터의 '뭉침(clumps)'이나 '틈새(gaps)'를 통해 집계된 통계량으로는 알 수 없었던 미세 구조(microstructure)를 파악할 수 있습니다.
*   **주의 사항 (Pitfalls)**: 데이터의 수가 $n$이 너무 클 경우, Overplotting 문제가 발생하여 점들이 너무 많아져 패턴을 알아보기 어려울 수 있습니다. 이 경우 다운샘플링(downsample)을 하거나 요약 통계량 플롯과 결합하는 것을 고려해야 합니다.

강의 음성에서는 주로 **Box Plot**과 **Violin Plot**에 대한 내용이 강조되었습니다. 이들은 데이터 분포의 요약 정보를 제공하는 데 중점을 둡니다.

*   **Box Plot (Box Chart)**: 데이터의 5가지 요약 통계량(최소값, 1사분위수($Q_1$), 중앙값($Q_2$), 3사분위수($Q_3$), 최대값)을 시각화하여 분포의 중심, 분산, 비대칭성 및 이상치를 파악하는 데 용이합니다.
*   **Violin Plot**: Box Plot의 기능에 더해, 각 데이터 포인트의 밀도 추정치를 스무딩된 커널 밀도 추정(KDE)으로 보여주어 분포의 형태를 더 자세히 파악할 수 있습니다.

### 코드/수식 해설

슬라이드에는 코드나 수식이 직접 포함되어 있지 않지만, `seaborn` 라이브러리를 사용하면 Strip Plot, Swarm Plot, Box Plot, Violin Plot을 쉽게 그릴 수 있습니다. 교수님이 언급하신 `class` (범주형)와 `alcohol` (수치형) 데이터를 예시로 들어보겠습니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 예시 데이터 생성 (교수님 언급과 유사하게 3개의 클래스를 가정)
data = {
    'class': ['Class A'] * 30 + ['Class B'] * 40 + ['Class C'] * 35,
    'alcohol': np.concatenate([
        np.random.normal(loc=12.0, scale=0.5, size=30),  # Class A
        np.random.normal(loc=13.0, scale=0.7, size=40),  # Class B
        np.random.normal(loc=11.5, scale=0.6, size=35)   # Class C
    ])
}
df = pd.DataFrame(data)

plt.figure(figsize=(15, 5))

# 1. Box Plot 예시
plt.subplot(1, 3, 1)
sns.boxplot(x='class', y='alcohol', data=df)
plt.title('Box Plot of Alcohol by Class')

# 2. Strip Plot 예시 (jitter 적용)
plt.subplot(1, 3, 2)
sns.stripplot(x='class', y='alcohol', data=df, jitter=True, color='purple', alpha=0.7)
sns.boxplot(x='class', y='alcohol', data=df, boxprops={'facecolor':'None', 'edgecolor':'black'}, width=0.3) # 박스플롯 위에 스트립플롯을 겹쳐 그릴 수 있습니다.
plt.title('Strip Plot (jittered) of Alcohol by Class')

# 3. Swarm Plot 예시
plt.subplot(1, 3, 3)
sns.swarmplot(x='class', y='alcohol', data=df, color='green')
plt.title('Swarm Plot of Alcohol by Class')

plt.tight_layout()
plt.show()
```

위 코드는 교수님이 언급하신 "X축은 class, Y축은 alcohol"의 형태를 시각화하는 방법을 보여줍니다. `sns.stripplot`은 개별 점을 표시하고 `jitter=True`로 겹침을 방지하며, `sns.swarmplot`은 점들이 겹치지 않게 밀도를 유지하며 표시합니다. 이들은 종종 `sns.boxplot`이나 `sns.violinplot` 위에 겹쳐서 그려져 요약 통계와 원본 데이터를 동시에 보여주는 데 사용됩니다.

### 구체적 예시

교수님이 언급하신 예시를 그대로 사용하면 됩니다.

*   **데이터**: 와인 데이터셋에서 **클래스 (Class)** (예: 와인의 종류 1, 2, 3)는 범주형 변수이고, **알코올 함량 (Alcohol)**은 수치형 변수입니다.
*   **Box Plot/Violin Plot 예시**:
    *   X축에 'Class 1', 'Class 2', 'Class 3'을 놓고, Y축에 각 클래스별 'Alcohol' 함량의 Box Plot이나 Violin Plot을 그립니다.
    *   'Class 1'의 와인들이 'Class 2'의 와인들보다 평균적으로 알코올 함량이 낮고 분포가 더 좁다는 것을 한눈에 파악할 수 있습니다. Violin Plot은 각 클래스 내 알코올 함량의 분포가 단봉형인지 다봉형인지 등 더 세부적인 형태까지 보여줍니다.
*   **Strip Plot/Swarm Plot 예시**:
    *   동일한 X축과 Y축에 Strip Plot 또는 Swarm Plot을 그려 각 클래스에 속하는 개별 와인들의 알코올 함량 데이터 포인트 하나하나를 시각화합니다.
    *   만약 'Class 1'의 알코올 함량 데이터 포인트들이 특정 구간에 집중되어 있고, 그 외 구간에는 듬성듬성 퍼져 있다면, Box Plot만으로는 알기 어려웠던 '알코올 함량 분포 내의 미세한 틈새나 뭉침'을 Strip/Swarm Plot으로 확인할 수 있습니다.
    *   예를 들어, 'Class A'의 알코올 함량이 11.5와 12.5 주변에 두 개의 뚜렷한 그룹으로 나뉘어 분포하는 경우, Swarm Plot은 이를 명확하게 보여줄 수 있습니다.

### 강의 내용

교수님은 주로 **Box Plot**과 **Violin Plot**에 대해 설명하셨습니다.
*   이러한 플롯들이 "univariate data" (단일 변수)와 "bivariate data" (두 변수) 모두에 사용될 수 있음을 강조하셨습니다.
*   특히, "bivariate data"의 경우, "first axis, I mean the attribute is a class, and the second attribute is a numeric attribute"라고 설명하며 **범주형 변수와 수치형 변수의 관계를 시각화하는 데 Box Plot이 유용**함을 말씀하셨습니다.
*   구체적인 예시로 "X attribute shows class" (3개의 클래스)와 "Y is set to alcohol"을 들어, 각 클래스별 알코올 함량 분포를 Box Plot으로 시각화하는 상황을 설명하셨습니다.
*   슬라이드는 Strip/Swarm Plot을 다루고 있으나, 음성 전사에서는 Box Plot과 Violin Plot을 언급하며 이들 시각화 방법이 데이터 분포를 이해하는 데 핵심적인 도구임을 강조한 것으로 보아, 분포 시각화 전반에 대한 맥락을 제공하거나 다음 슬라이드 내용과 연결되는 부분이 있었을 것으로 추정됩니다. Strip/Swarm Plot은 Box/Violin Plot과 함께 개별 데이터 포인트를 보여주어 전체적인 분포와 개별 관측치를 동시에 파악하는 데 시너지를 낼 수 있습니다.

### 시험 포인트

*   ⭐ **Strip Plot과 Swarm Plot의 정의 및 차이점**:
    *   두 플롯 모두 범주형 변수별 개별 관측치(1D scatter)를 시각화하지만, Strip Plot은 `jitter`로 겹침을 해결하고 Swarm Plot은 `non-overlapping packing` 방식으로 겹침 없이 밀도를 반영하여 시각화합니다.
*   ⭐ **Strip/Swarm Plot의 활용 목적**:
    *   집계된 통계량(예: Box Plot의 사분위수)으로 가려질 수 있는 데이터의 **원시 관측치(raw observations) 및 미세 구조(microstructure)**를 파악할 때 사용합니다. 특히 분포 내의 뭉침(clumps)이나 틈새(gaps)를 발견하는 데 유용합니다.
*   ⭐ **Box Plot, Violin Plot과의 관계 및 결합 사용**:
    *   Box Plot과 Violin Plot은 분포의 요약 통계(중앙값, 사분위수 등)나 밀도(KDE)를 보여주는 반면, Strip/Swarm Plot은 개별 데이터 포인트를 보여줍니다.
    *   이 세 가지 플롯은 서로 보완적이며, 종종 함께 그려져 요약 정보와 개별 관측치를 동시에 파악하는 데 사용됩니다. (예: `seaborn`에서 `boxplot` 위에 `stripplot`을 겹쳐 그리기)
*   ⭐ **범주형-수치형 변수 시각화**:
    *   X축에 범주형 변수 (예: `class`), Y축에 수치형 변수 (예: `alcohol`)를 놓고 각 범주별 수치형 변수의 분포를 비교하는 시각화는 데이터 분석에서 매우 흔하게 사용되며, Box Plot, Violin Plot, Strip Plot, Swarm Plot이 주요 도구로 활용됩니다.
    *   데이터의 규모 $n$이 클 때 `Overplotting` 문제를 인식하고 `downsample`이나 `summary`와 결합하는 등의 해결책을 고려해야 합니다.

---
## Slide 32

**핵심 개념**:
`stripplot`은 `seaborn` 라이브러리에서 제공하는 시각화 도구로, 범주형 변수에 따른 수치형 변수의 분포를 개별 데이터 포인트로 표현하는 데 사용됩니다. 각 범주에 해당하는 모든 데이터 포인트를 1차원 선 위에 점으로 표시하여 데이터의 밀도와 각 개별 관측치의 위치를 직관적으로 파악할 수 있게 합니다. 특히 데이터의 개별성을 강조할 때 유용합니다.

**코드 해설**:

```python
sns.stripplot(data=wine, x="class", y="flavanoids", jitter=0.25, alpha=0.6, size=3)
```

- `sns.stripplot()`: `seaborn` 라이브러리의 `stripplot` 함수를 호출합니다.
- `data=wine`: 시각화에 사용할 데이터셋으로 `wine` DataFrame을 지정합니다.
- `x="class"`: X축에 나타낼 변수로 `class` 컬럼을 지정합니다. 이는 범주형 변수로, 슬라이드에서는 `class_0`, `class_1`, `class_2`로 구분된 와인 클래스를 의미합니다.
- `y="flavanoids"`: Y축에 나타낼 변수로 `flavanoids` 컬럼을 지정합니다. 이는 수치형 변수로, 각 와인 클래스별 플라보노이드 함량 분포를 보여줍니다.
- `jitter=0.25`: ⭐**`jitter` 매개변수는 매우 중요합니다.** 동일한 `y` 값을 가지는 점들이 겹쳐서 보이지 않게 하기 위해 X축 방향으로 약간의 무작위 노이즈를 추가하는 정도를 설정합니다. 여기서는 `0.25`만큼의 지터링을 적용하여 점들이 옆으로 퍼져 보이게 만듭니다.
- `alpha=0.6`: 각 점의 투명도를 설정합니다. `0.6`은 반투명하게 만듭니다.
- `size=3`: 각 점의 크기를 설정합니다.

**구체적 예시**:
슬라이드에 첨부된 "Wine — Strip plot (jittered)" 차트는 `wine` 데이터셋의 `class`별 `flavanoids` 함량 분포를 `stripplot`으로 시각화한 예시입니다. `class_0`은 높은 `flavanoids` 값을, `class_2`는 낮은 `flavanoids` 값을 가지며, `class_1`은 중간 정도의 넓은 분포를 보이는 것을 한눈에 확인할 수 있습니다. 각 클래스 내에서도 개별 와인 샘플의 `flavanoids` 함량이 어디에 위치하는지 점으로 명확하게 볼 수 있습니다. `jitter` 덕분에 점들이 겹치지 않아 각 데이터 포인트의 존재를 확인할 수 있습니다.

**강의 내용**:
교수님께서는 이 슬라이드 구간에서 `stripplot`이 `boxplot`, `violinplot`, `swarmplot`과 같이 범주형 변수에 대한 수치형 변수의 분포를 시각화하는 데 사용되는 플롯 중 하나임을 강조하셨습니다. 특히 `stripplot`의 핵심 기능으로 "plotting point for each category(각 범주에 대한 점을 그리는 것)"을 언급하며, 많은 점을 그릴 때 발생하는 겹침(overlap) 문제를 해결하기 위해 ⭐**`jitter` 옵션을 사용해 점들을 퍼뜨려야(avoid some overlap) 한다고 강조**하셨습니다. `jitter` 값을 적절히 설정함으로써 각 데이터 포인트를 명확하게 볼 수 있게 됩니다.

**시험 포인트**:
- ⭐`stripplot`의 주된 용도: 범주형 변수에 따른 수치형 변수의 개별 데이터 포인트 분포를 시각화하는 경우.
- ⭐`stripplot`에서 `jitter` 매개변수의 역할과 중요성: 데이터 포인트 겹침을 방지하여 분포를 더 명확하게 보여주는 기능. `jitter` 없이 많은 데이터 포인트를 그릴 경우 정보 손실이 발생할 수 있습니다.
- `stripplot`과 `boxplot` 또는 `violinplot`의 차이점: `stripplot`은 개별 데이터 포인트를 모두 보여주는 반면, `boxplot`이나 `violinplot`은 분포의 통계적 요약(중앙값, 사분위수, 밀도 등)에 중점을 둡니다. 상황에 따라 적절한 시각화 방법을 선택하는 것이 중요합니다.

---
## Slide 33

**핵심 개념**
*   **Contingency Heatmap (교차표 히트맵)**: 두 범주형 변수 간의 관계를 시각화하는 방법입니다. 교차표(Cross-tabulation 또는 Contingency Table)의 각 셀에 해당하는 빈도나 비율을 색상으로 인코딩하여 보여줍니다.
*   **Cross-tabulation (교차표 / Contingency Table)**: 두 범주형 변수의 각 카테고리 쌍이 동시에 발생하는 빈도를 집계하는 격자 형태의 테이블입니다. 예를 들어, 성별과 선호하는 운영체제 간의 교차표는 '남성'이 'Windows'를 선호하는 수, '여성'이 'macOS'를 선호하는 수 등을 포함합니다.

**코드/수식 해설**
별도의 복잡한 수식이나 코드 블록은 없지만, 개념을 이해하는 데 도움이 되는 파이썬 라이브러리 사용 예시를 설명합니다.

*   **교차표 생성**: `pandas` 라이브러리의 `crosstab` 함수를 사용하여 두 범주형 변수 간의 교차표를 쉽게 생성할 수 있습니다.
    ```python
    import pandas as pd
    
    # 예시 데이터프레임
    data = {'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
            'OS': ['Windows', 'macOS', 'Windows', 'Linux', 'macOS']}
    df = pd.DataFrame(data)
    
    # 교차표 생성
    contingency_table = pd.crosstab(df['Gender'], df['OS'])
    print(contingency_table)
    ```
    출력 예시:
    ```
    OS      Linux  Windows  macOS
    Gender                     
    Female      1        0      1
    Male        0        2      1
    ```
*   **히트맵 시각화**: `seaborn` 라이브러리의 `heatmap` 함수를 사용하여 생성된 교차표를 시각화합니다.
    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # 위에서 생성한 contingency_table 사용
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='Blues')
    plt.title('Contingency Heatmap of Gender vs OS')
    plt.show()
    ```

**구체적 예시**
대학생들을 대상으로 '전공 계열 (인문, 자연, 공학)'과 '졸업 후 희망 진로 (취업, 대학원, 창업)'에 대한 설문조사를 했다고 가정해 봅시다.
*   **데이터**: 각 학생의 전공 계열과 희망 진로 데이터를 수집합니다.
*   **교차표**: 이 두 범주형 변수에 대한 교차표를 만들면 '공학 계열' 학생들이 '취업'을 희망하는 수, '인문 계열' 학생들이 '대학원'을 희망하는 수 등이 각 셀에 집계됩니다.
*   **히트맵**: 이 교차표를 히트맵으로 시각화하면, 특정 전공 계열에서 특정 진로를 희망하는 경향이 있는지 색상의 진하기로 한눈에 파악할 수 있습니다. 예를 들어, 공학 계열과 취업 셀의 색상이 유독 진하다면 해당 관계가 강하다는 것을 시사합니다.

**강의 내용**
교수님께서는 슬라이드의 핵심을 명확히 설명해 주셨습니다.
1.  **교차표 선행**: 히트맵을 만들기 전에 먼저 **교차표(Contingency Table)**를 생성해야 한다고 강조하셨습니다.
2.  **교차표의 역할**: 교차표는 "두 카테고리 쌍의 동시 발생 빈도(co-occurrence)를 세는 격자"라고 설명하며, 이것이 두 범주형 변수 간의 관계를 파악하는 출발점임을 명확히 하셨습니다.
3.  **히트맵의 역할**: 히트맵은 이 교차표를 "색상 척도에 따라 매핑하여 시각화"하는 도구라고 강조하며, 두 "범주형 속성(category attribute) 간의 비교"에 매우 유용하다고 설명하셨습니다. 즉, 숫자 데이터를 색상으로 변환하여 시각적 패턴을 찾기 쉽게 만듭니다.

**시험 포인트**
*   ⭐ **Contingency Heatmap의 정의와 목적**: 두 **범주형 변수** 간의 **연관성(association) 또는 불균형(imbalance)**을 평가하기 위해 교차표를 히트맵으로 시각화하는 것임을 정확히 이해해야 합니다. (강의 내용과 슬라이드 'Use when' 참조)
*   ⭐ **Pitfalls: 불균등한 그룹 크기 처리**: 그룹 크기가 불균등할 경우, **원시 빈도(raw counts) 대신 백분율(percentages)을 사용하여 비교**해야 한다는 점을 반드시 기억해야 합니다. 원시 빈도를 사용하면 단순히 표본 크기가 큰 그룹의 셀이 더 진하게 표시되어 잘못된 결론을 내릴 수 있습니다. 이는 데이터를 올바르게 해석하는 데 매우 중요한 주의사항입니다. (슬라이드 'Pitfalls' 참조)
*   ⭐ **데이터 해석 방법**: 히트맵에서 행/열 패턴을 찾거나 비율을 정규화하여 비교하는 방법을 알아야 합니다. 색상이 빈도 또는 비율을 어떻게 인코딩하는지 이해하는 것이 중요합니다.

---
## Slide 34

## Contingency Heatmap (교차표 히트맵)

### **핵심 개념**
*   **Contingency Heatmap (교차표 히트맵)**: 두 **범주형 변수** 간의 연관성(association) 또는 불균형(imbalance)을 시각적으로 평가하는 표준적인 방법입니다. `pd.crosstab`으로 생성된 교차표를 `sns.heatmap`으로 시각화하여 각 범주 조합의 빈도수를 색상으로 표현합니다.
*   **`pd.cut()`**: 연속형 수치 데이터를 지정된 개수의 구간으로 나누어 **범주형 데이터**로 변환하는 pandas 함수입니다. 데이터 분석 시 연속형 변수를 범주화하여 다른 범주형 변수와 함께 분석할 때 유용합니다.
*   **`pd.crosstab()`**: pandas 라이브러리에서 두 개 이상의 인자(변수)의 교차 빈도(contingency table)를 계산하는 함수입니다. 두 범주형 변수의 각 조합에 해당하는 데이터 포인트의 개수를 표 형태로 보여줍니다.
*   **`sns.heatmap()`**: Seaborn 라이브러리에서 2D 데이터를 색상 맵으로 시각화하는 함수입니다. 교차표와 같은 행렬 데이터를 시각적으로 표현하여 "hot cells" (높은 빈도)과 "cold cells" (낮은 빈도)을 통해 변수 간의 연관성을 직관적으로 파악할 수 있게 합니다.

### **코드/수식 해설**

```python
1 wine["alcohol_bin"] = pd.cut(wine["alcohol"], 3, labels=["low", "mid", "high"])
2 ct = pd.crosstab(wine["class"], wine["alcohol_bin"])
3 sns.heatmap(ct, annot=True, fmt="d")
```

1.  `wine["alcohol_bin"] = pd.cut(wine["alcohol"], 3, labels=["low", "mid", "high"])`
    *   `wine["alcohol"]`: `wine` 데이터프레임의 `alcohol` 컬럼(연속형 수치 데이터)을 입력으로 사용합니다.
    *   `3`: `alcohol` 데이터를 3개의 동일한 너비의 구간(bins)으로 나눕니다.
    *   `labels=["low", "mid", "high"]`: 생성된 3개의 구간에 각각 "low", "mid", "high"라는 범주형 레이블을 부여합니다. 이 결과로 `wine` 데이터프레임에 새로운 범주형 컬럼 `alcohol_bin`이 추가됩니다.
2.  `ct = pd.crosstab(wine["class"], wine["alcohol_bin"])`
    *   `pd.crosstab()`: `wine` 데이터프레임의 `class` 컬럼(와인 종류)과 새로 생성된 `alcohol_bin` 컬럼(알코올 함량 범주)을 사용하여 교차표(contingency table)를 생성합니다.
    *   `ct` 변수에는 `class`와 `alcohol_bin`의 각 조합에 해당하는 데이터 포인트의 개수(빈도수)를 담은 행렬이 저장됩니다.
3.  `sns.heatmap(ct, annot=True, fmt="d")`
    *   `sns.heatmap()`: `ct`에 저장된 교차표 데이터를 히트맵으로 시각화합니다.
    *   `annot=True`: 히트맵의 각 셀 내부에 해당 셀의 숫자 값(빈도수)을 표시합니다.
    *   `fmt="d"`: `annot=True`로 표시될 숫자 값의 형식을 정수형(`d`는 decimal integer)으로 지정합니다.

### **구체적 예시**

슬라이드에 표시된 "Wine — Contingency Heatmap"은 와인 데이터셋에서 `class` (와인 종류)와 `alcohol_bin` (알코올 함량 범주) 간의 관계를 보여줍니다.

*   예를 들어, `class_0`와 "high" 알코올 함량의 교차 셀에는 숫자 `38`이 표시되어 있습니다. 이는 `class_0` 와인 중 알코올 함량이 "high"인 샘플이 38개라는 것을 의미하며, 색상 스케일에서 노란색(높은 빈도)으로 나타납니다.
*   반면, `class_2`와 "high" 알코올 함량의 교차 셀에는 숫자 `11`이 표시되어 있습니다. 이는 `class_2` 와인 중 알코올 함량이 "high"인 샘플이 11개라는 것을 의미하며, 색상 스케일에서 보라색(낮은 빈도)으로 나타납니다.
*   이러한 시각화를 통해 `class_0` 와인은 상대적으로 "high" 알코올 함량을 가진 경우가 많고, `class_2` 와인은 "low" 또는 "mid" 알코올 함량을 가진 경우가 "high"보다 많다는 경향성을 한눈에 파악할 수 있습니다.

### **강의 내용**

*   이 슬라이드의 내용은 두 범주형 변수 간의 **연관성(association)** 또는 **불균형(imbalance)**을 평가하는 표준적인 시각화 방법입니다.
*   히트맵에서 색상이 진한 셀(예: 노란색에 가까운 셀)을 "**hot cells**", 색상이 옅은 셀(예: 보라색에 가까운 셀)을 "**cold cells**"이라고 부르며, 이들은 강한 연관성이나 특정 범주 조합의 높은/낮은 빈도를 나타냅니다.
*   ⭐**매우 중요**: 단순히 각 셀의 **원시 카운트(raw counts)**를 비교하는 것은 그룹 크기(전체 데이터 또는 각 `class`별 샘플 수)가 불균등할 경우 **오해의 소지가 매우 큽니다.**
*   이러한 문제를 해결하기 위해 테이블을 **정규화(normalize)**하여 각 셀의 **백분율(percentage) 또는 비율(ORD rates)**을 보는 것이 훨씬 더 정확하고 바람직합니다. (예: 각 `class` 내에서 `alcohol_bin`의 비율)
*   이러한 히트맵을 만들기 전에, `alcohol`과 같은 **연속형 수치 데이터**를 `pd.cut` 함수를 사용하여 "low", "mid", "high"와 같은 **세 개의 범주**로 나누는 전처리 과정이 필수적으로 선행되어야 합니다.

### **시험 포인트**

*   ⭐**`pd.cut()`의 역할과 사용법**: 연속형 데이터를 범주형 데이터로 효과적으로 변환하는 방법을 이해하고, `labels` 인자의 중요성을 파악해야 합니다.
*   ⭐**`pd.crosstab()`의 역할**: 두 범주형 변수 간의 빈도수를 집계하는 교차표 생성의 기본 원리를 이해해야 합니다.
*   ⭐**Contingency Heatmap의 해석**: "hot cells"과 "cold cells"이 데이터의 어떤 특성(높은/낮은 빈도, 강한/약한 연관성)을 나타내는지 설명할 수 있어야 합니다.
*   ⭐**원시 카운트(raw counts)의 한계점**: 그룹 크기 불균형 시 원시 카운트 해석의 문제점과 이를 보완하기 위한 **정규화(normalization)**의 필요성을 명확히 이해해야 합니다. 이는 데이터 분석에서 흔히 범하는 오류를 피하는 중요한 개념입니다.

---
## Slide 35

## 데이터분석 입문 (CSED226) — Correlation Heatmap

### 핵심 개념
**상관관계 히트맵 (Correlation Heatmap)**은 여러 수치형(numeric) 특징(features)들 간의 선형 상관관계(linear association)를 시각적으로 표현하는 도구입니다. 각 셀의 색상은 두 특징 간의 Pearson $r$ 상관계수 값을 나타내며, 색상의 강도(strength)는 상관관계의 크기를, 색상의 종류(sign)는 양(+) 또는 음(-)의 방향을 나타냅니다.

강의 음성에서는 *범주형(categorical) 속성* 간의 관계를 시각화하는 **분할표(Contingency Table) 히트맵**에 대해 설명하고 있습니다. 이는 상관관계 히트맵과는 목적하는 바가 다르지만, `seaborn.heatmap`과 같은 동일한 시각화 도구를 사용하여 행렬 형태의 데이터를 색상으로 표현한다는 공통점이 있습니다.

### 코드/수식 해설

**1. Pearson 상관계수 ($r$)**
상관관계 히트맵의 각 셀은 두 수치형 변수 $X$와 $Y$ 사이의 Pearson 상관계수 $r$을 나타냅니다. 그 수식은 다음과 같습니다:

$$r_{XY} = \frac{\sum_{i=1}^{n}(X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n}(X_i - \bar{X})^2}\sqrt{\sum_{i=1}^{n}(Y_i - \bar{Y})^2}}$$

여기서 $X_i, Y_i$는 $i$번째 데이터 포인트, $\bar{X}, \bar{Y}$는 각 변수의 평균, $n$은 데이터 포인트의 개수입니다. $r$ 값은 항상 $-1$과 $1$ 사이에 있습니다 (즉, $-1 \le r \le 1$).

**2. 히트맵 시각화 파라미터 (`annot=True`)**
강의 음성에서 언급된 `annot=True`는 `seaborn.heatmap` 함수에서 각 셀 안에 실제 값을 숫자로 표시할지 여부를 결정하는 파라미터입니다.
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 예시: 와인 데이터의 범주형 속성 'glasses'와 'alcohol_bins' 간의 분할표
# (강의 음성에 기반한 가상의 코드)
# wine_df = pd.read_csv('wine_data.csv')
# CT = pd.crosstab(wine_df['glasses'], wine_df['alcohol_bins'])

# 강의 음성의 맥락을 반영한 분할표 (Contingency Table) 예시
data = {
    'low': [10, 5, 2],
    'mid': [3, 15, 7],
    'high': [1, 2, 18]
}
CT = pd.DataFrame(data, index=['glass_A', 'glass_B', 'glass_C'])

plt.figure(figsize=(6, 5))
sns.heatmap(CT, annot=True, fmt='d', cmap='YlGnBu') # annot=True로 실제 count 표시
plt.title('Contingency Heatmap: Glasses vs Alcohol Bins')
plt.xlabel('Alcohol Bins')
plt.ylabel('Glasses')
plt.show()
```
*   `annot=True`: 각 셀에 해당 데이터 값(예: 빈도수)을 숫자로 표시합니다.
*   `fmt='d'`: 어노테이션 숫자의 형식을 정수로 지정합니다. (분할표의 경우)

### 구체적 예시

**1. 상관관계 히트맵 해석 예시 (슬라이드 내용)**
만약 어떤 데이터셋의 특징 A, B, C에 대한 상관관계 히트맵이 다음과 같다고 가정해 봅시다:
*   A와 B의 셀이 진한 파란색이면, 두 특징이 강한 양의 상관관계($r \approx 1$)를 가집니다. (예: 주택 면적이 클수록 가격이 비싸다)
*   A와 C의 셀이 진한 빨간색이면, 두 특징이 강한 음의 상관관계($r \approx -1$)를 가집니다. (예: 운동량이 많을수록 체지방률이 낮다)
*   B와 C의 셀이 거의 흰색에 가까우면, 두 특징은 약하거나 선형 상관관계가 거의 없습니다 ($r \approx 0$).

히트맵에서 특정 특징들이 묶여서 밝거나 어두운 `Blocks/stripes`를 형성한다면, 이는 해당 특징들이 서로 유사한 경향을 보이거나 특정 그룹을 이룬다는 것을 시사합니다. 예를 들어, 금융 데이터에서 특정 주식 그룹이 항상 함께 오르거나 내리는 패턴을 보이는 경우를 들 수 있습니다.

**2. 분할표 히트맵 예시 (강의 음성 내용)**
강의 음성에서 `wine data frame`의 `glasses`와 `alcohol bean categorical attribute`를 예로 들었습니다. `low`, `mid`, `high` 세 가지 알코올 빈(alcohol bin)과 세 가지 잔(glasses) 종류가 있다고 가정할 때, 이 두 범주형 변수 간의 **분할표(Contingency Table)**를 계산합니다. 이 분할표는 특정 잔 종류에 속하면서 특정 알코올 빈에 속하는 와인의 개수를 보여줍니다. `annot=True`를 사용하면 각 셀에 해당 개수(count)가 직접 표시되어 시각적으로 이해하기 쉬운 `contingency heat map`이 됩니다. 예를 들어, 'glass_A'와 'low' 알코올 빈의 셀에 '10'이 적혀 있다면, glass_A 잔으로 마신 와인 중 10개가 low 알코올 빈에 속한다는 의미입니다.

### 강의 내용
교수님께서는 강의 음성에서 `wine data frame`에 있는 `alcohol bean categorical attribute`와 또 다른 범주형 속성(예: `glasses`)을 사용하여 `contingency table`을 계산하는 과정을 설명하고 계십니다.
*   `categories. low and mid and high.`: 알코올 빈이 `low`, `mid`, `high` 세 가지 범주로 나뉜다는 것을 언급합니다.
*   `So we have a alcohol bean categorical attribute in the wine data frame.`: 와인 데이터프레임에 알코올 빈이라는 범주형 속성이 있음을 강조합니다.
*   `So we have two categorical attributes and we compute close table. Contingency table and is set to CT.`: 두 개의 범주형 속성으로 분할표(contingency table)를 계산하고, 그 결과를 `CT` 변수에 저장한다고 설명합니다.
*   `So we pass this setE to heatmap, plot this table. And this anode is equal to true means that we have to write the actual count into each cell. That's why we have numbers here, each count.`: `CT`를 `heatmap` 함수에 전달하여 테이블을 플롯하며, 특히 `annot=True` 파라미터가 각 셀 안에 실제 개수(count)를 숫자로 표시하는 역할을 한다고 명확히 설명합니다. 이것이 히트맵에 숫자가 나타나는 이유입니다.
*   `So we have three glasses and three alcohol beans and then we have a contingency heat map.`: 최종적으로 세 종류의 잔과 세 가지 알코올 빈을 가진 분할표 히트맵이 생성된다고 요약합니다.

**💡 중요한 점**: 교수님의 음성 내용은 슬라이드 제목인 "Correlation Heatmap"과는 달리, *범주형 데이터*를 다루는 **분할표 히트맵(Contingency Heatmap)**의 예시를 설명하고 있습니다. 하지만 `heatmap` 시각화 도구의 기본적인 사용법 (예: `annot=True`)은 공통적으로 적용될 수 있습니다.

### 시험 포인트
*   ⭐ **상관관계 히트맵의 정의 및 용도**: Pearson $r$ 상관계수를 사용하여 수치형 특징 간의 선형 관계를 시각화하며, 다중공선성(multicollinearity) 등을 파악하는 데 활용됩니다.
*   ⭐ **히트맵 해석 방법**:
    *   색상의 강도(intensity): 상관관계의 크기 ($|r|$)를 나타냅니다.
    *   색상의 종류(hue): 상관관계의 방향(양의 상관관계 또는 음의 상관관계)을 나타냅니다.
    *   `Blocks/stripes` 패턴: 특징 그룹화 또는 유사한 경향을 가진 특징들을 의미합니다.
*   ⭐ **상관관계의 함정 (Pitfalls)**:
    *   `Correlation $\ne$ causation`: 상관관계는 인과관계를 의미하지 않습니다. (예: 아이스크림 판매량과 익사 사고는 상관관계가 있지만 인과관계는 아님)
    *   `outliers inflate $|r|$`: 이상치(outliers)는 상관계수 $r$의 절대값($|r|$)을 과장할 수 있습니다.
*   `annot=True` 파라미터의 기능: `seaborn.heatmap`에서 각 셀에 실제 데이터 값(예: 상관계수 또는 빈도수)을 표시하는 역할.

---
## Slide 36

**핵심 개념**
상관 히트맵(Correlation Heatmap)은 데이터셋 내의 모든 수치형 특성(numerical features) 쌍 간의 선형 상관관계를 시각적으로 한눈에 파악하기 위한 강력한 도구입니다. 각 셀의 색상은 두 변수 간의 피어슨 상관계수 값을 나타내며, 이를 통해 변수들 사이의 관계의 강도와 방향(양의 상관관계 또는 음의 상관관계)을 쉽게 이해할 수 있습니다. 이는 데이터의 전반적인 구조를 파악하고, 예측 모델을 위한 특성 선택(feature selection)이나 다중공선성(multicollinearity) 진단 등에 유용하게 활용됩니다.

**코드/수식 해설**

```python
# 1. 'wine' 데이터프레임에서 'target'과 'class' 컬럼을 제외한 수치형 특성만 선택
num = wine.drop(columns=["target", "class"])
# 2. 선택된 수치형 특성들 간의 상관 행렬(Correlation Matrix) 계산
#    pandas의 .corr() 메서드는 기본적으로 피어슨 상관계수를 계산합니다.
corr = num.corr()
# 3. seaborn 라이브러리를 사용하여 상관 히트맵 시각화
sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap="vlag")
```

*   **`num = wine.drop(columns=["target", "class"])`**: 데이터프레임 `wine`에서 'target' 및 'class'와 같이 상관분석 대상이 아닌 컬럼(주로 범주형이거나 분석 목적상 제외되는 컬럼)을 제거하고, 순수 수치형 특성들만 포함하는 새 데이터프레임 `num`을 생성합니다.
*   **`corr = num.corr()`**: `pandas.DataFrame`의 `corr()` 메서드를 호출하여 `num` 데이터프레임 내의 모든 수치형 특성 쌍 간의 피어슨 상관계수(Pearson Correlation Coefficient)를 계산합니다. 이 결과는 각 특성을 행과 열로 하는 상관 행렬(correlation matrix)이 됩니다.

    피어슨 상관계수 $ r_{xy} $는 다음과 같이 계산됩니다:
    $$ r_{xy} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}} $$
    여기서 $x$와 $y$는 두 변수, $n$은 데이터 포인트의 수, $\bar{x}$와 $\bar{y}$는 각 변수의 평균입니다. 상관계수는 항상 $ -1 $과 $ 1 $ 사이의 값을 가집니다.

*   **`sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap="vlag")`**: `seaborn` 라이브러리의 `heatmap` 함수를 사용하여 `corr` 변수에 저장된 상관 행렬을 시각화합니다.
    *   `corr`: 시각화할 데이터(상관 행렬)입니다.
    *   `vmin=-1`, `vmax=1`: 히트맵의 색상 스케일(color scale)의 최소값과 최대값을 지정합니다. 상관계수는 $ -1 $에서 $ 1 $ 사이의 값을 가지므로 이 범위로 설정하는 것이 표준적입니다.
    *   `center=0`: 색상 팔레트의 중앙값을 $0$으로 설정합니다. 이는 $0$을 기준으로 양의 상관관계와 음의 상관관계를 시각적으로 명확하게 구분하는 데 도움을 줍니다. 예를 들어, $0$을 중심으로 양수는 한 가지 색조 스펙트럼으로, 음수는 다른 색조 스펙트럼으로 나타낼 수 있습니다.
    *   `cmap="vlag"`: 사용할 컬러맵(colormap)을 지정합니다. 'vlag'는 파란색-밝은색-빨간색 계열의 컬러맵으로, $0$ 주변을 밝게 표시하고 양수와 음수로 갈수록 색상이 진해져 상관관계의 방향과 강도를 직관적으로 보여주는 데 효과적입니다.

**구체적 예시**
슬라이드의 "Wine — Correlation Heatmap"은 와인 데이터셋의 다양한 물리화학적 특성들(예: `alcohol`, `malic_acid`, `total_phenols`, `proline` 등) 간의 상관관계를 보여줍니다.
*   **색상 해석**:
    *   밝은 노란색/밝은 색: $1$에 가까운 강한 양의 상관관계. 한 특성이 증가하면 다른 특성도 증가하는 경향이 큽니다.
    *   진한 파란색/보라색: $ -1 $에 가까운 강한 음의 상관관계. 한 특성이 증가하면 다른 특성은 감소하는 경향이 큽니다.
    *   녹색/중간 색: $0$에 가까운 약한 상관관계 또는 무상관. 두 특성 사이에 선형적인 관계가 거의 없거나 전혀 없음을 나타냅니다.
*   **대각선**: 모든 특성은 자기 자신과 완벽하게 양의 상관관계($ r=1 $)를 가지므로, 히트맵의 대각선은 항상 가장 밝은 노란색으로 표시됩니다.
*   **대칭성**: 상관 행렬은 대칭적입니다. 즉, 특성 A와 B의 상관계수는 특성 B와 A의 상관계수와 같습니다. 따라서 히트맵의 상삼각형과 하삼각형은 거울상처럼 동일한 정보를 가집니다.

이러한 시각화를 통해, 예를 들어 `total_phenols`와 `flavanoids` 사이에는 강한 양의 상관관계가 있고, `alcohol`과 `malic_acid` 사이에는 약한 양의 상관관계가 있음을 쉽게 파악할 수 있습니다.

**강의 내용**
교수님께서는 상관 히트맵이 "모든 수치형 특성들 간의 전체적인 그림을 한눈에 볼 수 있는(high level overview)" 매우 유용한 도구임을 강조하셨습니다. 특히, "모든 가능한 쌍(all possible pairs)"에 대해 "선형 상관관계(linear correlation)"를 측정하는 데 사용된다고 명확히 설명하셨습니다. 이는 이전 슬라이드에서 다루었을 수 있는 범주형-범주형 변수 간의 관계 시각화(categorical versus categorical view)와는 달리, 수치형 변수-수치형 변수 간의 관계를 탐색하는 방법임을 암시합니다.

**시험 포인트**
*   ⭐ 상관 히트맵은 두 **수치형 변수** 간의 **선형 상관관계**를 시각화하는 데 사용됩니다.
*   ⭐ 상관계수 값의 범위는 $ -1 $부터 $ 1 $까지이며, 각각 강한 음의 상관, 무상관, 강한 양의 상관을 의미합니다. ⭐
*   ⭐ `pandas.DataFrame.corr()` 함수를 사용하여 상관 행렬을 계산하고, `seaborn.heatmap()` 함수를 사용하여 이를 시각화합니다.
*   ⭐ `seaborn.heatmap` 사용 시 `vmin`, `vmax`, `center`, `cmap`과 같은 파라미터는 시각화의 가독성과 해석에 중요한 역할을 합니다. 특히 `center=0`은 상관관계의 방향을 직관적으로 보여주는 데 핵심입니다.

---
## Slide 37

## 데이터분석 입문 (CSED226) 강의 노트

### 핵심 개념

*   **Parallel Coordinates (평행 좌표계)**
    *   **정의**: 각 샘플(데이터 포인트)은 수직으로 정렬된 여러 특성(Feature) 축을 가로지르는 하나의 꺾은선(`polyline`)으로 표현되는 다변량 시각화 기법입니다. 각 축은 데이터셋의 한 특성을 나타내며, 이 축들은 서로 평행하게 배치됩니다.
    *   **사용 시점**:
        *   클래스(그룹)별 다변량 프로필(`multivariate profiles`)을 비교할 때 유용합니다.
        *   강한 분리(`strong separation`)를 보이거나 빈번한 교차(`crossings`)가 나타나는 축(특성)을 찾을 때 사용합니다.
    *   **해석 방법**:
        *   **축을 따라 나타나는 분리(Separation along an axis)**: 해당 특성이 범주를 구분하는 **식별력 있는 특성(discriminative feature)**임을 시사합니다.
        *   **빈번한 교차(Frequent crossings)**: 여러 특성 간의 **상호작용(interaction)**이나 **상충 관계(trade-offs)**가 있음을 나타냅니다.
    *   **주의 사항 (Pitfalls)**:
        *   데이터 샘플의 수가 `n`이 클 경우, 선들이 너무 많아져 **시각적 혼란(clutter)**이 발생할 수 있습니다.
        *   해결책: 특성을 **표준화(`standardize features`)**하거나, 투명도(`transparency`)를 사용하거나, 데이터 샘플을 **다운샘플링(`downsample`)** 또는 **취합(`aggregate`)**하여 해결할 수 있습니다.

### 코드/수식 해설

강의 음성에서 언급된 **Pearson 상관 계수(Pearson Correlation Coefficient)**는 두 변수 $X$와 $Y$ 사이의 선형 관계 강도와 방향을 측정하는 통계량입니다.

$$
r_{xy} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \sum_{i=1}^{n}(y_i - \bar{y})^2}}
$$

*   여기서 $x_i$와 $y_i$는 $i$번째 데이터 포인트의 $X$와 $Y$ 값입니다.
*   $\bar{x}$와 $\bar{y}$는 각각 $X$와 $Y$의 표본 평균입니다.
*   $n$은 데이터 포인트의 총 개수입니다.

이 계수 $r_{xy}$는 $-1$에서 $1$까지의 값을 가집니다.

*   $r_{xy} = 1$: 완벽한 양의 선형 상관관계 (Perfect Positive Correlation)
*   $r_{xy} = -1$: 완벽한 음의 선형 상관관계 (Perfect Negative Correlation)
*   $r_{xy} = 0$: 선형 상관관계 없음 (No Linear Correlation)

### 구체적 예시

**Parallel Coordinates 예시:**
어떤 자동차 데이터셋에 '연비', '마력', '무게', '가속 시간'이라는 4가지 특성이 있다고 가정해 봅시다. Parallel Coordinates 플롯에서 각 자동차는 이 4개의 수직 축을 연결하는 하나의 선으로 표현됩니다.

*   만약 '연비' 축에서 고연비 자동차들의 선이 모두 높은 값에 모여있고, 저연비 자동차들의 선이 낮은 값에 모여있다면, '연비' 특성이 자동차의 종류를 구분하는 중요한 특성임을 알 수 있습니다.
*   '무게' 축과 '가속 시간' 축 사이에서 선들이 서로 교차하는 패턴이 빈번하게 보인다면, 이는 차량의 무게가 증가할수록 가속 시간도 늘어나는 경향이 있지만, 특정 구간에서는 다른 특성(예: 엔진 종류)에 따라 상충 관계가 발생할 수 있음을 시사합니다.

**Pearson 상관 계수 시각화 예시:**
강의에서 언급된 것처럼, 여러 특성 간의 Pearson 상관 계수를 계산한 후 이를 **히트맵(heatmap)**으로 시각화하면 각 쌍의 특성 간 선형 연관성을 색상으로 빠르게 파악할 수 있습니다. 예를 들어, '무게'와 '마력' 특성 사이의 상관 계수가 $0.8$이라면, 히트맵에서 해당 셀은 진한 양의 상관을 나타내는 색으로 표시될 것입니다.

### 강의 내용

교수님께서는 이 슬라이드 구간에서 주로 **Pearson 상관 계수**와 **다중공선성(Multicollinearity)**의 개념을 설명하고 계십니다.

*   **Pearson 상관 계수의 범위와 의미**: Pearson 상관 계수가 $-1$에서 $1$까지의 값을 가지며, $-1$은 완전한 음의 상관관계, $1$은 완전한 양의 상관관계를 나타낸다고 강조하셨습니다.
*   **히트맵을 통한 시각화**: 이 값을 인코딩하기 위해 색상이 사용되며, 이러한 "히든 맵"(아마도 Correlation Heatmap을 의미하는 것으로 보임)을 통해 모든 선형 연관성을 빠르게 스캔할 수 있다고 설명하셨습니다.
*   **다중공선성의 중요성**: 특히 이 히트맵이 **다중공선성(Multicollinearity)**을 찾아내는 데 중요하다고 강조하셨습니다.
*   **다중공선성의 의미**: 다중공선성은 "두 개 이상의 특성(변수)이 서로 강하게 상관되어 있는 상태"를 의미하며, 이는 머신러닝 모델의 안정성과 해석에 문제를 일으킬 수 있는 중요한 문제입니다. 교수님은 "when two or more your..."라고 하시면서 다중공선성의 정의를 시작하셨습니다.

이러한 설명은 다변량 데이터 분석에서 각 특성 간의 관계를 이해하는 것이 얼마나 중요한지, 특히 단순한 쌍별 상관관계를 넘어 다중공선성과 같은 복합적인 문제를 파악하는 데 시각화 도구가 어떻게 활용될 수 있는지에 대한 맥락을 제공합니다. Parallel Coordinates는 이러한 다변량 관계를 탐색하는 또 다른 강력한 시각화 도구로 볼 수 있습니다.

### 시험 포인트

*   ⭐ **Parallel Coordinates의 정의, 사용 목적, 해석 방법, 그리고 한계점(Pitfalls) 및 해결책**을 명확히 이해하고 설명할 수 있어야 합니다. (특히 `standardize features`, `transparency`, `downsample/aggregate`는 중요합니다.)
*   ⭐ **Pearson 상관 계수**의 범위와 $-1$, $0$, $1$의 의미를 정확히 알아야 합니다.
*   ⭐ **다중공선성(Multicollinearity)**의 개념과 왜 데이터 분석에서 중요한 문제로 다뤄지는지 설명할 수 있어야 합니다. (히트맵을 통한 발견 방법과 함께 기억하면 좋습니다.)
*   Parallel Coordinates와 상관 히트맵이 각각 어떤 종류의 다변량 관계를 시각화하는 데 효과적인지 비교할 수 있으면 좋습니다.

---
## Slide 38

**핵심 개념**
*   **평행 좌표계 (Parallel Coordinates Plot)**: 다차원 데이터를 시각화하는 강력한 방법입니다. 각 변수는 평행한 세로축으로 표현되며, 각 데이터 샘플은 이 축들을 가로지르는 하나의 선으로 나타납니다. 이를 통해 여러 변수 간의 관계, 데이터의 군집 패턴, 이상치 등을 시각적으로 쉽게 파악할 수 있습니다.
*   **데이터 표준화 (Data Standardization)**: 데이터의 스케일을 통일하는 전처리 과정입니다. 각 특성(feature)의 평균을 0으로, 표준편차를 1로 조정합니다. 서로 다른 척도와 단위를 가진 변수들이 머신러닝 모델의 성능에 미치는 영향을 균일하게 만들고, 특히 거리 기반 알고리즘(예: K-Nearest Neighbors, SVM)에서 필수적입니다.

**코드/수식 해설**

```python
# Standardize in this exact order
X = iris[features].to_numpy()
X = StandardScaler().fit_transform(X)
df_scaled = pd.DataFrame(X, columns=features)
df_scaled["species"] = iris["species"]
plt.figure(figsize=(7.6, 4.4))
parallel_coordinates(df_scaled, "species", features, lw=0.9, alpha=0.45)
plt.tight_layout()
plt.show()
```

1.  `X = iris[features].to_numpy()`: `iris` 데이터셋에서 `features` 변수(꽃잎, 꽃받침 길이/폭)에 해당하는 열들만 선택하여 NumPy 배열 `X`로 변환합니다. `scikit-learn`의 `StandardScaler`는 주로 NumPy 배열을 입력으로 받기 때문에 이 과정이 필요합니다.
2.  `X = StandardScaler().fit_transform(X)`: `scikit-learn`의 `StandardScaler` 객체를 생성하고, `fit_transform()` 메소드를 사용하여 `X` 데이터를 표준화합니다.
    *   `fit()`: 입력 데이터 `X`의 각 특성별 평균($\mu$)과 표준편차($\sigma$)를 계산합니다.
    *   `transform()`: 계산된 $\mu$와 $\sigma$를 사용하여 데이터를 다음 수식에 따라 표준화합니다.
        $$z = \frac{x - \mu}{\sigma}$$
        여기서 $x$는 원본 데이터 포인트, $z$는 표준화된 데이터 포인트입니다.
3.  `df_scaled = pd.DataFrame(X, columns=features)`: 표준화된 NumPy 배열 `X`를 다시 `pandas` DataFrame으로 변환합니다. 이때 원본 `features` 이름을 열 이름으로 지정합니다.
4.  `df_scaled["species"] = iris["species"]`: 표준화된 특징들만 포함된 `df_scaled` DataFrame에 원본 `iris` DataFrame의 'species' (붓꽃의 종) 열을 추가합니다. 이는 평행 좌표계에서 각 종별로 다른 색상을 부여하여 시각적으로 구분하기 위함입니다.
5.  `parallel_coordinates(df_scaled, "species", features, lw=0.9, alpha=0.45)`: `pandas.plotting` 모듈의 `parallel_coordinates` 함수를 호출하여 평행 좌표계 그래프를 생성합니다.
    *   첫 번째 인자 `df_scaled`: 시각화할 DataFrame.
    *   두 번째 인자 `"species"`: 각 선을 색상으로 구분할 범주형 열의 이름.
    *   세 번째 인자 `features`: 평행 축으로 사용할 수치형 특징 변수들의 리스트.
    *   `lw=0.9`: 각 선의 두께(linewidth)를 0.9로 설정합니다.
    *   `alpha=0.45`: 각 선의 투명도(alpha)를 0.45로 설정하여, 여러 선이 겹칠 때 데이터 밀집도를 파악하기 용이하게 합니다.
6.  `plt.show()`: 생성된 평행 좌표계 그래프를 화면에 표시합니다.

**구체적 예시**
Iris 데이터셋은 붓꽃의 종(species)과 네 가지 수치형 특징(꽃잎 길이/폭, 꽃받침 길이/폭)으로 구성됩니다. 이 예시에서는 이 네 가지 특징을 표준화한 후 평행 좌표계로 시각화합니다.
그래프를 보면 'setosa' 종(일반적으로 주황색 선)의 선들이 다른 두 종('versicolor', 'virginica')과 확연히 구분되어 있는 것을 알 수 있습니다. 특히, 'petal length (cm)'와 'petal width (cm)' 축에서는 낮은 값에 집중되어 있고, 'sepal width (cm)' 축에서는 상대적으로 높은 값에 집중되어 있습니다. 슬라이드 하단의 분석("Setosa has smaller Petals, but its Sepal tends to be wider.")이 이 시각화 결과와 일치함을 보여줍니다. 평행 좌표계를 통해 각 특징의 분포와 종별 차이를 한눈에 파악할 수 있습니다.

**강의 내용**
교수님께서는 예측 변수(predictor variables)들이 서로 높은 상관관계를 가질 수 있으며, 이는 선형 상관관계(linear correlation)를 통해 확인할 수 있다고 강조하셨습니다. 또한, "각 속성이 자기 자신과 강하게 상관되어 있다(each attribute is strongly correlated with itself)"는 점은 상관 행렬(correlation matrix)의 대각선 요소가 항상 1인 기본적인 특성을 언급하며, 데이터 분석 시 이러한 관계를 고려해야 함을 시사했습니다.

강의 음성 후반부에 "So we drop the categorical value attribute from the Y data frame and then call this CORR and pass this information to hitmap." 부분은 현재 슬라이드의 평행 좌표계 시각화 코드와 직접적으로 관련되지는 않지만, 데이터 전처리 및 탐색적 데이터 분석(EDA) 과정에서 **상관 행렬(Correlation Matrix)을 생성하고 히트맵(Heatmap)으로 시각화**하는 단계에 대한 설명으로 해석됩니다. 이는 변수들 간의 선형 관계를 파악하는 또 다른 중요한 방법이며, 보통 수치형 변수들을 대상으로 하며 범주형 변수는 제외하거나 별도로 처리합니다.

**시험 포인트**
*   ⭐ **평행 좌표계의 해석**: 평행 좌표계 그래프를 보고 다변량 데이터의 특징 패턴, 변수 간의 관계, 그리고 특정 그룹(예: 붓꽃의 종)의 특성을 설명할 수 있어야 합니다.
*   ⭐ **데이터 표준화의 중요성**: `StandardScaler`와 같은 데이터 표준화가 왜 필요한지, 그리고 표준화가 머신러닝 모델의 성능과 결과 해석에 어떤 영향을 미치는지 구체적으로 설명할 수 있어야 합니다. (특히 거리 기반 알고리즘과의 연관성)
*   ⭐ **`scikit-learn` `StandardScaler`의 활용**: `fit_transform()` 메소드의 기능과 표준화 수식($z = (x - \mu) / \sigma$)을 이해하고, 이를 실제 코드에 적용할 수 있어야 합니다.
*   ⭐ **다변량 데이터 시각화 기법의 목적**: 여러 변수를 동시에 고려하는 시각화 기법(평행 좌표계 등)이 단변량/이변량 분석으로는 알기 어려운 어떤 통찰을 제공하는지 설명할 수 있어야 합니다.

---
## Slide 39

**핵심 개념**: 잔차 대 예측값(Residuals vs Fitted) 플롯

**코드/수식 해설**:
*   **정의**: 모델 가정을 평가하기 위해 예측값($\hat{y_i}$)과 잔차($y_i - \hat{y_i}$)를 플로팅하는 기법입니다. 선형 회귀 모델의 기본 가정이 잘 충족되는지 시각적으로 확인하는 데 사용됩니다.
*   **수식**: 플롯은 $(\hat{y_i}, y_i - \hat{y_i})$ 형태의 점들을 표시합니다.
    *   $\hat{y_i}$: $i$번째 관측치에 대한 모델이 예측한 종속 변수의 값 (Fitted value).
    *   $y_i$: $i$번째 관측치에 대한 실제 관측된 종속 변수의 값 (Observed value).
    *   $y_i - \hat{y_i}$: $i$번째 관측치에 대한 잔차(Residual). 실제 값과 예측 값의 차이입니다.

**구체적 예시**:
선형 회귀 모델을 통해 어떤 데이터셋을 학습한 후, 이 모델이 데이터의 패턴을 잘 포착했는지, 그리고 모델의 가정이 유효한지 진단할 때 Residuals vs Fitted 플롯을 사용합니다.
예를 들어, 교육 수준에 따른 소득을 예측하는 모델을 만들었다고 가정해 봅시다.
*   $x_i$: $i$번째 사람의 교육 수준 (예: 학년).
*   $y_i$: $i$번째 사람의 실제 소득.
*   $\hat{y_i}$: 모델이 예측한 $i$번째 사람의 소득.
*   $y_i - \hat{y_i}$: $i$번째 사람에 대한 소득 예측 오차(잔차).
이 플롯에서 만약 잔차들이 예측값($\hat{y_i}$)이 커질수록 더욱 넓게 퍼지는 부채꼴 형태를 보인다면, 이는 이분산성(heteroscedasticity) 문제(즉, 오차의 분산이 예측값에 따라 일정하지 않음)를 의미하며, 모델의 신뢰성에 영향을 줄 수 있습니다.

**강의 내용**:
제공된 음성 전사는 현재 슬라이드의 내용(잔차 대 예측값 플롯)과는 일치하지 않고, 상관 행렬(correlation matrix) 및 평행 좌표(parallel coordinates) 플롯 등 다른 시각화 기법에 대해 설명하고 있습니다 (예: Iris 데이터셋의 꽃잎, 꽃받침 길이/너비 속성).
현재 슬라이드는 선형 모델 진단 도구인 잔차 대 예측값 플롯의 **정의, 사용 시점, 해석 방법 및 주의사항**을 설명하고 있습니다. 이 플롯은 선형 회귀 모델의 가정을 평가하는 데 있어 매우 중요한 시각화 도구임을 강조합니다.

**시험 포인트**:
*   ⭐ **Residuals vs Fitted 플롯의 목적**: 선형 회귀 모델의 핵심 가정을 시각적으로 진단하는 데 사용됩니다. 특히, **비선형성(nonlinearity), 이분산성(heteroscedasticity), 이상치(outliers)** 등의 문제를 감지하는 데 유용합니다.
*   ⭐ **이상적인 플롯의 해석**: 잔차들이 0을 중심으로 무작위적으로(randomly) 분포하며, 특정 패턴(예: U자형, 곡선형, 부채꼴/나팔관 형태)이나 추세가 없어야 합니다. 이는 모델 가정이 잘 충족되고 있음을 의미합니다.
*   ⭐ **플롯에서 발견되는 문제점과 시사하는 바**:
    *   **잔차가 0을 중심으로 랜덤하게 분포하지 않고 패턴을 보일 경우**: 모델이 데이터의 비선형적인 관계를 제대로 포착하지 못했음을 시사합니다 (예: 선형 모델이 아닌 2차 함수 모델이 더 적합할 수 있음).
    *   **잔차의 분산이 예측값에 따라 변하는 부채꼴(fan-shape) 형태를 보일 경우**: **이분산성(heteroscedasticity)** 문제가 있음을 나타냅니다. 이는 모델의 표준 오차와 신뢰 구간이 부정확해질 수 있음을 의미합니다.
    *   **다른 점들로부터 크게 벗어난 점들**: **이상치(outliers)** 또는 **영향력 있는 관측치(influential observations)**일 수 있습니다.
*   ⭐ **주의사항 (Pitfalls)**: 잔차 플롯만으로는 모든 문제를 진단하기 어렵습니다. 특히, **영향력(leverage/influence)**이 큰 관측치는 잔차가 크지 않더라도 모델에 큰 영향을 미 미칠 수 있으므로, **쿡의 거리(Cook's distance)**와 같은 다른 통계량을 통해 별도로 확인해야 합니다.

---
## Slide 40

---
**핵심 개념**:
"잔차 대 적합값 (Residuals vs Fitted)" 플롯은 선형 회귀 모델의 진단에 사용되는 핵심적인 시각화 도구입니다. 모델이 데이터에 얼마나 잘 맞는지, 그리고 선형 회귀의 주요 가정이 충족되는지 확인하는 데 도움을 줍니다. 이 플롯은 예측값($\hat{y}$)을 가로축에, 잔차($e = y - \hat{y}$)를 세로축에 두어 그립니다.

**코드/수식 해설**:

```python
# Basic linear fit: target ~ bmi
x = diabetes["bmi"].to_numpy() # BMI 데이터를 numpy 배열로 변환하여 독립 변수 x로 사용
y = diabetes["target"].to_numpy() # Target 데이터를 numpy 배열로 변환하여 종속 변수 y로 사용
slope, intercept = np.polyfit(x, y, 1) # np.polyfit을 사용하여 1차 다항식(선형 회귀)의 기울기와 절편을 계산
fitted = slope * x + intercept # 계산된 기울기와 절편으로 예측값(적합값) fitted를 계산
residuals = y - fitted # 실제값 y에서 예측값 fitted를 빼서 잔차(residuals)를 계산

# Seaborn plot: residuals vs fitted
sns.set_theme() # Seaborn 기본 테마 설정
ax = sns.scatterplot(x=fitted, y=residuals, alpha=0.7) # 예측값(fitted)을 x축에, 잔차(residuals)를 y축에 두어 산점도 생성
ax.axhline(0, linestyle="--", linewidth=1.2) # y=0에 파선(대시 라인)을 그려 잔차의 기준선 표시
ax.set(
    xlabel="fitted (linear on bmi)", # x축 레이블 설정
    ylabel="residual", # y축 레이블 설정
    title="Diabetes: Residuals vs Fitted" # 플롯 제목 설정
)
plt.tight_layout() # 레이아웃을 자동으로 조절하여 겹치는 부분 없게 함
plt.show() # 플롯 출력

# Alternative (classic residual plot: predictor on x-axis):
# sns.residplot(data=diabetes, x="bmi", y="target")
# Seaborn의 residplot 함수는 독립 변수("bmi")를 x축에, 잔차를 y축에 두어 잔차 플롯을 쉽게 생성할 수 있는 대안적인 방법입니다.
```
*   **잔차($e$)**: 실제 관측값 $y$와 모델에 의해 예측된 값 $\hat{y}$의 차이입니다. 즉, $e = y - \hat{y}$입니다.
*   **적합값($\hat{y}$)**: 모델이 독립 변수($x$)를 사용하여 예측한 종속 변수($y$)의 값입니다. 선형 회귀에서는 $\hat{y} = \beta_0 + \beta_1 x$ 형태로 표현됩니다. (`slope`가 $\beta_1$, `intercept`가 $\beta_0$에 해당).

**구체적 예시**:
당뇨병 데이터셋(`diabetes`)에서 `bmi` (체질량 지수)를 사용하여 `target` (질병 진행도)을 예측하는 간단한 선형 회귀 모델을 가정합니다.
*   **이상적인 "잔차 대 적합값" 플롯**: 잔차들이 0을 중심으로 무작위적으로 흩어져 있는 형태여야 합니다. 이는 모델이 선형성을 잘 만족하고, 잔차의 분산이 일정하며(등분산성), 잔차가 독립적이라는 선형 회귀의 가정을 시사합니다.
*   **문제 상황 예시**:
    *   **패턴이 보이는 경우 (U자형, 깔때기형 등)**: 모델의 선형성 가정이 위배되었거나 (U자형), 잔차의 분산이 적합값에 따라 변동하는 이분산성(heteroscedasticity, 깔때기형) 문제가 있음을 나타냅니다.
    *   **특정 적합값에서 잔차가 비정상적으로 큰 경우**: 해당 관측치가 이상치(outlier)일 가능성이 있습니다.

**강의 내용**:
교수님께서는 이전 슬라이드의 내용(평행 좌표 플롯에서 Setosa 품종이 꽃잎 길이와 너비에서 낮은 값을 가지고, 꽃받침 너비에서 높은 값을 가짐을 통해 패턴을 확인하는 과정)을 먼저 설명하신 후, 본 슬라이드의 "잔차 대 적합값 플롯"에 대해 언급하셨습니다. 교수님께서는 이 플롯이 "그렇게 중요하지는 않다(not that important)"고 하시면서도, 그 역할에 대해서는 "단지 예측값(your prediction)과 잔차(residual)를 플롯하는 것"이라고 간략하게 설명하셨습니다. 이는 이 플롯의 개념을 간단히 소개하고 다음 주제로 넘어가기 위한 것으로 해석됩니다.

**시험 포인트**:
*   ⭐ **잔차($e$)의 정의**: 실제 관측값 $y$와 모델의 예측값 $\hat{y}$의 차이인 $y - \hat{y}$임을 정확히 이해해야 합니다.
*   ⭐ **"잔차 대 적합값" 플롯의 목적**: 선형 회귀 모델이 선형성, 등분산성(homoscedasticity), 잔차의 독립성 등 주요 가정을 잘 충족하는지 진단하기 위함입니다.
*   ⭐ **이상적인 "잔차 대 적합값" 플롯의 형태**: 잔차들이 0을 중심으로 무작위적으로 흩어져 있어야 합니다. 특정 패턴(U자형, 깔때기형 등)이 나타나면 모델에 문제가 있음을 의미합니다.

---
## Slide 41

- **핵심 개념**:
  'Residuals vs Fitted' 플롯은 회귀 모델의 진단에 사용되는 핵심 시각화 도구입니다. 이 플롯은 모델이 예측한 값(fitted values)과 실제 관측값 간의 차이, 즉 잔차(residuals)를 시각화합니다. 이 플롯을 통해 회귀 모델의 가정(선형성, 등분산성, 오차의 독립성 등)이 잘 충족되는지 평가할 수 있습니다. 이상적인 경우, 잔차들은 0을 중심으로 특별한 패턴 없이 무작위로 분포되어야 합니다.

- **코드/수식 해설**:
  잔차($e_i$)는 실제 관측값($y_i$)에서 모델의 예측값($\hat{y}_i$)을 뺀 값으로 정의됩니다.
  $$ e_i = y_i - \hat{y}_i $$
  슬라이드의 플롯에서 $x$-축은 모델의 예측값, 즉 'fitted (linear on bmi)'를 나타내고, $y$-축은 'residual'을 나타냅니다. 각 점은 특정 데이터 포인트에 대한 모델의 예측값과 해당 예측값의 잔차를 보여줍니다.

- **구체적 예시**:
  슬라이드에 제시된 'Diabetes: Residuals vs Fitted' 플롯은 당뇨병 데이터셋에 선형 회귀 모델을 적용했을 때의 잔차 분포를 보여줍니다.
  *   **$y=0$ 선**: 플롯의 가로 점선은 잔차가 0인 지점을 나타냅니다. 이 선에 가까운 점일수록 모델의 예측이 실제값에 매우 근접했다는 것을 의미합니다.
  *   **점들의 위치**:
      *   $y$-축 값이 0에 가까운 점: 예측과 실제값의 차이가 작아 모델의 예측이 정확했음을 의미합니다.
      *   $y$-축 값이 0에서 멀리 떨어진 점: 예측과 실제값의 차이가 커서 모델의 예측 오류가 컸음을 의미합니다. 예를 들어, $y=150$ 근처의 점은 모델이 실제값을 크게 과소평가했음을, $y=-150$ 근처의 점은 크게 과대평가했음을 나타냅니다.
  *   **패턴 분석**: 이 플롯에서 잔차들이 $x$-축을 따라 특정 패턴(예: 깔때기 모양, 곡선 모양)을 보인다면, 이는 모델이 데이터의 패턴을 잘 포착하지 못했거나, 회귀 모델의 기본 가정이 위배되었을 가능성이 있음을 시사합니다. 슬라이드의 플롯에서는 잔차들이 다소 넓게 퍼져 있으며, 특히 fitted 값이 높아질수록 잔차의 분산이 증가하는 경향(heteroscedasticity)이 있는 것처럼 보일 수 있습니다.

- **강의 내용**:
  교수님께서는 잔차를 "ground truth minus your prediction"으로 명확히 정의하며, $y$-축이 잔차($e_i$), $x$-축이 예측값($\hat{y}_i$)임을 강조하셨습니다. 특정 점(예: $y$-축 0 근처)을 지적하며 해당 지점에서는 "prediction is very close to ground truth"라고 설명하셨고, 다른 지점에서는 "significant error"가 존재함을 언급하셨습니다. 또한, 플롯에서 "some patterns"을 볼 수 있지만, 이 특정 플롯은 "very useful"하지 않을 수 있으며, "old style looking at the residuals"의 한 방법이라고 언급하셨습니다. 이는 이 기본적인 시각화 방법을 이해하는 것이 중요하지만, 더 정교한 분석 방법이나 현대적인 진단 도구가 존재함을 암시할 수 있습니다.

- **시험 포인트**:
  *   ⭐ **잔차(Residual)의 정의**: 실제값과 예측값의 차이를 정확히 설명할 수 있어야 합니다 ($e_i = y_i - \hat{y}_i$).
  *   ⭐ **Residuals vs Fitted Plot의 목적**: 왜 이 플롯을 사용하는지 (모델 진단, 가정 검토) 이해해야 합니다.
  *   ⭐ **이상적인 Residuals vs Fitted Plot의 특징**: 잔차가 0을 중심으로 무작위로 분포되어야 하며, 어떤 명확한 패턴도 없어야 함을 알고 있어야 합니다.
  *   ⭐ **Residuals vs Fitted Plot에서 패턴 발견 시의 의미**: 특정 패턴(예: 곡선, 깔때기 모양)이 나타났을 때 모델의 어떤 가정이 위배되었는지(선형성 부족, 등분산성 위배 등) 설명할 수 있어야 합니다.

---

