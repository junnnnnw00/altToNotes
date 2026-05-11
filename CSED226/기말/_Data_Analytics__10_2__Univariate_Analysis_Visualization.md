# CSED226 - _Data_Analytics__10_2__Univariate_Analysis_Visualization 상세 해설 노트 (음성 전사 포함)

> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다. Alt(altalt.io) 음성 전사 데이터를 함께 활용했습니다.

---

## Slide 1

**핵심 개념**
*   **일변량 데이터 분석 및 시각화 (Univariate Data Analysis & Visualization)**: 단일 속성 또는 변수에 대한 데이터를 분석하고 시각화하는 방법을 다루는 강의입니다.

**강의 맥락**
*   강의는 일변량 데이터 분석 및 시각화를 주제로 하며, `univariate data`는 단일 속성 또는 변수에 대한 데이터라고 설명합니다.
*   전체 강의는 어떤 플롯을 언제 사용해야 하는지에 대한 빠른 가이드로 시작하며, 이는 강의 전체를 요약하는 핵심 내용입니다.

**시험 포인트**
*   ⭐ "What plot to use and when (어떤 플롯을 언제 사용해야 하는지)"을 암기하는 것이 이 강의에서 가장 중요한 부분임을 강조합니다.

---

## Slide 2

**핵심 개념**:
이 슬라이드는 단변량 데이터 분석 및 시각화 시 어떤 플롯을 언제 사용해야 하는지에 대한 빠른 가이드라인을 제공한다. 이는 전체 강의 내용을 요약하며, 데이터를 올바르게 이해하고 표현하는 데 필수적인 각 플롯의 용도와 특징을 강조한다.

**강의 맥락**:
교수님은 이 슬라이드가 "전체 강의를 요약하는" **가장 중요한 부분**이며, 학생들이 "무엇을 언제 사용해야 할지 ⭐**암기해야 한다**"고 강하게 강조했다.

*   **Simple shape overview (간단한 형태 개요)**
    *   **Histogram**: 데이터 분포의 전반적인 형태를 빠르고 직관적으로 파악하는 데 사용한다.
    *   ⭐**Bins 튜닝**이 중요하며, 다른 크기의 그룹을 비교할 때는 반드시 **정규화**해야 한다.
*   **Bin-free, exact cumulative view (Bin-free, 정확한 누적 뷰)**
    *   **ECDF (Empirical Cumulative Distribution Function)**: Bin 설정에 따른 인공물을 피하고 정확한 누적 분포를 보여준다.
    *   ⭐특히 샘플 크기($n$)가 다른 경우(unequal $n$) 그룹 간 비교에 탁월하다.
*   **Smooth shape & modes (매끄러운 형태 및 모드)**
    *   **KDE (Kernel Density Estimate)**: 데이터의 부드러운 형태와 여러 개의 피크(modes, 봉우리)를 파악하는 데 사용한다.
    *   ⭐**대역폭(bandwidth)** 선택이 중요하며, 데이터가 양수 값만 갖는 등 경계가 있는 경우 편향을 피하기 위해 데이터를 **반영(reflect)하거나 변환(transform)해야 한다.**
*   **Compact group comparison (간결한 그룹 비교)**
    *   **Boxplot**: 여러 그룹의 중앙값(median), 사분위수 범위(IQR), 이상치(outlier) 등을 간결하게 비교하는 데 표준적으로 사용된다.
    *   샘플 크기가 큰($\text{large } n$) 경우, 꼬리 부분의 더 많은 세부 정보를 보여주는 **Boxen plot**이 더 나은 선택일 수 있다. 교수님은 Boxen plot을 "Box and plot"으로 언급하며 꼬리 부분의 상세함을 보여주는 것이 특징이라고 설명했다.
*   **Show observations (실제 관측치 표시)**
    *   **Rug plot / Strip plot**: 데이터의 실제 개별 관측치를 시각화한다.
    *   Box plot이나 Violin plot 위에 겹쳐서 표시하여 분포 요약이 실제 데이터와 일치하는지 ⭐**건전성 확인(sanity check)** 용도로 사용하기 좋다.
*   **Normality / tail checks (정규성 / 꼬리 확인)**
    *   **Q-Q plot (Quantile-Quantile plot)**: 데이터가 특정 이론적 분포(특히 정규 분포)를 따르는지 여부와 분포의 꼬리 부분을 확인하는 데 ⭐**가장 좋은 도구**이다.
*   **Heavy right tails or non-negativity (무거운 오른쪽 꼬리 또는 비음수 데이터)**
    *   **Log transform 또는 관련 변환**: 오른쪽으로 긴 꼬리를 갖는 데이터나 비음수 데이터의 경우, 플로팅 전에 로그 변환 등의 변환을 적용하는 것이 종종 좋은 첫 단계이다. 이는 시각화의 편향을 줄이는 데 도움이 된다.

---

## Slide 3

## Real Datasets & Setup

### 핵심 개념
본 강의에서는 `scikit-learn` 라이브러리에서 제공하는 세 가지 실제 데이터셋(`Iris`, `Wine`, `Diabetes`)을 활용하여 데이터 분석 및 시각화 실습을 진행합니다. 예시 코드에서는 데이터를 pandas DataFrame `df` 형태로 사용하며, `value` (측정값) 및 `group` (카테고리) 컬럼을 가정합니다.

### 코드/수식 해설
강의 예제에서는 다음 단계를 통해 데이터를 준비합니다.

1.  **필요 라이브러리 임포트**: `numpy`, `pandas`, `matplotlib.pyplot`, `seaborn` 및 `sklearn.datasets`에서 각 데이터셋을 로드하는 함수를 임포트합니다.

    ```python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.datasets import load_iris, load_wine, load_diabetes
    ```

2.  **데이터셋 로드**: 각 데이터셋을 로드할 때 `as_frame=True` 옵션을 사용하여 데이터를 pandas DataFrame 형태로 편리하게 가져옵니다.

    ```python
    iris_data = load_iris(as_frame=True)
    wine_data = load_wine(as_frame=True)
    diabetes_data = load_diabetes(as_frame=True)

    # 데이터프레임 변수에 저장
    iris = iris_data.frame
    wine = wine_data.frame
    diabetes = diabetes_data.frame
    ```

3.  **읽기 쉬운 레이블 컬럼 생성**: 각 데이터셋의 숫자형 타겟 변수를 문자열 레이블로 매핑하여 새로운 컬럼을 만듭니다.
    *   **Iris**: `target` (0, 1, 2)를 `species` (Setosa, Versicolor, Virginica)로 매핑
    *   **Wine**: `target` (0, 1, 2)를 `class` (A, B, C)로 매핑

    ```python
    # Iris 데이터셋 예시 (wine도 유사하게 적용)
    iris['species'] = iris_data.target.map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})
    wine['class'] = wine_data.target.map({0: 'A', 1: 'B', 2: 'C'})
    ```

### 구체적 예시
*   **Iris 데이터셋**: 150개의 꽃 샘플을 포함하며, `sepal length`, `sepal width`, `petal length`, `petal width` 같은 특징과 세 가지 종(`0, 1, 2`)을 나타내는 타겟 변수를 가집니다. (X: 특징, Y: 종)
*   **Wine 데이터셋**: 178개의 샘플을 포함하며, `alcohol`, `flavanoids` 등 물리화학적 특징과 세 가지 와인 종류(`0, 1, 2`)를 나타내는 타겟 변수를 가집니다. (X: 특징, Y: 와인 종류)
*   **Diabetes 데이터셋**: 442명의 환자 데이터를 포함하며, `BMI` 등 표준화된 특징과 질병 진행 정도를 나타내는 타겟 변수를 가집니다.

### 강의 맥락
교수님은 실습을 위해 `scikit-learn` 라이브러리의 세 가지 실제 데이터셋을 사용할 것이라고 소개했습니다. 각 데이터셋의 특징(샘플 수, 피처 종류, 타겟 변수)을 간략히 설명하면서, 타겟 변수가 `Y` 값에 해당하고 나머지 속성들이 `X` 값이라고 강조했습니다.

코드 예시에서는 데이터가 `value` 및 `group` 컬럼을 가진 pandas DataFrame `DF` 형태로 준비되었다고 가정한다고 설명했습니다. 특히, 데이터를 로드할 때 `as_frame=True` 옵션을 설정하면 데이터를 편리하게 pandas DataFrame으로 가져올 수 있다고 언급했습니다. 또한, 편의를 위해 숫자형 타겟 변수를 `Iris` 데이터셋에서는 `species` 컬럼으로, `Wine` 데이터셋에서는 `class` 컬럼으로 읽기 쉬운 문자열 레이블로 변환하는 과정을 설명하며, 이러한 데이터프레임이 주어진 상태에서 분석을 시작한다고 강조했습니다.

### 시험 포인트
*   `scikit-learn` 데이터셋을 pandas DataFrame으로 로드하기 위해 `load_iris()` 등의 함수에서 어떤 옵션을 사용해야 하는가? ⭐ **`as_frame=True`**
*   강의에서 활용되는 주요 3가지 데이터셋의 이름과 각각의 주요 특징 (예: Iris는 꽃, Wine은 와인 종류, Diabetes는 질병 진행)을 알아둘 것.

---

## Slide 4

**핵심 개념**:
이 슬라이드는 앞으로의 데이터 분석 실습에 사용될 세 가지 실제 데이터셋(Iris, Wine, Diabetes)을 로드하고 전처리하는 과정을 설명합니다. NumPy, Pandas, Matplotlib, Seaborn 등 핵심 라이브러리들을 임포트하고, Scikit-learn의 내장 데이터셋을 Pandas DataFrame 형태로 불러와 분석하기 쉽게 레이블을 추가합니다.

**코드/수식 해설**:

```python
import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
from sklearn.datasets import load_iris, load_wine, load_diabetes

iris = load_iris(as_frame=True).frame
wine = load_wine(as_frame=True).frame
diabetes = load_diabetes(as_frame=True).frame

# Convenience: readable group labels
iris["species"] = iris["target"].map({0:"setosa", 1:"versicolor", 2:"virginica"})
wine["class"] = wine["target"].map({0:"A", 1:"B", 2:"C"})
```
*   `import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns`: 데이터 과학 및 시각화에 필수적인 라이브러리들을 임포트합니다.
    *   `numpy`: 수치 계산을 위한 핵심 라이브러리.
    *   `pandas`: 데이터프레임 조작을 위한 라이브러리.
    *   `matplotlib.pyplot`: 기본적인 정적 시각화 라이브러리.
    *   `seaborn`: Matplotlib을 기반으로 더 세련된 통계 그래픽을 제공하는 라이브러리.
*   `from sklearn.datasets import load_iris, load_wine, load_diabetes`: Scikit-learn 라이브러리에서 제공하는 예제 데이터셋 로더 함수들을 임포트합니다.
*   `iris = load_iris(as_frame=True).frame`: `load_iris()` 함수를 사용하여 Iris 데이터셋을 로드합니다. 이때 ⭐`as_frame=True`⭐ 옵션을 사용하면 데이터셋이 Pandas DataFrame 형태로 반환되어 데이터 조작이 편리해집니다. `.frame`을 통해 데이터와 타겟이 통합된 단일 DataFrame을 얻습니다. Wine과 Diabetes 데이터셋도 동일한 방식으로 로드합니다.
*   `iris["species"] = iris["target"].map(...)`: Iris 데이터셋의 숫자형 `target` 변수(0, 1, 2)를 해당하는 종 이름("setosa", "versicolor", "virginica")으로 매핑하여 `species`라는 새로운 컬럼을 생성합니다.
*   `wine["class"] = wine["target"].map(...)`: Wine 데이터셋의 숫자형 `target` 변수(0, 1, 2)를 "A", "B", "C"와 같은 가독성 좋은 클래스 레이블로 매핑하여 `class`라는 새로운 컬럼을 생성합니다.

**강의 맥락**:
강의에서는 실습을 위해 Scikit-learn (강사님은 "CycliLon"으로 언급) 라이브러리의 세 가지 실제 데이터셋을 사용한다고 설명합니다. Iris, Wine, Diabetes 데이터셋 각각에 대해 샘플 수, 주요 특성(X 값), 그리고 목표 변수(Y 값)의 특징을 간략히 소개합니다. 코딩 예제에서는 데이터를 Pandas DataFrame `df` 형태로 가정한다고 언급하며, 기본적인 라이브러리 임포트의 중요성을 강조합니다. 특히, 데이터셋 로드 시 ⭐`as_frame=True`⭐ 옵션이 데이터를 Pandas DataFrame으로 편리하게 제공해주는 핵심 역할을 한다고 강조합니다. 마지막으로, 분석의 편의성을 위해 숫자형 타겟 변수를 "Setosa", "A" 등과 같이 읽기 쉬운 문자열 레이블로 변환하는 과정을 설명하며, 이러한 변환된 DataFrame을 사용하여 실습을 진행할 것임을 밝힙니다.

**시험 포인트**:
*   ⭐`as_frame=True` 옵션이 `sklearn.datasets`에서 데이터를 로드할 때 어떤 역할을 하는지 (Pandas DataFrame 반환) 반드시 기억해야 합니다.
*   데이터셋 로드 후 숫자형 타겟 변수를 문자열 레이블로 매핑하는 이유 (가독성 향상, 그룹 비교 용이성)를 이해하고 있어야 합니다.

---

## Slide 5

**핵심 개념**:
*   **히스토그램(Histogram)**: 단변수 데이터의 분포 형태를 빠르고 직관적으로 파악하는 데 가장 기본적인 시각화 도구입니다.
*   **빈(Bin) 정의**: 데이터를 특정 구간($b_{k-1}$부터 $b_k$)으로 나누어 각 구간에 속하는 데이터 포인트의 개수(`count`)나 밀도(`density`)를 막대 그래프로 표현합니다.
*   **사용 목적**: 데이터의 전반적인 형태를 빠르게 파악하고, 여러 그룹 간의 분포를 비교하는 데 활용됩니다.

**코드/수식 해설**:
히스토그램의 `count`와 `density`는 다음과 같이 정의됩니다.

*   **`count_k` (빈 $k$의 개수)**:
    $$ \text{count}_k = \#\{x_i \mid b_{k-1} < x_i \leq b_k\} $$
    $b_k$는 $k$번째 빈의 경계를 나타내며, `count_k`는 $k-1$번째 빈 경계와 $k$번째 빈 경계 사이에 속하는 데이터 포인트 $x_i$의 개수입니다.

*   **`density_k` (빈 $k$의 밀도)**:
    $$ \text{density}_k = \frac{\text{count}_k}{n(b_k - b_{k-1})} $$
    `density_k`는 `count_k`를 전체 데이터 포인트 수 $n$과 빈의 너비 $(b_k - b_{k-1})$로 나눈 값입니다. 이 정규화 과정을 통해 히스토그램 전체 면적이 1이 되도록 합니다.

**강의 맥락**:
교수님은 히스토그램을 단변수 데이터 분석의 "가장 근본적인(most fundamental)" 플롯이라고 강조하며, 그 정의와 사용법을 설명했습니다.

*   히스토그램의 `count`와 `density` 계산 방법을 수식과 함께 설명하며, 특히 `density` 계산 시 "전체 데이터 포인트 수 $n$"과 "빈의 너비($b_k - b_{k-1}$)"로 나누는 **정규화(normalization)**가 "총 면적이 1이 되도록(integrates to 1)" 하는 데 "결정적으로 중요(crucial)"하다고 강조했습니다.
*   히스토그램은 데이터의 "빠르고 직관적인 형태 파악(fast, intuitive view of shape)"에 유용하며, "그룹 비교(comparing groups)"에도 좋다고 언급했습니다.
*   하지만 그룹을 비교할 때는 반드시 "같은 빈 경계를 사용(shared bin edges)"하고 Y축을 "정규화(normalize)"해야 한다고 강조했습니다. 그렇지 않으면 "오렌지와 사과를 비교하는 것(comparing orange with the apple)"과 같아 올바른 비교가 불가능하다고 경고했습니다.
*   초기에는 `counts`로 시작하지만, "서로 다른 크기의 그룹(groups of different sizes)"이나 "다른 빈 너비(different bin widths)"를 가진 히스토그램을 비교할 때는 "확률(probability) 또는 밀도(density)"로 전환해야 "공정한 비교(fair comparison)"가 가능하다고 설명했습니다.

**시험 포인트**:
*   ⭐ 히스토그램의 `count_k`와 `density_k` 수식 정의를 이해하고 설명할 수 있어야 합니다.
*   ⭐ 히스토그램을 사용하는 주된 이유(데이터 형태 파악, 그룹 비교)를 알아야 합니다.
*   ⭐ **여러 그룹을 비교할 때 히스토그램을 올바르게 사용하는 두 가지 핵심 원칙**:
    1.  **Shared bins (공유된 빈 경계)**
    2.  **Density normalization (밀도 정규화)**
    이 두 가지를 지키지 않으면 올바른 비교가 불가능하다는 점을 명확히 기억해야 합니다.
*   ⭐ `count` 기반 히스토그램과 `density` 기반 히스토그램의 차이 및 각각을 언제 사용해야 하는지 (`density`는 그룹 비교 또는 빈 너비가 다른 경우에 필수) 이해해야 합니다.

---

## Slide 6

