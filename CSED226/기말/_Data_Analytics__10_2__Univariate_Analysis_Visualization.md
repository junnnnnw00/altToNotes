# CSED226 - _Data_Analytics__10_2__Univariate_Analysis_Visualization 상세 해설 노트 (음성 전사 포함)

> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다. Alt(altalt.io) 음성 전사 데이터를 함께 활용했습니다.

---

## Slide 1

**핵심 개념**:
*   **단변량 데이터 (Univariate Data)**: 하나의 속성(attribute) 또는 변수(variable)에 대한 데이터를 의미합니다. 예를 들어, 학생들의 키, 특정 상품의 가격, 특정 지역의 평균 기온 등 단일 측정값을 다루는 데이터입니다.
*   **단변량 데이터 분석 및 시각화**: 본 강의는 단변량 데이터를 분석하고 효과적으로 시각화하는 방법을 다룹니다. 특히, 주어진 데이터의 특성에 따라 "어떤 플롯(plot)을 언제 사용해야 하는지"에 대한 가이드가 중요하게 다뤄질 예정입니다.
*   **히스토그램 (Histogram)**: 데이터의 전반적인 형태(shape)나 분포(distribution)를 개략적으로 파악할 때 가장 기본적으로 활용되는 시각화 도구입니다. 데이터를 여러 구간(bins)으로 나누고 각 구간에 속하는 데이터의 빈도(frequency)를 막대 형태로 표현하여 분포의 특징을 보여줍니다.

**코드/수식 해설**:
이 슬라이드 구간에서는 특정 코드나 수식이 직접적으로 제시되지는 않았습니다. 그러나 교수님께서 히스토그램의 `bins` 매개변수 튜닝과 데이터 정규화의 중요성을 강조하셨으므로, 이후 강의에서 Matplotlib의 `plt.hist()` 함수나 Pandas의 `.hist()` 메소드 사용 시 `bins` 인자 조절 및 `density=True`와 같은 정규화 옵션에 대한 코드 예시가 다뤄질 것으로 예상됩니다.

**구체적 예시**:
*   **단변량 데이터 예시**: 한 반 학생들의 중간고사 `점수` 데이터가 대표적인 단변량 데이터입니다. 이 데이터는 학생 수라는 관측치 수와 점수라는 하나의 변수로 구성됩니다.
*   **히스토그램 예시**: 만약 학생들의 중간고사 점수가 $0$점에서 $100$점 사이에 분포한다면, 이 점수들을 $10$점 단위(예: $0-10$, $11-20$, ..., $91-100$)로 계급 구간(bins)을 나누어 각 구간에 속하는 학생 수를 막대로 표현할 수 있습니다. 예를 들어, $81-90$점 구간에 $15$명의 학생이 있다면, 이 구간의 막대 높이는 $15$가 됩니다. 이를 통해 점수 분포가 어느 쪽에 몰려 있는지, 고득점자와 저득점자의 비율은 어떤지 등을 시각적으로 파악할 수 있습니다.

**강의 내용**:
*   교수님께서는 "어떤 플롯을 언제 사용해야 하는가"가 이번 강의의 핵심이며, 이는 전체 강의를 요약하는 가장 중요한 부분이므로 ⭐**반드시 암기**해야 한다고 여러 번 강조하셨습니다.
*   히스토그램을 사용할 때는 데이터의 분포를 가장 잘 나타내도록 `bins` (계급 구간) 매개변수를 적절하게 튜닝하는 것이 매우 중요하다고 언급하셨습니다.
*   특히, 서로 다른 크기(데이터 포인트 수)를 가진 두 그룹의 분포를 히스토그램으로 비교할 때는 반드시 데이터를 ⭐**정규화(normalize)**하여 상대적인 비율이나 밀도를 비교해야 한다고 강조하셨습니다. (예: 단순히 빈도수를 비교하는 대신, 전체에서 차지하는 비율이나 확률 밀도로 비교)

**시험 포인트**:
*   ⭐**단변량 데이터의 정의**를 정확히 이해하고 설명할 수 있어야 합니다. (하나의 속성/변수에 대한 데이터)
*   ⭐히스토그램이 데이터의 **단순한 형태(simple shape)나 분포 개요(distribution overview)를 파악**하는 데 가장 기본적인 도구라는 점을 기억해야 합니다.
*   ⭐히스토그램 사용 시 **`bins` (계급 구간) 매개변수 튜닝의 중요성**과, **서로 다른 크기의 그룹을 비교할 때 정규화(normalize)를 반드시 해야 하는 이유**를 설명할 수 있어야 합니다.

---

## Slide 2

**핵심 개념**

*   **ECDF (Empirical Cumulative Distribution Function)**: 데이터의 누적 분포를 'bin-free'하고 '정확한 누적 뷰(exact cumulative view)'로 보여주는 함수입니다. 즉, 히스토그램처럼 특정 구간(bin)에 얽매이지 않고 각 데이터 포인트의 실제 값을 기반으로, 해당 값보다 작거나 같은 데이터의 비율을 나타냅니다. 특히 표본 크기($n$)가 서로 다른 여러 그룹을 비교할 때 강력한 도구입니다.
*   **KDE (Kernel Density Estimate)**: 데이터 분포의 '부드러운 모양(smooth shape)'과 '봉우리(modes, peaks)'를 파악하기 위한 비모수적인 밀도 추정 방법입니다. 히스토그램과 달리 연속적인 곡선 형태로 분포를 시각화하며, 데이터가 밀집된 부분을 봉우리로 나타냅니다. KDE의 형태는 '대역폭(bandwidth)' 선택에 크게 영향을 받으며, 데이터가 특정 범위에 유계(bounded)될 경우 편향을 피하기 위해 데이터를 변환하거나 반영해야 합니다.
*   **Boxplot (상자 그림)**: 여러 데이터 그룹 간의 분포를 '간결하게 비교(compact group comparison)'하는 데 사용되는 표준적인 시각화 도구입니다. 중앙값, 사분위수(Q1, Q3), 데이터의 퍼짐(IQR), 이상치(outliers) 등을 한눈에 보여줍니다.

**코드/수식 해설**

**ECDF 예시 (Python, `seaborn`)**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 가상 데이터 생성: 표본 크기가 다른 두 그룹
data_group1 = np.random.normal(loc=0, scale=1, size=100)
data_group2 = np.random.normal(loc=1, scale=0.8, size=150) # n이 다름

plt.figure(figsize=(8, 5))
sns.ecdfplot(data_group1, label='Group 1 (n=100)')
sns.ecdfplot(data_group2, label='Group 2 (n=150)')
plt.title('ECDF for Unequal Sample Sizes')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.grid(True)
plt.show()
```

**KDE 예시 (Python, `seaborn`)**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 가상 데이터 생성: 두 개의 봉우리를 가진 분포
data_bimodal = np.concatenate([np.random.normal(0, 1, 100),
                               np.random.normal(3, 0.5, 50)])

plt.figure(figsize=(8, 5))
# 대역폭 조절에 따른 KDE 형태 변화
sns.kdeplot(data_bimodal, bw_adjust=0.5, label='KDE (bw_adjust=0.5, sharper)')
sns.kdeplot(data_bimodal, bw_adjust=1, label='KDE (bw_adjust=1, default)')
sns.kdeplot(data_bimodal, bw_adjust=2, label='KDE (bw_adjust=2, smoother)')
plt.title('KDE Plot with Different Bandwidths')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
```

**KDE의 핵심 수식 아이디어**

KDE는 각 데이터 포인트 $x_i$에 커널 함수 $K$를 적용하고, 이를 모두 더하여 밀도 함수를 추정합니다.
KDE 추정치 $\hat{f}(x)$는 다음과 같습니다:

$$
\hat{f}(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right)
$$

여기서:
*   $n$은 데이터 포인트의 총 개수
*   $h$는 ⭐**대역폭(bandwidth)**⭐이며, 추정된 곡선의 부드러움을 결정하는 핵심 파라미터입니다.
*   $K(\cdot)$는 커널 함수(가장 흔하게 가우시안 커널)입니다.
*   $x_i$는 개별 데이터 포인트입니다.

**Boxplot 예시 (Python, `seaborn`)**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 가상 데이터 생성: 세 그룹의 데이터
data_group_a = np.random.normal(loc=0, scale=1, size=100)
data_group_b = np.random.normal(loc=2, scale=0.8, size=120)
data_group_c = np.random.normal(loc=-1, scale=1.2, size=90)

df = pd.DataFrame({
    'Value': np.concatenate([data_group_a, data_group_b, data_group_c]),
    'Group': ['A']*100 + ['B']*120 + ['C']*90
})

plt.figure(figsize=(8, 6))
sns.boxplot(x='Group', y='Value', data=df)
plt.title('Boxplot for Compact Group Comparison')
plt.xlabel('Group')
plt.ylabel('Value')
plt.grid(axis='y', linestyle='--')
plt.show()
```

**구체적 예시**

*   **ECDF**: 서로 다른 두 공장에서 생산된 부품들의 수명을 비교할 때, 각 공장 부품의 수가 달라도 ECDF를 사용하면 "수명이 100시간 이하인 부품의 비율"을 정확하게 비교하여 어느 공장이 더 안정적인 부품을 생산하는지 평가할 수 있습니다.
*   **KDE**: 도시 거주자들의 연봉 분포를 분석할 때, KDE는 연봉이 가장 많이 몰려 있는 구간(봉우리)과 전체적인 연봉 분포의 부드러운 형태를 곡선으로 보여줍니다. 만약 고소득자와 저소득자 간의 격차가 크다면 두 개 이상의 봉우리가 나타날 수 있습니다. 예를 들어, 연봉은 음수가 될 수 없으므로, 이러한 '유계(bounded)' 데이터에 KDE를 적용할 때는 데이터를 변환(예: 로그 변환)하여 분포의 왜곡을 피해야 합니다.
*   **Boxplot**: 여러 학과 학생들의 학점을 비교할 때, 각 학과의 Boxplot을 나란히 그려보면 중간 학점, 학점 분포의 폭, 그리고 이상치(매우 높거나 낮은 학점)를 가진 학과를 신속하게 파악하고 비교할 수 있습니다.

**강의 내용**

교수님께서는 데이터 분포를 시각화하는 다양한 도구들의 적절한 활용 시점을 강조하셨습니다.

*   **ECDF**: "bin-free"하고 "exact cumulative view"를 제공하여 히스토그램의 단점인 빈 설정의 영향을 받지 않는다고 설명하셨습니다. 특히 ⭐**"unequal sample sizes (unequal $n$)"**⭐, 즉 그룹 간 표본 크기가 다를 때 ECDF가 매우 유용하다는 점을 강조하셨습니다.
*   **KDE**: 데이터의 "smooth shape"과 "moles (peaks)"를 파악하는 데 적합하다고 설명하며, 히스토그램이 부드럽지 못한 형태를 가지는 것과 대조된다고 하셨습니다. ⭐**"bandwidth"를 선택하는 것이 KDE에서 "crucial kind of a concept"**⭐라고 매우 중요하게 강조하셨습니다. 또한, 데이터가 "bounded" (예: 오직 양수 값만)일 경우, 편향을 피하기 위해 데이터를 "reflect or transform"해야 한다고 지적하셨습니다. KDE에 대해서는 "we will spend some time for explaining the KDE plot"라고 하셨으므로, 추후 더 자세히 다뤄질 중요한 개념임을 알 수 있습니다.
*   **Boxplot**: "Compact group comparison"을 위한 "standard" 시각화 도구이며, 학생들이 "familiar with boxplot"해야 한다고 언급하며 기본적인 이해를 강조하셨습니다.

**시험 포인트**

*   ⭐**ECDF의 주요 특징 및 활용 시점**: "Bin-free", "exact cumulative view"라는 특징과 특히 ⭐**표본 크기가 다른 그룹($n$이 불균등한)을 비교할 때**⭐ ECDF가 강력하다는 점을 이해하고 설명할 수 있어야 합니다.
*   ⭐**KDE의 핵심 요소**: 데이터의 "smooth shape"과 "modes (peaks)"를 파악하는 데 사용되며, ⭐**'대역폭(bandwidth)'이 KDE 곡선에 미치는 영향**⭐과 '대역폭 선택'의 중요성을 반드시 알아야 합니다.
*   ⭐**KDE 사용 시 고려사항**: 데이터가 유계(bounded)인 경우, ⭐**편향을 피하기 위한 데이터 변환(reflect/transform)의 필요성**⭐을 기억해야 합니다.
*   **Boxplot의 기본 용도**: ⭐"Compact group comparison"에 적합한 표준 도구이며, 박스 플롯의 각 부분이 무엇을 의미하는지(중앙값, 사분위수, 이상치 등) 알고 해석할 수 있어야 합니다.⭐
*   ⭐**각 시각화 도구가 어떤 분석 목적에 가장 적합한지 (What to Use When)**⭐를 구분하고 설명할 수 있는 능력이 중요합니다.

---

## Slide 3

**핵심 개념**
이 슬라이드는 향후 데이터 분석 및 시각화 실습을 위해 사용할 실제 데이터셋과 기본적인 환경 설정을 소개합니다. 주로 `scikit-learn` 라이브러리에서 제공하는 대표적인 데이터셋 세 가지를 다루며, 이후 예제에서 `df`라는 `DataFrame`에 "value"와 "group"이라는 표준화된 컬럼 이름을 가정하고 진행할 것임을 명시합니다.

*   **실습 데이터셋**:
    *   **Iris (붓꽃)**: 150개의 붓꽃 샘플. 꽃받침 길이(sepal length), 꽃받침 너비(sepal width), 꽃잎 길이(petal length), 꽃잎 너비(petal width)의 네 가지 특징(cm 단위)과 0, 1, 2 세 가지 종(species)으로 분류되는 타겟 값을 가집니다.
    *   **Wine (와인)**: 178개의 와인 샘플. 알코올, 플라보노이드(flavanoids) 등 13가지 물리화학적 특징과 0, 1, 2 세 가지 클래스로 분류되는 타겟 값을 가집니다.
    *   **Diabetes (당뇨병)**: 442명의 환자 샘플. BMI와 같은 10가지 표준화된 특징과 질병 진행도(disease progression)를 나타내는 타겟 값을 가집니다.
*   **데이터프레임 가정**: 예제 코드에서는 `pandas.DataFrame` 객체를 `df`로 지칭하며, 분석 대상이 되는 연속형 데이터는 "value" 컬럼, 그룹을 나타내는 범주형 데이터는 "group" 컬럼에 저장되어 있다고 가정합니다.

**코드/수식 해설**
슬라이드 자체에는 코드가 없지만, `scikit-learn`에서 데이터셋을 로드하는 예시와 음성 강의에서 언급된 로그 변환의 수식을 제시합니다.

*   **데이터셋 로드 예시**:
    ```python
    from sklearn.datasets import load_iris, load_wine, load_diabetes
    import pandas as pd

    # Iris 데이터셋 로드
    iris = load_iris(as_frame=True)
    iris_df = iris.frame
    print("Iris DataFrame head:\n", iris_df.head())
    print("Iris target names:", iris.target_names)

    # Wine 데이터셋 로드
    wine = load_wine(as_frame=True)
    wine_df = wine.frame
    print("\nWine DataFrame head:\n", wine_df.head())

    # Diabetes 데이터셋 로드
    diabetes = load_diabetes(as_frame=True)
    diabetes_df = diabetes.frame
    print("\nDiabetes DataFrame head:\n", diabetes_df.head())
    ```
*   **로그 변환 (Log Transform)**:
    데이터의 분포가 한쪽으로 치우쳐 있거나(heavy right tails) 값이 항상 양수(non-negative)일 때, 데이터의 왜도를 줄이고 정규 분포에 가깝게 만들기 위해 적용하는 변환입니다. 주로 자연로그($\ln$)를 사용합니다.
    $$
    y' = \log(y)
    $$
    여기서 $y$는 원본 데이터, $y'$는 변환된 데이터입니다. 때로는 $y \ge 0$인 경우를 위해 $\log(y+1)$과 같이 작은 값을 더해 로그를 취하기도 합니다.

**구체적 예시**
`scikit-learn` 데이터셋을 활용하여 "value"와 "group" 컬럼을 만드는 예시입니다. 예를 들어, Iris 데이터셋에서 꽃잎 길이를 "value"로, 종을 "group"으로 설정할 수 있습니다.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
iris_df = iris.frame

# 'value'와 'group' 컬럼을 가정에 맞춰 데이터프레임 구성
# 예: 꽃잎 길이를 'value', 붓꽃 종을 'group'으로 사용
df_example = pd.DataFrame({
    'value': iris_df['petal length (cm)'],
    'group': iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
})
print("\nExample DataFrame with 'value' and 'group' columns:\n", df_example.head())
```
이런 형식의 `df_example`을 사용하여 이후 단변수 데이터 분석 및 시각화 예제들이 진행될 수 있습니다.

**강의 내용**
교수님께서는 슬라이드에서 소개된 데이터셋을 실제로 분석하고 시각화하기 전에 고려해야 할 중요한 점들을 강조하셨습니다.

*   **표본 크기($N$)와 시각화 선택**: 표본 크기가 큰 경우($\text{large } N$), 박스플롯(boxplot)이 좋은 선택입니다. 특히, 박스플롯은 데이터의 꼬리(tails) 부분에 대한 더 많은 세부 정보를 보여주기 때문에 유용합니다.
*   **실제 관측치 표현**: 실제 개별 관측치를 보고 싶을 때는 록 플롯(rock plot)이나 스트립 플롯(strip plot)을 사용할 수 있습니다. 이 플롯들은 박스플롯이나 바이올린 플롯(violin plot) 위에 겹쳐서(overlay) 사용하여 데이터의 이상 여부를 확인하는(sanity check) 데 좋습니다.
*   **정규성 검정 및 꼬리 검사**: 데이터의 정규성(normality)을 확인하거나 데이터의 꼬리 부분을 자세히 검사하는 데 가장 좋은 도구는 QQ 플롯(QQplot)입니다.
*   **데이터 변환**: 데이터가 무거운 오른쪽 꼬리(heavy right tails)를 가지거나 항상 양수(non-negative)인 경우, 로그 변환(log transform)과 같은 변환을 적용하는 것이 시각화를 위한 좋은 첫 단계가 될 수 있습니다. 이는 데이터 분포를 개선하여 패턴을 더 명확하게 보여줄 수 있습니다.
*   **실제 데이터셋 활용**: 이러한 이론적 배경을 바탕으로, `scikit-learn` (강의 음성에서는 "CycliLon library"로 언급되었으나, 슬라이드 내용상 `scikit-learn`으로 추정)에서 제공하는 세 가지 실제 데이터셋을 사용하여 실습할 것임을 언급하셨습니다.

**시험 포인트**
*   ⭐ **데이터셋의 종류와 특징**: Iris, Wine, Diabetes와 같은 `scikit-learn` 내장 데이터셋의 주요 특징(샘플 수, 특징 종류, 타겟의 의미)을 이해하고 있어야 합니다.
*   ⭐ **시각화 도구의 적절한 사용**:
    *   **박스플롯**: 대규모 데이터의 꼬리 부분 상세 정보를 확인하는 데 유용.
    *   **록 플롯/스트립 플롯**: 실제 개별 관측치를 보여주며, 박스/바이올린 플롯과 함께 sanity check 용도로 사용.
    *   **QQ 플롯**: 데이터의 정규성 검정 및 꼬리 분포 검사에 최적의 도구.
*   ⭐ **데이터 변환의 중요성**: 데이터가 특정 분포(예: heavy right tails, non-negative)를 가질 때, 로그 변환과 같은 적절한 변환이 시각화 및 분석의 품질을 향상시키는 데 매우 중요함을 이해해야 합니다.

---

## Slide 4

**핵심 개념**
*   **실제 데이터셋 로딩**: 머신러닝 실습을 위해 `scikit-learn` 라이브러리에서 제공하는 Iris, Wine, Diabetes와 같은 실제 데이터셋을 로드하고 활용합니다.
*   **Pandas DataFrame 활용**: 로드된 데이터셋을 `pandas`의 `DataFrame` 형태로 변환하여 데이터 조작 및 분석의 편리성을 높입니다.
*   **타겟 변수 레이블 변환**: 숫자 형태의 타겟 변수(예: 0, 1, 2)를 실제 의미를 가지는 문자열 레이블(예: "setosa", "versicolor")로 변환하여 가독성을 향상시킵니다.

**코드/수식 해설**

```python
import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
from sklearn.datasets import load_iris, load_wine, load_diabetes

# scikit-learn에서 제공하는 데이터셋을 pandas DataFrame으로 로드
# 'as_frame=True' 옵션은 데이터를 DataFrame 형태로 반환하도록 지시합니다.
# '.frame'은 Bunch 객체에서 data와 target을 결합한 DataFrame을 추출합니다.
iris = load_iris(as_frame=True).frame
wine = load_wine(as_frame=True).frame
diabetes = load_diabetes(as_frame=True).frame

# Convenience: readable group labels
# 'target' 열의 숫자 값을 의미 있는 문자열로 매핑하여 새로운 'species' 열을 생성합니다.
iris["species"] = iris["target"].map({0: "setosa", 1: "versicolor", 2:"virginica"})
# 'target' 열의 숫자 값을 와인 등급 'A', 'B', 'C'로 매핑하여 새로운 'class' 열을 생성합니다.
wine["class"] = wine["target"].map({0: "A", 1: "B", 2:"C"})
```
*   **라이브러리 임포트**: `numpy` (수치 계산), `pandas` (데이터 처리), `matplotlib.pyplot` (시각화), `seaborn` (시각화) 등 파이썬 데이터 분석의 핵심 라이브러리들을 임포트합니다.
*   **`sklearn.datasets`**: `scikit-learn` 패키지 내의 `datasets` 모듈에서 `load_iris`, `load_wine`, `load_diabetes` 함수를 가져와 데이터를 로드합니다.
*   **`as_frame=True`**: 이 인수는 로드된 데이터를 `Bunch` 객체 대신 `pandas.DataFrame` 형태로 가져오도록 설정합니다. 이는 데이터 처리에 매우 유용합니다.
*   **`.map()` 함수**: `pandas.Series`의 `map()` 함수는 시리즈의 각 값을 딕셔너리에 따라 새로운 값으로 변환하는 데 사용됩니다. 이를 통해 숫자 타겟 레이블을 사람이 읽기 쉬운 문자열 레이블로 바꿀 수 있습니다.

**구체적 예시**
*   **Iris 데이터셋**: 붓꽃의 꽃받침 길이($L_{sepal}$), 꽃받침 너비($W_{sepal}$), 꽃잎 길이($L_{petal}$), 꽃잎 너비($W_{petal}$) 네 가지 특성을 사용하여 세 가지 붓꽃 종(Setosa, Versicolor, Virginica) 중 하나로 분류하는 대표적인 분류 문제입니다.
*   **Wine 데이터셋**: 13가지 화학적 특성(예: alcohol, malic_acid, flavanoids)을 바탕으로 세 가지 다른 와인 품종(클래스 0, 1, 2 또는 'A', 'B', 'C') 중 하나로 분류하는 문제입니다.
*   **Diabetes 데이터셋**: 442명의 당뇨병 환자에 대한 10가지 신체 특성(예: BMI, age, sex)을 사용하여 1년 후 질병 진행도(질병의 심각성 정도)를 예측하는 회귀 문제입니다.

**강의 내용**
*   강의에서는 `Matplotlib`도 사용할 수 있지만 `Scikit-learn` 라이브러리에 중점을 두어 데이터 로딩과 머신러닝 개념을 다룰 것임을 언급했습니다.
*   **Iris 데이터셋**: 150개의 꽃 샘플을 포함하며, 꽃받침과 꽃잎의 길이 및 너비는 특징(`X` 값), 3가지 종(0, 1, 2)은 타겟 변수(`Y` 값)입니다.
*   **Wine 데이터셋**: 178개의 샘플을 가지며, 알코올, 플라보노이드 등의 물리화학적 특징은 `X` 속성, 3가지 와인 등급(0, 1, 2)은 `Y` 속성입니다.
*   **Diabetes 데이터셋**: 442명의 환자 샘플을 포함하며, BMI와 같은 표준화된 특징은 `X`, 질병 진행도를 나타내는 타겟 변수는 `Y`입니다.
*   코딩 예시에서는 데이터가 `pandas DataFrame` 형태로 `DF`라는 이름으로 존재한다고 가정하고 진행할 것이라고 강조했습니다. (슬라이드에서는 `iris`, `wine`, `diabetes`라는 변수명 사용).

**시험 포인트**
*   ⭐ `sklearn.datasets`에서 제공하는 데이터셋을 `pandas DataFrame`으로 로드하는 기본적인 코드 (`load_dataset(as_frame=True).frame`)를 정확히 이해하고 사용할 수 있어야 합니다.
*   ⭐ `DataFrame`의 `map()` 함수를 사용하여 숫자 레이블을 의미 있는 문자열 레이블로 변환하는 방법을 숙지하세요.
*   ⭐ 각 데이터셋(Iris, Wine, Diabetes)이 어떤 종류의 문제(분류 vs. 회귀)에 사용되는지, 그리고 주요 특징(`X`)과 타겟 변수(`Y`)가 무엇인지 명확히 구분할 수 있어야 합니다. (Iris, Wine은 분류, Diabetes는 회귀).
*   ⭐ 각 데이터셋의 샘플 수 (`Iris`: 150, `Wine`: 178, `Diabetes`: 442)도 기억해 두세요.

---

## Slide 5

## 데이터분석 입문 (CSED226) - Histogram (정의 및 사용 시점)

### 핵심 개념
히스토그램은 단일 변수의 분포를 시각화하는 데 사용되는 도구입니다. 데이터를 여러 구간(bin)으로 나누고, 각 구간에 속하는 데이터 포인트의 개수 또는 밀도를 막대 그래프 형태로 나타냅니다.

*   **Bin Edges ($b_k$)**: 데이터를 나누는 구간의 경계값입니다. $b_0, b_1, \dots, b_K$는 $K$개의 빈(bin)을 정의하며, 각 빈은 $(b_{k-1}, b_k]$의 범위를 가집니다.
*   **Count ($count_k$)**: 각 빈에 속하는 데이터 포인트의 개수입니다.
*   **Density ($density_k$)**: 각 빈의 데이터 밀도입니다. 빈의 개수를 총 데이터 수와 빈 너비로 나누어 정규화된 값으로, 서로 다른 그룹의 분포를 비교할 때 유용합니다.
*   **사용 시점**:
    *   데이터의 형태(shape)를 빠르고 직관적으로 파악할 때 사용됩니다. (예: 정규 분포, 왜도, 이상치 등)
    *   그룹 간 분포를 비교할 때, 동일한 빈 경계를 사용하거나 데이터를 정규화(normalize)하여 비교할 수 있습니다.
*   **Motivation**: 단일 표본에서는 `counts`로 시작하지만, 그룹 간 비교나 빈 너비가 다를 때는 `probability` 또는 `density`를 사용하는 것이 더 적절합니다. 필요에 따라 공통된 빈, 누적 보기, 가중치 등을 추가하여 분석을 심화할 수 있습니다.

### 코드/수식 해설
히스토그램의 각 막대 $k$는 다음과 같이 정의됩니다.

*   **데이터 개수 ($count_k$)**:
    각 빈 $(b_{k-1}, b_k]$에 포함되는 데이터 $x_i$의 개수를 나타냅니다.
    $$ count_k = \#\{x_i \mid b_{k-1} < x_i \le b_k\} $$
*   **밀도 ($density_k$)**:
    $k$번째 빈의 밀도는 해당 빈에 속하는 데이터 개수를 전체 데이터 수 $n$과 빈의 너비 $(b_k - b_{k-1})$로 나눈 값입니다. 이는 히스토그램의 전체 면적이 1이 되도록 정규화하는 데 사용됩니다.
    $$ density_k = \frac{count_k}{n(b_k - b_{k-1})} $$

### 구체적 예시
예를 들어, 100명의 학생 키 데이터를 히스토그램으로 나타낸다고 가정해 봅시다.
*   **Bin Edges**: 150cm, 155cm, 160cm, 165cm, 170cm, 175cm, 180cm 등으로 설정할 수 있습니다.
*   **Count**: 만약 160cm 초과 165cm 이하인 학생이 30명이라면, 해당 빈의 `count_k`는 30이 됩니다.
*   **Density**: 전체 학생 수 $n=100$이고, 빈의 너비가 $165 - 160 = 5$cm라면, 해당 빈의 `density_k`는 $\frac{30}{100 \times 5} = 0.06$이 됩니다. 이 밀도는 키가 1cm 증가할 때 해당 범위에 속하는 학생의 비율을 나타냅니다.

**강의 전사에서 언급된 데이터 로딩 예시 (사전 준비 단계):**
강의에서는 본 슬라이드의 내용을 진행하기에 앞서, `iris`, `wine`, `diabetes`와 같은 대표적인 데이터셋을 로드하는 과정을 설명했습니다. 이 데이터들은 향후 히스토그램을 포함한 다양한 시각화 및 분석 예시에서 활용될 것입니다.
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_wine, load_diabetes

# 데이터셋 로드 (as_frame=True로 pandas DataFrame 형태 로드)
iris = load_iris(as_frame=True)
wine = load_wine(as_frame=True)
diabetes = load_diabetes(as_frame=True)

# 데이터를 DataFrame으로 변환 및 target 컬럼에 이름 부여
iris_df = iris.frame
iris_df['species'] = iris.target.map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

wine_df = wine.frame
wine_df['class'] = wine.target.map({0: 'A', 1: 'B', 2: 'C'}) # 예시, 실제 데이터는 0,1,2 일 수 있음

