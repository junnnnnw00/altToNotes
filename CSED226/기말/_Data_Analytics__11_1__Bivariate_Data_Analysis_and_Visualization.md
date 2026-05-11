# CSED226 - _Data_Analytics__11_1__Bivariate_Data_Analysis_and_Visualization 상세 해설 노트 (음성 전사 포함)

> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다. Alt(altalt.io) 음성 전사 데이터를 함께 활용했습니다.

---

## Slide 1

**핵심 개념**
이번 강의는 `Bivariate & Multivariate Visualization`에 대한 입문입니다.
*   **Bivariate Visualization**: 두 가지 속성(attributes) 간의 관계를 시각화합니다.
*   **Multivariate Visualization**: 두 가지 이상의 여러 속성(multiple attributes) 간의 복잡한 관계를 이해하기 위한 시각화 기법을 다룹니다.

**강의 맥락**
교수님은 오늘 강의가 단일 변수(single variable) 시각화(예: 히스토그램)를 넘어, 데이터 내의 두 개 이상의 변수 간의 복잡한 관계를 파악하는 기술에 중점을 둘 것이라고 설명했습니다. 이는 데이터의 여러 차원(attributes)을 동시에 분석하고 이해하는 데 필요한 시각화 기법들을 학습하는 중요한 과정입니다.

**시험 포인트**
*   ⭐ **Bivariate**와 **Multivariate** 시각화의 정의를 정확히 이해하는 것이 중요합니다.
    *   `Bivariate`: 두 속성
    *   `Multivariate`: 다중 속성 (두 개 이상)

---

## Slide 2

이 슬라이드는 이변량(bivariate) 및 다변량(multivariate) 시각화 기법의 전체 로드맵을 제시합니다.

**핵심 개념**:
- **이변량(Bivariate) 시각화**: 두 개의 속성 간의 관계를 탐색하는 기법입니다.
  - `Relational (X-Y)`: Scatter plot, Line plot, Regression/LOESS (OLS, Loess), Figure-level faceting (relplot)
  - `Bivariate Density`: Hexbin/2D Hist (jointplot(kind="hex"/"hist")), 2D KDE (jointplot(kind="kde"))
- **다변량(Multivariate) 시각화**: 두 개 이상의 속성 간의 복잡한 관계를 이해하기 위한 기법입니다.
  - `Distributions (by group)`: Hist/KDE (displot, kdeplot), ECDF (ecdfplot), Box/Violin/Boxen (boxplot, violinplot, boxenplot), Raw points (stripplot/swarmplot)
  - `Matrix / Structure`: Pair plot, Correlation heatmap, Clustered heatmap
  - `Multivariate Projections`: PCA scatter (PCA + scatterplot), Parallel coordinates
  - `Diagnostics`: Residuals vs Fitted
- **Faceting & Encodings**: `hue`, `style`, `size`, `row`/`col`, `col_wrap` 등 시각적 인코딩을 통해 다변량 데이터를 효과적으로 표현할 수 있습니다.
- 강의에서 사용할 데이터셋은 Iris, Wine, Diabetes, Synthetic (df_long) 등입니다.

**강의 맥락**:
- 교수님은 오늘 강의가 "단일 변수(예: 히스토그램)를 넘어 두 개 이상의 변수 간의 복잡한 관계를 이해"하기 위한 이변량 및 다변량 시각화 기술을 다룰 것임을 강조합니다. 이 슬라이드가 오늘 다룰 내용의 로드맵이라고 설명합니다.
- `Relational (X-Y)` 플롯과 `Bivariate Density` 플롯이 첫 번째 주제로 소개됩니다.
- `Distributions (by group)` 플롯에 대해 설명하며, "히스토그램, KDE, ECDF, 바이올린, 박스 플롯 등이 단일 속성에 대한 것"이지만, "하나의 차트에 여러 플롯을 중첩하면 단일 속성 이상을 다룰 수 있다"고 설명하여 그룹별 분포 비교의 중요성을 강조합니다.
- `Matrix / Structure` 플롯은 "모든 피처의 전체 그림을 한 번에 볼 수 있는 매우 강력한 플롯"이라고 설명하며 `pair plot`, `correlation heatmap`, `cluster heatmap`을 예로 듭니다.
- `Multivariate Projections` 중 PCA는 건너뛰지만, "고차원 데이터 시각화를 위한 Parallel coordinates"와 "모델 진단을 위한 Diagnostic plots"는 다룰 것임을 명시합니다.
- 마지막으로 Iris, Wine, Diabetes, Synthetic 데이터셋을 사용할 것이라고 언급하며 지난주와 동일한 데이터셋을 활용할 것이라고 말합니다.

**시험 포인트**:
- ⭐ 이변량(bivariate)과 다변량(multivariate) 시각화의 개념적 차이와 목표를 이해해야 합니다.
- ⭐ 각 플롯 카테고리(예: Relational, Distributions by group, Matrix/Structure)에 속하는 대표적인 플롯들이 어떤 종류의 관계를 시각화하는 데 주로 사용되는지 알아야 합니다.
- ⭐ `hue`, `style`, `size`와 같은 시각적 인코딩이 어떻게 다변량 데이터를 단순한 X-Y 플롯에 추가하여 표현하는지에 대한 이해가 중요합니다.

---

## Slide 3

**핵심 개념**:
산점도(Scatter plot)는 가장 기본적이고 강력한 시각화 도구 중 하나로, 각 관측치를 $x_i, y_i$ 점으로 표현합니다. 두 개의 수치형 변수 간의 관계를 탐색하는 데 사용됩니다. `hue` (범주형), `size` (수치형), `style` (마커)와 같은 추가적인 인코딩을 통해 다변량 데이터를 표현할 수 있습니다.

**사용 시기**:
두 수치형 변수 간의 선형/비선형 관계, 데이터 군집(clusters), 이상치(outliers)를 탐색할 때 사용합니다.

**해석 방법**:
점들의 기울기(slope)와 형태(shape)를 관찰합니다. 점들이 조밀하게 밴드를 이루면 강한 관계를, 분산되어 있으면 약한 관계를 나타냅니다. 뚜렷하게 분리된 점들의 덩어리는 군집(clusters)을 의미합니다.

**주의사항**:
데이터의 양($n$)이 많을 경우, 점들이 서로 겹쳐서 데이터 패턴을 파악하기 어려운 오버플로팅(over-plotting) 문제가 발생할 수 있습니다. 이를 완화하기 위해 투명도(`alpha`)를 조절하거나 밀도 플롯(density plot)을 활용할 수 있습니다.

**강의 맥락**:
교수님은 산점도를 "가장 중요하고 기본적인 플롯"으로 소개하며, 각 관측치 $(x_i, y_i)$를 점으로 표시하는 것이 기본적인 정의라고 설명합니다. 산점도의 진정한 힘은 `hue` (범주형 변수에 색상 부여), `size` (수치형 변수에 크기 부여), `style` (마커 형태)와 같은 추가적인 인코딩을 통해 여러 변수를 동시에 다룰 수 있다는 점을 강조합니다. 산점도는 두 **수치형 변수** 간의 관계를 탐색하는 데 목표를 둡니다. 점들의 기울기, 점 구름의 형태를 보고, "tight band"는 강한 관계를, "diffuse cloud"는 약한 관계를 의미한다고 설명합니다. ⭐특히, 데이터셋이 매우 클 때 발생하는 **오버플로팅(over-plotting)** 문제를 언급하며, 투명도 조절이나 밀도 플롯을 대안으로 제시합니다.

**시험 포인트**:
*   산점도가 주로 탐색하는 두 변수의 ⭐**데이터 타입**은 무엇인가요? (정답: 두 수치형 변수)
*   산점도에서 다변량 데이터를 표현하기 위한 ⭐**추가 인코딩 방식 세 가지**를 설명하세요. (정답: `hue` (색상), `size` (크기), `style` (마커 형태))
*   대규모 데이터셋에서 산점도를 그릴 때 발생하는 ⭐**가장 큰 문제점**은 무엇이며, 이를 해결하기 위한 방법은 무엇인가요? (정답: 오버플로팅; 투명도 조절, 밀도 플롯 활용)

---

## Slide 4

---
### **핵심 개념**
이 슬라이드는 Seaborn 라이브러리를 사용한 산점도(Scatter plot)의 코드 예시와 그 실행 결과를 보여줍니다. 산점도는 두 개의 수치형 변수 간의 관계를 시각화하는 데 기본적이지만, `hue` (색상), `size` (크기), `style` (스타일) 등의 인코딩을 추가하여 여러 변수 간의 복합적인 관계를 표현할 수 있습니다.

### **코드/수식 해설**
```python
sns.scatterplot(data=iris,
                x="petal length (cm)", y="petal width (cm)",
                hue="species", alpha=0.7)
```
*   `sns.scatterplot()`: Seaborn 라이브러리에서 산점도를 그리는 함수입니다.
*   `data=iris`: 그래프를 그릴 데이터프레임으로 `iris` 데이터셋을 사용합니다.
*   `x="petal length (cm)"`: X축에 'petal length (cm)' 변수를 매핑합니다.
*   `y="petal width (cm)"`: Y축에 'petal width (cm)' 변수를 매핑합니다.
*   `hue="species"`: 'species' 변수를 색상(hue)으로 인코딩하여, 각 점의 색상이 붓꽃의 종(species)에 따라 달라지도록 합니다. 이는 범주형 변수를 시각화에 추가하는 방법입니다.
*   `alpha=0.7`: 점들의 투명도를 `0.7`로 설정하여, 점들이 겹치는 경우에도 밀도를 파악할 수 있도록 합니다.

### **구체적 예시**
아이리스(Iris) 데이터셋을 활용하여 꽃잎의 길이(`petal length`)와 꽃잎의 너비(`petal width`) 간의 관계를 산점도로 시각화한 예시입니다. 여기에 `species` 변수를 색상(`hue`)으로 추가하여, 세 가지 붓꽃 종(setosa, versicolor, virginica)이 꽃잎의 길이와 너비 공간에서 어떻게 분포하는지 한눈에 파악할 수 있습니다.

### **강의 맥락**
교수님은 이 슬라이드를 "Seabones scatter plot API"의 예시라고 설명하며, `x`축에 'petal length', `y`축에 'petal width'를 매핑했다고 강조합니다. 특히 `hue`를 'species'로 설정한 것이 핵심이라고 설명하는데, 이는 Seaborn이 세 가지 붓꽃 종 각각에 따라 점들을 색깔로 구분하도록 지시한 것입니다. `alpha`를 `0.7`로 설정하여 부분적인 투명도를 추가했습니다.

결과적으로, 만약 모든 점이 한 가지 색이었다면 단순히 강한 양의 선형 관계를 보았겠지만, `hue`를 추가함으로써 훨씬 더 풍부한 관계를 파악할 수 있게 되었다고 설명합니다.
*   'setosa' 종은 왼쪽 아래에 밀집되고 완전히 분리 가능한 클러스터를 형성합니다.
*   나머지 두 종(versicolor, virginica)도 서로 구별되며, 특히 'virginica'는 'setosa'에 비해 더 큰 'petal length'와 'petal width'를 가집니다.
이는 `hue`를 'species'로 설정함으로써 얻을 수 있는 새로운 정보라고 강조합니다.

### **시험 포인트**
*   ⭐ **산점도(Scatter Plot)의 기본 역할**: 두 수치형 변수 간의 관계(`x`, `y`)를 시각화합니다.
*   ⭐ **다변량 데이터 시각화**: `hue` (색상), `size` (크기), `style` (스타일) 등의 인코딩을 사용하여 산점도에 추가적인 변수(특히 범주형 변수)를 매핑하는 방법을 이해해야 합니다.
*   ⭐ `hue` 파라미터가 그래프 해석에 미치는 영향: 범주형 변수를 색상으로 구분하여 각 그룹별로 데이터의 분포 및 관계를 파악할 수 있게 합니다.
*   ⭐ `alpha` 파라미터의 역할: 데이터 포인트가 많아 겹쳐 보일 때 투명도를 조절하여 과밀도(over-plotting) 문제를 완화하고 밀집도를 시각적으로 파악하는 데 도움을 줍니다.

---

## Slide 5

### Line Plot - 정의 및 사용법

**핵심 개념**
Line plot은 데이터의 관측값들을 `x`축의 **순서(ordered)**에 따라 연결하여 시각화하는 차트입니다. Scatter plot과 혼동하기 쉽지만, Line plot은 `x`축의 순서가 핵심적인 차이점입니다.

**구체적 예시**
*   **사용 시점**: 시간 경과에 따른 추세(예: 주식 가격, 웹사이트 트래픽, 실험 데이터의 변화)나, 불확실성 구간(uncertainty bands)을 포함한 평균 추세(mean trend)를 보여줄 때 주로 사용됩니다.
*   **해석 방법**:
    *   **기울기(Slope)**: 변화율(rate of change)을 나타냅니다.
    *   **곡률(Curvature)**: 가속도(acceleration)를 나타냅니다.
    *   **신뢰 구간(CI band width)**: 추정치의 안정성(stability)이나 확실성을 나타냅니다.
*   **주의사항 (Pitfalls)**: `x`축이 시간, 날짜, 월, 연도 등과 같이 자연스럽고 논리적인 순서(natural logical order)를 가져야 합니다. 순서가 없는 범주형 데이터(예: 도시 이름 'New York', 'London', 'Tokyo')를 Line plot으로 연결해서는 안 됩니다. 이 경우 Bar chart와 같은 다른 시각화 방법을 고려해야 합니다.

**강의 맥락**
교수님은 Line plot이 Scatter plot과 자주 혼동되지만, 근본적으로 다르다고 강조하셨습니다. 특히, Line plot은 `x`축의 관측값들을 '순서대로(in order)' 연결하며, 여기서 'ordered'가 가장 중요한 키워드라고 설명하셨습니다. `x`축은 시간(time), 날짜(days), 월(months), 연도(years) 등과 같이 자연적인 순서를 가져야 한다고 하셨습니다. Line plot은 주로 시간의 흐름에 따른 추세(trends over time)를 시각화하는 데 사용되며, 주식 가격이나 웹사이트 트래픽 같은 데이터를 예시로 들었습니다. 또한, 기울기를 통해 변화율을, 곡률을 통해 가속도를, 그리고 신뢰 구간 밴드를 통해 추정치의 안정성을 파악할 수 있다고 하셨습니다. 가장 흔한 실수로, 순서가 없는 범주(unordered categories)를 연결하는 것을 지적하며, 'New York', 'London', 'Tokyo'와 같은 도시 데이터를 Line plot으로 연결하면 안 된다고 강조하셨습니다.

**시험 포인트**
*   ⭐Line plot은 `x`축이 **순서(ordered)**를 가지는 데이터에 사용된다. (예: 시간, 날짜)
*   ⭐**절대 순서가 없는 범주형 데이터(unordered categories)에는 Line plot을 사용하지 않아야 한다.** (예: 도시, 국가 등)

---

## Slide 6

### Line — Data Generation & Code (with CI)

**핵심 개념**:
이 슬라이드는 Seaborn의 `lineplot`을 사용하여 시계열 데이터의 추세와 그 추정치의 불확실성을 시각화하는 방법을 설명합니다. 특히, 여러 반복 측정(repeated measures)이 있는 데이터에 대해 평균 추세와 신뢰 구간(Confidence Interval, CI)을 함께 표시하여 데이터의 안정성 또는 추정치의 확실성을 보여줍니다.

**코드/수식 해설**:

```python
# 1-9: df_long 데이터프레임 생성
# 각 시간 단계(T=100)와 그룹('A', 'B')에 대해 30번(n_rep=30) 반복 측정된 가상 시계열 데이터 생성
rng = np.random.default_rng(42)
T, n_rep = 100, 30
time = np.arange(T)
rows = []
for g, base, slope in [("A", 0.0, 0.03), ("B", 0.3, 0.02)]:
    for r in range(n_rep):
        # y 값은 기본값 + 선형 추세 + 사인파 + 노이즈로 구성
        y = base + slope*time + 0.4*np.sin(time/7.5) + rng.normal(0,0.15,T)
        rows.append(pd.DataFrame({"time":time, "value":y, "group":g, "rep":r}))
df_long = pd.concat(rows, ignore_index=True)

# 11-12: sns.lineplot을 사용하여 데이터 시각화
sns.lineplot(data=df_long, x="time", y="value", hue="group", errorbar=("ci", 95))
```
- `rng = np.random.default_rng(42)`: 난수 생성을 위한 시드(seed)를 설정하여 결과를 재현 가능하게 합니다.
- `T = 100`: 시간 단계를 100으로 설정합니다. `time` 변수는 $0$부터 $99$까지의 배열이 됩니다.
- `n_rep = 30`: 각 그룹 및 시간 단계에 대해 30번의 반복 측정을 시뮬레이션합니다.
- `for g, base, slope in [("A", 0.0, 0.03), ("B", 0.3, 0.02)]`: 그룹 'A'와 'B'를 정의하고, 각각의 기본값(`base`)과 기울기(`slope`)를 설정합니다.
- `y = base + slope*time + 0.4*np.sin(time/7.5) + rng.normal(0,0.15,T)`: 각 반복 측정의 `value`($y$)를 계산하는 수식입니다. 선형 추세($\text{slope} \times \text{time}$), 주기적인 패턴($0.4 \times \sin(\text{time}/7.5)$), 그리고 가우시안 노이즈($\text{rng.normal}(0,0.15,T)$)가 더해져 복합적인 시계열 데이터를 만듭니다.
- `pd.concat(rows, ignore_index=True)`: 생성된 개별 `DataFrame`들을 하나로 합쳐 `df_long` 데이터프레임을 완성합니다.
- `sns.lineplot(...)`: 라인 플롯을 생성합니다.
    - `data=df_long`: 사용할 데이터프레임을 지정합니다.
    - `x="time"`: x축에 `time` 변수를 매핑합니다. (⭐라인 플롯은 x축이 반드시 순서가 있는(ordered) 데이터여야 합니다.)
    - `y="value"`: y축에 `value` 변수를 매핑합니다.
    - `hue="group"`: `group` 변수에 따라 다른 색상의 라인을 그립니다 (그룹 'A'와 'B').
    - `errorbar=("ci", 95)`: 이는 가장 중요한 매개변수로, 각 그룹의 30개 반복 측정값들을 집계하여 평균(solid line)을 표시하고, 95% 신뢰 구간(shaded regions)을 계산하여 시각화하도록 지시합니다.

