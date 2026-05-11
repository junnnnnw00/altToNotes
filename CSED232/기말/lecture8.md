# CSED232 - lecture8 상세 해설 노트 (음성 전사 포함)

> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다. Alt(altalt.io) 음성 전사 데이터를 함께 활용했습니다.

---

## Slide 1

**핵심 개념**:
이 슬라이드는 `CSED232 소프트웨어 작성 원리` 강의의 `Object-Oriented Contracts` (객체 지향 계약) 섹션의 제목이다. 이는 객체 지향 프로그래밍에서 클래스의 동작과 속성을 명세하고 구현하는 과정에서 지켜져야 할 "계약"의 개념을 다룬다.

**강의 맥락**:
강의는 중간고사 점수 공지 및 이의 제기 세션 안내 후, 곧바로 "객체(objects)"와 "객체 지향 예시(object-oriented example)"로 주의를 돌리며 시작된다. 교수님은 현대 소프트웨어 개발이 객체 지향 패러다임을 항상 포함하고 있으며, "스택 예시(stack example)"를 사용하여 객체 또는 클래스 명세(class specification)의 핵심 부분을 설명할 것이라고 언급한다. 이는 이 강의가 클래스 명세(class specification)와 관련된 여러 개념, 즉 추상 표현(abstract representation), 클래스 불변식(class invariant) 등을 다룰 것임을 예고한다.

**시험 포인트**:
⭐ 이 슬라이드 자체의 내용은 시험에 직접적으로 출제되기보다, 이어지는 강의 내용에서 다룰 **클래스 명세(class specification)**의 네 가지 구성 요소(메서드별 선행 조건/후행 조건, 클래스의 추상 표현/추상 값, 클래스 불변식) 및 **구현자 관점에서의 상세 내용**(구체적 표현, 추상화 함수, 표현 불변식)이 중요한 시험 포인트가 된다.

---

## Slide 2

---
### 핵심 개념

소프트웨어 개발에서 **명세(Specification)**는 우리가 무엇을 만들고자 하는지(`modules`, `classes`, `objects`, `types`, `functions` 등)에 대한 정의이자, 사용자와 개발자(생산자) 간의 **계약**과 같습니다. 이는 서로의 기대를 명확히 하고, 코드 변경이 발생하더라도 명세는 그대로 유지될 수 있어 소프트웨어 변경을 용이하게 합니다.

### 강의 맥락

교수님은 "Recall: Specifications" 슬라이드를 통해 **명세의 중요성**을 환기하며 지난 시간에 다룬 클래스 명세에 대한 심층적인 논의를 시작하는 도입부로 활용했습니다. 비록 슬라이드의 각 항목을 직접적으로 설명하지는 않았지만, 명세가 "사용자 수준 정보(usual level information)"와 "구현 수준(implementation level)" 사이의 "계약"이라는 점을 강조하며, 사용자는 실제 구현에 대해 알 필요 없이 명세 수준에서의 추상적인 동작만 이해해도 된다는 점을 역설했습니다.

특히 다음 부분에서 슬라이드의 핵심 개념이 반영되었습니다:
- **사용자와 개발자 간의 계약**: "users don't need to know anything about the concrete behavior, only need to understand the exact behavior, but it is still no problem because this abstract behavior completely or faithfully captures the internal behavior." (사용자는 구체적인 행동에 대해 아무것도 알 필요 없고, 정확한 행동만 이해하면 되지만, 이 추상적인 행동이 내부 행동을 완전히 또는 충실히 포착하기 때문에 문제가 되지 않습니다.)
- **변경 용이성**: "even though it is a specification level, the method may actually modify internal space. But as long as as long as abstract values are the same, then it's actually observable, right? So that because it doesn't modify observable state." (명세 수준이더라도 메서드가 내부 상태를 실제로 수정할 수 있지만, 추상 값이 동일한 한 실제로는 관찰 가능합니다. 이는 관찰 가능한 상태를 수정하지 않기 때문입니다.) 즉, 내부 코드 변경이 있어도 명세(추상 값)가 유지되면 사용자 입장에서는 변경을 인지하지 못한다는 의미입니다.

이는 명세가 소프트웨어의 **가시적인 동작과 기대치**를 정의하고, **내부 구현 변경으로부터 사용자를 격리**하여 유연한 개발을 가능하게 하는 핵심적인 역할을 수행함을 강조합니다.

### 시험 포인트

- 명세는 사용자-개발자 간의 **계약**이며, 서로의 기대를 정의한다. ⭐
- 명세는 **코드 변경으로부터 사용자를 보호**하여 유연한 개발을 가능하게 한다. ⭐

---

## Slide 3

**핵심 개념**
클래스 명세(Class Specifications)는 객체 지향 프로그래밍에서 클래스의 동작과 상태를 정의하는 중요한 요소입니다. 사용자 관점과 구현자 관점 모두에서 클래스의 올바른 사용과 구현을 보장하기 위한 원칙과 기법을 다룹니다.

**강의 맥락**
교수님은 지난 시간에 학습한 "클래스 명세" 내용을 복습하고 이번 강의에서도 이어서 다룰 것이라고 언급하며, 핵심 개념들을 다시 한번 강조했습니다.

*   **클래스 명세 (사용자 관점)**는 다음 네 가지 요소를 포함합니다:
    1.  각 메서드(함수)의 **전제조건(precondition)**
    2.  각 메서드(함수)의 **후제조건(postcondition)**
    3.  클래스의 **추상 표현(abstract representation)** 또는 **추상 값(abstract values)**: 사용자가 알아야 할 내부 상태의 추상적인 모습.
    4.  **클래스 불변식(class invariant)**: 추상 값이 항상 만족해야 하는 조건.
*   **구현 명세 (구현자 관점)**는 다음 요소들을 추가로 고려합니다:
    1.  **구체적인 표현(concrete representation)** 또는 **구체 값(concrete values)**: 실제 구현에 사용되는 구체적인 데이터 타입과 내부 상태.
    2.  **추상 함수(abstraction function)**: 구체 값이 추상 값으로 어떻게 매핑되는지를 정의하는 함수.
    3.  **표현 불변식(representation invariant)**: 구체 값이 항상 만족해야 하는 조건으로, 유효한 추상 값으로 매핑되기 위해 구체 값이 지켜야 할 내부적인 제약 조건입니다.

교수님은 또한 `private` 멤버 변수, `final` 키워드, 불변(immutable) 객체/데이터 타입, Java Record 등을 활용하여 의도치 않은 내부 표현 노출(representation exposure)을 방지하는 것이 중요하다고 재차 강조했습니다.

**시험 포인트**
*   ⭐ **클래스 명세의 4가지 주요 구성 요소** (전제조건, 후제조건, 추상 값, 클래스 불변식)를 정확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ **구현 명세의 3가지 주요 구성 요소** (구체 값, 추상 함수, 표현 불변식) 또한 중요하며, 클래스 명세와 구현 명세 간의 관계를 이해해야 합니다.
*   ⭐ **내부 표현 노출(representation exposure)의 개념과 이를 방지하기 위한 실제 코딩 기법** (예: `private` 접근 제한자, `final` 키워드, 불변 객체 사용, Java Record 활용)들을 숙지해야 합니다.

---

## Slide 4

**핵심 개념**
*   **스택(Stack)**은 `last-in, first-out (LIFO)` 특성을 가진 자료구조이다.
*   요소의 추가(`push`)와 제거(`pop`)는 항상 스택의 맨 위(`top`)에서 이루어진다.
*   **기본 연산**:
    *   `push(x)`: 요소 `x`를 스택의 맨 위에 추가한다.
    *   `pop()`: 스택의 맨 위 요소를 제거하고 그 값을 반환한다.
    *   `size()`: 현재 스택에 저장된 요소의 개수를 반환한다.
    *   `capacity()`: (크기가 제한된 스택의 경우) 스택이 가질 수 있는 최대 요소의 개수를 반환한다.

**구체적 예시**
*   슬라이드 우측의 다이어그램은 스택에 `1`부터 `5`까지 `push`하는 과정(1-5번)과, 이후 `pop`하여 스택에서 요소를 제거하는 과정(6-10번)을 시각적으로 보여주며 스택의 `LIFO` 동작 방식을 명확히 설명한다.

**강의 맥락**
*   교수님은 스택을 **객체(Object)** 또는 **클래스 명세(Class Specification)**의 필수적인 부분을 설명하기 위한 유명한 예시로 활용하고 있다.
*   함수 명세와 달리 클래스 명세는 각 메서드에 대한 전제조건(Precondition)과 후제조건(Postcondition) 외에, 내부 상태의 **추상적 표현(Abstract Representation)** 또는 **추상 값(Abstract Values)**과 이러한 추상 값이 만족해야 하는 조건인 **클래스 불변식(Class Invariant)**을 추가로 포함한다고 강조했다. 예를 들어, 스택의 현재 요소 수는 최대 개수를 초과할 수 없으며, 음수가 될 수 없다는 것이 클래스 불변식의 예시이다.
*   또한, 구현자 관점에서는 **구체적 표현(Concrete Representation)**(실제 데이터 타입), 구체적 값과 추상적 값 사이의 관계를 나타내는 **추상화 함수(Abstraction Function)**, 그리고 구현 단계에서 구체적 표현이 만족해야 하는 제약 조건인 **표현 불변식(Representation Invariant)**의 중요성을 설명하는 데 스택(특히 배열로 구현된 스택)을 예시로 들었다. 예를 들어, 스택을 배열로 구현했을 때 `top` 인덱스가 0 이상이고 배열의 크기보다 작아야 한다는 조건이 표현 불변식이다.

**시험 포인트**
*   ⭐ 스택의 **LIFO 특성**과 `push`, `pop`, `size`, `capacity` 등의 **기본 연산**을 정확히 이해해야 한다.
*   ⭐ 스택이 **클래스 명세(Class Specification)**, **추상적 표현(Abstract Representation)**, **클래스 불변식(Class Invariant)**, **구체적 표현(Concrete Representation)**, **표현 불변식(Representation Invariant)** 등 객체지향 프로그래밍의 핵심 개념들을 설명하는 **대표적인 예시**로 사용된다는 점을 인지하는 것이 중요하다.

---

## Slide 5

**핵심 개념**
*   **클래스 명세(Class Specification)**: 일반적인 함수 명세(Function Specification)가 `preconditions`(사전 조건)와 `postconditions`(사후 조건)만으로 동작을 정의하는 것과 달리, `Stack`과 같은 `stateful objects`(상태를 가지는 객체)의 동작을 명세하기 위해서는 추가적인 요소가 필요하다.
*   **Stateful Objects의 명세 요소**:
    1.  **메서드별 `preconditions` 및 `postconditions`**: 각 메서드의 호출 전후 조건을 명세한다.
    2.  **`abstract representation` (추상 값)**: 객체의 내부 상태를 사용자가 이해할 수 있는 추상적인 형태로 표현한다. 이는 `data abstraction`의 핵심 개념이다.
    3.  **`class invariant` (클래스 불변식)**: `abstract values`가 항상 만족해야 하는 조건으로, 객체의 유효한 상태를 정의한다.

**코드/수식 해설**
```java
public interface Stack {
    void push(Object item);  // 스택에 요소를 추가하는 메서드
    Object pop();            // 스택에서 최상단 요소를 제거하고 반환하는 메서드
    int size();              // 현재 스택에 있는 요소의 개수를 반환하는 메서드
    int capacity();          // 스택의 최대 용량을 반환하는 메서드
    // ...
}
```
*   위 코드는 `Stack`이라는 인터페이스의 정의를 보여주며, 스택이 제공하는 `public` 메서드들을 명세한다. 이러한 메서드들의 동작은 `preconditions`와 `postconditions`를 통해 정의될 수 있다.

**구체적 예시**
*   **`abstract representation` (추상 값) 예시**: `Stack`의 경우, 내부 상태를 "현재 스택에 들어있는 요소들의 리스트"와 같이 추상적으로 표현할 수 있다.
*   **`class invariant` (클래스 불변식) 예시**: 스택의 `abstract values`에 대해 "현재 요소의 개수($n$)는 $0$보다 크거나 같고 최대 용량($C$)보다 작거나 같아야 한다" ($0 \le n \le C$)와 같은 조건을 설정할 수 있다.

**강의 맥락**
교수님은 현대 소프트웨어 개발에서 `object-oriented example`인 `Stack`을 사용하여 `object` 또는 `class specification`의 필수 요소를 설명한다. 특히, `function specification`이 `precondition`과 `postcondition`만을 다루는 것과 달리, `class specification`은 `Stack`과 같은 `stateful objects`를 다루기 때문에 두 가지 추가적인 요소가 필요하다고 강조한다. 이 두 가지는 객체의 내부 상태에 대한 `abstract representation` (또는 `abstract values`)과 이 `abstract values`가 만족해야 하는 `class invariant`이다. 이러한 추가 요소들이 `stateful objects`의 복잡한 동작을 효과적으로 명세하는 데 필수적이라고 설명한다.

**시험 포인트**
*   ⭐`function specification`과 `class specification`의 차이점을 설명하고, `class specification`에 `preconditions`와 `postconditions` 외에 추가되는 두 가지 요소(⭐`abstract representation` 또는 `abstract values`, ⭐`class invariant`)를 그 개념과 함께 설명할 수 있어야 한다.
*   ⭐주어진 객체(예: `Stack`)에 대해 `abstract representation`과 `class invariant`의 구체적인 예시를 제시할 수 있어야 한다.

---

## Slide 6

### 핵심 개념

스택(Stack)은 추상적인 자료구조이며, 이를 구현하는 방식은 다양합니다. 예를 들어 배열(array)이나 연결 리스트(linked list) 등으로 구현할 수 있습니다. 각 구현 방식은 내부적인 표현(internal representation)이 다르지만, 스택의 "명세(specification)"는 특정 구현 방식에 의존해서는 안 됩니다. 즉, 사용자가 스택을 사용할 때 내부 구현을 몰라도 스택의 동작을 이해하고 사용할 수 있어야 합니다.

### 강의 맥락

교수님은 "현대 소프트웨어 개발은 항상 객체 지향적(object-oriented) 예시를 포함한다"고 언급하며, 스택(Stack) 예시를 통해 객체 또는 클래스 명세의 필수적인 부분을 설명하기 시작했습니다.

강의에서는 함수 명세(function specification)가 선행 조건(precondition)과 후행 조건(postcondition)만 포함하는 것과 달리, 클래스 명세는 두 가지 추가적인 요소를 포함한다고 강조했습니다.

1.  **추상적 표현 (Abstract Representation)**: 내부 상태의 추상적 표현으로, 사용자 수준에서 '추상 값(abstract values)'이라고 불립니다.
2.  **클래스 불변식 (Class Invariant)**: 이 추상 값들이 만족해야 하는 특정 조건입니다. 예를 들어 스택의 현재 요소 개수가 최대 개수를 넘을 수 없고 음수일 수 없다는 조건 등입니다.

따라서 클래스 명세는 다음 네 가지를 포함합니다:
*   각 메서드에 대한 선행 조건 및 후행 조건
*   사용자가 알아야 할 클래스의 추상적 표현(추상 값)
*   사용자 수준에서 추가적인 요구사항을 제공하는 클래스 불변식

이러한 클래스 명세를 통해 구현 방식과 독립적으로 동작을 명세할 수 있습니다.

⭐ **시험 포인트**: 클래스 명세가 구현과 독립적으로 동작을 기술하기 위해 포함해야 하는 요소 (추상적 표현, 클래스 불변식)를 정확히 이해하고 설명할 수 있어야 합니다. 특히 **추상적 표현**이 내부 구현에 의존하지 않는 추상적인 '값'을 나타낸다는 점이 중요합니다.

---

## Slide 7

### 핵심 개념

데이터 추상화(Data Abstraction)는 객체 지향 프로그래밍의 핵심 원칙 중 하나로, 클라이언트(사용자)에게 **무엇(what)**을 하는지에 대한 `operations` (명세)만 제공하고, **어떻게(how)** 구현되었는지에 대한 내부 `data` (내부 표현)는 숨기는 것을 의미합니다. 이를 통해 내부 구현의 변경이 외부에 미치는 영향을 최소화하고 코드의 모듈성과 유지보수성을 높일 수 있습니다.

*   **클라이언트에게 `operations`만 제공**: 클래스의 사용자는 특정 데이터 타입이 어떤 연산을 지원하는지(명세)만 알면 되고, 그 연산이 내부 데이터를 어떻게 조작하는지는 알 필요가 없습니다.
*   **`what`과 `how` 분리**:
    *   `what`: 추상적인 수준에서 객체가 제공하는 기능과 동작(명세).
    *   `how`: 구체적인 수준에서 객체의 내부 데이터 구조와 알고리즘(구현).
    *   내부 표현(internal representation)을 숨김으로써, 사용자는 복잡한 구현 세부 사항으로부터 격리됩니다.
*   **추상 데이터 타입(Abstract Data Type, ADT)**: 컴퓨터 과학의 근본적인 개념으로, 데이터 타입이 지원하는 연산들의 집합과 이들 연산의 추상적인 동작을 정의하지만, 실제 구현 방법은 명시하지 않습니다.

오른쪽에는 컴퓨터 과학자 **Barbara Liskov (튜링상, 2008)**의 사진이 있습니다. 그녀는 추상 데이터 타입과 객체 지향 프로그래밍 분야에 지대한 공헌을 했습니다.

### 강의 맥락

교수님은 지난 시간에 이어 클래스 명세(class specification)의 중요성을 강조하며 데이터 추상화 개념을 설명했습니다.

*   교수님은 "abstract representation (abstract values)"과 "concrete representation (concrete values)"을 구분하면서, 사용자는 클래스의 "abstract values"에 대해서만 알 필요가 있고 실제 "concrete information" (구현 세부 사항)에 대해서는 알 필요가 없다고 설명했습니다. 이는 바로 이 슬라이드의 "Separate what from how"와 "hide internal representation"에 해당합니다.
*   클래스 명세는 각 메서드의 `Precondition`과 `Postcondition`, 그리고 사용자 관점에서의 `abstract representation` (또는 `abstract values`) 및 `Class Invariant`를 포함한다고 요약했습니다. 반면 구현자(implementer)는 `concrete representation`과 `abstraction function`, 그리고 `representation invariant`를 고려해야 한다고 했습니다. 이 구분 자체가 데이터 추상화의 본질을 담고 있습니다.
*   교수님은 사용자가 내부 구현을 알 필요 없이 `abstract behavior`만으로 프로그램의 동작을 추론할 수 있어야 한다고 강조했습니다. 이는 추상화된 동작이 내부 동작을 "충실하게 (faithfully)" 포착해야 한다는 원칙입니다.
*   이러한 데이터 추상화 원칙을 위반하여 내부 표현이 외부에 노출되는 문제("representation exposure")를 경계해야 한다고 설명했습니다. 예를 들어, private 멤버 변수에 대한 참조를 반환하는 `getter` 메서드는 외부에서 객체의 내부 상태를 직접 변경할 수 있게 하여 `class invariant`나 `representation invariant`를 깨뜨릴 수 있다고 경고했습니다.
*   ⭐`representation exposure`를 피하기 위한 방법으로 모든 멤버 변수를 `private`으로 선언하고, `final` 키워드를 사용하며, 불변 객체(immutable object)를 활용하는 방법 등을 언급하며 데이터 추상화의 실질적인 적용 방법을 설명했습니다. 특히 불변 객체는 `class invariant` 위반 문제를 방지하는 데 매우 유용하다고 강조했습니다.

### 시험 포인트

*   ⭐**데이터 추상화의 정의**: 클라이언트에게 `operations`만 제공하고 `data`는 숨기는 것의 의미와 "what"과 "how"를 분리하는 중요성을 이해해야 합니다.
*   ⭐**추상 데이터 타입(ADT)**의 개념과 이것이 컴퓨터 과학의 근본적인 개념인 이유를 알아야 합니다.
*   ⭐**클래스 명세와 구현의 분리**: 추상 값(abstract values)과 구체 값(concrete values)의 역할 및 이 둘을 연결하는 추상화 함수(abstraction function)의 개념을 명확히 이해해야 합니다.
*   ⭐**Representation Exposure의 위험성**: 내부 구현을 노출했을 때 발생할 수 있는 문제점(예: `class invariant` 위반)과 이를 방지하기 위한 방법(private 멤버, final 키워드, 불변 객체 사용 등)을 설명할 수 있어야 합니다.

---

## Slide 8

**핵심 개념**
객체의 추상적 관점(Abstract View of Objects)은 사용자(클라이언트)가 객체를 이해하고 상호작용하는 방식에 중점을 둡니다. 이는 다음 두 가지로 정의됩니다:
*   **추상 값(Abstract Values)**: 객체의 내부 구현(internal representation)을 숨기고(정보 은닉, information hiding) 외부에서 관찰 가능한 논리적인 상태를 나타냅니다. 사용자는 이 추상 값만을 통해 객체의 상태를 이해합니다.
*   **연산(Operations)**: 객체와 상호작용하는 유일한 방법으로, 객체의 상태를 변경하거나 조회하는 메소드들을 의미합니다.

**구체적 예시**
*   **Stack**: 스택의 추상적 관점은 '요소들의 수학적 리스트(a mathematical list of elements)'로 볼 수 있습니다. 사용자는 스택이 배열로 구현되었는지, 연결 리스트로 구현되었는지 알 필요 없이, 단순히 push, pop 등의 연산을 통해 리스트 형태의 스택을 다룬다고 생각합니다.

**강의 맥락**
교수님은 현대 소프트웨어 개발에서 객체 지향 패러다임이 중요하며, 그 본질을 이해하기 위해 스택 예시를 사용한다고 강조했습니다. 함수 명세(precondition, postcondition) 외에 클래스 명세(class specification)에는 두 가지 추가적인 요소가 있다고 설명했습니다. 그중 하나가 바로 **내부 상태의 추상적 표현(abstract representation of internal states)**이며, 이를 **추상 값(abstract values)**이라고 부릅니다. 이는 사용자가 알아야 할 정보이며, 클래스 사용자의 관점에서 객체를 바라보는 방식입니다.

⭐ 클래스 명세는 다음 네 가지를 포함합니다:
1.  각 메소드에 대한 **Precondition**
2.  각 메소드에 대한 **Postcondition**
3.  클래스의 **추상 표현(Abstract Representation)** 또는 **추상 값(Abstract Values)** (사용자 관점에서 알아야 할 정보)
4.  **클래스 불변식(Class Invariant)** (추상 값이 만족해야 할 추가 조건)

또한, 교수님은 실제 내부 구현 수준의 상태 변화와 사용자 수준(추상적 수준)의 상태 변화가 있음을 설명하며, 사용자는 내부 구현에 대해 알 필요 없이 추상적 행동(abstract behavior)만을 이해하면 된다고 강조했습니다. 이는 정보 은닉의 중요성과 연결됩니다.

---

## Slide 9

**핵심 개념**:
이 슬라이드는 스택(Stack) 데이터 구조의 메서드들을 명세(Specification)하는 방법을 보여줍니다. 특히 메서드의 **선행 조건 (Precondition)**과 **후행 조건 (Postcondition)**을 명확히 정의함으로써, 해당 메서드가 어떤 상황에서 호출되어야 하고 (requires), 호출된 후 어떤 결과를 보장하는지 (ensures)를 설명합니다. 이는 객체지향 프로그래밍에서 클래스의 동작을 사용자 관점에서 명확히 이해하고 보장하는 데 필수적입니다.

**코드 해설**:

슬라이드는 스택의 세 가지 주요 메서드인 `size()`, `push(Object item)`, `pop()`에 대한 명세를 JML(Java Modeling Language) 스타일의 주석으로 보여줍니다.

1.  **`int size()`**: 스택의 현재 길이를 반환합니다.
    ```java
    //@ requires:
    //@   true
    //@ ensures:
    //@   returns the length of the stack
    int size();
    ```
    *   `requires: true`: 이 메서드는 항상 호출될 수 있습니다. (선행 조건 없음)
    *   `ensures: returns the length of the stack`: 이 메서드는 스택의 현재 요소 개수를 반환함을 보장합니다.

2.  **`void push(Object item)`**: 스택에 요소를 추가합니다.
    ```java
    //@ requires:
    //@   item is not null and size() < capacity()
    //@ ensures:
    //@   modifies the stack by adding item to the end of the stack
    void push(Object item);
    ```
    *   `requires: item is not null and size() < capacity()`: `item`은 `null`이 아니어야 하고, 스택이 최대 용량(`capacity()`)에 도달하지 않았을 때만 호출될 수 있습니다. (스택 오버플로우 방지)
    *   `ensures: modifies the stack by adding item to the end of the stack`: 스택의 상태를 변경하여 `item`을 스택의 끝(top)에 추가함을 보장합니다.

3.  **`Object pop()`**: 스택의 최상단 요소를 제거하고 반환합니다.
    ```java
    //@ requires:
    //@   size() > 0
    //@ ensures:
    //@   modifies the stack by removing the last item, and returns the removed item
    Object pop();
    ```
    *   `requires: size() > 0`: 스택에 최소 하나 이상의 요소가 있을 때만 호출될 수 있습니다. (스택 언더플로우 방지)
    *   `ensures: modifies the stack by removing the last item, and returns the removed item`: 스택의 상태를 변경하여 최상단 요소를 제거하고, 제거된 요소를 반환함을 보장합니다.

**강의 맥락**:
교수님은 이 슬라이드를 통해 "객체 또는 클래스 명세의 필수적인 부분"을 보여주기 위해 스택 예제를 사용한다고 언급합니다. 함수 명세가 선행 조건과 후행 조건만을 포함하는 것과 달리, **클래스 명세는 메서드별 선행 조건 및 후행 조건 외에 두 가지 추가 사항(추상 표현/추상 값, 클래스 불변식)을 포함**한다고 강조합니다. 이 슬라이드는 그중에서도 각 메서드의 선행 조건 (`requires`)과 후행 조건 (`ensures`)을 구체적으로 보여주는 부분입니다.