**핵심 개념**:
기본 히스토그램은 단일 변수 데이터의 분포를 빠르고 직관적으로 파악하기 위한 가장 기본적인 시각화 도구입니다. 데이터의 중심, 분포 범위(spread), 대략적인 봉우리(modality)를 확인하는 데 사용됩니다.

**코드 해설**:
데이터 프레임 `wine`에서 'alcohol' 컬럼을 추출하여 `x` 변수에 할당한 후, `matplotlib.pyplot` 또는 `seaborn` 라이브러리를 사용하여 기본 히스토그램을 그립니다.

```python
# wine 데이터셋에서 'alcohol' 컬럼을 x에 할당
x = wine["alcohol"]

# Matplotlib을 사용한 기본 히스토그램
plt.figure()
plt.hist(x) # 기본값: 약 10개의 동일 너비(equal-width) 빈, y축은 'counts'
plt.xlabel("alcohol")
plt.ylabel("count")
plt.title("Histogram: defaults")
plt.show()

# Seaborn을 사용한 동등한 히스토그램 (실행되지 않음)
# sns.histplot(x=x, bins=10, stat="count", element="bars", kde=False)
# plt.xlabel("alcohol")
# plt.ylabel("count")
# plt.title("Histogram: defaults")
# plt.show()
```
*   `plt.hist(x)`: `x` 데이터를 사용하여 히스토그램을 그리는 가장 기본적인 함수입니다. 기본적으로 약 10개의 동일한 너비의 빈(bin)을 사용하며, `y`축에는 각 빈에 해당하는 데이터 포인트의 개수(raw counts)를 표시합니다.
*   `sns.histplot()`: Seaborn의 히스토그램 함수입니다. Matplotlib의 `hist`와 동일한 결과를 얻기 위해 `bins=10`, `stat="count"`, `element="bars"`, `kde=False`와 같은 옵션을 명시적으로 설정할 수 있습니다.

**강의 맥락**:
교수님은 히스토그램이 단변량 데이터 분석의 가장 기본적인 플롯임을 강조하며, `plt.hist` 함수를 호출하는 것만으로 기본 히스토그램을 생성할 수 있다고 설명하셨습니다. 기본적으로 약 10개의 동일한 너비의 빈을 사용하며 `y`축에는 데이터 포인트의 개수를 나타낸다고 언급하셨습니다. 이러한 기본 히스토그램은 "빠른 단일 샘플 확인"에 유용하며, 데이터의 중심(center), 분포 범위(spread), 대략적인 봉우리(rough idea if it is a unimodal)를 파악하는 데 좋다고 강조하셨습니다. 또한, Seaborn의 `histplot`도 유사한 기능을 제공하지만, 모든 함수를 외울 필요는 없고 필요할 때 찾아보는 것이 효율적이라고 조언하셨습니다.

**시험 포인트**:
*   ⭐ **기본 히스토그램의 목적**: 빠른 단일 샘플 데이터의 형태(shape) 확인 (중심, 분포 범위, 대략적인 봉우리 파악).
*   ⭐ **`plt.hist()`의 기본 동작**: 약 10개의 동일 너비(equal-width) 빈을 사용하고, `y`축에 원시 개수(raw counts)를 표시합니다.

---

## Slide 7

**핵심 개념**
기본 히스토그램의 bin 개수는 데이터의 실제 분포를 왜곡하여 중요한 특징(mode)을 숨기거나 존재하지 않는 노이즈를 추가할 수 있습니다. 이를 해결하기 위해 **Freedman-Diaconis (FD) 규칙**과 같은 **데이터 적응형(data-adaptive) binning 규칙**을 사용하여 히스토그램의 bin을 설정하는 것이 좋습니다. FD 규칙은 과도한 스무딩(over-smoothing)이나 부족한 스무딩(under-smoothing)의 위험을 줄여 데이터의 실제 형태를 더 잘 나타냅니다.

**코드 해설**

```python
x = wine["alcohol"]
plt.hist(x, bins="fd") # matplotlib을 사용하여 FD 규칙으로 히스토그램 생성
plt.xlabel("alcohol"); plt.ylabel("count")

ax = sns.histplot(x=x, bins="fd", stat="count", element="bars", kde=False, discrete=False) # seaborn을 사용하여 FD 규칙으로 히스토그램 생성
ax.set(xlabel="alcohol", ylabel="count", title="Histogram: bins='fd'")
plt.show()
```
*   `x = wine["alcohol"]`: 'wine' 데이터프레임에서 'alcohol' 컬럼을 선택하여 `x` 변수에 할당합니다.
*   `plt.hist(x, bins="fd")`: `matplotlib.pyplot`의 `hist` 함수를 사용하여 히스토그램을 그립니다. `bins="fd"` 옵션은 Freedman-Diaconis 규칙에 따라 bin의 개수와 너비를 자동으로 결정합니다.
*   `sns.histplot(x=x, bins="fd", stat="count", element="bars", kde=False, discrete=False)`: `seaborn`의 `histplot` 함수를 사용하여 히스토그램을 그립니다. `bins="fd"` 옵션은 `matplotlib`와 동일하게 FD 규칙을 적용합니다.
    *   `stat="count"`: y축에 원시 데이터 개수(raw count)를 표시하도록 설정합니다.
    *   `kde=False`: KDE(Kernel Density Estimate) 플롯을 오버레이하지 않도록 설정합니다.
*   `plt.xlabel`, `plt.ylabel`, `ax.set`: x축, y축 레이블 및 플롯 제목을 설정하여 가독성을 높입니다.

**강의 맥락**
교수님께서는 기본 bin 개수가 데이터의 중요한 특징(mode)을 숨기거나 노이즈를 추가할 수 있다는 점을 강조하며, "much better approach is to use a data adaptive rule"라고 말씀하셨습니다. 여기서 "FD means Friedman and Diaconis rule"이라고 FD 규칙을 소개하고, 이 규칙이 "reduce the risk of over-smoothing or under-smoothing"하는 데 도움을 준다고 설명하셨습니다. 또한, `seaborn`에서도 `bins="fd"` 옵션을 사용할 수 있음을 언급하셨습니다. FD 규칙의 상세한 내용에 대해서는 Wikipedia를 참고할 것을 권장하셨습니다.

**시험 포인트**
*   ⭐ **Freedman-Diaconis (FD) 규칙의 목적**: 히스토그램 bin 선택 시 데이터의 특성에 맞게 조정하여 ⭐**과도한 스무딩(over-smoothing) 또는 부족한 스무딩(under-smoothing)을 방지**하고 데이터의 실제 형태를 더 잘 보여주는 것입니다.
*   ⭐ 히스토그램에서 `bins="fd"` 옵션 사용법 (matplotlib, seaborn).

---

## Slide 8

**핵심 개념**
히스토그램에서 `Probability`와 `Density`는 Y축의 정규화 방식에 따른 차이를 나타냅니다.
*   **Probability**: 각 막대의 높이(빈도)의 총합이 1이 되도록 정규화합니다.
    *   각 막대의 높이(`count / total_points`)를 표시하며, 모든 막대의 높이 합이 1입니다.
    *   빈(bin) 너비가 모두 같을 때 빠른 비교에 적합합니다.
*   **Density**: 각 막대의 면적(영역)의 총합이 1이 되도록 정규화합니다.
    *   각 막대의 높이(`count / (total_points * bin_width)`)를 표시하며, 모든 막대의 면적 합이 1입니다.
    *   빈 너비가 다르더라도 강건하게 비교할 수 있으며, 이론적 확률 밀도 함수(PDF)와 비교할 때 적합합니다.

**코드/수식 해설**

*   **Matplotlib**:
    ```python
    plt.hist(x, bins="fd", density=True) # y = density (area = 1)
    ```
    `density=True`로 설정하면 Y축이 밀도(density)로 정규화되어, 히스토그램 막대들의 전체 면적이 1이 됩니다. `bins="fd"`는 Friedman-Diaconis 규칙에 따라 빈의 개수를 자동으로 결정합니다.

*   **Seaborn**:
    ```python
    sns.histplot(x=x, stat="probability") # bar heights sum to 1
    sns.histplot(x=x, stat="density")     # area under bars = 1
    ```
    Seaborn의 `histplot`에서는 `stat` 인자를 사용하여 정규화 방식을 명시적으로 지정할 수 있습니다.
    *   `stat="probability"`: 각 막대의 높이(빈도)의 총합이 1이 되도록 합니다.
    *   `stat="density"`: 모든 막대의 면적(area)의 총합이 1이 되도록 합니다.

**강의 맥락**
"확률(probability)과 밀도(density)의 차이를 이해해야 합니다." 교수님은 Matplotlib에서 `density=True`를 설정하는 것을 언급하며, 확률로 정규화하면 모든 막대의 **높이** 합이 1이 되고, 밀도로 설정하면 모든 막대의 **총 면적**이 1이 된다고 설명합니다.
확률 히스토그램은 모든 빈 너비가 동일할 때 빠른 확인에 적합하지만, 밀도 히스토그램은 빈 너비가 동일하지 않을 경우 훨씬 더 강건하고 올바른 방법이며, 이론적 확률 밀도 함수(PDF)와 비교할 때 강력히 권장됩니다.
Matplotlib에서는 `density=True`로 설정하고, Seaborn에서는 `stat="probability"` 또는 `stat="density"`를 명시적으로 선택할 수 있다고 강조합니다.

**시험 포인트**
*   ⭐`density` 사용 시점:
    *   **서로 다른 그룹 간의 형태(shapes)를 비교할 때**
    *   **이론적인 밀도 곡선(theoretical density curves)을 겹쳐서 표시할 때**
    *   **빈 너비가 균일하지 않을 때** (강건한 비교를 위해)
*   ⭐`Probability`와 `Density`의 정규화 방식 차이 (`height sum to 1` vs `area sum to 1`)를 정확히 이해해야 합니다.

---

## Slide 9

**핵심 개념**:
*   **히스토그램을 이용한 공정한 그룹 비교**: 여러 그룹의 분포를 히스토그램으로 비교할 때, 각 그룹의 샘플 크기나 빈 너비의 차이로 인해 비교가 왜곡될 수 있습니다. 이를 해결하기 위해 두 가지 핵심 개념이 적용됩니다:
    1.  **공유 빈 (Shared bins)**: 모든 그룹의 데이터를 통합(pooled data)하여 하나의 빈 경계($B = \{b_0, \dots, b_K\}$)를 계산하고, 이 동일한 빈 경계를 모든 그룹에 적용합니다.
    2.  **밀도 정규화 (Density normalization)**: 각 그룹의 히스토그램이 전체 면적이 1이 되도록 밀도를 정규화합니다. 이를 통해 샘플 크기가 다른 경우에도 각 그룹의 분포 *형태(shape)*를 공정하게 비교할 수 있습니다.
*   **왜 필요한가**: 다른 빈을 사용하거나 원시 카운트(raw counts)를 사용하면, 빈 설정이나 샘플 크기 차이로 인해 실제 분포 형태의 차이가 왜곡될 수 있습니다.