**구체적 예시**:
슬라이드 하단의 그래프는 위 코드를 통해 생성된 두 그룹('group A', 'group B')의 시계열 데이터를 라인 플롯으로 시각화한 결과입니다. 각 그룹의 실선은 30회 반복 측정된 `value`의 평균 추세를 나타내며, 실선 주변의 음영 처리된 영역은 해당 평균 추세에 대한 95% 신뢰 구간을 보여줍니다. 이를 통해 시간에 따른 각 그룹의 변화 추세와 그 추세가 얼마나 안정적인지를 파악할 수 있습니다.

**강의 맥락**:
"Okay. So this is how we use a line plot. So I first sent the synthetic time series data and we created two groups A and B. And for each group we simulated 30 repetitions and over 100 time steps. And then we call this line plot. Here we map time to x, value to y, and group to hue. So that's why we have two curves, line plot, line curves for group A and group B. The most important parameter here is that error bar is a pair of CI, competence interval 55%. We have a 30 repetition for each group. Instead of drawing 60 message lines, this tells C-bone to aggregate them. And each time it calculates the mean of the 30 repetition and the bootstrap 95% confidence interval for that mean. Okay. So resulting plot is clean and powerful. And the solid line, the mean trend and the shaded regions are the 55% confidence interval. If you dream in, you will see this shaded area which corresponds to the 55% confidence interval. Okay."

교수님은 라인 플롯 사용 방법을 설명하며, 먼저 합성 시계열 데이터를 생성하여 그룹 A와 B를 만들었으며, 각 그룹에 대해 30번의 반복 측정과 100개의 시간 단계를 시뮬레이션했다고 강조합니다. 이후 `sns.lineplot`을 호출하여 `time`을 x축, `value`를 y축, `group`을 `hue`로 매핑했음을 설명합니다. 가장 중요한 매개변수는 `errorbar=('ci', 95)`이며, 이는 각 그룹에 대한 30개의 반복 측정을 집계하여 60개의 개별 라인을 그리는 대신, 각 시간 단계에서 30개 반복의 평균을 계산하고 부트스트랩 95% 신뢰 구간을 계산하도록 Seaborn에 지시한다고 설명합니다. 결과적으로 깔끔하고 강력한 플롯이 생성되며, 실선은 평균 추세를, 음영 처리된 영역은 95% 신뢰 구간을 나타낸다고 강조합니다. (교수님은 55%라고 언급했지만, 코드와 시각화에서는 95% 신뢰 구간을 사용하고 있습니다.)

**시험 포인트**:
* ⭐`seaborn.lineplot`에서 `errorbar=('ci', 95)`와 같은 파라미터가 어떤 역할을 하는지, 특히 반복 측정 데이터에서 평균 추세와 신뢰 구간을 함께 시각화하는 방법과 그 의미를 이해해야 합니다.
* ⭐라인 플롯은 x축 데이터가 시간, 날짜 등과 같이 "순서가 있는(ordered)" 경우에 주로 사용되며, 정렬되지 않은 범주형 데이터를 연결하는 데 사용해서는 안 됩니다.

---

## Slide 7

**핵심 개념**:
회귀 플롯은 산점도(scatter plot)에 적합된 모델(주로 선형 모델)을 추가하여 데이터의 추세를 요약하는 시각화 방법입니다. 주요 회귀 모델로는 OLS와 LOESS가 있습니다.

*   **OLS (Ordinary Least Squares)**: 가장 일반적인 선형 모델로, 잔차 제곱합을 최소화하는 단일 직선을 데이터에 맞춥니다.
    *   **정의**: $E[Y|X] = \beta_0 + \beta_1 X$ (여기서 $E[Y|X]$는 $X$가 주어졌을 때 $Y$의 기대값, $\beta_0$는 절편, $\beta_1$는 기울기).
*   **LOESS (Locally Estimated Scatterplot Smoothing)**: 지역적으로 가중치를 부여하여 부드러운 곡선을 피팅하는 비모수적 방법입니다. OLS가 이상치에 민감할 때 대안으로 사용될 수 있으며, 산점도가 노이즈가 많을 때 중심 추세를 요약하는 데 적합합니다.

**사용 시기**:
*   데이터의 중심 추세를 요약할 때.
*   그룹별 기울기(관계)를 비교할 때.

**그래프 해석**:
*   **기울기($\beta_1$)**: 관계의 방향(양의 상관관계/음의 상관관계)과 강도를 나타냅니다.
*   **음영 처리된 영역($\pm$ CI Envelope)**: 회귀선의 95% 신뢰 구간(confidence interval)을 나타내어 추정치의 안정성이나 불확실성을 보여줍니다.
*   **잔차 진단(Residual Diagnostics)**: 모델의 적합 품질을 평가하는 데 사용됩니다.

**주의 사항 (Pitfalls)**:
*   **OLS**: 이상치(outliers)에 매우 민감합니다.
*   **LOESS**: 대역폭(bandwidth) 매개변수가 부드러움(smoothness)을 제어하며, 적절한 대역폭 선택이 중요합니다.

**강의 맥락**:
교수님은 회귀 플롯이 산점도에 "fitted model, typically linear model"을 추가하여 "summarize the trend"한다고 설명합니다. OLS는 "Ordinary List Scale"이라고 하며, "single straight line that best minimize the error"를 피팅하며, 선형 대수학(linear algebra) 시간에 배웠을 것이라고 언급합니다. LOESS에 대해서는 "local smoother"로 "explicitly summarize a central trend when the scatterplot is noisy"할 때 사용한다고 강조합니다. 그래프를 읽는 방법으로 "look at the slope"와 "Shade Area is 55% confidence interval for the regression line itself"를 언급합니다. OLS가 이상치에 민감할 때 LOESS를 사용하며, LOESS의 대역폭이 "smoothness"를 제어한다고 설명합니다.

**시험 포인트**:
*   ⭐ **OLS와 LOESS의 정의 및 차이점**: OLS는 선형 모델, LOESS는 지역 가중 부드러움 모델.
*   ⭐ **각 모델의 주요 사용 목적**: OLS는 일반적인 선형 추세 요약, LOESS는 노이즈가 많거나 비선형적인 데이터의 중심 추세 요약.
*   ⭐ **각 모델의 주요 단점**: OLS는 이상치에 민감, LOESS는 대역폭 조절 필요.
*   ⭐ **회귀 플롯에서 기울기(slope)와 신뢰 구간(confidence interval)의 의미**.

---

## Slide 8

**핵심 개념**
회귀(Regression) 플롯은 산점도(scatter plot) 위에 데이터 간의 경향을 요약하는 모델, 주로 선형 모델을 추가하여 변수 간의 관계를 시각화합니다. 가장 일반적인 모델은 최소제곱법(OLS, Ordinary Least Squares)으로, 데이터에 가장 잘 맞는 직선을 찾아 그립니다. OLS가 이상치에 민감하거나 전반적인 선형 관계가 명확하지 않을 때는 지역 평활화(Loess, Locally Estimated Scatterplot Smoothing)를 사용하여 데이터의 지역적인 추세를 보여줄 수 있습니다.

**코드/수식 해설**

```python
# OLS 선형 회귀 모델 플롯
sns.regplot(data=wine, x="alcohol", y="color_intensity")

# 지역 평활화(Local smoother) Loess 모델 플롯
# lmplot은 regplot보다 더 강력한 기능을 제공하며, 'lowess=True'로 Loess를 지정할 수 있습니다.
sns.lmplot(data=wine, x="alcohol", y="color_intensity", lowess=True)
```
*   `sns.regplot()`: 두 수치형 변수 ($x$, $y$) 간의 관계를 산점도로 표현하고, 기본적으로 OLS 선형 회귀선을 추가합니다. `data` 인자로 사용할 데이터프레임을 지정합니다.
*   `sns.lmplot()`: `regplot`과 유사하지만, 더 많은 시각적 인코딩(예: `hue`, `col`, `row`)을 지원하는 figure-level 함수입니다. `lowess=True`를 설정하여 OLS 대신 Loess 회귀 곡선을 플로팅할 수 있습니다.

**구체적 예시**
슬라이드의 예시는 `wine` 데이터셋의 `alcohol` (알코올 함량)과 `color_intensity` (색상 강도) 변수 간의 관계를 `sns.regplot`을 사용하여 시각화한 것입니다. 플롯은 알코올 함량이 높아질수록 색상 강도도 높아지는 강한 양의 선형 관계를 보여줍니다. 주황색 선은 OLS로 추정된 선형 회귀선입니다.

**강의 맥락**
교수님께서는 회귀 플롯이 산점도에 적합 모델, 주로 선형 모델을 추가하여 추세를 요약한다고 설명하셨습니다. 가장 일반적인 모델인 OLS(Ordinary Least Squares)는 선형 대수학에서 배운 내용이라고 언급하시며, 오류를 최소화하는 직선을 찾는다고 하셨습니다. OLS의 대안으로 Loess(Local Smoother)를 설명하며, 산점도가 노이즈가 많을 때 중앙 추세를 명시적으로 요약하고 싶을 때 사용한다고 강조하셨습니다. OLS가 이상치(outlier)에 너무 민감할 때 Loess를 사용할 수 있다고 덧붙이셨습니다. 이 슬라이드의 코드는 `wine` 데이터셋의 `alcohol`과 `color_intensity`를 사용하며, `regplot`이 기본 OLS 선형 적합을 제공하고, Loess 곡선을 얻기 위해서는 `sns.lmplot`에서 `lowess=True`를 지정해야 함을 설명하셨습니다. 결과 플롯은 알코올과 색상 강도 사이에 강한 양의 선형 관계가 있음을 명확히 보여준다고 강조하셨습니다.

**시험 포인트**
*   ⭐ **회귀 플롯의 목적**: 두 수치형 변수 간의 관계를 산점도와 함께 추세선으로 요약하고 시각화합니다.
*   ⭐ **OLS(Ordinary Least Squares) vs. Loess(Locally Estimated Scatterplot Smoothing)**:
    *   **OLS**: 전역적인 선형 관계를 가정하고 단일 직선으로 추세를 요약합니다.
    *   **Loess**: 데이터의 지역적인 부분에 가중치를 두어 부드러운 곡선을 피팅하는 지역 평활화 기법입니다. 데이터에 비선형적인 추세가 있거나 OLS가 이상치에 민감할 때 유용합니다.
*   ⭐ **`seaborn` 함수**: `sns.regplot()`은 기본적으로 OLS 선형 회귀를 수행하고, `sns.lmplot(lowess=True)`를 사용하여 Loess 곡선을 그릴 수 있습니다.

---

## Slide 9

---

## relplot — Definition & When to Use

### 핵심 개념
`relplot`은 `scatterplot`과 `lineplot`의 상위 개념인 figure-level 래퍼 함수로, 데이터의 서브그룹별 관계를 여러 개의 작은 플롯(small multiples)으로 동시에 시각화할 때 사용됩니다. `kind` 파라미터를 통해 `scatter` 또는 `line` 플롯 중 하나를 선택하여 그릴 수 있습니다.

### 코드/수식 해설
`relplot` 사용 시 `kind` 파라미터로 시각화 종류를 지정합니다.
- `kind="scatter"`: 각 서브그룹에 대한 산점도를 그립니다.
- `kind="line"`: 각 서브그룹에 대한 선 그래프를 그립니다.

### 강의 맥락
교수님은 `relplot`을 새로운 플롯 타입이 아니라 `scatter plot`과 `line plot`을 위한 "figure-level wrapper"라고 설명하셨습니다. 주로 데이터를 서브그룹으로 나누어(small multiples) 각 서브그룹에 대해 동일한 플롯을 그리거나, 이를 그리드 형태로 배치하고자 할 때 사용한다고 강조했습니다. `kind` 파라미터를 `scatter` 또는 `line`으로 설정하는 방법을 언급했습니다.

### 시험 포인트
*   `relplot`이 `scatterplot`과 `lineplot`의 **figure-level 래퍼**라는 점을 이해하고 있어야 합니다. ⭐
*   `relplot`의 주요 사용 목적은 데이터를 **서브그룹으로 나누어(faceting)** 여러 개의 작은 플롯(small multiples)으로 관계를 비교하는 것입니다. ⭐
*   `kind` 파라미터를 통해 `scatter` 또는 `line` 플롯을 선택할 수 있다는 것을 기억하세요.

---

## Slide 10

**핵심 개념**
`relplot`은 Seaborn에서 제공하는 Figure-level 함수로, `scatterplot`과 `lineplot`의 상위 래퍼(wrapper)입니다. 데이터를 서브그룹으로 나누어(faceting), 각 서브그룹에 대해 동일한 유형의 플롯을 그리며 이를 그리드 형태로 배치하여 "small multiples"를 생성할 때 사용합니다. 이는 여러 범주형 변수에 따라 데이터의 관계를 시각적으로 비교할 때 매우 유용합니다.

**코드/수식 해설**

```python
sns.relplot(
    data=iris,
    x="sepal length (cm)", y="sepal width (cm)",
    hue="species", col="species", kind="scatter",
    col_wrap=3, height=3.0, aspect=1.05, alpha=0.75
)
```
- `data=iris`: 사용할 데이터프레임을 `iris`로 지정합니다.
- `x="sepal length (cm)"`, `y="sepal width (cm)"`: 각 산점도의 $x$축과 $y$축에 해당하는 수치형 변수를 지정합니다.
- `hue="species"`: `species` 범주에 따라 점의 색상을 다르게 지정합니다.
- `col="species"`: `species` 범주별로 별도의 산점도를 생성하여 열(column) 방향으로 배치합니다 (faceting).
- `kind="scatter"`: 생성할 플롯의 종류를 산점도(scatter plot)로 지정합니다. `line`으로도 설정 가능합니다.
- `col_wrap=3`: 열 방향으로 배치될 플롯의 최대 개수를 3개로 지정합니다. 3개를 초과하면 다음 행으로 넘어갑니다.
- `height=3.0`, `aspect=1.05`: 각 플롯의 높이와 종횡비를 설정하여 전체적인 레이아웃을 조정합니다.
- `alpha=0.75`: 점의 투명도를 설정합니다.

**구체적 예시**
Iris 데이터셋을 사용하여 `sepal length`와 `sepal width` 간의 관계를 `species`별로 분리하여 산점도를 그리는 예시입니다. `setosa`, `versicolor`, `virginica` 세 종별로 각기 다른 플롯이 생성되어 그리드 형태로 배치됩니다.

**강의 맥락**
"Ok, next plot is a real plot. So real plot is not a new plot type. It's a figure level wrapper for scatter plot and line plot. So you use this when you want to create small multiples. that is breaking your data into subgroups, drawing the same plot for each subgroup, and arrange in a grid. You just tell it kind is set to scatter or kind is equal to line. So we have three categories and we have three different scatterplots. by using this real plug. And if you look at the setosa, it has a clear kind of positive correlation between separate length and separate width. And versicola, the middle, shows a weaker correlation. And virginica shows a positive correlation."

`relplot`은 `scatterplot`이나 `lineplot` 자체는 아니지만, 이들을 여러 개 만들어서 그리드 형태로 보여주는 Figure-level 함수입니다. 데이터를 서브그룹으로 나누어 각 서브그룹에 대해 같은 플롯을 그리고 이를 그리드에 정렬할 때 사용합니다. `kind` 파라미터를 `scatter` 또는 `line`으로 설정할 수 있습니다. 이 예시에서는 Iris 데이터셋의 세 가지 종(`species`)에 따라 세 개의 다른 산점도를 만들었습니다. `setosa`는 `sepal length`와 `sepal width` 사이에 명확한 양의 상관관계를 보이며, `versicolor`는 약한 상관관계를, `virginica`는 양의 상관관계를 보여줍니다.

**시험 포인트**
- ⭐ `relplot`의 주요 용도는 무엇인가요? (Small multiples / Faceting)
- ⭐ `relplot`은 어떤 종류의 플롯을 감싸는(wrapper) 함수인가요? (`scatterplot`과 `lineplot`)
- ⭐ `col` 또는 `row` 파라미터는 `relplot`에서 어떤 역할을 하나요? (데이터를 서브그룹으로 나누어 그리드 형태로 플롯을 배치)

---

## Slide 11

### relplot — Line with CI & Facets (Repeated Measures)

-   **핵심 개념**:
    `sns.relplot`은 `scatterplot`과 `lineplot`의 상위 개념인 figure-level 래퍼 함수입니다. 데이터를 하위 그룹으로 나누어 각각 같은 종류의 플롯을 그린 후 그리드 형태로 배치하는 "small multiples"(작은 배수 플롯 또는 패싯)을 생성하는 데 사용됩니다. 특히 `kind="line"`을 사용하여 시간에 따른 추세나 순서 있는 데이터의 변화를 시각화하며, `errorbar` 파라미터를 통해 반복 측정 데이터의 평균과 신뢰 구간(Confidence Interval, CI)을 함께 보여줄 수 있습니다.