교수님은 다음 네 가지가 클래스 명세에 포함된다고 요약했습니다:
1.  각 메서드에 대한 선행 조건 (Precondition)
2.  각 메서드에 대한 후행 조건 (Postcondition)
3.  사용자가 알아야 할 클래스의 추상 표현 (Abstract Representation) 또는 추상 값 (Abstract Values)
4.  사용자 수준에서 추가 요구 사항을 제공하는 클래스 불변식 (Class Invariant)

이 슬라이드는 이 네 가지 중 첫 번째와 두 번째(메서드의 선행/후행 조건)를 스택 예시로 설명하고 있습니다.

**시험 포인트**:
*   ⭐ **클래스 명세의 구성 요소** (선행 조건, 후행 조건, 추상 표현, 클래스 불변식)를 이해하고 설명할 수 있어야 합니다.
*   ⭐ 각 스택 메서드(`size()`, `push()`, `pop()`)의 **선행 조건과 후행 조건을 정확히 구분하고 설명**할 수 있어야 합니다. 특히 `push`와 `pop`의 스택 오버플로우/언더플로우 관련 조건은 중요합니다.
*   `requires`와 `ensures` 키워드의 의미와 용도를 명확히 파악하는 것이 중요합니다.

---

## Slide 10

- **핵심 개념**:
객체 지향 프로그래밍에서 객체의 상태와 상호작용 방식에 따라 연산을 세 가지 유형으로 분류합니다.
1.  **Observer (또는 Getter)**: 객체의 내부 상태를 변경하지 않고 정보를 반환하는 연산입니다.
2.  **Mutator (또는 Setter)**: 객체의 내부 상태를 변경하는 연산입니다.
3.  **Producer**: 기존 객체를 변경하지 않고 새로운 객체를 생성하여 반환하는 연산입니다.

- **구체적 예시**:
    *   **Observer**: `size()`, `capacity()`
    *   **Mutator**: `push(item)`, `pop()`
    *   **Producer**: `clone()`

- **강의 맥락**:
강의에서는 객체의 내부 상태를 변경하지 않는 `Immutable object`를 설계할 때 `Producer` 연산의 중요성을 강조합니다. 교수님은 "일반적으로 데이터 타입이 `immutable`로 선언되면, 연산은 주로 새 객체를 반환합니다. 이것이 바로 `Producer`의 역할입니다."라고 설명했습니다. 이는 기존 객체를 수정하는 대신 새로운 객체를 생성하여 반환함으로써 `immutable`의 특성을 유지하게 합니다. 또한 자바의 `String`, `Integer`와 같은 기본 타입들이 `immutable`하며, `List.of()`와 같은 API들도 `immutable` 컨테이너를 반환하는 `Producer`의 역할을 한다고 언급하며, `Producer` 연산이 `representation exposure`를 방지하는 데 유용하다고 강조했습니다.

- **시험 포인트**:
    *   객체의 연산 유형 세 가지(Observer, Mutator, Producer)를 구분하고 각 유형의 특징과 예시를 설명하는 것 ⭐
    *   특히 `Immutable object` 설계 시 `Producer` 연산이 기존 객체 변경 없이 새로운 객체를 생성하여 반환한다는 점 ⭐
    *   `Producer` 연산이 `representation exposure` 방지에 어떻게 기여하는지 이해하는 것 ⭐

---

## Slide 11

### 핵심 개념

이 슬라이드는 **클래스 불변식(Class Invariant)**의 개념과 그 중요성을 설명합니다. 클래스 불변식은 클래스의 추상 값이 항상 유지해야 하는 제약 조건으로, 모든 클래스 연산(메서드)에 의해 **보존(preserved)**되어야 합니다. 이는 클래스의 `abstract values`가 항상 유효한 상태를 유지하도록 보장합니다.

### 코드/수식 해설

스택(Stack) 클래스의 경우, 다음과 같은 조건이 항상 만족되어야 합니다.
`0 <= size() <= capacity()`
이는 스택의 현재 원소 개수(`size()`)가 음수일 수 없고, 스택의 최대 용량(`capacity()`)을 초과할 수 없다는 것을 의미합니다.

아래는 `Stack` 인터페이스에 클래스 불변식을 명시하는 예시입니다:

```java
public interface Stack {
    //@ invariant: 0 <= size() <= capacity()
    // ...
}
```

여기서 `//@ invariant` 주석은 스택 객체가 어떤 상태에 있든 항상 `size()`가 0 이상이고 `capacity()` 이하라는 조건을 만족해야 함을 나타냅니다.

### 강의 맥락

교수님은 클래스 명세(Class Specification)가 함수 명세와 달리 두 가지 추가적인 요소를 포함한다고 설명합니다. 하나는 내부 상태의 **추상 표현(abstract representation)** 또는 **추상 값(abstract values)**이며, 다른 하나는 바로 이 **클래스 불변식(class invariant)**입니다.

클래스 불변식은 추상 값이 특정 조건을 만족해야 한다는 것을 명시합니다. 예를 들어 스택의 경우 "현재 원소의 개수가 최대 개수를 넘어서는 안 되고, 음수가 되어서도 안 된다"는 조건을 예로 들어 설명했습니다. 이는 `user level`에서 필요한 추가적인 요구사항으로, 클래스의 사용자에게 클래스의 추상적인 상태가 가져야 할 특징을 알려줍니다.

교수님은 클래스 명세가 궁극적으로 다음 네 가지를 포함한다고 요약했습니다:
1.  각 메서드의 **사전 조건(Precondition)**
2.  각 메서드의 **사후 조건(Postcondition)**
3.  클래스의 **추상 표현(Abstract Representation)** 또는 **추상 값(Abstract Values)**
4.  **클래스 불변식(Class Invariant)**

### 시험 포인트

*   **클래스 불변식의 정의와 역할**을 정확히 이해하고 설명할 수 있어야 합니다. ⭐
*   클래스 불변식이 `abstract values`가 항상 유효한 상태를 유지하도록 `모든 연산에 의해 보존`되어야 한다는 점을 기억하세요. ⭐
*   클래스 명세를 구성하는 네 가지 핵심 요소 중 하나라는 점을 숙지해야 합니다. ⭐
*   스택 예시를 통해 클래스 불변식을 구체적으로 설명할 수 있어야 합니다. ⭐

---

## Slide 12

---

### **핵심 개념**
클래스 불변식(Class Invariant)은 클래스의 추상 값(abstract values)이 항상 만족해야 하는 조건입니다. 이 조건은 모든 메소드의 실행 전후, 특히 공개 메소드의 호출이 완료된 후에 항상 참이어야 합니다. `ValueRange` 인터페이스의 추상 값은 정수 쌍 `(l, u)`로, 여기서 `l`은 하한(lower bound)이고 `u`는 상한(upper bound)입니다.

### **코드/수식 해설**

```java
public interface ValueRange {
    //@ ensures: returns the first entry of the pair
    int getLower();

    //@ ensures: returns the second entry of the pair
    int getUpper();

    //@ requires : i < getUpper()
    //@ ensures : modify the first entry to i
    void setLower(int i);

    //@ requires : i > getLower()
    //@ ensures : modify the second entry to i
    void setUpper(int i);
}
```

-   `getLower()`: 현재 추상 값 `(l, u)`에서 하한 $l$을 반환합니다.
-   `getUpper()`: 현재 추상 값 `(l, u)`에서 상한 $u$를 반환합니다.
-   `setLower(int i)`:
    -   `@requires i < getUpper()`: 메소드 호출 전, 새로운 하한 $i$가 현재 상한 $u$보다 작아야 합니다($i < u$).
    -   `@ensures`: 하한을 $i$로 변경합니다.
-   `setUpper(int i)`:
    -   `@requires i > getLower()`: 메소드 호출 전, 새로운 상한 $i$가 현재 하한 $l$보다 커야 합니다($i > l$).
    -   `@ensures`: 상한을 $i$로 변경합니다.

**추상 값**: `ValueRange`의 추상 값은 `(l, u)` 형태의 정수 쌍입니다.

**클래스 불변식**:
주어진 `ValueRange`의 추상 값 `(l, u)`와 메소드의 `requires` 및 `ensures` 조건을 고려할 때, 이 `ValueRange` 객체가 나타내는 '범위'가 유효하려면 하한이 상한보다 크지 않아야 합니다. 즉, 하한은 상한보다 작거나 같아야 합니다.
따라서 `ValueRange`의 클래스 불변식은 다음과 같습니다.
`getLower() <= getUpper()` 또는 추상 값 $l$, $u$를 사용하여 $l \le u$ 입니다.

메소드의 사전 조건(`@requires`)은 이 불변식이 깨지지 않도록 보장합니다. 예를 들어, `setLower(i)`의 경우 새로운 하한 $i$가 기존 상한 `getUpper()`보다 작아야 한다는 조건(`i < getUpper()`)이 있기 때문에, $l \le u$라는 불변식이 이미 만족된 상태라면, 새로운 $l'$도 $l' < u$를 만족하여 불변식이 유지될 수 있도록 돕습니다.

### **강의 맥락**
교수님은 클래스 스펙(Class Specification)이 함수 스펙과 달리 두 가지 추가적인 요소를 포함한다고 설명했습니다. 하나는 내부 상태의 **추상 표현(Abstract Representation)**이며, 이를 **추상 값(Abstract Values)**이라고 부릅니다. 다른 하나는 이 추상 값이 특정 조건을 만족해야 한다는 것이며, 이것이 바로 **클래스 불변식(Class Invariant)**입니다.

교수님은 스택(Stack) 예시를 들며 현재 요소의 개수가 최대 개수를 넘지 않아야 하고 음수일 수 없다는 조건을 언급하면서 이를 클래스 불변식의 예시로 들었습니다. 즉, 클래스 불변식은 "사용자 관점"에서 클래스의 추상 상태가 항상 만족해야 하는 추가적인 요구사항을 제공합니다.

이번 슬라이드는 이러한 클래스 불변식 개념을 `ValueRange` 예시를 통해 구체적으로 파악하는 질문을 던지고 있습니다. 비록 교수님이 음성 전사에서 `ValueRange` 코드 자체를 직접적으로 분석하지는 않았지만, 이 슬라이드는 클래스 불변식이라는 핵심 개념을 이해하기 위한 중요한 예시 자료로 활용됩니다.

### **시험 포인트**
*   **클래스 불변식의 정의와 역할**: 클래스 불변식이 클래스의 추상 값에 대해 항상 참이어야 하는 조건임을 이해하고 설명할 수 있어야 합니다. ⭐
*   **추상 값으로부터 클래스 불변식 도출**: 주어진 추상 값 정의와 메소드의 사전/사후 조건을 바탕으로 해당 클래스의 클래스 불변식을 올바르게 식별할 수 있어야 합니다. ⭐
*   **클래스 스펙 구성 요소**: 클래스 스펙이 각 메소드의 사전/사후 조건, 추상 값, 그리고 클래스 불변식으로 구성된다는 점을 기억하세요. ⭐

---

## Slide 13

**핵심 개념**:
이 슬라이드는 소프트웨어 객체의 **명세(Specification)**와 **구현(Implementation)** 간의 관계를 설명합니다.
*   **추상 객체 (Abstract objects)**: 사용자가 객체를 이해하는 방식에 대한 명세입니다. 이는 **추상 값(abstract values)**을 통해 객체가 어떤 상태를 가지며 어떻게 동작하는지 설명하며, 클라이언트가 객체를 어떻게 생각해야 하는지에 초점을 맞춥니다.
*   **구체 객체 (Concrete objects)**: 실제 구현의 내부 명세입니다. 이는 객체의 내부 **구체 값(internal concrete values)**과 그에 따른 동작을 상세히 정의합니다.
*   **추상화 (Abstraction)**: 구체 객체(구현)가 추상 값(명세)으로 어떻게 해석되는지를 정의하는 과정 또는 기능입니다. 구체적인 내부 표현을 외부에서 이해할 수 있는 추상적인 개념으로 매핑합니다.
*   **표현 불변식 (Representation invariant)**: 구체적인 구현이 반드시 만족해야 하는 내부적인 제약 조건입니다. 이는 클래스 구현의 올바른 상태를 보장하는 역할을 합니다.

**강의 맥락**:
교수님은 지난 시간에 논의했던 '클래스 명세(class specification)'를 상기시키며 강의를 시작했습니다. 클래스 명세는 각 메소드의 선행 조건(precondition)과 후행 조건(postcondition), 사용자 측에서 필요한 정보인 추상 표현(abstract representation 또는 abstract values), 그리고 추가적인 요구사항인 클래스 불변식(class invariant)으로 구성됩니다.

이번 슬라이드에서는 '구현자(implementer) 측면'에서 필요한 추가적인 개념들을 설명합니다.
1.  **구체 표현 (Concrete representation)**: 구현은 반드시 `concrete representation` 즉, 구체적인 데이터 타입을 가져야 합니다. 이를 `concrete values`라고 부릅니다.
2.  **추상화 함수 (Abstraction function)**: `concrete values`와 `abstract values` 간의 관계를 정의합니다. 즉, 구현자가 작성한 실제 값을 사용자 수준의 정보로 매핑하는 방식입니다.
3.  **표현 불변식 (Representation invariant)**: 이러한 추상화가 추가적인 제약 조건을 만족해야 합니다. 교수님은 스택(stack) 예시를 들어, 배열을 이용한 스택 구현에서 `top` 인덱스가 음수이거나 배열의 크기를 초과해서는 안 된다는 조건을 예로 들었습니다. 이처럼 구현이 항상 올바른 추상 값을 제공하기 위해 충족되어야 하는 조건이 바로 `representation invariant`입니다.

교수님은 `representation invariant`의 식별이 디버깅과 버그 발견에 유용하며, 테스트 케이스나 어설션(assertion) 작성에 좋은 후보가 된다고 강조했습니다. ⭐`Representation invariant`가 위반될 경우, 예상치 못한 오류나 "더럽고 어려운 버그(dirty and difficult bugs)"의 일반적인 원인이 된다고 언급했습니다.

**시험 포인트**:
*   ⭐**추상 객체와 구체 객체의 차이점**: 각각이 어떤 관점에서 객체를 정의하는지 이해하는 것이 중요합니다.
*   ⭐**추상화 함수(Abstraction function)의 역할**: `concrete values`를 `abstract values`로 매핑하는 기능입니다.
*   ⭐**표현 불변식(Representation invariant)의 정의와 중요성**: 구체 구현의 올바른 상태를 보장하는 제약 조건이며, 버그 예방 및 디버깅에 핵심적인 역할을 합니다. (예: 스택의 `top` 인덱스 조건).

---

## Slide 14

**핵심 개념**:
이 슬라이드는 배열을 이용한 스택(`ArrayStack`) 구현의 예시를 보여줍니다. `ArrayStack`은 `Stack` 인터페이스를 구현하며, 내부적으로 `Object` 배열(`array`)과 스택의 최상단 위치를 가리키는 정수(`top`)를 사용하여 스택의 기능을 구현합니다. 이 예시는 객체 지향 프로그래밍에서 클래스의 내부 상태(추상 값과 구체적 표현) 및 메서드 구현을 이해하는 데 사용됩니다.

**코드/수식 해설**:
슬라이드의 코드는 자바(Java)로 작성된 `ArrayStack` 클래스의 일부를 보여줍니다.

```java
class ArrayStack implements Stack {
    private Object[] array; // 스택의 요소를 저장하는 배열
    private private int top = 0; // 스택의 최상단 인덱스 (다음 요소가 추가될 위치)

    // 생성자: 스택의 용량을 받아 배열을 초기화
    ArrayStack(int capacity) {
        array = new Object[capacity];
    }

    @Override
    public void push(Object item) {
        array[top++] = item; // 배열에 요소를 추가하고 top을 증가
    }

    @Override
    public Object pop() {
        return array[--top]; // top을 감소시키고 해당 위치의 요소를 반환
    }
    // ... 기타 스택 메서드 (isEmpty, peek 등)
}
```
`array`와 `top` 필드가 `private`으로 선언되어 외부에서 직접 접근할 수 없도록 캡슐화되어 있습니다. `push` 메서드는 요소를 스택에 추가하며 `top` 포인터를 증가시키고, `pop` 메서드는 스택에서 요소를 제거하며 `top` 포인터를 감소시킵니다.

**강의 맥락**:
교수님은 이 `ArrayStack` 예시를 통해 객체/클래스 명세의 필수적인 부분을 설명하고 있습니다. 특히, 클래스 명세가 함수 명세(사전 조건, 사후 조건) 외에 추상적 표현(Abstract Representation)과 클래스 불변식(Class Invariant)을 포함한다는 점을 강조했습니다. 구현자 입장에서는 구체적인 표현(Concrete Representation)과 추상화 함수(Abstraction Function), 그리고 표현 불변식(Representation Invariant)이 중요합니다.

이 `ArrayStack` 예시는 주로 "표현 노출(Representation Exposure)" 문제를 설명하는 데 사용되었습니다. 즉, 비록 `array`와 `top` 같은 내부 필드가 `private`으로 선언되어 있지만, 만약 이 클래스에 내부 `array`의 참조를 반환하는 `getElementRentArray()`와 같은 getter 메서드가 추가된다면, 외부 사용자가 반환된 참조를 통해 스택의 내부 상태를 직접 변경할 수 있게 되어 클래스의 불변식이 쉽게 깨질 수 있음을 지적했습니다. 이는 의도치 않게 클래스 내부의 핵심 속성을 외부로 노출시켜 버그나 보안 취약점을 야기할 수 있는 위험한 설계라고 강조합니다.

**시험 포인트**:
*   ⭐`ArrayStack`과 같이 `private` 필드를 가진 클래스에서 `getter` 메서드가 **내부 필드의 변경 가능한 참조(mutable reference)를 반환할 때 발생할 수 있는 문제점(표현 노출)**을 이해하는 것이 중요합니다.
*   ⭐이러한 표현 노출이 **클래스 불변식(Class Invariant)을 어떻게 위반**하는지, 그리고 이로 인해 **소프트웨어의 무결성(integrity)이 어떻게 깨질 수 있는지** 설명할 수 있어야 합니다.

---

## Slide 15

### 핵심 개념
소프트웨어 작성 원리에서 **추상화(Abstraction)**는 객체의 내부적인 **구체적 표현(Concrete Representation)**을 외부에 노출되는 **추상적 표현(Abstract Representation)**으로 매핑하는 과정을 의미합니다. 이 슬라이드는 `ArrayStack`의 구체적인 구현 방식(배열과 `top` 포인터)을 추상적인 `Stack List`로 표현하는 예시를 통해 이를 설명합니다.

### 구체적 예시
*   **Concrete (구체적 표현)**: 스택을 배열(`array`)과 현재 스택의 맨 위 요소를 가리키는 `top` 포인터로 구현한 `ArrayStack`의 내부 상태를 보여줍니다.
*   **Abstract (추상적 표현)**: `ArrayStack`의 구체적인 내부 구현을 사용자에게는 단지 일련의 요소들이 순서대로 쌓여있는 `Stack List` 형태로 보여줍니다.
*   **Abstraction (추상화)**: 구체적 표현을 추상적 표현으로 변환하는 과정입니다.

이 과정은 **추상화 함수(Abstraction Function)**를 통해 `concrete values`를 `abstract values`로 매핑합니다.

### 강의 맥락
교수님께서는 클래스 명세(Class Specification)가 메소드의 사전/사후 조건 외에 **추상적 표현(Abstract Representation)** 또는 **추상 값(Abstract Values)**을 포함한다고 설명했습니다. 이는 사용자가 클래스의 내부 상태를 이해하기 위해 필요한 정보입니다. 반면, 구현자 측에서는 실제 **구체적 표현(Concrete Representation)** 또는 **구체 값(Concrete Values)**을 다루게 됩니다.

교수님은 "The relationship between concrete values and abstract values are given by abstraction function, meaning that for each concrete value, we have to map that to abstract value."라고 강조하며, 구현자가 작성하는 실제 값들이 사용자 레벨의 정보로 어떻게 매핑되는지를 설명했습니다. 스택의 `array`와 `top` 포인터가 구체적 표현이고, 이것이 "just a list of elements"인 추상적 표현으로 연결되는 과정이 바로 이 슬라이드의 핵심 내용입니다. 사용자(user)는 실제 구현에 대해 알 필요 없이 추상적 레벨의 정보만 이해하면 된다고 언급하셨습니다.

### 시험 포인트
*   **추상적 표현(Abstract Representation)**과 **구체적 표현(Concrete Representation)**의 차이를 이해하고 설명할 수 있어야 합니다. ⭐
*   **추상화 함수(Abstraction Function)**가 `concrete values`를 `abstract values`로 매핑하는 역할을 한다는 것을 기억하세요. ⭐
*   `ArrayStack` 예시에서 배열과 `top` 포인터가 구체적이고, 스택 리스트가 추상적인 예시임을 이해해야 합니다. ⭐

---

## Slide 16

**핵심 개념**:
`CharSet` 클래스는 문자를 저장하는 유한하고 변경 가능한(mutable) 집합을 정의합니다. 슬라이드는 클래스의 추상적인 명세(specification) 방식을 보여주며, 각 메서드의 동작을 명확히 설명하기 위해 사전 조건(precondition)과 사후 조건(postcondition)을 `@requires` 및 `@ensures` 주석을 통해 명시합니다.

**코드/수식 해설**:
```java
/**
 * A finite mutable set of Characters
 */
class CharSet {
    // @ensures: add c into the set
    public void insert(Character c) { /* ... */ }

    // @ensures : remove c from the set
    public void delete(Character c) { /* ... */ }

    // @requires : true
    // @ensures : returns true iff the set includes c
    public boolean member(Character c) { /* ... */ }
    // ...
}
```
-   `class CharSet`: 문자 집합을 나타내는 클래스입니다. Javadoc 주석은 "A finite mutable set of Characters"로 이 클래스가 유한하고 *변경 가능한* 문자 집합임을 명시합니다.
-   `insert(Character c)`: 문자 $c$를 집합에 추가하는 메서드입니다. `@ensures` 주석은 이 메서드 호출 후 $c$가 집합에 포함됨을 보장하는 사후 조건입니다.
-   `delete(Character c)`: 문자 $c$를 집합에서 제거하는 메서드입니다. `@ensures` 주석은 호출 후 $c$가 집합에서 제거됨을 보장하는 사후 조건입니다.
-   `member(Character c)`: 문자 $c$가 집합에 포함되어 있는지 여부를 반환하는 메서드입니다.
    -   `@requires: true`: 이 메서드를 호출하기 위한 특별한 사전 조건이 없음을 나타냅니다 (즉, 항상 호출 가능).
    -   `@ensures: returns true iff the set includes c`: 메서드 호출 후 $c$가 집합에 포함되어 있을 경우에만 `true`를 반환한다는 사후 조건입니다.

**구체적 예시**:
1.  `CharSet mySet = new CharSet();` // 빈 문자 집합 생성
2.  `mySet.insert('A');` // 집합에 'A' 추가 (사후 조건: 'A'가 `mySet`에 포함)
3.  `mySet.member('A');` // `true` 반환 (사전 조건: 없음, 사후 조건: 'A' 포함 여부 반환)
4.  `mySet.delete('A');` // 집합에서 'A' 제거 (사후 조건: 'A'가 `mySet`에서 제거)
5.  `mySet.member('A');` // `false` 반환

**강의 맥락**:
제공된 음성 전사에서는 **`CharSet` 예시에 대한 직접적인 언급이나 상세한 설명은 없습니다.** 다만, 강의 전반부에서 클래스 사양(Class Specification)의 구성 요소로 각 메서드에 대한 사전 조건(Precondition)과 사후 조건(Postcondition)의 중요성이 강조되었습니다. 이 슬라이드는 이러한 일반적인 클래스 사양의 한 예시로, `CharSet` 클래스에서 `insert`, `delete`, `member`와 같은 메서드에 `@ensures` 및 `@requires`를 통해 명세를 정의하는 방식을 보여줍니다. 특히, 이 클래스는 "A finite mutable set of Characters"로 정의되어, 강의에서 다룬 '변경 가능한(mutable)' 객체와 관련된 개념을 시사합니다.

**시험 포인트**:
-   ⭐클래스 사양에서 각 메서드의 **사전 조건($@requires$)과 사후 조건($@ensures$)**을 명시하는 방법과 그 중요성을 이해해야 합니다.
-   ⭐클래스의 추상적인 동작을 사용자 관점에서 명세하는 것이 중요하며, 이는 실제 구현 세부 사항과 분리되어야 합니다.
-   ⭐**Mutable(변경 가능한) 객체**의 특징과, 이후 강의에서 다룬 표현 노출(representation exposure)과 같은 문제점 및 이를 관리하기 위한 설계 원칙(불변 객체 사용 등)과의 연관성을 이해하는 것이 중요합니다.

---

## Slide 17

**핵심 개념**:
`CharSet` 클래스는 내부적으로 `ArrayList`를 사용하여 문자의 집합을 구현하려고 합니다. 그러나 일반적인 집합(Set)의 정의는 중복된 요소를 허용하지 않는데, 현재 구현된 `insert` 메서드는 중복 검사 없이 요소를 추가하므로 집합의 기본적인 불변식(uniqueness of elements)을 위반할 가능성이 있습니다.

**코드/수식 해설**:
```java
class CharSet {
    private List<Character> elmList = new ArrayList<Character>(); // 내부 표현: 가변 리스트

    public void insert(Character c) {
        elmList.add(c); // 중복 검사 없이 요소를 추가
    }

    public void delete(Character c) {
        elmList.remove(c); // 첫 번째 일치하는 요소만 제거
    }

    public boolean member(Character c) {
        return elmList.contains(c); // 요소 존재 여부 확인
    }
    // ...
}
```
`insert(c)` 메서드는 `elmList.add(c)`를 호출하여 `Character c`를 단순히 `ArrayList`에 추가합니다. `ArrayList`는 중복 요소를 허용하고 순서를 유지하므로, 이 `CharSet` 구현은 수학적 집합의 가장 중요한 특성인 **요소의 유일성(uniqueness)**을 보장하지 못합니다. 또한, `delete(c)`는 첫 번째 요소만 제거하므로, 중복이 허용된 상태에서는 의도한 대로 동작하지 않을 수 있습니다.