**코드/수식 해설**:
*   **밀도 정규화 수식**: 특정 그룹 $g$의 빈 $k$에 대한 밀도($\text{density}_{g,k}$)는 다음과 같이 정의됩니다.
    $$
    \text{density}_{g,k} = \frac{\#\{x_i \in g : b_{k-1} < x_i \leq b_k\}}{n_g (b_k - b_{k-1})}
    $$
    여기서,
    *   $\#\{x_i \in g : b_{k-1} < x_i \leq b_k\}$: 그룹 $g$에 속하며 빈 $k$에 해당하는 데이터 포인트의 개수(count).
    *   $n_g$: 그룹 $g$의 총 샘플 크기.
    *   $(b_k - b_{k-1})$: 빈 $k$의 너비.
    이 수식은 각 그룹의 히스토그램 전체 면적이 1이 되도록 보장하며, 이를 통해 샘플 크기에 관계없이 분포 형태를 공정하게 비교할 수 있습니다.

**구체적 예시**:
*   슬라이드 하단의 히스토그램은 `wine` 데이터셋의 `alcohol` 컬럼을 `class` (A, B, C)별로 그룹화하여 공유된 빈과 밀도 정규화를 적용한 결과를 보여줍니다. 각 그룹의 면적이 1로 정규화되어 있어, 샘플 수가 달라도 분포 형태를 직접 비교할 수 있습니다. 겹치는 어두운 영역은 여러 그룹이 공통적으로 많은 데이터를 가진 구간을 나타내고, 특정 색상만 진하게 나타나는 부분은 해당 그룹이 그 범위에서 상대적으로 우세함을 보여줍니다.

**강의 맥락**:
*   교수님은 히스토그램을 이용한 그룹 비교의 "적절한 방법"을 설명하며, "**공정한 비교를 위한 두 가지 핵심 개념**"으로 공유 빈과 밀도 정규화를 제시합니다.
*   특히, 밀도 정규화 수식을 자세히 설명하며, 각 그룹의 히스토그램 면적이 1이 되도록 하는 것이 "**샘플 크기에 관계없이 형태를 공정하게 비교할 수 있게 한다**"고 강조합니다.
*   "This is a very crucial part." (**매우 중요한 부분**임을 다시 한번 강조하며, 이 개념의 중요성을 부각합니다.)
*   서로 다른 빈을 사용하거나 원시 카운트만으로 비교하는 것이 "진정한 형태 차이를 왜곡할 수 있다"고 지적하며, 이 두 가지 개념을 적용해야 하는 이유를 설명합니다.
*   히스토그램에서 어둡게 겹쳐지는 영역은 그룹 간 "공통적인 질량(common mass)"이 있는 곳을, 특정 색상만 진한 부분은 해당 그룹이 그 범위에서 "상대적으로 우세함"을 나타낸다고 해석 방법을 제시합니다.

**시험 포인트**:
*   ⭐ **히스토그램으로 그룹을 공정하게 비교하기 위한 두 가지 핵심 개념 (공유 빈, 밀도 정규화)을 정확히 이해하고 설명할 수 있어야 합니다.**
*   ⭐ **밀도 정규화를 사용하는 이유 (서로 다른 샘플 크기의 그룹 간 형태 비교의 공정성 확보)를 아는 것이 중요합니다.**
*   ⭐ **`density_g,k` 수식의 각 항($n_g$, $b_k - b_{k-1}$)이 무엇을 의미하는지 이해하고 있어야 합니다.**

---

## Slide 10

---
### 핵심 개념

단변량 데이터를 여러 그룹으로 나누어 히스토그램으로 비교할 때, 각 그룹의 분포를 공정하게 비교하기 위한 두 가지 핵심 기법은 **공유 빈(Shared Bins)**과 **밀도 정규화(Density Normalization)**입니다.

*   **공유 빈 (Shared Bins)**: 전체 데이터(모든 그룹을 합친)를 사용하여 하나의 빈 경계(bin edges) 세트를 계산하고, 이 동일한 빈 경계를 모든 그룹의 히스토그램에 적용합니다.
*   **밀도 정규화 (Density Normalization)**: 각 그룹의 히스토그램이 합계 면적 1이 되도록 정규화합니다. 이는 각 그룹의 샘플 크기가 다르더라도 모양(shape)을 공정하게 비교할 수 있게 합니다.

결과적으로 얻어진 오버레이된 히스토그램에서, 짙게 겹치는 영역은 여러 그룹이 공통적으로 해당 범위에 많은 데이터 포인트를 가지고 있음을 나타내며, 특정 색상(그룹)에만 볼록하게 튀어나온 부분은 해당 그룹이 특정 범위에서 상대적으로 우세함을 보여줍니다.

### 코드/수식 해설

**1. 밀도 정규화 공식 (그룹 $G$, 빈 $K$)**

교수님은 앞선 히스토그램 슬라이드에서 설명된 밀도 개념을 확장하여 그룹별 밀도 정규화를 설명하셨습니다.
빈 $K$에 있는 그룹 $G$의 밀도는 다음과 같습니다.

$$
\text{Density}_{G,K} = \frac{\text{Count}_{G,K}}{\text{Total Samples in Group } G \times \text{Bin Width}}
$$

이 정규화를 통해 각 그룹의 히스토그램 면적은 1이 되어, 샘플 크기에 관계없이 분포의 모양을 직접 비교할 수 있습니다.

**2. `matplotlib`를 이용한 구현**

```python
# Shared bins + density normalization
xcol = "alcohol"

# 1) Compute common bin edges from pooled data
bins = np.histogram_bin_edges(wine[xcol], bins="fd")

# 2) Apply same bins to all groups + density=True
for g, sub in wine.groupby("class"):
    plt.hist(sub[xcol], bins=bins,
             density=True, # area = 1
             alpha=0.45, label=g)

plt.xlabel(f"{xcol}")
plt.ylabel("density")
plt.legend(title="class")
plt.title(f"Histogram by class (shared bins, density)")
plt.show()
```

*   `np.histogram_bin_edges(wine[xcol], bins="fd")`: `wine` 데이터셋의 `alcohol` 컬럼 전체를 사용하여 **공통 빈 경계**를 계산합니다. `bins="fd"`는 Friedman-Diaconis 규칙을 사용하여 데이터에 적합한 빈 너비를 자동으로 결정합니다.
*   `wine.groupby("class")`: `wine` 데이터셋을 `class` 컬럼 기준으로 그룹화합니다.
*   `plt.hist(sub[xcol], bins=bins, density=True, alpha=0.45, label=g)`: 각 그룹(`sub`)에 대해 히스토그램을 그립니다.
    *   `bins=bins`: 위에서 계산된 **공유 빈 경계**를 적용합니다.
    *   `density=True`: 히스토그램을 **밀도로 정규화**하여 총 면적이 1이 되게 합니다.
    *   `alpha=0.45`: 투명도를 설정하여 겹치는 부분을 시각적으로 구분할 수 있게 합니다.
    *   `label=g`: 각 그룹의 라벨을 설정하여 범례에 표시합니다.

**3. `seaborn`을 이용한 구현 (더 간단한 방법)**

```python
# Seaborn idea (reference):
sns.histplot(data=wine, x=xcol, hue="class",
             bins=bins, stat="density", common_bins=True)
```

*   `sns.histplot(...)`: `seaborn`의 `histplot` 함수는 그룹 비교 기능을 내장하고 있어 코드가 훨씬 간결해집니다.
*   `data=wine, x=xcol, hue="class"`: `wine` 데이터의 `xcol`(`alcohol`)을 사용하며, `class` 컬럼을 기준으로 색상(`hue`)을 다르게 하여 그룹별로 구분합니다.
*   `bins=bins`: `matplotlib` 예시와 마찬가지로 미리 계산된 공유 빈 경계를 사용합니다.
*   `stat="density"`: y축을 밀도로 정규화합니다. (`stat="probability"`는 높이의 합이 1이 되도록 정규화)
*   `common_bins=True`: 모든 그룹에 대해 동일한 빈 경계를 사용하도록 명시적으로 설정합니다.

### 구체적 예시

`wine` 데이터셋의 'alcohol' 함량을 3가지 와인 `class` (0, 1, 2)별로 비교할 때, 위 코드를 사용하면 각 클래스별 알코올 함량 분포의 모양을 공정하게 비교할 수 있습니다. 예를 들어, 특정 알코올 범위에서 여러 클래스의 히스토그램이 진하게 겹쳐 보인다면, 해당 범위의 알코올 함량을 갖는 와인이 여러 클래스에 걸쳐 분포함을 의미합니다. 반면, 특정 클래스의 히스토그램이 다른 클래스보다 현저히 높은 봉우리를 형성하는 구간이 있다면, 그 클래스의 와인이 해당 알코올 범위에 집중되어 있음을 알 수 있습니다.

### 강의 맥락

교수님께서는 히스토그램을 이용한 그룹 비교의 핵심 개념으로 **공유 빈**과 **밀도 정규화** 두 가지를 강조하셨습니다.
"**공정한 비교를 위해 두 가지 핵심 개념이 있습니다. 첫 번째는 공유 빈을 사용하는 것입니다. 모든 데이터를 함께 모아서 하나의 빈 경계를 계산한 다음, 그 동일한 경계를 모든 그룹에 적용해야 합니다.**"
"**두 번째 개념은 밀도 정규화입니다. 이 수식이 보여주듯이 그룹 G와 빈 K의 밀도는 해당 빈에 있는 그 그룹의 데이터 포인트 수를 그룹의 총 크기와 빈 너비로 나눈 것입니다. 이것은 각 그룹의 히스토그램이 1로 통합되도록 합니다. 이를 통해 샘플 크기에 관계없이 모양을 공정하게 비교할 수 있습니다.**"
또한, `matplotlib` 코드를 단계별로 설명하며 공통 빈 계산, 그룹별 플로팅 시 `density=True` 및 `alpha` 값 설정의 중요성을 설명하셨고, `seaborn`이 `hue`, `stat="density"`, `common_bins=True` 옵션으로 훨씬 간단하게 이를 구현할 수 있음을 보여주셨습니다. 마지막으로, 결과 그래프를 해석하는 방법에 대해 "**더 어두운 겹치는 영역은 그룹이 공통적인 질량을 갖는 부분을 보여주고, 한 가지 색상에만 고유한 볼록한 부분은 해당 특정 범위에서 그룹의 상대적 우위를 보여줍니다.**"라고 설명하셨습니다.

### 시험 포인트

*   ⭐ **히스토그램으로 여러 그룹을 비교할 때, 반드시 적용해야 하는 두 가지 핵심 원칙은 무엇이며 그 이유는?** (공유 빈, 밀도 정규화 - 샘플 크기 차이에 상관없이 공정한 모양 비교를 위함)
*   ⭐ **공유 빈과 밀도 정규화가 적용된 오버레이 히스토그램에서 '짙게 겹치는 영역'과 '특정 그룹에만 볼록하게 튀어나온 영역'은 각각 무엇을 의미하는가?**
*   `density=True` 옵션과 `alpha` 옵션이 `matplotlib` 히스토그램 플로팅에서 어떤 역할을 하는지.
*   `seaborn`의 `histplot`에서 `hue`, `stat="density"`, `common_bins=True` 옵션이 각각 어떤 기능을 하는지.

---

## Slide 11

### 핵심 개념
누적 히스토그램(Cumulative Histogram)은 데이터의 누적 분포를 시각화하는 히스토그램의 한 변형입니다. 특정 `x` 값 이하의 데이터가 전체에서 차지하는 누적 밀도 또는 비율을 보여주며, 일반적으로 스텝 함수 형태의 선 그래프로 표현됩니다.

*   **특징**:
    *   y-축은 누적 밀도(`cumulative density`) 또는 특정 `x` 값보다 작거나 같은 데이터의 **비율(proportion)**을 나타냅니다.
    *   결과 그래프는 x축 값이 증가함에 따라 y축 값이 증가하거나 유지되는 **상승 스텝 함수(rising step function)** 형태를 가집니다.
*   **활용**:
    *   ⭐ **분위수(Quantiles)**를 한눈에 파악하는 데 매우 유용합니다. 예를 들어, y값이 0.5인 지점의 x값이 중앙값(median)이 됩니다.
    *   확률적 지배(stochastic dominance)와 같은 개념을 이해하는 데 도움이 됩니다.
    *   빈(bin) 설정에 구애받지 않는 누적 뷰를 제공하는 **ECDF(Empirical Cumulative Distribution Function)**로 넘어가는 훌륭한 다리 역할을 합니다.

### 코드/수식 해설
누적 히스토그램은 `matplotlib.pyplot.hist` 함수에 특정 옵션을 설정하여 생성할 수 있습니다.

```python
import matplotlib.pyplot as plt
import pandas as pd # 예시를 위한 임포트

# 예시 데이터 (실제 강의에서는 'wine' 데이터셋의 'alcohol' 컬럼 사용)
# df = wine_data['alcohol'] # df는 pandas Series 객체라고 가정
x = pd.Series([11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0]) # 예시 데이터

plt.hist(x, bins="fd", density=True, cumulative=True, histtype="step")
plt.xlabel("alcohol")
plt.ylabel("cumulative density")
plt.show()
```

*   `plt.hist(x, ...)`: `x`는 플로팅할 데이터입니다 (예: `alcohol` 컬럼).
*   `bins="fd"`: Friedman-Diaconis 규칙을 사용하여 데이터에 적합한 bin 너비를 자동으로 선택합니다. (이전 슬라이드에서 다룬 내용)
*   `density=True`: 히스토그램의 총 면적이 1이 되도록 y축 값을 정규화합니다.
*   `cumulative=True`: 이 옵션을 `True`로 설정하여 누적 히스토그램을 생성합니다. 이로 인해 y축이 누적 밀도를 나타내게 됩니다.
*   `histtype="step"`: 막대 그래프 대신 스텝 함수 형태의 선 그래프로 플롯을 그립니다. 이는 누적 분포를 시각화하는 데 더 적합합니다.
*   `plt.xlabel("alcohol"); plt.ylabel("cumulative density")`: x축과 y축에 각각 'alcohol'과 'cumulative density'라는 레이블을 추가하여 그래프의 의미를 명확히 합니다.

### 구체적 예시
슬라이드의 그래프는 'alcohol' 데이터의 누적 히스토그램을 보여줍니다. 예를 들어, 'alcohol' 값이 대략 12.0 이하인 데이터는 전체의 약 25%를 차지하며, 'alcohol' 값이 14.0 이하인 데이터는 전체의 약 80%를 차지함을 그래프에서 확인할 수 있습니다. 이처럼 특정 값 이하의 데이터 비율을 쉽게 파악할 수 있습니다.

### 강의 맥락
교수님은 누적 히스토그램을 "최종 히스토그램 변형(final histogram variant)"으로 소개하며, `cumulative=True`와 `histtype="step"` 옵션을 통해 생성됨을 강조했습니다. 이 플롯은 "y-축이 누적 밀도(cumulative density) 또는 주어진 `x` 값보다 작거나 같은 데이터의 비율(proportion of data less than or equal to a given x value)을 나타낸다"고 설명했습니다. 또한, "분위수(quantile)를 읽고 확률적 지배(stochastic dominance) 개념을 파악하는 데 탁월하다"고 그 유용성을 강조하며, 이 개념은 "다음 주제인 ECDF(Empirical Cumulative Distribution Function)로 넘어가는 완벽한 다리(perfect bridge)" 역할을 한다고 언급했습니다.

### 시험 포인트
*   ⭐ **누적 히스토그램의 정의 및 목적**: 데이터의 누적 분포를 시각화하며, 특정 값 이하의 데이터 비율을 보여준다.
*   ⭐ `plt.hist()` 함수에서 누적 히스토그램을 생성하기 위한 핵심 매개변수: `cumulative=True` 및 `histtype="step"`.
*   ⭐ 누적 히스토그램의 y-축이 의미하는 바를 정확히 이해하고 설명할 수 있어야 한다: **누적 밀도 또는 주어진 `x` 값보다 작거나 같은 데이터의 비율**.
*   ⭐ **누적 히스토그램의 주요 활용처**: 분위수를 읽고, 확률적 지배를 파악하며, ECDF로의 연결점 역할을 한다.

---

## Slide 12

---

### ECDF — Bin-free Cumulative View

**핵심 개념**:
**ECDF (Empirical Cumulative Distribution Function)**는 데이터의 누적 분포를 시각화하는 방법으로, 특정 값 $x$ 이하의 데이터 포인트 비율을 보여줍니다. 이는 히스토그램과 달리 빈(bin) 선택에 따른 인위적인 영향을 받지 않는 "bin-free" 방식입니다.

**코드/수식 해설**:
ECDF는 다음과 같이 정의됩니다:
$$
\hat{F}(x) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}_{\{x_i \le x\}}, \quad 0 \le \hat{F}(x) \le 1
$$
- $\hat{F}(x)$: 주어진 값 $x$ 이하인 데이터 포인트의 비율을 나타내는 ECDF 값입니다.
- $n$: 전체 데이터 포인트의 개수입니다.
- $\mathbf{1}_{\{x_i \le x\}}$: 지시 함수(indicator function)로, $x_i \le x$가 참일 경우 1, 거짓일 경우 0의 값을 가집니다. 즉, $x$보다 작거나 같은 데이터 포인트의 개수를 세는 역할을 합니다.

**강의 맥락**:
교수님께서는 ECDF를 누적 히스토그램의 "bin-free 버전"으로 소개하며, "bins"나 "edges"를 선택할 필요가 없어 히스토그램의 인위적인 영향을 피할 수 있다고 강조하셨습니다.
ECDF를 사용하는 주된 이유로 다음 세 가지를 언급하셨습니다:
1.  **Bin-free**: "there is no beam with all edges to choose, so you avoid all histogram artifacts."
2.  **Robust comparison**: 특히 샘플 크기($n$)가 다른 경우에도 분포를 "robust"하게 비교할 수 있습니다. "Excellent when you have unequal sample sizes."
3.  **Quantiles at a glance**: 중앙값($0.5$)이나 90번째 백분위수($0.9$)와 같은 분위수(quantiles)를 y축에서 쉽게 읽어낼 수 있습니다. "median, 50% quantile is simply the x-value where the ECDF crosses 0.5".

ECDF의 주요 특성 및 팁은 다음과 같습니다:
-   **비감소 계단 함수(Non-decreasing step function)**: ECDF는 $x$ 값이 증가함에 따라 $y$ 값이 감소하지 않는 계단 형태의 함수이며, 각 데이터 포인트에서 $1/n$만큼 점프합니다.
-   **Ties produce larger jumps**: 동일한 값을 가진 데이터 포인트($x$)가 여러 개 있을 경우, 해당 지점에서 더 큰 폭으로 점프합니다.
-   **Overlay multiple ECDFs**: 여러 ECDF를 겹쳐 그려 분포들을 비교할 수 있습니다. "A curve that is shifted to right consists of stochastic larger values."
-   **KS distance**: 두 ECDF 사이의 최대 수직 간격(Kolmogorov-Smirnov distance)은 두 표본이 동일한 분포에서 왔는지 진단하는 간단한 척도로 사용될 수 있습니다.

**시험 포인트**:
*   ⭐ **ECDF의 정의**: ECDF가 무엇인지, 어떤 수식으로 표현되는지 이해하는 것이 중요합니다. 특히, "fraction of data points that are less than or equal to x"라는 정의와 지시 함수를 포함한 수식을 기억하세요.
*   ⭐ **ECDF의 장점**: "Bin-free", "Robust comparison (especially for unequal sample sizes)", "Quantiles at a glance" 이 세 가지 핵심적인 장점은 시험에 자주 나올 수 있습니다.
*   ⭐ **ECDF의 특징**: ECDF가 비감소 계단 함수이며, 각 데이터 포인트에서 $1/n$만큼 점프하고, 동일한 값(tied values)에서 더 큰 점프를 보인다는 점을 기억하세요.

---

## Slide 13

**핵심 개념**:
경험적 누적 분포 함수(ECDF, Empirical Cumulative Distribution Function)는 데이터 포인트 중 특정 값 $x$보다 작거나 같은 비율을 나타내는 플롯입니다. 히스토그램과 달리 빈(bin) 선택에 구애받지 않아 데이터의 원래 모양을 그대로 보여주며, 샘플 크기가 다른 그룹 간의 분포를 비교하는 데 매우 강건(robust)합니다. ECDF는 비감소(non-decreasing) 계단 함수 형태를 가지며, 각 데이터 포인트에서 $1/n$만큼 점프합니다.

**코드/수식 해설**:
*   **단일 샘플 ECDF 플롯**:
    ```python
    sns.ecdfplot(data=iris, x="sepal length (cm)")
    ```
    `seaborn` 라이브러리의 `ecdfplot` 함수를 사용하여 `iris` 데이터셋의 `sepal length (cm)` 컬럼에 대한 ECDF를 그립니다. 이는 기본적인 ECDF 플롯을 생성합니다.

*   **그룹 비교 ECDF 플롯**:
    ```python
    sns.ecdfplot(data=iris, x="sepal length (cm)", hue="species")
    plt.ylabel("ECDF")
    ```
    `hue` 파라미터를 `species`로 설정하여 `iris` 데이터셋의 각 종(species)별로 `sepal length (cm)`에 대한 ECDF를 그립니다. 이는 여러 그룹의 분포를 한 번에 비교할 수 있게 해주며, 샘플 크기가 같지 않은 경우에도 매우 안정적이고 정확한 비교를 제공합니다.

**구체적 예시**:
슬라이드 하단 그래프는 Iris 데이터셋의 세 가지 종(setosa, versicolor, virginica)에 대한 `sepal length (cm)`의 ECDF를 보여줍니다.
*   **Setosa (파란색)**: 세 가지 종 중 `sepal length`가 가장 작은 경향을 보입니다.
*   **Versicolor (주황색)**: Setosa보다 `sepal length`가 크고, Virginica보다는 작은 중간 분포를 보입니다.
*   **Virginica (초록색)**: `sepal length`가 가장 큰 경향을 보입니다. ECDF 곡선이 다른 곡선보다 오른쪽으로 이동해 있습니다.

**강의 맥락**:
교수님은 ECDF가 히스토그램의 '빈(bin)이 없는' 누적 보기를 제공한다고 강조하며, 다음과 같은 특징과 활용법을 설명하셨습니다.
*   **빈-프리(Bin-free)**: ⭐히스토그램의 빈 선택 아티팩트(artifacts)를 피할 수 있습니다.
*   **강건한 비교(Robust comparison)**: ⭐특히 샘플 크기($N$)가 같지 않은 그룹 간의 비교에 탁월합니다.
*   **분위수(Quantiles) 읽기**: ECDF 그래프에서 $y$축의 특정 비율에 해당하는 $x$값을 쉽게 찾아 분위수를 확인할 수 있습니다 (예: 중앙값은 $y$축 0.5 지점에서 ECDF 곡선과 만나는 $x$값).
*   **비감소 계단 함수(Non-decreasing step function)**: 각 데이터 포인트에서 $1/N$만큼 점프하며, 동일한 값이 많을수록 더 큰 점프를 보입니다.
*   **그룹 비교 해석**: ⭐오른쪽으로 시프트된 ECDF 곡선은 더 큰 값들로 구성된 분포(확률적으로 더 큰 값)를 의미합니다. `seaborn`에서 `ecdfplot`을 사용하여 `hue` 파라미터를 그룹 변수에 설정하면 다양한 샘플 크기를 가진 그룹도 안전하고 강건하게 비교할 수 있습니다.

---

## Slide 14