-   **코드/수식 해설**:

    ```python
    sns.relplot(
        data=df_long, # 사용할 데이터프레임 (예: 시계열 데이터)
        x="time",     # x축에 매핑할 변수 (시간)
        y="value",    # y축에 매핑할 변수 (관측값)
        hue="group",  # 'group' 변수에 따라 다른 색상 사용
        col="group",  # 'group' 변수에 따라 플롯을 열(column)로 분할하여 패싯 생성
        col_wrap=2,   # 열의 최대 개수를 2개로 제한하여 줄바꿈
        kind="line",  # 라인 플롯을 그림
        errorbar=("ci", 95), # 각 시점에서의 값들을 95% 신뢰 구간으로 집계
        height=3.0,   # 각 서브플롯의 높이
        aspect=1.25   # 각 서브플롯의 가로세로 비율
    )
    ```

    -   `data=df_long`: 시간 경과에 따른 값을 가진 `df_long`라는 합성 시계열 데이터를 사용합니다.
    -   `x="time"`, `y="value"`: `time`을 x축, `value`를 y축에 매핑하여 시계열 데이터의 변화를 나타냅니다.
    -   `hue="group"`: 데이터 내의 `group` 변수(예: 'group A', 'group B')에 따라 라인의 색상을 다르게 지정합니다.
    -   `col="group"`, `col_wrap=2`: `group` 변수의 각 고유값에 대해 별도의 열로 플롯을 분할하여 작은 배수 플롯(facets)을 만듭니다. `col_wrap=2`는 플롯이 2열을 초과하면 다음 줄로 넘어가도록 설정합니다.
    -   `kind="line"`: `relplot`이 내부적으로 `sns.lineplot`을 사용하여 선 그래프를 그리도록 지시합니다.
    -   `errorbar=("ci", 95)`: 이 파라미터가 가장 중요합니다. 각 시간 단계에서 여러 번의 반복 측정(예: 30회)이 있을 때, 모든 개별 라인을 그리는 대신, 해당 시점의 값들을 집계하여 평균(solid line)을 계산하고, 그 평균의 95% 부트스트랩 신뢰 구간(shaded regions)을 시각화합니다. 이를 통해 데이터의 중심 추세와 함께 추정치의 불확실성을 표현합니다.

-   **구체적 예시**:
    합성 시계열 데이터를 사용하여 두 개의 그룹(A와 B)을 생성하고, 각 그룹은 100개의 시간 단계에 걸쳐 30번 반복된 측정을 가집니다. 이 코드는 각 그룹에 대해 시간(`time`)에 따른 값(`value`)의 평균 변화 추이를 라인 플롯으로 보여주며, 그 주변에 95% 신뢰 구간을 음영 처리하여 표현합니다. `col="group"`으로 인해 'group A'와 'group B'의 플롯이 별도의 패싯으로 분리되어 비교하기 용이합니다.

-   **강의 맥락**:
    교수님은 `relplot`이 `scatter plot`과 `line plot`의 figure-level 래퍼이며, 데이터를 하위 그룹으로 나누어 같은 플롯을 그리드 형태로 배치하는 "small multiples"를 만들 때 유용하다고 설명합니다. 특히 이 슬라이드에 대해서는 "synthetic data `dflown`을 사용하고 `kind`를 `line`으로 설정했으며, `group`을 `color`(hue)로 사용했다. 이것은 group 1과 group 2, 즉 group A와 group B에 대해 각각 자체 95% 신뢰 구간을 가진 두 개의 개별 라인 플롯을 생성한다"고 강조합니다. 또한, 이전 `line plot` 설명에서 `errorbar=("ci", 95)`의 중요성에 대해 "각 그룹당 30번의 반복 측정이 있을 때, 60개의 라인을 그리는 대신, C-bone은 이들을 집계하여 각 시점의 30회 반복 측정의 평균과 해당 평균에 대한 95% 부트스트랩 신뢰 구간을 계산한다. 그 결과 플롯은 깔끔하고 강력하며, 실선은 평균 추세를, 음영 영역은 95% 신뢰 구간을 나타낸다"고 상세히 설명했습니다.

-   **시험 포인트**:
    *   ⭐ `sns.relplot`이 `sns.scatterplot`과 `sns.lineplot`의 figure-level 래퍼이며, "small multiples"(패싯)를 생성할 때 사용된다는 점을 이해해야 합니다.
    *   ⭐ `kind` 파라미터가 `scatter` 또는 `line`으로 설정될 수 있음을 알아야 합니다.
    *   ⭐ `errorbar=("ci", 95)` 파라미터가 반복 측정 데이터를 어떻게 집계하여 시각화하는지 (평균 선과 95% 신뢰 구간) 정확히 이해하고 설명할 수 있어야 합니다.

---

## Slide 12

### 핵심 개념
`Multiple Distributions`는 하나의 수치형 변수에 대해 여러 그룹(범주형 변수에 의해 정의됨) 간의 분포를 비교하는 시각화 기법입니다. 주로 `seaborn` 라이브러리의 `displot` (figure-level)이나 `kdeplot`, `histplot`, `ecdfplot` (axes-level)을 사용하여 구현됩니다.

### 강의 맥락
강의자는 이 섹션을 "비교 분포(comparing distributions), 다중 분포(multiple distributions)라고 부르는 다음 종류의 패밀리"로 소개하며, 하나의 수치형 변수와 하나의 범주형 변수가 있을 때 이들을 비교하는 데 사용된다고 설명합니다. `histogram`, `KDE`, `ECDF`와 같은 단일 변수 분포 플롯을 각 그룹별로 오버레이하여 여러 분포를 한 차트에 표시하는 방식입니다.

특히, `displot`에서 `hue` 파라미터를 사용하여 각 그룹(예: `species`)별로 색상을 다르게 하여 여러 히스토그램을 동시에 그리는 방법을 강조했습니다. 이는 단일 차트에서 여러 분포를 비교할 수 있게 합니다.

### 시험 포인트
*   **다중 분포 비교의 목적**: ⭐하나의 수치형 변수와 하나의 범주형 변수를 사용하여 그룹별 분포의 `location`(위치 이동), `spread`(분포 범위), `skew`(비대칭성), `tails`(꼬리), `multimodality`(여러 개의 봉우리)를 비교하는 것입니다. `stacked/fill` 옵션은 그룹별 `composition`(구성 비율)을 보여줄 때 유용합니다.
*   **정규화의 중요성**: ⭐`displot` 사용 시 `stat="density"` 파라미터는 각 히스토그램의 아래 면적 합이 1이 되도록 정규화하여, 샘플 수가 다른 그룹 간에도 공정한 비교를 가능하게 합니다. 그렇지 않으면 샘플이 많은 그룹이 단순히 더 커 보이게 되어 잘못된 해석을 유도할 수 있습니다.
    *   `stat="density"`
    *   `common_norm=False` (기본값)를 사용하여 각 그룹별로 정규화하는 것이 중요합니다.

---

## Slide 13

**핵심 개념**
`seaborn.displot`은 하나의 수치형 변수(`x`)의 분포를 여러 범주형 그룹(`hue`)에 걸쳐 비교할 때 사용됩니다. 이 슬라이드에서는 그룹별 히스토그램을 겹쳐 그려(`kind="hist"`) 분포의 차이를 시각적으로 파악하는 방법을 보여줍니다. `stat="density"`를 사용하여 각 히스토그램의 면적을 1로 정규화함으로써, 샘플 수가 다른 그룹 간에도 분포의 형태와 위치를 공정하게 비교할 수 있습니다.

**코드 해설**
```python
sns.displot(
    data=iris,                  # Iris 데이터셋 사용
    x="petal length (cm)",      # x축에 'petal length (cm)' 변수를 매핑
    hue="species",              # 'species' 변수를 기준으로 그룹을 나누고, 각 그룹을 다른 색상으로 표시
    kind="hist",                # 히스토그램 형태로 시각화
    bins=24,                    # 히스토그램의 막대(bin) 개수를 24개로 설정
    stat="density",             # y축 값을 밀도(density)로 표시하여 각 히스토그램의 전체 면적 합이 1이 되도록 정규화
    common_norm=False,          # 각 'species' 그룹별로 정규화를 수행 (전체 데이터셋 기준이 아님)
    element="step"              # 히스토그램 막대를 윤곽선(step) 형태로 표시하여 겹치는 부분을 명확하게 구분
)
```

**구체적 예시**
제공된 Iris 데이터셋 예시에서는 `petal length (cm)`의 분포를 세 가지 붓꽃 종(`setosa`, `versicolor`, `virginica`)별로 겹쳐진 히스토그램으로 보여줍니다. `stat="density"` 덕분에 각 종의 `petal length` 분포의 상대적인 모양과 집중도를 쉽게 비교할 수 있습니다. 예를 들어, `setosa` 종은 `petal length`가 2cm 미만으로 매우 짧은 곳에 밀집되어 있으며, `versicolor`와 `virginica`는 더 긴 `petal length`를 가지면서 서로 겹치지만, `virginica`가 `versicolor`보다 전반적으로 더 큰 `petal length` 분포를 보이는 것을 확인할 수 있습니다.

**강의 맥락**
교수님은 이 플롯이 "여러 분포를 비교하는" 데 사용되며, 특히 "하나의 수치형 변수와 하나의 범주형 변수"를 비교할 때 적합하다고 강조합니다. `hue` 파라미터를 `species`로 설정하여 세 개의 히스토그램을 하나의 차트에 "겹쳐서 그리는" 방법을 설명합니다. 특히 `stat="density"`의 중요성을 역설하며, "각 히스토그램 아래 면적의 합이 1이 되도록" 정규화하여 샘플 수가 다른 그룹 간에도 "공정한 비교"를 가능하게 한다고 설명합니다. 이는 그렇지 않으면 "샘플이 많은 그룹이 단순히 더 커 보일 것"이기 때문에 필수적인 설정이라고 언급합니다.

**시험 포인트**
*   ⭐ `sns.displot`을 사용하여 범주형 변수에 따른 수치형 변수의 분포를 비교하는 시각화 방법 (예: 겹쳐진 히스토그램)을 이해하는 것이 중요합니다.
*   ⭐ `hue` 파라미터의 역할: 데이터를 특정 범주형 변수를 기준으로 그룹화하여 시각화에 반영하는 데 사용됩니다.
*   ⭐ `stat="density"` 파라미터의 중요성: 이 파라미터가 각 그룹의 히스토그램 면적을 1로 정규화하여, 샘플 크기가 다른 그룹 간에도 분포의 형태를 왜곡 없이 공정하게 비교할 수 있게 하는 핵심적인 기능을 수행한다는 점을 기억해야 합니다.

---

## Slide 14

### kdeplot — Stacked/Fill Multiple KDEs

**핵심 개념**
`kdeplot`의 `multiple="fill"` 옵션을 사용하여 하나의 수치 변수(`x`)에 대한 여러 범주형 그룹(`hue`)의 분포를 누적 면적(stacked area) 형태로 시각화하는 방법입니다. 이 플롯은 특정 `x` 값에서 각 그룹이 전체에서 차지하는 **구성(composition) 또는 비율(proportion)**을 보여주며, 각 `x` 값에서의 총 높이는 100%로 정규화됩니다.

**코드 해설**

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

*   `sns.kdeplot()`: Seaborn 라이브러리의 커널 밀도 추정(Kernel Density Estimate) 플롯 함수입니다.
*   `data=iris`: 아이리스 데이터셋을 사용합니다.
*   `x="petal length (cm)"`: x축에 `petal length (cm)` 수치 변수를 매핑합니다.
*   `hue="species"`: `species` 범주에 따라 색상을 구분하여 각 종별 분포를 표시합니다.
*   `multiple="fill"`: KDE를 누적하여 채우는 방식으로 그립니다. 이 옵션은 각 `x` 값에서 모든 `hue` 그룹의 밀도를 합산하여 1 (100%)이 되도록 정규화합니다.
*   `common_norm=False`: 각 `hue` 그룹별로 정규화되지 않고, `multiple="fill"` 옵션에 따라 전체적으로 정규화되도록 설정합니다.
*   `bw_adjust=0.9`: 커널 밀도 추정 시 사용되는 대역폭(bandwidth)을 조정합니다. 값이 작을수록 더 세밀한 곡선이 생성됩니다.
*   `alpha=0.9`: 플롯의 투명도를 설정합니다.

**구체적 예시**
아이리스 데이터셋에서 `petal length (cm)` 값에 따라 세 가지 `species`(`setosa`, `versicolor`, `virginica`)가 각각 전체에서 어느 정도의 비율을 차지하는지 보여주는 누적 면적 그래프입니다. 예를 들어, `petal length`가 약 2.5cm 미만일 때는 대부분 `setosa` 종이 차지하고, 그 이후부터 `versicolor` 종이 점차 우세해지다가 `virginica` 종으로 넘어가는 패턴을 확인할 수 있습니다.

**강의 맥락**
교수님은 이 플롯이 `multiple="fill"` 옵션을 통해 "stacked area plot"을 생성한다고 강조하며, "각 `x` 값에서 전체 높이가 100%로 정규화된다"고 설명합니다. 또한, 이 플롯은 "개별 분포의 모양을 보여주기보다는 특정 `petal length`에서 종의 **구성(composition) 또는 비율(proportion)**"을 보여주는 데 중점을 둔다고 언급했습니다. x축은 `petal length`를 나타냅니다.

**시험 포인트**
*   ⭐ `kdeplot`에서 `multiple="fill"` 옵션의 역할 (누적 면적 그래프, 각 `x` 값에서 총 비율을 100%로 정규화).
*   ⭐ 이 플롯이 개별 분포의 모양이 아닌, 특정 `x` 값에서의 '구성 비율'을 파악하는 데 적합하다는 점.

---

## Slide 15

### Pair Plot (Scatter-Matrix) — Definition & When to Use

**핵심 개념**
Pair Plot (또는 Scatter-Matrix)은 데이터셋 내의 모든 숫자형 변수 쌍 간의 관계를 시각적으로 한눈에 파악할 수 있도록 해주는 강력한 다변량 시각화 도구입니다. 이 플롯은 각 변수 쌍에 대한 산점도(scatterplot)를 격자 형태로 배열하며, 대각선(diagonal)에는 각 변수의 단일 변수 분포(예: 히스토그램 또는 KDE)를 보여줍니다.

**강의 맥락**
교수님은 Pair Plot을 "**가장 중요하고 강력한(most important, powerful) 다변량 플롯**"으로 강조하며, "**데이터 분석을 시작할 때 가장 먼저 시도해야 할(start of your analysis)**" 플롯이라고 설명하셨습니다. 이는 "무차별적이지만(brute force) 놀랍도록 효과적인(incredibly effective)" 방법으로, "**모든 특징들의 전체 그림을 한 번에 볼 수 있는(seeing the entire picture of all your features at once)**" 데 매우 유용하다고 하셨습니다.

**사용 시점**
*   ⭐ **데이터 분석 초기 단계에서 변수 간의 모든 쌍별 관계를 빠르게 탐색할 때 사용합니다.**
*   변수들 간의 연관성(associations), 군집(clusters) 여부, 그리고 특정 레이블(label)에 따라 데이터가 얼마나 잘 분리되는지(separability)를 파악하고자 할 때 효과적입니다.

**읽는 방법**
*   **비대각선 셀(Off-diagonal cells)**: 두 변수 간의 관계를 보여주는 산점도입니다. 기울기, 점들의 밀집도 등을 통해 관계의 강도와 방향을 파악할 수 있습니다.
*   **대각선 셀(Diagonal cells)**: 각 변수의 단일 변수 분포를 보여줍니다 (예: 히스토그램, KDE). 이를 통해 각 변수의 분포 형태, 중심 경향, 퍼짐 정도를 알 수 있습니다.
*   `corner=True` 옵션을 사용하면 중복되는 플롯을 제거하여 아래쪽 삼각형 형태의 플롯만 표시할 수 있습니다.

**주의사항 (Pitfalls)**
*   ⭐ 특징(feature)의 개수 $d$에 따라 $O(d^2)$개의 축이 생성되므로, **변수의 개수가 많거나(many features) 데이터 포인트가 매우 많은(large $n$) 경우** 플롯이 너무 복잡해지거나 계산 비용이 커질 수 있습니다. 이 경우 샘플링(downsample)을 고려할 수 있습니다.

---

## Slide 16

**핵심 개념**
`Pair Plot`은 데이터셋 내의 모든 수치형 변수 쌍 간의 관계를 한눈에 파악할 수 있는 강력한 시각화 도구입니다. 각 변수의 단변수 분포(univariate distribution)와 변수 쌍 간의 이변수 관계(bivariate relationship)를 동시에 보여주며, 데이터 분석의 초기 단계에서 전반적인 특징을 파악하는 데 매우 유용합니다. 이는 데이터의 군집(cluster)을 찾고, 어떤 특성(feature)이 레이블 데이터를 잘 분리하는지 빠르게 스캔하는 데 도움을 줍니다.

**코드/수식 해설**

```python
sns.pairplot(
    iris,
    vars=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
    hue="species",
    corner=True,
    diag_kind="kde",
    plot_kws=dict(alpha=0.6, s=22)
)
```