**구체적 예시**:
`CharSet mySet = new CharSet();`
`mySet.insert('A');` // `elmList`는 `['A']`
`mySet.insert('A');` // `elmList`는 `['A', 'A']`
이 경우 `mySet`은 내부적으로 두 개의 'A'를 가지게 되어 집합의 정의에 위배됩니다.

**강의 맥락**:
교수님은 이전 시간까지 클래스 스펙, 추상 표현, 클래스 불변식, 구체적인 구현, 표현 불변식, 추상화 함수 등 객체지향 설계의 핵심 개념들을 설명했습니다. 이 슬라이드는 이러한 배경 지식을 바탕으로 "과연 이 구현이 올바른가?"라는 질문을 던지며, 실제 코드에서 발생할 수 있는 결함에 대한 논의를 시작합니다.

이 `CharSet` 예제는 두 가지 주요 결함을 내포하고 있습니다. 첫째, 집합으로서의 핵심 속성(중복 불가)을 보장하지 못하는 직접적인 구현 오류입니다. 둘째, 강의 맥락상 더 중요한 결함은 **표현 노출(representation exposure)**의 가능성입니다. 현재 코드에는 없지만, 만약 `elmList`와 같은 내부 가변(mutable) 객체의 참조를 반환하는 `public` 메서드(예: `List<Character> getElements() { return elmList; }`)가 추가된다면, 외부 코드가 이 참조를 통해 `elmList`를 직접 수정하여 `CharSet`의 내부 상태나 불변식을 훼손할 수 있습니다. 교수님은 "`private` 선언만으로는 충분하지 않다"며 이러한 잠재적 위험에 대해 강조하고, 이어지는 내용에서 `final` 키워드, 불변(immutable) 객체 사용, Java Record 등의 해결책을 논의할 것입니다.

⭐**시험 포인트**:
- **집합 불변식 위반**: `CharSet`이 수학적 집합을 의미할 때, `insert` 메서드가 중복 요소를 허용하는 것은 집합의 불변식인 '요소의 유일성'을 위반하는 주요 결함이다.
- **표현 노출의 위험성**: 이 코드 자체에는 없지만, 가변(mutable)한 내부 표현(`elmList`)의 참조를 외부로 반환하는 메서드가 존재할 경우, 외부에서 이를 수정하여 클래스의 불변식이나 예측 가능한 동작을 깨뜨릴 수 있는 '표현 노출' 문제에 취약하다. 이는 객체지향 설계에서 매우 중요한 고려사항이다.

---

## Slide 18

**핵심 개념**:
- **표현 불변식(Representation Invariant)**은 객체의 내부(구체적) 상태가 항상 만족해야 하는 조건입니다. 이는 추상 값과 구체적 값 간의 매핑(추상화 함수)이 유의미하게 작동하도록 보장하며, 데이터의 일관성과 무결성을 유지하는 데 필수적입니다.
- `CharSet` 클래스 예시에서는 `List<Character>`를 사용하여 문자의 집합을 표현하고 있습니다. 이때 내부 `elmList`는 `null` 값을 포함하지 않고 중복된 요소를 가지지 않아야 한다는 것이 표현 불변식으로 명시됩니다.
- ⭐ **메소드는 표현 불변식을 항상 유지해야 합니다.** (메소드 실행 전후로 불변식이 만족되어야 함)

**코드/수식 해설**:
```java
class CharSet {
    //@ invariant: elmList has no nulls and no duplicates
    private List<Character> elmList = new ArrayList<Character>();

    public void insert(Character c) {
        elmList.add(c);
    }

    public void delete(Character c) {
        elmList.remove(c);
    }

    public boolean member(Character c) {
        return elmList.contains(c);
    }
    // ...
}
```
- `elmList`: `CharSet`의 내부 데이터를 나타내는 `List<Character>` 타입의 구체적 표현입니다.
- `//@ invariant`: 주석으로 "elmList has no nulls and no duplicates"라는 표현 불변식이 명시되어 있습니다. 이 `CharSet`이 집합으로서 작동하기 위해 `elmList`는 `null` 값을 가지거나 중복 요소를 포함해서는 안 됩니다.
- `insert(Character c)`: 이 메소드는 단순히 `elmList.add(c)`를 호출합니다. 이 구현 방식은 `invariant` 조건을 **위반할 가능성**이 있습니다. 만약 `c`가 `null`이거나 이미 `elmList`에 존재하는 값(중복)이라면, 메소드 실행 후 `CharSet`의 표현 불변식은 깨지게 됩니다.

**구체적 예시**:
`CharSet`의 `insert` 메소드는 표현 불변식인 "no duplicates"와 "no nulls"를 직접적으로 확인하거나 방지하는 로직(예: `if (!elmList.contains(c) && c != null) { elmList.add(c); }`)이 현재 코드에는 포함되어 있지 않습니다. 따라서 `CharSet` 객체에 이미 존재하는 문자를 다시 `insert`하거나 `null`을 `insert`하면, `elmList`의 상태가 불변식을 위반하게 됩니다.

**강의 맥락**:
교수님은 이 슬라이드를 통해 클래스의 **표현 불변식(Representation Invariant)** 개념을 `CharSet` 예시로 설명하고 있습니다. 이전에 클래스 스펙과 구현 스펙(추상화 함수, 표현 불변식 등)을 다루었음을 상기시키며, 특히 "이러한 종류의 표현 불변식을 식별하는 것은 디버깅 및 버그 발견에 유용하며, 테스트 케이스 작성에도 아주 좋은 후보입니다. 이는 종종 더럽고 어려운 버그의 흔한 원인이 됩니다. 이것이 위반되면..." (2분 30초경)이라고 강조하며 표현 불변식의 중요성을 강조합니다.

`CharSet`의 `elmList`에 대한 `@invariant` 주석을 통해 어떤 조건이 유지되어야 하는지 보여주며, `insert`와 같은 메소드가 이 불변식을 제대로 유지하는지 확인해야 함을 암시합니다. "Now we can locate the error"라는 문구는 현재 `insert` 구현이 표현 불변식을 위반할 수 있는 '오류'를 내포하고 있음을 지적하며, 이는 내부 표현이 잘못 관리될 때 발생하는 문제점을 찾는 맥락에서 제시됩니다.

**시험 포인트**:
- ⭐ **표현 불변식(Representation Invariant)의 개념과 역할**을 명확히 이해하고 설명할 수 있어야 합니다.
- ⭐ `CharSet`의 `insert` 메소드처럼, **표현 불변식을 위반할 가능성이 있는 코드 부분을 식별하고 그 이유를 설명**할 수 있어야 합니다. (2분 30초경 언급된 "디버깅", "어려운 버그"와 관련된 핵심 내용입니다.)
- ⭐ **표현 불변식이 위반되었을 때 소프트웨어에 미칠 수 있는 영향**에 대해 설명할 수 있어야 합니다.

---

## Slide 19

**핵심 개념**:
*   **추상화 (Abstraction)**: 사용자 관점에서 객체의 내부 상태를 `abstract values`(추상 값)로 표현하는 개념입니다. 이는 사용자가 클래스의 실제 구현을 알 필요 없이, 추상적인 수준에서 클래스의 동작을 이해하고 추론할 수 있도록 합니다.
*   **구현 (Representation)**: 개발자 관점에서 객체의 내부 상태를 `concrete values`(구체 값)로 구현하는 개념입니다. 실제 데이터 타입과 구조를 사용하여 클래스의 내부 상태를 정의합니다.
*   **Representation Exposure (표현 노출)**: 객체의 내부 구현(`concrete representation`)이 의도치 않게 외부로 노출되어, 외부 사용자가 직접 내부 상태를 변경하거나 `class invariant` (클래스 불변식) 또는 `representation invariant` (표현 불변식)을 위반할 수 있게 되는 상황을 의미합니다. 이는 프로그램의 안정성 및 보안에 심각한 문제를 야기할 수 있습니다.

**코드/수식 해설**:
*   해당 슬라이드에는 코드나 수식이 없습니다.

**구체적 예시**:
*   해당 슬라이드 자체에는 구체적인 예시가 없지만, 교수님은 `Stack` 클래스를 예로 들어 클래스 스펙과 구현 간의 관계를 설명한 후, 다음 내용에서 `getElementRentArray`와 같이 내부 배열에 대한 참조를 반환하는 메서드를 통해 `Representation Exposure`가 발생하는 상황을 다룰 것임을 예고했습니다.

**강의 맥락**:
*   교수님은 지난 강의에서 다룬 클래스 스펙(`class specification`)의 핵심 개념을 상기시키며 강의를 시작했습니다. 클래스 스펙은 각 메서드의 `precondition`, `postcondition` 외에 `abstract representation` (또는 `abstract values`)과 `class invariant`를 포함한다고 강조했습니다.
*   `abstract representation`은 사용자 관점에서 내부 상태를 추상적으로 표현한 것이고, `class invariant`는 이러한 추상 값들이 만족해야 할 조건이라고 설명했습니다.
*   이어서 구현자 측면에서는 `concrete representation` (구체적인 구현), `abstraction function` (구체 값을 추상 값으로 매핑), 그리고 `representation invariant` (구체적인 표현이 만족해야 할 제약 조건)가 중요하다고 언급했습니다.
*   이 슬라이드는 이러한 추상화와 구현의 관계를 바탕으로, 객체지향 프로그래밍에서 발생할 수 있는 중요한 문제인 `Representation Exposure`를 본격적으로 다루기 위한 서론 역할을 합니다. 교수님은 `Representation Exposure`가 발생할 경우 클래스 불변식이 쉽게 위반될 수 있다고 경고하며, 이를 피하기 위한 방법을 다음 내용에서 설명할 것임을 암시했습니다.

**시험 포인트**:
*   ⭐ `Abstraction`과 `Representation`의 개념을 명확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ `Class Invariant`와 `Representation Invariant`가 각각 `Abstract values`와 `Concrete values`에 대해 어떤 조건을 명시하는지 알아야 합니다.
*   ⭐ `Representation Exposure`가 무엇인지, 왜 문제가 되는지 (예: 클래스 불변식 위반) 정확히 설명할 수 있어야 합니다.

---

## Slide 20

### 핵심 개념

추상화(Abstraction)의 속성은 다음과 같습니다.
1.  **추상화는 함수(function)이다**:
    *   어떤 구체적인 객체(concrete object)라도 하나의 추상 객체(abstract object)로 매핑됩니다.
    *   이는 추상화 함수($A: \text{ConcreteState} \to \text{AbstractValue}$)를 통해 구체적인 구현 상태가 사용자에게 보이는 추상 값으로 변환된다는 의미입니다.
2.  **추상화는 전사(onto) 함수이다**:
    *   어떤 추상 객체에 대해서도 그에 대응하는 구체적인 객체가 존재합니다.
    *   즉, 모든 추상 값은 최소한 하나의 구체적인 구현 상태에 의해 표현될 수 있어야 합니다.
3.  **추상화는 단사(one-to-one) 함수가 아니다**:
    *   두 개 이상의 구체적인 객체가 동일한 하나의 추상 객체로 매핑될 수 있습니다.
    *   이는 내부 구현(concrete representation)이 달라도 외부에서 관찰되는 추상적인 상태(abstract value)는 같을 수 있음을 의미합니다.

### 강의 맥락

교수님께서는 이 슬라이드 내용이 지난 시간에 다루었던 내용에 대한 "빠른 요약(quick summary)"이라고 언급하셨습니다. 특히, 추상화의 속성과 시각화에 대한 "좋은 슬라이드(nice slides)"를 지난 시간에 보았다고 강조하며, 이는 추상화가 어떻게 작동하는지에 대한 기본적인 이해를 돕기 위한 복습 차원의 슬라이드임을 명확히 하셨습니다. 즉, 현재 강의에서는 이러한 추상화의 속성 자체를 깊게 다루기보다는, 앞으로 논의될 클래스 명세(class specification)와 구현(implementation)의 관계를 이해하기 위한 배경 지식으로 다시 한번 상기시키는 역할을 합니다.

### 시험 포인트

*   ⭐ **추상화의 세 가지 핵심 속성(`function`, `onto`, `not one-to-one`)을 이해하고 설명할 수 있어야 합니다.**
*   ⭐ 특히 `not one-to-one`의 의미(두 개의 다른 구체적인 상태가 하나의 추상적인 상태로 매핑될 수 있음)는 객체지향 설계에서 중요한 개념이므로 잘 숙지해야 합니다.

---

## Slide 21

**핵심 개념**:
`ArrayStack` 예시를 통해 클래스의 **구체적 표현(Concrete Representation)**(내부 `array`와 `top` 인덱스)과 **추상적 표현(Abstract Representation)**(외부 사용자에게 보이는 요소들의 리스트) 간의 관계를 시각적으로 보여줍니다. 각 메서드 호출에 따라 구체적 상태와 추상적 상태가 어떻게 변화하며, 이 둘이 **추상화 함수($\text{Abstraction Function}$)**를 통해 어떻게 매핑되는지 설명합니다.

**코드/수식 해설**:
슬라이드 상단의 코드는 `ArrayStack` 클래스의 사용 예시를 보여줍니다.
```java
ArrayStack stack = new ArrayStack(5); // 크기 5의 스택 객체 생성
stack.push("A");                     // 스택에 문자열 "A" 푸시
stack.push("B");                     // 스택에 문자열 "B" 푸시
stack.pop();                         // 스택에서 가장 상단의 요소 팝
```
이 코드의 각 단계는 아래 다이어그램의 상태 변화와 일치합니다.
*   다이어그램의 `Abstraction` 화살표는 내부의 **구체적 값(concrete values)**을 외부 사용자가 이해할 수 있는 **추상적 값(abstract values)**으로 매핑하는 **추상화 함수($\text{Abstraction Function}$)**를 나타냅니다.

**구체적 예시**:
슬라이드 하단의 다이어그램은 위 코드에 따른 `ArrayStack`의 상태 변화를 구체적/추상적 레벨에서 보여줍니다.
1.  **`new ArrayStack(5)`**: `array`는 크기 5로 할당되지만 내용은 비어있고, `top`은 스택의 첫 요소를 넣을 위치를 가리키는 초기 상태입니다. 추상적 표현은 빈 리스트 `[]`입니다.
2.  **`stack.push("A")`**: `array`의 `top`이 가리키는 위치에 "A"가 저장되고, `top`은 다음 요소를 위한 위치로 이동합니다. 추상적 표현은 `["A"]` 리스트입니다.
3.  **`stack.push("B")`**: `array`의 `top`이 가리키는 위치에 "B"가 저장되고, `top`은 다음 요소를 위한 위치로 이동합니다. 추상적 표현은 `["A", "B"]` 리스트입니다.
4.  **`stack.pop()`**: `top` 인덱스가 한 칸 감소하여 스택의 최상단 요소("B")가 제거된 효과를 줍니다(실제로 배열에서 데이터를 지우지 않을 수 있음). 추상적 표현은 다시 `["A"]` 리스트입니다.

**강의 맥락**:
교수님은 이 `ArrayStack` 예시를 사용하여 객체지향 프로그래밍에서 클래스 명세의 핵심 원리를 설명합니다.
*   클래스 명세는 **추상적 표현(abstract values)**과 그에 대한 **클래스 불변식(`class invariant`)**을 포함하며, 구현은 **구체적 표현(concrete values)**을 가집니다.
*   ⭐ **추상화 함수($\text{Abstraction Function}$)**는 구체적 값을 추상적 값으로 매핑하는 역할을 하며, 이 슬라이드는 그 매핑 과정을 시각적으로 보여줍니다.
*   메서드(`push`, `pop`) 호출 시, **구체적 구현 레벨의 상태 변화와 사용자 레벨(명세 레벨)의 추상적 상태 변화가 일관되게 발생**해야 함을 강조합니다.
*   교수님은 **어떤 구체적인 행동이라도 명세에 의해 시뮬레이션(simulated)되어야 한다**는 중요한 원칙을 설명합니다. 이는 사용자가 내부 구현을 몰라도 추상적 명세만으로 프로그램의 동작을 정확히 예측하고 추론할 수 있도록 보장합니다.

**시험 포인트**:
*   ⭐ **구체적 표현 (`concrete representation`)**과 **추상적 표현 (`abstract representation`)**의 개념을 `ArrayStack` 예시를 들어 설명할 수 있어야 합니다.
*   ⭐ **추상화 함수($\text{Abstraction Function}$)**가 구체적 값을 추상적 값으로 어떻게 매핑하는지 이해하는 것이 중요합니다.
*   ⭐ 메서드 호출(`push`, `pop`)에 따른 **구체적 상태 변화와 추상적 상태 변화의 연관성**을 파악하는 것이 핵심입니다.
*   ⭐ 구현의 동작이 명세에 의해 **시뮬레이션(simulated)** 되어야 한다는 원칙과 그 의미.

---

## Slide 22

**핵심 개념**
이 슬라이드는 객체의 내부 상태 변경이 외부에서 관찰 가능한(observable) 추상적 상태에는 영향을 미치지 않는 경우를 설명합니다. 이는 "추상적 등가성(abstract equivalence)"의 개념과 관련이 있으며, 내부 구현 최적화(예: `move-to-front optimization`)가 클라이언트에게는 투명하게 이루어질 수 있음을 보여줍니다.

**코드/수식 해설**
주어진 `CharSet` 클래스의 `member` 메서드 구현은 다음과 같습니다:
```java
boolean member(Character c1) {
    var i = elmList.indexOf(c1);
    if (i == -1)
        return false;
    elmList.add(0, elmList.remove(i)); // move-to-front optimization
    return true;
}
```
이 메서드는 `c1`이 `elmList`에 포함되어 있는지 확인합니다. 만약 `c1`이 존재한다면, 해당 요소를 리스트에서 제거한 후 다시 리스트의 맨 앞에 삽입하는 `move-to-front optimization`을 수행합니다. 이는 내부적인 구체(concrete) 객체의 상태(리스트의 요소 순서)를 변경하지만, `CharSet`이라는 추상적 객체(포함된 문자 집합 자체)의 상태(어떤 문자가 포함되어 있는지)는 변경하지 않습니다.

**강의 맥락**
교수님은 지난 시간에 이어 클래스 명세(class specification)에 대해 설명하며, 메서드가 내부 상태를 변경하더라도 추상적인 값이 동일하다면 외부에서는 이를 관찰할 수 없다고 강조했습니다. `CharSet`의 `member` 메서드 예시는 이러한 개념을 보여줍니다. 이 메서드는 문자 `c1`이 집합에 포함되어 있는지 여부만을 클라이언트에게 알리며, 만약 `c1`이 존재할 경우 내부적으로 해당 문자의 위치를 변경하는 최적화(`move-to-front optimization`)를 수행합니다. 이 내부적인 순서 변경은 구체적인 객체(리스트)의 상태를 바꾸지만, `CharSet`이 나타내는 추상적인 집합의 멤버십(어떤 문자가 포함되어 있는가)은 그대로 유지되므로 클라이언트에게는 이러한 변경이 **관찰 불가능(not observable)**하다는 점을 명확히 했습니다. 이는 실용적인 측면에서 내부 구현을 최적화할 때 유용한 원리입니다.

**시험 포인트**
⭐ **관찰 불가능한 내부 상태 변경**: 메서드가 내부 구체 객체의 상태를 변경하더라도, 추상적 객체의 상태(클라이언트가 관찰하는 명세 수준)가 동일하게 유지된다면 이는 올바른 동작으로 간주됩니다. 이러한 내부 변경은 클라이언트에게 `observable`하지 않습니다.
⭐ **추상화 함수(Abstraction Function)**: 구체적인 여러 표현(여기서는 리스트 내 요소의 순서가 다른 경우)이 동일한 하나의 추상적 값(여기서는 집합의 멤버십)에 매핑될 수 있음을 이해하는 것이 중요합니다.

---

## Slide 23

**핵심 개념**:
이 슬라이드는 **"구현이 명세에 부합한다(Implementation Meets Specification)"**는 객체 지향 프로그래밍의 핵심 원리를 설명합니다. 이는 구체적인 구현(Concrete Implementation)의 동작이 추상적인 명세(Abstract Specification)의 동작을 정확하고 충실하게 모방(simulate)해야 한다는 것을 의미합니다. 사용자는 구체적인 내부 구현을 알 필요 없이 추상적인 명세만으로도 클래스의 동작을 이해하고 추론할 수 있어야 합니다.

**코드/수식 해설**:
슬라이드의 다이어그램은 두 가지 레벨의 상태 변화를 보여줍니다.
*   **추상 객체(Abstract objects)**: ADT (Abstract Data Type) $A$의 인스턴스인 `ABST_1`에서 `ABST_2`로 추상적 동작 `af`를 통해 상태가 변합니다.
*   **구체적 객체(Concrete objects)**: 클래스 $C$의 인스턴스인 `CONC_1`에서 `CONC_2`로 구체적 동작 `cf`를 통해 상태가 변합니다.
*   **추상화 함수(Abstraction function)** $a$: 구체적인 상태(`CONC_1`, `CONC_2`)를 해당하는 추상적인 상태(`ABST_1`, `ABST_2`)로 매핑합니다.

구체적인 동작 `cf`가 추상적인 동작 `af`를 만족한다는 조건은 다음 수식으로 표현됩니다:
$$ a ; af = cf ; a $$
이 수식은 **추상화와 연산의 교환성(Commutativity of Abstraction and Operation)**을 나타냅니다.
*   좌변 ($a ; af$): 구체적 상태에 추상화 함수 $a$를 적용하여 추상 상태로 만든 후, 추상적 동작 $af$를 수행합니다.
*   우변 ($cf ; a$): 구체적 상태에 구체적 동작 $cf$를 수행하여 구체적 상태를 변경한 후, 추상화 함수 $a$를 적용하여 추상 상태로 만듭니다.
이 두 결과가 동일해야 한다는 것은, 어떤 작업을 수행할 때 추상적인 관점에서 보든 구체적인 관점에서 보든 최종적인 추상적 결과는 동일해야 한다는 의미입니다.

**구체적 예시**:
스택(Stack)의 `push` 메서드를 예로 들어봅시다.
*   **구체적 상태**: `CONC_1`은 내부적으로 배열과 `top` 포인터로 구현된 스택의 특정 상태(예: `[1, 2, _, _], top=2`)를 나타냅니다. 여기에 구체적 동작 `cf` (배열에 새 원소를 추가하고 `top`을 증가)를 수행하면 `CONC_2` (예: `[1, 2, 3, _], top=3`)가 됩니다.
*   **추상적 상태**: `ABST_1`은 추상적 관점에서 본 스택의 상태(예: `[1, 2]`)입니다. 여기에 추상화 함수 $a$를 적용하면 `ABST_1`이 나옵니다.
*   **추상적 동작**: `ABST_1`에 추상적 동작 `af` (리스트에 원소 추가)를 수행하면 `ABST_2` (예: `[1, 2, 3]`)가 됩니다.
이때, $a ; af = cf ; a$가 성립해야 스택의 `push` 구현이 명세에 부합한다고 할 수 있습니다. 즉, 구체적인 배열 조작 후 추상화했을 때의 결과($cf ; a$)와, 먼저 추상화한 후 추상적인 스택 연산을 수행한 결과($a ; af$)가 같아야 합니다.

**강의 맥락**:
교수님은 이 슬라이드를 통해 클래스 명세와 구현 간의 중요한 관계를 설명합니다. 실제 컴퓨터가 바이너리 레벨에서 작동하지만 프로그래머가 고수준 언어를 사용하는 것과 같이, 소프트웨어에는 '내부 구현 레벨에서의 상태 변화'와 '사용자가 인지하는 추상화 레벨에서의 상태 변화'라는 두 가지 상태 변화가 존재한다고 강조했습니다.
이 다이어그램은 이러한 두 레벨의 관계를 나타내며, 특히 "어떤 구체적인 행동이라도 명세에 의해 시뮬레이션(simulate)되거나 모방(mimic)되어야 한다"는 것이 핵심 원칙이라고 설명했습니다. 이 조건이 충족되면 사용자는 구체적인 구현의 세부사항을 알 필요 없이 추상적인 명세만으로 프로그램의 동작을 정확하게 추론할 수 있게 됩니다. 이는 객체 지향 시스템의 '추상화' 개념이 성공적으로 작동하기 위한 필수 조건입니다.

**시험 포인트**:
*   ⭐**`a ; af = cf ; a` 수식의 의미와 이것이 구현이 명세에 부합하는지(Implementation Meets Specification)를 어떻게 나타내는지 정확히 이해해야 합니다.**
*   ⭐추상화 함수 ($a$), 추상적 동작 ($af$), 구체적 동작 ($cf$)의 역할을 명확히 설명할 수 있어야 합니다.
*   ⭐**구체적인 구현의 동작이 추상적인 명세의 동작을 '시뮬레이션(simulate)'해야 한다는 개념을 이해하고 설명할 수 있어야 합니다.**

---

## Slide 24

### 핵심 개념
이 슬라이드는 `ArrayStack` 예시를 통해 클래스의 **명세(Specification)**와 **구현(Implementation)** 간의 관계, 특히 **추상화(Abstraction)**의 개념을 설명합니다. 사용자 관점의 **추상적 값(Abstract Values)**과 구현자 관점의 **구체적 값(Concrete Values)**이 존재하며, 이 둘은 **추상화 함수(Abstraction Function)**를 통해 연결됩니다. 클래스 메서드(예: `push`, `pop`)는 두 수준에서 모두 상태 변화를 일으키지만, 추상적 상태 변화가 구체적 상태 변화를 충실히 **시뮬레이션**해야 합니다.

### 코드/수식 해설