**핵심 개념**:
이 슬라이드는 소규모 샘플 데이터($$n=6$$)로부터 전체 모집단의 분포를 추정하는 어려운 문제에 대해 설명합니다. 히스토그램이 작은 데이터에 민감한 한계를 극복하기 위해 KDE(Kernel Density Estimate)가 도입됩니다. KDE는 데이터의 내재된 밀도를 부드러운 정량적 추정치로 변환하여 보여줍니다.

**구체적 예시**:
*   **문제**: 적은 수의 샘플($$n=6$$)로 모집단의 분포를 추정하는 것.
*   **샘플**: 45, 52, 58, 78, 82, 95 (예: 6개의 시험 점수)
*   **직관**: 이 샘플은 대략 50점 근처, 80점 근처, 그리고 95점 근처에 고득점자가 있는 그룹들을 암시합니다.
*   **KDE의 역할**: 이러한 직관을 데이터의 근원적인 밀도에 대한 부드럽고 정량적인 추정치로 변환합니다.

**강의 맥락**:
교수님은 "세 번째 주요 플롯인 KDE로 넘어갈 슬라이드 14입니다. 우리가 해결하려는 문제는 작은 샘플 데이터로부터 그것이 유래한 모집단 분포를 어떻게 추정할 수 있는가입니다"라고 이 슬라이드의 목적을 명확히 설명합니다. 이어서 "샘플은 단 6개의 시험 점수입니다. 우리의 직관은 이 샘플이 50점 근처, 80점 근처에 그룹들이 있고 95점에 고득점자가 있다는 것을 암시합니다"라고 구체적인 예시와 직관을 제시합니다. 마지막으로 "데이터가 너무 적으면 히스토그램은 빈 배치에 매우 민감합니다. 하지만 KDE 플롯을 사용하면, KDE는 이 데이터를 근원적인 밀도의 부드럽고 정량적인 추정치로 바꿉니다"라고 KDE의 필요성과 역할을 강조합니다. 특히 작은 샘플 크기에서 히스토그램의 한계를 지적하며 KDE의 장점을 부각합니다.

**시험 포인트**:
*   ⭐KDE가 **작은 샘플 크기**에서 모집단 분포의 **부드러운 밀도 추정**을 제공하여 히스토그램의 한계를 극복하는 데 사용된다는 점을 이해하는 것이 중요합니다.

---

## Slide 15

### 핵심 개념
*   **Fundamental Insight: Local Evidence**: KDE(Kernel Density Estimate)의 핵심은 각 관측치 $x_i$가 자신뿐만 아니라 주변(neighborhood)에 대한 정보를 담고 있다는 생각입니다. 즉, 데이터 포인트 하나하나가 국소적인 증거(local evidence)를 제공합니다.
*   **Kernel Idea (커널 아이디어)**: 각 개별 데이터 포인트 $x_i$에 작은 종 모양의 확률 곡선(kernel)을 배치하여 주변 값에 대한 우리의 신뢰도를 인코딩합니다.
*   **Local Evidence 기여**: 각 종 모양의 커브는 $x_i$ 근처의 점수에 대해 '국소적 증거'를 기여하며, $x_i$에서 멀어질수록 기여도가 작아집니다. 최종 KDE 곡선은 이 개별 커널들의 합 또는 평균으로 이루어집니다.

### 구체적 예시
슬라이드 하단의 그래프는 이러한 KDE의 직관을 보여줍니다.
*   하단에 파란색 점으로 표시된 세 개의 데이터 포인트(52, 82, 95)가 있습니다.
*   각 데이터 포인트마다 주황색(52), 초록색(82), 빨간색(95)의 종 모양 가우시안 커브(kernel)가 배치됩니다.
*   이 세 개의 개별 가우시안 커브들을 합산 또는 평균하여 보라색으로 표시된 최종 KDE 곡선이 생성됩니다. 이 곡선은 데이터의 전반적인 밀도 추정치를 나타냅니다.

### 강의 맥락
교수님은 KDE에 대한 설명에 앞서 작은 표본 데이터로부터 모집단 분포를 추정하는 어려움을 언급하며 히스토그램이 데이터가 적을 때 bin 배치에 매우 민감하다고 지적합니다. 이어서 KDE가 데이터를 부드러운 정량적 밀도 추정치로 변환한다고 설명합니다.

*   "Okay, so the fundamental inside of KDE is the idea of **local evidence**. Okay, **local evidence**. This is **very important**." (KDE의 근본적인 통찰은 '국소적 증거'라는 아이디어입니다. 국소적 증거, 이것은 매우 중요합니다.) ⭐
*   "So each observed data point can raise information not just about itself, but about its neighbor." (각 관측된 데이터 포인트는 자신뿐만 아니라 이웃에 대한 정보도 제공합니다.)
*   "So the **kernel idea** is to place a small bell-shaped probability curve. which is called **kernel** at each individual data point." (커널 아이디어는 각 개별 데이터 포인트에 커널이라고 불리는 작은 종 모양의 확률 곡선을 배치하는 것입니다.) ⭐
*   "Suppose that we have three data point here and then we place a bell-shaped probability curve, right? ... So the final curve shown in black, not black, purple, is essentially the sum or average of all these individual corners. That's the definition actually." (여기에 세 개의 데이터 포인트가 있다고 가정하고 종 모양의 확률 곡선을 배치합니다. ... 검은색, 아니 보라색으로 표시된 최종 곡선은 본질적으로 이 모든 개별 커널들의 합 또는 평균입니다. 이것이 실제 정의입니다.)

### 시험 포인트
*   KDE의 ⭐**근본적인 통찰(Fundamental Insight)**이 무엇인지 설명할 수 있어야 합니다. (정답: Local Evidence)
*   KDE가 밀도 곡선을 생성하는 ⭐**커널 아이디어(Kernel Idea)**의 작동 방식을 설명할 수 있어야 합니다. (정답: 각 데이터 포인트에 종 모양의 커널을 배치하고 이들을 합산/평균하여 최종 곡선을 얻음)

---

## Slide 16

### 핵심 개념
KDE(Kernel Density Estimate)는 주어진 데이터 샘플로부터 모집단의 확률 밀도 함수(PDF)를 비모수적으로 추정하는 방법입니다. 각 개별 관측치 $x_i$에 커널(대부분 종 모양의 확률 분포)을 배치하고, 이 커널들의 값을 평균하여 전체 데이터의 부드러운 밀도 추정 곡선을 생성합니다. KDE의 핵심은 **"Local Evidence"**와 **"Averaging Predictions"**입니다.

### 코드/수식 해설
KDE의 작동 방식은 다음 세 단계로 요약됩니다:
1.  각 관측치 $x_i$에 커널을 중앙에 배치합니다.
2.  쿼리 지점 $x$에 대해 각 커널의 해당 지점에서의 값(예측치)을 읽습니다.
3.  이 모든 $n$개 예측치를 평균합니다.

KDE 추정량은 다음과 같은 수식으로 정의됩니다:
$$ \hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right) $$
이때, $\hat{f}_h(x)$는 확률 밀도 함수이므로 전체 면적은 1이 됩니다:
$$ \int \hat{f}_h(x) \, dx = 1 $$

*   $K$: **커널 함수**로, 각 데이터 포인트에 배치되는 확률 분포입니다. (종종 가우시안 분포가 사용됩니다.)
*   $h$: **대역폭(bandwidth)**으로, 각 커널의 너비를 제어하는 파라미터입니다. 이는 KDE 곡선의 부드러운 정도(smoothness)를 조절하는 중요한 '스무딩 노브(smoothness knob)' 역할을 합니다.
*   $x_i$: $i$번째 개별 관측치입니다.
*   $n$: 전체 데이터 포인트의 개수입니다.
*   $1/nh$: 추정량 전체가 1로 정규화되도록 하는 상수입니다.

### 구체적 예시
강의에서 언급되었듯, 예를 들어 3개의 데이터 포인트가 있다면 각 포인트에 작은 종 모양의 확률 곡선을 놓습니다. 최종 KDE 곡선은 이 3개 개별 커널 곡선들의 합 또는 평균이 됩니다. 이 과정이 데이터를 부드러운 밀도 추정치로 변환합니다.

### 강의 맥락
교수님은 KDE가 "소규모의 데이터 샘플로부터 모집단 분포를 어떻게 추정할 수 있는가"라는 질문에 답하는 방법이라고 설명했습니다. 특히, "KDE turns this data into a smooth quantitative estimate of the underlying density"라고 강조하며, KDE의 **핵심은 "local evidence"**에 기반하여 각 데이터 포인트가 자신뿐만 아니라 이웃에 대한 정보도 제공한다는 점이라고 했습니다.

슬라이드의 "How it works" 세 가지 단계는 교수님의 설명과 정확히 일치합니다: "you center a kernel at each observation $x_i$", "you read the height of every kernel at that point", "and then you then average those $n$ predictions".

수식에 대해서는 $\hat{f}_h(x)$가 $n$개의 커널을 평균한 것이며, 각 커널 $K$가 $x_i$에 중앙이 맞춰지고 대역폭 $h$에 의해 스케일링된다고 설명했습니다. 특히 $1/nh$ 항이 전체 함수가 1로 적분되도록 하는 **"normalization constant"**임을 강조하여 KDE 곡선이 PDF의 특징을 갖도록 한다고 설명했습니다.

$K$는 커널 함수(대부분 가우시안)이고 $h$는 **대역폭**이라고 명시하며, "bandwidth $h$ is critical. Smoothness knob you have to tune." 이라고 대역폭의 중요성을 강조했습니다.

### 시험 포인트
*   ⭐ **KDE의 작동 원리**: 각 데이터 포인트에 커널을 배치하고 이들을 평균하여 밀도 추정 곡선을 만드는 과정.
*   ⭐ **KDE 추정량 수식의 이해**: 수식의 각 항($K, h, x_i, n, 1/nh$)이 무엇을 의미하는지 정확히 알아야 합니다.
*   ⭐ **대역폭 $h$의 역할**: KDE의 "smoothness knob"으로서 $h$가 너무 작거나 클 때 그래프가 어떻게 달라지는지 이해하는 것이 중요합니다. (다음 슬라이드에서 더 자세히 다루지만, 여기서 개념을 잡아야 함)

---

## Slide 17

**핵심 개념**:
KDE(Kernel Density Estimate)에서 커널의 너비를 결정하는 **대역폭(bandwidth) $h$**는 추정된 밀도 곡선의 부드러움(smoothness)을 조절하는 가장 중요한 매개변수입니다. $h$ 값에 따라 그래프의 형태가 크게 달라지며, 적절한 $h$를 선택하는 것이 중요합니다.

**코드/수식 해설**:
*   **$h$의 선택**: 최적의 $h$를 찾기 위해 교차 검증(cross-validation) 또는 플러그인 규칙(plug-in rules)을 사용합니다.
*   **Seaborn에서의 대역폭 조정**: Seaborn 라이브러리에서는 데이터 기반의 기본 대역폭 $h_{base}$를 자동으로 선택하며, 사용자는 `bw_adjust` 인자를 통해 이 값을 조정할 수 있습니다.
    $$ h_{used} = \text{bw\_adjust} \times h_{base} $$
    *   `bw_adjust` 값이 작으면 더 세부적인(detail) 플롯이, 크면 더 부드러운(smoother) 플롯이 생성됩니다.

**강의 맥락**:
교수님께서는 대역폭 $h$가 KDE에서 가장 핵심적인 개념이자 조절해야 할 "smoothness knob"임을 강조하셨습니다.
*   ⭐ **$h$가 너무 작을 때($h \downarrow$): Under-smooth (과소 평활)**
    *   추정치가 들쭉날쭉하고(jagged) 노이즈가 많아집니다.
    *   실제 분포에 없는 여러 개의 가짜 봉우리(spurious peaks)가 나타날 수 있습니다. (sample artifacts)
*   ⭐ **$h$가 너무 클 때($h \uparrow$): Over-smooth (과대 평활)**
    *   추정치가 흐릿하고(blurry) 평평해집니다.
    *   데이터의 진정한 모드(modes)나 중요한 구조를 놓칠 수 있습니다.
*   Seaborn에서는 데이터 기반으로 선택된 기본 대역폭이 제공되며, `bw_adjust` 인자를 사용하여 이를 조절할 수 있습니다. `bw_adjust` 값이 작으면 더 자세한 모양을, 크면 더 부드러운 모양을 보여준다고 설명하셨습니다.

**시험 포인트**:
*   ⭐ KDE에서 대역폭 $h$가 어떤 역할을 하는지, 그리고 $h$가 너무 작거나 클 때 그래프가 어떻게 변하는지 (under-smooth, over-smooth) 이해하는 것이 중요합니다.
*   ⭐ `bw_adjust`가 대역폭을 어떻게 조정하며, 그 결과 그래프의 디테일과 부드러움에 어떤 영향을 미치는지 알아두세요.

---

## Slide 18

### 핵심 개념

KDE(Kernel Density Estimate)는 히스토그램의 한계를 넘어 데이터의 분포 형태(모드, 꼬리 행동)를 부드럽게 추정하고, 여러 그룹 간의 모양을 비교하는 데 사용됩니다.

*   **사용 시점 (When to use)**: 히스토그램의 빈(bin) 설정에 따른 한계를 넘어 데이터의 모드(peak)와 꼬리(tail) 행동을 상세히 파악하고, 여러 그룹의 분포 '모양'을 비교할 때 유용합니다.
*   **경계 처리 (Boundaries)**: 데이터가 특정 범위(예: $x \ge 0$인 양수 값)에 한정될 때, KDE가 경계를 넘어 밀도를 추정하는 문제를 피하기 위해 반사(reflection) 기법을 사용하거나 데이터를 변환(예: `log` 변환)해야 합니다.
*   **그룹 비교 (Groups)**: 여러 그룹을 비교할 때는 일관된 설정(공통된 축 범위)을 사용하고, 밀도로 정규화하는 경우 '개수'보다는 '모양'을 비교하는 데 초점을 맞춥니다.
*   **비모수적 특징 (Nonparametric power)**: KDE는 비모수적(non-parametric) 방법으로, 데이터가 단봉형(unimodal), 이봉형(bimodal), 다봉형(multimodal) 등 어떤 형태를 가지든 엄격한 가정 없이 분포에 적응합니다.

### 강의 맥락

교수님은 KDE의 활용법, 경계 문제 처리, 그룹 비교 시 주의사항, 그리고 비모수적 특성을 강조하며 설명하셨습니다.

"So when to use it? So use a KDE to reveal Moh's entailed behavior, especially when you want to get beyond the limitation of history and meaning. And it is excellent for comparing the shapes of different groups." (KDE의 주요 용도를 설명하며, 히스토그램의 한계를 넘어 분포의 모드와 꼬리를 파악하고, 그룹 간 모양 비교에 탁월함을 강조)

"Standard KDE does not know about data boundaries. So if data is bounded, for example, it cannot be negative, the KDE spill the density over the boundary. So this would be problem. So you can reduce this bias by using reflection or by transforming the data first. Maybe you can use some log function. You can take a log." (데이터가 양수 값만 가지는 등 경계가 있을 때, KDE가 밀도를 경계 밖으로 "유출"시키는 문제를 지적하며, 이를 피하기 위해 데이터 변환(예: `log` 변환)이나 반사 기법을 사용할 수 있음을 설명)

"When comparing groups, Make sure that you use a consistent setting. Okay. Common axis limits. And if you normalize my density, compare shape rather than just count." (그룹을 비교할 때 일관된 설정(공통 축 범위)의 중요성을 강조하고, 밀도 정규화 시 개수가 아닌 '모양'을 비교해야 함을 재차 강조)

"So a real power of KDE is a non-parametric. Okay. So this is non-parametric. Okay, let me write down. KDE is non-parametric. Which means that it will adapt to whatever shape your data has. Unimodal, bimodal, and multimodal. So without you having to make rigid assumptions. Because this is non-parameter." (KDE의 가장 큰 장점 중 하나인 비모수적 특성을 설명하며, 데이터를 단봉형, 이봉형, 다봉형 등 어떠한 형태로든 유연하게 모델링할 수 있음을 강조)

### 시험 포인트

*   ⭐ **KDE의 주요 사용 목적**: 히스토그램의 한계를 극복하고 데이터의 모드 및 꼬리 행동을 부드럽게 파악하며, 특히 그룹 간 '분포 모양'을 비교하는 데 강점이 있습니다.
*   ⭐ **경계 데이터 처리 방법**: 데이터에 경계(예: 음수 불가)가 있을 경우, KDE의 밀도 유출(spill over) 문제를 해결하기 위해 `reflection` 또는 `log transform`과 같은 `transformations`을 적용해야 합니다.
*   ⭐ **KDE의 비모수적 특징**: KDE는 데이터 분포에 대한 어떠한 사전 가정(예: 정규 분포) 없이 데이터의 실제 형태(단봉형, 이봉형, 다봉형 등)에 유연하게 적응하는 비모수적인 방법이라는 점을 이해해야 합니다.

---

## Slide 19

---

### 핵심 개념

*   **로버스트 요약(Robust Summaries)**: 이상치(outliers)의 영향을 덜 받는 방식으로 데이터의 중앙 경향성 및 분포의 확산 정도를 요약하는 통계량입니다.
    *   **중앙값(Median)**: 데이터를 정렬했을 때 중앙에 위치하는 값으로, 50번째 백분위수($P_{50}$)입니다.
    *   **사분위 범위(IQR - Interquartile Range)**: 3사분위수($Q_3$, 75번째 백분위수)에서 1사분위수($Q_1$, 25번째 백분위수)를 뺀 값입니다. 데이터의 중간 50%가 분포하는 범위를 나타냅니다.
    *   **중앙 절대 편차(MAD - Median Absolute Deviation)**: 데이터 포인트들이 중앙값으로부터 얼마나 떨어져 있는지에 대한 분산 측도로, 편차들의 중앙값을 사용하므로 이상치에 매우 강건합니다.