diabetes_df = diabetes.frame
# diabetes는 target이 연속형이므로 별도 매핑이 필요 없을 수 있음
```
위와 같이 준비된 `iris_df`, `wine_df`, `diabetes_df`와 같은 데이터프레임이 주어진 상태에서 이제 히스토그램을 사용해 데이터 분포를 분석하게 됩니다.

### 강의 내용
교수님께서는 슬라이드의 내용이 시작되기 전, 데이터 분석을 위한 필수 라이브러리(`NumPy`, `Pandas`, `Matplotlib`, `Seaborn`)를 임포트하고, `iris`, `wine`, `diabetes`와 같은 예제 데이터셋을 로드하는 과정을 강조하셨습니다. 특히, `load_iris()` 등의 함수를 호출할 때 `as_frame=True` 옵션을 사용하는 것이 중요하다고 언급하셨습니다. 이는 데이터가 NumPy 배열이 아닌 편리한 **Pandas DataFrame 형태로 로드되도록 하기 위함**입니다.

또한, 로드된 데이터셋의 숫자형 타겟(target) 값을 **읽기 쉬운 문자열 레이블로 매핑하여 새로운 컬럼을 생성하는 과정**을 설명하셨습니다. 예를 들어, Iris 데이터셋의 숫자형 타겟(0, 1, 2)을 `setosa`, `versicolor`, `virginica`와 같은 종(species) 이름으로 변환하여 `species` 컬럼을 생성하는 것이 이에 해당합니다. Wine 데이터셋에 대해서도 유사하게 `class` 컬럼을 생성하는 과정을 설명했습니다.

교수님은 이 슬라이드를 시작하며 "**이것이 첫 번째 중요한 플롯, 히스토그램이다.**"라고 명확히 언급하여, 히스토그램이 데이터 분석 입문에서 가장 기본적이고 핵심적인 시각화 도구임을 강조하셨습니다. 즉, 이전의 데이터 로딩 및 전처리 과정은 이러한 시각화 도구를 사용하기 위한 사전 준비 단계입니다.

### 시험 포인트
*   ⭐ **히스토그램의 `count_k`와 `density_k` 공식**: 두 공식을 정확히 이해하고 서술할 수 있어야 합니다. 특히, `density_k`가 `count_k`를 `n`과 빈 너비로 나누어 정규화한다는 점이 중요합니다.
*   ⭐ **히스토그램의 주요 사용 목적**: "빠르고 직관적인 데이터 형태 파악" 및 "정규화 또는 동일 빈 경계를 통한 그룹 간 비교"를 명확히 설명할 수 있어야 합니다.
*   ⭐ **`counts`에서 `density` 또는 `probability`로 전환하는 이유**: 특히 그룹 간 비교나 빈 너비가 다를 때 `density`를 사용하는 이유를 설명할 수 있어야 합니다.
*   ⭐ **데이터 로딩 시 `as_frame=True`의 역할**: Pandas DataFrame 형태로 데이터를 얻는 것의 중요성을 이해해야 합니다.
*   ⭐ **숫자형 타겟을 읽기 쉬운 레이블로 매핑하는 이유**: 데이터 분석의 가독성 및 해석 용이성 측면에서 중요합니다.

---

## Slide 6

### 핵심 개념

*   **히스토그램(Histogram) 정의**: 단변량(univariate) 데이터의 분포를 시각화하는 가장 근본적인 플롯입니다. 데이터를 여러 구간(bin)으로 나누고 각 구간에 속하는 데이터 포인트의 수를 막대 그래프로 표현하여 데이터의 중심, 퍼짐, 대략적인 형태(modality)를 빠르게 파악할 수 있습니다.
*   **빈(Bin)과 카운트(Count)**:
    *   **빈 경계(Bin Edges)**: 데이터 범위를 $V_0$부터 $V_K$까지의 구간으로 나눕니다.
    *   **바 카운트(Bar Count)**: $k$번째 바의 카운트($\text{Count}_k$)는 $B_{k-1}$과 $B_k$ 사이에 속하는 데이터 포인트의 수입니다.
*   **밀도(Density)**:
    *   $k$번째 바의 밀도($\text{Density}_k$)는 카운트를 전체 데이터 포인트 수와 해당 빈의 너비로 나눈 값입니다. 이는 히스토그램의 총 면적이 1이 되도록 정규화하는 데 중요합니다.
*   **히스토그램의 활용**:
    *   데이터의 형태(shape)를 빠르고 직관적으로 파악합니다.
    *   그룹 간 데이터를 비교하는 데 유용하지만, 이때는 빈 경계를 공유하고 y축을 정규화하는 것이 필수적입니다.

### 코드/수식 해설

*   **Matplotlib을 이용한 기본 히스토그램 생성**:
    ```python
    import matplotlib.pyplot as plt
    import pandas as pd # 예시 데이터를 위한 임포트 (슬라이드에는 없지만 일반적으로 필요)

    # 예시 데이터 (슬라이드의 'wine["alcohol"]'을 가정)
    # wine = pd.DataFrame({'alcohol': [12.0, 13.5, 12.8, 14.2, 11.5, 12.9, 13.8, 14.0, 12.5, 11.8]})
    # x = wine["alcohol"]

    # 실제 강의 슬라이드 코드
    # x = wine["alcohol"] # 'wine' 데이터프레임이 있다고 가정
    plt.figure()
    plt.hist(x) # 기본값: 약 10개의 동일 너비 빈, y축은 카운트(counts)
    plt.xlabel("alcohol")
    plt.ylabel("count")
    plt.title("Histogram: defaults")
    plt.show()
    ```
    *   `plt.hist(x)`: 가장 기본적인 히스토그램 함수입니다. `x`는 플롯할 데이터 배열입니다. 기본적으로 약 10개의 동일한 너비의 빈을 사용하며, y축은 각 빈에 해당하는 데이터 포인트의 개수(count)를 나타냅니다.
*   **Seaborn을 이용한 히스토그램 생성 (동일 기능)**:
    ```python
    import seaborn as sns
    # x = wine["alcohol"] # 'wine' 데이터프레임이 있다고 가정
    sns.histplot(x=x, bins=10, stat="count", element="bars", kde=False)
    plt.xlabel("alcohol")
    plt.ylabel("count")
    plt.title("Histogram: defaults")
    plt.show()
    ```
    *   `sns.histplot()`: Seaborn 라이브러리의 히스토그램 함수입니다.
        *   `x`: 플롯할 데이터.
        *   `bins=10`: 빈의 개수를 10개로 명시적으로 설정합니다.
        *   `stat="count"`: y축이 각 빈의 데이터 포인트 개수를 나타내도록 설정합니다. (기본값은 'count', 'frequency', 'density', 'probability' 등이 가능합니다.)
        *   `element="bars"`: 히스토그램을 막대로 표시합니다.
        *   `kde=False`: 커널 밀도 추정(Kernel Density Estimate) 곡선을 표시하지 않습니다.
*   **밀도(Density) 수식**:
    *   $k$번째 바의 밀도는 다음과 같이 정의됩니다:
        $$ \text{Density}_k = \frac{\text{Count}_k}{\text{Total Number of Points} \times \text{Bin Width}_k} $$
    *   이 정규화는 히스토그램의 전체 면적이 1이 되도록 보장하며, 확률 밀도 함수(PDF)와 유사한 해석을 가능하게 합니다.

### 구체적 예시

*   **와인 데이터셋 'alcohol' 분석**: 슬라이드의 코드는 `wine` 데이터프레임의 'alcohol' 컬럼 데이터를 `x` 변수에 할당하여 해당 데이터의 분포를 히스토그램으로 시각화하는 과정을 보여줍니다. 이를 통해 'alcohol' 함량의 대략적인 범위, 가장 흔한 함량 구간 등을 빠르게 파악할 수 있습니다.
*   **사과와 오렌지 비유**: 교수님께서는 서로 다른 두 그룹의 데이터를 히스토그램으로 비교할 때, 빈 경계(bin edges)를 동일하게 설정하고 y축을 밀도(density)로 정규화하지 않으면 마치 '사과와 오렌지를 비교하는 것'과 같다고 비유하셨습니다. 이는 공정한 비교를 위해 통일된 기준이 필요함을 강조하는 예시입니다.

### 강의 내용

*   히스토그램은 단변량 데이터 분석을 위한 가장 근본적인 시각화 방법입니다.
*   히스토그램의 바(bar)는 특정 구간($B_{k-1}$과 $B_k$)에 속하는 데이터 포인트의 수를 나타내는 카운트(count)로 시작합니다.
*   밀도(density)로 변환할 때는 카운트를 전체 데이터 포인트 수와 해당 빈의 너비로 나누어 정규화합니다. 이 정규화 과정을 통해 히스토그램의 총 면적이 1이 되며, 이는 데이터 분포의 확률적 해석에 필수적입니다.
*   히스토그램은 데이터의 대략적인 형태(shape)를 빠르고 직관적으로 파악하는 데 매우 유용합니다 (중심, 퍼짐, 모드 등).
*   여러 그룹의 데이터를 비교할 때 히스토그램을 사용할 수 있지만, 반드시 모든 그룹에 대해 동일한 빈 경계를 사용하고 y축을 정규화(밀도 기준)해야 의미 있는 비교가 가능합니다. 그렇지 않으면 잘못된 결론을 내릴 수 있습니다.
*   데이터 분석 시작 시에는 `simple counts` (기본 카운트)로 시작하여 데이터의 원시적인 분포를 파악하는 것이 중요합니다.

### 시험 포인트

*   ⭐**히스토그램의 목적**: 단변량 데이터의 분포(shape, center, spread, modality)를 빠르고 직관적으로 시각화하는 가장 기본적인 방법임을 이해해야 합니다.
*   ⭐**`count`와 `density`의 차이 및 정규화의 중요성**: `density` 계산 시 `Total Number of Points`와 `Bin Width`로 나누는 이유, 즉 히스토그램의 총 면적이 1이 되도록 정규화하는 과정과 그 의미(확률 밀도 함수와의 연결성)를 설명할 수 있어야 합니다.
*   **Matplotlib `plt.hist()`와 Seaborn `sns.histplot()`의 기본 사용법**: 특히 `bins`, `stat` (count vs density), `kde` 등의 주요 인자를 이해하고 사용할 수 있어야 합니다.
*   ⭐**그룹 간 비교 시 주의사항**: 서로 다른 그룹의 히스토그램을 비교할 때 왜 빈 경계(bin edges)를 통일하고 y축을 정규화(밀도 기준)해야 하는지 그 이유와 중요성을 설명할 수 있어야 합니다.

---

## Slide 7

**핵심 개념**
히스토그램의 '빈(bin)' 너비를 적절하게 설정하는 것은 데이터 분포의 진정한 모습을 파악하는 데 매우 중요합니다. 기본적으로 히스토그램은 데이터의 개수를 y축에 표시하지만, 서로 다른 크기의 그룹이나 다른 빈 너비를 가진 히스토그램을 비교할 때는 **확률(probability)** 또는 **밀도(density)** 개념을 사용해야 공정한 비교가 가능합니다. 빈 너비가 너무 넓으면 데이터의 중요한 특징(예: 여러 개의 봉우리, 즉 모드)이 가려질 수 있고, 너무 좁으면 불필요한 노이즈로 인해 패턴이 왜곡될 수 있습니다. 이를 해결하기 위해 데이터에 적응적인 빈 너비를 결정하는 알고리즘 중 하나가 **Freedman-Diaconis Rule**입니다.

**코드/수식 해설**

*   **기본 히스토그램 그리기**:
    ```python
    x = wine["alcohol"]
    plt.hist(x) # 기본 히스토그램, 약 10개의 동일 너비 빈 사용
    plt.xlabel("alcohol")
    plt.ylabel("count") # y축에 raw counts 표시
    plt.show()
    ```
    이 코드는 `wine` 데이터셋의 'alcohol' 컬럼에 대한 가장 기본적인 히스토그램을 생성합니다. `plt.hist()` 함수는 기본적으로 약 10개의 동일한 너비의 빈(bin)을 사용하며, y축에는 각 빈에 해당하는 데이터의 **개수(count)**를 표시합니다. `xlabel`과 `ylabel`은 그래프의 가독성을 높이기 위해 축에 이름을 부여합니다.

*   **Freedman-Diaconis Rule 적용**:
    ```python
    x = wine["alcohol"]
    plt.hist(x, bins="fd") # data-adaptive; reduces oversmoothing/undersmoothing risk
    plt.xlabel("alcohol"); plt.ylabel("count")
    plt.show()
    ```
    `bins="fd"` 옵션은 Freedman-Diaconis Rule을 사용하여 데이터에 최적화된 빈 너비를 자동으로 계산합니다. 이 방법은 데이터의 과도한 평활화(oversmoothing) 또는 부족한 평활화(undersmoothing) 위험을 줄여줍니다.

*   **Seaborn의 `histplot` 사용**:
    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # ... (x = wine["alcohol"] 부분은 동일) ...
    
    ax = sns.histplot(x=x, bins="fd", stat="count", element="bars",
                      kde=False, discrete=False)
    ax.set(xlabel="alcohol", ylabel="count", title="Histogram: bins='fd'")
    plt.show()
    ```
    `seaborn` 라이브러리의 `histplot` 함수도 히스토그램을 그릴 수 있으며, `bins="fd"` 옵션을 통해 Freedman-Diaconis Rule을 적용할 수 있습니다. `stat="count"`는 y축이 개수를 나타내도록 하고, `element="bars"`는 막대 형태를 유지합니다. `kde=False`는 커널 밀도 추정(Kernel Density Estimation) 그래프를 함께 그리지 않도록 합니다. `ax.set()`을 사용하여 x, y축 레이블 및 제목을 설정합니다.

*   **Freedman-Diaconis Rule 수식**:
    Freedman-Diaconis Rule에 따른 빈 너비 $h$는 다음과 같이 계산됩니다.
    $$
    h = 2 \frac{IQR}{n^{1/3}}
    $$
    여기서 $IQR$은 데이터의 사분위수 범위(Interquartile Range, $Q_3 - Q_1$)이며, $n$은 데이터 포인트의 총 개수입니다.

**구체적 예시**
와인 데이터셋에서 'alcohol' 함량 분포를 히스토그램으로 시각화하는 상황을 가정해 봅시다. 만약 기본 10개 빈으로 그렸을 때, 알코올 함량에 실제로는 뚜렷한 두 그룹(예: 저알코올 와인과 고알코올 와인)이 존재함에도 불구하고 하나의 넓은 봉우리로 나타날 수 있습니다. 하지만 `bins="fd"`를 사용하여 Freedman-Diaconis Rule을 적용하면, 데이터의 특성에 맞춰 빈 너비가 조절되어 두 개의 봉우리가 명확하게 드러나 데이터의 '모드(mode)'를 숨기거나 노이즈를 추가하지 않고 실제 분포를 더 정확하게 보여줄 수 있습니다.

**강의 내용**
*   **공정한 비교를 위한 전환**: 서로 다른 크기의 그룹이나 다른 빈 너비의 히스토그램을 비교할 때는 단순히 `count`가 아닌 `probability` 또는 `density`로 전환하여 공정하게 비교해야 합니다.
*   **`plt.hist`의 기본 동작**: `plt.hist()` 함수는 기본적으로 약 10개의 동일한 너비의 빈을 생성하며, y축에는 각 빈에 해당하는 **원시 개수(row counts)**를 표시합니다.
*   **레이블의 중요성**: `xlabel`, `ylabel`을 사용하여 그래프에 명확한 레이블을 추가하는 것이 중요합니다.
*   **도구 사용의 유연성**: `matplotlib`의 `plt.hist` 대신 `seaborn`의 `histplot`을 사용할 수도 있습니다. 하지만 특정 함수 이름을 전부 외울 필요는 없으며, 시각화의 기본 개념을 이해하고 필요할 때 `ChatGPT`와 같은 도구를 활용하여 코드를 찾아 사용하는 것이 더 중요하다고 강조하셨습니다.
*   **기본 빈 개수의 문제점**: 기본 빈 개수는 데이터의 실제 모드(mode)를 숨기거나 불필요한 노이즈를 추가할 수 있습니다.

**시험 포인트**
*   ⭐ **히스토그램 빈 너비 선택의 중요성**: 부적절한 빈 너비가 데이터 분포 해석에 미치는 영향(모드 숨김, 노이즈 추가).
*   ⭐ **Freedman-Diaconis Rule의 역할**: 데이터에 적응적인(data-adaptive) 빈 너비를 제공하여 과도한 평활화(oversmoothing)나 부족한 평활화(undersmoothing)를 줄이는 방법.
*   ⭐ **다른 크기의 그룹 또는 빈 너비 비교 시 필요한 접근**: `count` 대신 `probability` 또는 `density` 개념을 사용해야 하는 이유.
*   `plt.hist`와 `sns.histplot`의 기본적인 사용법 및 `bins="fd"` 옵션의 의미. (함수 자체를 암기하기보다 그 개념을 이해하는 것이 중요)

---

## Slide 8

**핵심 개념**:
- **히스토그램의 Y축 스케일: Probability vs Density**
    - `Probability` (확률): 각 막대의 높이가 해당 구간에 속하는 데이터의 **비율**을 나타냅니다. 모든 막대 높이의 합은 $1$입니다. 주로 빈(bin) 너비가 동일할 때 각 빈의 상대적 빈도를 빠르게 비교하는 데 사용됩니다.
    - `Density` (밀도): 각 막대의 높이가 해당 구간에서의 **확률 밀도**를 나타냅니다. 모든 막대 아래의 **면적 합**이 $1$입니다. 빈 너비가 일정하지 않을 때도 분포의 모양을 강건하게 비교할 수 있으며, 확률 밀도 함수(PDF)와 직접적으로 비교하기에 적합합니다.
- **FD (Friedman-Diaconis) Rule**: 데이터의 특성을 기반으로 히스토그램의 최적 빈(bin) 개수 또는 너비를 자동으로 결정하는 데이터 적응형 규칙입니다. 이 규칙은 과도한 스무딩(over-smoothing)이나 부족한 스무딩(under-smoothing)으로 인해 데이터의 중요한 특징이 가려지거나 불필요한 노이즈가 추가되는 것을 방지합니다.

**코드/수식 해설**:

1.  **Matplotlib에서 밀도 히스토그램 그리기**:
    ```python
    plt.hist(x, bins="fd", density=True) # y = density (area = 1)
    ```
    - `x`: 히스토그램을 그릴 데이터 배열입니다.
    - `bins="fd"`: Friedman-Diaconis 규칙에 따라 히스토그램의 빈(bin) 개수를 자동으로 설정합니다. 이를 통해 데이터의 분포를 가장 잘 나타낼 수 있는 빈 너비를 찾습니다.
    - `density=True`: 히스토그램의 Y축을 확률 밀도로 설정합니다. 이 경우, 모든 막대 아래의 총 면적은 $1$이 됩니다.

2.  **Seaborn에서 확률 및 밀도 히스토그램 그리기**:
    ```python
    sns.histplot(x=x, stat="probability") # bar heights sum to 1
    sns.histplot(x=x, stat="density") # area under bars = 1
    ```
    - `sns.histplot()`: Seaborn 라이브러리의 히스토그램 플로팅 함수입니다.
    - `x=x`: 히스토그램을 그릴 데이터입니다.
    - `stat="probability"`: Y축을 확률로 설정합니다. 각 막대의 높이는 해당 빈에 속하는 데이터의 비율이며, 모든 막대 높이의 합은 $1$이 됩니다.
    - `stat="density"`: Y축을 밀도로 설정합니다. `matplotlib`의 `density=True`와 동일하게, 모든 막대 아래 면적의 합은 $1$이 됩니다. `sns.histplot`에서도 `bins="fd"` 옵션을 사용할 수 있습니다.

**구체적 예시**:
- **사용 사례**: 두 개 이상의 그룹에 대한 데이터 분포의 **모양(shape)**을 서로 비교하거나, 특정 이론적 확률 밀도 함수(예: 정규 분포, 지수 분포의 PDF)를 실제 데이터 히스토그램 위에 겹쳐서 비교하고자 할 때 `Density` 스케일을 사용하면 매우 유용합니다. 예를 들어, 서로 다른 반 학생들의 시험 점수 분포가 어떻게 다른지 비교할 때 `Density` 히스토그램을 사용하면, 학생 수가 달라도 분포의 상대적인 모양을 효과적으로 비교할 수 있습니다.
- 반면, 특정 빈에 몇 개의 데이터가 포함되어 있는지 또는 전체 데이터 중 몇 퍼센트가 해당 빈에 속하는지 빠르게 파악할 때는 `Probability` 스케일이 직관적일 수 있습니다.

**강의 내용**:
- 교수님은 기본 히스토그램 설정(디폴트 빈 개수)이 데이터의 중요한 특징(예: 모드)을 가리거나 존재하지 않는 노이즈를 추가할 수 있기 때문에, `bins="fd"`와 같은 데이터 적응형 규칙을 사용하는 것이 더 나은 접근 방식임을 강조했습니다.
- `FD rule`은 `Friedman and Diaconis rule`의 약자이며, 이 규칙을 사용하면 과도한 스무딩(over-smoothing) 또는 부족한 스무딩(under-smoothing)의 위험을 줄여 히스토그램이 데이터의 실제 분포를 더 정확하게 반영할 수 있다고 설명했습니다.
- Matplotlib의 `plt.hist`와 마찬가지로 Seaborn의 `sns.histplot`에서도 `bins="fd"` 옵션을 사용하여 Friedman-Diaconis 규칙을 적용할 수 있다고 언급했습니다.
- `FD rule`의 세부적인 수학적 내용은 이 강의에서 다루지 않는다고 설명했습니다.

**시험 포인트**:
- ⭐ **`Probability`와 `Density` Y축 스케일의 핵심 차이점과 적절한 사용 시나리오**를 명확히 이해해야 합니다.
    - `Probability`는 막대 높이의 합이 $1$이고, `Density`는 막대 아래 면적의 합이 $1$이라는 점을 기억해야 합니다.
    - 분포의 모양 비교 또는 PDF와 겹쳐 그릴 때는 `Density`를 사용합니다.
- ⭐ **`bins="fd"` 옵션의 중요성**: 이 옵션이 히스토그램의 빈 개수를 데이터에 맞게 최적화하여 분포의 특징을 더 잘 드러내고, 과도한 스무딩이나 부족한 스무딩을 방지하는 역할을 한다는 것을 알아야 합니다.

---

## Slide 9

## 데이터분석 입문 (CSED226) 마크다운 노트: Extend 3: Fair Group Comparison

### 핵심 개념

이 슬라이드는 여러 그룹의 분포를 공정하게 비교하는 방법에 대해 다룹니다. 특히, `Shared bins` (공유 빈)과 `Density normalization` (밀도 정규화) 개념을 통해 그룹 간 비교 시 발생할 수 있는 오해를 줄이는 방법을 제시합니다.

1.  **Shared bins (공유 빈)**
    *   여러 그룹의 히스토그램을 비교할 때, 모든 그룹에 대해 **동일한 빈 경계**($B = \{b_0, \ldots, b_K\}$)를 사용합니다.
    *   이는 전체(pooled) 데이터를 기준으로 빈 경계를 먼저 계산한 후, 각 그룹의 데이터에 적용하여 일관된 비교 기준을 마련합니다.
    *   **목적**: 그룹별로 빈 경계가 다르면 히스토그램의 모양이 달라져 그룹 간 비교가 어려워지기 때문에, 빈 경계를 고정하여 비교의 공정성을 확보합니다.

2.  **Density normalization (밀도 정규화)**
    *   각 그룹의 히스토그램이 그리는 **전체 면적이 1**이 되도록 정규화하는 방법입니다.
    *   **목적**: 그룹별 표본 크기($n_g$)가 다를 경우, 단순히 빈에 속하는 데이터의 `count` (빈도)만으로는 분포의 실제 모양(shape)을 비교하기 어렵습니다. 밀도 정규화를 통해 표본 크기에 상관없이 분포의 상대적인 모양을 공정하게 비교할 수 있습니다.

3.  **Why (사용 이유)**
    *   서로 다른 빈 경계를 사용하거나 단순히 원시 `counts` (빈도)를 사용하면, 데이터의 실제 분포 모양 차이를 파악하기 어렵고, 빈을 나누는 방식이나 표본 크기 차이로 인한 착시 현상(artifacts)이 발생할 수 있기 때문입니다.

### 코드/수식 해설

**Density Normalization 수식:**