#### 코드 예시
다음 C++/Java 유사 코드는 `ArrayStack` 객체를 생성하고 몇 가지 스택 연산을 수행하는 과정을 보여줍니다.
```cpp
ArrayStack stack = new ArrayStack(3); // 크기가 3인 스택 생성
stack.push("A"); // "A" 푸시
stack.push("B"); // "B" 푸시
stack.pop();     // 팝 연산
```
-   `ArrayStack(3)`: 내부적으로 크기 3의 배열로 스택을 구현합니다.
-   `push("A")`, `push("B")`: 스택에 요소를 추가합니다.
-   `pop()`: 스택의 최상단 요소를 제거합니다.

#### 상태 변화 다이어그램
슬라이드의 다이어그램은 `push` 및 `pop` 연산에 따른 추상적 상태와 구체적 상태의 변화를 시각적으로 보여줍니다.

**구체적 상태 (Implementation Level):**
`array`와 `top` 변수로 표현됩니다.
-   `array`: 실제 데이터를 저장하는 배열.
-   `top`: 스택의 최상단(다음 요소가 들어갈 위치 또는 실제 요소의 개수)을 가리키는 인덱스입니다.

**추상적 상태 (Specification/User Level):**
사용자가 인지하는 스택의 논리적인 상태, 즉 요소들의 리스트(`[]`, `["A"]`, `["A", "B"]`, `["A"]`)로 표현됩니다.

**Abstraction 화살표:**
`Abstraction` 화살표는 구체적 상태(`array`, `top`)가 어떻게 추상적 상태(리스트)로 매핑되는지를 나타내는 **추상화 함수**를 의미합니다. 예를 들어, `array = [A, B, _]`이고 `top = 2`인 구체적 상태는 추상적으로 `["A", "B"]` 리스트로 해석됩니다.

#### 명세와 구현의 관계
강의에서는 이 관계를 다음과 같이 표현할 수 있다고 설명합니다.
`Abstraction(ConcreteState_initial) -> AbstractBehavior -> Abstraction(ConcreteState_final)`
이는 구체적 상태가 추상화 함수를 통해 추상적 상태로 변환된 후 추상적 동작을 수행하고, 이 결과가 다시 추상화 함수를 통해 최종 구체적 상태로 매핑된 것과 일치해야 함을 의미합니다.

### 강의 맥락
교수님은 이 슬라이드를 통해 객체지향 프로그래밍에서 클래스 명세의 핵심 부분을 설명합니다. 클래스 명세는 각 메서드에 대한 전제 조건(Precondition)과 후속 조건(Postcondition) 외에, 사용자가 알아야 할 내부 상태의 **추상적 표현(Abstract Representation)** 또는 **추상적 값(Abstract Values)**, 그리고 **클래스 불변식(Class Invariant)**을 포함한다고 강조했습니다.

특히 이 슬라이드는 구현자 측면에서 추가적인 고려사항을 다룹니다. 구현 시에는 구체적인 **표현(Concrete Representation)**이 필요하며, 슬라이드의 `array`와 `top`이 이에 해당합니다. 이 구체적 값과 추상적 값 사이의 관계는 **추상화 함수(Abstraction Function)**에 의해 정의됩니다. 또한, 구체적 표현이 만족해야 하는 추가적인 제약 조건이 있는데, 이를 **표현 불변식(Representation Invariant)**이라고 합니다. 예를 들어, `top`이 음수이거나 배열 크기보다 클 수 없다는 조건이 있습니다.

교수님은 스택의 `push`와 `pop` 연산을 예로 들며, 실제 구현 레벨의 상태 변화(구체적 상태)와 사용자 레벨의 상태 변화(추상적 상태)가 모두 존재함을 설명했습니다. 이 두 수준의 상태 변화는 마치 컴퓨터가 이진 수준에서 동작하지만 우리는 추상적인 프로그래밍 언어를 사용하는 것과 같다고 비유했습니다. 중요한 것은 **어떤 구체적 동작도 추상적 명세의 동작에 의해 '시뮬레이션'되어야 한다**는 원칙입니다. 즉, 사용자는 구체적인 구현을 알 필요 없이 추상적인 동작만으로도 전체 소프트웨어의 동작을 추론할 수 있어야 하며, 이는 추상적 동작이 내부 동작을 충실히 반영하기 때문입니다.

### 시험 포인트
*   **추상화 함수(Abstraction Function)**의 정의와 역할 ⭐: 구체적 값을 추상적 값으로 매핑하는 함수.
*   **추상적 값(Abstract Values)**과 **구체적 값(Concrete Values)**의 차이 및 예시 ⭐: 사용자 관점과 구현자 관점의 상태 표현.
*   클래스 명세와 구현 간의 **시뮬레이션 원칙** ⭐: 추상적 동작이 구체적 동작을 충실히 반영해야 한다는 원칙.

---

## Slide 25

**핵심 개념**
*   **CharSet**: 문자(character)들의 집합을 나타내는 클래스입니다. 일반적으로 집합은 원소의 순서가 중요하지 않으므로, 추상적으로는 단순히 어떤 문자들이 포함되어 있는지만 중요합니다.
*   **`move-to-front optimization`**: 이 최적화는 `CharSet`의 `member()`와 같은 검색 연산의 성능을 향상시키기 위한 내부 구현 기법입니다. 특정 원소가 `member()` 호출을 통해 접근되면, 해당 원소를 내부적으로 저장된 데이터 구조(예: 연결 리스트나 배열)의 맨 앞으로 옮겨 다음 번 접근 시 더 빠르게 찾을 수 있도록 합니다. 이 과정에서 집합의 **추상적인 내용(어떤 문자가 포함되어 있는지)**은 변경되지 않지만, **구체적인 내부 표현(원소들의 순서)**은 변경됩니다.

**코드/수식 해설**

```java
1 CharSet cset = new CharSet();
2 cset.insert('A');
3 cset.insert('B');
4 cset.insert('C');
5 cset.member('B'); // move-to-front optimization version
```
이 코드는 `CharSet` 객체 `cset`을 생성하고 'A', 'B', 'C' 문자를 삽입한 후, 'B' 문자가 집합에 포함되어 있는지(`member('B')`) 확인하는 과정을 보여줍니다. `move-to-front optimization`이 적용된 버전이라고 주석에 명시되어 있습니다.

**구체적 예시**
`CharSet`의 내부 구현이 연결 리스트라고 가정했을 때:
1.  `new CharSet()`: `cset`은 비어있는 리스트 `[]`가 됩니다.
2.  `cset.insert('A')`: `cset`은 `['A']`가 됩니다.
3.  `cset.insert('B')`: `cset`은 `['A', 'B']`가 됩니다.
4.  `cset.insert('C')`: `cset`은 `['A', 'B', 'C']`가 됩니다. (순서는 구현에 따라 다를 수 있지만, 예시를 위해 가정)
5.  `cset.member('B')`: 이 호출은 'B'가 집합에 있는지 확인합니다. 'B'를 찾았다면, `move-to-front optimization`에 따라 'B'를 리스트의 맨 앞으로 이동시킵니다. 따라서 `cset`의 내부 상태는 `['B', 'A', 'C']`로 변경될 수 있습니다.

**강의 맥락**
교수님은 이 슬라이드를 "Another example"로 잠시 언급했으나, 제공된 음성 전사에서는 이 예시에 대한 구체적인 설명이 상세하게 이어지지 않았습니다. 그러나 이전 강의 내용과 종합해 볼 때, 이 예시는 다음의 핵심 개념들을 설명하기 위해 사용될 수 있습니다:
*   **추상 명세와 구체 구현의 분리**: `CharSet`의 추상적인 명세는 단순히 "어떤 문자들이 집합에 포함되어 있는가"입니다. `move-to-front optimization`은 이 추상적인 명세를 변경하지 않으면서도, 내부적인 구체 구현(원소의 순서)을 변경하여 성능을 최적화하는 방법을 보여줍니다.
*   **관찰 불가능한 상태 변경**: `cset.member('B')` 호출은 'B'가 집합에 있다는 사실을 반환하며, 이는 집합의 추상적인 상태를 변경하지 않습니다. 하지만 내부적으로 `move-to-front optimization`이 동작하여 원소들의 순서가 변경되는 것은 클라이언트에게는 관찰되지 않는 구체 상태의 변경입니다.
*   **추상화 함수**: 이 예시는 구체적인 내부 표현(예: `['A', 'B', 'C']`와 `['B', 'A', 'C']`)이 다를 수 있음에도 불구하고, 동일한 추상적 값(집합 $\{'A', 'B', 'C'\}$)을 나타낼 수 있다는 추상화 함수 ($AF$)의 개념을 잘 보여줍니다.

**시험 포인트**
*   ⭐**추상 상태와 구체 상태**: `move-to-front optimization`과 같이 내부 구현에 따른 성능 최적화가 **추상적인 명세에 영향을 미치지 않으면서 구체적인 상태를 변경**하는 방식의 중요성을 이해해야 합니다. 이는 객체의 **관찰 가능한 행동(observable behavior)**과 **내부 구현(internal implementation)**을 분리하는 핵심 개념입니다.
*   ⭐**추상화 함수 ($AF$)**: 여러 구체 상태($C_1, C_2, \dots$)가 동일한 추상 상태($A$)에 매핑될 수 있다는 점($AF(C_1) = A$, $AF(C_2) = A$)을 이 예시를 통해 설명할 수 있어야 합니다.
*   ⭐**캡슐화와 추상화**: 객체 지향에서 캡슐화가 어떻게 내부 구현의 세부 사항을 숨기고, 클라이언트가 추상적인 명세에만 의존하여 객체를 사용할 수 있도록 하는지 설명할 때 이러한 최적화 예시가 활용될 수 있습니다.

---

## Slide 26

**핵심 개념**:
Representation Exposure (표현 노출)은 객체의 내부 상태(표현)가 외부에 직접 접근되거나 수정될 수 있도록 노출되는 상황을 의미합니다. 일반적으로 클래스의 멤버 변수는 `private`으로 선언하여 외부 접근을 제한하지만, 내부 객체에 대한 참조를 반환하는 메서드를 통해 여전히 내부 상태가 노출될 수 있습니다.

**코드/수식 해설**:

```java
class ArrayStack implements Stack {
    // ...
    // private Object[] array; // 내부 배열은 private으로 선언되어 있을 것임
    // private int top; // 스택의 상단을 가리키는 변수
    // ...

    // getElements() 메서드는 내부 배열 'array'의 참조를 직접 반환합니다.
    Object[] getElements() { return array; } 

    // ...
}
```
위 `ArrayStack` 클래스의 `getElements()` 메서드는 내부적으로 스택 요소를 저장하는 `array` 배열의 참조를 외부로 반환합니다.

```java
ArrayStack stack = new ArrayStack(10); // ArrayStack 객체 생성
stack.push(1); // 1을 스택에 추가
stack.getElements()[0] = null; // getElements()로 얻은 참조를 통해 내부 배열의 첫 번째 요소 직접 수정
System.out.println(stack.pop()); // 스택에서 요소를 팝
```
이 클라이언트 코드는 `getElements()` 메서드를 통해 `ArrayStack` 객체의 내부 `array`에 대한 참조를 얻은 후, `stack.getElements()[0] = null;`와 같이 해당 배열의 내용을 직접 수정합니다. 이는 `private`으로 선언된 내부 상태를 우회하여 변경하는 것으로, 클래스 내부의 불변식(Class Invariant)을 깨뜨릴 위험이 있습니다.

**구체적 예시**:
위 코드 예시는 `ArrayStack`의 `getElements()` 메서드가 내부 `array`의 참조를 반환함으로써 발생하는 표현 노출을 보여줍니다. 스택에 `1`을 `push`했지만, 외부에서 `getElements()`를 통해 얻은 배열의 첫 번째 요소를 `null`로 직접 변경했습니다. 이후 `pop()`을 호출하면 `null`이 반환되거나, 스택의 불변식이 깨져 예상치 못한 오류가 발생할 수 있습니다. 예를 들어, 스택에 `1`이 들어있어야 하지만 실제로는 `null`이 되어버리는 상황입니다.

**강의 맥락**:
교수님께서는 프로그램에서 오류가 발생했을 때 클래스 불변식이 위반될 수 있는 흔한 원인 중 하나로 표현 노출을 언급하셨습니다. 특히, 멤버 변수가 `private`으로 선언되어 있어도, `getElements()`와 같이 내부 상태를 직접 반환하는 "getter" 메서드를 통해 참조를 노출하면 문제가 발생할 수 있음을 강조하셨습니다. 처음에는 `private` 변수이므로 문제가 없을 것처럼 보이지만, 사실상 모든 프로그래밍 언어에서 `private` 멤버 변수의 참조를 반환하는 것이 가능하며, 이를 통해 외부 사용자가 내부 표현을 쉽게 수정할 수 있다고 설명하셨습니다.

이는 마치 "해커"가 클래스 내부의 모든 것을 수정할 수 있게 되어 클래스 불변식이 깨질 수 있는 상황과 같다고 비유하며, 클래스를 설계하고 구현할 때 이러한 표현 노출을 피해야 한다고 말씀하셨습니다. 또한, 단순히 모든 멤버 변수를 `private`으로 선언하는 것만으로는 이러한 문제가 해결되지 않으며, 이는 좋은 습관이지만 충분하지 않다고 강조하셨습니다.

**시험 포인트**:
*   ⭐ **Representation Exposure의 개념과 발생 원인**: `private` 멤버 변수라도, 해당 변수에 대한 참조를 직접 반환하는 `getter` 메서드 등을 통해 내부 상태가 외부에 노출되어 수정될 수 있음을 이해해야 합니다.
*   ⭐ **클래스 불변식(Class Invariant) 위반 가능성**: 표현 노출이 발생할 경우, 외부에서 내부 상태를 임의로 조작하여 클래스의 핵심적인 속성이나 조건을 깨뜨릴 수 있다는 점을 알아야 합니다.
*   ⭐ **`private` 접근 제어자의 한계**: `private` 키워드가 내부 상태를 보호하는 데 필수적이지만, 참조 반환을 통한 표현 노출을 완전히 막을 수는 없다는 점을 인지해야 합니다.

---

## Slide 27

**핵심 개념**:
Representation Exposure(표현 노출)는 클래스의 내부 구현(concrete representation)이 외부로 노출되어, 클래스 인variant(불변식)나 객체의 추상적인 상태가 외부에서 의도치 않게 변경될 수 있는 문제를 의미합니다. 멤버 변수를 `private`으로 선언하는 것만으로는 이러한 문제를 완전히 해결할 수 없습니다.

**코드/수식 해설**:
(해당 없음)

**구체적 예시**:
`ArrayStack` 클래스에서 내부 배열을 직접 반환하는 `getElements()`와 같은 메서드가 있다면, 외부에서 반환된 배열의 요소를 직접 수정하여 스택의 내부 상태(예: `top` 인덱스와 배열 내용의 불일치)를 망가뜨릴 수 있습니다.
```cpp
class ArrayStack {
private:
    int* elements; // 내부 배열
    int top;
    int capacity;
public:
    // ... (생성자, push, pop 등)

    // 문제의 소지가 있는 메서드 (representation exposure)
    int* getElements() { // 또는 std::vector<int>& getElements()
        return elements; // 내부 배열의 직접 참조를 반환
    }
};

// 외부 코드에서
ArrayStack stack;
stack.push(1);
int* internalArray = stack.getElements(); // 내부 배열의 참조 획득
internalArray[0] = 99; // 내부 상태를 직접 수정하여 클래스 불변식 위반 가능성 발생
```

**강의 맥락**:
교수님은 클래스 내부 상태의 "표현 노출(representation exposure)" 문제를 강조하며, 이는 개발자의 실수나 악의적인 시도로 인해 클래스 불변식(class invariant)이 위반될 수 있는 흔한 원인이라고 설명합니다. 특히, 멤버 변수를 `private`으로 선언하는 것이 중요하지만, 이것만으로는 **충분하지 않다(`Not enough`)**고 지적했습니다. 이전 슬라이드의 `ArrayStack` 예시에서 `getElements()`와 같이 내부 표현(예: 배열)의 참조를 반환하는 메서드가 있을 경우, 외부 사용자가 이 참조를 통해 클래스의 `private` 멤버 변수에 직접 접근하여 내부 상태를 변경할 수 있다고 설명했습니다. 이는 클래스의 캡슐화를 깨뜨리고 예상치 못한 버그를 유발할 수 있습니다. 예를 들어, 스택에 1을 push 한 후 `getElements()[0]`을 99로 변경하면 스택의 논리적 상태가 `top`과 불일치하게 되어 올바른 동작을 기대할 수 없게 됩니다.

**시험 포인트**:
⭐`private` 접근 제한자가 `Representation Exposure`를 완전히 막을 수 없는 이유를 설명하고, 그 예시(`getElements()`와 같은 메서드가 내부 표현의 참조를 반환하는 경우)를 제시할 수 있어야 합니다.
⭐객체지향 설계에서 `Representation Exposure`가 왜 문제이며, 이를 피하는 것이 중요한 이유를 이해해야 합니다.

---

## Slide 28

**핵심 개념**:
`final` 키워드는 변수가 단 한 번만 할당될 수 있음을 나타내어, 참조 변수의 재할당이나 원시 타입 값의 변경을 방지합니다. 하지만 `final`로 선언된 참조 변수가 가리키는 객체의 내부 상태 변경은 막지 못하므로, 표현 노출(Representation Exposure)을 완전히 피하기에는 충분하지 않습니다. ⭐

**코드 해설**:
`final` 키워드의 동작 방식을 보여주는 예시입니다.

```java
final int x = 1;
final StringBuilder y = new StringBuilder();

x = 2; // 컴파일 타임 에러 발생. final 원시 변수 x는 재할당될 수 없습니다.
y = new StringBuilder(100); // 컴파일 타임 에러 발생. final 참조 변수 y는 다른 객체를 참조하도록 재할당될 수 없습니다.

y.append('a'); // 허용됨: final 변수 y가 참조하는 StringBuilder 객체의 내부 상태를 수정하는 것은 가능합니다.
System.out.println(y); // output: a
```
위 예시에서 `y`는 `final`이지만, `y`가 참조하는 `StringBuilder` 객체의 내부 메서드인 `append('a')`를 통해 객체의 상태는 변경될 수 있습니다.

**강의 맥락**:
교수님은 클래스 설계 시 `private` 접근 제한자를 사용하는 것이 중요하다고 강조하면서도, 이것만으로는 표현 노출을 완전히 막을 수 없다고 설명했습니다. 그 다음으로 `final` 키워드를 언급하며, Java에서 `final`은 변수가 한 번만 할당될 수 있음을 의미하며, C++의 `const`와 유사하다고 설명했습니다.

슬라이드의 예시 코드를 통해 `final int x`와 `final StringBuilder y` 변수에 대한 재할당이 컴파일 에러를 발생시키는 것을 보여주었지만, `y.append('a')`와 같이 `final` 객체의 내부 상태를 변경하는 메서드 호출은 허용된다는 점을 명확히 지적했습니다. 이를 통해 `final`이 유용하지만, 내부 표현의 변경을 완전히 막는 데는 한계가 있으며, 따라서 표현 노출 문제를 해결하기에는 `final`만으로는 부족하다는 점을 강조했습니다. ⭐

**시험 포인트**:
*   `final` 키워드가 참조 변수의 "재할당"은 막지만, 참조하는 "객체의 내부 상태 변경"은 허용한다는 점을 이해하는 것이 중요합니다. ⭐
*   `private`과 `final` 키워드만으로는 표현 노출을 완전히 방지할 수 없으며, 추가적인 대책(예: 불변(immutable) 객체 사용)이 필요하다는 점을 기억하세요. ⭐

---

## Slide 29

---

### 핵심 개념

표현 노출(Representation Exposure)을 방지하는 효과적인 방법 중 하나는 **불변 객체(Immutable objects)**를 사용하는 것입니다. 불변 객체는 생성된 이후에는 그 상태를 변경할 수 없는 객체를 의미합니다.

*   **설계 원칙**: 불변 객체의 연산(operations)은 기존 객체를 변경하는 대신 항상 **새로운 객체를 반환**합니다 (생산자(producer) 역할).
*   **장점**:
    *   표현 노출을 원천적으로 차단하여 표현 불변식(representation invariants)이 깨질 위험이 없습니다.
    *   ⭐ **안전한 공유(Safe sharing)**: 여러 스레드(thread)에서 동시에 접근해도 경합 조건(race condition) 문제가 발생하지 않아 멀티스레드 환경에서 안전합니다.
    *   코드 추론을 단순화하고 디버깅을 용이하게 합니다.
*   **단점/고려사항**: 모든 것을 불변으로 만드는 것은 때로는 프로그래밍을 더 복잡하게 하거나 성능에 영향을 줄 수 있습니다. 하지만 가능한 한 불변 객체를 사용하는 것이 권장됩니다.

### 코드/수식 해설

*   **`final` 키워드의 한계**: Java의 `final` 키워드나 C++의 `const`는 변수(`x`)나 참조(`y`)가 한 번 할당된 후 재할당될 수 없도록 하지만, 해당 참조가 가리키는 **객체 내부의 상태까지 변경 불가능하게 만드는 것은 아닙니다.** 즉, `final`로 선언된 객체 참조 `y`라도 `y.append(a)`와 같이 내부 상태를 변경하는 메서드를 호출할 수 있다면 여전히 표현 노출의 위험이 있습니다.

### 구체적 예시

Java 표준 라이브러리에는 이미 여러 불변 클래스들이 존재합니다:
*   `String`: 문자열은 한 번 생성되면 변경할 수 없습니다. 문자열을 조작하는 모든 메서드는 새로운 `String` 객체를 반환합니다.
*   `Character`, `Integer`, `Double`: 원시 타입(primitive types)의 래퍼(wrapper) 클래스들은 모두 불변 객체입니다.
*   `BigNumber` (정확히는 `BigInteger`와 `BigDecimal`): 큰 숫자들을 다루는 클래스 역시 불변입니다.

### 강의 맥락

교수님은 앞선 강의에서 `private` 접근 제한자를 사용하고 내부 배열의 복사본을 반환하는 대신 참조를 반환하는 `getter` 메서드가 어떻게 클래스의 표현 불변식을 깨뜨릴 수 있는지 설명했습니다. 이 슬라이드에서는 이러한 **표현 노출(representation exposure) 문제를 근본적으로 해결하기 위한 "더 완전한(more complete)" 방법으로 불변 객체**를 소개합니다.

*   `private` 필드와 `final` 키워드만으로는 내부 표현을 완벽하게 보호하기 어렵다는 점을 지적하며, 특히 `final`은 참조 자체의 변경을 막을 뿐, 참조가 가리키는 객체 내부 상태의 변경은 막지 못한다고 강조했습니다.
*   불변 객체는 일단 생성되면 상태를 변경할 수 없으므로, 내부 표현을 외부에 노출하더라도 **외부 사용자가 객체의 상태를 임의로 변경하여 클래스 불변식을 위반할 수 없다**는 핵심적인 장점을 설명합니다.
*   불변 객체를 사용하면 ⭐ **동시성 프로그래밍(concurrent programming)에서 스레드 안전성(thread-safety)을 확보**할 수 있어 경합 조건과 같은 복잡한 버그를 방지할 수 있다고 강조했습니다. 또한, ⭐ **코드 공유 및 추론이 단순해진다**는 점도 중요한 이점으로 언급했습니다.
*   일부 프로그래밍 방식에서는 "가치 지향 프로그래밍(value-oriented programming)"이라 부르며 불변 객체 사용을 적극 권장하기도 한다고 언급했습니다.
*   모든 것을 불변으로 만드는 것이 항상 쉬운 것은 아니며 성능이나 설계 복잡성 측면에서 트레이드오프가 있을 수 있지만, 특별한 이유가 없다면 **보안상의 이점 때문에 불변 객체를 선택하는 것이 더 좋은 관행**이라고 결론지었습니다.

### 시험 포인트

*   ⭐ **표현 노출을 피하기 위한 `private`, `final` 키워드의 한계점을 설명하고, 불변 객체가 왜 더 근본적인 해결책이 되는지 설명하시오.**
*   ⭐ **불변 객체(Immutable Objects)의 정의와 주요 특징(생성 후 상태 변경 불가, 연산 시 새 객체 반환 등)을 설명하고, 멀티스레드 환경에서 불변 객체가 가지는 이점(스레드 안전성, 경합 조건 방지)을 서술하시오.**
*   ⭐ **Java에서 `String`, `Integer`와 같은 내장 클래스들이 불변 객체인 이유와 그 장점을 설명하시오.**

---

---

## Slide 30

### 핵심 개념
내부 구현의 노출(Representation Exposure)을 방지하는 방법으로 불변 객체(Immutable Object)를 활용하는 여러 기법을 다룹니다. 이는 클래스 불변식(Class Invariant)이 외부에서 예기치 않게 깨지는 것을 막아 소프트웨어의 안정성과 예측 가능성을 높이는 데 필수적입니다.

### 코드/수식 해설
슬라이드의 예시 코드는 내부 `array`를 직접 반환하는 대신 `List.of()`를 사용하여 불변 리스트로 감싸서 반환함으로써 내부 상태 노출을 방지합니다.

```java
class ArrayStack implements Stack {
    // ...
    List getElements() { 
        return List.of(array); 
    }
    // ...
}
```
*   `List.of(array)`: Java 9부터 도입된 정적 팩토리 메서드로, 주어진 요소들로 구성된 불변(`immutable`) 리스트를 생성하여 반환합니다. 이 리스트는 요소를 추가, 삭제, 수정할 수 없으며, 시도할 경우 `UnsupportedOperationException`이 발생합니다.

### 강의 맥락
교수님은 지난 시간에 다룬 "표현 노출(Representation Exposure) 문제"를 다시 상기시키며, `private` 선언만으로는 부족하다고 강조합니다. 내부 배열을 직접 반환하는 `getElementRentArray`와 같은 게터(getter) 메서드가 있을 경우, 외부에서 내부 상태를 직접 수정하여 클래스 불변식을 쉽게 위반할 수 있기 때문입니다. 이를 피하기 위한 효과적인 방법들을 설명합니다.