*   **활용 동기**:
    *   여러 그룹의 데이터를 한눈에 간결하게 요약하고 비교하기 위해 사용됩니다.
    *   표본 크기(`n`)가 작을 때는 원시 데이터 포인트(raw points)를 추가하여 시각화합니다.
    *   `n`이 클 때는 `boxen plot`을 선호하여 데이터의 꼬리(tails) 부분을 더 상세하게 파악합니다.

### 코드/수식 해설

*   **IQR(Interquartile Range)**
    $$
    \text{IQR} = Q_3 - Q_1
    $$
    여기서 $Q_3$는 75번째 백분위수, $Q_1$은 25번째 백분위수를 나타냅니다.

*   **MAD(Median Absolute Deviation)**
    $$
    \text{MAD} = \text{median}(|x_i - \text{median}(x)|)
    $$
    여기서 $x_i$는 개별 데이터 포인트, $\text{median}(x)$는 데이터셋의 중앙값을 의미합니다. 각 데이터 포인트와 중앙값의 절대 편차를 구한 후, 이 편차들의 중앙값을 계산합니다.

### 강의 맥락

교수님은 **로버스트 요약**의 개념을 설명하며, 이전에 다룬 히스토그램과 같은 요약 통계량의 연장선상에 있음을 언급합니다. 특히, `Median`은 익숙하지만, `IQR`과 `MAD`는 처음 접할 수 있는 개념임을 강조하며 자세한 정의를 알려주셨습니다.

*   **IQR**은 "inter quartile range"의 약자이며, $Q_3$ (75th percentile)에서 $Q_1$ (25th percentile)을 뺀 값이라고 명확히 정의하면서 ⭐**시험에 출제될 수 있는 중요한 개념**임을 시사했습니다.
*   **MAD**는 "median absolute deviation"의 약자로, 중앙값으로부터의 절대 편차들의 중앙값으로 정의되며, 이상치에 강한 분산 측도임을 설명했습니다.

이러한 로버스트 요약 통계량들은 주로 **박스 플롯(box plot)**의 기초가 되며, 여러 그룹의 데이터를 한 번에 효율적으로 요약하고 비교하는 데 매우 유용하다고 강조했습니다.

### 시험 포인트

*   ⭐**중앙값($\text{Median}$), 사분위 범위($\text{IQR}$), 중앙 절대 편차($\text{MAD}$)의 정의와 의미를 정확히 이해해야 합니다.** 특히 이들이 이상치에 강건한(robust) 통계량이라는 점을 기억하세요.
*   ⭐**IQR 및 MAD의 수식을 암기하고 그 의미를 설명할 수 있어야 합니다.**
*   ⭐이러한 로버스트 요약 통계량들이 박스 플롯(boxplot), 바이올린 플롯(violin plot), 박스젠 플롯(boxen plot)과 같은 시각화 도구의 기반이 된다는 점을 알아두세요.

---

## Slide 20

### 핵심 개념
*   **Box Plot (Tukey)**: 데이터의 견고한 요약(중앙값, IQR, 위스커, 이상치)을 제공합니다. 빠르게 읽을 수 있지만, 사분위수 내부의 분포 형태를 숨깁니다.
*   **Violin Plot**: Box Plot에 KDE(Kernel Density Estimate) 형태를 더하여 분포의 다중 모드(multimodality), 왜도(skewness), 꼬리(tails) 부분을 시각화합니다. KDE를 사용하므로 대역폭(bandwidth) 설정에 민감합니다.
*   **Boxen Plot (Letter-Value Plot)**: 사분위수를 넘어 더 깊은(더 세분화된) 분위수들을 표시하며, 특히 큰 샘플 크기($N$) 데이터의 꼬리 부분을 신뢰성 있게 시각화하기 위해 고안되었습니다.
*   **핵심 차이**: Box Plot과 Violin Plot의 가장 큰 차이점은 Violin Plot은 KDE를 사용하여 분포 형태를 보여주지만, Box Plot은 KDE를 사용하지 않는다는 점입니다.

### 강의 맥락
교수님은 **로버스트 요약(Robust Summaries)** 설명 이후 이 세 가지 플롯을 소개하며 "이러한 견고한 데이터는 Box, Violin, Boxen 플롯 패밀리로 우리를 이끈다"고 언급했습니다.

*   **Box Plot**: "견고한 요약: 중앙값, IQR, 위스커, 이상치를 제공한다"고 설명하며, "읽기 매우 빠르지만, 메인 박스 안에 분포의 형태를 숨긴다"고 강조했습니다. 이 플롯이 "가장 널리 사용되는 플롯이므로 매우 익숙해야 한다"고 덧붙였습니다.
*   **Violin Plot**: "Box Plot *플러스* KDE 플롯, 즉 KDE 형태"라고 설명하며, "다중 모달리티, 왜도, 꼬리를 드러낸다"고 말했습니다. 또한 "일반 KDE와 동일하게 대역폭 선택에 민감하다"고 주의를 주었습니다. Violin Plot의 너비가 "해당 지점의 추정 밀도에 비례한다"고 언급했습니다.
*   **Boxen Plot**: "큰 $N$을 위해 설계되었다"며, "사분위수 이상으로 더 깊은 사분위수를 제공하여 꼬리를 훨씬 더 생생하게 시각화할 수 있다"고 강조했습니다.

교수님은 이 세 플롯의 가장 큰 차이점으로 "Box Plot과 Violin Plot의 가장 큰 차이점은 KDE의 사용이다"라고 명확히 언급했습니다.

### 시험 포인트
*   ⭐ **Box Plot, Violin Plot, Boxen Plot 각각의 주요 용도와 특징**을 명확히 이해해야 합니다.
*   ⭐ **Box Plot과 Violin Plot의 가장 큰 차이점은 KDE 사용 여부**라는 점을 기억하세요 (Violin은 KDE 사용, Box는 사용하지 않음).
*   ⭐ **Boxen Plot이 큰 $N$ 데이터의 꼬리 부분을 시각화하는 데 특히 유용**하다는 점을 알아두세요.

---

## Slide 21

**핵심 개념**
박스 플롯(Box Plot), 또는 터키 플롯(Turkey Plot)은 데이터의 분포를 시각적으로 요약하고 여러 그룹 간의 분포를 비교하는 데 사용되는 그래프입니다. 이 플롯은 데이터의 중앙값, 사분위수(Interquartile Range, IQR), 수염(whiskers), 그리고 이상치(outliers)를 간결하게 보여줍니다.

**코드/수식 해설**
*   **중앙값 (Median, $Q_2$)**: 데이터를 크기 순으로 정렬했을 때 가운데 위치하는 값 (50번째 백분위수)으로, 박스 안의 선으로 표시됩니다.
*   **상자 (Box)**: 1사분위수($Q_1$, 25번째 백분위수)부터 3사분위수($Q_3$, 75번째 백분위수)까지의 범위를 나타냅니다. 이 범위가 바로 사분위수 범위(`IQR`)입니다.
    $$IQR = Q_3 - Q_1$$
*   **수염 (Whiskers)**: 일반적으로 $Q_1 - 1.5 \times IQR$부터 $Q_3 + 1.5 \times IQR$ 이내에 있는 가장 극단적인 데이터 포인트까지 확장됩니다.
*   **이상치 (Outliers)**: 수염의 범위를 벗어나는 개별 데이터 포인트들입니다. Seaborn에서는 `showfliers=True`가 기본값입니다.

**구체적 예시**
슬라이드에 제시된 이미지에서 박스 플롯의 각 구성 요소(중앙값, $Q_1$, $Q_3$, IQR, 수염, 이상치)가 데이터 분포에서 어떤 위치와 의미를 가지는지 시각적으로 확인할 수 있습니다.

**강의 맥락**
*   교수님은 박스 플롯이 "군집 비교에 표준적인 방법"이며, 가장 널리 사용되는 플롯이므로 "매우 익숙해야 한다"고 강조하셨습니다.
*   박스 플롯의 해부학적 구조에 대해 자세히 설명했습니다:
    *   "상자 자체는 1사분위수($Q_1$, 25번째 백분위수)부터 3사분위수($Q_3$, 75번째 백분위수)까지의 사분위수 범위(IQR)를 나타냅니다."
    *   "수염은 일반적으로 박스 끝에서 $1.5 \times IQR$ 이내의 가장 극단적인 데이터 포인트까지 뻗어 나갑니다."
    *   "이 수염을 넘어가는 모든 포인트는 개별적인 이상치(outlier)로 그려집니다."
*   박스 플롯의 **장점**은 "견고하고(robust), 간결하며(compact), 여러 그룹 간의 중앙값과 분포 확산을 비교하는 데 탁월하다"는 점입니다.
*   **한계점**으로는 "데이터가 이봉 분포(bimodal)이거나 사분위수 내부에 다른 흥미로운 형태를 가지고 있는지 보여주지 못한다"는 점을 언급했습니다. 즉, 분포의 세부적인 모양을 숨깁니다.
*   Seaborn에서 박스 플롯을 그릴 때 `showfliers`, `whis`, `notch`와 같은 파라미터를 조절할 수 있습니다.

**시험 포인트**
*   ⭐박스 플롯의 주요 구성 요소(중앙값, 상자, 수염, 이상치)와 각각이 나타내는 통계적 의미를 정확히 이해해야 합니다.
*   ⭐수염의 확장 범위가 '$1.5 \times IQR$' 규칙에 의해 결정된다는 것을 기억해야 합니다.
*   ⭐박스 플롯의 장점(로버스트한 요약, 간결함, 그룹 간 비교 용이성)과 한계점(분포의 세부적인 모양이나 다중 모드 여부를 알 수 없음)을 명확히 구분할 수 있어야 합니다.

---

## Slide 22

### 핵심 개념
*   **바이올린 플롯(Violin Plot) 정의**: 박스 플롯(Box plot)에 KDE (Kernel Density Estimate) 형태를 결합하여 데이터 분포의 밀도를 시각적으로 표현하는 그래프입니다.
*   **KDE Envelope**: 플롯의 중심을 기준으로 미러링된 KDE 곡선으로, 너비가 해당 지점의 데이터 밀도에 비례합니다.
*   **내부 마크 (Inner Marks)**: 바이올린 내부에는 분포의 특정 지점을 표시할 수 있습니다. 예를 들어 `"quartile"` (사분위수), `"box"` (미니 박스 플롯), `"point"` (개별 데이터 점) 또는 아무것도 표시하지 않을 수 있습니다 (`None`).
*   **대역폭 (Bandwidth)의 중요성**: KDE와 마찬가지로 대역폭($h$) 선택에 매우 민감합니다.
    *   **작은 대역폭**: 플롯이 과소평활(under-smooth)되어 노이즈가 많고 실제 데이터에는 없는 봉우리(spurious peaks)를 만들 수 있습니다.
    *   **큰 대역폭**: 플롯이 과대평활(over-smooth)되어 흐릿하고 평탄해져 데이터의 중요한 구조나 특징을 놓칠 수 있습니다.
*   **장점 (Strengths)**: 데이터의 왜도(skewness), 꼬리(tails) 형태, 다봉성(multimodality) 등을 명확하게 시각화하여 분포의 모양을 직관적으로 파악하는 데 유용합니다.
*   **한계 (Limits)**: 대역폭 선택에 민감하며, 작은 표본 크기($n$)에서는 잘못된 봉우리를 생성하여 분포를 오해하게 만들 수 있습니다.
*   **박스 플롯과의 주요 차이점**:
    *   **바이올린 플롯**: 박스 플롯 + KDE 형태로, 너비가 밀도를 인코딩하여 데이터 분포의 모양을 보여줍니다.
    *   **박스 플롯**: 오직 사분위수(median, IQR, whiskers, outliers)와 같은 요약 통계만을 보여줍니다.

### 코드/수식 해설
해당 슬라이드에는 직접적인 코드나 수식 예시가 포함되어 있지 않습니다. `seaborn` 라이브러리의 `violinplot` 함수를 사용하여 구현할 수 있습니다.

### 구체적 예시
(슬라이드에 예시 코드가 없으므로 생략)

### 강의 맥락
교수님은 바이올린 플롯을 "박스 플롯 + KDE 플롯, KDE 쉐이프"로 정의하며, 이것이 바이올린 플롯의 핵심 특징이라고 강조하셨습니다. 플롯의 너비가 "데이터의 추정 밀도에 비례"하여 분포의 모양을 보여준다고 설명하셨습니다. 또한, 바이올린 내부에 "quartile, box, point" 등 다양한 `inner marks`를 지정할 수 있다고 언급하셨습니다. KDE와 동일하게 "대역폭 선택이 중요"하며, 작은 표본 크기에서는 "오해의 소지가 있는 봉우리(misleading bumps)"를 만들 수 있다는 한계점을 지적하셨습니다. 가장 중요한 차이점으로, "바이올림 플러트는 박스 플러트 + KDE 쉐이며 위치에 인코드의 덴스티티를, 박스 플러트는 only shows quantile summaries"라고 말씀하시며, KDE의 사용 여부가 두 플롯의 가장 큰 차이임을 강조하셨습니다.

### 시험 포인트
*   ⭐**바이올린 플롯이 박스 플롯과 KDE의 결합 형태이며, KDE를 통해 데이터 분포의 밀도 정보를 시각화한다는 점.**
*   ⭐**대역폭($h$) 선택의 중요성 (과소/과대평활 시의 문제점).**
*   ⭐**바이올린 플롯의 장점 (왜도, 꼬리, 다봉성 시각화) 및 단점 (대역폭 민감성, 작은 $N$에서의 오독 가능성).**
*   ⭐**박스 플롯과의 주요 차이점: 바이올린 플롯은 KDE를 통해 밀도를 인코딩한 분포 모양을 보여주는 반면, 박스 플롯은 사분위수와 같은 요약 통계만 보여준다는 점.**

---

## Slide 23

**핵심 개념**
Boxen Plot은 'Letter-Value Plot'이라고도 불리며, 중앙값(median)을 중심으로 점진적으로 더 깊은 대칭적인 분위수(quantile) 쌍을 쌓아 올려 데이터 분포의 꼬리 부분을 시각적으로 강조하는 플롯입니다. 이는 특히 데이터의 꼬리 부분에 대한 신뢰할 수 있는 시각화를 제공하며, 큰 샘플 크기($N$)에서 유용합니다.

**코드/수식 해설**
Boxen Plot은 `nested boxes`(중첩된 상자들)로 구성됩니다.
각 상자는 `depth` $j$에 따라 정의되며, 다음 수식을 따릅니다:
$p_j = 2^{-j}$ (단, $j = 1, 2, \ldots, k$)
여기서 $k$는 상자의 깊이를 나타냅니다.

`box` $j$는 분위수 $[Q_{p_j/2}, Q_{1-p_j/2}]$ 범위로 그려집니다.
이는 `box` $j$의 `central mass`가 $1 - p_j$임을 의미합니다.

*   $j=1$일 경우: $p_1 = 2^{-1} = 0.5$. 따라서 `box`는 $[Q_{0.25}, Q_{0.75}]$가 되며, 이는 IQR (25%~75%) 상자를 나타냅니다.
*   $j=2$일 경우: $p_2 = 2^{-2} = 0.25$. 따라서 `box`는 $[Q_{0.125}, Q_{0.875}]$가 되며, 이는 12.5%~87.5% 범위를 나타냅니다.
*   이런 식으로 $j$ 값이 증가함에 따라 $p_j$는 작아지고, `box`는 점점 더 깊은(중앙에서 멀리 떨어진) 분위수 범위까지 확장되어 데이터의 꼬리 부분을 보여줍니다.

**구체적 예시**
첨부된 이미지에서 `fixed depth (k_depth=3)` 예시를 볼 수 있습니다.
*   가장 안쪽의 어두운 파란색 상자는 25th percentile부터 75th percentile까지의 IQR을 나타냅니다. ($j=1$)
*   그 다음 상자는 12.5th percentile부터 87.5th percentile까지의 범위를 보여줍니다. ($j=2$)
*   가장 바깥쪽 상자는 6.25th percentile부터 93.75th percentile까지의 범위를 나타냅니다. ($j=3$)
각 상자는 깊어질수록 너비와 두께가 줄어들어 시각적으로 깊이가 강조됩니다. 중앙값은 선으로 표시됩니다.

**강의 맥락**
교수님께서는 Boxen Plot을 설명하며 다음과 같이 말씀하셨습니다:
"세 번째 플롯은 이 계열의 플롯입니다. 'Letter-Value Plot'이라고도 불립니다. 이 플롯은 `nested boxes`의 스택을 표시합니다. 이 중첩된 상자가 무엇인지 설명해 드릴게요. 중앙값에서 시작하여 각 단계에서 남은 꼬리 질량을 절반으로 줄이는 점진적으로 더 깊은 대칭 분위수 쌍을 추가합니다. 그래서 여기에 하나의 상자가 있습니다. 첫 번째 상자는 25% 분위수부터 75% 분위수까지의 IQR 상자를 보여줍니다. 그런데 만약 $j$가 2로 설정되면, 12.5%에서 87.5%까지를 제공합니다. 그리고 세 번째 상자는 이것을 보여줍니다. 상자들은 너비와 두께가 줄어들면서 그려지므로, 더 깊은 상자들이 시각적으로 강조됩니다. 선은 중앙값을 표시합니다. 이것이 Boxen Plot입니다."