$$
\text{density}_{g,k} = \frac{\#\{x_i \in g : b_{k-1} < x_i \le b_k\}}{n_g (b_k - b_{k-1})}
$$

*   $\text{density}_{g,k}$: 그룹 $g$의 $k$번째 빈에 대한 밀도 값입니다.
*   $\#\{x_i \in g : b_{k-1} < x_i \le b_k\}$: 그룹 $g$에서 $k$번째 빈 ($b_{k-1}$부터 $b_k$까지)에 속하는 데이터 포인트의 개수 (빈도)입니다.
*   $n_g$: 그룹 $g$의 전체 데이터 포인트 수 (표본 크기)입니다.
*   $(b_k - b_{k-1})$: $k$번째 빈의 너비(width)입니다.

이 수식은 특정 빈의 빈도를 해당 그룹의 전체 데이터 수와 빈 너비로 나누어 밀도를 계산합니다. 이 방식으로 계산된 밀도를 통해 각 막대의 높이를 결정하면, 모든 막대의 전체 면적 합이 1이 됩니다.

**Python 라이브러리에서의 활용:**
matplotlib이나 seaborn 같은 라이브러리에서 히스토그램을 그릴 때 `density=True` 옵션을 설정하면 위 수식에 따라 밀도 정규화된 히스토그램을 얻을 수 있습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 예시 데이터 (실제 그룹 데이터 대신 가상의 데이터)
group_a_data = np.random.normal(loc=13.0, scale=0.8, size=200)
group_b_data = np.random.normal(loc=12.0, scale=0.5, size=100)

# 1. 공유 빈 (Shared bins) 계산
# 전체 데이터를 합쳐서 빈 경계 계산 (예: Freedman-Diaconis rule 등)
# 여기서는 간단하게 고정된 빈을 사용
bins = np.linspace(10.0, 15.0, 10) # 10.0부터 15.0까지 10개 빈 경계

plt.figure(figsize=(8, 5))
plt.hist(group_a_data, bins=bins, density=True, alpha=0.5, label='Group A')
plt.hist(group_b_data, bins=bins, density=True, alpha=0.5, label='Group B')
plt.title('Histogram Comparison with Shared Bins and Density Normalization')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()
```

### 구체적 예시

슬라이드 하단의 "Histogram by class (shared bins)" 그래프가 좋은 예시입니다. 'alcohol'이라는 특징(feature)에 대해 A, B, C 세 그룹의 분포를 비교하고 있습니다.
*   **공유 빈**: X축(alcohol 값)의 빈 경계가 A, B, C 세 그룹 모두에게 동일하게 적용되었습니다.
*   **밀도 정규화**: Y축이 'density'로 표시되어 있으며, 각 그룹(A, B, C)의 히스토그램 면적 합이 1이 되도록 정규화되어 있습니다. 이를 통해 각 그룹의 표본 크기가 다르더라도, 알코올 함량 분포의 **모양**을 직접적으로 비교할 수 있습니다. 예를 들어, B 그룹은 12.0~13.0 구간에 밀도가 집중되어 있고, A 그룹은 13.5~14.5 구간에 밀도가 높은 것을 확인할 수 있습니다.

### 강의 내용

*   **빈 너비 결정 규칙**: 교수님은 `Friedman-Daikonis rule`과 같은 빈 너비 결정 규칙의 중요성을 언급하며, 이 규칙들이 과도한 스무딩(over-smoothing)이나 부족한 스무딩(under-smoothing)을 방지한다고 강조했습니다. 상세 설명은 Wikipedia를 참조할 것을 권장했습니다.
*   **`probability` vs `density` 정규화**:
    *   **`probability` 정규화**: 히스토그램의 **모든 막대 높이의 합이 1**이 되도록 정규화하는 방식입니다. (예: `plt.hist(..., weights=np.ones_like(data) / len(data))`)
    *   **`density` 정규화**: 히스토그램의 **모든 막대 면적의 합이 1**이 되도록 정규화하는 방식입니다. (예: `plt.hist(..., density=True)`)
    *   교수님은 **빈 너비가 모두 동일한 경우**에는 `probability` 정규화로도 빠른 확인이 가능하다고 언급했습니다. 하지만 빈 너비가 다를 수 있는 일반적인 상황에서는 `density` 정규화가 분포의 모양을 공정하게 비교하는 데 필수적임을 강조했습니다.

### 시험 포인트

*   ⭐ **공정한 그룹 비교를 위해 `shared bins`와 `density normalization`을 사용하는 이유**를 설명할 수 있어야 합니다. (표본 크기 차이 극복, 빈 경계 일관성 유지)
*   ⭐ `probability` 정규화와 `density` 정규화의 **차이점**을 명확히 이해하고 설명할 수 있어야 합니다. 특히, 무엇의 합이 1이 되는지 (`height` vs `area`) 구분할 줄 알아야 합니다.
*   ⭐ `density_{g,k}` 수식에서 각 항이 무엇을 의미하는지, 그리고 왜 이러한 방식으로 계산하는지 이해하는 것이 중요합니다.
*   `Friedman-Daikonis rule`과 같은 빈 너비 결정 규칙이 히스토그램 시각화에 어떤 영향을 미치는지 개념적으로 이해하고 있으면 좋습니다.

---

## Slide 10

**핵심 개념**:
이 슬라이드는 여러 그룹 간의 분포를 비교하기 위해 **공유 빈(Shared Bins)**과 **밀도 정규화(Density Normalization)**를 활용한 히스토그램 시각화 방법을 다룹니다. 특히, `matplotlib`과 `seaborn` 라이브러리를 사용하여 밀도 히스토그램을 그리는 방법을 보여줍니다.

**코드/수식 해설**:

1.  **공유 빈 계산 (Shared Bins Computation)**
    ```python
    bins = np.histogram_bin_edges(wine[xcol], bins="fd")
    ```
    *   `np.histogram_bin_edges()`: `numpy` 함수를 사용하여 히스토그램의 빈(bin) 경계를 계산합니다.
    *   `wine[xcol]`: 전체 데이터셋(`wine`)에서 `'alcohol'` 컬럼의 값을 사용합니다.
    *   `bins="fd"`: 빈 너비를 결정하는 알고리즘으로 Freedman-Diaconis 규칙을 사용합니다. 이는 이상치에 덜 민감하고 데이터에 기반하여 최적의 빈 너비를 찾아줍니다. 이렇게 계산된 `bins`는 모든 그룹에 동일하게 적용됩니다.

2.  **그룹별 밀도 히스토그램 플로팅 (Per-Group Density Histogram Plotting)**
    ```python
    for g, sub in wine.groupby("class"):
        plt.hist(sub[xcol], bins=bins, density=True, alpha=0.45, label=g)
    ```
    *   `wine.groupby("class")`: `wine` 데이터를 `class` 컬럼을 기준으로 그룹화합니다. 각 그룹(`g`)과 해당 서브 데이터(`sub`)에 대해 반복합니다.
    *   `plt.hist()`: 각 그룹의 데이터를 공유 빈(`bins`)을 사용하여 히스토그램으로 그립니다.
    *   `density=True`: 이 인자가 중요하며, 히스토그램의 전체 면적이 `1`이 되도록 정규화합니다. 이는 y축이 확률 밀도 함수(Probability Density Function, PDF)의 근사값이 되도록 합니다.
    *   `alpha=0.45`: 히스토그램 막대의 투명도를 설정하여 여러 그룹의 분포가 겹쳐 보일 때 각 그룹을 구분하고 겹치는 부분을 시각화하기 쉽게 합니다.
    *   `label=g`: 각 그룹의 라벨을 설정하여 범례에 표시합니다.

3.  **Seaborn을 이용한 간결한 표현 (Seaborn Concise Representation)**
    ```python
    sns.histplot(data=wine, x=xcol, hue="class", bins=bins, stat="density", common_bins=True)
    ```
    *   `sns.histplot()`: `seaborn` 라이브러리의 히스토그램 함수는 `matplotlib`보다 훨씬 간결하게 여러 그룹의 히스토그램을 그릴 수 있습니다.
    *   `hue="class"`: `class` 컬럼을 기준으로 그룹을 나누고 색상으로 구분합니다.
    *   `stat="density"`: `matplotlib`의 `density=True`와 동일하게 전체 면적을 1로 정규화합니다. `stat="probability"`를 선택할 경우, 각 빈의 높이가 확률이 되며, 빈의 너비가 다를 경우 전체 면적이 1이 되지 않을 수 있습니다.
    *   `common_bins=True`: 모든 그룹에 대해 동일한 빈 경계를 사용하도록 합니다.

**구체적 예시**:
와인(wine) 데이터셋에서 "알코올(alcohol)" 함량 분포를 와인의 "클래스(class)"별로 비교하는 예시입니다. 여러 클래스의 알코올 분포가 하나의 그래프에 밀도 히스토그램으로 겹쳐 표시됩니다.
*   **해석**: 겹치는 부분이 어두워지는 것은 해당 범위에서 여러 그룹이 공통적으로 많은 데이터를 가진다는 것을 의미합니다. 특정 그룹의 막대가 다른 그룹보다 튀어나와("bulge") 보이는 부분은 해당 범위에서 그 그룹의 상대적인 지배력(dominance)이 높다는 것을 나타냅니다. 예를 들어, A 클래스가 B 클래스보다 낮은 알코올 함량 범위에서 더 높은 밀도를 보인다면, A 클래스 와인에 낮은 알코올 함량인 경우가 더 많다는 것을 알 수 있습니다.

**강의 내용**:
교수님은 **밀도 히스토그램(density histogram)**의 중요성을 여러 번 강조하셨습니다.
*   **확률 히스토그램 vs. 밀도 히스토그램**:
    *   확률 히스토그램(probability histogram)은 각 막대의 높이가 해당 빈의 데이터 발생 확률을 나타냅니다. 모든 막대 높이의 합이 1입니다. (빈 너비가 동일할 경우 면적도 1).
    *   밀도 히스토그램(density histogram)은 각 막대의 면적이 해당 빈의 확률을 나타내며, 전체 히스토그램의 면적이 1입니다. 따라서 y축은 확률 밀도 값을 의미합니다. 빈의 너비가 다를 경우, 밀도 히스토그램은 확률 히스토그램보다 분포의 형태를 더 정확하게 반영합니다.
*   **밀도 히스토그램 사용을 강력히 권장하는 경우**:
    *   ⭐ **빈 너비가 같지 않을 때 (unequal bin widths)**: 빈 너비가 다르면 확률 히스토그램은 분포의 실제 형태를 왜곡할 수 있습니다. 밀도 히스토그램은 면적을 통해 확률을 표현하므로 이러한 왜곡을 방지합니다.
    *   **이론적 확률 밀도 함수(PDF)와 비교할 때**: 히스토그램을 정규분포 곡선 등 이론적인 PDF와 비교하고자 할 때, 밀도 히스토그램을 사용해야 합니다. 밀도 히스토그램의 y축이 PDF의 y축과 직접 비교 가능한 밀도 값을 나타내기 때문입니다.
    *   **다른 그룹 간의 분포 형태를 비교할 때**: 슬라이드의 예시처럼 여러 그룹의 분포를 겹쳐서 비교할 때, 각 그룹의 분포 형태를 정확히 파악하고 상대적인 밀도를 비교하기 위해 밀도 히스토그램이 필수적입니다.
    *   **이론적 밀도 곡선을 오버레이할 때**: 히스토그램 위에 이론적인 밀도 곡선을 그릴 때도 밀도 히스토그램을 사용해야 합니다.
*   **Matplotlib과 Seaborn의 파라미터**:
    *   `matplotlib.pyplot.hist()`: `density=True`
    *   `seaborn.histplot()`: `stat="density"` (또는 `stat="probability"` 선택 가능)
*   **히스토그램의 한계**: 히스토그램은 기본적으로 단변량(univariate) 분석을 위한 도구라고 언급하셨습니다.

**시험 포인트**:
*   ⭐ **밀도 히스토그램(`density=True` 또는 `stat="density"`)을 사용해야 하는 주요 상황 3가지 이상을 설명하시오.** (정답: 빈 너비가 같지 않을 때, 이론적 PDF와 비교할 때, 다른 그룹 간 분포 형태를 비교할 때)
*   ⭐ **확률 히스토그램과 밀도 히스토그램의 차이점을 설명하고, 왜 밀도 히스토그램이 더 견고한(robust) 방법으로 간주되는지 서술하시오.** (핵심: 밀도 히스토그램은 전체 면적이 1이며, 빈 너비가 달라도 분포 형태를 정확히 반영)
*   겹쳐진 밀도 히스토그램에서 '어두워진 겹침 영역'과 '그룹의 튀어나온 부분(bulge)'이 각각 무엇을 의미하는지 설명할 수 있어야 합니다.

---

## Slide 11

- **핵심 개념**:
    *   **누적 히스토그램 (Cumulative Histogram)**: 데이터 분포의 누적 밀도를 시각화하는 방법입니다. 각 빈(bin)은 해당 빈까지의 모든 데이터 포인트의 누적 비율 또는 밀도를 나타냅니다. 데이터의 특정 값 이하가 전체에서 차지하는 비율을 파악하는 데 유용합니다.
    *   **그룹 비교를 위한 히스토그램 사용 원칙**: 여러 그룹의 분포를 공정하게 비교하기 위해서는 두 가지 핵심 원칙을 준수해야 합니다.
        1.  **공유된 빈 (Shared Bins)**: 비교하려는 모든 그룹의 데이터를 통합하여 하나의 bin 경계 세트를 계산하고, 이를 모든 그룹의 히스토그램에 동일하게 적용해야 합니다.
        2.  **밀도 정규화 (Density Normalization)**: 각 그룹의 히스토그램 전체 면적이 1이 되도록 정규화하여, 표본 크기의 차이에 관계없이 분포의 *형태*를 공정하게 비교할 수 있도록 합니다.

- **코드/수식 해설**:
    *   **`matplotlib.pyplot.hist` 코드**:
        ```python
        plt.hist(x, bins="fd", density=True, cumulative=True, histtype="step")
        plt.xlabel("alcohol"); plt.ylabel("cumulative density")
        ```
        *   `x`: 히스토그램을 그릴 데이터 배열입니다.
        *   `bins="fd"`: 'Freedman-Diaconis rule'을 사용하여 bin의 개수를 자동으로 결정합니다. 이는 데이터의 분포에 따라 적절한 bin 너비를 찾아주는 방법 중 하나입니다.
        *   `density=True`: 히스토그램 막대의 높이를 확률 밀도(Probability Density)로 정규화합니다. 이 경우, 모든 막대의 면적 합이 1이 됩니다. 강의에서 강조하는 '밀도 정규화'에 해당합니다.
        *   `cumulative=True`: 누적 히스토그램을 생성합니다. 각 막대의 높이는 해당 빈까지의 데이터의 누적 비율을 나타냅니다. 그래프는 `0`에서 `1`까지의 `cumulative density`를 가집니다.
        *   `histtype="step"`: 히스토그램을 계단형 그래프로 표시합니다. 이는 누적 히스토그램을 시각화할 때 일반적으로 사용되는 형태입니다.
    *   **밀도 정규화 수식**:
        그룹 $G$의 빈 $K$에 대한 밀도 `$\text{Density}_{G,K}$`는 다음과 같이 계산됩니다.
        $$ \text{Density}_{G,K} = \frac{\text{Count}_{G,K}}{N_G \times \text{BinWidth}} $$
        여기서,
        *   `$\text{Count}_{G,K}$`: 그룹 $G$에서 빈 $K$에 속하는 데이터 포인트 수.
        *   `$N_G$`: 그룹 $G$의 전체 데이터 포인트 수 (표본 크기).
        *   `$\text{BinWidth}$`: 각 빈의 너비.
        이 수식을 통해 각 그룹의 히스토그램 전체 면적이 1이 되어, 표본 크기에 관계없이 분포의 *형태*를 공정하게 비교할 수 있게 됩니다.

- **구체적 예시**:
    *   **누적 히스토그램**: 와인 데이터셋에서 'alcohol' 도수를 누적 히스토그램으로 그렸을 때, 그래프에서 13.5% 지점의 'cumulative density'가 0.8이라면, 이는 전체 와인 중 80%가 알코올 도수 13.5% 이하임을 의미합니다.
    *   **그룹 비교**: 남성과 여성 두 그룹의 학점(GPA) 분포를 비교할 때, 남성 표본 수가 여성보다 훨씬 많다고 가정해봅시다. 이때 공유된 빈을 사용하고 `density=True`로 밀도를 정규화하면, 남성 그룹의 막대가 여성 그룹보다 단순히 높게 그려지는 것을 방지하고, 성별에 따른 학점 분포의 *상대적인 모양*을 공정하게 비교하여 어떤 성별이 더 높은 학점에 집중되어 있는지 등을 판단할 수 있습니다.

- **강의 내용**:
    *   교수님은 여러 그룹 간의 분포를 비교할 때 히스토그램을 사용하는 '적절한 방법'에 대해 강조하셨습니다.
    *   **공정한 비교를 위한 두 가지 핵심 개념**:
        1.  **공유된 빈(Shared Bins)**: 여러 히스토그램을 겹쳐서 비교할 때, 모든 그룹의 데이터를 한데 모아 빈(bin) 경계를 한 번만 계산하고, 이 경계를 모든 그룹에 똑같이 적용해야 합니다. 이를 통해 같은 데이터 범위가 같은 위치에 표현되어 비교가 유의미해집니다.
        2.  **밀도 정규화(Density Normalization)**: `density=True` 옵션을 사용하여 각 그룹 히스토그램의 전체 면적이 1이 되도록 정규화해야 합니다. 이를 통해 각 그룹의 표본 크기(`$N_G$`)가 달라도 분포의 상대적인 모양을 왜곡 없이 비교할 수 있습니다.
    *   누적 히스토그램은 **ECDF(Empirical Cumulative Distribution Function)**로 가는 다리 역할을 합니다. ECDF는 bin에 의존하지 않는(bin-free) 누적 분포를 제공하며, Quantiles(백분위수) 및 stochastic dominance(확률적 우위)와 같은 개념을 이해하는 데 중요한 시각화 도구입니다.

- **시험 포인트**:
    *   ⭐ 여러 그룹의 히스토그램을 비교할 때, 공정한 비교를 위한 **두 가지 핵심 개념 (공유된 빈, 밀도 정규화)**을 설명하고 실제 코드(`plt.hist`의 `bins`와 `density` 파라미터)에 어떻게 적용하는지 이해하는 것이 매우 중요합니다.
    *   ⭐ `matplotlib.pyplot.hist` 함수에서 `density=True`와 `cumulative=True` 파라미터가 각각 어떤 의미를 가지며, 시각화 결과에 어떻게 영향을 미치는지 정확히 알고 있어야 합니다. 특히 `density=True`가 '각 그룹의 히스토그램을 통합적으로 비교 가능하게 만드는' 이유를 수식을 통해 설명할 수 있어야 합니다.
    *   ⭐ 누적 히스토그램이 ECDF와 어떤 관계를 가지는지, 그리고 Quantiles(백분위수)와 stochastic dominance(확률적 우위) 개념과 어떻게 연결되는지 설명할 수 있어야 합니다.

---

## Slide 12

**핵심 개념**
*   **경험적 누적 분포 함수 (ECDF; Empirical Cumulative Distribution Function)**: 주어진 데이터 셋에서 특정 값 $x$보다 작거나 같은 데이터 포인트의 비율을 나타내는 함수입니다. 이론적인 누적 분포 함수(CDF)의 비모수적 추정치로, 데이터의 분포를 시각화하고 비교하는 데 사용됩니다.
*   **Bin-free**: ECDF는 히스토그램처럼 구간(bin) 너비나 경계를 임의로 설정할 필요가 없습니다. 이로 인해 bin 선택에 따른 인위적인 왜곡(histogram artifacts)을 피할 수 있어 데이터의 실제 분포를 더욱 객관적으로 반영합니다.
*   **견고한 비교 (Robust comparison)**: 샘플 크기($n$)가 서로 다른 두 분포를 직접적으로 비교하는 데 매우 효과적입니다. 비율을 기반으로 하므로, 샘플 크기 차이에 따른 시각적 오해를 줄여줍니다.
*   **한눈에 파악하는 분위수 (Quantiles at a glance)**: ECDF 그래프에서 특정 y축 값에 해당하는 x축 값을 찾아 중앙값($\hat{F}(x) = 0.5$), 90번째 백분위수($\hat{F}(x) = 0.9$) 등 다양한 분위수를 쉽게 파악할 수 있습니다.

**코드/수식 해설**

*   **ECDF 수식**:
    ECDF $\hat{F}(x)$는 다음과 같이 정의됩니다:
    $$ \hat{F}(x) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}\{x_i \le x\}, \quad 0 \le \hat{F}(x) \le 1. $$
    *   `$\hat{F}(x)$`: $x$ 값에서의 경험적 누적 분포 함수의 값입니다.
    *   `$n$`: 관측된 총 데이터 포인트 수입니다.
    *   `$x_i$`: $i$번째 데이터 포인트의 값입니다.
    *   `$\mathbf{1}\{x_i \le x\}$`: 지시 함수(indicator function)입니다. 만약 $x_i$가 $x$보다 작거나 같으면 1을, 그렇지 않으면 0을 반환합니다.
    *   이 수식은 주어진 $x$보다 작거나 같은 데이터 포인트의 개수를 전체 데이터 포인트 수로 나누어 $x$까지의 누적 비율을 계산합니다.

*   **히스토그램 공통 Bin 및 정규화 예시 (강의 음성 기반)**:
    교수님께서 언급하신 "공정한 비교(fair comparison)"를 위한 히스토그램 코드 예시는 여러 그룹의 분포를 비교할 때, 모든 그룹에 대해 동일한 bin 경계를 사용하고 밀도(`density=True`)로 정규화하며 투명도(`alpha`)를 조절하여 겹쳐 그리는 방식입니다. ECDF가 Bin-free한 솔루션을 제공하기 이전에 히스토그램의 한계를 보완하는 방법으로 사용될 수 있습니다.

    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd # pandas DataFrame 사용 가정

    # 예시 데이터 생성 (실제 와인 데이터프레임 가정)
    data = {'alcohol': np.concatenate([np.random.normal(13, 0.5, 50),
                                        np.random.normal(12, 0.7, 70),
                                        np.random.normal(14, 0.4, 60)]),
            'class': [1]*50 + [2]*70 + [3]*60}
    wine_df = pd.DataFrame(data)

    # 1단계: 전체 데이터에서 공통 bin 경계 계산 (FD rule 사용)
    # 교수님께서 언급하신 'MPHistorium_bin_edges'는 특정 라이브러리 함수이거나 가칭일 수 있으나,
    # 여기서는 numpy의 'fd' (Freedman-Diaconis) 규칙을 활용하는 예시를 사용합니다.
    pooled_alcohol = wine_df['alcohol']
    common_bins = np.histogram_bin_edges(pooled_alcohol, bins='fd')

    # 2단계: 각 클래스 그룹별로 히스토그램을 공통 bin으로 그리고 정규화(density=True)
    plt.figure(figsize=(10, 6))
    for class_name, group_data in wine_df.groupby('class'):
        plt.hist(group_data['alcohol'], bins=common_bins,
                 density=True,     # 면적 합이 1이 되도록 정규화
                 alpha=0.5,        # 투명도 설정으로 겹쳐진 부분 시각화
                 label=f'Class {class_name} Alcohol')

    plt.xlabel('Alcohol Content')
    plt.ylabel('Density')
    plt.title('Alcohol Distribution by Class (Shared Bins, Density Normalized)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    ```

**구체적 예시**

*   **시험 점수 분포 비교**: 두 반의 학생들의 수학 시험 점수를 비교한다고 가정해 봅시다. 한 반은 30명, 다른 반은 50명입니다. 히스토그램으로 그리면 학생 수가 많다는 이유만으로 50명 반의 막대그래프 높이가 더 높아 보일 수 있습니다. 하지만 ECDF를 사용하면 각 반의 점수가 특정 값보다 낮은 학생의 *비율*을 보여주기 때문에, 학생 수($n$)의 차이와 무관하게 두 반의 점수 분포 경향을 객관적으로 비교할 수 있습니다. 예를 들어, ECDF 그래프에서 두 반 모두 70점에 해당하는 누적 비율이 0.5라면, 두 반 모두 학생의 절반이 70점 이하라는 것을 바로 알 수 있습니다.
*   **와인 데이터 'alcohol' 컬럼 비교**: 강의 음성에서 언급된 와인 데이터프레임의 'alcohol' 컬럼을 여러 와인 클래스별로 비교하는 예시를 들어보겠습니다. 히스토그램을 사용할 때는 위 코드 예시처럼 공통 bin을 설정하고 `density=True`로 정규화해야만 공정한 비교가 가능합니다. 그러나 ECDF는 애초에 누적 비율을 그리기 때문에 이런 복잡한 설정 없이도 각 와인 클래스별 알코올 함량 분포의 차이를 직관적으로 파악할 수 있습니다. 예를 들어, 한 클래스의 ECDF가 다른 클래스보다 전반적으로 오른쪽에 위치한다면, 해당 클래스의 알코올 함량이 더 높은 경향이 있다는 것을 의미합니다.

**강의 내용**

*   **"This is a very crucial part." 강조**: 교수님께서는 데이터 분포를 공정하게 비교하는 것이 통계적 분석에서 매우 중요한 부분임을 강조하셨습니다. 이는 히스토그램의 한계를 인식하고 ECDF와 같은 견고한 도구의 필요성을 부각하는 맥락으로 이해할 수 있습니다.
*   **히스토그램의 한계와 ECDF의 필요성**: 교수님께서 "공간과 사이즈의 차이가 비율과 상품의 차이가 비율이 아닙니다. 사실은, 실제 형태의 차이가 비율이 아닙니다. 그래서, 이게 전혀 이해하지 않습니다. 그래서, 이런 식으로 변화해야 할 수 있습니다."라고 언급하신 부분은 히스토그램이 bin 선택에 따라 데이터의 실제 분포 형태나 비율을 오해하게 만들 수 있다는 점을 지적하며, ECDF처럼 bin 설정에 의존하지 않고 분포를 직관적으로 비교할 수 있는 방법의 중요성을 강조하는 것으로 해석됩니다.
*   **히스토그램 '공정한 비교'의 구체적 방법**: 음성에서 "sharing beans (bins) and normalization"이라는 표현과 함께 'alcohol column' 예시, `MPHistorium_bin_edges`, `FD rule`, `plt-hist` 사용법, `density=True` 및 `alpha` 값 설정 등을 구체적으로 설명하신 부분은 히스토그램으로도 '공정한 비교'를 시도할 수 있는 한 가지 방법입니다. 하지만 ECDF는 이러한 추가적인 설정 없이도 본질적으로 'bin-free'하며 '비율' 기반이므로 더욱 직관적이고 견고한 비교를 제공하는 대안이 됩니다.

**시험 포인트**

*   ⭐ **ECDF의 정의와 수식** (`$\hat{F}(x)$`)을 정확히 이해하고 설명할 수 있어야 합니다. 특히 수식의 각 구성 요소가 무엇을 의미하는지 중요합니다.
*   ⭐ **ECDF가 히스토그램보다 가지는 핵심적인 장점 3가지**: Bin-free, Robust comparison, Quantiles at a glance를 명확히 구분하고 설명할 수 있어야 합니다.
*   ⭐ **ECDF의 주요 속성**:
    *   ECDF는 항상 **단조 증가하는 계단 함수(Nondecreasing step function)**입니다.
    *   각 데이터 포인트에서 **$1/n$ 크기의 점프(jump)**를 가집니다.
    *   동일한 값($x$)을 가지는 데이터 포인트(ties)가 여러 개 있을 경우, 해당 위치에서 **더 큰 점프**를 발생시킵니다.
*   ⭐ **ECDF를 이용한 분포 비교 방법**: 여러 ECDF를 한 그래프에 **겹쳐 그려(overlay)** 분포를 비교할 수 있으며, 이 때 ECDF 간의 **수직 간격(vertical gaps)**은 분포 간의 통계적 우위(stochastic dominance)를 시사합니다.
*   ⭐ **Kolmogorov-Smirnov (KS) distance**: 두 ECDF 사이의 **최대 수직 간격(maximum vertical gap)**을 사용하여 두 표본이 동일한 분포에서 왔는지(`goodness-of-fit`) 또는 두 표본의 분포가 서로 다른지(`two-sample diagnostic`)를 판단하는 간단한 진단 도구로 활용될 수 있습니다.

---

## Slide 13

## 데이터분석 입문 (CSED226) - ECDF (Empirical Cumulative Distribution Function)

### 핵심 개념

**ECDF (Empirical Cumulative Distribution Function; 경험적 누적 분포 함수)**는 주어진 데이터셋에서 특정 값 $x$보다 작거나 같은 데이터 포인트의 **비율**을 나타내는 함수입니다. 이는 데이터의 분포를 누적된 형태로 보여주며, 데이터 값들이 어떻게 분포되어 있는지, 특히 데이터의 중앙값, 사분위수 등 전반적인 분포 형태를 파악하는 데 유용합니다.

**ECDF 그래프 해석**:
*   **X축**: 데이터의 값 (예: `sepal length (cm)`).
*   **Y축**: 해당 X축 값보다 작거나 같은 데이터의 비율 (0에서 1 사이).
*   **우측으로 이동한 곡선**: 곡선이 오른쪽으로 더 이동해 있을수록 해당 그룹의 데이터 값들이 전반적으로 **더 크다**는 것을 의미합니다. (예: 동일한 Y값(누적 비율)에 도달하기 위해 더 큰 X값이 필요).

### 코드/수식 해설

**`seaborn.ecdfplot` 함수**:
Seaborn 라이브러리의 `ecdfplot` 함수를 사용하여 ECDF를 쉽게 시각화할 수 있습니다.

```python
# 단일 샘플 ECDF 플롯
import seaborn as sns
import matplotlib.pyplot as plt

# iris 데이터셋 로드 가정
# sns.load_dataset('iris')

sns.ecdfplot(data=iris, x="sepal length (cm)")
plt.ylabel("ECDF") # y축 레이블 설정

# 그룹별 ECDF 비교
sns.ecdfplot(data=iris, x="sepal length (cm)", hue="species")
plt.ylabel("ECDF") # y축 레이블 설정
plt.show()
```

*   `data`: ECDF를 그릴 데이터가 포함된 DataFrame을 지정합니다. (예: `iris`)
*   `x`: ECDF를 그릴 수치형 변수의 컬럼 이름을 지정합니다. (예: `"sepal length (cm)"`)
*   `hue`: 데이터를 특정 범주형 변수의 그룹으로 나누어 각 그룹별 ECDF를 그릴 때 사용합니다. (예: `"species"`)

**ECDF 수식**:
$n$개의 관측치 $X_1, X_2, \dots, X_n$으로 구성된 데이터셋이 있을 때, ECDF $F_n(x)$는 다음과 같이 정의됩니다.
$$ F_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{X_i \le x} $$
여기서 $\mathbf{1}_{X_i \le x}$는 지시 함수(indicator function)로, $X_i \le x$이면 1, 그렇지 않으면 0의 값을 가집니다. 즉, $x$보다 작거나 같은 관측치들의 수를 전체 관측치 수 $n$으로 나눈 값입니다.

### 구체적 예시

첨부된 슬라이드의 `iris` 데이터셋 예시를 통해 ECDF를 이해할 수 있습니다.
*   **`sepal length (cm)`** 특성에 대해 **`species`**별로 ECDF가 그려져 있습니다.
*   **파란색(`setosa`)** 곡선이 가장 왼쪽에 위치합니다. 이는 setosa 종의 `sepal length`가 다른 두 종에 비해 전반적으로 가장 작다는 것을 의미합니다. 예를 들어, sepal length가 5.0cm 이하인 setosa는 전체 setosa의 약 60%를 차지합니다.
*   **주황색(`versicolor`)** 곡선은 setosa보다 오른쪽에 있지만 virginica보다는 왼쪽에 있습니다. 이는 versicolor의 `sepal length`가 setosa보다는 길고 virginica보다는 짧은 경향이 있음을 보여줍니다.
*   **초록색(`virginica`)** 곡선이 가장 오른쪽에 위치합니다. 이는 virginica 종의 `sepal length`가 전반적으로 가장 길다는 것을 의미합니다. 동일한 50% 지점(Y=0.5)을 보면, setosa는 약 5.0cm, versicolor는 약 5.8cm, virginica는 약 6.5cm에서 나타납니다.

### 강의 내용

교수님은 **누적 히스토그램 (cumulative histogram)**을 ECDF의 한 변형으로 설명하며, `matplotlib.pyplot.hist` 함수를 사용하여 유사한 그래프를 그릴 수 있는 방법을 언급했습니다.

*   `hist` 함수에서 `cumulative=True`로 설정하면 누적 빈도를 계산합니다.
*   `histtype='step'`으로 설정하면 계단형 그래프로 나타내어 ECDF와 유사한 시각적 효과를 얻을 수 있습니다.
*   이는 `seaborn.ecdfplot`이 기본적으로 수행하는 기능과 유사하며, ECDF는 각 데이터 포인트에 대해 전체 데이터의 비율(0부터 1까지)을 Y축에 나타내는 누적 분포 그래프입니다.

### 시험 포인트

*   ⭐ **ECDF의 정의와 의미**: ECDF가 무엇이며, Y축 값이 나타내는 것이 무엇인지 정확히 이해해야 합니다.
*   ⭐ **ECDF 그래프 해석**: ECDF 곡선이 **오른쪽으로 이동할수록** 데이터 값이 전반적으로 **더 커진다**는 것을 이해하고, 이를 실제 데이터 분포에 적용하여 해석할 수 있어야 합니다. (예: 슬라이드의 `iris` 데이터 예시).
*   ⭐ **`seaborn.ecdfplot`의 사용법**: `data`, `x`, `hue`와 같은 주요 파라미터의 역할을 알고 사용할 수 있어야 합니다.
*   ECDF와 누적 히스토그램의 관계: 누적 분포를 시각화하는 방법 중 하나로 ECDF가 있으며, `hist` 함수의 `cumulative=True`와 `histtype='step'` 조합으로 유사한 형태를 얻을 수 있음을 인지하세요.

---

## Slide 14

다음은 "데이터분석 입문 (CSED226)" 강의 자료 중 해당 슬라이드 구간에 대한 노트입니다.

---

### **핵심 개념**
*   **모집단 분포 추정 (Estimating Population Distribution)**: 소규모 표본(`small sample`) 데이터를 기반으로 전체 모집단(`population`)의 데이터 분포를 추정하는 것이 데이터 분석의 핵심적인 도전 과제입니다.
*   **KDE (Kernel Density Estimation)**: 표본으로부터 기저(`underlying`) 밀도(`density`)의 부드럽고(`smooth`), 정량적인(`quantitative`) 추정치를 얻기 위한 통계적 기법입니다. 이는 히스토그램의 빈(bin) 선택 문제에서 자유롭게 밀도 함수를 추정합니다.
*   **누적 분포 뷰 (Cumulative Distribution View)**: 데이터의 분포를 특정 값 $x$ 이하인 데이터의 비율 또는 누적 밀도로 시각화하는 방법입니다. 이는 데이터의 퀀타일(`quantile`) 정보를 파악하는 데 유용합니다.
*   **eCDF (Empirical Cumulative Distribution Function)**: 표본 데이터를 사용하여 얻은 누적 분포 함수의 "경험적(`empirical`)" 버전입니다. 누적 히스토그램의 '빈(bin)'에 의존하지 않는 "빈-프리(`bean-free`)" 방식으로 누적 분포를 표현합니다.

### **코드/수식 해설**
eCDF는 특정 값 $x$보다 작거나 같은 데이터 포인트의 비율로 정식적으로 정의됩니다.
$n$개의 데이터 포인트($X_1, X_2, \ldots, X_n$)로 구성된 표본이 있을 때, eCDF $\hat{F}_n(x)$는 다음과 같습니다.

$$
\hat{F}_n(x) = \frac{\text{데이터 포인트 중 } X_i \le x \text{ 인 개수}}{n} = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{X_i \le x}
$$
여기서 $\mathbf{1}_{X_i \le x}$는 지시 함수(`indicator function`)로, $X_i \le x$ 이면 1, 그렇지 않으면 0의 값을 가집니다.

### **구체적 예시**
*   **문제 상황**: 슬라이드에 제시된 표본 데이터는 $n=6$개의 값 `45, 52, 58, 78, 82, 95`입니다. 이 작은 표본을 통해 모집단의 전체 분포를 추정하는 것이 목표입니다. 이 표본을 통해 대략 50점대, 80점대, 그리고 95점 근처의 고득점자 그룹이 존재할 것이라는 직관을 얻을 수 있습니다. KDE는 이러한 직관을 바탕으로 실제 모집단의 밀도 함수를 부드럽게 추정합니다.
*   **eCDF 계산 예시**: 위 표본 데이터를 사용하여 $\hat{F}_n(60)$을 계산해봅시다.
    *   표본 중 60 이하인 데이터 포인트는 `45, 52, 58`로 총 3개입니다.
    *   전체 데이터 포인트는 6개입니다.
    *   따라서 $\hat{F}_n(60) = 3/6 = 0.5$입니다. 이는 표본 데이터의 50%가 60 이하라는 것을 의미합니다.
*   **누적 뷰 시각화**: 강의에서는 누적 히스토그램(쌓인 막대 그래프)을 선 그래프로 전환하면 y축이 누적 밀도 또는 비율을 나타내는 **상승하는 계단 함수(`rising step function`)** 형태의 플롯이 된다고 설명했습니다. eCDF 그래프도 이와 같은 계단 함수 형태를 띱니다.

### **강의 내용**
*   교수님은 작은 표본($n=6$)으로부터 모집단(`population`) 분포를 추정하는 것이 중요하고 도전적인 문제임을 강조하셨습니다.
*   제시된 표본(45, 52, 58, 78, 82, 95)을 통해 데이터가 대략 50점대, 80점대, 그리고 95점 근처의 고득점자 그룹으로 나뉠 수 있다는 직관을 얻을 수 있다고 설명하셨습니다.
*   **KDE의 역할**은 이러한 직관을 바탕으로 기저 밀도(`underlying density`)에 대한 부드럽고(`smooth`), 정량적인(`quantitative`) 추정치를 제공하는 것이라고 하셨습니다.
*   이어서, 교수님은 (이전 슬라이드의 내용 또는 누적 막대 그래프와 관련하여) 누적 밀도를 보여주는 선 플롯은 **상승하는 계단 함수(`rising step function`)** 형태로 나타난다고 설명했습니다.
*   이 플롯의 y축은 특정 $x$ 값보다 작거나 같은 데이터의 **누적 밀도(`cumulative density`) 또는 비율(`proportion`)**을 나타냅니다.
*   이러한 누적 뷰는 **퀀타일(`quantile`)**을 파악하거나 **확률적 지배(`stochastic dominance`)** 개념을 이해하는 데 매우 유용하다고 하셨지만, 확률적 지배는 이번 강의에서 다루지 않고 관심 있는 학생은 Wikipedia를 찾아볼 것을 권유하셨습니다.
*   또한, 이 누적 뷰 개념은 **eCDF (Empirical Cumulative Distribution Function)**라는 다음 주제로 이어지는 "완벽한 다리(`perfect bridge`)" 역할을 한다고 강조하셨습니다.
*   eCDF는 누적 히스토그램과 달리 '빈(`bin`)'에 얽매이지 않는 **"빈-프리(`bean-free`)"** 버전의 누적 뷰를 제공하며, eCDF는 $x$ 이하의 데이터 포인트 비율로 정식적으로 정의됩니다.

### **시험 포인트**
*   ⭐ **모집단 분포 추정의 필요성**: 왜 작은 표본으로 모집단의 분포를 추정해야 하는지, 그리고 이 과정에서 KDE가 어떤 역할을 하는지 (e.g., `smooth, quantitative estimate of underlying density`).
*   ⭐ **eCDF의 정의와 의미**: eCDF가 무엇이며, 어떤 정보를 제공하는 함수인지 정확히 설명할 수 있어야 합니다 (e.g., $x$ 이하의 데이터 포인트 비율).
*   ⭐ **누적 히스토그램과 eCDF의 차이**: eCDF가 "빈-프리" 버전이라는 것의 의미와 장단점.
*   ⭐ **누적 분포 플롯의 특징**: 누적 분포 플롯이 '상승하는 계단 함수' 형태로 나타나는 이유와 y축이 나타내는 의미(누적 밀도/비율).

---

## Slide 15

**핵심 개념**

*   **Local Information (지역 정보)**: 각 관측 데이터 포인트 $x_i$는 자기 자신뿐만 아니라 주변(neighborhood)의 값들에 대한 정보도 포함하고 있습니다. 이는 데이터 분포를 이해할 때 단순히 개별 점 하나하나를 보는 것을 넘어 그 주변 영역의 밀도를 함께 고려해야 함을 의미합니다.
*   **Kernel Idea (커널 아이디어)**: 이러한 지역 정보를 활용하기 위해, 각 데이터 포인트 $x_i$에 종 모양(bell-shaped)의 확률 곡선인 **커널(kernel)**을 배치합니다. 이 커널은 $x_i$ 근처 값들에 대한 우리의 "확신(confidence)"을 인코딩합니다. 일반적으로 가우시안 커널이 많이 사용됩니다.
*   **Local Evidence (지역 증거)**: 각 종 모양 커널은 $x_i$에 가까운 점들에 대해 **지역 증거(local evidence)**를 제공합니다. $x_i$에서 멀어질수록 해당 커널의 기여도(contribution)는 작아집니다.
*   **KDE (Kernel Density Estimation) 직관**: 슬라이드의 그래프는 KDE의 직관을 보여줍니다. 여러 데이터 포인트에 배치된 개별 가우시안 커널들을 합산(또는 평균)하여 전체적인 밀도 추정 곡선을 얻게 됩니다. 이 방법은 히스토그램의 '빈(bin)' 경계에 따른 인위적인 왜곡(artifacts)을 피하고 더 부드러운 밀도 추정치를 제공합니다.

**코드/수식 해설**

*   **커널 밀도 추정 (KDE) 수식**:
    $n$개의 데이터 포인트 $X = \{x_1, x_2, \dots, x_n\}$가 주어졌을 때, 커널 밀도 추정량 $\hat{f}_h(x)$는 다음과 같이 정의됩니다.
    $$ \hat{f}_h(x) = \frac{1}{n} \sum_{i=1}^n K_h(x - x_i) = \frac{1}{nh} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right) $$
    여기서:
    *   $K(\cdot)$는 커널 함수(예: 표준 가우시안 커널).
    *   $h$는 대역폭(bandwidth) 또는 스무딩 파라미터로, 커널의 폭을 결정합니다. $h$가 클수록 더 부드러운 곡선이 되고, 작을수록 뾰족한 곡선이 됩니다.
    *   $K_h(u) = \frac{1}{h} K(\frac{u}{h})$는 스케일링된 커널 함수입니다.