1.  **불변 컨테이너(Immutable containers)**:
    *   Java 9+에서 도입된 `List.of(...)`, `Set.of(...)`, `Map.of(...)`와 같은 메서드를 사용하여 불변 컬렉션을 생성하는 방법입니다. 교수님은 이전 예시에서 내부 `array`를 직접 반환하는 대신 `List.of(array)`를 반환하는 것이 더 나은 구현이라고 설명합니다.
    *   ⭐**강조**: `List.of()`로 생성된 리스트는 요소를 추가하거나 제거할 수 없으므로, 외부에서 내부 배열을 직접 변경하는 것을 막을 수 있습니다.

2.  **불변 래퍼(Immutable wrappers)**:
    *   `Collections.unmodifiableList(...)`, `Collections.unmodifiableSet(...)` 등 `java.util.Collections` 클래스가 제공하는 `unmodifiable` 래퍼 메서드를 사용하는 방법입니다. 이 메서드들은 기존 컬렉션의 "읽기 전용 뷰(read-only view)"를 반환합니다.
    *   교수님은 `Collections.unmodifiableList()`의 경우 리스트에 요소를 추가하려 하면 예외가 발생하여 "진정한 불변(real immutable)"처럼 작동한다고 설명합니다.
    *   ⭐**주의점**: `unmodifiable` 래퍼는 반환된 래퍼 객체를 통해 원본 컬렉션을 수정할 수 없게 하지만, 만약 원본 컬렉션이 외부에서 수정되면 래퍼를 통해 보이는 내용도 함께 변경됩니다. 또한, 리스트 내의 요소 자체가 가변(mutable) 객체라면, 그 객체의 내부 상태는 여전히 변경될 수 있습니다.

3.  **Records 사용**:
    *   교수님은 Java Records가 불변 객체를 선언하는 데 매우 유용하다고 설명합니다. Records는 간결한 문법으로 불변 데이터를 표현하며, 자동으로 `private` 필드와 해당 필드의 `public accessor`(getter)를 생성하고, `equals()`, `hashCode()`, `toString()` 메서드를 오버라이드합니다.
    *   ⭐**핵심**: Records는 기본적으로 불변 객체로 설계되어 있어, 표현 노출을 피하는 좋은 방법 중 하나입니다. 코드의 양을 획기적으로 줄이면서 안전한 데이터 클래스를 정의할 수 있습니다.

교수님은 어떤 프로그래밍 언어에서든 가변(mutable) 데이터 타입을 최소화하고 불변(immutable) 데이터 타입을 최대한 활용하는 것이 잠재적인 보안 취약점이나 디버깅하기 어려운 버그를 피하는 데 매우 중요하다고 강조합니다. 표현 노출을 막기 위한 방법으로 "모든 멤버 변수를 `private`으로 선언하고, `final` 키워드를 최대한 사용하며, 불변 레코드와 데이터 타입을 활용하는 것"을 재차 언급합니다.

### 시험 포인트
*   ⭐**표현 노출(Representation Exposure)의 개념과 왜 피해야 하는지** 설명할 수 있어야 합니다.
*   ⭐`private` 접근 제어자만으로는 표현 노출을 완전히 막을 수 없는 이유를 이해해야 합니다.
*   ⭐**표현 노출을 피하기 위한 주요 기법**:
    *   **불변 컨테이너 (예: `List.of()`, `Set.of()`)**
    *   **불변 래퍼 (예: `Collections.unmodifiableList()`)**
    *   **Java Records**
    각 기법의 특징과 `List.of(array)`와 같은 구체적인 코드 예시를 통해 설명할 수 있어야 합니다.
*   ⭐불변 래퍼(`Collections.unmodifiableList()`)의 한계점 (원본 컬렉션의 변경에는 취약하며, 컬렉션 내부 요소가 가변 객체일 경우 해당 객체의 상태는 변경될 수 있음)을 이해하는 것이 중요합니다.

---

## Slide 31

## Records and Pattern Matching

### 핵심 개념
*   **Java Records**: Java 16에 도입된 특별한 종류의 클래스로, 데이터 홀더 역할을 하는 불변(immutable) 객체를 간결하게 선언하는 데 사용됩니다. 필드, 생성자, 접근자(getter), `equals()`, `hashCode()`, `toString()` 메서드를 컴파일러가 자동으로 생성해줍니다.
*   **Pattern Matching**: 객체의 타입 검사(`instanceof`)와 변수 바인딩을 한 번에 처리하여 조건문을 간결하고 가독성 높게 작성할 수 있게 해주는 기능입니다. 특히 `record`와 함께 사용될 때 강력한 시너지를 발휘하며, `if`문과 `switch` 표현식에서 활용될 수 있습니다.

### 코드/수식 해설
**1. Record 선언:**
레코드는 매우 간결한 구문으로 선언할 수 있습니다.
```java
public record Point(int x, int y) {
    // 추가 메서드나 검증 로직을 자유롭게 추가할 수 있습니다.
    // 예를 들어, x와 y가 양수인지 검증하는 compact constructor를 추가할 수 있습니다.
    public Point {
        if (x < 0 || y < 0) {
            throw new IllegalArgumentException("Coordinates must be positive");
        }
    }
}
```
위 `Point` 레코드는 다음과 같은 요소를 자동으로 생성합니다:
*   `private final int x;`
*   `private final int y;`
*   `public Point(int x, int y)` (생성자)
*   `public int x()` (접근자, getter)
*   `public int y()` (접근자, getter)
*   `equals()`, `hashCode()`, `toString()` 메서드

**2. `instanceof`를 사용한 패턴 매칭:**
Java 16부터 `instanceof` 연산자와 함께 타입 패턴을 사용하여 객체의 타입 확인과 동시에 변수를 선언하고 할당할 수 있습니다.
```java
interface Shape {}
record Rectangle(double length, double width) implements Shape {}
record Circle(double radius) implements Shape {}

public void processShape(Shape shape) {
    if (shape instanceof Rectangle r) {
        // shape가 Rectangle 타입이면 자동으로 r 변수에 캐스팅되어 바인딩됩니다.
        System.out.println("Rectangle area: " + (r.length() * r.width()));
    } else if (shape instanceof Circle c) {
        // shape가 Circle 타입이면 자동으로 c 변수에 캐스팅되어 바인딩됩니다.
        System.out.println("Circle area: " + (Math.PI * c.radius() * c.radius()));
    }
}
```
**3. `switch` 표현식을 사용한 패턴 매칭:**
Java 17부터 `switch` 표현식도 패턴 매칭을 지원하여, 여러 타입에 대한 처리를 더욱 간결하게 할 수 있습니다.
```java
public double calculateArea(Shape s) {
    return switch (s) {
        case Rectangle r -> r.length() * r.width();
        case Circle c -> Math.PI * c.radius() * c.radius();
        // sealed interface가 아니거나 모든 경우를 커버하지 않으면 default 케이스가 필요합니다.
        default -> throw new IllegalArgumentException("Unknown shape: " + s);
    };
}
```

### 구체적 예시
`record Rectangle(double length, double width)`를 선언하고 이를 사용하는 예시입니다.
```java
record Rectangle(double length, double width) {
    // 추가 메서드: 면적 계산
    public double area() {
        return length * width;
    }
}

public class Example {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(4, 5); // Rectangle 객체 생성
        System.out.println("Length: " + rect.length()); // Getter 사용
        System.out.println("Width: " + rect.width());   // Getter 사용
        System.out.println("Area: " + rect.area());     // 추가 메서드 사용
    }
}
```

### 강의 맥락
교수님은 Java의 `record` 기능을 소개하며, 이는 클래스 선언을 매우 간결하게 만들어주는 "문법적 설탕(syntactic sugar)"이라고 설명합니다. 특히 데이터 홀더 역할을 하는 클래스에 유용하며, 생성자, getter, `equals()`, `hashCode()`, `toString()`과 같은 상용구 코드를 자동으로 생성해주어 개발자가 핵심 로직에 집중할 수 있게 돕는다고 강조합니다.

더 나아가, `record`의 "가장 큰 장점"은 **패턴 매칭(Pattern Matching)**과의 시너지라고 역설합니다. `instanceof`와 `switch` 문에서 패턴 매칭을 활용하면, 특정 인터페이스를 구현하는 여러 레코드 클래스를 다룰 때 복잡한 `if-else if` 체인이나 명시적인 타입 캐스팅 없이도 깔끔하고 안전하게 코드를 작성할 수 있다고 설명합니다. 이를 통해 코드의 가독성이 크게 향상되고, 오류 발생 가능성이 줄어든다고 강조했습니다.

### 시험 포인트
*   ⭐**Java `record`의 특징과 장점**: 간결한 문법으로 불변 데이터 클래스를 선언하고, 필요한 기본 메서드(생성자, getter, `equals`, `hashCode`, `toString`)를 자동으로 생성하여 코드량을 줄이고 가독성을 높일 수 있다는 점을 이해해야 합니다.
*   ⭐**`record`와 패턴 매칭의 연계**: `record`가 `instanceof` 및 `switch` 패턴 매칭과 결합될 때 어떻게 코드의 복잡성을 줄이고 타입 안전성을 높이는지 그 활용법과 이점을 명확히 설명할 수 있어야 합니다. (예: `if (shape instanceof Rectangle r)` 또는 `switch (shape) { case Rectangle r -> ... }` 구문)

---

## Slide 32

### 핵심 개념
Java Records는 불변(immutable) 데이터 객체를 간결하게 선언하기 위한 `class`의 '문법적 설탕(syntactic sugar)'입니다. 주로 데이터를 저장하는 목적으로 사용되는 클래스(Data Transfer Object, DTO)의 작성을 크게 단순화합니다.

### 코드/수식 해설
`record` 키워드를 사용하여 필드와 그 타입을 괄호 안에 나열하는 것만으로 다음과 같은 기능들을 자동으로 제공하는 클래스가 생성됩니다.

```java
record Point(double x, double y) {}
```
위 코드는 다음과 같은 특징을 가진 `Point` 클래스를 자동으로 정의합니다:
*   `private` `final` 필드 `x`와 `y`를 가집니다. (불변 객체 특성)
*   모든 필드를 인자로 받는 `public` 생성자를 가집니다.
*   각 필드에 대한 `public` 접근자(getter) 메서드인 `x()`와 `y()`를 가집니다. (예: `pointInstance.x()`)
*   `toString()`, `equals()`, `hashCode()` 메서드가 자동으로 오버라이드됩니다.

### 구체적 예시
`Point(double x, double y)` 레코드 선언을 통해, 개발자는 필드 선언, 생성자, 접근자, `equals()`, `hashCode()`, `toString()`과 같은 상용구 코드(boilerplate code)를 직접 작성할 필요 없이 데이터 객체를 정의할 수 있습니다. 예를 들어, `Point p = new Point(10.0, 20.0);`와 같이 객체를 생성하고, `double px = p.x();`와 같이 값에 접근할 수 있습니다.

### 강의 맥락
교수님께서는 Java `record`가 "open immune target types" (불변 타입을 선언하는 유용한 방법)이라고 강조하며, `class`의 "syntactic show" (문법적 설탕)라고 설명하셨습니다. `record`를 사용하면 `Point` 예시처럼 두 멤버 변수 `x`와 `y`만으로 실제 `class Point`가 두 `private` 필드와 이 필드들을 초기화하는 생성자, 그리고 각 필드에 대한 `public` 접근자(getter) (`x()`, `y()`) 및 기타 유용한 보조 함수들을 자동으로 갖게 된다고 하셨습니다. 이를 통해 일반적인 클래스 선언에서 필요한 많은 "manualize" (수동 작업)를 피할 수 있다고 그 이점을 설명하셨습니다. 특히, `record`가 불변(immutable) 타입의 선언을 크게 단순화한다고 강조하셨습니다.

### 시험 포인트
*   Java Records의 정의와 목적 (불변 데이터 객체 선언 간소화) ⭐
*   `record` 선언 시 자동으로 생성되는 요소들 (private final 필드, 모든 필드를 인자로 받는 생성자, 필드에 대한 public 접근자, `toString()`, `equals()`, `hashCode()` 메서드 오버라이드) ⭐
*   `record`가 "syntactic sugar"인 이유와 그 이점 (상용구 코드 감소, 가독성 향상) ⭐

---

## Slide 33

### 핵심 개념
자바 `record`를 사용하여 데이터 클래스를 간결하게 정의하고, 기본으로 제공되는 접근자(accessor) 메서드 외에 사용자가 직접 커스텀 메서드를 추가할 수 있음을 보여주는 예시 슬라이드입니다. `record`는 내부적으로 private 필드와 public 접근자, 생성자 등을 자동으로 생성해주지만, 필요에 따라 이러한 기본 동작을 오버라이드하거나 추가 메서드를 정의하여 기능을 확장할 수 있습니다.

### 코드/수식 해설
```java
record Rectangle(double length, double width) {
    public double length() {
        System.out.println("Length is " + length);
        return length;
    }
}

Rectangle r = new Rectangle(4,5);
System.out.println("length: " + r.length() + " width: " + r.width());
```
*   `record Rectangle(double length, double width)`: `Rectangle` 레코드를 선언합니다. `length`와 `width`는 이 레코드의 컴포넌트이며, 자동으로 private 필드로 선언되고, 해당 필드를 초기화하는 생성자와 값을 반환하는 public 접근자 메서드(`length()`, `width()`)가 생성됩니다.
*   `public double length() { ... }`: 이 부분은 `Rectangle` 레코드의 `length` 컴포넌트에 대한 기본 접근자 메서드를 오버라이드한 것입니다. 이 커스텀 `length()` 메서드는 길이를 반환하기 전에 "Length is "와 길이를 콘솔에 출력하는 추가적인 동작을 수행합니다.
*   `Rectangle r = new Rectangle(4,5);`: `length`가 $4$, `width`가 $5$인 `Rectangle` 객체 `r`을 생성합니다.
*   `System.out.println("length: " + r.length() + " width: " + r.width());`: `r` 객체의 `length()` 메서드와 `width()` 메서드를 호출하여 길이를 출력합니다. 이때 `r.length()`는 위에 정의된 커스텀 메서드가 호출되어 콘솔에 "Length is 4.0"을 먼저 출력한 후 $4.0$을 반환하고, `r.width()`는 자동으로 생성된 접근자 메서드가 호출되어 $5.0$을 반환합니다. 따라서 최종 출력은 "length: 4.0 width: 5.0"이 됩니다 (첫 `r.length()` 호출 시의 추가 출력은 제외).

### 강의 맥락
교수님은 앞서 `record`가 `Point`와 같은 단순 데이터 타입을 선언할 때 생성자, private 필드, getter 등을 자동으로 만들어주어 코드를 크게 줄일 수 있다고 설명했습니다. 이 슬라이드에서는 `Rectangle` 레코드를 예로 들어, `record`가 자동으로 생성하는 기본 기능 외에 **사용자가 직접 메서드를 추가하거나 오버라이드할 수 있음**을 강조합니다. 특히 `length()`라는 추가 메서드를 정의하여 기본 `length` 접근자와는 다른 동작(출력)을 수행하도록 함으로써 `record`의 유연성을 보여줍니다. 교수님은 "you can also add additional methods as well so this rectangle has an additional method length that will return to the length", "it's possible to freely define your own method because the record is a syntactic show of course with additional things"라고 언급하며 이 점을 강조했습니다.

### 시험 포인트
*   **Java `record`의 특징**: `record`가 자동으로 생성하는 요소(private 필드, 생성자, public 접근자)와 함께, 사용자가 커스텀 메서드를 추가하거나 기본 메서드를 오버라이드할 수 있다는 점을 이해하고 설명할 수 있어야 합니다. ⭐
*   **불변 객체(Immutable Object)와의 연관성**: `record`가 기본적으로 불변 객체를 생성하는 데 유리하며, 이를 통해 표현 노출(representation exposure) 문제를 예방하는 데 도움이 된다는 점을 ⭐**기억하는 것이 중요**합니다.

---

## Slide 34

---
### Class Pattern Matching (1)

**핵심 개념**
Java의 `instanceof` 패턴 매칭은 타입 검사와 형 변환(캐스팅)을 한 번의 표현식으로 처리하여 코드를 간결하게 만드는 기능입니다. 특히 `record` 타입과 함께 사용될 때 강력한 시너지를 발휘하여, 복합적인 데이터 타입에 대한 처리를 용이하게 합니다.

**코드/수식 해설**

```java
interface Shape {}
record Rectangle(double length, double width) implements Shape {}
record Circle(double radius) implements Shape {}

public static double getPerimeter(Shape shape) throws IllegalArgumentException {
    if (shape instanceof Rectangle r) { // s가 Rectangle 타입이면 r 변수에 자동 할당
        return 2 * r.length() + 2 * r.width();
    } else if (shape instanceof Circle c) { // s가 Circle 타입이면 c 변수에 자동 할당
        return 2 * c.radius() * Math.PI;
    } else {
        throw new IllegalArgumentException("Unrecognized shape");
    }
}
```
위 코드는 `Shape` 인터페이스와 이를 구현하는 `Rectangle`, `Circle` `record` 타입을 정의하고 있습니다. `getPerimeter` 메소드에서는 `instanceof` 키워드를 사용하여 입력된 `Shape` 객체의 실제 타입을 확인하고, 동시에 해당 타입으로 형 변환된 변수(`r` 또는 `c`)를 선언하여 바로 사용할 수 있도록 합니다. 이는 기존에 `instanceof` 검사 후 별도로 캐스팅(`((Rectangle)s)`)하던 방식보다 코드를 훨씬 간결하게 만듭니다.

**강의 맥락**
교수님은 `record` 타입의 중요한 이점 중 하나로 "패턴 매칭(pathology)"을 언급하며, 이는 특히 함수형 프로그래밍 경험이 있는 사람들에게 친숙할 것이라고 강조했습니다. 이 슬라이드는 `interface Shape`와 이를 구현하는 `record Rectangle`, `record Circle`의 예시를 통해 `instanceof` 키워드를 활용한 패턴 매칭이 어떻게 코드를 간결하게 만드는지 보여줍니다. 교수님은 `if (s instanceof Rectangle r)`와 같은 구문이 `s`가 `Rectangle` 타입인지 자동으로 검사하고, 맞으면 `r` 변수에 캐스팅된 `Rectangle` 객체를 할당해 바로 사용할 수 있게 한다고 설명했습니다. 이는 명시적인 캐스팅을 계속 해야 했던 이전 방식("ugly report" 또는 "worst" 코드)과 비교하여 코드 복잡성을 줄이고 가독성을 높이는 "매우 유용한 프로그래밍 구성(useful programming construct)"이라고 강조했습니다.

**시험 포인트**
*   `record` 타입이 `instanceof` 패턴 매칭과 결합될 때 얻는 이점 (코드 간결성, 자동 타입 검사 및 캐스팅)을 설명할 수 있어야 합니다. ⭐
*   `instanceof` 패턴 매칭을 사용하지 않았을 때와 비교하여 코드의 차이점 및 개선점을 이해하는 것이 중요합니다. ⭐

---

## Slide 35

## Class Pattern Matching (2)

### 핵심 개념
자바의 향상된 `switch` 문은 타입 패턴 매칭을 지원하여 객체의 타입을 확인하고 해당 타입으로 안전하게 형 변환하는 과정을 간소화합니다. 특히 `when` 절을 사용하면 타입 매칭에 더해 추가적인 조건까지 함께 검사할 수 있습니다.

### 코드/수식 해설

#### 1. `switch` 문을 위한 패턴 매칭
`switch` 문이 이제 객체 타입을 기반으로 패턴을 매칭하고, 매칭되는 타입의 변수를 자동으로 바인딩합니다.

```java
public static double getPerimeter(Shape s) throws IllegalArgumentException {
    return switch (s) { // Shape 타입 s에 대해 switch
        case Rectangle r -> 2 * r.length() + 2 * r.width(); // s가 Rectangle이면 r로 바인딩
        case Circle c -> 2 * c.radius() * Math.PI; // s가 Circle이면 c로 바인딩
        default -> throw new IllegalArgumentException("Unrecognized shape");
    };
}
```
- `switch (s)`: `Shape` 타입의 객체 `s`를 평가합니다.
- `case Rectangle r`: `s`가 `Rectangle` 타입의 인스턴스이면, `s`를 `Rectangle` 타입의 변수 `r`에 바인딩하고 해당 람다 표현식을 실행합니다.
- `case Circle c`: `s`가 `Circle` 타입의 인스턴스이면, `s`를 `Circle` 타입의 변수 `c`에 바인딩하고 해당 람다 표현식을 실행합니다.
- `default`: 위의 어떤 `case`에도 매칭되지 않을 경우 실행됩니다.

#### 2. `when` 절을 활용한 조건부 패턴 매칭
`when` 절은 타입 매칭 패턴에 추가적인 조건(guard clause)을 부여하여, 해당 조건까지 만족할 때만 `case` 블록이 실행되도록 합니다.

```java
static void test(Object obj) {
    switch (obj) {
        case String s when s.length() == 1 -> System.out.println("Short: " + s); // String 타입 s, 길이가 1인 경우
        case String s -> System.out.println(s); // String 타입 s (길이 1이 아닌 경우)
        default -> System.out.println("Not a string");
    }
}
```
- `case String s when s.length() == 1`: `obj`가 `String` 타입이면서 그 길이가 $1$일 때 `s`에 바인딩하고 실행합니다.
- `case String s`: 앞선 `when` 조건에 해당하지 않는 `String` 타입일 경우 `s`에 바인딩하고 실행합니다.
- `default`: 위의 어떤 `case`에도 매칭되지 않을 경우 실행됩니다.

### 강의 맥락
교수님은 이 슬라이드에서 `switch` 문에 통합된 패턴 매칭을 설명하며, 이전 슬라이드에서 언급된 `instanceof`를 사용한 번거로운 (`if-else if`) 코드와 비교하여 얼마나 코드가 간결해지는지 강조했습니다. 특히 `when` 절을 사용하면 단순히 타입 매칭뿐만 아니라 `s.length() == 1`과 같은 **"전통적인 추가 제약 조건(traditional constraint)"**을 붙여 더욱 세밀한 패턴 매칭이 가능함을 설명했습니다. 이는 C++ 기반의 객체지향 프로그래밍에서 다형성(Polymorphism)을 다룰 때 발생하는 다양한 타입 처리를 자바에서 현대적인 방식으로 어떻게 효율적으로 처리하는지 보여주는 중요한 예시입니다.

### 시험 포인트
*   **`switch` 문 패턴 매칭의 기본 문법 및 활용**: `case Type var -> expression;` 형태를 이해하고, 객체의 타입을 기반으로 자동으로 변수 바인딩이 이루어지는 과정을 알아두세요. ⭐
*   **`when` 절의 역할**: 타입 매칭에 더해 추가적인 논리적 조건을 부여하여 특정 `case`를 더욱 정교하게 만들 수 있음을 이해해야 합니다. ⭐
*   **다형성 처리의 효율성**: 전통적인 `instanceof`와 강제 형 변환 없이 다형성을 처리하는 코드를 간결하게 작성하는 방법에 대한 이해가 필요합니다. 이는 객체지향 프로그래밍의 중요한 측면입니다.

---

## Slide 36

### 핵심 개념
Java Record를 활용한 패턴 매칭(Record Patterns)에 대해 설명합니다. 특히 `instanceof` 연산자를 사용하여 객체의 타입을 확인하는 동시에 레코드의 컴포넌트를 구조 분해하여 직접 추출하는 방법을 소개합니다.

### 코드/수식 해설

*   **레코드 패턴 매칭 예시**:
    ```java
    static void printAngleFromXAxis(Object obj) {
        if (obj instanceof Point(double x, double y)) { // obj가 Point 타입이면서 x, y 컴포넌트 추출
            System.out.println(Math.toDegrees(Math.atan2(y, x)));
        }
    }
    ```
    `obj`가 `Point` 레코드의 인스턴스인지 확인하는 동시에, `Point` 레코드의 컴포넌트인 `x`와 `y`를 `double` 타입으로 추출합니다. 이로 인해 코드 내부에서 `x`, `y` 변수를 바로 사용할 수 있습니다.

*   **일반적인 타입 패턴 매칭 예시**:
    ```java
    static void printAngleFromXAxisTypePattern(Object obj) {
        if (obj instanceof Point p) { // obj가 Point 타입인지 확인하고 p 변수에 할당
            System.out.println(Math.toDegrees(Math.atan2(p.y(), p.x())));
        }
    }
    ```
    `obj`가 `Point` 타입이면 `p` 변수에 할당하지만, `x`와 `y` 컴포넌트에 접근하기 위해서는 `p.y()`와 `p.x()`와 같은 accessor 메서드를 명시적으로 호출해야 합니다.

### 강의 맥락
교수님은 Java `record`가 간결한 문법으로 클래스를 선언하는 데 유용하며, 특히 불변(immutable) 데이터 타입 선언에 강점을 가진다고 다시 한번 강조합니다. 이 슬라이드에서는 이전 슬라이드에서 소개된 `instanceof`를 활용한 타입 패턴 매칭보다 "더욱 정교한(more sophisticated)" `record` 패턴 매칭을 설명합니다. `if (obj instanceof Point(double x, double y))`와 같이 `record`의 컴포넌트(`x`, `y`)를 직접 추출하여 사용할 수 있음을 강조하며, 이는 기존의 `instanceof Point p` 후 `p.x()`처럼 getter를 호출하는 방식보다 코드를 훨씬 간결하고 가독성 있게 만들어준다고 설명합니다.