**시험 포인트**
*   ⭐ Boxen Plot이 `nested boxes`를 사용하여 데이터의 꼬리 부분을 시각화하는 방식의 정의를 이해해야 합니다.
*   ⭐ Boxen Plot이 박스플롯(Box Plot) 및 바이올린플롯(Violin Plot)과 비교했을 때, 특히 **대규모 데이터($N$이 큰 경우)**의 **꼬리(tails) 부분을 더 신뢰성 있게 시각화**하는 데 적합하다는 점을 기억하세요.

---

## Slide 24

**핵심 개념**:
`Boxen Plot` (또는 `Letter Value Plot`)은 기존 `Box Plot`보다 더 많은 분위수(quantile) 정보를 보여주어 데이터의 꼬리 부분을 더 상세하게 시각화하는 데 유용합니다. Seaborn 라이브러리에서 `sns.boxenplot` 함수를 사용하여 그릴 때, 데이터의 특성과 시각화 목적에 따라 다양한 옵션을 조절할 수 있습니다.

**코드/수식 해설**:
`sns.boxenplot` 함수 사용 시 주요 옵션들은 다음과 같습니다.
-   `k_depth`: 몇 개의 letter-value 레벨을 그릴 것인지 제어합니다.
    -   "tukey" (기본값): 전통적인 `Box Plot`의 이상치 정의 방식과 유사하게 작동합니다.
    -   "proportion": 최소 꼬리 비율에 도달할 때까지 깊이 있게 그립니다.
    -   "trustworthy": 샘플 크기에 따라 안정적으로 신뢰할 수 있는 수준까지만 깊이 있게 그립니다.
    -   정수 값: 특정 개수의 깊이를 지정합니다.
-   `scale`: 박스의 수평 너비가 깊이에 따라 어떻게 줄어들지 제어합니다.
    -   "exponential" (기본값): 지수적으로 너비가 줄어듭니다.
    -   "linear": 선형적으로 너비가 줄어듭니다.
    -   "area": 박스의 면적에 비례하여 너비가 줄어듭니다.
-   `outlier_prop`: 이상치로 플래그를 지정하는 데 사용되는 꼬리 부분의 비율을 정의합니다.
-   `showfliers`: 이상치(outlier) 포인트를 그릴지 여부를 결정합니다. (기본값은 `True`)
-   `Others`: `width` (박스의 전체 너비), `dodge` (hue 사용 시 그룹 간 박스 분리), `linewidth` (박스 테두리 선 굵기) 등이 있습니다.

**강의 맥락**:
교수님은 `sns.boxenplot` 사용 시 `k_depth`와 `scale` 옵션이 핵심적이라고 강조했습니다. `k_depth`는 "얼마나 많은 레벨을 그릴 것인가"를 제어하며, "trustworthy" 옵션은 샘플 크기가 허용하는 만큼만 깊게 들어가도록 하는 좋은 자동 선택지라고 설명했습니다. 또한 `scale`은 "박스의 수평 너비가 어떻게 줄어들지"를 제어하는 옵션으로, "exponential"이나 "linear"와 같은 선택지가 있다고 언급하며 직접 코드를 통해 이 옵션들을 바꿔가며 시각화의 변화를 탐색해 볼 것을 권장했습니다.

**시험 포인트**:
-   ⭐ `boxenplot`의 `k_depth` 옵션은 letter-value 레벨의 수를 조절하여 데이터 꼬리 부분의 상세함을 제어합니다.
-   ⭐ `scale` 옵션은 `boxenplot`의 중첩된 박스들의 수평 너비 감소 방식을 결정합니다. ("exponential", "linear" 등)
-   ⭐ `boxenplot`은 특히 `N` (샘플 크기)이 큰 데이터셋에서 꼬리 부분의 분포를 훨씬 더 안정적으로 볼 수 있다는 장점이 있습니다.

---

## Slide 25

## Boxen Plot — Seaborn Code (Updated API)

### 핵심 개념
**Boxen plot** (혹은 **Letter value plot**)은 특히 대규모 데이터셋($N$)에서 데이터 분포의 꼬리 부분을 더 자세하고 신뢰성 있게 시각화하기 위해 고안된 플롯입니다. 중앙값(median)에서 시작하여 점진적으로 더 깊은 대칭적인 사분위수 쌍을 추가하며, 각 쌍은 나머지 꼬리 부분의 질량(mass)을 절반으로 줄여 나가는 방식으로 중첩된 박스들을 표시합니다. 표준 Box plot이 중앙값과 사분위수 범위(IQR)를 주로 보여주는 반면, Boxen plot은 꼬리 부분의 미묘한 구조까지 탐색할 수 있게 해줍니다.

### 코드 해설

`seaborn` 라이브러리의 `sns.boxenplot()` 함수를 사용하여 Boxen plot을 생성합니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd # 예시를 위한 pandas 임포트

# 예시 데이터 로드 (강의 내용에 따라 wine 데이터셋 사용 가정)
from sklearn.datasets import load_wine
wine_data = load_wine(as_frame=True)
df_wine = wine_data.frame
df_wine['class'] = df_wine['target'].map({0: 'A', 1: 'B', 2: 'C'})
```

**1. 단일 분포 요약 (Single distribution summary)**
데이터셋의 단일 변수에 대한 Boxen plot을 그립니다.

```python
ax = sns.boxenplot(
    data=df_wine,
    x="flavanoids",
    k_depth="tukey", # ⭐ k_depth: 박스의 깊이 조절. 'tukey'는 자동 깊이 설정 (기본값)
    width_method="exponential", # ⭐ width_method: 박스의 수평 너비가 줄어드는 방식 ('exponential', 'linear' 등)
    outlier_prop=0.007, # 이상치로 간주될 데이터의 비율
    showfliers=True, # 이상치 점들을 표시할지 여부
    linewidth=1.2
)
ax.set_xlabel("flavanoids")
ax.set_title("Boxen (letter-value) summary")
plt.show()
```

**2. 그룹 비교 (Group comparison with hue)**
`hue` 파라미터를 사용하여 여러 그룹 간의 분포를 비교합니다. `x`와 `y`를 함께 사용하여 가로 박스 플롯을 생성할 수 있습니다.

```python
ax = sns.boxenplot(
    data=df_wine,
    x="class",
    y="flavanoids",
    hue="class", # hue: 그룹 비교를 위한 변수
    dodge=True, # 그룹별 박스를 분리하여 표시 (x, y, hue 사용 시)
    width=0.8,
    k_depth="trustworthy", # ⭐ k_depth: 샘플 크기가 허용하는 만큼만 깊이를 조절하여 신뢰성을 확보
    width_method="linear", # width_method: 선형적으로 너비 감소
    outlier_prop=0.01,
    showfliers=True,
    linewidth=1.1
)
ax.set_xlabel("class")
ax.set_ylabel("flavanoids")
ax.set_title("Boxen by class (deeper tail summaries)")
plt.show()
```

**3. 고정 깊이 (Fixed depth - instructional)**
`k_depth`를 정수 값으로 직접 지정하여 박스의 깊이를 고정합니다.

```python
ax = sns.boxenplot(
    data=df_wine,
    x="flavanoids",
    k_depth=3, # k_depth=3: 3단계의 중첩된 박스 표시 (예: 25-75%, 12.5-87.5%, 6.25-93.75%)
    showfliers=False # 이상치 점 표시 안함
)
ax.set_title("Fixed depth (k_depth=3) instructional view")
plt.show()
```

### 강의 맥락
교수님은 `boxenplot`을 "letter value plot"이라고도 부르며, **대규모 데이터셋($N$)에 적합하다**고 강조하셨습니다. 이는 표준 `boxplot`이나 `violinplot`보다 데이터의 꼬리 부분을 **"훨씬 더 신뢰성 있게 볼 수 있는"** 장점이 있다고 설명합니다. 박스의 깊이를 조절하는 `k_depth` 파라미터는 기본적으로 `tukey` (자동) 옵션을 사용하지만, `trustworthy` 옵션을 통해 샘플 크기에 따라 신뢰할 수 있는 깊이까지만 그리도록 할 수 있다고 언급하셨습니다. 또한, 박스의 너비가 줄어드는 방식을 제어하는 `width_method` 파라미터(`'exponential'` 또는 `'linear'`)가 기존의 `scale` 파라미터를 대체한다고 설명하며, 이러한 옵션들을 직접 변경하며 데이터에 최적화된 시각화를 찾아볼 것을 권장하셨습니다.

### 시험 포인트
*   **Boxen plot의 주된 사용 목적**: ⭐ 대규모 데이터셋에서 데이터 분포의 **꼬리 부분(tails)을 더 자세하고 신뢰성 있게 시각화**하는 데 유용합니다.
*   **Boxen plot과 Box plot의 차이**: Box plot이 중앙값과 사분위수(IQR) 요약에 중점을 둔다면, Boxen plot은 중첩된 박스를 통해 ⭐**더 깊은 사분위수를 보여주어 꼬리 부분의 상세 정보**를 드러냅니다.
*   **주요 파라미터**: `k_depth` (박스 깊이), `width_method` (박스 너비 감소 방식)의 역할과 ⭐`'tukey'` (기본 자동), `'trustworthy'` (샘플 크기에 따른 신뢰성 있는 깊이) 옵션의 의미를 이해해야 합니다.

---

## Slide 26

### **When to Use Which?**

**핵심 개념**: Box plot, Violin plot, Boxen plot의 주된 차이점은 KDE (Kernel Density Estimate) 사용 여부이며, 데이터의 크기($n$)와 강조하려는 특징(분포의 모양 또는 통계적 요약)에 따라 적절한 시각화 도구를 선택해야 합니다.

**강의 맥락**:
교수님께서는 Box plot, Violin plot, Boxen plot의 차이점과 각 플롯을 언제 사용해야 하는지에 대해 설명하셨습니다.

"The biggest difference between boxplot and violinplot is the use of KDE. Okay. Violin emphasizes shape via KDE. Box emphasizes robust summaries."
"If you have a small sample size less than 50, you can use box plot. And overlay row points using 3 plot. Okay, strip plot. So box plot plus strip plot to plot row points. Okay. And the violin plot with so little data can be very misleading. Okay."
"If shape matters, use violin flag. Just remember tune the vm-adjust and set cut being equal to zero to stop the KDE from drawing the tail beyond the data range. So you can use this cut b=0 option."
"And if you have a large sample size, consider 박승plot. To get a much more reliable look at the tails."
"And for fair comparison, keep your axis consistent. Okay, that's it."

**시험 포인트**:
*   ⭐ **Box plot**은 `robust summaries`(중앙값, 사분위수 등)를 강조하며, 특히 `small sample size`($n < 50$)일 때 `stripplot` 또는 `swarmplot`과 함께 사용하면 KDE의 잘못된 'bump' 해석을 피할 수 있습니다.
*   ⭐ **Violin plot**은 `shape`(분포의 모양)를 강조하며 `KDE`를 통해 다봉성(multi-modality), 비대칭성, 꼬리 부분을 보여줍니다. 사용 시 `bw_adjust`를 조정하고 `cut=0`으로 설정하여 데이터 범위를 넘어선 꼬리 그리는 것을 방지해야 합니다.
*   ⭐ **Boxen plot**(`letter value plot`)은 `large sample size`($n$)에 적합하며, 더 깊은 사분위수(`deeper quantiles`)를 제공하여 꼬리(`tails`) 부분을 더 신뢰성 있게 비교할 수 있게 해줍니다.
*   ⭐ 플롯 간 `fair comparison`을 위해서는 항상 `consistent axes`를 사용하고, 옆으로 나란히 비교할 때 해석을 왜곡할 수 있는 `mixing scale modes`를 피해야 합니다.

---

## Slide 27

**핵심 개념**:
Box, Violin, Boxen 플롯은 단변량 데이터의 분포를 요약하고 여러 그룹을 비교하는 데 사용되는 시각화 도구입니다. 이들은 데이터의 중심, 분산, 이상치, 그리고 분포 형태를 각기 다른 방식으로 강조합니다.
- `Box plot`: 중앙값($$Q_2$$), 사분위수($$Q_1$$, $$Q_3$$), 이상치 등 강건한 통계적 요약을 빠르게 제공합니다.
- `Violin plot`: Box plot에 KDE(Kernel Density Estimate)를 더하여 분포의 다봉성(multi-modality), 비대칭성(skewness), 꼬리(tails) 부분을 시각적으로 보여줍니다.
- `Boxen plot` (Letter-Value plot): `n`이 큰 데이터셋을 위해 설계되었으며, 더 깊은 사분위수를 계층적으로 표시하여 꼬리 부분을 더 자세히 시각화하는 데 유용합니다.

**코드/수식 해설**:
```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1행 3열의 서브플롯을 생성하며, 전체 그림의 크기를 (12, 3)으로 설정합니다.
fig, axes = plt.subplots(1, 3, figsize=(12, 3))

# 첫 번째 서브플롯에 Box plot을 그립니다.
# x축은 'class' (그룹), y축은 'alcohol' (측정값) 데이터를 사용합니다.
sns.boxplot(data=wine, x="class", y="alcohol", ax=axes[0])
axes[0].set_title("Box")

# 두 번째 서브플롯에 Violin plot을 그립니다.
# inner="quartile": 바이올린 내부에 사분위수를 표시합니다.
# cut=0: KDE가 데이터 범위 밖으로 밀도를 그리는 것을 방지합니다.
sns.violinplot(data=wine, x="class", y="alcohol", inner="quartile", cut=0, ax=axes[1])
axes[1].set_title("Violin")

# 세 번째 서브플롯에 Boxen plot을 그립니다.
sns.boxenplot(data=wine, x="class", y="alcohol", ax=axes[2])
axes[2].set_title("Boxen")