*   `sns.pairplot(iris, ...)`: Seaborn 라이브러리의 `pairplot` 함수를 사용하여 `iris` 데이터프임을 시각화합니다.
*   `vars=["sepal length (cm)", ..., "petal width (cm)"]`: `pairplot`에 포함할 수치형 변수들을 지정합니다.
*   `hue="species"`: `species` 변수의 값에 따라 점들의 색깔을 다르게 하여, 각 품종별 패턴을 구분할 수 있게 합니다.
*   `corner=True`: 기본적으로 전체 변수 쌍의 행렬을 그리지만, 이 옵션을 `True`로 설정하면 대각선을 포함한 하삼각 행렬만 그려 불필요한 중복을 제거합니다.
*   `diag_kind="kde"`: 대각선(diagonal) 셀에 각 변수의 단변수 분포를 커널 밀도 추정(KDE, Kernel Density Estimate) 그래프로 표시합니다. 기본값은 히스토그램입니다.
*   `plot_kws=dict(alpha=0.6, s=22)`: 산점도(scatter plot)에 대한 추가적인 키워드 인수를 딕셔너리 형태로 전달합니다. `alpha=0.6`은 점의 투명도를 설정하여 겹침(over-plotting) 문제를 완화하고, `s=22`는 점의 크기를 설정합니다.

**구체적 예시**
제공된 슬라이드의 실행 결과는 `corner=True` 옵션이 적용되어 전체 변수 쌍 중 일부만 표시됩니다.
*   **대각선 셀**: `sepal length (cm)`와 `sepal width (cm)` 각 변수의 단변수 분포를 KDE 대신 히스토그램으로 보여줍니다. `diag_kind="kde"`로 지정되었으나, 슬라이드의 결과 이미지에서는 히스토그램으로 나타나 있습니다. (실제 코드 실행 시에는 KDE로 나타납니다.)
*   **대각선 외 셀**: `sepal length (cm)`와 `sepal width (cm)` 간의 관계를 나타내는 산점도(scatter plot)를 보여줍니다. `hue="species"` 덕분에 각 점이 Iris 품종에 따라 색깔이 다르게 표시되어, `sepal length`와 `sepal width` 조합으로 'setosa' 품종이 다른 두 품종과 명확히 구분되는 것을 확인할 수 있습니다.

**강의 맥락**
교수님은 `pair plot`을 "가장 중요하고, 무식하지만(brute force) 믿을 수 없을 정도로 효과적인 플롯"이라고 강조하며, 데이터 분석을 시작할 때 반드시 시도해봐야 한다고 설명합니다. 이는 각 셀이 플롯인 그리드 또는 행렬을 생성하는데, 대각선이 아닌 셀은 모든 가능한 특성 쌍 간의 관계를 보여주는 산점도이고, 대각선 셀은 해당 특성의 단변수 분포를 보여줍니다. 교수님은 `pair plot`을 통해 데이터의 군집을 찾고, 어떤 특성들이 레이블 데이터를 잘 분리하는지 빠르게 파악할 수 있다고 언급합니다. 특히 Iris 데이터셋의 `sepal length`와 `sepal width`가 데이터를 두 그룹으로 분류하는 데 좋은 조합임을 예시로 들었습니다.

**시험 포인트**
*   ⭐`pairplot`의 주요 기능 (모든 변수 쌍 간의 관계 및 각 변수의 단변수 분포 시각화)
*   ⭐`pairplot`을 데이터 분석의 어느 단계에서 활용하는 것이 가장 효과적인지
*   ⭐`hue` 매개변수가 `pairplot`에서 어떤 역할을 하는지 (범주형 변수에 따른 데이터 구분)
*   `diag_kind` 매개변수의 역할 및 가능한 값들 (예: `hist`, `kde`)
*   `corner=True` 옵션의 의미
*   산점도에서 `plot_kws`를 통해 점의 투명도(`alpha`)나 크기(`s`)를 조절하여 과밀도(over-plotting) 문제를 완화하는 방법

---

## Slide 17

---
### Clustermap — Definition & When to Use

**핵심 개념**
`Clustermap`은 일반적인 `heatmap`에 계층적 클러스터링(`hierarchical clustering`) 알고리즘을 적용하여 행(rows)과 열(columns)을 재정렬하는 시각화 기법입니다. 이를 통해 데이터 내에 숨겨진 블록 구조나 모듈을 발견하는 데 유용합니다.

**강의 맥락**
교수님께서는 `Clustermap`을 "더 똑똑한 히트맵(smarter heatmap)"이라고 설명하시며, 일반 히트맵이 단순히 숫자 행렬을 그리는 것과 달리 `Clustermap`은 먼저 행과 열 모두에 계층적 클러스터링 알고리즘을 실행하여 유사성을 기반으로 행과 열을 재정렬한다고 강조하셨습니다.
- **정의 (Definition)**: 계층적으로 클러스터링된 히트맵으로, 유사성을 기반으로 행과 열을 재정렬하여 숨겨진 블록 구조를 드러냅니다.
- **사용 시기 (Use when)**: 데이터 내에 숨겨진 블록이나 모듈이 있을 것으로 의심될 때 사용합니다. 함께 움직이는 특성 그룹(feature groups)이나 유사한 프로필을 가진 샘플 그룹(sample clusters)을 찾거나, 상관관계 블록(correlation blocks)을 탐색하는 데 탁월합니다.
- **읽는 방법 (How to read)**: 양쪽에 있는 나무 모양의 다이어그램인 덴드로그램(dendrogram)은 유사성을 나타냅니다. 대각선 상의 블록은 모듈을 시사합니다.
- **주의사항 (Pitfalls)**: 거리(distance)나 연결(linkage) 방식에 민감하며, 스케일이 다른 데이터를 혼합할 때는 표준화(standardize)하는 것이 좋습니다. 또한 너무 많은 레이블은 피해야 합니다.

**시험 포인트**
- ⭐ `Clustermap`이 일반 `heatmap`과 다른 점은 무엇이며, 어떤 용도로 사용되는지 이해해야 합니다. (계층적 클러스터링을 통한 재정렬, 숨겨진 블록/모듈 발견)
- ⭐ 덴드로그램이 무엇을 의미하는지 알아야 합니다.

---

## Slide 18

### ClusterMap — Code & Executed Example (Wine Correlations)

**핵심 개념**:
`ClusterMap`은 일반적인 히트맵(heatmap)과 달리 계층적 클러스터링(hierarchical clustering) 알고리즘을 사용하여 데이터의 행과 열을 유사성에 따라 재정렬한 후 시각화하는 도구입니다. 이를 통해 데이터 내에 숨겨진 블록이나 모듈, 즉 함께 움직이는 특징 그룹이나 유사한 프로필을 가진 샘플 그룹을 효과적으로 찾아낼 수 있습니다. 이 슬라이드에서는 Wine 데이터셋의 수치형 특징들 간의 상관관계(correlation)를 `ClusterMap`으로 시각화하는 예시를 보여줍니다.

**코드/수식 해설**:

```python
num = wine.drop(columns=["class", "target"], errors="ignore")
corr = num.corr()
sns.clustermap(
    corr, 
    center=0, 
    cmap="vlag", 
    linewidths=0.3, 
    method="average", 
    metric="euclidean"
)
```

1.  `num = wine.drop(columns=["class", "target"], errors="ignore")`: Wine 데이터프레임에서 "class"와 "target"과 같은 범주형 특징들을 제거하여 `num`이라는 새로운 데이터프레임을 생성합니다. 상관관계를 계산하기 위해서는 모든 특징이 수치형이어야 하기 때문입니다.
2.  `corr = num.corr()`: `num` 데이터프레임의 모든 수치형 특징들 간의 피어슨 상관계수(Pearson correlation coefficient)를 계산하여 상관 행렬(`corr`)을 생성합니다. 상관계수는 $-1$에서 $1$ 사이의 값을 가집니다.
3.  `sns.clustermap(...)`: `seaborn` 라이브러리의 `clustermap` 함수를 호출하여 상관 행렬을 시각화합니다.
    *   `corr`: 시각화할 상관 행렬 데이터입니다.
    *   `center=0`: 색상 척도의 중앙을 `0`에 맞춥니다. 이는 양의 상관관계와 음의 상관관계를 명확하게 구분하는 데 도움이 됩니다.
    *   `cmap="vlag"`: 색상 맵(colormap)을 지정합니다. "vlag"는 중앙 `0`을 기준으로 대칭적인 색상을 제공하여 상관관계의 방향성을 잘 보여줍니다.
    *   `linewidths=0.3`: 각 셀 사이의 경계선 두께를 설정합니다.
    *   `method="average"`: 계층적 클러스터링 시 링크age(linkage) 방법을 "average"로 설정합니다.
    *   `metric="euclidean"`: 클러스터링 시 유사성(거리)을 측정하는 방법을 "유클리드 거리(Euclidean distance)"로 설정합니다.

**구체적 예시**:
제공된 슬라이드의 하단 이미지에는 Wine 데이터셋의 여러 수치형 특징들(예: `ash`, `alcohol`, `proline` 등) 간의 상관관계가 `ClusterMap` 형태로 시각화되어 있습니다. 유사한 특징끼리 재정렬되어 블록을 형성하는 것을 볼 수 있습니다. 예를 들어, `flavanoids`, `total_phenols`, `od280/od315_of_diluted_wines`, `proanthocyanins`와 같은 특징들이 서로 강한 양의 상관관계를 보여 하나의 그룹을 형성하는 경향이 있습니다.

**강의 맥락**:
교수님은 `ClusterMap`이 일반적인 히트맵(heatmap)과는 다르다고 강조하셨습니다. 일반 히트맵은 단순히 숫자의 매트릭스를 그대로 플로팅하지만, `ClusterMap`은 먼저 행과 열 모두에 계층적 클러스터링 알고리즘을 실행하여 유사성을 기반으로 재정렬한다고 설명하셨습니다. 이를 통해 유사한 열과 행이 서로 옆에 배치됩니다. 교수님은 데이터 내에 숨겨진 블록이나 모듈을 찾을 때, 또는 함께 움직이는 특징 그룹이나 유사한 프로필을 가진 샘플 그룹을 찾을 때 `ClusterMap`이 매우 유용하다고 강조했습니다. 그래프 측면에 있는 트리 형태의 다이어그램(덴드로그램)이 유사성을 보여준다고 언급하셨지만, 현재 슬라이드의 예시에서는 덴드로그램이 명시적으로 그려져 있지 않다고 덧붙이셨습니다. 이 코드에서는 범주형 특징을 제외한 수치형 특징들만을 사용하여 상관 행렬을 계산한 다음, `clustermap` 함수를 통해 시각화하여 재정렬된 특징들 간의 상관관계를 파악하고 있습니다.

**시험 포인트**:
*   ⭐`ClusterMap`과 일반 `Heatmap`의 차이점 (계층적 클러스터링을 통한 행/열 재정렬)을 설명할 수 있어야 합니다.
*   ⭐`ClusterMap`을 사용하는 주된 목적 (숨겨진 블록/모듈, 특징 그룹, 샘플 프로필 찾기)을 알아야 합니다.
*   상관관계를 계산하고 `ClusterMap`을 그리기 전에 **범주형 특징을 제거**해야 하는 이유를 이해해야 합니다.
*   ⭐상관관계는 선형 관계만을 보여준다는 점을 기억해야 합니다.

---

## Slide 19

**핵심 개념**
Hexbin 및 2D Histogram은 산점도(scatterplot)에서 데이터 포인트가 너무 많아 겹쳐 보이는 과밀화(over-plotting) 문제를 해결하기 위한 시각화 기법입니다. $x,y$ 평면을 육각형(hexbin) 또는 사각형(2D histogram) 형태의 빈(bin)으로 나누고, 각 빈에 포함된 데이터 포인트의 개수를 색상 강도로 인코딩하여 데이터 분포의 밀도를 시각화합니다.

**코드/수식 해설**
해당 슬라이드에는 직접적인 코드나 수식은 포함되어 있지 않습니다.

**구체적 예시**
(현재 슬라이드에 예시 이미지가 없으므로 생략)

**강의 맥락**
교수님께서는 이 시각화 기법에 대해 "만약 산점도를 사용하는데 과밀화 문제가 발생한다면, 예를 들어 10만 개의 포인트가 있다면, 개별 점을 그리는 대신 2D 비닝(beaming)을 사용할 수 있다. 이것이 2D 히스토그램이다."라고 설명하며, $x,y$ 평면을 육각형 또는 사각형 그리드 빈으로 나누어 각 빈에 떨어지는 점의 수를 세고 색상 강도로 그 수를 표현한다고 강조합니다. 이는 매우 밀도 높은 산점도에 대한 직접적인 해결책이며, 효과적으로 2D 밀도 맵을 생성하여 데이터의 분포를 파악할 수 있게 해줍니다.

**시험 포인트**
*   ⭐ **Hexbin 및 2D Histogram의 주된 사용 목적**: 과밀화된 산점도(dense scatter clouds)에서 데이터의 2D 밀도 분포를 확인하기 위함입니다. 즉, "over-plotting" 문제를 해결하고 "2D density map"을 생성하는 것이 핵심입니다.
*   ⭐ **정보 인코딩 방식**: 각 빈에 들어있는 점의 `count`를 `color intensity`로 표현합니다. "Hotspots" (가장 어둡거나 강렬한 색상의 빈)는 빈번한 조합을 나타냅니다.
*   ⭐ **Pitfalls (주의사항)**: `bin size` (또는 `grid size`)가 시각화 결과와 인식에 큰 영향을 미치므로, 적절한 빈 크기를 선택하는 것이 중요합니다. 빈이 너무 크면 세부 정보를 잃고, 너무 작으면 플롯이 듬성듬성하고 노이즈처럼 보일 수 있습니다.

---

## Slide 20

**핵심 개념**
Hexbin plot과 2D Histogram은 대규모 데이터셋에서 발생하는 산점도(scatterplot)의 **오버플로팅(over-plotting)** 문제를 해결하기 위한 시각화 기법입니다. 이는 $xy$-평면을 육각형(hexbin) 또는 사각형(2D Histogram) 격자로 나누고, 각 격자(bin)에 포함된 데이터 포인트의 개수를 세어 색상의 강도로 표현하여 데이터 밀도를 시각화합니다.
-   **Hexbin Plot**: 육각형 격자를 사용하여 데이터를 집계하고 밀도를 표현합니다.
-   **2D Histogram**: 사각형 격자를 사용하여 데이터를 집계하고 밀도를 표현합니다.

이를 통해 개별 포인트를 그리는 대신 데이터의 2D 밀도 맵을 효과적으로 생성하여 "핫 스팟"(가장 밀도가 높은 영역)을 쉽게 식별할 수 있습니다.

**코드/수식 해설**
Seaborn 라이브러리의 `sns.jointplot` 함수를 사용하여 구현합니다. `kind` 매개변수를 통해 Hexbin 또는 2D Histogram을 지정할 수 있습니다.

```python
# Hexbin plot 예시
sns.jointplot(data=wine, x="alcohol", y="malic_acid", kind="hex")

# 2D Histogram 예시
sns.jointplot(data=diabetes, x="bmi", y="target", kind="hist")
```
-   `data`: 시각화할 데이터프레임.
-   `x`, `y`: $x$축과 $y$축에 매핑할 숫자형 변수.
-   `kind`: 플롯의 종류를 지정합니다.
    -   `"hex"`: Hexbin plot을 생성합니다.
    -   `"hist"`: 2D Histogram을 생성합니다.

**구체적 예시**
-   **Wine 데이터셋**: `alcohol`과 `malic_acid` 변수 간의 관계를 Hexbin plot(`kind="hex"`)으로 시각화한 결과, 특정 `alcohol` 및 `malic_acid` 범위에서 데이터 밀도가 높은(노란색에 가까운) "핫 스팟"이 나타남을 확인할 수 있습니다.
-   **Diabetes 데이터셋**: `bmi`와 `target` 변수 간의 관계를 2D Histogram(`kind="hist"`)으로 시각화한 결과, 역시 특정 `bmi` 및 `target` 범위에서 데이터 밀도가 높은 영역을 색상 강도로 보여줍니다.

**강의 맥락**
교수님은 Hexbin plot과 2D Histogram이 산점도에서 10만 개 이상의 포인트와 같이 데이터가 매우 밀집되어 **오버플로팅이 발생하는 문제**에 대한 직접적인 해결책임을 강조했습니다. 개별 점을 그리는 대신 $xy$-평면을 육각형 또는 사각형 빈으로 분할하고, 각 빈에 속하는 점의 개수를 세어 색상 강도로 표현함으로써 **2D 밀도 맵을 효과적으로 생성**한다고 설명했습니다. 이를 통해 가장 어둡거나 강렬하게 색칠된 빈인 "핫 스팟"을 찾을 수 있습니다. 특히, **빈(bin) 크기 또는 격자(grid) 크기**가 매우 중요하다고 강조하며, 너무 크면 세부 정보를 잃고, 너무 작으면 플롯이 희박하고 노이즈처럼 보일 수 있으므로 적절한 크기를 선택해야 한다고 언급했습니다. 이 플롯을 만들기 위해서는 `sns.jointplot` 함수를 사용하고 `kind` 인자를 `"hex"` 또는 `"hist"`로 설정해야 한다고 설명했습니다.

**시험 포인트**
-   ⭐ 대량 데이터셋에서 산점도의 **오버플로팅 문제를 해결**하기 위한 시각화 기법으로 Hexbin plot과 2D Histogram을 사용하는 이유를 설명할 수 있어야 합니다.
-   ⭐ 이 두 플롯의 작동 방식($xy$-평면을 격자로 나누고, 각 격자 내 데이터 포인트 수를 색상 강도로 표현)을 이해해야 합니다.
-   ⭐ `sns.jointplot` 함수와 `kind="hex"`, `kind="hist"` 매개변수를 사용하여 Hexbin plot과 2D Histogram을 생성하는 방법을 알아야 합니다.
-   ⭐ **빈(bin) 크기 또는 격자(grid) 크기**가 플롯의 해석에 미치는 영향(너무 크거나 작을 때의 문제점)을 설명할 수 있어야 합니다.

---