### 시험 포인트
*   ⭐ `record` 패턴 매칭은 `instanceof` 연산자를 사용하여 객체 타입을 확인하는 동시에 해당 레코드의 컴포넌트를 구조 분해(deconstruct)하여 변수로 추출할 수 있게 해 코드의 가독성과 간결성을 크게 향상시킵니다.
*   ⭐ 기존 `instanceof` 타입 패턴(예: `instanceof Point p`)과 `record` 패턴(예: `instanceof Point(double x, double y)`)의 문법적 차이점과 각각의 장단점, 특히 `record` 패턴이 제공하는 간결성을 이해하는 것이 중요합니다.

---

## Slide 37

**핵심 개념**
이 슬라이드는 Java의 레코드 패턴에서 **중첩 패턴(Nested Patterns)** 기능을 설명합니다. 레코드 패턴을 중첩하여 사용하면 복잡한 데이터 구조의 내부 필드까지 한 번의 패턴 매칭으로 해체(destructure)하고 필요한 값을 추출할 수 있어 코드를 간결하고 가독성 높게 작성할 수 있습니다.

**코드 해설**
슬라이드의 코드는 `enum`, `record`, 그리고 중첩된 레코드 패턴을 활용한 `instanceof` 조건문을 보여줍니다.

```java
enum Color { RED, GREEN, BLUE }
record ColoredPoint(Point p, Color c) {} // Point 레코드(x, y 필드 가짐)가 존재한다고 가정
record ColoredRectangle(ColoredPoint upperLeft, ColoredPoint lowerRight) {}

static void printXCoordOfUpperLeftPointWithPatterns(ColoredRectangle r) {
    // r이 ColoredRectangle 타입인지 확인하고, 동시에 그 내부 구조를 해체하여 값을 추출
    if (r instanceof ColoredRectangle(ColoredPoint(Point(var x, var y), var upperLeftColor),
                                      var lowerRightCorner)) {
        // 매칭 성공 시, 상단 좌측 Point의 x 좌표를 직접 사용할 수 있음
        System.out.println("Upper-left corner: " + x);
    }
}
```

1.  **`enum Color`**: 빨강, 초록, 파랑 세 가지 색상을 정의하는 열거형입니다.
2.  **`record ColoredPoint(Point p, Color c)`**: `Point` 객체(여기서는 `(int x, int y)` 필드를 가진다고 가정)와 `Color`를 가지는 `ColoredPoint` 레코드를 정의합니다.
3.  **`record ColoredRectangle(ColoredPoint upperLeft, ColoredPoint lowerRight)`**: 두 개의 `ColoredPoint`(`upperLeft`와 `lowerRight`)를 가지는 `ColoredRectangle` 레코드를 정의합니다.
4.  **`printXCoordOfUpperLeftPointWithPatterns` 메서드**:
    *   `if (r instanceof ColoredRectangle(...))` 구문은 `r` 객체가 `ColoredRectangle` 타입인지를 확인하는 동시에, 괄호 `(...)` 안의 패턴을 통해 `r`의 내부 구조를 해체합니다.
    *   `ColoredRectangle(...)` 내부에서 `upperLeft` 필드는 `ColoredPoint(Point(var x, var y), var upperLeftColor)` 패턴으로 다시 해체됩니다.
    *   `ColoredPoint(...)` 내부에서 `Point p` 필드는 `Point(var x, var y)` 패턴으로 해체되어, 최종적으로 `upperLeft` `ColoredPoint`의 `Point` 객체에 있는 `x`와 `y` 좌표를 `var x`, `var y` 변수에 바인딩합니다.
    *   `upperLeft` `ColoredPoint`의 `c` 필드는 `var upperLeftColor` 변수에 바인딩됩니다.
    *   `lowerRight` 필드는 `var lowerRightCorner` 변수에 통째로 바인딩됩니다.
    *   이 패턴 매칭이 성공하면, `x` 변수(상단 좌측 `Point`의 $x$ 좌표)를 직접 사용하여 출력합니다.

**강의 맥락**
교수님께서는 이전 슬라이드에서 `instanceof`를 통한 단순한 타입 식별 패턴 매칭도 유용하지만 "더 복잡한 패턴 매칭"이 가능하다고 강조하며 이 슬라이드를 설명하셨습니다. 특히 `ColoredPoint`, `ColoredRectangle`과 같은 레코드를 활용하여 클래스 구조 내부에 중첩된 필드(예: `ColoredRectangle` 내의 `ColoredPoint`, 그 안의 `Point(x, y)`)까지 한 번의 패턴으로 "아주 복잡한 패턴"을 매칭하고, 필요한 모든 변수를 자동으로 식별하여 추출할 수 있다고 설명하셨습니다. 이는 코드를 훨씬 간결하고 이해하기 쉽게 만든다는 점을 중요하게 언급하셨습니다.

**시험 포인트**
*   ⭐ **중첩 레코드 패턴의 개념과 활용**: 여러 계층으로 구성된 복합 객체의 특정 내부 필드에 접근하고 값을 추출하기 위해 `instanceof`와 함께 레코드 패턴을 중첩하여 사용하는 방법을 이해하고 설명할 수 있어야 합니다.
*   ⭐ **코드 간결화 및 가독성 향상**: 중첩 패턴이 복잡한 `if-else` 또는 여러 단계의 `.get()` 호출을 대체하여 코드를 어떻게 단순화하고 가독성을 높이는지 설명할 수 있어야 합니다.

---

## Slide 38

**핵심 개념**
Java의 `switch` 식에서 패턴 매칭을 사용할 때는 모든 가능한 입력 패턴을 **완벽하게 커버(exhaustive)**해야 합니다. 만약 특정 패턴에 대해 `switch` 문이 처리하지 못하는 경우가 발생할 수 있다면, Java 컴파일러는 컴파일 오류를 발생시켜 잠재적인 런타임 문제를 방지합니다. 이러한 `exhaustiveness`를 보장하기 위해 `default` 케이스를 사용하여 나머지 모든 경우를 처리할 수 있습니다.

**코드/수식 해설**

```java
record Pair<T>(T x, T y) {} // 제네릭 타입 T를 가진 두 요소를 저장하는 Pair 레코드
class A {} // 기본 클래스 A
class B extends A {} // A를 상속받는 클래스 B

static void notExhaustive(Pair<A> p) {
    switch (p) {
        // error: the switch statement does not cover all possible input values
        // Pair<A>의 x와 y가 A 타입일 때 가능한 조합은 (A, A), (A, B), (B, A), (B, B) 네 가지이다.
        // 현재 코드는 (A, B)와 (B, A) 두 가지 경우만 명시적으로 처리하고 있다.
        // (A, A)와 (B, B) 케이스가 누락되어 컴파일 에러 발생.
        case Pair<A>(A a, B b) -> System.out.println("Pair<A>(A a, B b)");
        case Pair<A>(B b, A a) -> System.out.println("Pair<A>(B b, A a)");
    }
}
```
위 코드는 `Pair<A>` 타입의 객체 `p`를 `switch` 문으로 패턴 매칭하려고 시도합니다. `Pair<T>`는 `T` 타입의 두 필드 `x`와 `y`를 가집니다. 여기서 `T`는 `A`로 지정되었으므로, `p.x`와 `p.y`는 `A` 타입 또는 `A`를 상속하는 `B` 타입이 될 수 있습니다. 따라서 `(x, y)` 필드에 대해 가능한 조합은 `(A, A)`, `(A, B)`, `(B, A)`, `(B, B)`의 네 가지입니다. 그러나 `switch` 문은 `Pair<A>(A a, B b)`와 `Pair<A>(B b, A a)` 두 가지 케이스만 명시적으로 처리하고 있어, `(A, A)`와 `(B, B)` 조합이 누락되었습니다. 이로 인해 컴파일러는 "switch statement does not cover all possible input values"라는 오류를 발생시킵니다.

**강의 맥락**
교수님은 Java의 `switch` 패턴 매칭이 모든 가능한 경우를 처리해야 한다는 점(`exhaustiveness`)을 강조합니다. 만약 모든 경우가 커버되지 않으면 컴파일 에러가 발생하며, 이는 개발자가 놓칠 수 있는 런타임 오류를 사전에 방지하기 위함입니다. 현재 슬라이드에서 제시된 `Pair<A>` 예시처럼, `x`와 `y` 필드가 각각 `A` 또는 `B` 타입일 수 있는 상황에서 모든 조합(`(A, A)`, `(A, B)`, `(B, A)`, `(B, B)`)을 명시적으로 처리하지 않으면 컴파일 에러가 발생한다고 설명합니다. 이 문제를 해결하는 가장 간단한 방법은 `default` 키워드를 사용하여 나머지 모든 케이스를 포괄적으로 처리하는 것입니다. 이 슬라이드는 이후에 `sealed` 키워드를 소개하며 `default`를 사용하지 않고도 `exhaustiveness`를 보장하는 방법을 설명하기 위한 배경 지식을 제공합니다.

**시험 포인트**
*   ⭐ `switch` 식에서 패턴 매칭 사용 시 **`exhaustiveness` (모든 경우의 수 커버)**의 중요성.
*   ⭐ `exhaustiveness`가 보장되지 않을 때 **컴파일 에러**가 발생하는 이유.
*   ⭐ `default` 키워드가 `switch` 패턴 매칭의 `exhaustiveness`를 보장하는 데 어떻게 사용될 수 있는지.

---

## Slide 39

 ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `

---

## Slide 40

**핵심 개념**
이 슬라이드는 재귀적인 자료구조인 이진 트리(Binary Tree)를 Java의 `sealed interface`와 `record`를 활용하여 간결하고 타입 안전하게 구현하는 방법을 보여줍니다. `sealed interface`는 특정 타입 계층 내에서만 확장을 허용하여, 패턴 매칭 시 모든 경우의 수를 컴파일러가 파악할 수 있도록 돕습니다.

**코드/수식 해설**
*   **`sealed interface IntTree permits Leaf, Node {}`**:
    *   `IntTree`는 이진 트리의 모든 구성 요소(노드와 잎)를 나타내는 인터페이스입니다.
    *   `sealed` 키워드는 이 인터페이스를 구현하거나 확장할 수 있는 클래스를 `permits` 절에 명시된 `Leaf`와 `Node`로만 제한합니다. 이를 통해 컴파일러가 `IntTree`의 가능한 모든 서브타입을 정확히 파악하고, 불완전한(non-exhaustive) 패턴 매칭으로 인한 잠재적 오류를 방지할 수 있습니다. ⭐
*   **`record Leaf(int value) implements IntTree {}`**:
    *   `Leaf`는 트리의 말단 노드(잎)를 나타내는 `record` 타입입니다.
    *   `int value` 필드를 가지며, `IntTree` 인터페이스를 구현합니다. `record`는 기본적으로 불변(immutable)이며, `value` 필드를 위한 생성자, 접근자(getter), `equals()`, `hashCode()`, `toString()` 등을 자동으로 제공합니다.
*   **`record Node(IntTree left, IntTree right) implements IntTree {}`**:
    *   `Node`는 두 자식을 가지는 트리의 내부 노드를 나타내는 `record` 타입입니다.
    *   `IntTree` 타입의 `left`와 `right` 두 필드를 가지며, `IntTree` 인터페이스를 구현합니다. 이는 이진 트리의 재귀적 구조를 직접적으로 표현합니다.

**구체적 예시**
슬라이드의 다이어그램은 이진 트리의 시각적인 구조를 보여줍니다.
*   `Node`는 항상 두 자식을 가집니다.
*   `Leaf` 노드는 정수 값 (예: (1), (2), (3))을 가집니다.
제공된 Java 코드는 이 정의를 `sealed interface`와 `record`를 사용하여 그대로 구현한 예시입니다. `IntTree`는 `Leaf`와 `Node` 중 하나로 구성될 수 있음을 명확하게 보여줍니다.

**강의 맥락**
교수님은 `record`와 패턴 매칭을 사용하면 트리와 같은 재귀적 자료구조를 매우 쉽게 구현할 수 있다고 강조했습니다. 특히, 이 예시는 `IntTree` 인터페이스를 `Leaf`와 `Node`라는 두 가지 형태의 `record`로 정의함으로써 트리의 "귀납적 타입 정의(inductive type definition)"를 직관적으로 표현한 것입니다.

강의에서는 `sealed` 키워드의 중요성을 자세히 설명했습니다. 일반적인 상속 구조에서는 패턴 매칭 시 예측 불가능한 추가 서브클래스가 생길 수 있어 모든 경우의 수를 커버하지 못할 위험이 있습니다. 이 경우 컴파일러는 `default`와 같은 폴백(fallback) 케이스를 강제하여 컴파일 에러를 발생시킵니다. 그러나 `sealed` 인터페이스는 `permits` 절을 통해 구현 가능한 서브클래스를 명시적으로 제한하므로, 컴파일러가 모든 가능한 케이스를 파악할 수 있어 ⭐**`default` 케이스 없이도 완전하고 안전한 패턴 매칭을 보장**할 수 있게 됩니다. 이는 코드의 안정성을 높이고 가독성을 개선하는 데 매우 유용합니다.

**시험 포인트**
*   ⭐`record`를 사용하여 불변(immutable) 데이터 타입을 간결하게 정의하는 방법과 그 장점(자동 생성자, 접근자 등).
*   ⭐`sealed interface`와 `permits` 키워드를 사용하여 클래스 계층 구조를 제한하는 방법 및 이 기술이 **패턴 매칭 시 모든 케이스를 처리함을 보장하여 컴파일러의 도움을 받을 수 있는 이유와 중요성**.

---

## Slide 41

**핵심 개념**
이 슬라이드는 Java Record와 패턴 매칭(`switch` 식)을 활용하여 이진 트리의 모든 노드에 저장된 정수 값의 합계를 계산하는 `sum` 함수의 구현과 사용 예시를 보여줍니다.

**코드/수식 해설**

```java
static int sum(IntTree tree) {
    return switch (tree) {
        case Leaf(int value) -> value;
        case Node(IntTree left, IntTree right) -> sum(left) + sum(right);
    };
}
```
*   `sum` 함수는 `IntTree` 타입의 `tree`를 인자로 받아 트리의 모든 정수 값을 합산하여 반환합니다.
*   Java 17 이상에서 도입된 `switch` 식을 사용하며, 패턴 매칭을 통해 `tree` 객체의 실제 타입(`Leaf` 또는 `Node`)에 따라 다른 동작을 수행합니다.
*   `case Leaf(int value) -> value;`: 만약 `tree`가 `Leaf` 타입이라면, `Leaf` 레코드의 `value` 필드를 추출하여 그 값을 반환합니다.
*   `case Node(IntTree left, IntTree right) -> sum(left) + sum(right);`: 만약 `tree`가 `Node` 타입이라면, `Node` 레코드의 `left`와 `right` 필드를 추출하여 각각 재귀적으로 `sum` 함수를 호출한 후 그 결과를 더하여 반환합니다.

```java
IntTree tree = new Node(new Leaf(1), new Node(new Leaf(2), new Leaf(3)));
System.out.println("Sum: " + sum(tree));
```
*   이 예시는 `sum` 함수의 사용법을 보여줍니다. `new Node(new Leaf(1), new Node(new Leaf(2), new Leaf(3)))` 코드는 다음 구조의 `IntTree`를 생성합니다:
    ```
        Node
       /    \
    Leaf(1)  Node
             /    \
          Leaf(2) Leaf(3)
    ```
*   `sum(tree)`를 호출하면 이 트리의 모든 잎(Leaf) 노드의 값인 $1, 2, 3$이 더해져 총합 $6$이 계산되고, 콘솔에 "Sum: 6"이 출력됩니다.

**강의 맥락**
교수님은 앞선 슬라이드에서 정의된 `IntTree`와 같은 **귀납적 타입 정의(inductive type definition)**를 Java Record와 `sealed` 인터페이스, 그리고 패턴 매칭을 통해 매우 직관적이고 깔끔하게 구현할 수 있음을 강조했습니다. 특히 이 `sum` 함수는 패턴 매칭을 사용하면 트리의 연산을 구현하는 것이 얼마나 "straightforward(매우 간단하고 직접적)"하고 "beautiful(아름다운)" 코드인지를 보여주는 예시입니다. 일반적인 트리 자료구조 연산은 복잡하게 느껴질 수 있지만, 이와 같은 방법을 통해 매우 간결하게 코드를 작성할 수 있습니다.

**시험 포인트**
*   ⭐Java `record`와 `switch` 식의 **패턴 매칭**을 활용하여 **재귀적 자료구조(예: 트리)의 연산**을 구현하는 방법을 이해하고 설명할 수 있어야 합니다.
*   ⭐`Leaf`와 `Node` 같은 서브클래스별로 다른 로직을 처리하는 재귀적 함수의 구현 원리를 파악하세요.

---

## Slide 42

**핵심 개념**
이 슬라이드는 객체지향 프로그래밍에서 객체가 지켜야 할 일반적인 계약(contract), 즉 명세(specification)에 대한 논의를 시작하는 도입부입니다. 객체의 올바른 동작과 사용을 보장하기 위한 다양한 규칙과 설계 원칙을 포괄적으로 다룹니다.

**강의 맥락**
교수님은 지난 시간에 배운 내용을 빠르게 요약하며 이 슬라이드의 주제를 강조합니다. 객체의 계약이란 다음을 포함하는 클래스 명세를 의미합니다:
1.  **메서드별 선행/후행 조건(Precondition and Postcondition)**: 각 메서드의 호출 전후 상태에 대한 약속입니다.
2.  **추상 값(Abstract Values)**: 사용자(클라이언트)가 객체를 이해하는 데 필요한 내부 상태의 추상적인 표현입니다. 이는 정보 은닉(data abstraction)의 핵심입니다.
3.  **클래스 불변식(Class Invariant)**: 객체의 모든 공개 메서드 호출 전후에 항상 참이어야 하는 조건으로, 추상 값 수준에서 객체의 일관성을 유지합니다.

또한, 구현자(implementer) 관점에서는 다음이 추가적으로 고려됩니다:
1.  **구체적 표현(Concrete Representation)**: 실제 내부 데이터 구조입니다.
2.  **추상화 함수(Abstraction Function)**: 구체적 표현을 추상 값으로 매핑하는 함수로, 구현이 명세를 어떻게 만족하는지 설명합니다.
3.  **표현 불변식(Representation Invariant)**: 구체적 표현이 항상 유효한 상태를 유지하기 위한 조건입니다.

이러한 객체 계약을 위반하는 것을 방지하기 위해, 내부 표현을 외부에 노출하지 않는 `private` 접근 제한자 사용, `final` 키워드를 통한 불변성 강화, 불변 객체(immutable objects)의 설계 및 활용, Java `record`와 `sealed interface`를 통한 안전하고 간결한 데이터 타입 정의 및 패턴 매칭 활용 등 다양한 기법이 소개되었습니다. 이 슬라이드는 이러한 모든 내용이 결국 객체의 견고한 "계약"을 어떻게 만들고 지킬 것인가에 대한 논의의 큰 줄기임을 제시합니다.

**시험 포인트**
*   ⭐ **객체의 계약(Contract for Objects)**이 무엇을 의미하며, 이를 구성하는 주요 명세 요소들(추상 값, 클래스 불변식, 표현 불변식, 추상화 함수 등)을 정확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ 클래스의 **내부 표현 노출(Representation Exposure)**을 방지하고 불변성을 유지하기 위한 다양한 방법들(예: `private` 필드, `final` 키워드, 불변 객체 설계, Java `record` 및 `sealed interface`)의 특징과 장단점을 숙지해야 합니다.

---

## Slide 43

---

### 핵심 개념

객체 동등성(Object Equality)은 두 객체가 같다고 판단되는 기준을 의미하며, 이를 정의하는 것은 단순하지 않고 여러 가지 관점을 가진다. 주요한 동등성 판단 기준은 다음과 같다:

1.  **값 동등성 (Value Equality)**: 두 객체가 동일한 내부 값(데이터)을 가지는 경우. 이는 구체적인 필드들의 일치 여부를 따진다.
2.  **추상 값 동등성 (Abstract Value Equality)**: 두 객체가 클래스의 **추상적인 표현(abstract representation)** 수준에서 동일한 상태를 가지는 경우. 이는 사용자가 인지하는 객체의 논리적인 상태가 동일한지를 의미하며, 내부의 구체적인 구현 방식이 달라도 추상적 값이 같으면 동등하다고 본다.
3.  **참조 동등성 (Reference Equality)**: 두 객체가 메모리상에서 동일한 객체 인스턴스를 가리키는 경우 (동일한 ID 또는 참조).

이처럼 동등성을 정의하는 방식은 한 가지가 아니므로, 객체지향 프로그래밍에서 `equals` 메서드 등을 오버라이드할 때 어떤 종류의 동등성을 의도하는지 명확히 해야 한다.

### 구체적 예시

자바(Java)와 같은 언어에서는 기본적으로 `==` 연산자가 참조 동등성을 확인하고, `equals()` 메서드는 기본적으로 `==`와 동일하게 참조 동등성을 확인하지만, `String` 클래스처럼 값 동등성을 확인하도록 오버라이드될 수 있다.

```java
// 참조 동등성
Object obj1 = new Object();
Object obj2 = new Object();
System.out.println(obj1 == obj2); // false (다른 인스턴스)

// 값 동등성을 확인하도록 오버라이드된 경우 (예: String)
String s1 = new String("hello");
String s2 = new String("hello");
System.out.println(s1 == s2);      // false (다른 인스턴스)
System.out.println(s1.equals(s2)); // true (내부 값이 동일)
```

### 강의 맥락

교수님은 앞선 강의에서 다루었던 클래스 명세(class specification), 추상 표현(abstract representation) 등의 개념을 상기시키며, 객체 동등성을 판단하는 기준 또한 여러 "개념(notion)"이 있음을 강조했습니다. 특히 "추상 값(abstract value)"이 같은지 여부를 질문함으로써, 사용자가 객체의 내부 구현에 상관없이 명세 수준에서 객체의 상태를 이해하는 것의 중요성을 다시 한번 언급했습니다. 이는 객체지향 설계에서 내부 구현과 외부 명세를 분리하는 추상화의 핵심 원리와 연결됩니다. 동등성을 단순히 내부 필드의 일치로 볼 것인지, 아니면 객체의 추상적인 의미나 참조 동일성으로 볼 것인지에 대한 정의가 간단하지 않음을 지적하며, 프로그래머가 이를 명확히 이해하고 구현해야 함을 강조했습니다.

### 시험 포인트

*   ⭐ **객체 동등성을 판단하는 세 가지 주요 기준(값 동등성, 추상 값 동등성, 참조 동등성)을 정확히 이해하고 설명할 수 있어야 합니다.**
*   ⭐ **'추상 값 동등성'이 클래스 명세 및 추상화 개념과 어떻게 연결되는지 설명할 수 있어야 합니다.**
*   ⭐ **프로그래밍 언어에서 `equals()` 메서드 오버라이딩 시 어떤 종류의 동등성을 정의해야 하는지 설명하는 문제로 출제될 수 있습니다.**

---

## Slide 44

**핵심 개념**
객체 지향 프로그래밍에서 두 객체의 '동등성(Equality)'을 정의할 때 일반적으로 기대되는 세 가지 핵심 속성과, 이 속성들을 만족하는 관계인 '동치 관계(Equivalence Relation)'에 대해 설명합니다.

**코드/수식 해설**

*   **반사성 (Reflexive)**
    어떤 객체 `a`는 자기 자신과 항상 동등해야 합니다.
    `a.equals(a) == true`
*   **대칭성 (Symmetric)**
    만약 객체 `a`가 객체 `b`와 동등하면, 객체 `b`도 객체 `a`와 동등해야 합니다.
    `a.equals(b)` 이면 `b.equals(a)`
*   **추이성 (Transitive)**
    만약 객체 `a`가 객체 `b`와 동등하고, 객체 `b`가 객체 `c`와 동등하면, 객체 `a`는 객체 `c`와도 동등해야 합니다.
    `a.equals(b)` 이고 `b.equals(c)` 이면 `a.equals(c)`

이러한 세 가지 속성(반사성, 대칭성, 추이성)을 모두 만족하는 관계를 **동치 관계(equivalence relation)**라고 합니다.

**강의 맥락**
(제공된 음성 전사에서 현재 슬라이드의 내용("Expected Properties of Equality"의 반사성, 대칭성, 추이성, 동치 관계)과 직접적으로 일치하는 설명 구간이 명확하게 확인되지 않습니다. 교수님께서는 강의 말미에 "some type of sentence"나 "common sense of education"에 대해 언급하셨지만, 이는 슬라이드의 동등성 속성과는 다른 맥락으로 보입니다.)

**시험 포인트**
*   ⭐ 객체의 `equals()` 메서드를 오버라이드할 때 반드시 만족해야 하는 세 가지 속성(반사성, 대칭성, 추이성)을 정확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ 동치 관계(Equivalence Relation)의 정의와 중요성을 파악하는 것이 중요합니다. 특히, `equals()` 구현 시 이 속성들이 깨지면 예상치 못한 버그를 유발할 수 있음을 유의해야 합니다.

---

## Slide 45

## Reference Equality (참조 동등성)

### 핵심 개념
참조 동등성(Reference Equality)은 두 객체가 메모리상에서 **동일한 객체**를 참조하는지 여부를 판단하는 개념입니다. 이는 객체의 내용(값)이 아니라, 객체의 **메모리 주소(ID)**가 같은지를 비교하는 가장 강력한 형태의 동등성 정의입니다.

### 코드/수식 해설
두 객체 `a`와 `b`가 참조 동등하다는 것은 다음과 같은 조건을 만족할 때입니다:
- 이들이 **동일한 객체(same object)**를 참조합니다 (동일한 ID/참조).
- C++, Java와 같은 언어에서 기본적으로 제공되는 `==` 연산자를 사용하여 `a == b`가 `true`를 반환합니다.

### 구체적 예시
Java 코드를 예시로 들면:
```java
class MyObject {
    int value;
    MyObject(int v) { this.value = v; }
}