# 서브플롯 간의 간격을 자동으로 조정하여 겹치지 않도록 합니다.
plt.tight_layout()
```
- `plt.subplots(1, 3, figsize=(12, 3))`: `matplotlib`을 사용하여 가로로 3개의 플롯을 배치할 `Figure`와 `Axes` 객체를 생성합니다.
- `sns.boxplot(...)`, `sns.violinplot(...)`, `sns.boxenplot(...)`: `seaborn` 라이브러리의 함수를 이용해 각 `Axes`에 지정된 플롯을 그립니다.
    - `data=wine`: `wine` 데이터셋을 사용합니다.
    - `x="class"`, `y="alcohol"`: `class` 열을 그룹(범주형)으로, `alcohol` 열을 측정값(수치형)으로 지정합니다.
    - `ax=axes[idx]`: 각 플롯이 그려질 서브플롯을 지정합니다.
    - `inner="quartile"` (Violin plot): 바이올린 플롯 내부에 사분위수 선을 표시하여 Box plot의 요약 정보를 추가합니다.
    - `cut=0` (Violin plot): KDE가 데이터의 실제 최솟값/최댓값 범위 밖으로 밀도 추정치를 그리지 않도록 제한합니다.

**구체적 예시**:
(코드 블록에 제시된 `wine` 데이터셋의 `class`별 `alcohol` 분포를 Box, Violin, Boxen 플롯으로 비교하는 예시로 충분합니다.)

**강의 맥락**:
교수님께서는 이 코드를 통해 Box, Violin, Boxen 플롯을 나란히 비교하여 "데이터의 스토리를 가장 잘 전달하는 플롯이 무엇인지 탐색"하는 방법을 제시했습니다.
- `Box plot`은 "robust summaries(강건한 요약)"를 강조합니다.
- `Violin plot`은 "shape via KDE(KDE를 통한 형태)"를 강조합니다.
- ⭐**샘플 사이즈(`n`)에 따른 적절한 플롯 선택**:
    - **샘플 사이즈가 작은 경우(`n` < 50)**: `Box plot`이 적합하며, 원본 데이터 포인트의 시각화를 위해 `strip plot`과 함께 사용하는 것을 권장했습니다. 데이터가 너무 적을 경우 `Violin plot`은 오해의 소지가 있을 수 있다고 설명했습니다.
    - **분포 형태가 중요한 경우**: `Violin plot`이 유용하며, 이때 KDE의 `bandwidth`를 조정하고 `cut=0` 옵션을 사용하여 KDE가 데이터 범위 밖으로 밀도를 그리지 않도록 하는 것이 중요하다고 강조했습니다.
    - **샘플 사이즈가 큰 경우**: `Boxen plot`을 사용하여 꼬리 부분(`tails`)을 더 신뢰성 있게 시각화할 수 있다고 언급했습니다.
- 공정한 비교를 위해 모든 플롯에서 축(`axis`)을 일관되게 유지하는 것이 중요합니다.

**시험 포인트**:
- ⭐ Box, Violin, Boxen 플롯 각각의 주요 기능과 시각화 목적을 이해해야 합니다. (Box: 강건한 요약, Violin: KDE 기반 분포 형태, Boxen: 큰 데이터셋의 꼬리 상세 시각화)
- ⭐ 데이터 샘플 크기(`n`)에 따라 가장 적절한 플롯을 선택하는 기준을 알아야 합니다. (작은 `n` -> Box + Strip, 큰 `n` -> Boxen)
- ⭐ `Violin plot`에서 `cut=0` 파라미터가 어떤 역할을 하는지 설명할 수 있어야 합니다.

---

## Slide 28

---
### **Pitfalls & Best Practices**

**핵심 개념**:
데이터 시각화에서 흔히 발생하는 문제점들을 피하고, 더 효과적인 시각화를 위한 모범 사례들을 다룹니다.

*   **Overplotting (겹쳐 그리기)**:
    *   데이터 포인트가 너무 많거나 좁은 공간에 집중되어 서로 겹쳐 보일 때 발생합니다.
    *   해결책으로 `stripplot`을 사용해 `jitter` (데이터 포인트에 약간의 무작위 노이즈를 주어 겹침 방지)를 추가하거나, 겹침을 자동으로 피하는 `swarmplot`을 사용할 수 있습니다.
    *   또한, `alpha` 값을 낮춰 투명도를 높이는 방법도 있습니다.
*   **Bandwidth sensitivity (Violin 플롯)**:
    *   `Violin plot`은 KDE(Kernel Density Estimate)를 기반으로 하므로, KDE의 `bandwidth` (대역폭) 선택에 민감합니다.
    *   `bw_adjust` 파라미터를 조정하고, `cut=0`으로 설정하여 데이터 범위 밖으로 밀도 추정치가 그려지는 것을 방지해야 합니다. ⭐
*   **Outliers (Box 플롯)**:
    *   `Box plot`에서 이상치(outlier)와 수염(whisker)의 정의를 명확히 이해하고 의도적으로 설정해야 합니다.
    *   `whis` (수염 길이) 및 `showfliers` (이상치 표시 여부) 파라미터를 신중하게 선택하고, 사용한 규칙을 문서화하는 것이 중요합니다.
*   **Scaling (스케일링)**:
    *   여러 패널(서브플롯)에 걸쳐 데이터를 비교할 때는 항상 축의 범위를 일관되게 유지해야 합니다.
    *   `Violin plot`에서 다양한 스케일 모드를 혼합하지 않도록 주의합니다.
*   **Explain the summary (요약 설명)**:
    *   시청자가 `Box plot`과 같은 요약 플롯의 의미를 정확히 이해하고 있다고 가정하지 말아야 합니다.
    *   중앙값(median), 사분위수(quartiles), 수염(whiskers), 이상치(outliers)가 무엇을 나타내는지 명확하게 설명하여 오해를 방지해야 합니다.

**강의 맥락**:
교수님께서는 이 슬라이드를 "Here are some common pitfalls and best practices for this family overplotting."이라는 말로 시작하시며, 앞에서 다룬 시각화 도구들의 주의사항을 설명하셨습니다.

*   **Overplotting**: "So if you add row points and have a lot of data, it can become a mess, right? So you should add a jitter using a strip plot. Okay? ... Or better, you can use a swarm plot, which avoids overlap. ... And also you can use the transparency by setting alpha." (데이터가 많아 겹칠 때 `stripplot`의 `jitter`나 `swarmplot`, `alpha`를 통한 투명도 조절로 해결할 수 있음을 강조)
*   **Bandwidth sensitivity (Violin)**: "So violin plots, as we said, tune the beat double adjust and set cut to zero. That's what we already explained." (KDE의 `bandwidth`에 민감하므로 `bw_adjust`를 조정하고, `cut=0`을 통해 불필요한 꼬리 생성을 막으라고 재차 강조) ⭐
*   **Outliers (Box)**: "So, in the outlier for box plot, right, so be deliberate about your whisker and show flyers. This is setting. And always document the rule you have used. I strongly recommend you to try with these show flyers." (`whis`, `showfliers` 설정을 신중하게 하고 사용 규칙을 문서화할 것을 권장)
*   **Scaling**: "And for fair comparison, keep your axis consistent." (공정한 비교를 위해 축을 일관되게 유지하는 것이 중요함을 언급)
*   **Explain the summary**: "Don't assume your audience knows what a Voxpla shows. So you label the median, quantile, with curves and so on. Okay." (청중이 `Box plot`의 의미를 안다고 가정하지 말고, 중앙값, 사분위수 등 구성 요소를 명확히 설명할 것을 지시) ⭐

**시험 포인트**:
*   `Overplotting`을 피하기 위한 방법 (jitter, `swarmplot`, `alpha`)을 아는 것이 중요합니다.
*   `Violin plot`에서 `bandwidth` 민감성 문제를 해결하기 위한 파라미터(`bw_adjust`, `cut=0`)를 ⭐반드시 기억해야 합니다.
*   `Box plot`의 이상치(`outlier`) 및 수염(`whisker`) 설정 시의 주의사항과 요약 플롯의 구성 요소를 설명하는 중요성을 이해해야 합니다. ⭐
---

---

## Slide 29

**핵심 개념**

*   **Rug Plot**: 데이터의 `atoms` (개별 관측치)를 보여주는 플롯으로, 각 관측치마다 축 위에 작은 틱(tick)을 표시합니다.
*   **Strip Plot**: 1차원 산점도로, 각 관측치를 점으로 표시합니다. 점들이 겹치는 것을 피하기 위해 작은 양의 무작위 `jitter`(미세한 흔들림)를 추가합니다.

**강의 맥락**

교수님께서는 이 슬라이드에서 `rug plot`과 `strip plot`을 설명하시며, 이들이 데이터의 `atoms`를 보여주는 역할을 한다고 강조하셨습니다.

*   "log plot은 단지 작은 틱들의 집합이다. 축을 따라 각 관측치마다 하나의 틱이 있다."
*   "strip plot은 1D 산점도이다. 점을 찍는 산점도이지만, 약간의 무작위 jitter를 사용하여 겹침을 피한다."

**Motivation (동기)**

히스토그램, KDE, 박스 플롯, 바이올린 플롯과 같은 **집계(aggregates) 플롯들은 데이터의 미세 구조(microstructure)를 숨깁니다.** `rug` 또는 `strip plot`으로 원본 데이터 포인트를 오버레이하면 다음과 같은 이점이 있습니다.

*   **Sanity Checks (정합성 검증)**: ⭐ KDE나 박스/바이올린 플롯이 실제 관측치의 위치를 제대로 반영하는지 확인할 수 있는 중요한 `sanity check` 도구입니다.
    *   교수님 강조: "low points를 rug나 strip으로 오버레이하는 것은 매우 중요한 sanity check이다. 왜냐하면 거기에 점들이 있다는 것을 볼 수 있기 때문이다."
*   **Small to Medium $N$ (작은-중간 크기의 샘플)**: 데이터의 뭉침(clumps), 간격(gaps), 그리고 이상치(outliers)를 빠르게 파악할 수 있습니다.
*   **Ties/Discreteness (동일 값/이산성)**: `jitter`를 통해 일반 산점도에서는 겹쳐 보여서 알 수 없는 쌓이거나 동일한 값들을 명확히 드러낼 수 있습니다.

**Interpretation (해석)**

*   **Density vs. Atoms**: `rug/strip plot`은 데이터 포인트가 **실제로 어디에 있는지** (atoms) 보여주는 반면, KDE나 바이올린 플롯은 **부드러운 경향(smoothed tendency)**을 보여줍니다.
*   **Jitter is Visual Only (Jitter는 시각적인 효과일 뿐)**: ⭐ `strip plot`의 `jitter`는 겹침을 해소하기 위한 **시각적인 추가(visual only add)**이며, **기저 데이터(underlying data)를 변경하지 않습니다.** `jitter`가 적용된 위치로부터 값을 정량화해서는 안 됩니다.
    *   교수님 강조: "strip plot의 jitter는 단지 시각적인 추가일 뿐이다. 데이터는 변경하지 않는다."
*   **제한 사항**: ⭐ 데이터가 **매우 많은 경우(very large data)**, `strip plot`은 많은 점들이 겹쳐서 오히려 쓸모없는 플롯이 될 수 있으므로, 이러한 경우에는 사용을 피해야 합니다.
    *   교수님 강조: "만약 매우 많은 데이터가 있다면, strip plot은 쓸모없는 플롯이 될 수 있다. 그래서 매우 많은 데이터가 있다면 이 strip plot을 피해야 한다."

---

## Slide 30

**핵심 개념**:
이 슬라이드는 Rug plot과 Strip plot을 효과적으로 시각화하기 위한 디자인 선택 사항들을 다룹니다. 이 플롯들은 데이터의 개별 '원자(atoms)'를 보여줌으로써, 히스토그램이나 KDE와 같은 집계 플롯이 숨길 수 있는 미세 구조를 드러내고 데이터의 건전성(sanity check)을 확인하는 데 중요합니다.

**강의 맥락**:
교수님께서는 Rug plot과 Strip plot의 기본 개념을 설명한 후, 해당 슬라이드에 대해서는 "Okay, so I think you just carefully read all description here. Okay, so it's not that big deal."라고 언급하며 학생들이 스스로 디자인 선택 사항들을 읽고 이해하기를 권장하셨습니다. 따라서 이 노트는 슬라이드의 내용을 간결하게 요약합니다.

*   **Rug Plot 디자인 선택**:
    *   `height` (축 비율): 눈금(ticks)이 데이터를 지배하지 않도록 짧게 (약 $0.02-0.05$) 설정합니다.
    *   `lw/alpha`: 데이터 포인트 수($n$)가 많을 때 어두운 띠가 생기는 것을 피하기 위해 얇고 반투명하게 설정합니다.
    *   `Orientation`: `x=`를 통해 가로 방향으로, `y=`를 통해 세로 방향으로 설정할 수 있습니다.

*   **Strip Plot 디자인 선택**:
    *   `jitter` (float 또는 `True`): 데이터 포인트들의 겹침(overlap)을 해소할 수 있을 정도로만 추가합니다. 너무 과하면 노이즈처럼 보일 수 있습니다.
    *   `alpha`, `size`: $n$이 증가함에 따라 `alpha` 값을 낮추고 마커 크기를 작게 합니다.
    *   `dodge with hue`: 더 공정한 겹침 방지를 위해 각 $x$ 레벨 내에서 범주(`hue`)를 분리하여 표시합니다.

*   **$n$이 큰 경우의 고려 사항**:
    *   데이터 포인트 수($n$)가 매우 클 경우 Downsample(표본 추출)하거나, 얇고 투명한 Rug plot을 사용하거나, 중간 규모의 $n$에서는 자동 비겹침(non-overlap) 기능을 제공하는 `swarmplot`으로 전환하는 것을 고려합니다.
    *   ⭐ 집계 플롯(히스토그램, KDE, ECDF)과 함께 사용하여 데이터의 '원자(atoms)' 정보를 보조적으로 미묘하게 보여주는 것이 좋습니다. (`strip plot`은 데이터가 매우 많을 경우 유용성이 떨어질 수 있습니다.)

**시험 포인트**:
*   ⭐ Rug plot과 Strip plot이 히스토그램, KDE, Box plot과 같은 집계 플롯이 숨기는 데이터의 `microstructure`를 보여주고 `sanity check` 역할을 한다는 점을 이해해야 합니다.
*   ⭐ Strip plot에서 데이터 겹침을 방지하기 위해 `jitter`를 사용하는 이유를 알아야 합니다.
*   ⭐ $n$이 큰 경우 `strip plot`의 한계와 대안 (예: `swarmplot` 또는 집계 플롯과 함께 사용)에 대해 인지해야 합니다.

---

## Slide 31

### 핵심 개념
`rug plot`과 `strip plot`은 데이터의 **개별 관측치(atoms)**를 시각화하여 밀도 추정이나 요약 통계량으로 가려질 수 있는 데이터의 **미세 구조(microstructure)**를 드러내기 위한 플롯입니다.
*   **Rug Plot**: X축을 따라 각 데이터 포인트에 작은 눈금(`tick`)을 표시하여 데이터의 밀집도를 시각적으로 보여줍니다. 주로 KDE 플롯과 함께 오버레이되어 KDE 곡선 아래에 실제로 데이터 포인트가 존재하는지 확인하는 "sanity check" 용도로 사용됩니다.
*   **Strip Plot**: 1차원 산점도로, 범주형 변수에 따라 개별 데이터 포인트를 표시합니다. 겹침을 방지하기 위해 `jitter`를 추가하여 포인트를 미세하게 분산시킬 수 있습니다.

### 코드/수식 해설

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Rug + KDE (Diabetes: bmi)
fig, ax = plt.subplots()
sns.kdeplot(data=diabetes, x="bmi", ax=ax, bw_adjust=1.0) # BMI 데이터의 KDE 플롯 생성
sns.rugplot(data=diabetes, x="bmi", ax=ax, height=0.03, lw=0.6, alpha=0.5) # 동일한 BMI 데이터에 러그 플롯 오버레이
ax.set_title("KDE + Rug (bmi)"); ax.set_ylabel("density")

# 2) Strip by group (Iris species vs sepal length)
fig, ax = plt.subplots()
sns.stripplot(
    data=iris, x="species", y="sepal length (cm)",
    jitter=0.25, alpha=0.6, size=3, ax=ax
) # Iris 데이터셋의 종(species)별 꽃받침 길이(sepal length)를 스트립 플롯으로 시각화
ax.set_title("Strip: species vs sepal length (cm)")
```
*   `sns.kdeplot()`: Kernel Density Estimate를 그립니다. `bw_adjust`는 대역폭(`bandwidth`)을 조절하여 KDE 곡선의 부드러움을 제어합니다.
*   `sns.rugplot()`: 지정된 `x`축 변수에 해당하는 각 데이터 포인트 위치에 작은 눈금을 그립니다. `height`는 눈금의 높이, `lw`는 선의 두께, `alpha`는 투명도를 설정합니다.
*   `sns.stripplot()`: 범주형 변수(`x`)와 연속형 변수(`y`)에 대한 1차원 산점도를 그립니다.
*   `jitter`: 이 파라미터는 겹치는 데이터 포인트들을 시각적으로 분산시켜 개별 관측치를 더 잘 보이도록 무작위 노이즈를 추가합니다. `jitter=True` 또는 특정 값을 지정할 수 있으며, 실제 데이터 값은 변경하지 않고 **시각적인 목적**으로만 사용됩니다.
*   `alpha`: 포인트의 투명도를 설정합니다.
*   `size`: 포인트의 크기를 설정합니다.

### 구체적 예시
1.  **KDE + Rug (bmi)**: 당뇨병 데이터셋의 BMI 분포를 KDE로 부드럽게 보여주면서, X축 아래에 `rug plot`을 추가하여 각 BMI 값에 해당하는 개별 환자들의 실제 데이터 포인트 위치를 명확히 나타냅니다. 이를 통해 KDE 곡선의 봉우리(peak)가 실제 데이터가 밀집된 곳에 의해 형성되었는지 확인할 수 있습니다.
2.  **Strip: species vs sepal length (cm)**: Iris 데이터셋에서 세 가지 종(`setosa`, `versicolor`, `virginica`) 각각의 꽃받침 길이(`sepal length`)를 개별 점으로 보여줍니다. `jitter`를 적용하여 같은 꽃받침 길이를 가진 꽃들이 겹쳐 보이지 않고 옆으로 퍼져 시각적으로 구분될 수 있도록 합니다.

### 강의 맥락
교수님께서는 `rug plot`과 `strip plot`을 "데이터의 원자(atoms)"를 보여주는 플롯이라고 설명하시며, 집계된 플롯(히스토그램, KDE, 박스플롯)이 숨기는 "기저의 미세 구조"를 드러내는 것이 이 플롯들의 핵심 목적이라고 강조하셨습니다. 특히, 이 플롯들을 다른 요약 플롯과 함께 오버레이하는 것이 중요한 **"sanity check"** 역할을 한다고 말씀하셨습니다. 예를 들어, KDE 곡선의 특정 봉우리 아래에 실제로 데이터 포인트가 존재하는지, 데이터에 덩어리(clumps)나 공백(gaps), 이상치(outliers)가 있는지 빠르게 확인할 수 있다고 설명하셨습니다. 또한, `strip plot`에서 `jitter`를 사용하는 이유가 "겹침을 피하기 위함"이며, 이는 데이터 자체를 변경하는 것이 아닌 "시각적인 추가"일 뿐임을 강조하셨습니다. 마지막으로, 데이터가 매우 많을 경우 `strip plot`은 여전히 오버플로팅되어 "쓸모없는 플롯"이 될 수 있으므로 주의해야 한다고 언급하셨습니다.

### 시험 포인트
*   ⭐ `rug plot`과 `strip plot`의 주요 목적은 무엇이며, 어떤 상황에서 유용하게 사용되는가? (KDE/박스플롯의 보완, 데이터의 미세 구조 확인, sanity check)
*   ⭐ `strip plot`에서 `jitter` 파라미터의 역할은 무엇이며, 왜 사용해야 하는가? (겹침 방지, 실제 데이터 불변)
*   `rug plot`과 `strip plot`이 `KDE`, `boxplot` 등과 같은 집계 플롯과 어떻게 다른 정보를 제공하는가?
*   `strip plot` 사용 시 주의할 점은? (데이터 양이 매우 많을 경우의 한계)

---

## Slide 32

## Q-Q Plot — Normality & Tails