## Slide 21

---

### 2D KDE — Definition & When to Use

**핵심 개념**:
2D Kernel Density Estimate (KDE)는 두 개의 수치형 변수에 대한 확률 밀도 함수를 추정하여 데이터의 부드러운 밀도 구조를 시각화하는 기법입니다. 개별 데이터 포인트 위에 작은 2D 가우시안 커브(bell curve)를 배치하고, 이들을 합산하여 연속적인 확률 밀도 표면을 만듭니다. 이는 데이터 분포의 모드(peaks)나 능선(ridges), 등고선(contours)을 파악하는 데 유용합니다.

**코드/수식 해설**:
2D KDE의 수학적 정의는 다음과 같습니다.
$$ \hat{f}(x, y) = \frac{1}{nh_x h_y} \sum K_x(\cdot) K_y(\cdot) $$
여기서,
*   $n$은 데이터 포인트의 개수입니다.
*   $h_x, h_y$는 각각 $x$축과 $y$축에 대한 대역폭(bandwidth)입니다.
*   $K_x(\cdot), K_y(\cdot)$는 각 차원에 대한 커널 함수(예: 가우시안 커널)입니다.
*   $\sum K_x(\cdot) K_y(\cdot)$는 각 데이터 포인트에 대한 커널 값의 합산을 나타냅니다.

**구체적 예시**:
Seaborn 라이브러리에서 `sns.jointplot()` 함수를 사용하여 2D KDE 플롯을 생성할 수 있습니다. `kind='kde'` 옵션을 설정하여 2D KDE를 시각화합니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# iris 데이터셋을 예시로 사용
iris = sns.load_dataset("iris")

# 'petal_length'와 'petal_width'에 대한 2D KDE 플롯 생성
sns.jointplot(x="petal_length", y="petal_width", data=iris, kind="kde")
plt.show()
```

이 플롯에서 중앙의 등고선은 2D 밀도 등고선을 보여줍니다. 등고선이 밀집된 영역은 데이터 밀도가 높음을, 등고선이 성긴 영역은 밀도가 낮음을 의미합니다.

**강의 맥락**:
교수님께서는 "2D KDE는 유니베리엇 KDE의 정의가 2D로 일반화된 것"이라고 설명하며, 각 개별 점 위에 2D 가우시안 커브를 올려놓고 합산하여 부드럽고 연속적인 밀도 표면을 만든다고 강조하셨습니다.
*   **사용 시점**: "데이터의 부드러운 밀도 구조나 연속적인 뷰, 특히 모드(peaks)나 등고선(contours)을 식별하고 싶을 때 사용"합니다.
*   **해석 방법**: 등고선 봉우리(peaks)는 높은 밀도를 나타내며, 등고선 간격은 밀도의 경사(gradient)를 반영합니다.
*   **주의사항**: 유니베리엇 KDE와 마찬가지로 대역폭(bandwidth)이 매우 중요하며, `bw_adjust` 속성을 사용하여 조정할 수 있습니다.
*   **구현**: `jointplot` 함수에서 `kind='kde'`를 설정하여 그릴 수 있습니다.

**시험 포인트**:
*   ⭐2D KDE가 무엇인지 정의하고, 어떤 목적으로 사용하는지 (`smooth density structure`, `modes`, `ridges`) 설명할 수 있어야 합니다.
*   ⭐2D KDE의 핵심 매개변수 중 하나인 `bandwidth`의 중요성과 조절 방법(`bw_adjust`)을 알아야 합니다.
*   ⭐2D KDE 플롯의 등고선을 어떻게 해석하는지 (`contour peaks = high density`, `spacing reflects gradient`) 이해해야 합니다.
*   ⭐Seaborn에서 2D KDE를 그리는 데 사용되는 함수와 `kind` 옵션 (`sns.jointplot(..., kind="kde")`)을 숙지해야 합니다.

---

## Slide 22

### 2D KDE — Code & Executed Example

**핵심 개념**:
2D Kernel Density Estimate (KDE)는 두 개의 연속형 수치형 변수에 대한 결합 확률 밀도 함수를 시각화하는 방법입니다. 각 데이터 포인트 위에 작은 2차원 종 모양 커브(예: 2D 가우시안 커브)를 배치하고, 이 커브들을 모두 합산하여 데이터의 부드럽고 연속적인 밀도 표면을 생성합니다. 이 표면은 추정된 확률 밀도를 나타내며, 데이터 분포의 모드(최고점)나 윤곽(contour)을 식별하는 데 유용합니다.

**코드/수식 해설**:
2D KDE 플롯은 Seaborn의 `sns.jointplot()` 함수를 사용하여 그릴 수 있습니다. `kind` 파라미터를 `"kde"`로 설정하여 2D KDE 플롯을 생성합니다.

```python
sns.jointplot(data=iris,
              x="sepal length (cm)",
              y="sepal width (cm)",
              kind="kde")
```
*   `data`: 플롯을 그릴 데이터프레임 (`iris` 데이터셋).
*   `x`: x축에 매핑할 컬럼 (`"sepal length (cm)"`).
*   `y`: y축에 매핑할 컬럼 (`"sepal width (cm)"`).
*   `kind="kde"`: 중앙 플롯을 2D KDE 컨투어 플롯으로 지정합니다.

**구체적 예시**:
아이리스 데이터셋에서 `sepal length (cm)`와 `sepal width (cm)` 두 변수 간의 2D 밀도 분포를 2D KDE 컨투어 플롯으로 시각화한 결과입니다. 플롯의 중앙 부분에 2D 밀도 윤곽선이 표시되며, 윤곽선이 밀집된 부분이 데이터 포인트가 밀집된 고밀도 영역, 즉 모드를 나타냅니다. 예를 들어, `sepal length` 약 5.7cm, `sepal width` 약 2.7cm 부근에서 한 주요 모드(피크)를 확인할 수 있습니다.

**강의 맥락**:
교수님은 2D KDE에 대해 "KDE 메소드는 각 개별 포인트 위에 2D 종 모양 커브, 2D 가우시안 커브와 같은 작은 컬러를 배치한 다음, 그 모든 커브를 합산하여 부드럽고 연속적인 표면을 만듭니다. 이 표면은 추정된 확률 밀도를 나타냅니다."라고 설명하며, 데이터의 "부드러운 밀도 구조나 연속적인 뷰"를 원할 때 사용하고 "모드(피크) 또는 밀도의 윤곽을 식별"하는 데 특히 유용하다고 강조했습니다. 또한 "유니베리엇(단변수) KDE와 마찬가지로, 대역폭(`bandwidth`)이 매우 중요하며, `BW-adjust` 속성을 사용하여 조정할 수 있습니다."라고 언급했습니다. 코드 사용법에 대해서는 "`jointplot`을 사용해야 합니다. `kind`를 `KDE`로 설정하여" 만든다고 설명했습니다.

**시험 포인트**:
*   ⭐ 2D KDE가 무엇을 시각화하는지 (두 변수 간의 **결합 확률 밀도**, **부드러운 밀도 구조**, **모드/피크/컨투어**).
*   ⭐ 2D KDE 플롯을 생성하기 위해 `sns.jointplot()`에서 `kind` 파라미터를 어떻게 설정해야 하는지 (`kind="kde"`).
*   ⭐ 2D KDE에서 **대역폭(bandwidth)**의 중요성 및 조절 파라미터 (`BW-adjust`).

---

## Slide 23

**핵심 개념**:
버블 차트(Bubble Chart)는 기본적으로 산점도(scatterplot)의 한 종류로, 두 개의 수치형 변수를 $x, y$ 축에 매핑하고, 세 번째 수치형 변수를 각 마커(점)의 크기($size$)로 인코딩하여 표현한다. 선택적으로 범주형 변수를 `hue`(색상)로 매핑하여 그룹을 시각화할 수도 있다.

**언제 사용하는가**: 두 수치형 변수 간의 관계($X-Y$ 관계)를 탐색하면서 동시에 각 데이터 포인트의 세 번째 수치형 변수(크기)의 크기를 비교하고자 할 때 유용하다.

**해석 방법**:
*   점의 위치 $$(x, y)$$는 두 변수의 값을 나타낸다.
*   점의 크기는 세 번째 수치형 변수의 값을 나타낸다.
*   점의 색상(선택 사항)은 데이터의 그룹을 나타낸다.

**주의사항**:
*   인간의 면적 지각은 비선형적이므로, 크기 변화를 정확하게 인지하기 어려울 수 있다.
*   차트 해석의 정확성을 위해 반드시 범례(legend)를 포함해야 한다.
*   마커 크기 범위가 너무 커지지 않도록 조절하여 혼란을 방지해야 한다.

**강의 맥락**:
교수님은 버블 차트를 "특별한 산점도(special scatterplot)"로 정의하며, 마커의 크기($size$)가 세 번째 수치형 변수(third numerical variable)에 매핑된다는 점을 강조했습니다. 예를 들어, `hue` 대신 `size`를 사용하여 `pruroline`과 같은 수치형 변수를 마커 크기에 연결할 수 있다고 설명했습니다. 이를 통해 두 변수 간의 관계를 보면서 각 점들의 '크기'를 비교할 수 있다고 언급했습니다.

**시험 포인트**:
*   ⭐ 버블 차트가 일반 산점도와 다른 점은 **세 번째 수치형 변수를 마커의 크기로 인코딩**한다는 것이다.
*   ⭐ 버블 차트의 사용 목적은 **두 변수 간의 관계와 함께 각 데이터 포인트의 크기(magnitude)를 비교**하는 것이다.
*   ⭐ 버블 차트 사용 시 **인간의 면적 지각이 비선형적**이라는 점을 인지하고, **범례 포함 및 적절한 크기 범위 설정**에 주의해야 한다.

---

## Slide 24

### 핵심 개념
버블 차트(Bubble Chart)는 기본적인 산점도(scatterplot)를 확장하여 세 번째 **수치형 변수**를 시각화하는 방법입니다. 각 점의 크기를 이 세 번째 수치형 변수에 매핑하여, 두 개의 주요 변수($x, y$) 간의 관계뿐만 아니라 세 번째 변수의 영향까지 한 번에 파악할 수 있게 합니다.

### 코드/수식 해설
`seaborn.scatterplot` 함수를 사용하여 버블 차트를 생성합니다.
```python
sns.scatterplot(data=wine, x="alcohol", y="malic_acid",
                size="proline", hue="class", alpha=0.6)
```
*   `data=wine`: `wine` 데이터프레임을 사용합니다.
*   `x="alcohol"`: `alcohol` 변수를 x축에 매핑합니다.
*   `y="malic_acid"`: `malic_acid` 변수를 y축에 매핑합니다.
*   `size="proline"`: `proline` 변수를 각 마커의 크기에 매핑합니다. 이 파라미터가 버블 차트를 만드는 핵심입니다. `proline` 값이 클수록 마커 크기가 커집니다.
*   `hue="class"`: `class` 변수에 따라 각 마커의 색상을 다르게 지정하여, 추가적인 범주형 정보를 시각화합니다.
*   `alpha=0.6`: 마커의 투명도를 0.6으로 설정하여 겹침(over-plotting) 문제를 완화하고 밀집도를 파악하는 데 도움을 줍니다.

### 구체적 예시
제공된 슬라이드의 예시는 `wine` 데이터셋을 사용하여 알코올($x$축)과 말산($y$축)의 관계를 보여주면서, 각 와인의 프롤린 함량(`proline`)에 따라 점의 크기를 조절합니다. 또한, 와인의 종류(`class`)에 따라 색상을 다르게 표시하여 세 가지 다른 종류의 와인에 대한 알코올, 말산, 프롤린 함량의 복합적인 관계를 한눈에 파악할 수 있습니다.

### 강의 맥락
교수님은 버블 차트를 "특별한 산점도"라고 정의하며, "마커의 크기가 세 번째 수치형 변수에 매핑된다"는 점을 강조하셨습니다. 슬라이드 코드에서 `proline`이라는 수치형 변수가 `size` 파라미터에 할당되어, `proline` 값이 클수록 마커의 크기가 커지는 방식으로 시각화되는 것을 설명하며, 이를 통해 다변량 데이터를 간단한 산점도로도 다룰 수 있음을 보여주었습니다.

### 시험 포인트
*   ⭐ **버블 차트의 정의**: 일반 산점도에 세 번째 **수치형 변수**를 마커의 크기로 인코딩하여 시각화하는 차트.
*   ⭐ `seaborn.scatterplot`에서 버블 차트를 생성할 때 사용하는 주요 파라미터는 무엇이며, 어떤 역할을 하는지 설명할 수 있어야 합니다. (정답: `size` 파라미터가 수치형 변수를 마커 크기에 매핑)
*   `hue` 파라미터와 `size` 파라미터의 역할 차이를 이해해야 합니다. (`hue`는 범주형 변수를 색상으로, `size`는 수치형 변수를 크기로 인코딩)

---

## Slide 25

**핵심 개념**:
박스 플롯(Box Plot)은 데이터 분포의 주요 통계량(중앙값, 사분위수, 이상치)을 시각화하여 보여주는 그래프입니다. 단일 변수의 분포를 요약하는 데 사용되지만, 범주형 변수를 `x`축에, 수치형 변수를 `y`축에 배치하여 그룹별 분포를 비교하는 이변량 시각화에도 매우 유용합니다.

**코드/수식 해설**:
*   **중앙값($Median$)**: 박스 내부의 선으로 표시됩니다.
*   **박스($Box$)**: 1사분위수($Q_1$)부터 3사분위수($Q_3$)까지의 범위를 나타내며, 박스의 길이는 사분위수 범위($IQR = Q_3 - Q_1$)입니다. 이는 데이터의 중간 50%가 분포하는 범위를 보여줍니다.
*   **수염($Whiskers$)**: 박스에서 뻗어 나오는 선으로, 일반적으로 $Q_1 - 1.5 \times IQR$부터 $Q_3 + 1.5 \times IQR$까지의 데이터를 포함합니다. (단, 데이터가 이 범위 안에 없으면 최솟값/최댓값까지)
*   **이상치($Outliers$)**: 수염 범위를 벗어나는 개별 데이터 포인트들입니다.

**구체적 예시**:
강의에서는 와인 데이터셋에서 알코올 함량(`alcohol`, 수치형) 분포를 와인의 `class`(범주형)별로 박스 플롯을 사용하여 비교하는 예시를 언급했습니다. 각 와인 클래스에 대해 알코올 함량의 중앙값, 분포의 퍼짐, 그리고 이상치를 한눈에 파악할 수 있습니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 (실제 강의에서 언급된 와인 데이터셋의 구조를 가정)
# wine_df = pd.read_csv('wine_dataset.csv')
# 예시를 위한 가상의 데이터 생성
data = {
    'class': ['Class_0', 'Class_0', 'Class_0', 'Class_1', 'Class_1', 'Class_1', 'Class_2', 'Class_2', 'Class_2', 'Class_0'],
    'alcohol': [13.5, 12.8, 14.2, 12.0, 11.5, 12.5, 13.0, 13.8, 14.5, 10.0] # 10.0은 이상치 예시
}
wine_df_example = pd.DataFrame(data)

# Seaborn을 사용한 박스 플롯
plt.figure(figsize=(8, 6))
sns.boxplot(x='class', y='alcohol', data=wine_df_example)
plt.title('Alcohol Distribution by Wine Class')
plt.xlabel('Wine Class')
plt.ylabel('Alcohol Content')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

**강의 맥락**:
교수님은 박스 플롯이 원래 단변량 데이터에 사용되지만, "이변량 데이터에도 사용될 수 있다"고 강조하며, 특히 '범주형 변수(`x`축)'와 '수치형 변수(`y`축)'의 조합을 통해 여러 그룹의 분포를 비교할 때 유용하다고 설명했습니다. "첫 번째 축은 `class`이고, 두 번째 축은 수치 속성입니다. 따라서 각 클래스에 대해 박스 플롯을 가집니다."라고 언급하며, `x`축에 와인 `class`를, `y`축에 `alcohol`을 설정하여 각 클래스별 알코올 분포를 시각화하는 예시를 들었습니다. 이는 그룹별 알코올 함량의 중앙값, 퍼짐, 이상치를 한눈에 파악하는 데 효과적입니다.

**시험 포인트**:
*   ⭐ 박스 플롯의 핵심 구성 요소인 중앙값, 박스($IQR$), 수염($1.5 \times IQR$), 이상치의 의미와 계산 방법을 이해해야 합니다.
*   ⭐ 박스 플롯이 '강력한 그룹 간 위치 및 퍼짐 비교'를 위해 사용된다는 점을 기억해야 합니다. (예: 범주형 변수와 수치형 변수 간의 관계 시각화)
*   ⭐ 박스 플롯의 한계점 중 하나로 '데이터의 다봉성(multimodality)을 숨길 수 있다'는 점을 알아두세요.

---

## Slide 26

**핵심 개념**
이 슬라이드는 Seaborn의 `boxplot`을 사용하여 범주형 변수(`class`)에 따른 수치형 변수(`alcohol`)의 분포를 시각화하는 방법을 설명합니다. 이는 단일 수치형 변수의 분포를 보는 유니베리엇(univariate) 분석을 넘어, 범주별로 수치형 변수의 분포를 비교하는 바이베리엇(bivariate) 분석에 해당합니다. 박스 플롯은 각 범주에 대한 데이터의 중앙값, 사분위수, 이상치 등을 한눈에 파악할 수 있게 해줍니다.

**코드/수식 해설**

```python
sns.boxplot(data=wine, x="class", y="alcohol",
            showfliers=True, whis=1.5)