public class Main {
    public static void main(String[] args) {
        MyObject obj1 = new MyObject(10);
        MyObject obj2 = new MyObject(10);
        MyObject obj3 = obj1;

        System.out.println(obj1 == obj2); // false (다른 객체)
        System.out.println(obj1 == obj3); // true (동일한 객체를 참조)
    }
}
```
위 예시에서 `obj1`과 `obj2`는 비록 `value`가 같지만, 서로 다른 메모리 위치에 생성된 객체이므로 `==` 연산 시 `false`를 반환합니다. 반면 `obj3`은 `obj1`이 참조하는 객체와 동일한 객체를 참조하므로 `==` 연산 시 `true`를 반환합니다.

### 강의 맥락
교수님께서는 이전 강의에서 클래스 사양, 추상 값, 클래스 불변식, 그리고 내부 표현의 노출 방지(mutable/immutable 객체, Java Record, 패턴 매칭 등)에 대해 다루셨습니다. 본 슬라이드는 이러한 객체 지향 프로그래밍 맥락에서 객체 간의 "동등성(equality)" 개념을 비교하는 부분으로 넘어가는 도입부로 보입니다.

음성 전사에서 "How to compare different sense of education. So, basically weaker education means, stronger education means, weaker education and stronger learning"이라는 비유적인 표현이 나오는데, 이는 **다양한 종류의 '동등성' 개념**을 비교하기 위한 서론적인 설명으로 추측됩니다. 참조 동등성은 객체의 내용(값)보다는 객체의 ID(메모리 주소)를 비교하는 가장 근본적이고 엄격한 동등성 정의이므로, 슬라이드에서 이를 "가장 강력한(strongest) 동등성 정의"라고 명시하고 있습니다.

### 시험 포인트
- ⭐ **참조 동등성의 정의**: 두 객체가 메모리상에서 동일한 객체를 참조하는 것. `==` 연산자로 확인 가능.
- ⭐ **참조 동등성의 특징**:
    - 반사성($a == a$), 대칭성(if $a == b$ then $b == a$), 전이성(if $a == b$ and $b == c$ then $a == c$)을 만족하는 **동치 관계(equivalence relation)** 입니다.
    - 객체 간 동등성을 정의하는 **가장 강력한(strongest) 정의**이며, 가장 작은 동치 관계입니다 (반사성 때문에).
    - 종종 원하는 동등성 정의이지만, 항상 그런 것은 아님 (객체의 *값*이 같은 것을 원할 때도 있음).

---

## Slide 46

## Example: Reference Equality

### 핵심 개념
객체 비교 시 `==` 연산자는 두 변수가 **동일한 객체(메모리 주소)**를 참조하는지 확인하는 **참조 동등성(Reference Equality)**을 검사합니다. 반면, 객체의 **값(내용)**이 동일한지 확인하는 **값 동등성(Value Equality)**은 일반적으로 `equals()` 메서드를 오버라이드하여 구현합니다. `==`는 더 엄격한 동등성 기준이며, `equals()`는 종종 이보다 '약한(weaker)' 동등성 관계를 정의하는 데 사용됩니다.

### 코드/수식 해설
```java
LocalDate d1 = LocalDate.of(2025, 4, 14);
LocalDate d2 = LocalDate.of(2025, 4, 14);
LocalDate d3 = d2;

System.out.println(d1 == d2); // output: false
System.out.println(d2 == d3); // output: true
```
*   `d1`과 `d2`는 같은 값을 가지지만, `LocalDate.of()`를 두 번 호출하여 각각 **다른 메모리 공간에 있는 두 개의 독립적인 객체**를 생성합니다. 따라서 `d1 == d2`는 `false`를 반환합니다.
*   `d3 = d2;`는 `d2`가 참조하는 객체(메모리 주소)를 `d3`에도 할당합니다. 즉, `d2`와 `d3`는 **동일한 객체**를 참조합니다. 따라서 `d2 == d3`는 `true`를 반환합니다.

### 구체적 예시
슬라이드의 Java 코드 예시는 `LocalDate` 객체를 사용하여 참조 동등성과 값 동등성의 차이를 명확히 보여줍니다. `d1`과 `d2`는 겉으로는 같은 "2025/04/14" 날짜를 나타내지만, 메모리상에서는 별개의 객체이므로 `==` 비교 시 `false`가 나옵니다. 반면 `d2`와 `d3`는 같은 객체를 참조하므로 `==` 비교 시 `true`가 나옵니다.

### 강의 맥락
교수님께서는 이 슬라이드를 "another example"로 언급하며, 객체 간의 "비교"에 대한 다양한 "sense of education" (동등성 기준)이 있으며, `==` 연산자보다 "weaker"한 동등성 관계를 원할 때가 있다고 강조하셨습니다. 이는 객체의 참조가 아닌 내용을 기반으로 한 비교(`equals()` 메서드를 통한)의 필요성을 설명하는 부분입니다. 자바에서는 `equals()` 메서드를 오버라이드하여 이처럼 더 넓은 의미의 동등성을 정의할 수 있다고 설명됩니다.

### 시험 포인트
*   객체 간 `==` 연산자의 의미와 동작 방식 (참조 동등성) ⭐
*   객체의 내용 비교를 위한 `equals()` 메서드의 필요성 및 오버라이딩 가능성 ⭐
*   `==`와 `equals()`의 차이점을 설명하고, 각각 언제 사용해야 하는지 예시와 함께 설명할 수 있어야 합니다. ⭐

---

## Slide 47

### 핵심 개념
`Object.equals` 메서드는 객체 간의 동등성(equality)을 정의하며, Java의 `Object` 클래스에 정의된 중요한 메서드입니다. 이는 특정 `Object`가 다른 `Object`와 "같은지"를 나타내며, `null` 참조를 제외한 모든 객체 참조에 대해 **동치 관계(equivalence relation)**를 구현해야 합니다.

`equals` 메서드의 계약(contract)은 다음과 같은 다섯 가지 속성을 준수해야 합니다:
1.  **반사성(Reflexive)**: `null`이 아닌 모든 참조 값 `x`에 대해 `x.equals(x)`는 반드시 `true`를 반환해야 합니다.
2.  **대칭성(Symmetric)**: `null`이 아닌 모든 참조 값 `x`와 `y`에 대해 `x.equals(y)`가 `true`를 반환하는 경우에만 `y.equals(x)`도 `true`를 반환해야 합니다.
3.  **추이성(Transitive)**: `null`이 아닌 모든 참조 값 `x`, `y`, `z`에 대해 `x.equals(y)`가 `true`이고 `y.equals(z)`가 `true`를 반환하면, `x.equals(z)`도 반드시 `true`를 반환해야 합니다.
4.  **일관성(Consistent)**: `null`이 아닌 모든 참조 값 `x`와 `y`에 대해, `equals` 비교에 사용되는 객체의 정보가 수정되지 않는 한, `x.equals(y)`를 여러 번 호출해도 항상 `true`를 반환하거나 항상 `false`를 반환해야 합니다. 즉, 객체가 변경되지 않는 한 동일한 결과를 일관되게 반환해야 합니다.
5.  **`null`과의 비교**: `null`이 아닌 모든 참조 값 `x`에 대해 `x.equals(null)`은 반드시 `false`를 반환해야 합니다.

### 코드/수식 해설
`Object` 클래스에 정의된 `equals` 메서드의 시그니처는 다음과 같습니다:
```java
public boolean equals(Object obj)
```
이 메서드는 입력된 `obj` 객체가 현재 객체(`this`)와 동일한지 여부를 `boolean` 값으로 반환합니다.

### 구체적 예시
`null` 값과의 비교는 특별히 주의해야 합니다.
*   `a.equals(b)`가 `b == null`인 경우, `Object`의 `equals` 계약에 따라 `false`를 반환해야 합니다. (이는 `a`가 `null`이 아닌 경우에 해당합니다.)
*   만약 `a == null`인 경우 `a.equals(b)`를 호출하면 `NullPointerException`이 발생합니다.
    ```java
    Object obj1 = new Object();
    Object obj2 = null;

    System.out.println(obj1.equals(obj2)); // false (계약 준수)
    // System.out.println(obj2.equals(obj1)); // NullPointerException 발생!
    ```

### 강의 맥락
제공된 음성 전사에서는 `Object.equals` 메서드와 관련된 직접적인 설명이나 강조 포인트가 명확하게 식별되지 않습니다. 이전 슬라이드에서 `immutable` 객체, `record` 클래스, `sealed` 인터페이스 등 다양한 Java 프로그래밍 기법에 대해 논의한 후, 새로운 주제로 전환되는 지점에서 해당 슬라이드가 제시된 것으로 보입니다. 하지만 전사 내용 자체에 오류가 많아, 이 슬라이드의 구체적인 강의 맥락을 파악하기는 어렵습니다. 따라서 슬라이드 자체의 내용에 충실하여 `equals` 메서드의 정의와 중요한 속성들을 설명하는 데 집중합니다.

### 시험 포인트
*   `Object.equals` 메서드가 만족해야 하는 ⭐**다섯 가지 속성(반사성, 대칭성, 추이성, 일관성, `null` 처리)**을 정확히 이해하고 설명할 수 있어야 합니다.
*   특히 ⭐**`a.equals(null)`은 `false`를 반환하지만, `null.equals(a)`는 `NullPointerException`을 발생시킨다는 점**을 명확히 구분해야 합니다.
*   ⭐사용자 정의 클래스에서 `equals` 메서드를 오버라이드할 때 이 계약을 준수하는 것이 매우 중요하며, 이를 위반할 경우 예측 불가능한 버그로 이어질 수 있습니다.

---

## Slide 48

**핵심 개념**

Java의 모든 클래스가 상속받는 `java.lang.Object` 클래스에 정의된 `equals()` 메서드는 기본적으로 **참조 동등성(reference equality)**을 구현합니다. 이는 두 객체가 메모리상에서 동일한 인스턴스인지를 `==` 연산자를 사용하여 비교하는 것을 의미합니다. 하지만 대부분의 경우 객체의 `값(value)`이 같은지를 비교하는 **값 동등성(value equality)**이 필요하므로, 하위 클래스에서 `equals()` 메서드를 오버라이드하여 사용자 정의 동등성 로직을 구현할 수 있습니다. 이때 `equals()` 메서드의 일반적인 규약(contract)을 준수해야 합니다.

**코드/수식 해설**

`java.lang.Object` 클래스에 정의된 기본 `equals()` 메서드의 구현은 다음과 같습니다:

```java
public class Object {
    ...
    public boolean equals(Object obj) {
        return (this == obj);
    }
    ...
}
```

-   `public boolean equals(Object obj)`: `Object` 타입의 다른 객체 `obj`를 인자로 받아 동등성 여부를 `boolean` 값으로 반환합니다.
-   `return (this == obj);`: 여기서 `==` 연산자는 `this`와 `obj` 두 객체 참조가 메모리상에서 동일한 객체 인스턴스를 가리키는지 비교합니다. 이것이 기본 `equals()`가 구현하는 **참조 동등성**입니다.

**구체적 예시**

`String` 클래스의 경우 `Object`의 `equals()`를 오버라이드하여 문자열 내용을 비교하는 값 동등성을 구현합니다.
```java
String strA = new String("hello");
String strB = new String("hello");
String strC = strA;

System.out.println(strA == strB);       // false (다른 메모리 인스턴스)
System.out.println(strA.equals(strB));  // true (String이 equals() 오버라이드하여 값 비교)
System.out.println(strA == strC);       // true (동일한 메모리 인스턴스를 참조)
```

**강의 맥락**

제공된 강의 음성 전사에서는 현재 슬라이드 내용(Object.equals 메서드)과 직접적으로 일치하는 설명 구간이 확인되지 않습니다. 슬라이드 내용은 객체 동등성 비교의 기본 원칙과 `Object` 클래스의 `equals` 메서드에 대한 이해를 다룹니다.

**시험 포인트**

*   `Object.equals()`의 기본 동작이 ⭐**참조 동등성**⭐임을 이해하는 것이 중요합니다.
*   하위 클래스에서 `equals()`를 오버라이드하여 ⭐**값 동등성**⭐을 구현해야 하는 경우와 이때 `equals()` 메서드 규약(contract)을 준수해야 함을 이해해야 합니다.
*   Java에서 `==` 연산자와 `equals()` 메서드의 차이점을 명확히 구분할 수 있어야 합니다.

---

## Slide 49

## Behavioral Equivalence

### 핵심 개념
**행동적 동치 (Behavioral Equivalence)**는 두 객체 `$a$`와 `$b$`가 모든 가능한 메서드 호출 시퀀스를 통해 외부에서 관찰했을 때 서로 구별될 수 없는 경우를 의미합니다. 즉, 어떤 메서드를 호출해도 두 객체가 동일하게 동작하고 동일한 결과를 반환한다면 이들은 행동적으로 동치입니다.

*   **불변 객체 (Immutable Types)**: 상태가 변경될 수 없는 객체이므로, 두 불변 객체가 동일한 (추상) 값을 가지고 있다면 이들은 행동적으로 동치입니다. 따라서 불변 객체는 `equals` 메서드를 직접 구현하여 값에 기반한 동치성을 올바르게 정의해야 합니다.
*   **가변 객체 (Mutable Types)**: 상태가 변경될 수 있는 객체의 경우, 두 객체가 현재 동일한 (추상) 값을 가지고 있더라도 한 객체를 변경함으로써 다른 객체와 구별될 수 있습니다. 이 경우 현재 시점에서 동일한 추상 값을 가지는 상태를 **관찰적 동치 (Observational Equivalence)**라고 합니다. 가변 객체는 일반적으로 완전한 행동적 동치를 유지하기 어렵습니다.

### 구체적 예시
*   **불변 객체 예시**:
    두 `String` 객체 `$s1 = "hello"$`와 `$s2 = "hello"$`가 있습니다. 이들은 동일한 값을 가지므로 행동적으로 동치입니다. `$s1.toUpperCase()$`와 같은 메서드를 호출해도 `$s1$` 자체의 상태는 변하지 않고 새로운 `String` 객체를 반환하므로, `$s1$`과 `$s2$`는 여전히 구별할 수 없습니다.
*   **가변 객체 예시**:
    두 `ArrayList<Integer>` 객체 `$list1 = new ArrayList<>()$`에 `1, 2`를 추가하고, `$list2 = new ArrayList<>()$`에도 `1, 2`를 추가했다고 가정해 봅시다. 현재 `$list1$`과 `$list2$`는 `[1, 2]`로 동일한 추상 값을 가지므로 관찰적으로 동치입니다. 그러나 `$list1.add(3)$`을 호출하면 `$list1$`은 `[1, 2, 3]`이 되고, `$list2$`는 `[1, 2]`로 유지되어 두 객체가 구별됩니다. 따라서 이들은 행동적으로 동치라고 할 수 없습니다.

### 강의 맥락
(음성 전사에서 해당 슬라이드의 내용이 명확하게 구분되지 않아, 이전 및 이후 강의 내용과 일반적인 소프트웨어 작성 원리 교육의 흐름을 바탕으로 맥락을 구성했습니다.)

교수님께서는 이전 강의에서 추상화, 객체의 상태, 그리고 클래스 명세(Precondition, Postcondition, Abstract Representation, Class Invariant) 및 구현(Concrete Representation, Abstraction Function, Representation Invariant) 간의 관계를 강조하셨습니다. 이번 슬라이드에서 다루는 **행동적 동치**는 이러한 맥락에서 두 객체가 "동일하다"는 것을 어떻게 정의하고 검증할 것인가에 대한 핵심 개념입니다.

특히, 불변 객체와 가변 객체의 설계 원칙을 앞서 설명하셨는데, 행동적 동치 개념은 이 두 가지 타입의 객체를 다룰 때 동치성 판단 기준이 어떻게 달라지는지를 명확히 보여줍니다.

*   **추상화와의 연결**: 객체의 내부 구현이 아닌, 외부에서 관찰 가능한 추상적인 동작을 기준으로 동치성을 판단하는 것이 중요합니다.
*   **불변 객체의 장점**: 불변 객체는 값이 같으면 행동적으로 동치로 간주될 수 있어 비교 및 추론이 단순해집니다. 이는 `equals` 메서드의 올바른 구현을 요구합니다.
*   **가변 객체의 복잡성**: 가변 객체는 상태가 변할 수 있기 때문에 단순한 값 비교만으로는 행동적 동치를 보장하기 어렵습니다. 이는 객체 복사(얕은 복사, 깊은 복사) 및 공유 상태 관리의 중요성과도 연결됩니다.

### 시험 포인트
*   **행동적 동치**의 정의를 정확히 이해하고 설명할 수 있어야 합니다. ⭐
*   **불변 객체**와 **가변 객체** 각각의 경우에 행동적 동치와 관찰적 동치 개념이 어떻게 적용되고 구분되는지 그 차이점을 설명할 수 있어야 합니다. ⭐
*   불변 객체에서 `equals` 메서드 구현의 중요성을 이해해야 합니다. ⭐

---

## Slide 50

## Example: LocalDate Revisited

**핵심 개념**:
객체 지향 프로그래밍에서 객체를 비교할 때 참조 동등성(`==`)과 값 동등성(`.equals()`)의 차이를 이해하는 것이 중요합니다. `LocalDate`와 같은 불변(Immutable) 객체는 내부 상태가 변경되지 않으므로, 값의 동등성을 확인하는 데 `equals()` 메서드가 주로 사용됩니다.

**코드/수식 해설**:
슬라이드의 Java 코드는 `LocalDate` 객체의 생성 및 비교 동작을 보여줍니다.

```java
LocalDate d1 = LocalDate.of(2025, 4, 14);
LocalDate d2 = LocalDate.of(2025, 4, 14);
LocalDate d3 = d2;

System.out.println(d1 == d2);       // output: false
System.out.println(d2 == d3);       // output: true

System.out.println(d1.equals(d2));  // output: true
System.out.println(d1.equals(d3));  // output: true
```
1.  `d1`과 `d2`는 동일한 날짜 값을 가지지만, `LocalDate.of()` 메서드를 두 번 호출하여 각각 **서로 다른 메모리 주소에 새로운 객체**를 생성합니다. 따라서 `d1`과 `d2`는 다른 객체를 참조합니다.
2.  `d3 = d2`는 `d3` 참조 변수가 `d2`가 참조하는 **동일한 객체**를 참조하도록 합니다. 즉, `d2`와 `d3`는 메모리 상에서 같은 객체를 가리킵니다.
3.  `d1 == d2`는 두 변수가 **동일한 객체를 참조하는지(참조 동등성)** 확인하므로 `false`를 반환합니다.
4.  `d2 == d3`는 두 변수가 **동일한 객체를 참조하는지** 확인하므로 `true`를 반환합니다.
5.  `d1.equals(d2)`는 두 객체의 **내부 값(날짜)이 동일한지(값 동등성)** 확인하므로 `true`를 반환합니다. `LocalDate`는 `equals()` 메서드를 오버라이드하여 값 비교를 수행합니다.
6.  `d1.equals(d3)`도 두 객체의 **내부 값(날짜)이 동일한지** 확인하므로 `true`를 반환합니다.

**강의 맥락**:
제공된 강의 음성 전사에는 본 슬라이드에 제시된 `LocalDate` 예시 및 `==`와 `.equals()`의 비교에 대한 직접적인 설명이 포함되어 있지 않습니다. 강의는 주로 클래스 명세, 추상화, 구현 상세, 표현 불변성(representation invariant), 그리고 Java의 불변(immutable) 객체(`String`, `Record`, `sealed interface` 등)와 관련된 깊은 개념들을 다루고 있습니다. 따라서 슬라이드의 내용에 직접적으로 일치하는 강의 구간은 찾을 수 없습니다.

**시험 포인트**:
*   ⭐Java에서 객체를 비교할 때 `==` 연산자는 **참조 동등성**을, `.equals()` 메서드는 **값 동등성**을 확인한다는 점을 명확히 이해해야 합니다.
*   ⭐`String`, `LocalDate` 등 Java의 주요 불변(Immutable) 객체들은 `equals()` 메서드를 오버라이드하여 값 비교를 제공한다는 것을 알아야 합니다.
*   ⭐불변 객체를 다룰 때 `==`와 `.equals()`의 사용법을 정확히 구분하는 것이 중요합니다.

---

## Slide 51

### 핵심 개념

이 슬라이드는 자바에서 `equals` 메서드를 올바르게 오버라이드(Override)하지 않고 오버로드(Overload)할 때 발생할 수 있는 흔한 실수를 보여줍니다. 특히, `@Override` 어노테이션을 사용했음에도 불구하고 `Object.equals(Object)`를 오버라이드하지 못하고 `equals(Point)`라는 새로운 메서드를 오버로드하게 되는 상황을 설명합니다.

*   **오버라이드(Override)**: 상위 클래스의 메서드와 동일한 시그니처(메서드 이름, 매개변수 타입 및 개수)를 가진 메서드를 하위 클래스에서 재정의하는 것입니다.
*   **오버로드(Overload)**: 같은 클래스 내에서 메서드 이름은 같지만 매개변수 시그니처가 다른 여러 메서드를 정의하는 것입니다.
*   **`Object.equals`**: 모든 자바 클래스의 최상위 부모인 `Object` 클래스에 정의된 메서드로, 두 객체가 논리적으로 동등한지 비교할 때 사용됩니다. 이 메서드를 올바르게 재정의하는 것은 컬렉션 사용 등 여러 상황에서 매우 중요합니다. `public boolean equals(Object obj)` 형태의 시그니처를 가집니다.

### 코드/수식 해설

```java
public class Point {
    private final int x;
    private final int y;
    // ... 생성자 등 다른 멤버

    @Override
    public boolean equals(Point p) { // 주의: 매개변수 타입이 Object가 아닌 Point
        return p.x == x && p.y == y;
    }
    // ...
}
```
위 코드에서 `equals(Point p)` 메서드는 `@Override` 어노테이션이 붙어 있지만, `Object` 클래스의 `equals(Object obj)` 메서드를 오버라이드하지 못합니다. 그 이유는 매개변수 타입이 `Object`가 아닌 `Point`이기 때문입니다. 따라서 이것은 `Object.equals`를 오버라이드하는 것이 아니라 `equals`라는 이름의 새로운 메서드를 오버로드하는 결과를 초래합니다. 최신 자바 컴파일러는 이 경우 `@Override` 어노테션 때문에 컴파일 에러를 발생시켜 이러한 실수를 방지해줍니다.

### 강의 맥락

교수님은 앞서 클래스 설계 시 상태 노출(representation exposure)을 피하고 불변 객체(immutable object)를 사용하는 중요성에 대해 설명한 후, 흔히 발생할 수 있는 또 다른 예시를 제시하며 이 슬라이드의 내용을 언급합니다. 특히, `equals` 메서드와 같이 중요한 `Object` 클래스의 메서드를 오버라이드할 때 시그니처를 잘못 지정하여 오버로딩이 발생하는 실수를 지적하고 있습니다. "some typing and some placing are different"라는 언급은 바로 메서드의 시그니처가 다름으로 인해 발생하는 문제를 가리키는 것으로 보입니다.

### 시험 포인트

*   ⭐ **`equals` 메서드 오버라이딩 규칙**: `Object.equals(Object obj)` 시그니처를 정확히 기억하고, 매개변수 타입이 `Object`여야 한다는 점을 아는 것이 중요합니다.
*   ⭐ **오버라이딩(Overriding)과 오버로딩(Overloading)의 차이**: 두 개념의 명확한 정의와 차이점을 이해하고 있어야 합니다.
*   ⭐ **`@Override` 어노테이션의 역할**: 이 어노테이션이 컴파일러에게 오버라이딩을 의도했음을 알려주어, 시그니처 불일치와 같은 실수를 컴파일 시점에 감지하는 데 도움을 준다는 점을 이해해야 합니다. 만약 `equals(Point p)` 위에 `@Override`가 붙어있으면, 컴파일 에러가 발생하여 개발자가 잘못된 오버라이딩을 했다는 것을 알려줍니다.

---

## Slide 52

**핵심 개념**:
이 슬라이드는 Java에서 `equals()` 메소드를 올바르게 오버라이딩하는 방법을 보여줍니다. 특히, 비교 대상 객체의 타입 안전성을 확보하기 위해 `instanceof` 연산자를 사용하여 명시적으로 타입을 확인하는 것이 핵심입니다. 이는 잘못된 타입의 객체와 비교할 때 발생할 수 있는 `ClassCastException`을 방지하고, 객체의 논리적인 동등성을 정확하게 판단하는 데 중요합니다.

**코드/수식 해설**:
`Point` 클래스는 `Object` 클래스의 `equals` 메소드를 오버라이딩하여 두 `Point` 객체가 동등한지 비교합니다.

```java
public class Point {
    // ... (다른 멤버 변수 및 메소드) ...

    @Override
    public boolean equals(Object o) {
        // 1. 'o'가 Point 클래스의 인스턴스인지 확인 (Java 16+의 instanceof 패턴 매칭)
        if (o instanceof Point p) {
            // 2. 만약 Point 인스턴스라면, 'o'를 Point 타입 'p'로 자동 캐스팅하여 x, y 값을 비교
            return p.x == x && p.y == y;
        }
        // 3. 'o'가 Point 인스턴스가 아니면, 동등하지 않으므로 false 반환
        return false;
    }