### 핵심 개념
Q-Q (Quantile-Quantile) 플롯은 데이터의 분포가 특정 이론적 분포(주로 정규 분포)를 따르는지 확인하고, 분포의 꼬리(tails) 특성을 진단하는 데 사용되는 주요 도구입니다.

### 코드/수식 해설
Q-Q 플롯은 데이터의 순서 통계량(order statistics) $x_{(i)}$와 그에 해당하는 확률 $p_i$를 사용하여 데이터를 이론적 분포의 분위수(quantile)와 비교합니다.

*   **확률 $p_i$ 계산**:
    $$p_i = \frac{i - 0.5}{n}$$
    여기서 $i$는 $1$부터 $n$까지의 순서 통계량 인덱스이고, $n$은 전체 데이터 포인트 수입니다.
*   **플로팅**: Q-Q 플롯은 각 데이터 포인트에 대해 다음 쌍을 플로팅합니다:
    $$(F^{-1}(p_i), x_{(i)}), \quad i = 1, \dots, n$$
    여기서 $F^{-1}(p_i)$는 참조 분포(reference distribution) $F$의 이론적 분위수(theoretical quantile)이고, $x_{(i)}$는 데이터의 실제 샘플 분위수(sample quantile)입니다. $F^{-1}(p_i)$가 x축에, $x_{(i)}$가 y축에 플롯됩니다.

### 강의 맥락
"Our final plot is QQ plot. Quantile and quantile plot. Let me write that. This is a primary tool for checking normality and the diagonalizing tails. So let's look at the definition. QQ plot. plus the quantile of your data that is very important against theoretical quantile of reference distribution like a normal distribution so this is a normal distribution reference distribution. And this is your data. Okay. And the QQ plots quantile of your data against this reference distribution. And the formula shows that for each data point i, we calculate its plotting position pi. and find the theoretical quantile, F inverse of P_i. Okay, this is a theoretical quantile, when we write down. Because this is the inverse, right? Theoretical quantile. So we plot this on the x-axis, theoretical quantiles. On the y-axis, we plot the actual data point, x_i, sample quantile. Okay? So if data perfectly follows the reference distribution, all data points will lie on the straight line. Right? So that's why this is very useful for checking normality. Which means that if your distribution is normal distribution, why not?"

### 시험 포인트
*   **Q-Q 플롯의 목적**: ⭐데이터가 특정 이론적 분포(특히 정규 분포)를 따르는지 확인하고, 분포의 꼬리(tails) 특성 및 이상치를 진단하는 데 사용됩니다.
*   **직선 해석**: ⭐만약 데이터가 참조 분포를 완벽하게 따른다면, 플롯의 모든 점들은 직선 위에 놓이게 됩니다.
*   **곡선 해석**: 곡선 형태는 분포의 왜도(skew)를, 꼬리 부분의 발산(divergence)은 heavy/light tails를 나타냅니다.
*   **표준화의 중요성**: Q-Q 플롯을 그리기 전에 데이터를 표준화하면 참조선이 `y = x` 직선이 되어 해석이 더 용이합니다.

---

## Slide 33

### 핵심 개념
*   **Q-Q 플롯 변형 (Variants)**: Q-Q 플롯은 정규 분포 외에 다른 이론적 분포(예: t-분포, 지수 분포, 카이제곱 분포)를 참조 분포로 사용하여 데이터가 해당 분포를 따르는지 확인할 수 있습니다. 또한, 통계 모델의 `잔차(residuals)`에 적용하여 모델의 분포 가정을 검토하는 데 활용될 수 있습니다.
*   **Q-Q 플롯 모범 사례 (Good Practices)**:
    *   정규 Q-Q 플롯을 그리기 전에는 데이터를 **표준화**하는 것이 좋습니다.
    *   표본 크기가 `$n$`이 작은 경우, 데이터가 이론 분포에서 약간 벗어나는 것은 흔한 일이므로, 표본 크기를 명시하고 필요하다면 신뢰구간(bands)을 고려해야 합니다.
    *   견고성(robustness)이 중요한 경우, `$median/MAD$`(중앙값/중앙값 절대 편차)로 표준화된 값들을 함께 살펴보는 것이 좋습니다.

### 구체적 예시
*   **표준화의 이점**: 데이터를 표준화하면 정규 Q-Q 플롯의 참조선이 단순한 `$y=x$` 형태로 나타나 기울기나 절편의 해석이 더 직관적이고 쉬워집니다.

### 강의 맥락
교수님은 QQ 플롯을 "정규성을 확인하고 꼬리를 진단하는 주요 도구"라고 강조하며, 특히 "정규 Q-Q 플롯을 만들기 전에 데이터를 먼저 **표준화**해야 한다"고 설명했습니다. 표준화를 통해 "참조선이 단순한 `$y=x$` 선이 되어 해석하기 더 쉬워진다"고 덧붙였습니다. 이는 슬라이드의 "Standardize before Normal Q-Q so slope/intercept are interpretable" 항목과 직접적으로 연결됩니다.

### 시험 포인트
*   ⭐ 정규 Q-Q 플롯을 사용하기 전에 데이터를 **표준화**하는 이유와 그 이점 (참조선 `$y=x$`의 해석 용이성).
*   ⭐ Q-Q 플롯이 `모델 잔차(model residuals)`의 분포 가정을 확인하는 데 사용될 수 있다는 점.

---

## Slide 34

### Q-Q (Wine: z-scored alcohol vs Normal) — Code

**핵심 개념**:
이 슬라이드는 와인 데이터셋의 `alcohol` 컬럼에 대한 Q-Q Plot을 생성하는 Python 코드를 보여줍니다. Q-Q Plot은 데이터의 분포가 특정 이론적 분포(여기서는 정규 분포)를 따르는지 시각적으로 확인하는 데 사용됩니다. 데이터를 표준화(z-scoring)한 후 정규 Q-Q Plot을 그리면, 데이터가 정규 분포를 따른다면 모든 점이 $y=x$ 직선 위에 놓이게 됩니다.

**코드 해설**:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
import scipy.stats as st

# 와인 데이터셋 로드 및 'alcohol' 컬럼 추출
wine = load_wine(as_frame=True)
x = wine.frame["alcohol"].to_numpy()

# 데이터 z-score 변환 (표준화)
# 평균을 0, 표준편차를 1로 맞춰줍니다.
x = (x - x.mean()) / x.std(ddof=0) # z-score

# 이론적(정규) 분위수와 샘플 분위수 계산
# st.probplot은 데이터 x와 비교할 이론적 분포('norm' = 정규분포)를 받아
# 이론적 분위수(osm)와 샘플 분위수(osr)를 반환합니다.
# fit=False는 적합 선을 그리지 않고, 점들만 계산하도록 합니다.
osm, osr = st.probplot(x, dist="norm", fit=False)

# Matplotlib을 사용하여 Q-Q Plot 생성
plt.figure()
# 이론적 분위수(osm)를 x축에, 샘플 분위수(osr)를 y축에 플로팅
plt.scatter(osm, osr, s=18, alpha=0.7)

# y=x 참조선 생성: 데이터가 정규 분포를 따를 경우 점들이 이 선 위에 위치합니다.
mn, mx = np.min(osm), np.max(osm)
plt.plot([mn, mx], [mn, mx], linestyle="--", linewidth=1.2)

# 축 레이블 및 제목 설정
plt.xlabel("Theoretical quantiles (Normal)")
plt.ylabel("Sample quantiles (z-scored)")
plt.title("Q-Q Plot: Wine alcohol vs Normal")
plt.tight_layout() # 레이아웃 조정
plt.savefig("qq_wine_alcohol.png", dpi=150) # 이미지 파일로 저장
```

**강의 맥락**:
교수님은 Q-Q Plot이 데이터의 정규성을 확인하고 꼬리 부분을 검사하는 데 가장 좋은 도구라고 강조하며, 특히 이 슬라이드의 코드를 통해 `scipy.stats.probplot` 함수 사용법을 설명했습니다.
*   "before you plan your data, you need to first standardize your data first. Okay? So before making a normal QQ plan. So this makes the reference line just a simple, $y = x$ line, which is easier to interpret." (Q-Q Plot을 그리기 전에 데이터를 먼저 표준화해야 하며, 이렇게 하면 참조선이 $y=x$ 선이 되어 해석이 더 쉬워진다는 점을 강조)
*   "So we first load our data, R code column from the wine data set, and then we compute the G square for data, and then we call this the prob plot, right? by setting `distance_norm` and this return a theoretical quantile. Okay, so this will return the theoretical quantile." (와인 데이터셋에서 `alcohol` 컬럼을 로드하고 `x`로 z-score 변환한 후, `st.probplot` 함수를 `dist="norm"`으로 호출하여 이론적 분위수와 샘플 분위수를 얻는 과정을 설명)
*   "And the rest of code is just standard metaflott library. Right? And we create a scatter plot of OSM versus OSR. We have OSM, OSR and we just plot these numbers. OSM, OSR. And then finally we plot the $y$ is equal to $x$ reference line. which draws a dashed line. Here." (이후의 코드는 표준 `matplotlib` 라이브러리를 사용하여 `osm`과 `osr`을 산점도로 그리고, $y=x$ 참조선을 점선으로 그리는 부분임을 설명)

**시험 포인트**:
*   ⭐ Q-Q Plot의 주요 목적은 무엇인가요? (데이터 분포의 정규성 검사 및 꼬리 부분 진단)
*   ⭐ 정규 Q-Q Plot을 그리기 전에 데이터를 **표준화(z-scoring)**해야 하는 이유는 무엇인가요? (참조선 $y=x$를 사용하여 해석을 용이하게 하기 위함)
*   ⭐ `scipy.stats.probplot` 함수가 반환하는 두 값(`osm`, `osr`)이 각각 무엇을 의미하며, Q-Q Plot의 x축과 y축에 무엇이 플로팅되는지 설명하세요. (일반적으로 `osm`은 이론적 분위수(x축), `osr`은 샘플 분위수(y축)를 나타냅니다.)
*   ⭐ Q-Q Plot에서 데이터가 정규 분포를 따를 때 점들이 어떻게 분포되어야 하는지 설명하세요. (점들이 $y=x$ 직선 위에 가깝게 놓여야 합니다.)

---

## Slide 35

**핵심 개념**:
Q-Q (Quantile-Quantile) Plot은 데이터의 분포가 특정 이론적 분포(주로 정규 분포)를 따르는지 시각적으로 확인하고, 특히 분포의 꼬리 부분을 진단하는 데 사용되는 주요 도구입니다.

**코드/수식 해설**:
Q-Q Plot은 데이터의 **샘플 분위수**($x_i$)를 **이론적 분포의 분위수**($F^{-1}(P_i)$)와 비교하여 플로팅합니다. 여기서 $P_i$는 $i$번째 데이터 포인트의 플로팅 위치(plotting position)를 나타냅니다.

*   `Theoretical quantiles (Normal)`: X축은 정규 분포와 같은 참조 분포에서 계산된 이론적 분위수를 나타냅니다.
*   `Sample quantiles (z-scored)`: Y축은 정규 분포와의 비교를 용이하게 하기 위해 Z-점수(표준화) 처리된 실제 데이터의 샘플 분위수를 나타냅니다.

데이터가 참조 분포(여기서는 정규 분포)를 완벽하게 따른다면, 모든 데이터 포인트는 기울기가 1인 직선 `y=x` 상에 놓이게 됩니다.

**구체적 예시**:
Wine 데이터셋의 `alcohol` 컬럼에 대한 Q-Q Plot은 다음과 같이 해석됩니다:
*   **중앙부(Central region)**: 대부분의 데이터 포인트가 대시선(참조선)과 거의 일치합니다. 이는 데이터의 중앙 부분이 정규 분포와 유사하다는 것을 나타냅니다.
*   **우측 꼬리(Right tail)**: 플롯의 우측 상단에서 데이터 포인트들이 참조선 위쪽으로 약간 벗어나 있습니다. 이는 데이터의 우측 꼬리가 참조 정규 분포보다 약간 더 무겁거나(heavy right tail) 몇몇 큰 이상치(large values)가 존재할 수 있음을 시사합니다.

**강의 맥락**:
교수님은 Q-Q Plot을 "정규성을 확인하고 꼬리를 진단하는 **주요 도구(primary tool)**"라고 강조했습니다. 데이터가 참조 분포를 완벽하게 따르면 모든 데이터 포인트가 **"직선 위에 놓일 것(lie on the straight line)"**이라고 설명하며, 이것이 정규성 검사에 매우 유용하다고 하셨습니다. 또한, QQ Plot을 만들기 전에 데이터를 **"먼저 표준화(standardize your data first)"**해야 `y=x` 참조선을 사용해 해석하기가 더 쉽다고 강조했습니다. 이 슬라이드에 표시된 와인 알코올 데이터 Q-Q Plot은 이러한 해석 원리를 실제 데이터에 적용한 결과입니다.

**시험 포인트**:
*   ⭐ Q-Q Plot의 **주요 목적**: 데이터의 정규성 검사 및 꼬리 부분 진단
*   ⭐ Q-Q Plot의 **해석 방법**: 데이터 포인트가 참조선(`y=x`)에 얼마나 가깝게 정렬되어 있는지로 정규성 판단.
    *   직선과 일치하면 정규 분포를 따름.
    *   꼬리 부분이 직선에서 벗어나면 해당 꼬리가 더 무겁거나 가볍다는 것을 의미 (예: 우측 꼬리가 위로 벗어나면 무거운 우측 꼬리).
*   ⭐ Q-Q Plot 생성 전 데이터 **표준화(standardization)**의 중요성: `y=x` 참조선을 통해 쉽게 해석할 수 있도록 함.

---

## Slide 36

---
**핵심 개념**:
이 슬라이드는 단일 변수 데이터 분석 및 시각화를 위한 전반적인 "읽기 전략"을 요약합니다. 다양한 시각화 도구를 어떤 순서와 목적에 맞게 활용해야 하는지 단계별 접근법을 제시합니다.

**강의 맥락**:
교수님은 강의의 결론 부분에서 "Okay, so to conclude, let's pull this all together into a reading strategy."라고 말씀하시며, 이 슬라이드를 통해 지금까지 배운 내용을 종합하는 전략을 제시했습니다.

1.  **히스토그램 (계수)으로 시작**:
    *   빠른 데이터 형태 파악을 위해 히스토그램을 (기본 `counts` 기준으로) 사용합니다.
    *   강의 맥락: "So you can first start with histogram or count for fast anchor on data shape."
    *   ⭐시험 포인트: 히스토그램은 데이터 형태를 빠르게 파악하는 데 가장 기본적인 도구입니다.

2.  **그룹 비교 또는 불균일한 $N$일 경우**:
    *   `probability` 또는 `density` 히스토그램을 사용하며, 반드시 `shared bins`를 적용해야 합니다.
    *   강의 맥락: "For group comparison or unequal n, you can switch to probability or density histogram and make sure that you used shared beans."
    *   ⭐시험 포인트: 그룹 비교 시에는 반드시 `shared bins`와 `density` 정규화를 사용해야 합니다.

3.  **ECDF 추가**:
    *   빈(bin)에 구애받지 않는 분위수(quantiles) 확인과 확률적 지배(stochastic dominance)를 확인하기 위해 `ECDF`를 추가합니다.
    *   강의 맥락: "and add an ECDF to get a bin-free loop at quantile and to check stochastic dominance."
    *   ⭐시험 포인트: `ECDF`는 `bin-free`하며, 분위수와 확률적 지배를 시각화하는 데 유용합니다.

4.  **KDE 추가 및 소규모 $N$일 때 `rug/strip` 플롯으로 건전성 확인**:
    *   부드러운 모드(modes)를 확인하기 위해 `KDE`를 추가합니다.
    *   데이터 포인트 수($N$)가 작을 때는 `rug` 또는 `strip` 플롯을 사용하여 실제 관측값을 확인하는 건전성 검사(sanity check)를 합니다.
    *   강의 맥락: "And add KDE to get a smooth mode. If the N is very small, send a check with a log or strip plot."
    *   ⭐시험 포인트: `KDE`는 데이터의 부드러운 형태를 파악하는 데 좋지만, $N$이 작을 때는 `rug/strip` 플롯으로 실제 데이터 분포를 확인하는 것이 중요합니다.

5.  **`Box/Boxen/Violin` 플롯 사용**:
    *   여러 그룹을 요약하고 비교하기 위해 `Box`, `Boxen`, `Violin` 플롯을 사용합니다.
    *   강의 맥락: "Use a box and box name violin to summarize and compare many groups at once."
    *   ⭐시험 포인트: 이 세 가지 플롯은 그룹 간의 분포를 요약하고 비교하는 데 사용되며, 각각의 특징(예: `KDE` 사용 여부, `N`에 따른 적합성)을 이해해야 합니다.

6.  **`Q-Q` 플롯으로 진단**:
    *   분포를 공식적으로 진단하고 특히 정규 분포와 비교하여 꼬리 부분을 확인하기 위해 `Q-Q` 플롯을 사용합니다.
    *   강의 맥락: "Finally, use QQ plot to formally diagnose the distribution and check its tail especially against the normal distribution."
    *   ⭐시험 포인트: `Q-Q` 플롯은 데이터 분포가 특정 이론적 분포(특히 정규 분포)를 따르는지 여부와 꼬리 부분을 진단하는 데 핵심적인 도구입니다.
---

---