**구체적 예시**

슬라이드 하단의 그래프는 KDE의 직관을 잘 보여줍니다.
*   선택된 세 개의 데이터 포인트(예: 52, 82, 95) 각각에 대해 종 모양의 가우시안 커널(주황색, 연두색, 빨간색 곡선)이 생성됩니다.
*   이 개별 커널들을 모두 합산(또는 평균)한 것이 보라색 곡선으로 표현됩니다. 이 보라색 곡선이 바로 전체 데이터 분포의 KDE 밀도 추정치입니다.
*   데이터 포인트가 밀집한 구간에서는 여러 커널이 겹쳐져 밀도 값이 높아지고, 데이터 포인트가 드문 구간에서는 밀도 값이 낮아지는 것을 확인할 수 있습니다.

**강의 내용**

교수님께서 음성으로 강조하신 내용은 슬라이드의 KDE 내용과는 별개로 **ECDF(Empirical Cumulative Distribution Function, 경험적 누적 분포 함수)**에 대한 설명입니다. 이는 데이터 분포를 시각화하는 또 다른 중요한 방법입니다.

*   **ECDF의 정의**: ECDF는 주어진 데이터셋에서 특정 값 $x$보다 작거나 같은 데이터 포인트의 비율을 나타냅니다. 그 정의는 다음과 같습니다:
    $\hat{F}_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}(X_i \le x)$
    여기서 $\mathbb{I}(\cdot)$는 지시 함수(indicator function)로, 괄호 안의 조건이 참이면 1, 거짓이면 0의 값을 가집니다. 교수님께서는 "$1$ over $n$ times the sum of indicator function"이라고 강조하셨습니다.
*   **ECDF의 장점**:
    *   **Beam-free / Histogram Artifacts Avoidance**: 히스토그램처럼 빈(bin)의 너비나 시작점에 따라 모양이 달라지는 인위적인 왜곡(histogram artifacts)이 없습니다.
    *   **Robust Comparison**: 특히 샘플 크기가 다른 경우에도 분포를 강건하게 비교할 수 있습니다.
    *   **Quantiles at a Glance**: 분위수(quantiles)를 한눈에 쉽게 읽을 수 있습니다.
        *   중앙값(median, 50% 분위수)은 ECDF가 $0.5$를 교차하는 $x$ 값입니다.
        *   90번째 백분위수(90th percentile)는 ECDF가 $0.9$ (y축)를 교차하는 $x$ 값입니다.
*   **ECDF의 특징**: ECDF는 항상 **비감소(non-decreasing) 함수**입니다. 즉, $x$ 값이 증가할수록 ECDF 값은 같거나 커지며 절대 작아지지 않습니다.

**시험 포인트**

*   ⭐ **KDE의 기본 아이디어**: 각 데이터 포인트가 주변에 "지역 증거"를 제공하며, 커널 함수를 사용하여 이를 부드럽게 통합한다는 개념.
*   ⭐ **ECDF의 정의**: $\hat{F}_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}(X_i \le x)$ 수식과 그 의미를 정확히 이해해야 합니다.
*   ⭐ **ECDF의 주요 장점**: 히스토그램 아티팩트 방지, 불균등 샘플 크기 비교의 강건성, 분위수를 쉽게 파악할 수 있다는 점을 숙지해야 합니다.
*   ⭐ **ECDF를 통한 분위수 파악**: 중앙값(median)과 백분위수(percentile)를 ECDF 그래프에서 어떻게 찾아내는지 이해하는 것이 중요합니다. (예: 50% 분위수는 $y=0.5$, 90% 분위수는 $y=0.9$와 만나는 $x$ 값).
*   ⭐ **ECDF의 성질**: ECDF가 항상 비감소 함수라는 특징.

---

## Slide 16

- **핵심 개념**:
    *   **커널 밀도 추정 (KDE, Kernel Density Estimation)**: 주어진 데이터 포인트들을 사용하여 데이터의 확률 밀도 함수(PDF, Probability Density Function)를 비모수적으로 추정하는 방법입니다. 각 데이터 포인트에 커널 함수를 중심(center)에 두고, 이 커널들의 예측값(밀도에 대한 기여도)을 평균하여 전체 데이터 분포의 부드러운 형태를 추정합니다. 이 과정은 데이터의 분포를 시각화하거나 이상치를 탐지하는 데 유용하게 사용됩니다.

- **코드/수식 해설**:
    *   **KDE 추정량 (Estimator, with normalization)**:
        $$ \hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right) $$
        *   $\hat{f}_h(x)$: 특정 지점 $x$에서의 추정된 확률 밀도 값입니다.
        *   $n$: 전체 데이터 포인트의 개수.
        *   $h$: **대역폭 (bandwidth)**. 각 커널 함수의 너비를 조절하는 파라미터로, 추정된 밀도 함수의 '부드러움(smoothness)' 정도를 결정합니다. $h$ 값이 작을수록 추정된 밀도 함수는 뾰족해지고 데이터에 더 민감하게 반응하며, $h$ 값이 클수록 더욱 부드럽고 일반화된 형태를 보입니다.
        *   $K(\cdot)$: **커널 함수 (kernel function)**. 각 데이터 포인트 $x_i$에 centered 되는 가중치 함수입니다. 주로 가우시안(Gaussian) 커널이 많이 사용됩니다. 이 함수는 $x$가 $x_i$에 가까울수록 높은 값을 가집니다.
        *   $\frac{x - x_i}{h}$: $x$와 각 데이터 포인트 $x_i$ 사이의 거리를 대역폭 $h$로 스케일링한 값입니다.
    *   **정규화 조건**:
        $$ \int \hat{f}_h(x) \, dx = 1 $$
        *   추정된 밀도 함수 $\hat{f}_h(x)$는 확률 밀도 함수이므로, 전체 구간에 대해 적분하면 그 값이 1이 되어야 합니다. 이는 추정된 함수가 유효한 확률 분포임을 보장합니다.

- **구체적 예시**:
    *   여러분에게 학생들의 키 데이터 $X = \{160\text{cm}, 165\text{cm}, 170\text{cm}, 172\text{cm}, 180\text{cm}\}$가 있다고 가정해 봅시다.
    *   KDE는 각 키 값 $x_i$에 작은 언덕 형태의 커널(예: 종 모양의 가우시안 커널)을 세웁니다.
    *   대역폭 $h$ 값에 따라 이 언덕들의 너비가 달라집니다. $h$가 작으면 각 키 값 주변에 좁고 뾰족한 언덕들이 생기고, $h$가 크면 언덕들이 넓게 퍼져 서로 겹쳐지면서 전체적으로 부드러운 곡선이 됩니다.
    *   이 모든 언덕들을 합하고 평균을 내면, 전체 학생들의 키 분포를 나타내는 부드러운 곡선(확률 밀도 함수)을 얻게 됩니다. 예를 들어, 170cm 근처에 키를 가진 학생이 많다면 해당 구간의 밀도가 높게 추정되어 곡선이 위로 솟아오르게 됩니다.

- **강의 내용**:
    *   ⚠️ **음성 전사와 슬라이드 내용 불일치**: 제공된 음성 전사는 현재 슬라이드(KDE)의 내용과 일치하지 않고, ECDF (Empirical Cumulative Distribution Function, 경험적 누적 분포 함수)에 대한 설명입니다. 따라서, 다음 강의 내용은 ECDF에 대한 설명으로 구성됩니다.
    *   **ECDF의 동작 원리**:
        *   ECDF는 계단 함수(step function) 형태를 띠며, 각 데이터 포인트($x_i$)에서 $1/n$만큼 누적 확률이 점프합니다. ($n$은 전체 데이터 포인트의 개수)
        *   만약 여러 데이터 포인트가 동일한 값(tied value)을 가질 경우, 해당 지점에서 묶인 값의 개수에 비례하여 더 큰 점프가 발생합니다.
        *   여러 ECDF를 한 그래프에 겹쳐 그리면 서로 다른 데이터 분포들을 시각적으로 쉽게 비교할 수 있습니다. 예를 들어, ECDF 곡선이 다른 곡선보다 전반적으로 오른쪽으로 이동해 있다면, 해당 분포는 확률적으로 더 큰 값들로 구성되어 있음을 나타냅니다.
    *   **`seaborn`을 이용한 ECDF 시각화 (음성에서 'CERBON'은 `seaborn`의 오타로 추정)**:
        *   `seaborn` 라이브러리(`sns`)의 `ecdfplot` 함수를 사용하면 ECDF를 매우 직관적으로 그릴 수 있습니다.
        *   **단일 샘플 ECDF 플롯**: 데이터프레임의 특정 열에 대해 `sns.ecdfplot(data=df, x='column_name')`과 같이 호출합니다.
        *   **그룹별 ECDF 비교**: `hue` 파라미터를 사용하여 그룹별 ECDF를 그릴 수 있습니다.
            ```python
            import seaborn as sns
            import pandas as pd
            import numpy as np

            # 예시 데이터 생성
            data = {
                'value': np.random.normal(0, 1, 100).tolist() + np.random.normal(1, 0.8, 80).tolist(),
                'group': ['A']*100 + ['B']*80
            }
            df = pd.DataFrame(data)

            # 그룹별 ECDF 시각화
            sns.ecdfplot(data=df, x='value', hue='group')
            ```
            음성에서는 `species` 변수를 `hue`로 설정하여 종(species)별로 ECDF를 비교하는 예시를 들었습니다. 이 방법은 각 그룹의 샘플 크기가 다르더라도 정확하고 견고하게(robust) 작동합니다. 예를 들어, 세 그룹이 있다면 세 개의 ECDF 곡선이 그려집니다.

-   **시험 포인트**:
    *   ⭐ **KDE의 기본 원리**: 각 데이터 포인트에 커널을 centered하고 이 커널들의 예측값을 평균하여 부드러운 밀도 함수를 추정한다는 점을 이해해야 합니다.
    *   ⭐ **KDE 수식의 각 요소**: 특히 $K$ (커널 함수, 주로 가우시안)와 $h$ (대역폭)의 역할과 의미를 정확히 알아야 합니다. 특히 $h$ 값이 KDE 결과(부드러움 정도)에 미치는 영향을 설명할 수 있어야 합니다.
    *   ⭐ **ECDF의 개념 및 특징**: ECDF가 계단 함수이며, 각 데이터 포인트에서 $1/n$만큼 점프하고, 동점(tied values) 처리 방식, 그리고 여러 분포 비교에 활용될 수 있다는 점을 이해하는 것이 중요합니다.
    *   ⭐ **`seaborn.ecdfplot` 사용법**: 특히 `hue` 파라미터를 사용한 그룹별 ECDF 시각화 방법을 알아두세요.

---

## Slide 17

---
### **핵심 개념**
커널 밀도 추정(KDE)에서 **대역폭 ($h$)**은 추정된 확률 밀도 함수의 부드러움을 결정하는 가장 중요한 매개변수입니다. 각 데이터 포인트 주변에 위치한 커널 함수의 '퍼짐' 정도를 조절하여 전체 분포의 형태를 만듭니다.

*   **`h`가 너무 작을 경우 (undersmooth)**: 추정 곡선이 들쭉날쭉하고 노이즈가 많아집니다 (Jagged, noisy estimate). 실제로는 존재하지 않는 많은 가짜 피크(spurious peaks)들이 나타나 데이터의 아티팩트처럼 보일 수 있습니다.
*   **`h`가 너무 클 경우 (oversmooth)**: 추정 곡선이 너무 뭉툭하고 평평해집니다 (Blurry, flat estimate). 데이터 내에 존재하는 실제 모드(mode)나 중요한 구조적 특징을 놓칠 수 있습니다.

### **코드/수식 해설**

**최적의 $h$ 선택**:
이상적인 $h$ 값은 데이터의 특징을 가장 잘 반영하면서도 노이즈에 과민반응하지 않고 중요한 구조를 놓치지 않는 'sweet spot'을 찾는 것입니다. 이는 **교차 검증(cross-validation)**이나 **플러그인 규칙(plug-in rules)**과 같은 통계적 방법을 통해 찾을 수 있습니다.

**Seaborn에서의 대역폭 조정**:
데이터 시각화 라이브러리인 Seaborn에서는 기본 대역폭 $h_{\text{base}}$가 데이터에 기반하여 자동으로 선택됩니다. 사용자는 `bw_adjust` 인자를 통해 이 기본 대역폭을 조정할 수 있습니다.

$$ h_{\text{used}} = \text{bw\_adjust} \times h_{\text{base}} $$

*   `bw_adjust` 값이 작을수록 추정 곡선은 더 세밀해집니다 ($\Rightarrow$ `more detail`).
*   `bw_adjust` 값이 클수록 추정 곡선은 더 부드러워집니다 ($\Rightarrow$ `smoother`).

### **구체적 예시**

사진 편집 프로그램에서 '블러(Blur)' 효과를 생각해보세요.
*   블러 강도가 너무 약하면 (작은 $h$), 사진의 원래 노이즈나 작은 디테일이 그대로 남아 지저분해 보일 수 있습니다.
*   블러 강도가 너무 강하면 (큰 $h$), 사진이 너무 뭉개져서 원래 사물의 형태나 중요한 특징을 알아보기 어렵게 됩니다.
KDE의 대역폭 $h$는 이 블러 강도와 유사하게, 데이터 분포를 얼마나 부드럽게 '블러' 처리하여 근본적인 형태를 드러낼지 결정합니다.

예를 들어, 학생들의 시험 점수 데이터 (50점대, 80점대, 95점 고득점자)가 있다고 할 때:
*   $h$가 너무 작으면, 50점대에도 여러 개의 작은 봉우리가 생기고 80점대에도 여러 봉우리가 생겨 실제로는 50점대 그룹, 80점대 그룹 두 개이지만 마치 여러 개의 작은 그룹이 있는 것처럼 보일 수 있습니다.
*   $h$가 너무 크면, 50점대 그룹과 80점대 그룹이 하나의 거대한 봉우리로 합쳐져 두 개의 명확한 그룹이 존재한다는 사실을 놓칠 수 있습니다.

### **강의 내용**
교수님께서는 슬라이드 14에서 우리가 "작은 데이터 샘플로부터 그것이 유래한 모집단 분포를 어떻게 추정할 수 있는가"라는 도전에 직면해 있다고 설명하셨습니다. 히스토그램은 데이터가 적을 때 구간 설정(bin placement)에 매우 민감하여 불안정하지만, KDE 플롯은 "데이터를 기저 밀도의 부드러운 정량적 추정치로 변환"할 수 있다고 강조하셨습니다.

이 슬라이드(17)의 **대역폭 ($h$)**은 바로 이 "부드러운 정량적 추정치"를 얻기 위한 핵심적인 부분입니다. KDE의 근본적인 아이디어인 **"지역적 증거(local evidence)"**를 통해 커널 곡선을 생성하는데, 이때 $h$가 각 데이터 포인트 주변의 '지역'이 얼마나 넓게 분포에 기여할지를 정의하여 최종적인 부드러움을 결정합니다. 따라서 $h$를 어떻게 설정하느냐에 따라 우리가 얻는 "부드러운 추정치"의 품질이 크게 달라지며, 이는 실제 모집단 분포를 얼마나 정확하게 반영하는지와 직결됩니다.

### **시험 포인트**
*   ⭐ **대역폭 ($h$)의 역할과 중요성**: KDE에서 $h$가 무엇을 의미하고 왜 중요한 매개변수인지 설명할 수 있어야 합니다.
*   ⭐ **`h` 값에 따른 결과의 차이**: `h`가 너무 작을 때(undersmooth)와 너무 클 때(oversmooth) 나타나는 현상 (들쭉날쭉함, 뭉툭함, 가짜 피크, 실제 구조 손실 등)을 명확히 구분하여 설명할 수 있어야 합니다. (예: 그림을 통해 $h$가 다른 경우의 KDE 곡선을 보여주고 어느 것이 undersmooth/oversmooth인지 판단)
*   ⭐ **최적의 `h` 선택 방법**: 교차 검증 또는 플러그인 규칙이 최적의 $h$를 찾는 데 사용될 수 있음을 기억해야 합니다.
*   ⭐ **Seaborn의 `bw_adjust`**: `bw_adjust`가 무엇이고, 이 값을 어떻게 조절함으로써 KDE 곡선의 부드러움을 변경할 수 있는지 이해해야 합니다. (`bw_adjust`가 작을 때/클 때 곡선이 어떻게 변화하는지)
---

---

## Slide 18

**핵심 개념**:
KDE(Kernel Density Estimation)는 데이터의 숨겨진 확률 밀도 함수를 추정하는 비모수적 방법입니다. 핵심 아이디어는 각 관측 데이터 포인트에 "지역적인 증거(local evidence)"로 작은 종 모양의 확률 곡선(커널)을 배치하고, 이 모든 개별 커널들의 합 또는 평균을 통해 전체 데이터 분포를 부드러운 곡선으로 나타내는 것입니다. 이를 통해 히스토그램보다 데이터의 모드(봉우리)와 꼬리 부분의 행동(tail behavior)을 더 잘 드러내고, 그룹 간 데이터 분포의 '형태(shapes)'를 효과적으로 비교할 수 있습니다.

**코드/수식 해설**:
KDE는 $N$개의 데이터 포인트 $x_1, x_2, \dots, x_N$에 대해 다음과 같은 수식으로 확률 밀도 함수 $\hat{f}(x)$를 추정합니다.
$$
\hat{f}(x) = \frac{1}{Nh} \sum_{i=1}^{N} K\left(\frac{x - x_i}{h}\right)
$$
여기서 각 기호는 다음과 같은 의미를 가집니다:
*   $N$: 데이터 포인트의 총 개수
*   $h$: 대역폭(bandwidth) 또는 스무딩(smoothing) 매개변수로, 커널의 폭과 스무딩 정도를 결정합니다. $h$가 작으면 추정량이 뾰족하고, $h$가 크면 너무 부드러워질 수 있습니다.
*   $K(\cdot)$: 커널 함수입니다. 주로 가우시안 커널(Gaussian kernel)이 사용되며, 그 형태는 다음과 같습니다.
    $$
    K(u) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2}
    $$
    이 가우시안 커널은 데이터 포인트 $x_i$를 중심으로 하는 작은 종 모양의 확률 곡선을 생성합니다.

**구체적 예시**:
만약 우리가 세 개의 데이터 포인트($x_1, x_2, x_3$)를 가지고 있다면, KDE는 다음과 같이 작동합니다.
1.  첫 번째 데이터 포인트 $x_1$에 작은 종 모양의 가우시안 곡선(커널)을 놓습니다.
2.  두 번째 데이터 포인트 $x_2$에 또 다른 가우시안 곡선을 놓습니다.
3.  세 번째 데이터 포인트 $x_3$에 마지막 가우시안 곡선을 놓습니다.
이 세 개의 개별 가우시안 곡선들을 모두 합치거나 평균을 내면, 세 데이터 포인트의 분포를 나타내는 하나의 부드러운 최종 곡선이 만들어집니다. 이 보라색(강의 음성에서 언급) 곡선이 바로 KDE 추정량이며, 이는 데이터의 밀도 분포를 시각화합니다.

**강의 내용**:
교수님께서는 "Local evidence" 개념이 매우 중요하다고 강조하셨습니다. 이는 각 관측 데이터 포인트가 자신뿐만 아니라 주변 이웃에 대한 정보도 제공한다는 의미입니다. KDE의 핵심은 각 데이터 포인트에 "작은 종 모양의 확률 곡선"(커널)을 배치하는 것이며, 최종 곡선은 이러한 개별 커널들의 "합 또는 평균"이라는 점을 분명히 하셨습니다. 커널은 일반적으로 "작은 가우시안"과 같이 중심을 맞추는 방식으로 사용된다고 설명했습니다.
또한, KDE의 실제 적용에 있어 몇 가지 중요한 고려사항을 언급하셨습니다.
*   **사용 시점**: 히스토그램보다 데이터의 `modes`와 `tail behavior`를 더 잘 보여주고, 그룹 간 `shapes`를 비교할 때 유용합니다.
*   **경계 처리**: 데이터가 특정 경계($x \ge 0$)를 가질 경우, `boundary bias`를 줄이기 위해 `reflection` 또는 `transformations`(예: `log` 변환)을 사용할 수 있습니다.
*   **그룹 비교**: 여러 그룹의 데이터를 비교할 때는 `common axis limits`와 같은 `consistent settings`를 사용해야 하며, 밀도를 정규화할 때 `counts`보다는 `shapes`를 비교하는 것이 중요합니다.
*   **비모수적 강점**: KDE는 데이터가 `unimodal`(단봉형)이든 `multimodal`(다봉형)이든 `rigid assumptions`(엄격한 가정) 없이 데이터가 나타내는 어떤 형태에도 유연하게 적응할 수 있다는 `nonparametric power`를 가지고 있습니다.

**시험 포인트**:
*   ⭐ **KDE의 기본 원리와 작동 방식**: 각 데이터 포인트에 커널(주로 가우시안)을 배치하고, 이들의 합 또는 평균으로 전체 밀도 함수를 추정한다는 점을 이해해야 합니다. (강의 음성에서 핵심으로 강조)
*   ⭐ **KDE의 주요 장점**: 히스토그램 대비 `modes`와 `tail behavior`를 더 잘 파악하고, 여러 그룹 간 `shapes`를 비교하는 데 유리하다는 점을 숙지하세요.
*   ⭐ **비모수적 특성**: KDE가 데이터 분포에 대한 엄격한 가정 없이 유연하게 적응할 수 있는 `nonparametric power`를 가진다는 점이 중요합니다.
*   ⭐ **경계 처리 기법**: 데이터가 특정 경계값을 가질 때(`x >= 0` 등) `boundary bias`를 줄이기 위한 `reflection` 또는 `log transformations`의 개념과 필요성을 알아두세요.
*   수식에서 $h$ (대역폭)가 추정량의 스무딩 정도에 미치는 영향과 중요성.

---

## Slide 19

**핵심 개념**
이 슬라이드 구간의 강의 내용은 **커널 밀도 추정(Kernel Density Estimation, KDE)**에 대한 설명입니다. KDE는 주어진 데이터 포인트로부터 확률 밀도 함수(Probability Density Function, PDF)를 비모수적으로 추정하는 방법입니다. 각 데이터 관측치에 커널 함수를 배치하고, 이 커널들의 합을 통해 전체 데이터 분포의 밀도를 추정합니다.

**코드/수식 해설**
강의 음성에서 설명하는 커널 밀도 추정 $\hat{f}_h(x)$는 다음과 같은 수식으로 표현할 수 있습니다.
$$
\hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right)
$$
*   $\hat{f}_h(x)$: 새로운 쿼리 포인트 $x$에서의 추정된 밀도 값
*   $n$: 데이터 관측치의 총 개수
*   $h$: **대역폭(bandwidth)**. 커널의 너비를 조절하는 파라미터.
*   $K(\cdot)$: **커널 함수(kernel function)**. 일반적으로 가우시안(Gaussian) 함수가 사용됩니다.
*   $x_i$: $i$번째 데이터 관측치
*   $\frac{1}{nh}$: 전체 밀도가 1로 적분되도록 하는 정규화 상수. 교수님은 이를 "1 over n h term is the normalization constant that makes the whole thing integrate to 1"이라고 설명하셨습니다.

**구체적 예시**
교수님은 "So I place probability distribution curve for $X_i$"라고 설명하셨는데, 이는 다음과 같이 시각적으로 이해할 수 있습니다:
1.  **각 데이터 포인트에 커널 배치**: 데이터셋에 $n$개의 데이터 포인트(예: $x_1, x_2, \ldots, x_n$)가 있다면, 각 $x_i$ 위치에 작은 확률 분포 곡선(커널, 주로 가우시안 형태)을 하나씩 놓습니다.
2.  **밀도 계산**: 새로운 쿼리 포인트 $x$에서 밀도 값을 알고 싶다면, 이 $x$ 위치에서 모든 $n$개의 커널 곡선들의 높이(밀도 값)를 읽어옵니다.
3.  **평균**: 이렇게 읽어온 $n$개의 높이 값들을 평균내어 최종적으로 $x$에서의 밀도를 추정합니다. 이는 "you read the height of every kernel at that point... And then you then average those n predictions"와 일치합니다.
이렇게 각 커널이 합쳐져서 전체적인 부드러운 "보라색 곡선(purple curve)"이 만들어지며, 이 곡선은 데이터의 PDF와 유사한 형태를 띠게 됩니다.

**강의 내용**
*   강의에서는 KDE의 기본 원리를 설명하며, 각 관측치 $x_i$에 커널(예: 가우시안)을 중심에 두고 배치한다고 강조합니다.
*   새로운 쿼리 포인트 $x$에서의 밀도는 모든 커널의 해당 높이를 읽어 평균 내는 방식으로 계산됩니다.
*   KDE 수식에서 핵심적인 두 파라미터는 **커널 함수 ($K$)**와 **대역폭 ($h$)**입니다.
*   특히 대역폭 $h$는 "critical", "Smoothness knob you have to tune"이라고 강조되며, 데이터 밀도 추정의 "부드러움"을 조절하는 매우 중요한 요소임을 명시했습니다.
*   $\frac{1}{nh}$ 항은 전체 추정 밀도 함수가 확률 밀도 함수로서 적분 값이 1이 되도록 하는 정규화 상수입니다.