```

*   `sns.boxplot()`: Seaborn 라이브러리의 박스 플롯 함수를 호출합니다.
*   `data=wine`: `wine` DataFrame을 데이터 소스로 지정합니다.
*   `x="class"`: x축에 범주형 변수인 'class'를 할당합니다. 이 변수의 각 고유값(class\_0, class\_1, class\_2)에 대해 별도의 박스 플롯이 그려집니다.
*   `y="alcohol"`: y축에 수치형 변수인 'alcohol'을 할당합니다. 각 클래스별 알코올 함량 분포를 나타냅니다.
*   `showfliers=True`: 이상치(outliers)를 점으로 표시합니다. 기본값은 `True`입니다.
*   `whis=1.5`: 박스 플롯의 수염(whisker) 길이를 설정합니다. 기본적으로 사분위범위(IQR)의 $1.5$배 내에 있는 데이터를 수염으로 표현합니다.

**구체적 예시**
제공된 박스 플롯은 `wine` 데이터셋에서 `class` 변수(class\_0, class\_1, class\_2)에 따른 `alcohol` 함량의 분포를 보여줍니다. 예를 들어, `class_0`은 가장 높은 알코올 함량을 가지며 분포의 범위도 넓은 편임을 알 수 있고, `class_1`은 가장 낮은 평균 알코올 함량과 함께 여러 이상치(outliers)를 보여줍니다.

**강의 맥락**
교수님은 박스 플롯이 원래 유니베리엇 데이터에 사용되지만, 여기서는 바이베리엇 데이터(하나의 수치형 변수와 하나의 범주형 변수)를 비교하는 데 사용된다고 강조합니다. 특히 "첫 번째 축은 `class`라는 속성이고, 두 번째 속성은 수치형 속성입니다. 그래서 각 클래스에 대해 박스 플롯이 하나씩 그려집니다."라고 설명하며, `x`축은 범주형 `class`를, `y`축은 수치형 `alcohol`을 나타낸다고 명확히 언급합니다. 이는 각 클래스별 알코올 함량 분포를 시각화하는 목적을 설명합니다.

**시험 포인트**
*   ⭐ **`sns.boxplot()` 함수를 사용하여 범주형 변수에 따른 수치형 변수의 분포를 시각화하는 방법**
*   ⭐ `x`와 `y` 파라미터에 어떤 종류의 변수(범주형/수치형)가 할당되어야 하는지 이해하기
*   ⭐ 박스 플롯의 각 구성 요소(중앙값, 사분위수, 수염, 이상치)가 무엇을 의미하는지 해석할 수 있어야 합니다.

---

## Slide 27

## Violin — Definition & When to Use

### 핵심 개념
바이올린 플롯은 수치형 데이터의 분포를 그룹별로 비교하는 데 사용되는 시각화 도구입니다. 커널 밀도 추정(KDE)을 기반으로 한 분포의 윤곽을 중앙선을 기준으로 대칭으로 보여주며, 내부에는 사분위수나 중앙값을 표시하여 분포의 주요 통계치를 함께 제공합니다.

### 코드/수식 해설
바이올린 플롯 자체는 수식이 필요하지 않지만, 그 너비는 데이터 밀도($\text{density}$)에 비례($\text{width} \propto \text{density}$)합니다. 즉, 너비가 넓은 구간은 데이터 포인트가 밀집해 있음을 의미합니다.

### 구체적 예시
와인 데이터셋에서 각 클래스(`class`)별 알코올 함량(`alcohol`) 분포를 바이올린 플롯으로 시각화할 수 있습니다.
```python
import seaborn as sns
import matplotlib.pyplot as plt

# wine_df는 와인 데이터셋을 담고 있는 pandas DataFrame이라고 가정
# sns.violinplot(x="class", y="alcohol", data=wine_df)
# plt.show()
```
이 플롯은 `class`와 같은 범주형 변수를 x축에, `alcohol`과 같은 수치형 변수를 y축에 매핑하여 각 클래스별 알코올 분포의 모양(비대칭성, 꼬리, 다봉성)을 상세히 보여줍니다.

### 강의 맥락
교수님은 여러 분포를 비교하는 맥락에서 바이올린 플롯을 설명하셨습니다. 박스 플롯과 마찬가지로 "하나의 수치형 변수와 하나의 범주형 변수를 가지고 비교할 때" 사용하며, 특히 "X축이 범주형 값(예: 클래스 이름 또는 ID)이고, Y축이 어떤 수치형 속성을 나타낼 때" 사용한다고 강조하셨습니다. 박스 플롯과 함께 범주형 값에 따른 수치형 값의 분포를 시각화하는 강력한 방법으로 소개되었습니다.

### 시험 포인트
*   ⭐ **바이올린 플롯의 정의:** KDE 윤곽이 중앙을 중심으로 대칭을 이루며, 내부에는 사분위수 또는 중앙값이 표시되는 플롯.
*   ⭐ **사용 시기:** 그룹별로 데이터의 분포 형태(비대칭성, 꼬리, 다봉성)를 시각적으로 보여줄 때 유용합니다. 특히 박스 플롯보다 더 상세한 분포의 밀도 정보를 제공합니다.
*   ⭐ **해석 방법:** 플롯의 너비는 데이터 밀도에 비례합니다. 즉, 너비가 넓은 구간은 데이터가 많이 집중되어 있음을 나타냅니다.
*   ⭐ **주의 사항:** 대역폭(bandwidth) 선택이 중요하며, 샘플 수가 작은($n$) 경우 플롯의 작은 돌출부를 과도하게 해석하지 않도록 주의해야 합니다.

---

## Slide 28

**핵심 개념**
바이올린 플롯(Violin Plot)은 범주형 변수와 수치형 변수 간의 관계를 시각화할 때 사용됩니다. 각 범주에 대한 수치형 변수의 분포 형태(확률 밀도)를 바이올린 모양으로 보여주며, 이는 박스 플롯에 커널 밀도 추정(KDE)을 결합하여 데이터의 밀도와 분포 범위를 함께 파악할 수 있게 합니다.

**코드/수식 해설**

```python
sns.violinplot(data=wine, x="class", y="flavanoids",
               inner="quartile", cut=0, bw_adjust=1.0)
```
*   `data=wine`: `wine` 데이터셋을 사용합니다.
*   `x="class"`: X축에는 범주형 변수인 'class'를 매핑합니다. 이는 `class_0`, `class_1`, `class_2` 세 가지 그룹으로 나뉩니다.
*   `y="flavanoids"`: Y축에는 수치형 변수인 'flavanoids'를 매핑하여 각 클래스별 'flavanoids' 값의 분포를 시각화합니다.
*   `inner="quartile"`: 바이올린 내부에는 박스 플롯처럼 중앙값(median)과 사분위수(quartiles, Q1, Q3)를 표시합니다.
*   `cut=0`: KDE 곡선이 데이터의 실제 범위 밖으로 확장되지 않도록 잘라냅니다.
*   `bw_adjust=1.0`: 커널 밀도 추정(KDE)에 사용되는 대역폭(bandwidth)을 조절합니다. 기본값 1.0은 Seaborn의 기본 대역폭 추정치를 사용합니다.

**구체적 예시**
`wine` 데이터셋에서 각 와인 클래스(`class_0`, `class_1`, `class_2`)에 따른 'flavanoids' 함량 분포를 바이올린 플롯으로 보여줍니다. 각 클래스에 해당하는 바이올린 모양은 'flavanoids' 값의 밀도 함수를 나타내며, 바이올린의 폭이 넓을수록 해당 구간에 데이터 포인트가 밀집되어 있음을 의미합니다. 내부에 표시된 사분위수(세 개의 가로선)를 통해 중앙값 및 Q1, Q3 값을 직관적으로 파악할 수 있습니다. 예를 들어, `class_1`은 다른 클래스에 비해 'flavanoids' 함량이 전반적으로 높고 분포 범위가 넓은 것을 알 수 있습니다.

**강의 맥락**
교수님께서는 바이올린 플롯이 단일 변수(univariate) 데이터에 사용되지만, 이 슬라이드처럼 범주형 변수($X$축)와 수치형 변수($Y$축)를 함께 사용하여 여러 그룹 간의 분포를 비교할 때 이변량(bivariate) 데이터 시각화 도구로 활용될 수 있음을 강조하셨습니다. 특히 "X축은 범주형 값(클래스 이름 또는 ID)이고 Y축은 일부 수치형 속성을 나타낸다"고 설명하시며 현재 슬라이드의 예시와 같이 각 클래스별 `flavanoids`와 같은 수치형 속성의 분포를 비교하는 데 적합하다고 하셨습니다.

**시험 포인트**
*   ⭐ 바이올린 플롯은 범주형 변수와 수치형 변수 간의 관계를 시각화할 때 유용하며, 특히 각 범주 내 수치형 변수의 **밀도 분포 형태**를 보여주는 데 강점이 있습니다.
*   ⭐ 박스 플롯과 달리 바이올린 플롯은 **데이터 밀도** 정보를 제공하여 분포의 모양(예: 다봉성 분포)을 더 잘 이해할 수 있도록 돕습니다.
*   ⭐ `inner` 매개변수를 통해 바이올린 내부의 표시 방식을 제어할 수 있으며, `inner="quartile"`은 중앙값과 사분위수를 표시합니다.

---

## Slide 29

**핵심 개념**
Boxen plot(Box-and-whisker plot의 변형으로 'Letter-Value Box Plot'이라고도 함)은 대규모 데이터($n$이 큰 경우)의 분포를 시각화하는 데 사용되는 그래프입니다. 특히 데이터의 꼬리(tails) 부분에 많은 관측치가 있을 때, 이 부분을 더 깊이 있게 강조하여 보여줍니다. 기존 Box plot이 사분위수(quartiles)만 나타내는 반면, Boxen plot은 더 많은 'letter-value' 양분위수(quantiles)를 시각화하여 데이터의 중앙뿐만 아니라 꼬리 부분의 밀도와 분포를 더 자세히 파악할 수 있게 합니다.

*   **정의**: 대규모 데이터($n$)를 위한 더 깊고 대칭적인 양분위수 박스(letter-value boxes)를 제공합니다.
*   **사용 시점**: 관측치가 많은 꼬리 부분을 강조하여 보여줄 필요가 있을 때 유용합니다.
*   **해석 방법**: 쌓여있는 박스들은 더 깊은 양분위수를 보여주며, 중앙선은 중앙값(median)을 나타냅니다.
*   **주의사항**: 충분한 데이터($n$)가 필요하며, 적절한 `k_depth`를 선택해야 합니다. `k_depth`는 양분위수를 계산하는 깊이를 조절하는 파라미터입니다.

**강의 맥락**
교수님께서는 Boxen plot을 Box plot, Violin plot과 함께 여러 분포를 비교하는 도구로 언급하셨습니다. Box plot이 단일 변수 데이터에도 사용되지만, 범주형 변수와 수치형 변수가 함께 있을 때 각 범주별 수치형 변수의 분포를 비교하는 데 활용될 수 있음을 설명하며, Boxen plot도 이와 유사하게 활용될 수 있음을 시사하셨습니다. 즉, `X`축에 범주형 변수를, `Y`축에 수치형 변수를 매핑하여 각 범주에 대한 수치형 변수의 분포를 Boxen plot으로 나타낼 수 있습니다.

**시험 포인트**
*   ⭐ **Boxen plot의 목적**: 기존 Box plot과 비교하여, Boxen plot이 대규모 데이터에서 어떤 특징(특히 꼬리 부분의 분포)을 더 잘 보여주는지 이해해야 합니다.
*   ⭐ **Letter-value boxes**: Boxen plot의 핵심적인 특징인 'letter-value boxes'가 무엇을 의미하며, 이것이 데이터의 어떤 측면을 나타내는지 알고 있어야 합니다.

---

## Slide 30

## Boxen — Code Example

### 핵심 개념
`Boxenplot` (Box-and-whisker plot의 변형인 letter-value plot)은 범주형 변수(x축)에 따른 수치형 변수(y축)의 분포를 비교하는 데 사용됩니다. 일반적인 박스 플롯보다 더 많은 분위수(quantile)를 표시하여 데이터의 꼬리 부분(tail)을 더 세밀하게 시각화하고, 특히 큰 데이터셋에서 분포의 밀집도를 더 잘 보여줍니다.

### 코드/수식 해설
이 슬라이드는 `Seaborn` 라이브러리의 `boxenplot` 함수를 사용하여 와인 데이터셋에서 'class'별 'flavanoids'의 분포를 시각화하는 예시 코드를 보여줍니다.

```python
sns.boxenplot(data=wine, x="class", y="flavanoids",
              k_depth="trustworthy", width_method="linear",
              showfliers=True, outlier_prop=0.01)
```
-   `data=wine`: 시각화에 사용할 데이터프레임으로 `wine` 데이터셋을 지정합니다.
-   `x="class"`: x축에 표시될 범주형 변수로 `class` 컬럼을 지정합니다. 이는 각 와인의 종류를 나타냅니다.
-   `y="flavanoids"`: y축에 표시될 수치형 변수로 `flavanoids` 컬럼을 지정합니다. 이는 와인의 플라보노이드 함량을 나타냅니다.
-   `k_depth="trustworthy"`: `boxenplot`의 핵심 파라미터로, 박스를 그리는 데 사용할 "letter value"의 깊이를 결정합니다. `"trustworthy"`는 데이터의 크기에 따라 신뢰할 수 있는 수준의 분위수를 자동으로 선택합니다.
-   `width_method="linear"`: 박스의 너비를 조정하는 방법을 지정합니다. `"linear"`는 각 박스 내의 관측치 수에 비례하여 너비를 조정합니다.
-   `showfliers=True`: `boxenplot`에서 일반적으로 박스 밖에 위치하는 이상치(outlier)를 점으로 표시할지 여부를 결정합니다. `True`로 설정하면 이상치가 표시됩니다.
-   `outlier_prop=0.01`: 데이터 중 이상치로 간주할 비율을 지정합니다. 여기서는 상위/하위 1%를 이상치로 처리합니다.

### 강의 맥락
교수님은 `box plot`과 `violin plot`, 그리고 `boxenplot`이 모두 하나의 범주형 변수와 하나의 수치형 변수를 비교할 때 사용된다고 설명합니다. 특히 `box plot`에 대해 "이것은 단일 변수 데이터에 사용되지만, 이변량 데이터에도 사용될 수 있습니다. 첫 번째 축, 즉 속성은 'class'이고 두 번째 속성은 숫자 속성입니다. 따라서 각 클래스에 대해 우리는 박스 플롯을 가집니다."라고 언급하며, `x`축에 범주형 변수(`class`), `y`축에 수치형 변수(`alcohol` 또는 이 슬라이드의 `flavanoids`)를 배치하여 그룹별 분포를 시각화함을 강조합니다.

### 시험 포인트
-   ⭐ `boxenplot`이 `boxplot`과 유사하게 범주형 변수에 따른 수치형 변수의 분포를 비교하는 데 사용됨을 이해해야 합니다.
-   ⭐ 특히 `boxenplot`은 큰 데이터셋에서 분포의 꼬리 부분을 더 세밀하게 보여주며, `"k_depth"`와 같은 파라미터를 통해 이를 조절할 수 있다는 점을 기억하세요.

---

## Slide 31

### Strip/Swarm — Definition & When to Use

**핵심 개념**:
`Strip plot`과 `Swarm plot`은 범주형 변수에 따른 단일 수치형 변수의 분포에서 개별 관측치를 시각화하는 데 사용되는 1차원 산점도입니다.

*   **Strip plot**: 점들이 겹치는 것을 피하기 위해 약간씩 무작위로 옆으로 흔들리게(jittered) 표시됩니다.
*   **Swarm plot**: 점들이 겹치지 않도록 밀집하여 정렬됩니다 (non-overlapping packing).

**Use when**:
요약 통계(예: 상자 그림, 바이올린 그림)와 함께 원본 관측치를 보여줄 때 유용합니다. 이를 통해 평균이나 중앙값 같은 집계 값에 의해 가려질 수 있는 데이터의 미세 구조(microstructure), 즉 군집(clumps)이나 간격(gaps)을 파악할 수 있습니다.

**Pitfalls**:
데이터 포인트의 개수 $n$이 많을 때 ⭐**과도한 중첩(overplotting)**⭐ 문제가 발생할 수 있습니다. 이 경우 데이터를 다운샘플링하거나 다른 요약 플롯과 결합하여 사용해야 합니다.

**강의 맥락**:
교수님께서는 이 플롯들을 "각 범주에 대한 점들을 그리는 것"이라고 설명하시며, 특히 `strip plot`에서 점들이 겹치는 것을 피하기 위해 `jitter` 값을 설정할 수 있다고 강조하셨습니다.

> "Strip and swarm. So it's like a plotting point for each category. Okay, so strip plot. Here you can set `jitter` to some value so that we can avoid some overlap while we are plotting many points here."

**코드/수식 해설**:
`seaborn` 라이브러리의 `stripplot` 함수에서 `jitter` 파라미터를 사용하여 점들의 겹침을 피할 수 있습니다. `swarmplot`은 기본적으로 겹치지 않게 그립니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 예시 데이터 (와인 데이터셋을 가정)
# wine_df는 categorical 'class'와 numerical 'alcohol'을 가진 DataFrame이라 가정
# sns.stripplot(x="class", y="alcohol", data=wine_df, jitter=True) # strip plot
# sns.swarmplot(x="class", y="alcohol", data=wine_df) # swarm plot
# plt.show()
```

**시험 포인트**:
*   ⭐`Strip plot`과 `Swarm plot`의 주요 차이점 (jittered vs. non-overlapping packing)⭐
*   ⭐과도한 중첩(overplotting) 문제의 해결 방법 (jitter 사용, swarm plot 활용)⭐
*   이러한 플롯이 집계 값에 의해 가려진 데이터의 미세 구조를 보여주는 데 유용하다는 점.