    // ... (다른 멤버 변수 및 메소드) ...
}
```
*   `@Override`: 이 메소드가 상위 클래스(`Object`)의 메소드를 재정의함을 나타냅니다.
*   `if (o instanceof Point p)`: 이 부분은 `o`가 `Point` 타입인지 확인하고, 만약 맞다면 해당 `o`를 `p`라는 `Point` 타입 변수로 캐스팅하여 `if` 블록 내에서 사용할 수 있게 합니다. 이는 `instanceof` 연산자에 추가된 패턴 매칭 기능(Java 16 이상)으로, 이전 버전에서는 `if (o instanceof Point) { Point p = (Point) o; ... }`와 같이 사용했습니다.
*   `return p.x == x && p.y == y;`: 두 `Point` 객체의 `x` 좌표와 `y` 좌표가 모두 같으면 `true`를 반환합니다.
*   `return false;`: 비교 대상 `o`가 `Point` 타입이 아니라면, 동등하다고 볼 수 없으므로 `false`를 반환합니다.

**구체적 예시**:
만약 `Point p1 = new Point(1, 2);`가 있고, `Object obj = "hello";`가 있다면, `p1.equals(obj)`를 호출할 때 `if (o instanceof Point p)` 조건은 `false`가 되어 바로 `false`를 반환합니다. 이로써 `ClassCastException` 발생 없이 안전하게 비교를 수행할 수 있습니다. `Point p2 = new Point(1, 2);`와 비교하는 `p1.equals(p2)`의 경우 `true`를 반환합니다.

**강의 맥락**:
제공된 전체 강의 음성 전사에서 현재 슬라이드(`Another Example (2): A Fix`)의 내용, 즉 `equals` 메소드 오버라이딩과 `instanceof` 연산자의 활용에 대한 직접적인 설명은 찾을 수 없습니다. 전사 내용 중 "Another example"이라는 언급이 있었으나, 이어진 내용은 슬라이드의 기술적 내용과 무관한 것으로 판단됩니다.

**시험 포인트**:
*   ⭐ `equals` 메소드를 올바르게 오버라이딩하는 방법 (동치성, 일관성, 대칭성, 전이성 등 `Object` 클래스 규약 준수)을 이해하는 것이 중요합니다.
*   ⭐ `equals` 메소드 내에서 비교 대상 객체의 타입을 확인하기 위해 `instanceof` 연산자를 사용하는 것이 중요하며, 이는 `ClassCastException` 방지에 필수적입니다.
*   ⭐ 자바 16+의 `instanceof` 패턴 매칭(`if (o instanceof Point p)`) 문법을 이해하고 활용할 수 있어야 합니다. (기존 방식: `if (o instanceof Point) { Point p = (Point) o; ... }`)

---

## Slide 53

**핵심 개념**
*   **`equals()` 메서드 오버라이딩 문제**: 객체 지향 프로그래밍에서 `equals()` 메서드를 올바르게 오버라이딩하는 것은 중요하며, 특히 상속 관계에서는 `equals` 계약의 **대칭성(Symmetry)** 원칙을 위반하기 쉽습니다.
*   **대칭성 원칙 위반**: 상위 클래스와 하위 클래스 객체 간 `equals()` 비교 시, `a.equals(b)`와 `b.equals(a)`의 결과가 달라지는 비대칭적인 상황이 발생할 수 있습니다.

**코드/수식 해설**

`ColorPoint` 클래스는 `Point` 클래스를 상속받아 색상(`color`) 정보를 추가한 예시입니다.

```java
class ColorPoint extends Point {
    private final Color color;
    // ...
    @Override
    public boolean equals(Object o) {
        if (o instanceof ColorPoint cp) { // o가 ColorPoint 타입인지 확인
            return super.equals(o) && cp.color == color; // 상위 클래스 비교 후 color 비교
        }
        return false; // ColorPoint 타입이 아니면 false 반환
    }
    // ...
}
```
위 `equals()` 메서드 구현은 `o`가 `ColorPoint` 타입인 경우에만 `super.equals()`를 호출하고 `color` 필드를 비교합니다. 만약 `o`가 `ColorPoint`가 아니라면 즉시 `false`를 반환합니다. 이 방식은 `equals` 계약의 대칭성 원칙을 위반하는 주요 원인이 됩니다.

**구체적 예시**

```java
Point p = new Point(1, 2);
ColorPoint cp = new ColorPoint(1, 2, RED);

System.out.println(p.equals(cp)); // true
System.out.println(cp.equals(p)); // false
```
1.  `p.equals(cp)` 호출 시: `Point` 클래스의 `equals` 메서드가 호출됩니다. `Point`는 `color` 필드를 알지 못하므로, `cp`가 `Point` 타입이며 `x`와 `y` 값이 같다면 `true`를 반환합니다.
2.  `cp.equals(p)` 호출 시: `ColorPoint` 클래스의 오버라이딩된 `equals` 메서드가 호출됩니다. 이 메서드는 `o instanceof ColorPoint` 조건을 먼저 확인하는데, `p`는 `Point` 타입이므로 이 조건이 `false`가 되어 즉시 `false`를 반환합니다.
이처럼 `p.equals(cp)`와 `cp.equals(p)`의 결과가 달라져 `equals`의 대칭성 원칙이 위반됩니다.

**강의 맥락**
*   객체 지향 프로그래밍에서 `equals` 메서드를 오버라이딩할 때 발생하는 중요한 문제점을 지적합니다.
*   특히, 상속 관계에서 `equals`를 구현할 때 `instanceof` 연산자를 사용하여 타입을 확인하는 방식이 `equals` 계약의 중요한 원칙인 **대칭성(Symmetry)**을 위반할 수 있음을 강조합니다.
*   `Point` 객체와 `ColorPoint` 객체를 비교하는 예시를 통해, `p.equals(cp)`는 `true`를 반환하지만 `cp.equals(p)`는 `false`를 반환하여 비교 결과가 비대칭적임을 시연합니다.

**시험 포인트**
*   ⭐ `equals` 메서드 오버라이딩 시 `instanceof` 사용으로 인한 **대칭성(Symmetry)** 위반 문제점을 이해하고 설명할 수 있어야 합니다. (Java의 `equals` 계약 5가지 원칙 중 하나)
*   ⭐ 위 예시(`Point`와 `ColorPoint` 간 비교)를 통해 `equals` 대칭성 위반이 어떻게 발생하는지 설명할 수 있어야 합니다.

---

## Slide 54

**핵심 개념**:
이 슬라이드는 `Point`를 상속받는 `ColorPoint` 클래스에서 `equals` 메서드를 재정의할 때 발생할 수 있는 문제점과 그 "잠재적 해결책"을 제시합니다. Java 16+의 `switch` 표현식과 패턴 매칭을 활용하여 인스턴스 타입에 따라 다른 비교 로직을 적용했지만, 이 구현은 대칭성(Symmetry)은 만족시키더라도 `equals` 계약의 핵심 속성인 추이성(Transitivity)을 위반하는 문제점을 가지고 있습니다.

**코드/수식 해설**:
`ColorPoint` 클래스의 `equals` 메서드 구현은 다음과 같습니다:
```java
class ColorPoint extends Point {
    // ...
    @Override
    public boolean equals(Object o) {
        return switch (o) {
            case ColorPoint cp -> super.equals(o) && cp.color == color;
            case Point _     -> super.equals(o);
            default          -> false;
        };
    }
    // ...
}
```
- `@Override`: `Object` 클래스의 `equals` 메서드를 오버라이딩합니다.
- `public boolean equals(Object o)`: 비교 대상 객체 `o`를 인자로 받습니다.
- `return switch (o)`: Java의 `switch` 표현식과 패턴 매칭을 사용하여 `o`의 런타임 타입에 따라 다른 로직을 적용합니다.
    - `case ColorPoint cp -> super.equals(o) && cp.color == color;`: 만약 `o`가 `ColorPoint` 타입이라면 `cp`로 자동 캐스팅되고, 부모 클래스(`Point`)의 `equals` 메서드를 호출하여 좌표가 같은지 확인한 후, `color` 필드도 같은지 추가로 검사합니다.
    - `case Point _ -> super.equals(o);`: 만약 `o`가 `Point` 타입이지만 `ColorPoint`는 아니라면(즉, 순수한 `Point` 객체라면), 부모 클래스(`Point`)의 `equals` 메서드만 호출하여 좌표만으로 비교합니다. 여기서 `_`는 변수 이름을 사용하지 않음을 나타냅니다.
    - `default -> false;`: 위 두 케이스에 해당하지 않는 다른 타입의 객체는 `false`를 반환하여 같지 않다고 처리합니다.

**구체적 예시**:
슬라이드 하단의 코드는 이 `equals` 구현이 추이성을 위반하는 경우를 보여줍니다:
```java
ColorPoint p1 = new ColorPoint(1, 2, RED);    // (1,2) RED
Point p2 = new Point(1, 2);                   // (1,2)
ColorPoint p3 = new ColorPoint(1, 2, BLUE);   // (1,2) BLUE

System.out.println(p1.equals(p2)); // true
System.out.println(p2.equals(p3)); // true
System.out.println(p1.equals(p3)); // false
```
1. `p1.equals(p2)`: `p1`은 `ColorPoint`이고 `p2`는 `Point`입니다. `p1`의 `equals` 메서드 내 `switch`문은 `case Point _`에 매치되어 `super.equals(p2)`를 호출합니다. `Point(1,2)`와 `Point(1,2)`는 같으므로 `true`를 반환합니다.
2. `p2.equals(p3)`: `p2`는 `Point`이고 `p3`는 `ColorPoint`입니다. (가정하건대) `Point` 클래스의 `equals`는 좌표만 비교하므로 `Point(1,2)`와 `Point(1,2)`는 같아 `true`를 반환합니다.
3. `p1.equals(p3)`: `p1`과 `p3` 모두 `ColorPoint`입니다. `p1`의 `equals` 메서드 내 `switch`문은 `case ColorPoint cp`에 매치됩니다. `super.equals(p3)`는 좌표가 같으므로 `true`이지만, `p1.color (RED)`와 `cp.color (BLUE)`는 다르므로 `false`를 반환합니다.

결론적으로 ($p1=p2$)이고 ($p2=p3$)이지만 ($p1 \ne p3$)이므로, `equals`의 추이성($a=b$ 이고 $b=c$ 이면 $a=c$이다)이 위반됩니다.

**강의 맥락**:
이 슬라이드는 `equals` 메서드의 올바른 구현이 얼마나 복잡한 문제인지 보여주는 예시입니다. 특히 상속 계층 구조에서 `equals`를 재정의할 때 대칭성(Symmetry), 추이성(Transitivity)과 같은 `equals` 계약의 핵심 원칙을 유지하기 어렵다는 점을 강조합니다. 교수님은 앞서 `switch` 패턴 매칭과 `record` 타입을 포함한 Java의 최신 문법을 설명했는데, 이 슬라이드는 이러한 문법적 개선 사항을 활용하여 `equals`를 구현하더라도, 객체지향 설계 원칙과 `equals` 계약의 미묘한 부분을 놓치면 의도치 않은 문제가 발생할 수 있음을 지적하고 있습니다. 이는 단순한 코딩 스킬을 넘어, `equals`와 같은 핵심 메서드의 속성에 대한 깊이 있는 이해가 중요함을 역설합니다.

**시험 포인트**:
- ⭐ **`equals` 계약 위반**: 상속 관계에서 `equals`를 재정의할 때 추이성을 위반하는 이 예시의 문제점을 정확히 설명할 수 있어야 합니다.
- ⭐ **`switch` 패턴 매칭**: Java 16+의 `switch` 표현식과 패턴 매칭 문법이 `equals` 구현에 어떻게 활용되었는지 이해하고, 특정 타입에 대한 처리 로직을 구분하는 방법을 설명할 수 있어야 합니다.
- ⭐ **`equals`의 속성**: `equals` 메서드가 갖춰야 할 5가지 속성(반사성, 대칭성, 추이성, 일관성, null 처리)을 명확히 이해하고, 이 예시가 어떤 속성을 위반하는지 설명할 수 있어야 합니다.

---

## Slide 55

**핵심 개념**
이 슬라이드는 객체 지향 언어에서 `Object.equals` 메서드를 오버라이딩(overriding)하면서 상속(subclassing)을 사용할 때 발생하는 근본적인 문제점을 다룹니다. 특히, 확장 가능한 클래스에 새로운 값 컴포넌트를 추가할 경우 `equals` 계약(contract)을 유지하기 어렵다는 것이 핵심입니다.

`Object.equals` 메서드를 올바르게 오버라이딩하려면 다음 세 가지 속성을 만족해야 합니다:
1.  **반사성(Reflexivity)**: 모든 null이 아닌 참조 값 `$x$`에 대해 `$x.equals(x)$`는 `true`를 반환해야 합니다.
2.  **대칭성(Symmetry)**: 모든 null이 아닌 참조 값 `$x, y$`에 대해 `$x.equals(y)$`가 `true`를 반환하면 `$y.equals(x)$`도 `true`를 반환해야 합니다.
3.  **추이성(Transitivity)**: 모든 null이 아닌 참조 값 `$x, y, z$`에 대해 `$x.equals(y)$`가 `true`를 반환하고 `$y.equals(z)$`도 `true`를 반환하면 `$x.equals(z)$`도 `true`를 반환해야 합니다.

클래스를 상속하여 새로운 필드를 추가하고 `equals`를 오버라이딩할 때 이 대칭성 및 추이성 속성이 깨지기 쉽습니다.

**구체적 예시**
고전적인 예시로 `Point` 클래스를 상속하여 `ColorPoint` 클래스를 만들 때 이 문제가 발생합니다.
-   `Point`는 `$x, y$` 좌표를 가집니다.
-   `ColorPoint`는 `$x, y$` 좌표와 추가로 `Color`를 가집니다.
만약 `ColorPoint`가 `Point`를 상속받아 `equals`를 오버라이딩하면, `Point` 객체와 `ColorPoint` 객체를 비교할 때 `equals` 계약이 위반될 수 있습니다.

**문제 해결을 위한 접근법**:
1.  **상속보다는 컴포지션(Composition) 사용 (Composition over subclassing)**:
    `ColorPoint`가 `Point`를 상속받는 대신, `ColorPoint` 내부에 `Point` 인스턴스를 필드로 포함(contain)하는 방식입니다. 이 방식은 `equals` 계약을 유지하면서 새로운 기능을 추가할 수 있는 강력한 대안입니다.
2.  **추상 클래스(Abstract Class) 사용**:
    `Point`와 `ColorPoint` 모두 공통의 추상 클래스의 서브클래스로 선언하여, `equals` 메서드를 추상 클래스에서 정의하거나 각 서브클래스에서 독립적으로 구현하도록 합니다. 이는 두 클래스 간의 동등성 비교 방식을 명확히 분리할 수 있게 합니다.

**강의 맥락**
교수님은 이전 슬라이드까지 클래스 명세(class specification)의 중요성, 추상화 함수(abstraction function), 표현 불변식(representation invariant), 그리고 내부 표현 노출(representation exposure) 문제에 대해 자세히 설명했습니다. 특히 `final` 키워드, 불변 객체(immutable object), Java `record` 및 `sealed` 인터페이스/클래스를 통한 안전하고 견고한 객체 설계를 강조했습니다.

이 슬라이드는 이러한 견고한 객체 설계의 연장선상에서 발생하는 고급 문제 중 하나인 `equals` 오버라이딩과 상속의 충돌을 다룹니다. `Effective Java`의 인용구를 통해 이 문제가 객체 지향 추상화의 이점을 포기하지 않고는 해결하기 어렵다는 점을 강조하며, 컴포지션이나 추상 클래스 사용과 같은 실용적인 해결책을 제시합니다. 이는 단순히 기능 구현을 넘어 올바르고 유지보수 가능한 객체 지향 시스템을 구축하기 위한 중요한 설계 원칙입니다.

**시험 포인트**
*   ⭐`Object.equals` 메서드의 세 가지 계약 속성(반사성, 대칭성, 추이성)을 정확히 이해하고 설명할 수 있어야 합니다.
*   ⭐상속과 `equals` 오버라이딩 시 발생하는 문제점(특히 대칭성 및 추이성 위반)을 알고 있어야 합니다.
*   ⭐문제 해결을 위한 두 가지 주요 대안: "상속보다는 컴포지션(Composition over subclassing)"과 "추상 클래스 사용"에 대해 설명할 수 있어야 합니다.
*   ⭐"Effective Java, Item 10"의 `equals` 계약 관련 인용구의 의미를 이해하는 것이 중요합니다.

---

## Slide 56

### 핵심 개념
이 슬라이드는 복합 객체(composite object)에서 깊은 불변성(deep immutability)을 달성하는 것이 얼마나 어려운지, 그리고 내부 가변 객체(mutable object)를 직접 반환할 때 발생할 수 있는 표현 노출(representation exposure) 문제를 보여주는 예시입니다. `private final` 키워드만으로는 객체 전체의 불변성을 보장하기에 불충분하며, 내부 객체까지 불변해야 진정한 불변성을 얻을 수 있음을 강조합니다.

### 코드 해설
주어진 `ColorPoint` 클래스는 `Point`와 `Color` 타입의 두 필드를 가집니다.

```java
class ColorPoint {
    private final Point point;
    private final Color color;
    // ...
    @Override
    public boolean equals(Object o) {
        if (o instanceof ColorPoint cp) { // Java 16+ pattern matching for instanceof
            return cp.point.equals(point) && cp.color.equals(color);
        } else {
            return false;
        }
    }
    // Returns the point-view of this color point.
    public Point asPoint() {
        return point; // Potential representation exposure!
    }
    // ...
}
```

*   `private final Point point;` 와 `private final Color color;`
    *   `private`는 외부에서 직접 필드에 접근하는 것을 막고, `final`은 이 참조 변수($\text{point}$와 $\text{color}$)가 초기화된 후 다른 객체를 참조하도록 변경될 수 없음을 의미합니다.
    *   하지만 `final`은 참조 변수 자체를 변경할 수 없게 할 뿐, 참조되는 객체(`Point`와 `Color` 인스턴스)의 내부 상태가 변경되는 것을 막지는 못합니다. 만약 `Point`나 `Color` 클래스 자체가 가변(mutable) 객체라면, `ColorPoint`는 완전한 불변 객체가 될 수 없습니다.
*   `public boolean equals(Object o)`
    *   `ColorPoint` 객체의 동등성(equality)을 비교하기 위해 `equals` 메서드를 오버라이드했습니다.
    *   인자로 받은 객체 `o`가 `ColorPoint`의 인스턴스이고, 그 `ColorPoint`의 $\text{point}$와 $\text{color}$ 필드가 현재 객체의 $\text{point}$와 $\text{color}$ 필드와 각각 동일한지 확인합니다. 이는 일반적으로 값 객체(Value Object)의 `equals` 구현 방식입니다.
*   `public Point asPoint()`
    *   이 메서드는 `ColorPoint` 객체 내부의 `point` 필드에 대한 참조를 직접 반환합니다.
    *   만약 `Point` 클래스가 가변 객체라면, 이 메서드를 통해 반환된 `Point` 객체의 상태를 외부에서 변경할 수 있습니다. 이는 곧 `ColorPoint` 객체의 내부 상태를 외부에서 변경하는 것이 되어, `ColorPoint`가 불변이라고 기대했던 속성을 위반하게 됩니다. 이것이 바로 **표현 노출(representation exposure)**의 전형적인 예시입니다.

### 강의 맥락
교수님께서는 `private`과 `final` 키워드, 그리고 `record` 타입을 사용하여 불변 객체를 만드는 좋은 관행에 대해 설명한 후, **"declaring everything in mutual is a challenging all the time"** (모든 것을 불변으로 선언하는 것은 항상 어렵다)라는 점을 강조하며 이 슬라이드를 소개했습니다.

특히, `IntTree` 예시에서 `integer`와 같은 기본 타입은 불변이라 문제가 없었지만, 만약 내부 노드의 값이 `public` 필드를 가진 가변 클래스 `A`였다면 문제가 발생한다고 지적하셨습니다. `record` 타입이 `private` 필드와 getter만 제공하여 겉으로는 불변처럼 보이지만, "If the return member variable is still mutable, Then, you can, after creating a record, you just get any member variable, and modify the member variable directly, then you will change the entire code." (만약 반환되는 멤버 변수가 여전히 가변이라면, record를 생성한 후 해당 멤버 변수를 가져와 직접 수정할 수 있고, 이는 전체 코드의 변경으로 이어진다)라고 설명하시며, **내부에서 사용하는 객체가 가변일 경우 완벽한 불변성을 보장하기 어렵다**는 점을 강조하셨습니다.

이 `ColorPoint` 예시는 이러한 맥락에서 `asPoint()` 메서드가 내부의 `point` 객체에 대한 참조를 그대로 반환함으로써, 만약 `Point` 객체가 가변이라면 외부에서 `ColorPoint`의 내부 상태를 변경할 수 있는 '표현 노출'의 위험을 보여줍니다. 이는 `private final` 필드만으로는 진정한 **깊은 불변성**을 달성하기 어렵다는 점을 구체적으로 보여주는 사례입니다.

### 시험 포인트
*   **표현 노출(Representation Exposure)**: 내부의 가변 객체 참조를 외부로 직접 반환할 때 발생하며, 이는 객체의 캡슐화를 위반하고 불변성을 깨뜨릴 수 있음을 이해해야 합니다. ⭐
*   **얕은 불변성(Shallow Immutability) vs. 깊은 불변성(Deep Immutability)**: `private final`은 참조가 가리키는 객체를 변경할 수 없게 할 뿐, 참조되는 객체의 상태 변경은 막지 못합니다(얕은 불변성). 진정한 불변성은 내부의 모든 멤버 객체까지도 불변해야 합니다(깊은 불변성). ⭐
*   이러한 문제를 해결하기 위한 방안으로 **방어적 복사(defensive copy)** (내부 가변 객체를 반환하기 전에 복사본을 만들어 반환)나, 내부 객체 자체를 **불변 객체**로 디자인하는 방법이 있음을 알아두세요. (강의에서는 "deep cutting" 즉, 딥 카피를 언급했습니다.) ⭐

---

## Slide 57

**핵심 개념**
`Object.hashCode()` 메서드는 객체에 대한 해시 코드 정수 값을 반환하며, `java.util.HashMap`과 같은 해시 테이블에서 객체를 효율적으로 저장하고 검색하는 데 사용됩니다.

이 메서드는 다음과 같은 두 가지 중요한 계약(Contracts)을 따릅니다:
1.  객체 `o`의 정보가 변경되지 않는 한, `o.hashCode()`가 반환하는 값은 항상 동일해야 합니다.
2.  두 객체 `a`와 `b`가 `a.equals(b)` 메서드에 의해 동등하다고 판단되면, `a.hashCode()`와 `b.hashCode()`는 반드시 같은 값을 반환해야 합니다.

**강의 맥락**
현재 제공된 강의 음성 전사에는 `Object.hashCode`에 대한 직접적인 설명이나 강조 내용이 포함되어 있지 않습니다.

**시험 포인트**
*   ⭐ `equals()` 메서드를 오버라이드할 경우, 반드시 `hashCode()` 메서드도 함께 오버라이드해야 합니다. 이는 해시 기반 컬렉션(예: `HashMap`, `HashSet`)이 올바르게 동작하도록 보장하기 위함입니다.
*   ⭐ `equals()`와 `hashCode()` 메서드 간의 계약 관계 (즉, `a.equals(b)`가 참이면 `a.hashCode() == b.hashCode()`여야 한다는 조건)를 이해하는 것이 중요합니다.

---

## Slide 58

**핵심 개념**
본 슬라이드는 소프트웨어 작성 원리 (CSED232) 강의에서 다루는 주요 개념들에 대한 참고 자료 목록을 제시합니다. 주로 `Core Java`와 `Effective Java` 서적의 특정 챕터들, B. Liskov의 "Program Development in Java" 챕터 5, 그리고 Wikipedia의 "Class invariant" 항목을 참고할 수 있도록 안내하고 있습니다.

**강의 맥락**
제공된 강의 음성 전사에서는 이 'References' 슬라이드에 대한 직접적인 언급이나 설명이 없습니다. 교수님은 이전 강의 내용 요약과 현재 강의의 주요 개념(클래스 명세, 추상화, 표현 불변식, 불변 객체, 레코드, 패턴 매칭 등)에 대해 설명하고 있습니다.

**시험 포인트**
강의에서 직접적으로 언급되지 않았으므로 이 슬라이드 자체에서 특정 시험 포인트를 도출하기는 어렵습니다. 하지만 언급된 참고 자료들은 강의 내용의 심화 학습에 도움이 될 수 있습니다.

---

## Slide 59

- **핵심 개념**: 본 슬라이드는 강의의 중요한 내용 전달 후 학생들이 질문할 시간을 주기 위한 목적으로 제시되었습니다.

- **강의 맥락**: 교수님은 주요 강의 내용(클래스 스펙, 구현과 추상화의 관계, 표현 노출 문제, 불변 객체, Java Record 및 패턴 매칭)을 모두 설명한 후 학생들에게 질문할 기회를 제공하며 다음과 같이 말했습니다:

    > "Okay. So today, we are talking about the data. Thank you. I'm sorry. So here is a piece of paper. This is 53 years ago. Is there any 50p? If you have a new one, Okay, thank you. Do you have a video on the video? Is it possible for you to do the video? Or is it possible for you to do the video? Or is it possible for you to do the video? I think it's a big deal. I think it's a big deal. I think it's a big deal. I think it's a big deal. I think it's a big deal. I think it's a big deal. I think it's a big deal. I think it's a big deal. I don't know. I think it's a lot. I think it's a lot of time. I think it's a lot of time. I think it's a lot of time. I think it's a lot of time. I think it's a lot of time. I think it's a lot of time. I think it's hard to do this. I think it's hard to do this. Do you have any other time to do this? Do you have any other time? Do you have any other time? It's about 10-30. I think it's about 10-30. 10-30. I think it's about 10-30. The option is to use the option to use the option. The option is to use the option. The option is to use the option. If you do this, I will use the option to use the option. I'm not sure how to do this. I'm not sure how to do this online, but I'm not sure how to do this. I'm not sure how to do this. I'm not sure how to do this. Okay. Two more questions. I'll ask you a question. Next exercise is the rest of the day."

    이는 강의의 핵심 내용을 마무리하고 질의응답 및 다음 과제 안내 등으로 넘어가는 전환 시점에 해당합니다.

- **시험 포인트**: 수업 내용을 명확히 이해하고 궁금한 점을 질문하여 해결하는 것은 학습에 매우 중요합니다. ⭐ 이해가 되지 않는 부분이 있다면 적극적으로 질문하는 자세를 가지는 것이 좋습니다.

---