**시험 포인트**
*   ⭐ **커널 밀도 추정(KDE)의 개념과 목적**: 데이터로부터 비모수적으로 확률 밀도 함수를 추정하는 방법임을 이해해야 합니다.
*   ⭐ **KDE 수식의 각 항의 의미**: $n$, $h$, $K( \cdot )$, $x_i$가 각각 무엇을 의미하는지 정확히 알아야 합니다.
*   ⭐ **대역폭 ($h$)의 역할**: 밀도 추정의 "부드러움(smoothness)"을 조절하는 핵심 파라미터이며, 튜닝이 매우 중요함을 기억해야 합니다.
*   ⭐ **커널 함수 ($K$)**: 주로 가우시안 함수가 사용된다는 점을 기억하세요.

---

## Slide 20

- **핵심 개념**:
    *   **Box Plot (Tukey)**: 데이터의 중앙값, 사분위수 범위(IQR), 수염(whiskers), 이상치(outliers)를 시각화하여 데이터 분포의 견고한 요약을 제공합니다. 빠르고 읽기 쉽지만, 사분위수 내부의 데이터 분포 모양을 숨기는 단점이 있습니다.
    *   **Violin Plot**: Box plot에 커널 밀도 추정(KDE)을 추가하여 데이터 분포의 모양을 보여주는 시각화입니다. 다봉성(multimodality), 왜도(skewness), 꼬리 부분의 특징을 드러내어 Box plot보다 더 풍부한 정보를 제공합니다. KDE 사용으로 인해 `bandwidth` 매개변수에 민감하게 반응합니다.
    *   **Boxen Plot (Letter-Value Plot)**: Box plot과 유사하지만, 사분위수 외에 더 깊은 분위수(letter-values)를 시각화하여 데이터의 꼬리 부분을 보다 신뢰성 있게 보여주기 위해 설계되었습니다. 특히 데이터셋의 크기가 클($n$) 때 유용합니다.
    *   **핵심 차이점**: Box plot과 Violin plot의 가장 큰 차이점은 **KDE의 사용 여부**입니다. Violin plot은 KDE를 사용하여 분포의 밀도를 표현하는 반면, Box plot은 그렇지 않습니다.

- **코드/수식 해설**:
    *   강의 내용에서 언급된 `bandwidth`($h$)는 KDE(Kernel Density Estimation)에서 사용되는 핵심 매개변수입니다. KDE는 데이터 포인트 주변의 밀도를 추정하여 부드러운 확률 밀도 함수를 생성합니다.
    *   KDE는 다음과 같은 수식으로 표현될 수 있습니다:
        $$ \hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right) $$
        여기서 $K(\cdot)$는 커널 함수이고, $h$는 `bandwidth`입니다.
    *   `bandwidth` $h$는 커널 함수의 폭을 결정하여 추정된 밀도 곡선의 부드러움을 조절합니다.

- **구체적 예시**:
    *   **`bandwidth`($h$)의 중요성**: 마치 카메라의 초점(focus)과 같습니다.
        *   `h`가 **너무 작으면 (undersmooth)**: 초점이 너무 날카로워져서 노이즈가 많고, 불필요하게 튀는 부분이 많은(jagged and noisy) 이미지를 얻습니다. 데이터의 실제 분포가 아닌 샘플링의 결과로 인한 가짜 피크(spurious peaks)들이 많이 나타날 수 있습니다.
        *   `h`가 **너무 크면 (oversmooth)**: 초점이 너무 흐려져서 모든 것이 흐릿하고(blurry) 평평한(flat) 이미지를 얻게 됩니다. 데이터의 중요한 특징이나 실제 모드(genuine modes)를 놓쳐버릴 수 있습니다.
    *   목표는 데이터의 진정한 구조를 가장 잘 나타내는 **"스윗 스팟(sweet spot)"**을 찾는 것입니다.

- **강의 내용**:
    *   `bandwidth` $h$는 분포의 부드러움을 제어하는 **가장 중요한 매개변수**입니다.
    *   `h`가 너무 작으면(undersmooth) 플롯이 들쭉날쭉하고 노이즈가 많으며, 샘플링 아티팩트에 의한 수많은 가짜 피크를 생성할 수 있습니다.
    *   `h`가 너무 크면(oversmooth) 플롯이 흐릿하고 평평해져, 데이터의 진정한 모드와 중요한 구조를 놓치게 됩니다.
    *   적절한 `bandwidth`는 교차 검증(cross-validation)이나 플러그인 규칙(plug-in rules)을 통해 찾을 수 있습니다.
    *   다행히 Seaborn 라이브러리에서는 합리적인 데이터 기반의 기본 `bandwidth`를 자동으로 선택해 줍니다.
    *   사용자는 `bw_adjust` 매개변수를 통해 이 기본 `bandwidth`를 조정할 수 있습니다. 최종적으로 사용되는 `bandwidth`는 `bw_adjust` 값에 기본 `bandwidth`를 곱한 값입니다. 예를 들어, `bw_adjust=0.5`이면 기본 `bandwidth`의 절반을 사용합니다.

- **시험 포인트**:
    *   ⭐ Box plot, Violin plot, Boxen plot의 **각각의 정의와 목적, 그리고 주요 차이점**을 정확히 이해하고 설명할 수 있어야 합니다. 특히 Box plot과 Violin plot의 차이점(KDE 사용 여부)은 중요합니다.
    *   ⭐ Violin plot에서 `bandwidth`($h$) 매개변수의 역할과 이 값이 너무 작거나 클 때 발생하는 **플롯의 시각적 특징 및 문제점** (undersmoothing/oversmoothing)을 서술할 수 있어야 합니다.
    *   Seaborn에서 `bandwidth`를 조절하는 매개변수 `bw_adjust`의 역할.

---

## Slide 21

다음은 슬라이드 이미지와 음성 전사를 분석하여 작성한 마크다운 노트입니다.

---

### **핵심 개념**

이 슬라이드는 **박스 플롯(Box Plot)**의 구조와 기본 설정에 대해 다룹니다. 박스 플롯은 데이터의 분포를 다섯 가지 요약 통계량(five-number summary: 최소값, 1사분위수, 중앙값, 3사분위수, 최대값)을 기반으로 시각화하는 강력한 도구입니다.

*   **중앙선 (Median line)**: 상자 내에 있는 선으로, 데이터의 중앙값($Q_2$, 50th percentile)을 나타냅니다.
*   **상자 (Box)**: 데이터의 1사분위수($Q_1$, 25th percentile)부터 3사분위수($Q_3$, 75th percentile)까지의 범위를 나타냅니다. 이 상자의 길이는 **사분위 범위(IQR, Interquartile Range)**라고 불리며, 데이터의 중앙 $50\%$가 얼마나 퍼져있는지를 보여줍니다.
*   **수염 (Whiskers)**: 상자에서 뻗어 나오는 선으로, 일반적으로 $Q_1 - 1.5 \times \text{IQR}$에서 $Q_3 + 1.5 \times \text{IQR}$ 범위 내의 가장 극단적인 데이터 포인트까지 확장됩니다. 이는 데이터의 일반적인 변동 범위를 나타냅니다.
*   **이상치 (Outliers)**: 수염 바깥에 점으로 표시되는 데이터 포인트입니다. 이들은 $Q_1 - 1.5 \times \text{IQR}$보다 작거나 $Q_3 + 1.5 \times \text{IQR}$보다 큰 값들로, 일반적인 데이터 패턴에서 벗어난 값으로 간주됩니다. `seaborn`에서는 `showfliers=True`가 기본값입니다.

**박스 플롯의 장점:**
*   **견고함(Robust)**: 이상치에 덜 민감하여 데이터의 전반적인 분포를 잘 보여줍니다.
*   **간결함(Compact)**: 많은 양의 데이터를 요약하여 한눈에 파악하기 쉽습니다.
*   **그룹 비교에 탁월**: 여러 그룹의 중앙값과 데이터의 퍼짐(spread)을 효율적으로 비교할 수 있습니다.

**박스 플롯의 한계:**
*   데이터의 **다봉성(multimodality)**이나 사분위수(quartiles) 내의 **상세한 분포 모양**을 파악하기 어렵습니다. 예를 들어, 상자 안에 데이터가 두 개의 봉우리(peak)를 가지고 있더라도 박스 플롯으로는 이를 알 수 없습니다.

### **코드/수식 해설**

**1. 사분위 범위 (IQR) 계산:**
사분위 범위는 3사분위수와 1사분위수의 차이입니다.
$$ \text{IQR} = Q_3 - Q_1 $$

**2. 수염의 한계 (Whisker Limits) 및 이상치 판별:**
수염의 끝은 $Q_1$ 또는 $Q_3$에서 $\pm 1.5 \times \text{IQR}$ 떨어진 위치까지의 가장 극단적인 데이터 포인트입니다. 이 범위를 벗어나는 데이터는 이상치로 분류됩니다.
*   **하한 (Lower Bound)**: $Q_1 - 1.5 \times \text{IQR}$
*   **상한 (Upper Bound)**: $Q_3 + 1.5 \times \text{IQR}$
따라서, 데이터 포인트 $x$가 $x < Q_1 - 1.5 \times \text{IQR}$ 이거나 $x > Q_3 + 1.5 \times \text{IQR}$일 경우, $x$는 이상치로 간주됩니다.

**3. Seaborn 박스 플롯 설정:**
`seaborn` 라이브러리에서 박스 플롯을 그릴 때 다양한 파라미터를 조절할 수 있습니다.
*   `showfliers`: 이상치를 표시할지 여부를 결정합니다. (기본값: `True`)
*   `whis`: 수염의 길이를 조절합니다. 기본값은 $1.5 \times \text{IQR}$이며, `whis=(5, 95)`와 같이 설정하면 데이터의 5th percentile부터 95th percentile까지로 수염을 그릴 수 있습니다.
*   `notch`: `notch=True`로 설정하면 상자 중앙에 노치(notch)를 추가하여 중앙값의 신뢰구간을 시각화합니다. 두 박스 플롯의 노치가 겹치지 않으면 중앙값이 통계적으로 유의미하게 다르다고 해석할 수 있습니다.

### **구체적 예시**

학생들의 시험 점수 데이터를 박스 플롯으로 시각화하여 여러 반의 성적 분포를 비교하는 시나리오를 생각해 볼 수 있습니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 가상의 시험 점수 데이터 생성
np.random.seed(42) # 재현성을 위해 시드 설정

# 반 A 데이터 (정규 분포)
class_A_scores = np.random.normal(loc=75, scale=10, size=50) # 평균 75, 표준편차 10
# 반 B 데이터 (약간 낮은 평균, 높은 분산, 이상치 포함)
class_B_scores = np.random.normal(loc=65, scale=15, size=50)
class_B_scores = np.append(class_B_scores, [20, 110]) # 이상치 추가

# 데이터 프레임으로 통합하여 seaborn에서 사용하기 용이하게 만듦
data = pd.DataFrame({
    'Score': np.concatenate([class_A_scores, class_B_scores]),
    'Class': ['Class A'] * len(class_A_scores) + ['Class B'] * len(class_B_scores)
})