---

## Slide 32

**핵심 개념**:
`stripplot`은 범주형 변수에 따른 수치형 변수의 개별 데이터 포인트 분포를 시각화하는 데 사용됩니다. 각 범주에 대해 모든 관측치를 개별 점으로 표시하여 데이터의 밀도와 개별 값들을 명확하게 볼 수 있게 해줍니다.

**코드/수식 해설**:
```python
sns.stripplot(data=wine, x="class", y="flavanoids",
              jitter=0.25, alpha=0.6, size=3)
```
*   `data=wine`: `wine` 데이터프레임을 사용합니다.
*   `x="class"`: X축은 `class` 범주형 변수를 나타냅니다.
*   `y="flavanoids"`: Y축은 `flavanoids` 수치형 변수를 나타냅니다.
*   `jitter=0.25`: `jitter` 매개변수는 같은 위치에 많은 점이 겹쳐서 가려지는 오버플로팅(over-plotting) 문제를 해결하기 위해, 각 점에 작은 무작위 변동(offset)을 X축 방향으로 추가합니다. `0.25`는 지터링 강도를 의미합니다.
*   `alpha=0.6`: 점의 투명도를 설정합니다. `0.6`은 반투명하게 만듭니다.
*   `size=3`: 각 점의 크기를 설정합니다.

**구체적 예시**:
주어진 예시는 와인 데이터셋에서 `class` (와인 등급)에 따른 `flavanoids` (플라보노이드 함량)의 분포를 보여줍니다. `class_0`, `class_1`, `class_2` 각 와인 등급별로 플라보노이드 함량의 개별 측정값들이 점으로 표시되어 있습니다. `jitter` 덕분에 각 점의 밀집된 분포를 명확하게 확인할 수 있습니다.

**강의 맥락**:
"Okay, so strip and swarm. So it's like a plotting point for each category. Okay, so strip plot. Here you can set jitter to some value so that we can avoid some overlap while we are plotting many points here."
교수님은 `strip plot`이 각 범주에 대해 개별 점들을 플로팅하는 방식임을 설명하며, 특히 `jitter` 파라미터를 사용하여 많은 점을 플로팅할 때 발생할 수 있는 오버랩(겹침) 문제를 피할 수 있다고 강조합니다.

**시험 포인트**:
*   ⭐`stripplot`의 주된 용도: 범주별 수치 데이터의 개별 관측치 분포 시각화.
*   ⭐`jitter` 매개변수의 역할: 오버플로팅 방지 및 데이터 포인트의 밀도 시각화.

---

## Slide 33

*오류 발생으로 해설을 생성하지 못했습니다.*

---

## Slide 34

### 핵심 개념
**Contingency Heatmap (교차표 히트맵)**은 두 범주형 변수(categorical variables) 간의 공동 발생 빈도(co-occurrence) 또는 연관성을 시각화하는 방법입니다. `pd.crosstab` 함수를 사용하여 두 범주형 변수의 교차표(contingency table)를 생성하고, 이를 `seaborn.heatmap`으로 시각화하여 각 조합의 빈도를 색상의 강도로 표현합니다. 이를 통해 어떤 범주 조합이 더 자주 발생하는지, 또는 특정 패턴이나 불균형이 있는지 파악할 수 있습니다.

### 코드/수식 해설
```python
wine["alcohol_bin"] = pd.cut(wine["alcohol"], 3, labels=["low", "mid", "high"])
ct = pd.crosstab(wine["class"], wine["alcohol_bin"])
sns.heatmap(ct, annot=True, fmt="d")
```
1.  `wine["alcohol_bin"] = pd.cut(wine["alcohol"], 3, labels=["low", "mid", "high"])`:
    *   `pd.cut()` 함수는 연속적인 숫자형 변수 `wine["alcohol"]`을 지정된 구간(bins)으로 나누어 범주형 변수로 변환합니다.
    *   `3`은 데이터를 세 개의 동일한 간격의 구간으로 나누라는 의미입니다.
    *   `labels=["low", "mid", "high"]`는 생성된 각 구간에 `low`, `mid`, `high`라는 레이블을 부여합니다.
    *   이 과정을 통해 숫자형 `alcohol` 특징을 `alcohol_bin`이라는 새로운 범주형 특징으로 변환합니다.
2.  `ct = pd.crosstab(wine["class"], wine["alcohol_bin"])`:
    *   `pd.crosstab()` 함수는 두 개 이상의 범주형 변수에 대한 교차표(contingency table)를 생성합니다.
    *   여기서는 `wine["class"]`와 새로 생성된 `wine["alcohol_bin"]` 두 범주형 변수 간의 공동 발생 빈도를 계산하여 `ct`라는 이름의 데이터프레임으로 저장합니다. `ct`는 각 `class`와 `alcohol_bin` 조합의 빈도수를 담고 있습니다.
3.  `sns.heatmap(ct, annot=True, fmt="d")`:
    *   `seaborn.heatmap()` 함수는 행렬 형태의 데이터를 히트맵으로 시각화합니다.
    *   `ct`는 위에서 생성된 교차표 데이터를 의미합니다.
    *   `annot=True`는 히트맵의 각 셀 내부에 실제 값(빈도수)을 숫자로 표시하도록 합니다. ⭐
    *   `fmt="d"`는 셀 안에 표시될 숫자의 형식을 정수(decimal integer)로 지정합니다.

### 구체적 예시
와인 데이터셋에서 `class` (class_0, class_1, class_2)와 `alcohol_bin` (low, mid, high)이라는 두 범주형 변수 간의 관계를 Contingency Heatmap으로 나타낸 결과입니다. 예를 들어, `class_0`과 `high` alcohol_bin의 교차점에는 `38`이라는 숫자가 표시되어 있는데, 이는 `class_0`에 속하면서 `high` alcohol 함량을 가진 와인이 38개 있다는 것을 의미합니다. 색상이 더 밝거나 어두운 셀을 통해 특정 `class`가 특정 `alcohol_bin`과 강한 연관성이 있음을 시각적으로 확인할 수 있습니다.

### 강의 맥락
교수님께서는 Contingency Heatmap이 두 범주형 변수 간의 연관성이나 불균형을 평가하는 표준적인 방법이라고 강조하셨습니다. 특히, `pd.crosstab`을 사용하여 교차표를 생성하는 과정과 `sns.heatmap`으로 이를 시각화하는 방법을 설명하셨습니다. 숫자형 `alcohol` 특징을 `pd.cut`을 사용하여 `low`, `mid`, `high`의 세 가지 범주형 `alcohol_bin`으로 변환하는 단계의 중요성을 언급하며, 이는 두 범주형 변수 간의 비교를 위한 필수 전처리 과정임을 강조하셨습니다. 또한, `annot=True` 파라미터를 사용하여 각 셀에 실제 빈도수를 표시하는 것이 분석에 도움이 된다고 설명하셨습니다. 히트맵을 통해 `class`와 `alcohol_bin` 간의 강한 관계를 시각적으로 확인할 수 있다고 언급하셨습니다.

### 시험 포인트
*   **Contingency Heatmap의 목적**: 두 **범주형 변수** 간의 공동 발생 빈도 및 연관성 파악. ⭐
*   `pd.cut()`을 사용하여 **숫자형 변수를 범주형 변수로 변환**하는 방법과 그 필요성. ⭐
*   `pd.crosstab()`을 사용하여 **교차표를 생성**하는 방법. ⭐
*   `sns.heatmap()`에서 `annot=True` 파라미터가 **셀 내부에 값을 표시**하는 역할. ⭐
*   히트맵에서 'hot cells' (색상이 밝은 셀)과 'cold cells' (색상이 어두운 셀)이 각각 무엇을 의미하는지 해석할 수 있어야 함.

---

## Slide 35

### Correlation Heatmap — Definition & When to Use

**핵심 개념**
상관 관계 히트맵은 두 수치형 변수 간의 선형 관계를 시각화하는 데 사용됩니다. 이는 피어슨 상관 계수($r$) 행렬을 색상으로 인코딩하여 강도와 부호를 나타냅니다.

**강의 맥락**
교수님은 상관 관계 히트맵이 "모든 수치형 피처를 한 번에 높은 수준에서 개괄적으로 파악하는 데 매우 유용하다"고 강조했습니다. 즉, 데이터셋에 있는 모든 가능한 수치형 피처 쌍 간의 선형 상관 관계를 측정하고 시각화하는 도구입니다.

*   **정의**: 피어슨 상관 계수($r$)는 두 변수 간의 선형 관계를 측정하며, 그 값은 $-1$부터 $1$까지입니다.
    *   $r = -1$: 완벽한 음의 선형 상관 관계
    *   $r = 1$: 완벽한 양의 선형 상관 관계
    *   $r = 0$: 선형 상관 관계 없음
*   **사용 시점**: 주로 데이터의 선형 연관성, 특히 ⭐**다중공선성(Multicollinearity)**을 스캔할 때 사용됩니다. 다중공선성은 두 개 이상의 예측 변수가 서로 높은 상관 관계를 가질 때 발생합니다.
*   **해석 방법**: 히트맵 내의 블록이나 줄무늬 패턴은 특징 그룹을 나타낼 수 있습니다. 색상의 강도와 방향(음수/양수)을 통해 상관 관계의 크기와 방향을 파악합니다.
*   **주의사항**:
    *   ⭐**상관 관계가 인과 관계를 의미하지는 않습니다($\text{Correlation} \neq \text{Causation}$).**
    *   이상치(outliers)는 피어슨 상관 계수 $r$의 절댓값을 과장할 수 있습니다.

**시험 포인트**
*   상관 관계 히트맵이 주로 사용되는 목적 (선형 연관성, 다중공선성 파악)을 이해하고 설명할 수 있어야 합니다.
*   ⭐피어슨 상관 계수 $r$의 범위($-1$에서 $1$)와 각 값의 의미를 정확히 알고 있어야 합니다.
*   ⭐상관 관계와 인과 관계의 차이점을 명확히 인지하고 있어야 합니다.

---

## Slide 36

**핵심 개념**
상관 히트맵(Correlation Heatmap)은 데이터셋 내의 모든 수치형 특성 쌍 간의 선형 상관관계를 시각화하는 강력한 도구입니다. 각 셀의 색상은 두 특성 간의 피어슨 상관계수(Pearson correlation coefficient)를 나타내며, 이 계수는 $-1$ (완벽한 음의 상관관계)부터 $1$ (완벽한 양의 상관관계)까지의 값을 가집니다. 이를 통해 여러 특성 간의 관계를 한눈에 파악하고, 특히 모델 학습에 영향을 미칠 수 있는 다중공선성(Multicollinearity)을 빠르게 식별하는 데 유용합니다.

**코드/수식 해설**

```python
num = wine.drop(columns=["target", "class"])
corr = num.corr()
sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap="vlag")
```

1.  `num = wine.drop(columns=["target", "class"])`: `wine` 데이터프레임에서 "target" 및 "class"와 같은 범주형 또는 분석에 필요 없는 열을 제외하고 순수하게 수치형 특성만 남깁니다. 상관관계는 수치형 데이터에 대해서만 계산할 수 있기 때문입니다.
2.  `corr = num.corr()`: 남은 수치형 특성들 간의 모든 쌍별 피어슨 상관계수를 계산하여 상관 행렬(correlation matrix)을 생성합니다.
3.  `sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap="vlag")`:
    *   `corr`: 생성된 상관 행렬을 히트맵의 데이터로 사용합니다.
    *   `vmin=-1`, `vmax=1`: 컬러바의 최솟값과 최댓값을 각각 $-1$과 $1$로 설정하여 피어슨 상관계수의 전체 범위를 표현합니다.
    *   `center=0`: 컬러맵의 중심을 $0$에 맞춰, 상관관계가 없는 경우를 시각적으로 명확하게 구분합니다.
    *   `cmap="vlag"`: `vlag` 컬러맵을 사용하여 음의 상관관계는 한 가지 색상(예: 파란색 계열), 양의 상관관계는 다른 색상(예: 노란색 계열), 그리고 $0$에 가까운 상관관계는 중립적인 색상으로 표현합니다.

**구체적 예시**
슬라이드에 제시된 와인(Wine) 데이터셋의 상관 히트맵은 `alcohol`, `malic_acid`, `ash` 등 여러 수치형 특성들 간의 관계를 보여줍니다. 예를 들어, `flavanoids`와 `total_phenols`는 밝은 노란색으로 표시되어 강한 양의 상관관계를 가짐을 알 수 있습니다. 반면, `malic_acid`와 `flavanoids`는 녹색 계열로 표시되어 상대적으로 약하거나 음의 상관관계를 가질 수 있음을 나타냅니다. 대각선은 각 특성 자신과의 상관관계이므로 항상 $1$로 표시됩니다.

**강의 맥락**
"And there is also another heatmap called the correlation heatmap. And this is very useful for getting a high level overview of all medical features at once. I want to measure the linear correlation between each pair of numerical features. And this pairs correlation range from the $-1$, Pears coefficient. Correlation. $-1$, this is the perfect negative. Correlation. $2$, $1$, perfect. Positive. and color is used to encode this value. And we can use this hidden map to quickly scan all linear associations. So this is especially important for spotting multi-colonial, I mean the Multicolinearity. The meaning of this is when two or more your predictor variables are highly correlated with each other. And this only shows linear correlation. See, we have a correlation. Because this is natural. Because each attribute is strongly correlated with itself, right? So we drop the categorical value attribute from the Y data frame and then call this CORR and pass this information to hitmap. So we can scan all the cells in this matrix to find the relationship. You can either find strongly positive correlated or strongly negatively correlated by looking at the colors."

교수님은 상관 히트맵이 모든 수치형 특성의 관계를 한눈에 파악하는 데 매우 유용하다고 강조하며, 각 쌍의 선형 상관관계를 측정한다고 설명합니다. 피어슨 상관계수가 $-1$에서 $1$까지의 범위이며 색상을 통해 이 값을 인코딩한다고 말합니다. 특히, 이 플롯이 다중공선성(Multicolinearity), 즉 두 개 이상의 예측 변수가 서로 강하게 상관되어 있는 경우를 탐지하는 데 중요하다고 강조합니다. 또한, 상관 히트맵은 선형 상관관계만 보여주며, 실제 코드에서 범주형 특성을 제외하고 `corr()` 함수로 상관 행렬을 계산한 후 `heatmap()` 함수에 전달하여 시각화한다고 설명합니다.

**시험 포인트**
*   ⭐ **상관 히트맵의 목적**: 데이터셋의 모든 수치형 특성 쌍 간의 선형 상관관계를 파악하고, 다중공선성(Multicolinearity)을 식별하는 데 사용됩니다.
*   ⭐ **피어슨 상관계수**: $-1$ (완벽한 음의 상관관계)부터 $1$ (완벽한 양의 상관관계)까지의 값을 가지며, $0$은 선형 상관관계가 없음을 의미합니다.
*   ⭐ `sns.heatmap` 함수에서 `vmin`, `vmax`, `center`, `cmap` 파라미터의 역할과 중요성을 이해해야 합니다.
*   ⭐ 상관 히트맵은 **선형** 상관관계만을 보여준다는 점을 기억해야 합니다.

---

## Slide 37

---
### 핵심 개념

Parallel Coordinates Plot은 고차원 데이터의 다변량 시각화 기법입니다. 각 관측치(sample)는 여러 개의 평행한 수직 축(feature axes)을 가로지르는 하나의 꺾은선(polyline)으로 표현됩니다. 각 수직 축은 데이터셋의 한 특성(feature)을 나타내며, 꺾은선은 해당 관측치의 각 특성 값을 연결합니다.

*   **정의**: 각 샘플($x_i$)이 여러 특성 축($F_1, F_2, ..., F_m$)을 따라 그 값을 연결하는 하나의 polyline으로 그려집니다.
*   **사용 시점**:
    *   클래스별 다변량 프로파일(multivariate profiles)을 비교할 때 유용합니다.
    *   데이터를 효과적으로 분리하는(strong separation) 특성 축이나, 특성 간의 복잡한 상호작용(crossings)을 파악하고자 할 때 사용합니다.
*   **해석 방법**:
    *   특정 축을 따라 선들이 명확하게 분리되는 경우 $\Rightarrow$ 해당 특성이 데이터를 잘 구분하는 **판별 특성(discriminative feature)**임을 의미합니다.
    *   선들이 빈번하게 교차하는 경우 $\Rightarrow$ 특성 간의 **상호작용(interaction) 또는 상충 관계(trade-offs)**가 있음을 나타냅니다.

### 구체적 예시

강의에서는 Iris 데이터셋을 예시로 들어 설명했습니다. 붓꽃의 종(species)별로 꽃잎 길이(petal length), 꽃잎 너비(petal width), 꽃받침 길이(sepal length), 꽃받침 너비(sepal width)라는 네 가지 특성에 대한 값을 평행 좌표계로 그리면, 각 종에 속하는 붓꽃들이 해당 특성들에서 어떤 패턴을 보이는지 시각적으로 확인할 수 있습니다. 예를 들어, Setosa 종은 petal length와 petal width에서 낮은 값을 보이지만, sepal width에서는 높은 값을 가지는 경향이 있습니다.

### 강의 맥락

교수님께서는 Parallel Coordinates Plot을 "고차원 데이터를 시각화하기 위한 (multivariate projections) 방법" 중 하나로 소개하며, 특히 "species"에 대해 이 플롯을 사용한다고 언급했습니다. "각 데이터셋의 관측치는 모든 축에서 각 값을 연결하는 하나의 polyline으로 그려집니다"라고 정의하면서, 이를 통해 "어떤 클래스가 특정 특성에서 높은 값을 가지고 다른 특성에서는 낮은 값을 가지는지 쉽게 볼 수 있다"고 강조했습니다. Iris 데이터셋의 Setosa 종을 예로 들어, "petal length와 petal width에서 낮은 값을 가지지만, sepal width에서는 높은 값을 가진다"고 설명하며, "단일 클래스에 대한 이 선들을 추적함으로써 어떤 패턴을 볼 수 있다"고 실제 데이터 해석 방법을 설명했습니다.

### 시험 포인트

*   **정의**: Parallel Coordinates Plot에서 각 샘플이 무엇으로 표현되는가? (⭐각 특성 축을 가로지르는 하나의 polyline)
*   **사용 목적**: 고차원 데이터에서 클래스별 다변량 프로파일 비교, 특성 간의 관계 및 분리 능력을 파악하는 데 사용됨.
*   **해석 방법**:
    *   특정 축에서 선들이 분리되는 패턴 $\Rightarrow$ ⭐**판별 특성(discriminative feature)**
    *   선들이 빈번하게 교차하는 패턴 $\Rightarrow$ ⭐**특성 간 상호작용 또는 상충 관계(interaction/trade-offs)**
*   **주의사항 (Pitfalls)**: 데이터의 수가 많을 때(large $n$) plot이 복잡해져(clutter) 판독이 어려울 수 있으므로, ⭐**특성 정규화(standardize features)**, 투명도 사용(transparency), 샘플링(downsample) 또는 집계(aggregate)와 같은 기법을 사용하여 시각적 혼란을 줄일 수 있어야 합니다.

---

## Slide 38

**핵심 개념**
*   **Parallel Coordinates (평행 좌표 그래프)**는 고차원 데이터를 시각화하는 강력한 방법입니다. 데이터셋의 각 관측치를 여러 축(변수)을 가로지르는 하나의 꺾은선(polyline)으로 표현하여, 각 변수 간의 관계와 그룹별 특성을 한눈에 파악할 수 있도록 합니다.
*   각 변수는 수직 축으로 표현되며, 관측치의 각 변수 값은 해당 축에 점으로 표시됩니다. 이 점들이 연결되어 하나의 관측치를 나타내는 선이 됩니다.
*   다양한 그룹이나 클래스별로 선의 색상을 다르게 하여 패턴을 비교할 수 있습니다.

**코드/수식 해설**
주어진 코드는 Iris 데이터셋을 표준화(Standardization)한 후 Parallel Coordinates 그래프를 그리는 과정을 보여줍니다.

```python
# Standardize in this exact order
X = iris[features].to_numpy() # 1. 선택된 feature들을 NumPy 배열로 변환
X = StandardScaler().fit_transform(X) # 2. StandardScaler를 사용하여 데이터를 표준화
df_scaled = pd.DataFrame(X, columns=features) # 3. 표준화된 데이터를 DataFrame으로 변환
df_scaled["species"] = iris["species"] # 4. 'species' 컬럼을 추가하여 그룹 정보를 포함
plt.figure(figsize=(7.6, 4.4)) # 5. 플롯의 크기를 설정
parallel_coordinates(df_scaled, "species", features, lw=0.9, alpha=0.45) # 6. Parallel Coordinates 플롯 생성
plt.tight_layout() # 7. 플롯 요소들의 레이아웃을 자동으로 조정
plt.show() # 8. 플롯을 화면에 표시
```
*   `StandardScaler().fit_transform(X)`: `StandardScaler`는 데이터를 표준 정규 분포로 변환합니다. 즉, 각 피처의 평균을 0, 표준편차를 1로 조정하여 스케일을 맞춥니다. 이는 서로 다른 스케일을 가진 변수들을 공정하게 비교하기 위해 중요합니다. 표준화된 값 $z$는 다음 수식으로 계산됩니다:
    $$z = \frac{x - \mu}{\sigma}$$
    여기서 $x$는 원본 값, $\mu$는 피처의 평균, $\sigma$는 피처의 표준편차입니다.
*   `parallel_coordinates(df_scaled, "species", features, ...)`: 이 함수는 `pandas.plotting` 모듈에 포함된 것으로, `df_scaled` 데이터프레임을 사용하여 평행 좌표 플롯을 생성합니다.
    *   `"species"`: `class_column` 인자로, 이 컬럼의 값에 따라 선의 색상이 결정됩니다 (예: `setosa`, `versicolor`, `virginica` 세 종류).
    *   `features`: 플롯에 사용할 변수(축) 목록을 지정합니다. 여기서는 `petal length`, `petal width`, `sepal length`, `sepal width`가 사용됩니다.
    *   `lw=0.9`, `alpha=0.45`: 선의 두께(linewidth)와 투명도(alpha)를 조절하여 겹치는 선이 많을 때 가독성을 높입니다.

**구체적 예시**
Iris 데이터셋의 표준화된 Petal 및 Sepal 관련 4가지 특징을 species(종)별로 시각화한 예시입니다.
*   `setosa` 종(주황색/노란색 계열)은 Petal Length와 Petal Width에서 낮은 값을 보이고, Sepal Width에서 높은 값을 보이는 경향이 있습니다.
*   `virginica` 종(검은색 계열)은 Petal Length와 Petal Width에서 높은 값을 보이며, Sepal Width에서 낮은 값을 보입니다.
*   `versicolor` 종(보라색 계열)은 이 두 종의 중간 특성을 나타냅니다.

**강의 맥락**
"So last one is called the parallel coordinates. Let's look at this one. So I will call this parallel coordinates on the species. That's why we have three species and we have four attributes. Petal length and petal width and petal length and petal... Seppal length and seppal width. And each observation in the dataset is drawn as a single polyline. That connects each value across all axes. So you can easily see which classes have high values on some features and low on others. So if you look at Setosa, they have low values and petal lengths and petal widths, but high value on setal widths and also there is some trend between the setal lengths and setal widths. okay so by tracing this line for the single class you can see some patterns okay"

교수님은 Parallel Coordinates가 **고차원 데이터를 시각화**하는 데 사용되며, 특히 **데이터셋의 각 관측치를 하나의 꺾은선으로 표현하여 여러 축(변수)에 걸친 값의 연결성**을 보여준다고 강조합니다. Iris 데이터셋 예시에서 `setosa` 종이 `petal length`와 `petal width`에서는 낮은 값을, `sepal width`에서는 높은 값을 보이는 경향이 있음을 언급하며, **단일 클래스에 대한 선을 따라가면서 패턴을 식별**하는 방법을 설명합니다.

**시험 포인트**
*   ⭐ **Parallel Coordinates의 목적**: 고차원 데이터의 시각화 및 변수 간 관계, 그룹별 특성 파악.
*   ⭐ **데이터 표현 방식**: 각 관측치가 하나의 꺾은선(polyline)으로 모든 변수 축을 연결함.
*   ⭐ **데이터 전처리**: 스케일이 다른 변수들을 비교하기 위해 `StandardScaler` 등을 이용한 **표준화가 필수적**이라는 점.
*   ⭐ **해석 방법**: 특정 그룹(여기서는 species)의 선들을 추적하여 어떤 변수에서 높거나 낮은 값을 가지는지, 그리고 변수들 간의 상대적인 경향성(예: 선의 기울기)을 분석할 수 있어야 함.

---

## Slide 39

**핵심 개념**
Residuals vs Fitted 플롯은 회귀 모델의 잔차(Residuals)를 예측값(Fitted Values)에 대해 시각화하여 모델 가정을 평가하는 데 사용되는 진단 도구입니다.

*   **정의**: 예측값($\hat{y}_i$)을 x축으로, 잔차($y_i - \hat{y}_i$)를 y축으로 하여 각 관측치를 점으로 표시한 플롯입니다.
*   **사용 목적**: 선형 모델의 가정(비선형성, 이분산성, 이상치 존재 여부 등)을 진단합니다.
*   **해석**:
    *   잔차가 0을 중심으로 무작위적인 밴드를 형성하면 모델 가정이 잘 충족되고 있음을 의미합니다.
    *   잔차에 경향(trend)이나 부채꼴(fan) 모양 등의 패턴이 보이면 모델에 문제가 있음을 나타냅니다 (예: 비선형성, 이분산성).
*   **주의사항**: 레버리지(leverage)나 영향력(influence)이 큰 점(예: Cook's distance)은 이 플롯만으로는 확인하기 어려우므로 별도로 검사해야 합니다.

**코드/수식 해설**
Residuals vs Fitted 플롯에서 사용하는 기본적인 수식은 잔차($e_i$)의 정의입니다.
$$e_i = y_i - \hat{y}_i$$
여기서,
*   $y_i$: 실제 관측값 (ground truth)
*   $\hat{y}_i$: 모델의 예측값 (prediction, fitted value)

이 플롯은 x축에 $\hat{y}_i$를, y축에 $e_i$를 사용하여 점을 그립니다.

**강의 맥락**
교수님은 이 플롯이 "아주 중요하지는 않다(not that important)"고 언급하며, 단순히 예측값(prediction)과 잔차(ground truth - prediction)를 시각화하는 것이라고 설명했습니다. 만약 데이터 포인트가 Y축의 0에 가깝다면 예측이 실제 값에 매우 가깝다는 것을 의미한다고 강조했습니다. 특정 패턴(patterns)이 보이면 잔차가 크다는 것을 나타내며, 이는 모델에 문제가 있음을 시사합니다. 교수님은 이를 "오래된 방식(old style)"으로 잔차를 확인하는 방법이라고 덧붙였습니다.

**시험 포인트**
*   ⭐ Residuals vs Fitted 플롯의 **x축과 y축이 각각 무엇**인지 정확히 아는 것이 중요합니다. (x: 예측값 $\hat{y}_i$, y: 잔차 $y_i - \hat{y}_i$)
*   ⭐ 이 플롯을 통해 어떤 **모델 가정**을 진단할 수 있는지 (비선형성, 이분산성, 이상치) 알아두세요.
*   ⭐ 잔차 플롯에서 **"좋은" 패턴과 "나쁜" 패턴** (무작위 밴드 vs. 경향/부채꼴 모양)을 구분할 수 있어야 합니다.

---

## Slide 40

### 핵심 개념
잔차(Residuals) 대 예측값(Fitted Values) 플롯은 회귀 모델의 진단을 위한 중요한 시각화 도구입니다. 이 플롯은 모델이 데이터를 얼마나 잘 설명하고 있는지, 그리고 모델의 가정이 충족되는지를 평가하는 데 사용됩니다. $x$축에는 모델의 예측값(fitted values)을, $y$축에는 실제값과 예측값의 차이인 잔차(residuals)를 배치합니다. 이상적인 경우, 잔차는 $x$축에 대해 무작위로 분포하며 특정 패턴을 보이지 않아야 합니다.

### 코드/수식 해설

슬라이드의 코드는 `diabetes` 데이터셋을 사용하여 `bmi` 특성으로 `target` 특성을 예측하는 기본적인 선형 회귀 모델을 만들고, 그 잔차를 시각화하는 과정을 보여줍니다.

```python
# 1. 기본적인 선형 회귀 모델 피팅: target ~ bmi
# 'bmi' 특성을 독립 변수 x로 설정
x = diabetes["bmi"].to_numpy()
# 'target' 특성을 종속 변수 y로 설정
y = diabetes["target"].to_numpy()

# numpy의 polyfit을 사용하여 1차 다항식 (선형 모델)을 피팅
# 반환값은 기울기(slope)와 절편(intercept)
slope, intercept = np.polyfit(x, y, 1)

# 피팅된 모델을 사용하여 예측값(fitted values) 계산
fitted = slope * x + intercept
# 실제값(y)에서 예측값(fitted)을 빼서 잔차(residuals) 계산
residuals = y - fitted

# 2. Seaborn을 사용한 잔차 대 예측값 플롯
sns.set_theme() # Seaborn 테마 설정

# 예측값(fitted)을 x축, 잔차(residuals)를 y축으로 하는 산점도 생성
ax = sns.scatterplot(x=fitted, y=residuals, alpha=0.7)
# y=0에 수평 기준선 추가 (잔차가 0인 지점 표시)
ax.axhline(0, linestyle="--", linewidth=1.2)

# 축 레이블과 플롯 제목 설정
ax.set(
    xlabel="fitted (linear on bmi)", # x축 레이블: 예측값
    ylabel="residual",             # y축 레이블: 잔차
    title="Diabetes: Residuals vs Fitted" # 플롯 제목
)
plt.tight_layout() # 레이아웃 자동 조정
plt.show() # 플롯 표시

# 3. Seaborn의 residplot을 사용한 간편한 잔차 플롯 (대안)
# sns.residplot은 predictor를 x축으로, target을 y축으로 받아 자동으로 잔차 플롯을 생성
# sns.residplot(data=diabetes, x="bmi", y="target")
```

위 코드에서 잔차($e_i$)는 다음과 같이 계산됩니다:
$$
e_i = y_i - \hat{y}_i
$$
여기서 $y_i$는 $i$번째 관측치의 실제값이고, $\hat{y}_i$는 $i$번째 관측치의 예측값입니다.

### 구체적 예시
이 플롯에서 점들이 $y=0$ 선 주위에 무작위로 밀집되어 있다면, 모델의 예측이 전반적으로 잘 맞고 잔차에 특별한 패턴이 없음을 의미합니다. 만약 점들이 특정 패턴(예: U자형, V자형, 나팔형 등)을 보이거나, $y=0$ 선에서 멀리 떨어진 아웃라이어가 많다면 모델의 가정이 위배되거나 모델이 데이터를 잘 설명하지 못하고 있음을 시사합니다.

### 강의 맥락
교수님께서는 잔차 대 예측값 플롯이 모델의 예측값과 잔차($\text{실제값} - \text{예측값}$)를 보여주는 플롯이라고 설명하셨습니다. 만약 데이터가 잔차가 $0$인 선(강의 중에는 $0,9$로 언급되었으나 $0,0$을 의미) 근처에 밀집해 있다면 예측이 실제값과 매우 가깝다는 것을 의미한다고 강조하셨습니다. 반대로 $0$에서 멀리 떨어져 있다면 상당한 오차가 있음을 나타내며, 잔차에 특정 패턴이 나타나는지 확인해야 한다고 하셨습니다. 교수님께서는 이 플롯이 "아주 중요하지는 않지만 (not that important)" "오래된 방식(old style)"으로 잔차를 확인하는 한 가지 방법이라고 덧붙이셨습니다.

### 시험 포인트
*   ⭐ **잔차(Residuals)의 정의**: 실제값과 예측값의 차이 ($e_i = y_i - \hat{y}_i$).
*   ⭐ **잔차 대 예측값 플롯의 목적**: 회귀 모델의 가정을 평가하고, 모델이 데이터를 얼마나 잘 설명하는지 진단.
*   ⭐ **이상적인 잔차 플롯의 특징**: 잔차가 $y=0$ 주위에 무작위로 분포하며, 특정 패턴을 보이지 않아야 함.
*   **잔차 패턴 해석**: 특정 패턴(예: 곡선 형태)이 나타나면 모델에 문제가 있거나 더 복잡한 모델이 필요함을 의미할 수 있음.

---

## Slide 41

**핵심 개념**:
잔차(Residual) vs 예측값(Fitted Value) 플롯은 회귀 모델의 진단 플롯 중 하나로, 모델의 예측값($\hat{y}$)에 대한 잔차($e$)를 시각화하여 모델의 가정 충족 여부, 오차의 패턴, 이상치 등을 확인합니다. 잔차는 실제값($y$)에서 예측값($\hat{y}$)을 뺀 값입니다: $e = y - \hat{y}$.

**구체적 예시**:
슬라이드의 `Diabetes: Residuals vs Fitted` 플롯은 당뇨병 데이터셋에 대한 모델의 잔차와 예측값을 보여줍니다.
*   **X축**은 `fitted (linear on bmi)`로, 모델의 예측값을 나타냅니다.
*   **Y축**은 `residual`로, 실제값에서 예측값을 뺀 잔차를 나타냅니다.
*   점선으로 표시된 `residual = 0` 라인을 기준으로, 잔차들이 무작위로 분포하는 것이 이상적입니다. 플롯을 보면 잔차들이 완전히 무작위로 분포하지 않고, 예측값이 높은 부분에서 잔차의 분산이 커지는 경향(fan shape)이나 특정한 패턴이 관찰될 수 있습니다. 이는 모델의 예측 오차가 일관되지 않거나, 모델이 데이터의 일부 패턴을 제대로 포착하지 못했음을 시사할 수 있습니다.

**강의 맥락**:
교수님은 이 `residual fitted plot`이 모델의 예측값(x축)과 잔차(`ground truth - prediction`, y축)를 보여주는 플롯이라고 설명했습니다. 잔차가 0인 선에 가까운 데이터는 예측이 실제값에 매우 가깝다는 것을 의미하며, 이 선에서 멀리 떨어진 데이터는 상당한 오차가 있음을 나타냅니다. 교수님은 플롯에서 잔차의 크기가 다르거나 패턴이 보인다고 언급하며, "You see some patterns there."라고 강조했습니다. 이는 모델의 예측 오차가 일관되지 않거나, 잡지 못한 패턴이 있을 수 있음을 의미합니다. 다만, 교수님은 이 플롯이 "not that important"하고 "old style"의 잔차 분석 방법 중 하나라고 덧붙였습니다.

**시험 포인트**:
⭐ 이 플롯은 회귀 모델 진단에 사용되며, 잔차($e = y - \hat{y}$)가 0선 주변에 무작위로 분포하는 것이 이상적이라는 점을 이해하는 것이 중요합니다. 하지만 교수님이 "not that important"하다고 언급했습니다.

---