plt.figure(figsize=(10, 7))
sns.boxplot(x='Class', y='Score', data=data, palette='viridis', whis=1.5, showfliers=True)
plt.title('각 반의 시험 점수 분포 비교', fontsize=16)
plt.xlabel('반 (Class)', fontsize=14)
plt.ylabel('점수 (Score)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# notch=True 예시
plt.figure(figsize=(10, 7))
sns.boxplot(x='Class', y='Score', data=data, palette='plasma', notch=True)
plt.title('노치(Notch)를 포함한 박스 플롯', fontsize=16)
plt.xlabel('반 (Class)', fontsize=14)
plt.ylabel('점수 (Score)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```
위 예시에서 `Class A`와 `Class B`의 박스 플롯을 비교하여 각 반의 중앙값, 점수 범위, 그리고 이상치를 한눈에 파악할 수 있습니다. `notch=True` 옵션으로 중앙값의 신뢰구간을 비교할 수도 있습니다.

### **강의 내용**

교수님의 음성 전사는 현재 슬라이드의 주제인 **박스 플롯(Box Plot)**과는 다른 내용인 **KDE (Kernel Density Estimation, 커널 밀도 추정)**에 대한 설명입니다. 이는 이전 슬라이드나 다른 맥락에서 다루어진 내용일 수 있습니다.

**KDE (Kernel Density Estimation) 관련 교수님 강조 내용:**

*   **KDE 사용 시점**: 데이터에 내재된 숨겨진 행동(Moh's entailed behavior)을 밝히고자 할 때, 특히 과거 데이터의 제약을 넘어서고 싶을 때 KDE를 활용합니다.
*   **KDE의 강점**:
    *   서로 다른 그룹 간의 데이터 분포 **모양(shapes)을 비교**하는 데 매우 뛰어납니다.
    *   KDE는 ⭐**비모수적(non-parametric)** 방법론이라는 점이 핵심적인 강점입니다. 이는 데이터가 특정 분포를 따른다고 가정하지 않고, 실제 데이터로부터 분포를 추정하는 방식임을 의미합니다.
*   **KDE의 한계 및 해결책**:
    *   **데이터 경계 문제 (Data Boundaries)**: 표준 KDE는 데이터의 경계(예: 음수가 될 수 없는 값)를 인식하지 못합니다. 따라서 데이터가 특정 경계에 묶여 있을 때, KDE는 밀도를 그 경계 밖으로 '흘려보내어(spill the density over)' 왜곡된 분포를 추정할 수 있습니다.
    *   **편향 감소 방법**: 이러한 편향을 줄이기 위해 '반사(reflection)' 기법을 사용하거나, 데이터를 먼저 변환(transforming)하는 방법(예: 로그 함수를 사용하여 데이터를 `log` 변환)을 고려할 수 있습니다. 교수님께서는 "BW(Bandwidth)가 더 조절한 것이며"라고 반복적으로 언급하시며 대역폭 조절의 중요성을 강조했습니다. 대역폭은 KDE의 부드러움을 결정하는 핵심 파라미터입니다.
*   **그룹 비교 시 주의사항**:
    *   여러 그룹의 KDE를 비교할 때는 반드시 ⭐**일관된 설정(consistent setting)**을 사용해야 합니다. 특히, ⭐**공통된 축 범위(common axis limits)**를 설정하는 것이 중요합니다.
    *   밀도를 정규화(normalize)하여 단순한 **개수(count)보다는 분포의 모양(shape)을 비교**하는 데 집중해야 합니다.

### **시험 포인트**

*   ⭐ **박스 플롯의 5-number summary (최소값, $Q_1$, 중앙값, $Q_3$, 최대값) 및 각 구성 요소 (중앙선, 상자, 수염, 이상치)의 정의와 의미를 정확히 이해하고 설명할 수 있어야 합니다.**
*   ⭐ **사분위 범위(IQR)와 이상치($Q_1 - 1.5 \times \text{IQR}$ 및 $Q_3 + 1.5 \times \text{IQR}$ 기준)의 계산 방법을 숙지해야 합니다.**
*   ⭐ **박스 플롯의 주요 장점 (견고함, 간결함, 그룹 비교 용이)과 한계 (다봉성, 상세 분포 파악 어려움)를 명확히 구분하여 설명할 수 있어야 합니다.**
*   ⭐ (강의 내용 관련) **KDE가 비모수적(non-parametric) 방법론이라는 점과 그 의미**를 이해해야 합니다.
*   ⭐ (강의 내용 관련) **KDE의 데이터 경계 문제와 이를 해결하기 위한 대역폭(BW) 조절, 로그 변환 등의 방법**을 알고 있어야 합니다.
*   ⭐ (강의 내용 관련) **여러 그룹의 KDE를 비교할 때 일관된 설정(consistent setting)과 공통 축 범위(common axis limits)를 사용하는 것의 중요성**을 기억해야 합니다.

---

---

## Slide 22

### 바이올린 플롯 (Violin Plot)

---

- **핵심 개념**:
    *   **바이올린 플롯 정의**: 단일 수치 변수의 분포를 시각화하는 방법으로, 박스 플롯(Box Plot)에 커널 밀도 추정(KDE) 모양을 결합한 형태입니다. 데이터의 양적 요약(quantile summaries)과 함께 분포의 전체적인 모양(밀도)을 동시에 보여줍니다.
    *   **KDE Envelope**: 바이올린 플롯의 외부 윤곽선은 커널 밀도 추정(KDE)을 통해 얻은 밀도 함수를 중앙에 대칭적으로 미러링한 것입니다. 너비는 해당 지점의 데이터 밀도에 비례하며, 데이터가 밀집된 구간은 너비가 넓고, 드문 구간은 좁습니다.
    *   **Inner Marks**: 바이올린 플롯 내부에는 'quartile', 'box', 'point' 또는 'None'과 같은 다양한 마크를 사용하여 중앙값, 사분위수 등의 핵심 통계량을 표시할 수 있습니다. 슬라이드 예시에서는 박스 플롯의 요소(중앙값, $Q_1$, $Q_3$, 최소/최대)가 표시되어 있습니다.
    *   **Bandwidth (대역폭)**: KDE 계산 시 사용되는 중요한 파라미터로, 플롯의 매끄러움 정도를 결정합니다. 대역폭이 작으면 플롯이 'noisy'해지고, 너무 크면 'over-smooth'해져 실제 분포를 왜곡할 수 있습니다.
    *   **Robust Summaries (로버스트 통계량)**: 이상치(outliers)에 덜 민감하게 데이터의 중심 경향과 퍼짐을 나타내는 통계량입니다. 대표적으로 중앙값(Median), 사분위 범위(IQR), MAD(Median Absolute Deviation) 등이 있습니다.

- **코드/수식 해설**:
    *   **사분위 범위 (Interquartile Range, IQR)**:
        $IQR = Q_3 - Q_1$
        여기서 $Q_1$은 제1 사분위수(25th percentile)를, $Q_3$은 제3 사분위수(75th percentile)를 나타냅니다.

    *   **중앙값 (Median)**:
        데이터를 크기 순으로 정렬했을 때 중앙에 위치하는 값으로, 제2 사분위수($Q_2$) 또는 50th percentile이라고도 합니다.

- **구체적 예시**:
    *   **KDE의 유연성**: 데이터 분포가 단봉형(unimodal), 이봉형(bimodal), 다봉형(multimodal) 등 어떤 형태를 가지든, KDE는 이에 맞춰 유연하게 분포 모양을 시각화할 수 있습니다. 예를 들어, 시험 성적 데이터가 고득점과 저득점에 몰려 있는 경우(이봉형), 바이올린 플롯은 이를 명확하게 보여줄 수 있습니다.
    *   **대역폭의 영향**: 대역폭이 너무 작으면 데이터의 작은 변동에도 민감하게 반응하여 들쑥날쑥한(noisy) 모양을 만들 수 있고, 반대로 너무 크면 실제로는 구별되는 여러 봉우리를 하나의 매끄러운 봉우리로 뭉개버려(over-smooth) 정보 손실을 초래할 수 있습니다.

- **강의 내용**:
    *   교수님께서는 KDE가 **비모수적(non-parametric)**이라는 점을 강조하셨습니다. 이는 데이터가 특정 분포(예: 정규 분포)를 따른다는 엄격한 가정을 할 필요 없이, 데이터 자체의 모양에 맞춰 유연하게 밀도를 추정한다는 것을 의미합니다. 따라서 단봉형, 이봉형, 다봉형 등 다양한 형태의 데이터 분포를 정확하게 반영할 수 있습니다.
    *   `Median`, `IQR`, `MAD`와 같은 통계량들이 **로버스트 요약(robust summaries)**이라는 점을 강조하셨습니다. 특히 `median`은 50th percentile에 해당하며, `IQR`은 75th percentile($Q_3$)에서 25th percentile($Q_1$)을 뺀 값으로 정의된다고 설명하며, 이들이 이상치에 덜 영향을 받는 중요한 통계량임을 역설하셨습니다.

- **시험 포인트**:
    *   ⭐ **바이올린 플롯과 박스 플롯의 주요 차이점**: 바이올린 플롯은 박스 플롯의 퀀타일 요약 정보에 더해, KDE를 통해 데이터의 분포 밀도 모양까지 시각화한다는 점을 이해하는 것이 중요합니다. 박스 플롯은 퀀타일 요약만 보여줍니다.
    *   ⭐ **KDE의 비모수적 특성과 장점**: KDE가 데이터 분포의 형태에 대한 사전 가정 없이 다양한(단봉형, 이봉형, 다봉형 등) 분포를 유연하게 표현할 수 있다는 점을 설명할 수 있어야 합니다.
    *   ⭐ **IQR의 정의 및 로버스트 통계량으로서의 의미**: $IQR = Q_3 - Q_1$ 이라는 정의와 함께, IQR이 데이터의 중간 50% 범위의 퍼짐을 나타내며 이상치에 강건한(robust) 통계량이라는 점을 알아야 합니다.
    *   ⭐ **대역폭(bandwidth)이 KDE 및 바이올린 플롯에 미치는 영향**: 대역폭 설정에 따라 플롯이 너무 'noisy'하거나 'over-smooth'해질 수 있다는 점을 인지하고 있어야 합니다.

---

## Slide 23

**핵심 개념**:
*   **강건한 통계량 (Robust Summaries)**: 이상치(outliers)에 덜 민감하며 데이터의 중심 경향성과 퍼짐 정도를 안정적으로 나타내는 통계량입니다. 대표적으로 중앙값(median), 사분위 범위(IQR), 중앙값 절대 편차(MAD) 등이 있습니다.
*   **Box Plot (Tukey Plot)**: 데이터의 중앙값, IQR, 수염(whiskers), 그리고 이상치를 시각적으로 요약하여 보여주는 플롯입니다. 데이터 분포의 기본적인 특성을 빠르게 파악할 수 있지만, 사분위수 상자 내부의 실제 분포 형태는 숨겨지는 한계가 있습니다.
*   **Violin Plot**: Box Plot의 단점을 보완하기 위해 커널 밀도 추정(KDE, Kernel Density Estimate) 그래프를 추가한 플롯입니다. Box Plot이 제공하는 정보에 더해 데이터 분포의 다중 모드(multi-modality), 왜도(skewness), 꼬리(tails)와 같은 세부적인 형태를 시각적으로 보여줍니다.
*   **Boxen (Letter-Value) Plot**: Box Plot과 Violin Plot의 장점을 결합한 형태로, 여러 겹의 중첩된 상자(nested boxes)를 사용하여 중앙값으로부터 점진적으로 더 깊은(넓은 범위의) 분위수(quantile) 쌍을 시각화합니다. 이는 Box Plot이 숨기는 분포의 형태를 보다 상세하게 보여주면서도 Violin Plot보다 해석이 직관적일 수 있습니다. 각 상자는 꼬리 부분의 데이터 질량(tail mass)을 단계적으로 절반으로 줄여나가며 구성됩니다.

**코드/수식 해설**:
*   **중앙값 절대 편차 (Median Absolute Deviation, MAD)**:
    데이터셋 $X = \{x_1, x_2, \ldots, x_n\}$의 중앙값 $M = \text{median}(X)$가 있을 때, MAD는 다음과 같이 정의됩니다:
    $$ MAD = \text{median}(|x_i - M|) $$
    즉, 각 데이터 포인트가 중앙값으로부터 얼마나 떨어져 있는지의 절댓값 차이들의 중앙값입니다.
*   **Boxen Plot의 상자 구성**:
    Boxen Plot은 깊이(depth) $j = 1, 2, \ldots, k$에 따라 상자를 구성합니다.
    각 깊이 $j$에서 $p_j$는 다음과 같이 정의됩니다:
    $$ p_j = 2^{-j} $$
    깊이 $j$에서 그려지는 상자 $box_j$는 다음 분위수 범위에 해당합니다:
    $$ box_j = [Q_{p_j/2}, Q_{1-p_j/2}] $$
    이 상자가 포괄하는 데이터의 중앙 질량(central mass) 비율은 $1 - p_j$입니다.

**구체적 예시**:
Boxen Plot에서 각 깊이 $j$에 따른 상자의 퀀타일 범위는 다음과 같습니다:
*   $j=1$: $p_1 = 2^{-1} = 0.5$. $box_1 = [Q_{0.5/2}, Q_{1-0.5/2}] = [Q_{0.25}, Q_{0.75}]$.
    *   이는 25번째 백분위수부터 75번째 백분위수까지의 범위로, 일반적인 IQR 상자(Box Plot의 메인 상자)와 동일하며 데이터의 중앙 50%를 나타냅니다.
*   $j=2$: $p_2 = 2^{-2} = 0.25$. $box_2 = [Q_{0.25/2}, Q_{1-0.25/2}] = [Q_{0.125}, Q_{0.875}]$.
    *   이는 12.5번째 백분위수부터 87.5번째 백분위수까지의 범위로, 데이터의 중앙 75%를 나타냅니다.
*   $j=3$: $p_3 = 2^{-3} = 0.125$. $box_3 = [Q_{0.125/2}, Q_{1-0.125/2}] = [Q_{0.0625}, Q_{0.9375}]$.
    *   이는 6.25번째 백분위수부터 93.75번째 백분위수까지의 범위로, 데이터의 중앙 87.5%를 나타냅니다.
이러한 상자들은 깊이가 깊어질수록(바깥으로 갈수록) 너비나 두께를 줄여 시각적으로 중첩된 형태로 그려지며, 중앙값은 선으로 표시됩니다. 이를 통해 데이터 분포의 중심뿐만 아니라 꼬리 부분까지 점진적으로 살펴볼 수 있습니다.

**강의 내용**:
교수님은 **강건한 통계량**의 중요성을 강조하며, IQR과 MAD가 Box Plot의 기초가 됨을 설명했습니다. 특히, **MAD의 정의($\text{median}(|x_i - M|)$)**를 명확히 제시하며 이 개념을 기억해야 한다고 언급했습니다. Box Plot은 데이터를 빠르게 요약하고 여러 그룹을 한 번에 비교하기 용이하지만, **"메인 상자 내부의 분포 형태를 숨긴다"**는 본질적인 한계를 지적했습니다. 이러한 Box Plot의 단점을 보완하기 위해 **Violin Plot**이 Box Plot에 KDE 플롯을 추가하여 **"다중 모드, 왜도, 꼬리"**와 같은 분포의 상세한 형태를 드러내는 핵심적인 특징을 가진다고 강조했습니다. Boxen Plot은 이러한 Box Plot과 Violin Plot과 함께 데이터 분포를 강건하게 요약하고 시각화하는 데 사용되는 플롯 계열 중 하나로 소개되었습니다.

**시험 포인트**:
*   ⭐ **강건한 통계량(Robust Summaries)**인 IQR과 MAD의 정의와 중요성을 정확히 이해해야 합니다. 특히 MAD의 수식($MAD = \text{median}(|x_i - M|)$)과 의미를 기억하세요.
*   ⭐ **Box Plot의 장점** (빠른 요약, 이상치 시각화)과 **주요 단점** (상자 내부 분포 형태 은폐)을 명확히 구분하여 설명할 수 있어야 합니다.
*   ⭐ **Violin Plot이 Box Plot 대비 가지는 핵심적인 장점** (KDE를 통한 분포의 다중 모드, 왜도, 꼬리 등 세부 형태 시각화)을 설명할 수 있어야 합니다.
*   ⭐ **Boxen Plot의 정의와 상자 구성 원리**($p_j = 2^{-j}$ 및 $box_j = [Q_{p_j/2}, Q_{1-p_j/2}]$)를 이해하고, 각 깊이 $j$가 나타내는 분위수(예: $j=1$이 25%~75% IQR)를 설명할 수 있어야 합니다. 이는 Boxen Plot이 어떻게 데이터의 다양한 깊이의 중앙 집중 경향을 보여주는지 파악하는 데 필수적입니다.

---

## Slide 24

**핵심 개념**:
*   **Boxen Plot (Letter-Value Plot)**: `seaborn` 라이브러리의 `boxenplot`은 전통적인 Box Plot의 확장된 형태로, 특히 데이터의 양($N$)이 매우 많을 때 데이터 분포의 꼬리(tail) 부분을 더 세밀하게 시각화하기 위해 고안되었습니다. 다양한 "letter-value" (사분위수보다 더 깊은 백분위수)를 사용하여 여러 겹의 상자를 그려 데이터의 밀도 변화와 꼬리 부분의 분포를 상세하게 보여줍니다.
*   **Box Plot과의 비교**: 일반 Box Plot이 $Q_1, Q_2, Q_3$ 및 $1.5 \times IQR$ 범위의 이상치를 보여주는 데 반해, Boxen Plot은 더 많은 분위수(예: 1/8, 1/16 분위수 등)를 시각화하여 데이터 꼬리의 분포를 훨씬 더 신뢰성 있게 나타냅니다.
*   **`seaborn.boxenplot` 주요 옵션**:
    *   `k_depth`: 얼마나 많은 letter-value 레벨을 그릴지 정의합니다. `"tukey"` (기본값, 고전적인 이상치 기준), `"proportion"` (최소 꼬리 비율까지), `"trustworthy"` (샘플 크기에 따라 신뢰할 수 있는 만큼 깊게), 또는 정수 값으로 설정할 수 있습니다.
    *   `scale`: 수평 상자 너비가 깊이에 따라 어떻게 줄어들지 (예: `"exponential"`, `"linear"`, `"area"`) 결정합니다.
    *   `outlier_prop`: 이상치를 플래그하는 데 사용되는 꼬리 비율을 지정합니다.
    *   `showfliers`: 이상치 포인트를 그릴지 여부를 결정합니다.

**코드/수식 해설**:
일반적인 Box Plot의 구성 요소 및 정의는 Boxen Plot 이해의 기초가 됩니다.
*   $Q_1$ (First Quartile): 25th percentile. 데이터의 하위 25% 지점.
*   $Q_2$ (Median, Second Quartile): 50th percentile. 데이터의 중앙값.
*   $Q_3$ (Third Quartile): 75th percentile. 데이터의 상위 25% 지점.
*   $IQR$ (Interquartile Range, 사분위 범위): 중앙 50% 데이터가 포함되는 범위.
    $$IQR = Q_3 - Q_1$$
*   **수염 (Whisker)**: 일반적으로 이상치로 간주되지 않는 가장 극단적인 데이터 포인트를 나타냅니다.
    *   상한선: $Q_3 + 1.5 \times IQR$ 이내의 최대값
    *   하한선: $Q_1 - 1.5 \times IQR$ 이내의 최소값
    *   이 범위를 벗어나는 데이터 포인트는 이상치(outlier)로 표시됩니다.

**구체적 예시**:
*   **Box Plot (예시)**: 비교적 적은 수의(예: 수백 개) 학생들의 시험 점수 분포를 파악할 때, Box Plot은 중앙값, 25%, 75% 지점, 그리고 $1.5 \times IQR$ 범위 내의 극단값을 보여주어 전반적인 집중 경향과 대칭성을 빠르게 파악하기 좋습니다.
*   **Boxen Plot (예시)**: 수백만 건의 온라인 거래 금액 데이터를 시각화한다고 가정해 봅시다. 대부분의 거래는 낮은 금액대에 집중되어 있고, 소수의 매우 큰 금액 거래들이 꼬리 부분을 형성합니다. 이때 Box Plot만으로는 최상위 1%나 최하위 1%의 미묘한 분포 차이를 파악하기 어렵습니다. Boxen Plot은 여러 겹의 상자를 통해 $Q_1, Q_3$ 외에 12.5%, 87.5% ($Q_1 \pm 0.5 \times IQR$), 6.25%, 93.75% 등의 더 세분화된 분위수를 보여주어, 거래 금액 데이터의 꼬리 부분(고액 거래 또는 소액 거래)의 밀집도와 패턴을 훨씬 더 생생하고 상세하게 시각화할 수 있게 해줍니다.

**강의 내용**:
*   **Boxen Plot의 주 목적**: Boxen Plot (또는 letter-value plot)은 **`large N` (대규모 데이터)**을 위해 설계되었으며, 일반적인 Box Plot보다 "더 깊은 사분위수($Q_1, Q_2, Q_3$를 넘어선 letter-values)"를 제공하여 데이터의 **꼬리(tails) 부분을 훨씬 더 생생하게 시각화**할 수 있게 합니다. 대규모 데이터에서 꼬리 부분을 신뢰성 있게 시각화하고자 할 때 유용합니다.
*   **Box Plot vs. Boxen Plot vs. Violin Plot**:
    *   **Box Plot**과 **Violin Plot**은 일반적으로 **`small N` 또는 `medium N` (소규모 또는 중간 규모 데이터)**에 사용됩니다.
    *   **Boxen Plot**은 **`large N`**에 특화되어 꼬리 부분의 상세한 분포를 보여줍니다.
*   **Box Plot 기본 개념 강조**: 교수님은 Box Plot의 핵심 구성 요소들을 다시 한번 강조했습니다. 상자는 $Q_1$부터 $Q_3$까지의 `IQR`을 나타내며, 상자 안의 중앙선은 중앙값($Q_2$, 50th percentile)을 나타냅니다. 수염(whisker)은 일반적으로 $1.5 \times IQR$ 범위 내의 가장 극단적인 데이터 포인트까지 뻗어 나가며, 이 범위를 벗어나는 데이터는 이상치로 간주됩니다.
*   **Violin Plot과 KDE**: Box Plot과 Violin Plot의 가장 큰 차이점은 Violin Plot이 **`KDE` (Kernel Density Estimation)**를 사용하여 데이터 분포의 전체적인 형태를 시각화한다는 점입니다. (강의 음성에서 Boxen Plot이 KDE를 사용한다는 언급이 있었으나, 일반적으로 Boxen Plot은 Letter-Value 기반이며, KDE는 Violin Plot의 주요 특징입니다.)

**시험 포인트**:
*   ⭐ **Boxen Plot의 목적과 장점**: `large N` 데이터에서 꼬리(tail) 부분의 분포를 상세히 시각화하는 데 유용하며, 일반 Box Plot보다 더 깊은 분위수(letter-values)를 사용한다는 점을 이해하고 설명할 수 있어야 합니다.
*   ⭐ **Box Plot, Boxen Plot, Violin Plot 간의 주요 차이점**: 어떤 데이터 규모(`N`)에 적합한지, 그리고 각 플롯이 분포를 나타내는 방식(예: Box Plot은 사분위수, Violin Plot은 KDE, Boxen Plot은 여러 겹의 letter-values)을 구분할 수 있어야 합니다.
*   ⭐ **Box Plot의 핵심 구성 요소 및 정의**: $Q_1, Q_2, Q_3$, $IQR$, 그리고 수염($1.5 \times IQR$ 기준)의 의미를 정확히 알고 설명할 수 있어야 합니다.

---

## Slide 25

## 데이터분석 입문 (CSED226) 마크다운 노트

### 핵심 개념

*   **Box Plot (상자 그림)**
    *   데이터 분포를 시각화하는 표준적인 방법으로, 주로 연속형 변수의 중앙값, 사분위수, 이상치 등을 요약하여 보여줍니다.
    *   상자의 중앙선은 **중앙값(Median)**을 나타내며, 상자의 경계는 **첫 번째 사분위수($Q_1$)**와 **세 번째 사분위수($Q_3$)**를 나타냅니다.
    *   상자 길이는 **사분위 범위(IQR, Interquartile Range)**인 $Q_3 - Q_1$입니다.
    *   상자 밖으로 뻗어 나온 선을 **수염(Whiskers)**이라고 하며, 수염 밖의 점들은 **이상치(Outliers)**로 표시됩니다.
    *   데이터의 견고한(robust) 요약을 제공하며, 여러 그룹 간의 중앙값과 퍼짐(spread)을 비교하는 데 탁월합니다.
*   **Boxen Plot (Letter-Value Plot)**
    *   Box Plot의 일반화된 형태로, 특히 대규모 데이터셋의 꼬리(tail) 부분을 더 세밀하게 보여주기 위해 고안되었습니다.
    *   데이터를 더 많은 "Letter-Value" (상위/하위 사분위수를 여러 단계로 나눈 것)로 나누어 그립니다.
    *   이는 분포의 극단적인 부분(extreme parts)에 대한 추가적인 정보를 제공하며, Box Plot보다 덜 민감하게 이상치를 시각화할 수 있습니다.
    *   Seaborn 라이브러리에서 `boxenplot` 함수로 구현됩니다.
*   **Violin Plot (바이올린 그림)**
    *   Box Plot에 **커널 밀도 추정(KDE, Kernel Density Estimate)** 결과를 결합하여 데이터의 분포 밀도 정보를 추가한 시각화 방법입니다.
    *   중앙에 Box Plot과 유사한 요약 통계(중앙값, 사분위수 등)를 포함하고, 양쪽으로 데이터 밀도에 비례하는 폭을 가진 KDE 곡선이 대칭적으로 그려집니다.
    *   이를 통해 데이터의 중앙값과 사분위수뿐만 아니라 분포의 모양(예: 이봉성, 왜도)까지 한눈에 파악할 수 있습니다.

### 코드/수식 해설

*   **Box Plot 수염(Whisker) 길이 (강의 내용 기반)**
    교수님 음성에서 언급된 Box Plot의 수염 길이는 다음과 같습니다.
    $$ \text{이 수염의 길이는 상자 가장자리에서 } (1+5) \times \text{IQR 입니다.} $$
    즉, 이상치로 간주되는 지점은 통상적으로 다음과 같습니다.
    $$ \text{Lower Outlier Boundary} = Q_1 - (1+5) \times IQR = Q_1 - 6 \times IQR $$
    $$ \text{Upper Outlier Boundary} = Q_3 + (1+5) \times IQR = Q_3 + 6 \times IQR $$
    ⭐ **참고**: 일반적으로 Box Plot의 수염은 $Q_1 - 1.5 \times IQR$부터 $Q_3 + 1.5 \times IQR$ 범위 내의 가장 먼 데이터 포인트를 나타내며, 이 범위를 벗어나는 데이터는 이상치로 간주됩니다. 교수님이 언급하신 $1+5 \times IQR$ (즉, $6 \times IQR$)는 매우 넓은 범위로, 이상치를 더욱 엄격하게 정의하는 경우일 수 있습니다.

*   **`seaborn.boxenplot()` 함수**
    ```python
    sns.boxenplot(
        data,           # 데이터프레임
        x,              # X축 변수 (범주형 또는 연속형)
        y,              # Y축 변수 (연속형)
        hue,            # 그룹 비교를 위한 추가 범주형 변수
        k_depth,        # 상자의 깊이 (몇 개의 letter-value를 보여줄지).
                        # "tukey" (기본값, Box Plot과 유사), "trustworthy", 숫자 (예: 3) 등.
                        # 숫자는 해당 깊이까지의 분위수를 그림.
        width_method,   # 상자의 폭을 결정하는 방법. "exponential" (기본값), "linear" 등.
                        # 너비가 분위수 범위의 밀도를 반영하는 방식.
        outlier_prop,   # 이상치로 간주될 데이터의 비율 (k_depth="tukey"에서 사용).
                        # 이 비율을 벗어나는 데이터는 이상치로 처리.
        showfliers,     # 이상치(outliers)를 표시할지 여부 (True/False).
        dodge,          # hue 변수 사용 시 상자들을 겹치지 않게 옆으로 분리할지 여부.
        linewidth       # 상자, 수염, 이상치 마커 선의 두께
    )
    ```

### 구체적 예시

**1. Boxen Plot: 단일 분포 요약**
`k_depth="tukey"`는 표준 Box Plot과 유사하게 분위수를 사용하여 상자를 그립니다. `width_method="exponential"`은 상자의 폭이 데이터 밀도에 따라 지수적으로 변화하도록 합니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 가상의 데이터 생성 (실제 'wine' 데이터셋을 대신)
data_single = pd.DataFrame({'flavanoids': np.random.normal(5, 1.5, 200)})

ax = sns.boxenplot(data=data_single, x="flavanoids", k_depth="tukey",
                   width_method="exponential", outlier_prop=0.007,
                   showfliers=True, linewidth=1.2)
ax.set_xlabel("flavanoids")
ax.set_title("Boxen (letter-value) summary")
plt.show()
```

**2. Boxen Plot: 그룹 비교 (`hue` 사용)**
`hue` 파라미터를 사용하여 `class` 별로 `flavanoids` 분포를 비교합니다. `k_depth="trustworthy"`는 더 깊은 꼬리 정보를 신뢰성 있게 보여주며, `dodge=True`는 각 그룹의 Boxen Plot이 겹치지 않도록 분리합니다.

```python
# 가상의 데이터 생성
data_group = pd.DataFrame({
    'flavanoids': np.concatenate([np.random.normal(5, 1.5, 100), np.random.normal(7, 1, 100)]),
    'class': ['A']*100 + ['B']*100
})

ax = sns.boxenplot(data=data_group, x="class", y="flavanoids", hue="class",
                   dodge=True, width=0.8, k_depth="trustworthy",
                   width_method="linear", outlier_prop=0.01,
                   showfliers=True, linewidth=1.1)
ax.set_xlabel("class")
ax.set_ylabel("flavanoids")
ax.set_title("Boxen by class (deeper tail summaries)")
plt.show()
```

**3. Boxen Plot: 고정된 깊이 (`k_depth=3`)**
`k_depth`에 특정 숫자를 지정하여 상자의 깊이를 조절합니다. 예를 들어 `k_depth=3`은 Box Plot이 보여주는 것보다 더 많은 분위수를 세밀하게 보여주게 됩니다. `showfliers=False`로 설정하면 이상치를 그리지 않습니다.

```python
# 가상의 데이터 사용
data_fixed_depth = pd.DataFrame({'flavanoids': np.random.normal(10, 2, 200)})

ax = sns.boxenplot(data=data_fixed_depth, x="flavanoids", k_depth=3, showfliers=False)
ax.set_title("Fixed depth (k_depth=3) instructional view")
plt.show()
```

**4. Violin Plot:**
Box Plot과 유사하게 중앙값과 사분위수를 보여주지만, 양옆의 '바이올린' 모양은 데이터의 밀도 추정치를 나타냅니다. 예를 들어, 데이터가 이봉(bimodal) 분포를 가질 경우, 바이올린 그림은 두 개의 봉우리를 보여주어 Box Plot으로는 알 수 없었던 분포의 형태를 시각화할 수 있습니다.

```python
# 가상의 이봉 분포 데이터
data_bimodal = pd.DataFrame({
    'value': np.concatenate([np.random.normal(0, 1, 100), np.random.normal(5, 1, 100)])
})

plt.figure(figsize=(6, 4))
sns.violinplot(data=data_bimodal, y="value", inner="quartile") # inner="quartile"로 Box Plot 요소 표시
plt.title("Violin Plot showing bimodal distribution")
plt.show()
```

### 강의 내용

*   **Box Plot:**
    *   **수염 길이**: "이 수염의 길이는 상자 가장자리에서 $1+5$ times IQR입니다." (즉, $6 \times IQR$ 범위 밖을 이상치로 간주)
    *   수염 밖의 점들은 개별 **이상치(outlier)**로 그려집니다.
    *   **강건(robust)하며, 간결(compact)하고**, 여러 그룹 간의 **중앙값(mediums)과 퍼짐(spreads)을 비교하는 데 탁월**합니다.
    *   하지만 데이터가 **이봉성(bimodal)이거나 사분위수 내에 다른 흥미로운 모양**을 가지고 있는지 **드러낼 수 없습니다.**
    *   "이 Box Plot은 **가장 널리 사용되는 플롯**이라고 생각합니다. 따라서 Box Plot에 매우 익숙해져야 합니다."
*   **Violin Plot:**
    *   "Box Plot에 **KDE envelope**를 더한 것"입니다.
    *   "**미러링된(mirrored) KDE**"로, 플롯의 너비가 해당 지점의 **데이터 추정 밀도에 비례**합니다.
    *   바이올린 내부에 **무엇을 표시할지 지정**할 수 있습니다 (예: 사분위수, 미니 Box Plot, 개별 점 등).
    *   **KDE의 대역폭(bandwidth)이 중요**합니다.

### 시험 포인트

*   ⭐ **Box Plot의 기본 구성 요소와 해석**: 중앙값, 사분위수, IQR, 수염, 이상치에 대한 이해는 필수입니다.
*   ⭐ **교수님이 언급하신 Box Plot의 수염 정의**: 일반적인 $1.5 \times IQR$ 대신 **$1+5 \times IQR$ (즉, $6 \times IQR$)**을 기준으로 이상치를 판단하는 방식을 이해하고 있어야 합니다. (이 부분이 특이하므로 특히 주의!)
*   **Box Plot의 장단점**: 강건성, 비교 용이성, 간결성은 장점이지만, 이봉성 등 세부적인 분포 형태를 파악하기 어렵다는 한계를 명확히 이해해야 합니다.
*   **Violin Plot의 강점**: Box Plot의 정보를 포함하면서 **데이터의 분포 밀도(KDE)까지 시각화**하여 **이봉성 등 복잡한 분포 형태를 파악**할 수 있다는 점이 핵심입니다.
*   **Boxen Plot의 목적**: Box Plot보다 **데이터의 꼬리 부분(tails)을 더 상세하게 요약**하여 보여주며, 대규모 데이터셋에 특히 유용하다는 점을 알아야 합니다.
*   `sns.boxenplot`에서 `k_depth`, `width_method`, `showfliers` 등 **주요 파라미터들의 역할**을 이해하고 실제 코드를 해석할 수 있어야 합니다.

---

## Slide 26

**핵심 개념**:
*   **Box Plot (박스 플롯)**: 데이터의 중앙값($\text{median}$), 사분위수($\text{quartiles}$), 이상치($\text{outliers}$)를 보여주는 견고한 요약 통계 그래프입니다. 데이터의 전반적인 분포와 중심 경향, 퍼짐 정도를 파악하는 데 유용합니다.
*   **Violin Plot (바이올린 플롯)**: 박스 플롯에 커널 밀도 추정(KDE)을 통해 데이터의 분포 형태(밀도)를 추가로 시각화한 그래프입니다. 데이터의 왜도($\text{skew}$), 꼬리($\text{tails}$), 다중 봉우리($\text{multi-modality}$)를 명확하게 보여줄 수 있습니다.
*   **Boxen Plot (박센 플롯, Letter Value Plot)**: 일반 박스 플롯보다 더 깊은 분위수($\text{quantiles}$)를 여러 겹의 상자로 표시하는 플롯입니다. 특히 데이터 크기($\text{n}$)가 클 때 데이터의 꼬리 부분을 더 세밀하게 비교하는 데 효과적입니다.

**코드/수식 해설**:
*   **KDE (Kernel Density Estimation)**: 주어진 데이터 샘플을 기반으로 확률 밀도 함수($\text{PDF}$)를 추정하는 비모수적인 방법입니다. 각 데이터 포인트에 커널 함수(예: 가우시안 커널)를 배치하고 이들의 합을 통해 전반적인 밀도 곡선을 만듭니다. 바이올린 플롯에서 사용되는 KDE의 핵심 매개변수는 대역폭($\text{bandwidth}$, `bw_adjust`)으로, 이 값이 크면 부드러운 곡선이 되고 작으면 데이터 포인트에 더 민감한(덜 부드러운) 곡선이 됩니다.
*   **Boxen Plot의 분위수**: 박센 플롯은 중앙값($\text{median}$)을 시작으로, 데이터의 남은 꼬리 질량($\text{tail mass}$)을 각 단계마다 절반씩 줄여가며 대칭적인 분위수 쌍을 추가합니다. 예를 들어, 중앙값($\text{Q}_2$)에서 시작하여 다음 상자는 사분위수($\text{Q}_1, \text{Q}_3$)를 포함하고, 그 다음 상자는 8분위수($\text{Q}_{1/8}, \text{Q}_{7/8}$) 등을 나타내는 방식으로 깊은 분위수를 표시합니다.

**구체적 예시**:
*   **작은 샘플 크기($n < 50$)**: 데이터가 적을 때는 KDE의 민감도 때문에 바이올린 플롯이 실제와 다른 분포 형태를 보여줄 수 있습니다. 이럴 때는 **박스 플롯**과 함께 원본 데이터 포인트(`seaborn.stripplot` 또는 `seaborn.swarmplot` 등)를 함께 표시하여 오해를 방지하는 것이 좋습니다.
*   **데이터 분포 형태가 중요할 때**: 데이터가 단일 모드($\text{unimodal}$)인지, 여러 개의 봉우리($\text{multi-modal}$)를 가지는지, 혹은 특정 방향으로 치우쳐 있는지($\text{skewed}$)를 파악하고 싶을 때는 **바이올린 플롯**을 사용합니다. 예를 들어, 특정 그룹의 시험 점수 분포가 두 개의 봉우리를 가진다면, 이는 두 개의 다른 특성을 가진 하위 그룹이 존재할 수 있음을 시사합니다.
*   **큰 데이터셋의 꼬리 부분을 세밀하게 비교할 때**: 수십만, 수백만 개의 데이터 포인트가 있는 경우, 일반 박스 플롯은 5가지 요약 정보만 제공하므로 데이터의 극단적인 꼬리 부분에 대한 정보가 부족합니다. 이럴 때는 **박센 플롯**을 사용하여 더 많은 분위수 정보를 통해 꼬리 부분의 미묘한 차이를 파악할 수 있습니다.

**강의 내용**:
*   교수님께서는 KDE의 단점으로 "대역폭($\text{bandwidth}$)에 매우 민감하며 작은 샘플 크기에서 'misreading pumps' (오해의 소지가 있는 봉우리)를 생성할 수 있다"고 강조하셨습니다.
*   바이올린 플롯은 "박스 플롯 + KDE 쉐이며 위치에 인코드의 덴스티티를" (박스 플롯과 KDE 형태를 결합하여 데이터 밀도를 인코딩함) 보여주며, 박스 플롯은 "only shows quantile summaries" (오직 분위수 요약만 보여준다)고 설명하셨습니다.
*   박센 플롯(음성으로는 "boxed plot"이라고 언급됨)은 "letter value plot"이라고도 불리며, "a stack of nested boxes" (중첩된 상자의 스택)을 표시한다고 설명하셨습니다. 이는 "starts with the median and then adds progressively deeper symmetric quartile pairs that each half the remaining tail mass" (중앙값부터 시작하여 남은 꼬리 질량을 절반씩 줄여가며 점진적으로 더 깊은 대칭적인 분위수 쌍을 추가한다)고 자세히 설명하셨습니다.

**시험 포인트**:
*   ⭐ **Box, Violin, Boxen 플롯의 주요 차이점과 각 플롯이 강조하는 정보**: 박스 플롯은 견고한 요약, 바이올린 플롯은 분포의 형태(KDE 기반), 박센 플롯은 깊은 분위수(큰 $N$에 적합).
*   ⭐ **Violin 플롯에서 KDE의 역할과 장단점**: 분포의 형태를 시각화하는 강력한 도구이지만, 대역폭 선택과 작은 샘플 크기에 따라 "오해의 소지가 있는 봉우리"를 생성할 수 있다는 점.
*   ⭐ **샘플 크기($N$)에 따른 적절한 시각화 방법 선택**: 작은 $N$일 때는 박스 플롯과 원본 데이터 포인트를 함께, 큰 $N$일 때는 박센 플롯을 고려하는 기준.
*   ⭐ **Boxen 플롯의 "nested boxes" 개념**: 중앙값부터 시작하여 점진적으로 깊은 분위수를 표시하는 방식 이해.

---

## Slide 27

**핵심 개념**

*   **Box Plot (상자 그림)**: 데이터의 5가지 요약 통계량(최솟값, $P_{25}$ (1사분위수), 중앙값($P_{50}$), $P_{75}$ (3사분위수), 최댓값)을 시각화합니다. 상자(box)는 $P_{25}$부터 $P_{75}$까지의 IQR(사분위 범위)을 나타내며, 중앙선은 중앙값을 표시합니다. 수염(whiskers)은 데이터의 범위를 나타내고, 점은 이상치(outliers)를 표시합니다.
*   **Violin Plot (바이올린 그림)**: Box Plot과 함께 데이터의 분포 밀도(Kernel Density Estimate, KDE)를 시각화하여 데이터의 실제 분포 형태를 보여줍니다. Box Plot이 제공하는 요약 통계량 정보에 더해, 데이터가 어느 값에서 밀집되어 있는지, 다중 모드(multi-modal) 분포인지 등을 파악하는 데 유용합니다.
*   **Boxen Plot (Letter-Value Plot)**: Box Plot을 확장하여 데이터의 더 깊은 분위수(deeper quantiles)를 시각화하는 데 특화된 플롯입니다. 특히 대용량 데이터($N$이 큰 경우)에서 Box Plot보다 더 상세한 분포 정보를 제공하여 분포의 꼬리 부분이나 희귀한 값들의 패턴을 파악하기에 좋습니다. 여러 개의 상자가 겹쳐지며, 안쪽으로 갈수록 더 깊은 분위수를 나타내고, 상자의 폭과 두께가 점차 줄어들어 시각적으로 강조됩니다.

**코드/수식 해설**

아래 코드는 `matplotlib`과 `seaborn` 라이브러리를 사용하여 Box Plot, Violin Plot, Boxen Plot을 나란히 그리는 방법을 보여줍니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1행 3열의 서브플롯을 생성하고 전체 그림의 크기를 설정합니다.
fig, axes = plt.subplots(1, 3, figsize=(12, 3))

# 첫 번째 서브플롯에 Box Plot을 그립니다.
# 'wine' 데이터셋에서 'class'별 'alcohol' 분포를 나타냅니다.
sns.boxplot(data=wine, x="class", y="alcohol", ax=axes[0])
axes[0].set_title("Box") # 서브플롯 제목 설정

# 두 번째 서브플롯에 Violin Plot을 그립니다.
# 'inner="quartile"'은 바이올린 내부에 사분위수(IQR)를 표시하고,
# 'cut=0'은 밀도 곡선이 데이터 범위 밖으로 잘리지 않도록 합니다.
sns.violinplot(data=wine, x="class", y="alcohol", inner="quartile", cut=0, ax=axes[1])
axes[1].set_title("Violin") # 서브플롯 제목 설정

# 세 번째 서브플롯에 Boxen Plot을 그립니다.
sns.boxenplot(data=wine, x="class", y="alcohol", ax=axes[2])
axes[2].set_title("Boxen") # 서브플롯 제목 설정

# 서브플롯 간의 간격을 자동으로 조정하여 겹침을 방지합니다.
plt.tight_layout()
plt.show() # 그림을 화면에 표시합니다.
```

*   `plt.subplots(1, 3, figsize=(12, 3))`: 1행 3열의 서브플롯을 생성하고, 반환되는 `fig`는 전체 그림 객체, `axes`는 각 서브플롯의 축 객체 리스트입니다.
*   `sns.boxplot()`, `sns.violinplot()`, `sns.boxenplot()`: 각각 Box, Violin, Boxen Plot을 그리는 `seaborn` 함수입니다.
    *   `data`: 사용할 데이터프레임.
    *   `x`, `y`: x축과 y축에 매핑될 데이터프레임의 열 이름.
    *   `ax`: 그림을 그릴 `matplotlib` 축 객체.
*   `inner="quartile"` (Violin Plot): 바이올린 그림 내부에 사분위수(중앙값, $P_{25}$, $P_{75}$)를 선으로 표시하도록 지정합니다.
*   `cut=0` (Violin Plot): 커널 밀도 추정(KDE) 곡선이 데이터의 실제 범위 밖으로 확장되지 않도록 제한합니다.

**구체적 예시**

슬라이드 코드는 `wine` 데이터셋의 각 `class`별 `alcohol` 함량 분포를 시각화합니다.

*   **Box Plot**은 각 와인 클래스별 알코올 함량의 중앙값, 사분위수, 최솟값/최댓값 및 이상치를 빠르게 보여줍니다.
*   **Violin Plot**은 Box Plot의 정보에 더해 각 클래스별 알코올 함량의 밀도 분포를 보여줍니다. 예를 들어, 특정 알코올 함량 구간에 데이터가 더 밀집되어 있는지, 또는 분포가 양봉(bimodal) 형태인지 등을 알 수 있습니다.
*   **Boxen Plot**은 대용량 데이터에서 알코올 함량의 분포를 Box Plot보다 훨씬 세밀하게 보여줍니다. $P_{25}$에서 $P_{75}$ 사이의 IQR뿐만 아니라, 그보다 더 깊은 분위수들($P_{12.5}$에서 $P_{87.5}$, $P_{6.25}$에서 $P_{93.75}$ 등)을 여러 개의 상자로 표시하여 분포의 꼬리 부분까지도 상세하게 관찰할 수 있게 합니다.

**강의 내용**

*   **Boxen Plot의 분위수**:
    *   첫 번째 상자(가장 바깥쪽)는 일반 Box Plot처럼 $P_{25}$ (25번째 백분위수)부터 $P_{75}$ (75번째 백분위수)까지의 IQR을 나타냅니다.
    *   `j` (또는 `k_depth`) 파라미터가 깊이를 제어합니다. 만약 `j`가 $2$로 설정되면, 이는 $P_{12.5}$부터 $P_{87.5}$까지의 범위를 나타내는 상자를 그립니다. 즉, 더 깊은 분위수 정보를 시각화합니다.
    *   Boxen Plot의 상자들은 안쪽으로 갈수록 폭과 두께가 점차 감소하게 그려져, 더 깊은 분위수 구간이 시각적으로 강조됩니다.
    *   가운데 선은 중앙값(median)을 나타냅니다.
*   `seaborn.boxenplot`의 주요 옵션으로는 `k_depth`, `scale`, `width_method` 등이 있습니다. 특히 `k_depth`는 몇 단계의 분위수 레벨을 그릴지 제어하는 핵심 파라미터입니다.
*   **가이드라인**:
    *   데이터 샘플의 개수 $n$이 작을 때는 일반 Box Plot에 원본 데이터 점(`raw points`, 예: `stripplot`과 함께)을 함께 그리는 것이 분포 파악에 좋습니다.
    *   $n$이 큰 대용량 데이터에서는 Boxen Plot을 사용하여 더 깊은 분위수까지 상세하게 파악하는 것이 유용합니다.

**시험 포인트**

*   **Box, Violin, Boxen Plot의 특징 및 사용 시점 비교** ⭐: 각 플롯이 어떤 정보를 제공하고, 어떤 상황(데이터 크기, 필요 정보의 깊이 등)에서 가장 적합한지 이해하는 것이 중요합니다.
*   **Boxen Plot의 원리** ⭐: 여러 개의 상자가 겹쳐지며 더 깊은 분위수를 시각화하는 방식, 그리고 상자의 폭과 두께가 감소하는 시각적 효과에 대해 이해해야 합니다.
*   **`seaborn.boxenplot`의 `k_depth` 파라미터의 역할** ⭐: 이 파라미터가 Boxen Plot에서 몇 단계의 분위수 레벨을 그릴지 결정한다는 점을 기억하세요. `j=2`일 때 $12.5\%$에서 $87.5\%$를 의미하는 것과 같은 분위수 계산 방식도 중요합니다.

---

## Slide 28

## 데이터 시각화의 함정과 모범 사례 (Pitfalls & Best Practices)

### 핵심 개념

이 슬라이드는 데이터 시각화, 특히 `violin plot`과 `box plot`을 사용할 때 발생할 수 있는 문제점(pitfalls)과 이를 피하기 위한 모범 사례(best practices)를 다룹니다.

1.  **Overplotting (겹쳐 그리기 방지)**: 데이터 포인트가 너무 많아 겹쳐 보여 개별 관측치를 구별하기 어려운 상황을 의미합니다. 이를 해결하기 위해 `stripplot`이나 `swarmplot`을 사용하여 개별 데이터 포인트를 시각화하거나, 투명도(`alpha`)를 낮추는 방법이 있습니다.
2.  **Bandwidth sensitivity (Violin)**: `violin plot`은 커널 밀도 추정(KDE)을 기반으로 데이터 분포의 형태를 나타내므로, KDE의 대역폭(bandwidth) 설정에 민감합니다. 부적절한 대역폭은 실제 범위(`beyond-range tails`)를 벗어나는 왜곡된 분포를 표현할 수 있습니다. `bw_adjust` 및 `cut=0` 등의 옵션을 조절하여 이를 방지해야 합니다.
3.  **Outliers (Box)**: `box plot`은 이상치(outliers)를 시각화합니다. 이상치 결정 기준(whiskers)과 이상치 표시 여부(`showfliers`)를 명확하게 설정하고, 사용된 규칙을 문서화해야 합니다.
4.  **Scaling (스케일링)**: 여러 패널에 걸쳐 시각화할 때는 일관된 축 제한(limits)을 유지하고, `violin plot`에서 `scale` 모드(예: `area`, `count`, `width`)를 혼합하여 사용하지 않도록 주의해야 합니다.
5.  **Explain the summary (요약 설명)**: 시각화된 요약 정보(예: 중앙값, 사분위수, whisker, 이상치)가 무엇을 의미하는지 명확하게 레이블링하여 오해를 방지해야 합니다.

### 코드/수식 해설

강의에서 언급된 `violin plot`의 주요 파라미터와 개념은 다음과 같습니다:

*   **`bw_adjust` (Bandwidth adjustment)**: KDE의 대역폭을 조절하여 스무딩 정도를 변경합니다. 값이 클수록 더 부드러운 분포가 됩니다.
    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # 예시 데이터 로드
    tips = sns.load_dataset("tips")
    
    # bw_adjust 조절 예시
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    sns.violinplot(x="day", y="total_bill", data=tips, bw_adjust=0.5)
    plt.title("bw_adjust = 0.5")
    
    plt.subplot(1, 2, 2)
    sns.violinplot(x="day", y="total_bill", data=tips, bw_adjust=2.0)
    plt.title("bw_adjust = 2.0")
    plt.show()
    ```
*   **`cut=0`**: KDE의 추정 범위가 실제 데이터 범위(`range`)를 벗어나지 않도록 잘라내는 옵션입니다.
    ```python
    # cut=0 예시 (실제 데이터 범위 내에서만 KDE 그리기)
    sns.violinplot(x="day", y="total_bill", data=tips, cut=0)
    plt.title("Violin plot with cut=0")
    plt.show()
    ```
*   **`whis` (Whiskers in boxplot)**: `box plot`에서 whisker의 길이를 결정하는 파라미터입니다. 기본적으로 $1.5 \times \text{IQR}$ (사분위 범위)입니다.
    $$ \text{IQR} = Q_3 - Q_1 $$
    Lower whisker = $\max(Q_1 - \text{whis} \times \text{IQR}, \min(\text{data}))$
    Upper whisker = $\min(Q_3 + \text{whis} \times \text{IQR}, \max(\text{data}))$
*   **`showfliers` (Outliers in boxplot)**: `box plot`에서 whisker 바깥의 이상치를 점으로 표시할지 여부를 결정합니다.
    ```python
    # boxplot 파라미터 예시
    sns.boxplot(x="day", y="total_bill", data=tips, whis=1.5, showfliers=True)
    plt.title("Box plot with whis=1.5 and showfliers=True")
    plt.show()
    ```
*   **`scale` (Violin plot width method)**: `violin plot`의 수평 너비를 조절하는 방식입니다. `area` (전체 면적을 동일하게), `count` (관측치 수에 비례하게), `width` (최대 너비를 동일하게) 등이 있습니다. 강의에서는 "exponential or linear"와 같이 폭이 줄어드는 방식에 대한 개념적인 설명을 하셨습니다.

### 구체적 예시

*   **Overplotting 방지**:
    작은 샘플 사이즈($N < 50$)의 데이터를 시각화할 때, `box plot`만으로는 개별 데이터 포인트의 분포를 정확히 파악하기 어렵습니다. 이때 `box plot` 위에 `stripplot`을 겹쳐 그리면, 각 데이터 포인트의 위치를 시각적으로 확인할 수 있어 데이터의 밀집도나 특정 값의 존재 여부를 더욱 명확하게 이해할 수 있습니다. 예를 들어, `sns.boxplot(data=df)`와 `sns.stripplot(data=df, color='black', alpha=0.5)`를 함께 사용합니다.

*   **`violin plot`의 `transport` 옵션**:
    교수님이 언급하신 `transport` 옵션은 `violin plot`에서 샘플 사이즈가 허용하는 범위 내에서만 분포의 깊이(밀도 추정)를 표현하도록 하여, 샘플이 부족한 영역에서 과도한 외삽을 방지하는 개념으로 이해할 수 있습니다. 이는 `cut` 옵션과 유사하게 분포의 '꼬리' 부분을 신뢰할 수 있는 데이터 범위 내로 제한하는 효과가 있습니다.

### 강의 내용

*   **`violin plot` 강조**: `violin plot`은 KDE를 통해 데이터의 *형태(shape)*를 강조하는 데 유용합니다.
*   **`box plot` 강조**: `box plot`은 중앙값, 사분위수 등 데이터의 *강건한 요약(robust summaries)*을 강조합니다.
*   **선택 기준**:
    *   `violin plot`은 데이터 분포의 전체적인 모양과 밀도를 파악하고 싶을 때 좋습니다.
    *   `box plot`은 주요 통계량(중앙값, 사분위수)과 이상치를 빠르게 확인하고 싶을 때 좋습니다.
*   **⭐작은 샘플 사이즈 처리 ($N < 50$)**: 샘플 크기가 50개 미만으로 작을 때는 `box plot`을 사용하는 것이 더 적합합니다. 이 경우, `box plot` 위에 `stripplot`을 겹쳐 그려 원본 데이터 포인트들을 함께 시각화하는 것이 중요합니다. (`box plot` + `stripplot` = raw points 시각화).
*   `violin plot`의 다양한 옵션 언급: `key`, `transport`, `choice-worth`, `two-key` 옵션 등이 분포의 형태를 조절하는 데 사용될 수 있다고 언급하셨으며, 특히 `transport`는 샘플 크기에 따라 신뢰할 수 있는 깊이까지만 표현하도록 돕는다고 강조하셨습니다.
*   `width method`와 `scale` 옵션: `violin plot`의 가로 폭을 조절하는 "width method option"으로 `scale`이 있으며, `exponential` 또는 `linear` 방식으로 폭이 줄어들도록 조절할 수 있다고 언급하셨습니다.

### 시험 포인트

*   ⭐**`violin plot`과 `box plot`의 주요 목적 및 사용 상황 차이점**: `violin plot`은 분포의 `shape` (KDE), `box plot`은 `robust summaries` (Q1, 중앙값, Q3, 이상치)를 강조함을 이해해야 합니다.
*   ⭐**작은 샘플 사이즈 시각화 (특히 $N < 50$일 때)**: `box plot`을 사용하고, `stripplot`을 추가하여 `raw points`를 함께 보여주는 것이 모범 사례임을 기억하세요.
*   ⭐`violin plot`의 `bandwidth sensitivity` 및 관련 파라미터 (`bw_adjust`, `cut=0`)의 역할.
*   `box plot`에서 `outliers`를 다루는 방법 (`whis`, `showfliers`).
*   `overplotting`을 방지하기 위한 방법 (`stripplot`, `swarmplot`, `alpha`).
*   다양한 시각화 옵션(`key`, `transport`, `scale`의 `exponential/linear` 등)이 분포의 형태나 폭에 어떻게 영향을 미치는지 개념적으로 이해하고 있어야 합니다.

---

## Slide 29

---

### 핵심 개념

*   **Rug Plot**: 데이터 축(axis)을 따라 각 관측치마다 작은 눈금(tick)을 표시하여 데이터의 정확한 위치를 보여주는 1차원 시각화 기법입니다. 데이터 포인트의 실제 밀도와 분포를 직관적으로 파악하는 데 유용합니다.
*   **Strip Plot**: 1차원 산점도(scatter plot)의 한 형태로, 데이터 포인트가 겹쳐서 가려지는 현상(overplotting)을 방지하기 위해 각 점에 작은 무작위 '지터(jitter)'를 추가하여 모든 관측치를 개별적으로 볼 수 있게 합니다. 특히 범주형 변수에 따른 수치형 변수의 분포를 확인할 때 유용합니다.
*   **요약 플롯의 한계 보완**: `히스토그램(hist)`, `KDE(Kernel Density Estimation)`, `박스 플롯(box plot)`, `바이올린 플롯(violin plot)`과 같은 집계(aggregate) 기반의 플롯들은 데이터의 전반적인 분포를 보여주지만, 미세한 구조(microstructure)나 개별 관측치의 위치를 숨길 수 있습니다. `rug` 또는 `strip` 플롯을 함께 오버레이하여 이러한 요약 플롯이 실제 관측치 위치를 잘 반영하는지 **건전성 검사(sanity check)**를 수행할 수 있습니다.
*   **Jitter의 시각적 역할**: `strip plot`에서 사용되는 지터는 겹치는 포인트를 시각적으로 분리하기 위한 목적이며, 실제 데이터의 값 자체를 변경하는 것은 아닙니다. 따라서 지터링된 위치에서 통계량이나 값을 정량적으로 분석해서는 안 됩니다.

### 코드/수식 해설

`seaborn` 라이브러리는 `box plot`, `violin plot`, `boxen plot` 등 다양한 분포 시각화 도구를 제공하며, 이들을 활용하여 데이터의 분포를 탐색할 수 있습니다.

**Violin Plot의 `cut` 옵션:**

바이올린 플롯은 KDE를 사용하여 데이터의 밀도 분포를 보여줍니다. 이때 `cut` 옵션은 KDE 커널이 데이터의 최소값과 최대값 범위를 얼마나 벗어나서 꼬리를 그릴지 제어합니다. `cut=0`으로 설정하면 KDE가 데이터 범위 밖으로 꼬리를 그리는 것을 방지하여, 데이터에 존재하지 않는 분포가 그려져 오해를 불러일으키는 것을 막습니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 예시 데이터 생성
np.random.seed(42)
data = np.random.normal(loc=10, scale=2, size=50) # 중간 크기 샘플 n
df = pd.DataFrame({'value': data, 'category': ['A']*50})

# 세 개의 서브플롯을 가진 Figure 생성
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 첫 번째 서브플롯: Box Plot
sns.boxplot(y='value', data=df, ax=axes[0])
axes[0].set_title('Box Plot')

# 두 번째 서브플롯: Violin Plot (교수님 강조: cut=0 옵션 사용)
# 데이터가 적을 때 잘못된 해석을 줄이고, KDE가 데이터 범위 밖으로 확장되는 것을 방지
sns.violinplot(y='value', data=df, ax=axes[1], cut=0) # cut=0 설정
axes[1].set_title('Violin Plot (cut=0)')

# 세 번째 서브플롯: Boxen Plot (교수님 강조: 큰 샘플 사이즈에 유용)
# 꼬리 부분의 분포를 더 상세하게 보여줌
sns.boxenplot(y='value', data=df, ax=axes[2])
axes[2].set_title('Boxen Plot')

plt.tight_layout() # 서브플롯 간의 간격 자동 조절
plt.show()
```

### 구체적 예시

대학생들의 주당 공부 시간을 데이터로 가지고 있다고 가정해 봅시다.
*   **히스토그램**이나 **KDE**는 공부 시간 분포의 전반적인 형태(예: 정규 분포와 유사한지, 여러 봉우리가 있는지)를 보여줄 것입니다.
*   하지만 **`strip plot`**을 추가하면, 10시간 공부하는 학생이 몇 명인지, 15시간 공부하는 학생은 얼마나 되는지 등 정확히 같은 시간을 공부한 학생들의 수를 지터를 통해 시각적으로 분리하여 볼 수 있습니다. 만약 평범한 산점도였다면 모든 10시간 공부한 학생들이 한 점에 겹쳐 보여 몇 명인지 알 수 없었을 것입니다.
*   **`rug plot`**을 함께 사용하면, 예를 들어 30시간 이상 공부하는 학생들이 극소수 이상치로 보이는 경우, `rug` 눈금이 실제 해당 위치에 찍혀있는 것을 확인하여 해당 값이 실제로 존재하는 관측치임을 검증할 수 있습니다.
*   **`violin plot`**을 사용했는데, 만약 데이터의 범위가 0시간에서 40시간인데, `cut` 옵션을 사용하지 않아 KDE가 -5시간이나 45시간까지 꼬리를 그리는 경우, 이는 비현실적인 분포를 나타내므로 오해를 줄 수 있습니다. 이때 `cut=0`을 설정하여 실제 데이터 범위 안에서만 밀도를 보여주게 됩니다.

### 강의 내용

*   데이터의 양, 즉 샘플 크기 $n$이 적을 때 **바이올린 플롯(violin plot)**은 분포의 모양을 정확하게 나타내기 어려워 **오해의 소지**가 매우 클 수 있습니다. 이러한 경우 **박스 플롯(box plot)**이나 **스트립 플롯(strip plot)**을 사용하는 것이 더 적절합니다.
*   데이터의 **분포 형태(shape)**가 중요할 때는 바이올린 플롯을 사용하되, **`cut=0`** 옵션을 반드시 사용하여 KDE(Kernel Density Estimation)가 실제 데이터 범위 밖으로 꼬리를 그리는 것을 방지해야 합니다. `vm-adjust`와 `cut=0`은 이러한 과도한 KDE 꼬리를 막는 중요한 설정입니다.
*   **샘플 크기가 클 때(large sample size)**는 `seaborn.boxenplot` (강의 중 '박승plot' 또는 'boxon plot'으로 발음)을 고려하여 데이터의 꼬리 부분(tails)을 훨씬 더 신뢰성 있게 살펴볼 수 있습니다.
*   다양한 플롯을 비교할 때는 **축(axis)을 일관성 있게 유지**하여 공정한 비교가 가능하도록 해야 합니다.

### 시험 포인트

*   ⭐ **`Rug plot`**과 **`Strip plot`**이 `Box plot`이나 `Violin plot` 같은 집계(aggregate) 플롯이 숨기는 데이터의 **미세구조(microstructure)**를 어떻게 드러내고, 어떤 목적으로 사용되는지 설명할 수 있어야 합니다. (특히 **Sanity checks**, **small to medium $n$**, **Ties/discreteness**의 의미를 이해해야 합니다.)
*   ⭐ **`Strip plot`**의 `jitter` 기능이 **시각적인 목적**으로만 사용되며, 데이터의 실제 값을 변경하지 않는다는 점을 강조합니다. 지터링된 위치에서 통계량을 계산하는 오류를 범하지 않도록 주의해야 합니다.
*   ⭐ **`Violin plot`** 사용 시 데이터 수가 적을 경우 오해의 소지가 있다는 점과, 이를 방지하기 위한 `cut=0` 옵션의 중요성을 이해해야 합니다.
*   ⭐ **`Box plot`**, **`Violin plot`**, **`Boxen plot`**의 특징 및 각각이 어떤 데이터 샘플 크기($n$) 또는 어떤 분석 목적(전반적인 분포 vs 꼬리 부분 상세)에 더 적합한지 구분하여 설명할 수 있어야 합니다.

---

---

## Slide 30

**핵심 개념**
이 슬라이드는 데이터 시각화 시 발생할 수 있는 데이터 **오버플로팅(overplotting)** 문제를 해결하기 위한 디자인 선택과 모범 사례를 다룹니다. 특히 `rugplot`과 `stripplot`을 중심으로 데이터가 많을 때 점들이 겹쳐서 패턴을 파악하기 어려워지는 현상을 방지하는 기법들을 소개합니다. 주요 목표는 데이터의 스토리를 가장 잘 전달하는 플롯을 만드는 것입니다.

**코드/수식 해설**

*   **Rug Plot (`rugplot`)**: 데이터 분포를 축에 따라 작은 눈금(tick)으로 표시합니다.
    *   `height (axis fraction)`: 눈금의 높이를 축의 일정 비율로 설정합니다. 너무 크면 다른 시각화를 가릴 수 있으므로, 일반적으로 $0.02$에서 $0.05$ 사이의 값을 권장합니다.
    *   `lw/alpha`: 선의 두께($lw$)와 투명도($alpha$)를 조절하여 데이터 포인트 $n$이 많을 때 눈금이 겹쳐 어두운 띠를 형성하는 것을 방지합니다. 얇고 반투명하게 설정하는 것이 좋습니다.
    *   `orientation`: 눈금의 방향을 `x=` (수평) 또는 `y=` (수직)로 설정합니다.

*   **Strip Plot (`stripplot`)**: 개별 데이터 포인트를 흩뿌려 표시합니다.
    *   `jitter (float or True)`: ⭐ **지터(Jitter)**는 데이터 포인트의 겹침(overlap)을 해소하기 위해 각 포인트의 위치에 작은 무작위 노이즈를 추가하는 기법입니다. `float` 값으로 노이즈의 강도를 조절하거나 `True`로 설정하여 자동 적용할 수 있습니다. 너무 강한 지터는 노이즈처럼 보여 데이터의 실제 분포를 왜곡할 수 있으므로 적절한 강도가 중요합니다.
    *   `alpha, size`: 데이터 포인트 $n$이 증가함에 따라 마커의 투명도($alpha$)를 낮추고 크기($size$)를 줄여 오버플로팅을 줄일 수 있습니다.
    *   `dodge with hue`: 범주형 데이터가 있을 때 `hue` 인자를 사용하여 각 `x` 레벨 내에서 범주별로 점들을 분리하여 표시함으로써 겹침 문제를 완화하고 비교를 용이하게 합니다.

*   **데이터 $n$이 많을 때의 전략**:
    *   **다운샘플링(Downsample)**: 데이터의 양이 너무 많을 경우, 전체 데이터의 일부만을 사용하여 시각화합니다.
    *   **얇고 투명한 Rug 사용**: `rugplot`에서 `lw`와 `alpha`를 조절하여 사용합니다.
    *   **Swarm Plot (`swarmplot`) 사용**: 중간 규모($n$)의 데이터에 적합하며, 자동으로 데이터 포인트 간의 겹침을 방지하여 각 포인트를 명확하게 볼 수 있게 합니다.
    *   **집계(Aggregates) 플롯과 결합**: 히스토그램(`hist`), 커널 밀도 추정(`KDE`), 경험적 누적 분포 함수(`ECDF`)와 같은 요약 통계량 시각화와 함께 사용하면 개별 데이터 포인트(`atoms`)는 보조적인 역할로 미묘하게 표현하면서 전체적인 분포를 효과적으로 전달할 수 있습니다.

**구체적 예시**
수십 개의 데이터 포인트가 정확히 같은 $x$ 좌표를 가지는 상황을 가정해 봅시다. 이 경우 일반적인 산점도(scatter plot)에서는 이 모든 점들이 하나의 점으로 겹쳐 보여 실제 데이터의 양을 파악하기 어렵습니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 같은 x 값을 가진 데이터 생성
data_narrow = np.repeat([1, 2, 3], 10) + np.random.rand(30) * 0.01 # 좁은 공간에 여러 점

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.stripplot(x=data_narrow, color="blue", size=5)
plt.title("Without Jitter (Overplotting)")

plt.subplot(1, 2, 2)
sns.stripplot(x=data_narrow, jitter=0.2, color="green", size=5) # jitter 적용
plt.title("With Jitter (Resolved Overlap)")

plt.tight_layout()
plt.show()
```
위 예시에서 `jitter=0.2`를 적용하면 겹쳐 보이는 점들이 옆으로 퍼져나가면서 각 점의 존재를 확인할 수 있게 됩니다. 이는 마치 한 줄로 서 있던 사람들이 좁은 공간에 빽빽하게 모여 있다가 조금씩 옆으로 비켜 서서 서로를 볼 수 있게 되는 것에 비유할 수 있습니다. `swarmplot`은 `stripplot`의 `jitter`보다 더 정교하게 점들이 겹치지 않도록 자동으로 배치해줍니다.

**강의 내용**
교수님께서는 슬라이드의 내용이 "데이터의 스토리를 가장 잘 전달하는 플롯을 탐색하는 좋은 방법"이라고 강조하셨습니다. 특히 **오버플로팅(overplotting)**이 흔한 문제임을 지적하며, 많은 데이터 포인트가 좁은 공간에 밀집될 때 시각화가 지저분해지는 "mess" 상태가 된다고 설명하셨습니다.
이 문제에 대한 해결책으로 `stripplot`의 `jitter` 사용을 강력히 추천하셨습니다. **지터(jitter)**는 "매우 좁은 공간에 많은 점을 그릴 때 좋지 않으므로, 점의 위치에 약간의 노이즈를 추가하여 그림에서 겹침이 많이 발생하지 않도록 하는 것"이라고 상세히 설명하셨습니다.
더 나은 방법으로 **`swarmplot`**을 언급하시며, 이는 자동으로 겹침을 피하는 시각화 방식이라고 하셨습니다. 이러한 기법들은 특히 "아주 많은 데이터"보다는 "중간 규모($n$)"의 데이터에서 오버플로팅을 피하는 데 유용하다고 덧붙이셨습니다.

**시험 포인트**
*   ⭐ **오버플로팅(Overplotting) 문제와 그 해결책**에 대해 설명하고 시각화 예시를 드는 문제가 출제될 수 있습니다.
*   ⭐ **지터(Jitter)**의 개념과 `stripplot`에서의 역할에 대해 설명하고, `jitter`를 사용하지 않았을 때의 문제점과 사용했을 때의 효과를 비교 설명하는 문제가 나올 수 있습니다.
*   `stripplot`과 `swarmplot`의 차이점 및 각각 어떤 상황에 더 적합한지 비교하는 문제가 출제될 수 있습니다. 특히 `swarmplot`이 "자동으로 겹침을 피한다(avoids overlap)"는 특징과 "중간 규모의 데이터($n$)"에 적합하다는 점을 기억하세요.
*   데이터 $n$이 클 때 시각화를 개선하기 위한 다른 방법들 (다운샘플링, 투명도/크기 조절, 집계 플롯과 결합)도 중요하게 다뤄질 수 있습니다.

---

## Slide 31

**핵심 개념**
*   **러그 플롯 (Rug Plot)**: 데이터의 '원자'(atoms), 즉 개별 관측치를 시각적으로 표현하는 방법입니다. 각 데이터 포인트를 축을 따라 작은 눈금($\text{tick}$)으로 표시하여, 데이터가 어느 구간에 밀집되어 있는지 직관적으로 파악할 수 있게 해줍니다. 주로 커널 밀도 추정(KDE) 플롯과 함께 사용되어 밀도 추정 곡선과 실제 데이터 분포를 동시에 보여줍니다.
*   **스트립 플롯 (Strip Plot)**: 1차원 스캐터 플롯($\text{1D scatter plot}$)의 한 형태로, 각 관측치를 점으로 표시합니다. 특히 범주형 변수에 따라 데이터를 그룹화하고 각 그룹 내에서 개별 데이터 포인트의 분포를 시각화할 때 유용합니다. 데이터 포인트가 겹치는 현상을 줄이기 위해 $\text{jitter}$ 옵션을 사용할 수 있습니다.
*   **투명도 ($\text{alpha}$)**: 시각화에서 요소의 투명도를 설정하는 파라미터입니다. 여러 플롯을 겹쳐서 그릴 때 특정 요소의 가시성을 조절하는 데 사용됩니다. $0$은 완전 투명, $1$은 완전 불투명을 의미합니다.

**코드/수식 해설**

1.  **Rug + KDE (Diabetes: bmi)**:
    ```python
    fig, ax = plt.subplots()
    sns.kdeplot(data=diabetes, x="bmi", ax=ax, bw_adjust=1.0)
    sns.rugplot(data=diabetes, x="bmi", ax=ax, height=0.03, lw=0.6, alpha=0.5)
    ax.set_title("KDE + Rug (bmi)"); ax.set_ylabel("density")
    ```
    *   `sns.kdeplot(...)`: 당뇨병 데이터셋의 $\text{bmi}$($\text{Body Mass Index}$)에 대한 커널 밀도 추정 플롯을 그립니다. $\text{bw\_adjust}$는 대역폭 조절 계수입니다.
    *   `sns.rugplot(...)`: 동일한 $\text{bmi}$ 데이터에 대한 러그 플롯을 그립니다.
        *   $\text{height}$: 각 눈금($\text{tick}$)의 높이를 설정합니다.
        *   $\text{lw}$: 눈금($\text{tick}$)의 선 두께($\text{linewidth}$)를 설정합니다.
        *   $\text{alpha}$: 눈금($\text{tick}$)의 투명도를 $0.5$로 설정하여 KDE 플롯과 겹쳐도 자연스럽게 보이게 합니다.

2.  **Strip by group (Iris species vs sepal length)**:
    ```python
    fig, ax = plt.subplots()
    sns.stripplot(data=iris, x="species", y="sepal length (cm)",
                  jitter=0.25, alpha=0.6, size=3, ax=ax)
    ax.set_title("Strip: species vs sepal length (cm)")
    ```
    *   `sns.stripplot(...)`: 붓꽃(Iris) 데이터셋의 $\text{species}$ (종)별 $\text{sepal length (cm)}$ (꽃받침 길이) 분포를 스트립 플롯으로 시각화합니다.
        *   $\text{jitter=0.25}$: 동일한 위치에 여러 데이터 포인트가 겹쳐서 잘 보이지 않는 것을 방지하기 위해 각 점에 약간의 무작위 노이즈를 추가합니다. $0$이면 노이즈가 없고, 값이 클수록 더 많이 분산됩니다.
        *   $\text{alpha=0.6}$: 점의 투명도를 $0.6$으로 설정합니다.
        *   $\text{size=3}$: 각 점의 크기를 설정합니다.

**구체적 예시**
*   **KDE + Rug (bmi) 플롯**: $\text{bmi}$ 분포를 부드러운 곡선(KDE)으로 보여주면서, x축 아래에 작은 눈금(러그)들을 통해 각 $\text{bmi}$ 데이터 포인트가 실제로 어디에 위치하는지 정확하게 보여줍니다. 이로써 KDE 곡선이 데이터의 실제 밀집도를 얼마나 잘 반영하고 있는지 시각적으로 확인하는 데 도움이 됩니다. 예를 들어, KDE 곡선이 높은 봉우리를 형성하는 부분에 러그 눈금들이 촘촘하게 모여 있는 것을 볼 수 있습니다.
*   **Strip: species vs sepal length (cm) 플롯**: 세 가지 붓꽃 종($\text{setosa}$, $\text{versicolor}$, $\text{virginica}$) 각각에 대해 꽃받침 길이($\text{sepal length}$)의 개별 측정값을 점으로 보여줍니다. $\text{jitter}$ 옵션 덕분에 각 종 내에서 꽃받침 길이의 분포가 점들이 겹치지 않고 펼쳐져서 각 개별 데이터의 값과 분포의 형태를 한눈에 파악할 수 있습니다. 예를 들어, $\text{setosa}$ 종의 꽃받침 길이가 $\text{4.5cm}$에서 $\text{6.0cm}$ 사이에 밀집되어 있음을 시각적으로 확인할 수 있습니다.

**강의 내용**
*   교수님은 러그 플롯($\text{rug plot}$)을 "rock plot"이라고 발음하셨으나, 슬라이드와 코드에 따르면 러그 플롯이 맞습니다.
*   러그 플롯과 스트립 플롯은 모두 데이터의 '원자'(atoms of your data), 즉 **개별 관측치**를 시각적으로 보여주는 데 목적이 있습니다.
*   러그 플롯은 단순히 작은 눈금($\text{small ticks}$)의 집합으로, 한 축을 따라 각 관측치($\text{one observation per tick}$)를 나타냅니다.
*   스트립 플롯은 1차원 스캐터 플롯($\text{1D scatter plot}$)이라고 설명하셨습니다.
*   이전 슬라이드에서 다루었던 박스 플롯에 대해, $\text{whisker}$와 $\text{show\_flyers}$ 설정을 신중하게 사용하여 이상치($\text{outlier}$)를 명확히 보여줄 것을 강조하셨습니다. 청중이 박스 플롯의 모든 요소(중앙값, 사분위수 등)를 안다고 가정하지 말고, 사용된 규칙을 항상 문서화하고 레이블을 명확히 할 것을 당부하셨습니다.
*   $\text{alpha}$ 파라미터는 플롯 요소의 투명도를 설정하는 데 사용됩니다.

**시험 포인트**
*   ⭐ **러그 플롯**과 **스트립 플롯**의 기본 정의와 목적을 설명할 수 있어야 합니다. (개별 데이터 포인트를 시각화하여 분포의 '원자'를 보여줌)
*   ⭐ $\text{sns.rugplot}$ 및 $\text{sns.stripplot}$ 함수의 사용법과 주요 파라미터(특히 $\text{alpha}$, $\text{jitter}$, $\text{height}$)의 역할을 설명할 수 있어야 합니다.
*   ⭐ **$\text{stripplot}$에서 $\text{jitter}$ 파라미터가 왜 필요한지, 어떤 역할을 하는지** 명확히 이해해야 합니다. (겹치는 점들을 분산시켜 가시성 향상)
*   러그 플롯을 KDE 플롯과 함께 사용하는 이유(밀도 추정 곡선과 실제 데이터 분포의 관계 확인)를 설명할 수 있어야 합니다.
*   ⭐ 이전 슬라이드에서 언급된 내용이지만, 박스 플롯에서 **$\text{show\_flyers}$**의 중요성과 이상치 시각화의 필요성을 기억해야 합니다.

---

## Slide 32

**핵심 개념**: Q-Q Plot (Quantile-Quantile Plot)은 데이터의 분포가 특정 이론적 분포(참조 분포)를 따르는지 시각적으로 확인하는 데 사용되는 강력한 통계적 시각화 도구입니다. 특히, 데이터가 정규 분포를 따르는지, 분포의 꼬리(tail) 부분이 어떤 특성을 가지는지, 그리고 이상치(outliers)가 존재하는지 진단하는 데 유용합니다.

**코드/수식 해설**:
Q-Q 플롯은 주어진 샘플 데이터 $x_{1:n}$의 순서 통계량(order statistics) $x_{(i)}$와 참조 분포 $F$의 분위수(quantile)를 비교하여 점을 그립니다.
1.  **순서 통계량**: 샘플 데이터 $x_1, \ldots, x_n$를 오름차순으로 정렬한 것이 $x_{(1)}, x_{(2)}, \ldots, x_{(n)}$입니다.
2.  **확률 계산**: 각 순서 통계량에 해당하는 경험적 확률 $p_i$는 일반적으로 다음 수식으로 계산됩니다:
    $$ p_i = \frac{i-0.5}{n}, \quad \text{for } i = 1, \ldots, n $$
    여기서 $i$는 순위(rank)이고, $n$은 데이터 포인트의 총 개수입니다.
3.  **Q-Q 플롯의 점**: Q-Q 플롯은 각 $i$에 대해 다음 쌍을 점으로 그립니다.
    $$ (F^{-1}(p_i), x_{(i)}) $$
    여기서 $F^{-1}(p_i)$는 참조 분포 $F$의 $p_i$ 분위수에 해당하는 값입니다. 즉, x축은 이론적 분위수, y축은 관측된 데이터의 분위수를 나타냅니다.

**구체적 예시**:
*   **정규성 확인**: 만약 데이터가 표준 정규 분포를 따른다고 가정하고, 참조 분포 $F$를 표준 정규 분포로 설정하면, Q-Q 플롯의 점들은 대략적으로 기울기가 $1$이고 y절편이 $0$인 직선 위에 놓이게 됩니다.
    *   **직선**: 데이터 분포가 참조 분포와 매우 유사함을 나타냅니다.
    *   **곡선 형태**: 데이터가 참조 분포와 다름을 시사합니다. 예를 들어, 플롯이 S자 형태로 휘어지면 데이터의 꼬리 부분이 참조 분포보다 두껍거나 얇음을 의미할 수 있습니다.
    *   **양 끝의 이탈**: 직선에서 멀리 벗어난 점들은 해당 데이터가 이상치(outliers)일 가능성을 나타냅니다.
*   **선형 모델의 잔차 분석**: 선형 회귀 모델을 구축한 후, 모델의 가정이 유효한지 확인하기 위해 잔차(residuals)의 정규성을 Q-Q 플롯으로 검사할 수 있습니다. 잔차가 정규 분포에 가까울수록 모델 가정이 잘 충족된다고 판단할 수 있습니다.

**강의 내용**:
제공된 강의 음성 전사는 Q-Q Plot 슬라이드와 직접적으로 일치하지 않습니다. 음성 전사는 주로 산점도(scatter plot), 지터(jitter), 러그 플롯(rug plot), 스트립 플롯(strip plot)에 대한 내용을 다루며, 이러한 시각화가 히스토그램, KDE, 박스플롯과 같은 집계(aggregate) 방식이 감추는 "기저의 미시 구조(underlying microstructures)"를 드러내어 "sanity check" 역할을 한다고 강조합니다. 특히 "jitter"가 오버랩을 피하고 이산적이고 묶인 값(discrete and tied values)을 드러내는 데 도움이 된다고 설명합니다.

슬라이드 자체의 "Motivation" 섹션은 Q-Q Plot의 핵심 사용 목적을 다음과 같이 설명합니다:
*   **모델 검증 (Model checks)**: 선형 모델의 잔차가 정규 분포를 따르는지 등 통계 모델의 가정을 확인하는 데 사용됩니다.
*   **분포 형태 진단 (Shape diagnostics)**: 플롯의 곡률은 데이터의 왜도(skew)를, 꼬리 부분의 발산은 데이터의 꼬리가 무거운지(heavy tails) 가벼운지(light tails)를 보여줍니다.
*   **이상치 (Outliers)**: 직선에서 크게 벗어난 양 끝의 점들은 비정상적인 극단값(unusual extremes) 즉, 이상치를 나타내는 신호입니다.

"Reading the line" 섹션에서는 Z-점수화된(z-scored) 데이터와 정규 분포를 비교할 때, Q-Q 플롯의 기울기가 약 $1$이고 y절편이 약 $0$이면 좋은 적합(good fit)을 의미한다고 설명합니다. 체계적인 곡률(systematic curvature)은 데이터가 참조 분포에 부적합(misfit)하다는 것을 나타냅니다.

**시험 포인트**:
*   ⭐ **Q-Q Plot의 정의 및 목적**: 데이터의 분포가 특정 이론적 분포(특히 정규 분포)를 따르는지 시각적으로 확인하는 데 사용되는 도구임을 이해해야 합니다.
*   ⭐ **Q-Q Plot의 구성 원리**: $(F^{-1}(p_i), x_{(i)})$ 쌍을 그리는 방식과 $p_i = \frac{i-0.5}{n}$ 수식을 정확히 알아야 합니다.
*   ⭐ **Q-Q Plot 해석**:
    *   점이 **직선에 가까울수록** 데이터가 참조 분포와 유사하다는 의미입니다.
    *   **곡선 형태**는 왜도(skewness)나 꼬리 특성(heavy/light tails)의 차이를 나타냅니다.
    *   **직선에서 벗어난 끝점들**은 이상치(outliers)를 시사합니다.
*   ⭐ **Q-Q Plot의 활용 분야**: 모델 가정 검증(예: 잔차의 정규성), 분포의 형태 진단(왜도, 꼬리 특성), 이상치 탐지에 사용됨을 숙지해야 합니다.
*   ⭐ 특히 Z-점수화된 데이터와 표준 정규 분포를 비교할 때, **기울기 $\approx 1$, y절편 $\approx 0$**가 좋은 적합을 의미한다는 점을 기억해야 합니다.

---

## Slide 33

## Q-Q 플롯 심화 및 모범 사례 (Q-Q Variants & Good Practices)

### 핵심 개념
Q-Q 플롯(Quantile-Quantile plot)은 데이터의 분포가 특정 이론적 분포(예: 정규 분포)를 따르는지 시각적으로 확인하는 데 사용되는 강력한 통계 도구입니다. 데이터의 양자(quantile)를 참조 분포의 이론적 양자와 비교하여 플롯합니다. 이를 통해 데이터의 정규성(normality)을 확인하고, 분포의 꼬리(tails) 부분이 이론적 분포와 어떻게 다른지 진단할 수 있습니다.

**Q-Q 플롯의 활용 변형:**
*   **다양한 분포와의 비교**: 정규 분포 외에도 Student's t-분포(`"t"`), 지수 분포(`"expon"`), 카이제곱 분포(`"chi2"`) 등 다양한 이론적 분포와 데이터의 양자를 비교하여 더 적합한 분포를 찾을 수 있습니다. 이때, 각 분포의 매개변수를 적절히 선택해야 합니다.
*   **모델 잔차(Model Residuals) 분석**: 회귀 모델 등 통계 모델의 잔차가 특정 분포(일반적으로 정규 분포)를 따르는지 확인하는 데 Q-Q 플롯을 적용할 수 있습니다. 이는 모델의 가정을 평가하는 중요한 단계입니다.

**Q-Q 플롯 사용 시 모범 사례:**
*   **정규화(Standardization)**: 정규 Q-Q 플롯을 그리기 전에 데이터를 표준화(standardize)하는 것이 좋습니다. 표준화를 하면 플롯의 기울기(slope)와 절편(intercept)이 각각 표준 편차와 평균을 나타내게 되어 해석이 용이해집니다.
    *   표준화는 보통 각 데이터 포인트에서 평균을 빼고 표준 편차로 나누는 방식으로 이루어집니다: $z = \frac{x - \mu}{\sigma}$
*   **작은 표본 크기($n$)**: 표본 크기 $n$이 작을 경우, Q-Q 플롯에 나타나는 작은 편차는 흔히 발생합니다. 이 경우, $n$을 명시하고 필요에 따라 신뢰 구간(confidence bands)을 함께 고려하여 해석해야 합니다.
*   **강건성(Robustness) 고려**: 데이터의 이상치(outliers)나 극단값에 민감하지 않은 강건한 분석이 필요할 때는 평균/표준 편차 대신 중앙값(median)과 MAD(Median Absolute Deviation)를 사용하여 표준화된 값을 검토하는 것도 유용합니다.

### 코드/수식 해설
Q-Q 플롯은 데이터의 $k$-번째 양자(quantile) $Q_d(k)$와 특정 이론적 분포의 $k$-번째 양자 $Q_t(k)$를 2D 평면에 점 $(Q_t(k), Q_d(k))$으로 나타냅니다. 데이터가 이론적 분포를 따른다면 이 점들은 대각선($y=x$) 근처에 놓이게 됩니다.

Q-Q 플롯을 그리는 일반적인 파이썬 코드 예시는 다음과 같습니다. `statsmodels` 라이브러리가 자주 사용됩니다.

```python
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 1. 정규 분포를 따르는 가상의 데이터 생성
data_normal = np.random.normal(loc=0, scale=1, size=100)

# 2. 정규 Q-Q 플롯 그리기
# sm.qqplot 함수의 dist 매개변수는 기본값이 'norm' (정규 분포) 입니다.
fig_norm = sm.qqplot(data_normal, line='45', fit=True)
plt.title("Normal Q-Q Plot of Normal Data")
plt.show()

# 3. 다른 분포 (예: 지수 분포)를 따르는 가상의 데이터 생성
data_exponential = np.random.exponential(scale=1, size=100)

# 4. 지수 분포 Q-Q 플롯 그리기 (이론적 분포를 지수 분포로 설정)
# dist='expon'으로 이론적 분포를 지정할 수 있습니다.
fig_expon = sm.qqplot(data_exponential, dist='expon', line='45', fit=True)
plt.title("Exponential Q-Q Plot of Exponential Data")
plt.show()

# 5. 정규 분포를 따르지 않는 데이터 (예: t-분포)의 정규 Q-Q 플롯
data_t = np.random.standard_t(df=5, size=100) # 자유도 5인 t-분포
fig_t_norm_qq = sm.qqplot(data_t, line='45', fit=True) # 이론적 분포는 정규 분포
plt.title("Normal Q-Q Plot of t-distributed Data (df=5)")
plt.show()
```
`line='45'`는 데이터가 이론적 분포를 따를 경우 나타나는 $y=x$ 대각선을 그려줍니다. `fit=True`는 데이터를 표준화하여 기울기와 절편이 해석 가능하도록 합니다.

### 구체적 예시
*   **정규성 확인**: 데이터가 정규 분포를 따른다면 Q-Q 플롯의 점들이 대각선에 가깝게 분포합니다. 만약 점들이 대각선 아래로 휘어진다면 (S-자 모양), 데이터가 정규 분포보다 꼬리가 무겁거나(heavy-tailed) 왜곡(skewed)되어 있음을 나타냅니다. 반대로 위로 휘어지면 꼬리가 가볍거나(light-tailed) 왜곡되어 있음을 시사합니다.
*   **모델 잔차 분석**: 예를 들어, 선형 회귀 모델을 구축한 후 잔차(residuals)를 Q-Q 플롯으로 그려서 정규성을 확인합니다. 만약 잔차 Q-Q 플롯이 대각선에서 크게 벗어난다면, 잔차가 정규 분포 가정을 위배하여 모델의 신뢰성에 문제가 있을 수 있음을 의미합니다.

### 강의 내용
교수님께서는 Q-Q 플롯이 "정규성(normality)을 확인하고 꼬리(tails)를 진단하는 주요 도구(primary tool)"라고 강조하셨습니다. 특히 "데이터의 양자(quantile of your data)를 참조 분포의 이론적 양자(theoretical quantile of reference distribution)에 대해 플롯하는 것"이 Q-Q 플롯의 핵심 정의임을 강조하셨습니다.

이전 논의에서 언급되었던 `strip plot`은 데이터가 매우 많을 경우 유용하지 않을 수 있으며, 겹침(overlap)을 피하기 위해 `jittered points`를 사용하는 방법 등을 언급하시며 다양한 시각화 기법의 장단점과 한계를 짚어주셨습니다. 이러한 논의 끝에 "우리 강의의 최종 플롯은 Q-Q 플롯"이라고 하시며 이 플롯의 중요성을 부각하셨습니다. `KDE plot`과 `log plot` 또한 데이터 분포를 시각화하는 다른 방법으로 언급되었습니다.

### 시험 포인트
*   **Q-Q 플롯의 정의와 목적**: ⭐Q-Q 플롯이 무엇이며(데이터의 양자를 이론적 양자에 대해 플롯), 어떤 목적으로 사용되는지 (정규성 확인, 꼬리 진단) 명확히 이해해야 합니다.
*   **Q-Q 플롯의 주요 활용**: ⭐다른 이론적 분포와의 비교, 특히 `모델 잔차`의 분포 가정을 확인하는 데 Q-Q 플롯을 적용하는 방법에 대해 알아두어야 합니다.
*   **모범 사례**: ⭐정규 Q-Q 플롯 사용 시 데이터를 `표준화`해야 하는 이유와 그 효과(기울기/절편 해석)를 반드시 기억해야 합니다. 또한 작은 표본 크기($n$)에서의 해석 유의점도 중요합니다.

---

## Slide 34

---

### **핵심 개념**
Q-Q Plot (Quantile-Quantile Plot)은 데이터의 분포가 특정 이론적 분포(참조 분포)를 따르는지 시각적으로 확인하는 데 사용되는 그래프입니다. 특히, 데이터가 정규 분포를 따르는지 여부(정규성)를 검정하는 데 매우 유용합니다. Q-Q Plot은 데이터의 **샘플 분위수(Sample Quantiles)**를 이론적 분포의 **이론적 분위수(Theoretical Quantiles)**에 대해 플로팅합니다.

### **코드/수식 해설**

**Q-Q Plot의 기본 원리 수식:**
각 데이터 포인트 $i$에 대해 다음과 같은 단계를 거쳐 플로팅 위치 $P_i$와 이론적 분위수를 계산합니다.

1.  **플로팅 위치(Plotting Position) 계산**: 데이터 포인트의 순위(rank)를 기반으로 확률 $P_i$를 계산합니다. 일반적인 방법 중 하나는 다음 공식입니다.
    $$ P_i = \frac{i - 0.5}{N} $$
    여기서 $i$는 정렬된 데이터의 순위(rank), $N$은 총 데이터 포인트 수입니다.

2.  **이론적 분위수(Theoretical Quantile) 계산**: 참조 분포의 역누적분포함수(Inverse Cumulative Distribution Function, CDF$^{-1}$ 또는 Quantile Function)를 사용하여 위에서 계산된 확률 $P_i$에 해당하는 분위수를 찾습니다.
    $$ \text{이론적 분위수} = F^{-1}(P_i) $$
    여기서 $F^{-1}$는 참조 분포의 역누적분포함수입니다. 예를 들어, 정규 분포를 참조하는 경우 $\Phi^{-1}(P_i)$가 됩니다.

Q-Q Plot은 X축에 이론적 분위수 $F^{-1}(P_i)$를, Y축에 샘플 데이터 포인트 $x_i$ (샘플 분위수)를 플로팅합니다.

**코드 해설:**
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
import scipy.stats as st # 통계 함수를 위한 라이브러리 임포트

# Wine 데이터셋 로드 및 'alcohol' 피처 추출
wine = load_wine(as_frame=True)
x = wine.frame["alcohol"].to_numpy()

# 데이터를 z-score로 표준화 (평균을 0, 표준편차를 1로 만듦)
# z-score: (개별 값 - 평균) / 표준편차
# ddof=0은 모집단 표준편차(N)를 사용함을 의미 (기본값은 표본 표준편차 N-1)
x = (x - x.mean()) / x.std(ddof=0) # z-score

# scipy.stats.probplot을 사용하여 이론적 분위수와 샘플 분위수를 계산
# x: 분석할 데이터
# dist="norm": 참조 분포를 정규 분포로 설정
# fit=False: 최적선을 맞추지 않고 분위수 값만 반환 (플로팅은 직접 수행)
osm, osr = st.probplot(x, dist="norm", fit=False)
# osm (order statistic medians): 이론적 분위수 (x축 값)
# osr (ordered sample data): 샘플 분위수 (y축 값)

plt.figure() # 새 그림 생성

# 산점도 플로팅: 이론적 분위수(x) vs 샘플 분위수(y)
plt.scatter(osm, osr, s=18, alpha=0.7)

# 완벽한 일치 시 그려질 직선의 시작점과 끝점 계산
mn, mx = np.min(osm), np.max(osm) # 이론적 분위수 범위
# 이론적 분위수와 샘플 분위수가 완벽히 일치하면 y=x 직선이 됨
plt.plot([mn, mx], [mn, mx], linestyle="--", linewidth=1.2) # 참조선 플로팅

# 축 라벨과 제목 설정
plt.xlabel("Theoretical quantiles (Normal)") # x축 라벨: 이론적 분위수 (정규 분포)
plt.ylabel("Sample quantiles (z-scored)")   # y축 라벨: 샘플 분위수 (z-scored)
plt.title("Q-Q Plot: Wine alcohol vs Normal") # 그래프 제목
plt.tight_layout() # 여백 자동 조정

plt.savefig("qq_wine_alcohol.png", dpi=150) # 그래프 이미지 파일로 저장
```

### **구체적 예시**
이 슬라이드의 코드는 `wine` 데이터셋의 `alcohol` 함량 데이터를 사용하여 Q-Q Plot을 생성합니다.
1.  먼저 `alcohol` 데이터를 추출하고, 정규 분포와의 비교를 용이하게 하기 위해 평균이 $0$이고 표준편차가 $1$인 **z-score** 형태로 표준화합니다.
2.  `scipy.stats.probplot` 함수를 사용하여 이 표준화된 `alcohol` 데이터의 샘플 분위수와, 표준 정규 분포의 이론적 분위수를 계산합니다.
3.  계산된 두 분위수 값을 산점도로 플로팅하고, 데이터가 완벽하게 정규 분포를 따른다면 나타날 $y=x$ 직선(참조선)을 함께 그립니다.
4.  만약 플로팅된 점들이 이 참조선에 가까이 위치할수록 `alcohol` 데이터의 분포가 정규 분포와 유사하다는 것을 시각적으로 확인할 수 있습니다. 예를 들어, 데이터가 참조선 아래로 볼록하게 나타나면 꼬리가 얇은 분포(light-tailed), 위로 볼록하면 꼬리가 두꺼운 분포(heavy-tailed)일 가능성이 높습니다.

### **강의 내용**
교수님께서는 Q-Q Plot의 핵심을 다음과 같이 강조하셨습니다:
*   Q-Q Plot은 **참조 분포(reference distribution)**, 특히 **정규 분포(normal distribution)**와 데이터의 분위수를 비교하는 플롯입니다.
*   X축에는 이론적 분위수 $F^{-1}(P_i)$를 플로팅하고, Y축에는 실제 데이터의 샘플 분위수 $x_i$를 플로팅합니다.
*   데이터가 참조 분포를 완벽하게 따른다면, 모든 데이터 포인트가 **직선(straight line)** 위에 놓이게 됩니다.
*   이러한 특성 때문에 Q-Q Plot은 데이터의 **정규성(normality)을 확인하는 데 매우 유용**하며, 분포가 정규 분포인지 아닌지를 판단하는 데 활용됩니다.

### **시험 포인트**
*   Q-Q Plot의 ⭐**목적**: 데이터 분포가 특정 이론적 분포(특히 정규 분포)를 따르는지 시각적으로 확인하는 데 사용됩니다.
*   Q-Q Plot의 ⭐**해석 방법**: 플로팅된 점들이 참조선(보통 $y=x$ 직선)에 가까울수록 데이터의 분포가 참조 분포와 유사하다는 것을 의미합니다.
*   Q-Q Plot의 ⭐**X축과 Y축**: X축은 이론적 분위수, Y축은 샘플 분위수를 나타냅니다.
*   ⭐**정규성 검정**: Q-Q Plot은 데이터의 정규성을 시각적으로 검정하는 강력한 도구입니다.
*   ⭐`scipy.stats.probplot` 함수의 역할: 이 함수를 사용하면 이론적 분위수와 샘플 분위수를 쉽게 계산하여 Q-Q Plot을 그릴 수 있습니다. `dist` 파라미터를 통해 참조 분포를 지정할 수 있습니다 (`"norm"`은 정규 분포).
*   ⭐**Z-score의 의미**: 데이터를 표준화하여 평균 0, 표준편차 1로 만드는 과정으로, 다른 분포와의 비교 시 유용합니다.

---

---

## Slide 35

### **핵심 개념**
Q-Q Plot (Quantile-Quantile Plot)은 데이터의 분포가 특정 이론적 분포(주로 정규 분포)와 얼마나 유사한지 시각적으로 평가하는 데 사용되는 도구입니다. 이 플롯은 표본 데이터의 분위수(Sample Quantiles)를 x축에, 비교하고자 하는 이론적 분포의 분위수(Theoretical Quantiles)를 y축에 플로팅하여 두 분위수를 비교합니다.

*   **목적**: 데이터의 정규성 검정 또는 다른 이론적 분포와의 유사성 파악.
*   **해석**: 플롯의 점들이 기준선($y=x$ 직선)에 가까울수록, 표본 데이터의 분포가 이론적 분포와 유사하다고 해석합니다. 점들이 기준선에서 벗어나면, 표본 분포가 이론적 분포와 다르다는 것을 의미합니다.

### **코드/수식 해설**

Q-Q Plot을 생성할 때는 주로 `scipy.stats.probplot` 함수를 사용합니다.

```python
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# 가상의 와인 알코올 데이터 생성 (실제 강의에서는 wine_df['alcohol'] 사용)
np.random.seed(42)
data = np.random.normal(loc=13.0, scale=0.8, size=100)

# Q-Q Plot 생성
# stats.probplot 함수는 이론적 분위수(osm)와 샘플 분위수(osr)를 반환하고, plot=ax를 통해 지정된 축에 그래프를 그립니다.
# dist='norm'은 정규 분포를 이론적 비교 분포로 사용하도록 지정합니다.
fig, ax = plt.subplots(figsize=(8, 6))
osm, osr = stats.probplot(data, dist="norm", plot=ax)

ax.set_title('Q-Q Plot: Wine alcohol vs Normal')
ax.set_xlabel('Theoretical quantiles (Normal)')
ax.set_ylabel('Sample quantiles (z-scored)')
plt.grid(True)
plt.show()
```

*   **`scipy.stats.probplot(x, dist='norm', plot=ax)`**:
    *   `x`: 분석할 데이터 배열입니다.
    *   `dist='norm'`: 표본 분위수를 비교할 이론적 분포를 지정합니다. `'norm'`은 정규 분포를 의미합니다.
    *   `plot=ax`: 생성된 Q-Q 플롯을 그릴 `matplotlib` axes 객체를 지정합니다.
    *   반환 값 `osm, osr`: `osm`은 `Ordered Statistics Medians`로 **이론적 분위수**를 나타내고, `osr`은 `Ordered Statistics Ranks`로 **샘플 데이터의 분위수**를 나타냅니다.

*   **기준선**: Q-Q Plot에서 데이터 분포가 이론적 분포를 따른다면, 점들은 이상적인 $y=x$ 직선에 놓이게 됩니다.
    $$ y = x $$

### **구체적 예시**
슬라이드에 제시된 "Wine: alcohol" 데이터의 Q-Q Plot 예시를 보면 다음과 같이 해석할 수 있습니다:
*   **중앙 부분**: 데이터 포인트들이 기준선(점선)에 가깝게 정렬되어 있습니다. 이는 데이터의 중앙 영역이 정규 분포의 중앙 부분과 매우 유사하다는 것을 의미합니다.
*   **오른쪽 꼬리 부분**: 플롯의 오른쪽 상단(Theoretical quantiles가 1 이상인 부분)에서 데이터 포인트들이 기준선보다 약간 위쪽으로 벗어나는 경향을 보입니다. 이러한 **상향 편차(upward deviation)**는 데이터 분포가 정규 분포보다 "더 무거운 오른쪽 꼬리(heavier right tail)"를 가졌거나, 몇 개의 큰 값들(large values)이 존재하여 분포가 오른쪽으로 길게 늘어져 있음을 시사합니다. 즉, 데이터가 약간 **양의 왜도(positive skewness)**를 가질 가능성이 있습니다.

### **강의 내용**
*   Q-Q Plot을 그리기 전에 데이터를 먼저 **표준화(Standardize)**하는 것이 중요하다고 강조되었습니다. 표준화를 통해 $z$-score로 변환된 샘플 분위수를 이론적 분위수와 비교하게 됩니다.
*   Q-Q Plot의 기준선은 단순한 $y=x$ 직선이며, 이 선에 점들이 잘 놓여야 데이터가 정규 분포를 따른다고 쉽게 해석할 수 있습니다.
*   `scipy.stats.probplot` 함수를 사용하여 Q-Q Plot을 그리며, `dist='norm'` 파라미터를 통해 정규 분포를 기준으로 분위수를 비교합니다. 이 함수가 **이론적 분위수**를 반환하여 플롯의 x축을 구성합니다.
*   슬라이드의 예시 (`wine` 데이터셋의 `alcohol` 컬럼)를 통해 데이터가 완전히 정규 분포를 따르지는 않지만, 중앙 부분은 유사하며 오른쪽 꼬리 부분에 다소 차이가 있음을 확인했습니다.

### **시험 포인트**
*   ⭐ **Q-Q Plot의 목적**: 데이터가 특정 이론적 분포(특히 정규 분포)를 따르는지 시각적으로 확인하는 방법임을 이해해야 합니다.
*   ⭐ **Q-Q Plot 해석 방법**:
    *   점들이 $y=x$ 기준선에 가까울수록 해당 이론적 분포를 잘 따름.
    *   점들이 기준선에서 벗어나는 양상에 따라 분포의 특성(예: 왜도, 첨도, 이상치)을 추론할 수 있어야 합니다. (예: 오른쪽 꼬리가 위로 벗어나면 heavy right tail 또는 큰 값 존재)
*   ⭐ Q-Q Plot을 그리기 전 **데이터 표준화**의 중요성을 숙지해야 합니다.
*   ⭐ `scipy.stats.probplot` 함수의 사용법 및 주요 파라미터 (`dist='norm'`)에 대한 이해.

---

## Slide 36

### 데이터 시각화 전략 요약 (Univariate Data Analysis & Visualization)

**핵심 개념**:
이 슬라이드는 단변량 데이터 분석 및 시각화를 위한 체계적인 "읽기 전략(Reading Strategy)"을 제시합니다. 데이터를 처음 접했을 때부터 심층적으로 분포를 진단하기까지, 어떤 시각화 도구를 어떤 순서로 활용해야 하는지에 대한 가이드라인을 제공합니다. 주요 시각화 도구로는 히스토그램, ECDF, KDE, Box/Boxen/Violin 플롯, Q-Q 플롯 등이 있으며, 각 도구의 목적과 활용 시점이 핵심입니다.

**코드/수식 해설**:
이 슬라이드에서는 직접적인 코드나 수식보다는 시각화 기법들의 활용 전략을 다룹니다. 다만, 강의 음성에서 언급된 `y = x` 참조선은 Q-Q 플롯에서 정규 분포(또는 다른 기준 분포)와의 일치 여부를 시각적으로 확인하는 데 사용됩니다.
예를 들어, Q-Q 플롯에서 데이터의 분위수(quantile)와 이론적 분포의 분위수가 일치할 때, 점들이 `$$y = x$$` 선 위에 놓이게 됩니다.

**구체적 예시**:
1.  **데이터의 첫인상**: 새로운 데이터셋을 받았을 때, 가장 먼저 `히스토그램(counts)`을 그려 데이터의 전반적인 모양(shape)을 빠르게 파악합니다.
2.  **그룹 비교**: 여러 그룹의 데이터를 비교해야 할 때, 각 그룹의 크기($n$)가 다르더라도 `shared bins`를 사용한 `확률(probability)` 또는 `밀도(density)` 히스토그램을 사용해 분포를 비교합니다.
3.  **정확한 분위수**: 히스토그램의 binning에 영향을 받지 않고 데이터의 분위수(quantile)를 정확히 보고 싶거나, 한 분포가 다른 분포를 확률적으로 지배하는지(`stochastic dominance`) 확인하고 싶을 때는 `ECDF`를 추가합니다.
4.  **부드러운 모드**: 데이터 분포의 `부드러운 모드(smooth mode)`를 파악하고 싶을 때는 `KDE`를 사용합니다. 데이터 포인트의 수가 ($n$) 매우 작을 때는 `rug` 플롯이나 `strip` 플롯을 함께 사용하여 개별 데이터 포인트를 확인하며 분포를 검증(sanity-check)합니다.
5.  **다수 그룹 요약**: 여러 그룹의 데이터를 한눈에 요약하고 비교해야 할 때는 `Box` 플롯, `Boxen` 플롯, `Violin` 플롯을 활용합니다.
6.  **분포 진단**: 데이터가 특정 이론적 분포(특히 정규 분포)를 따르는지 `형식적으로 진단(formally diagnose)`하고, 특히 분포의 `꼬리(tail)` 부분을 확인하고자 할 때는 `Q-Q 플롯`을 사용합니다.

**강의 내용**:
*   강의에서는 `y = x` 참조선이 대시(dashed) 라인으로 그려지는 것에 대한 언급이 있었습니다. 이는 주로 Q-Q 플롯 등에서 비교 기준선으로 사용되는 경우를 지칭합니다.
*   데이터 분석의 "읽기 전략"을 강조하며, 각 시각화 도구가 어떤 질문에 답하는 데 유용한지 설명했습니다.
*   히스토그램 사용 시 `count`를 통해 데이터 형태에 대한 빠른 기준점(fast anchor)을 잡는 것이 중요하다고 언급했습니다.
*   그룹 비교 시 `확률(probability)` 또는 `밀도(density)` 히스토그램을 사용해야 하며, 반드시 `shared bins`를 사용해야 한다고 강조했습니다.
*   ECDF를 통해 `bin-free quantile`을 얻고 `stochastic dominance`를 확인할 수 있다고 설명했습니다.
*   KDE는 `smooth mode`를 얻는 데 유용하며, $N$이 매우 작을 때는 `rug` 또는 `strip plot`으로 보완해야 한다고 했습니다 (강의에서는 `log` 플롯을 언급했지만 슬라이드에는 `rug/strip`이 명시되어 있습니다).
*   Box/Boxen/Violin 플롯은 여러 그룹을 한 번에 요약하고 비교하는 데 효과적이라고 강조했습니다.
*   Q-Q 플롯은 분포를 `형식적으로 진단(formally diagnose)`하고, 특히 `정규 분포(normal distribution)`에 대한 `꼬리(tail)` 부분을 확인하는 데 사용된다고 설명했습니다.

**시험 포인트**:
*   ⭐ **각 시각화 기법의 목적과 적절한 사용 시점을 반드시 이해해야 합니다.** (예: 히스토그램은 데이터의 빠른 형태 파악, ECDF는 bin-free 분위수 및 확률적 지배 확인, Q-Q 플롯은 분포 진단 및 꼬리 부분 확인 등)
*   ⭐ **그룹 비교 시 `shared bins`를 사용한 `probability/density` 히스토그램의 중요성.**
*   ⭐ **ECDF의 두 가지 주요 활용 목적: `bin-free quantiles`와 `stochastic dominance` 확인.**
*   ⭐ **$N$이 작을 때 `KDE`를 `rug` 또는 `strip` 플롯으로 보완하는 이유.**
*   ⭐ **Q-Q 플롯이 `형식적인 분포 진단`과 `꼬리 부분` 확인에 특히 유용하다는 점, 특히 `정규 분포`에 대한 검증.**
*   ⭐ **이 슬라이드에 제시된 시각화 전략의 전체적인 흐름을 이해하고, 각 단계에서 어떤 도구를 사용해야 하는지 설명할 수 있어야 합니다.**

---

