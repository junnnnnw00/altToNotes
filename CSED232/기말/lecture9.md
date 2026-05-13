# CSED232 - lecture9 상세 해설 노트

> 이 노트는 Gemini 3 Flash를 이용해 자동 생성되었습니다.

---

## Slide 1

## CSED232: Subtypes and Generics (강의 개요)

- **핵심 개념**
    - **서브타입 (Subtypes)**: 한 타입의 객체가 다른 타입의 객체를 대신하여 사용될 수 있는 관계를 의미하며, 주로 클래스 상속을 통해 구현됩니다.
    - **제네릭 (Generics)**: 데이터 타입을 매개변수화하여, 하나의 코드가 다양한 타입에 대해 동작하도록 만드는 기법입니다 (C++에서는 `template`으로 구현).

- **코드/수식 해설**
    - **서브타입 관계의 수학적 표기**: 타입 $S$가 $T$의 서브타입일 때, 보통 $S <: T$로 표기합니다. 이는 $T$가 기대되는 모든 문맥에서 $S$를 안전하게 사용할 수 있음을 뜻합니다.

- **구체적 예시**
    - **Subtyping**: `class Dog : public Animal` 관계에서 `Dog` 객체를 `Animal` 포인터로 가리키는 것.
    - **Generics**: `std::vector<int>`나 `std::vector<string>`처럼 동일한 리스트 로직을 다른 타입에 적용하는 것.

- **시험 포인트**
    - ⭐ **다형성(Polymorphism)의 분류**: 서브타입 다형성(Subtype Polymorphism)과 매개변수 다형성(Parametric Polymorphism, Generics)의 개념적 차이와 활용 목적을 구분하는 문제가 자주 출제됩니다.

---

## Slide 2

- **핵심 개념**: **서브타입(Subtypes)**은 객체지향 프로그래밍에서 특정 타입($S$)의 객체가 다른 타입($T$)의 객체가 필요한 곳에 대신 사용될 수 있는 관계를 의미합니다. 이는 주로 상속(Inheritance)을 통해 구현되며, 인터페이스의 호환성을 보장합니다.

- **코드/수식 해설**:
  - 타입 $S$가 타입 $T$의 서브타입임을 수학적으로 다음과 같이 표기합니다:
    $$S <: T$$
  - C++에서 서브타입 관계를 형성하는 기본적인 문법:
    ```cpp
    class T { ... };           // 슈퍼타입 (Base class)
    class S : public T { ... }; // 서브타입 (Derived class)
    ```

- **구체적 예시**: 
  - `Shape`가 상위 타입이고 `Circle`이 이를 상속받는다면, `Circle`은 `Shape`의 서브타입입니다 ($Circle <: Shape$). 따라서 `Shape` 포인터가 필요한 함수에 `Circle` 객체를 전달할 수 있습니다.

- **시험 포인트**: 
  - ⭐ **리스코프 치환 원칙(Liskov Substitution Principle, LSP)**: 서브타입 객체는 프로그램의 정확성을 깨뜨리지 않으면서 언제나 슈퍼타입 객체로 치환 가능해야 함을 이해해야 합니다.
  - ⭐ **상속 vs 서브타이핑**: 단순히 코드를 재사용하는 '구현 상속'과 인터페이스 호환성을 유지하는 '서브타이핑'의 차이점이 자주 출제됩니다.

---

## Slide 3

### B is a Subtype of A (서브타입 관계)

**핵심 개념**
*   **Subtyping**: 객체 $B$가 객체 $A$의 서브타입($B <: A$)이라는 것은, $A$ 타입의 객체가 필요한 모든 곳에 $B$ 타입의 객체를 안전하게 사용할 수 있음을 의미합니다 (Liskov Substitution Principle의 기초).
*   **Stronger Specification**: 서브타입 $B$의 명세는 슈퍼타입 $A$의 명세보다 최소한 같거나 더 **강해야(strong)** 합니다. 즉, $B$는 $A$가 약속한 모든 동작을 보장하며, 더 엄격한 조건을 만족해야 합니다.
*   **Class Invariant**: 클래스가 생성된 후 유지되어야 하는 상태의 조건인 '클래스 불변식' 역시 서브타입에서 더 강해야 합니다.

**수식 해설**
*   **서브타입 관계 표기**: $B <: A$ (B는 A의 서브타입)
*   **명세의 강도**: $Spec_{B} \implies Spec_{A}$
    *   $B$의 명세가 $A$의 명세를 함의해야 함을 의미합니다.
*   **메소드 명세의 강화**:
    *   Precondition(사전 조건): $Pre_{A} \implies Pre_{B}$ (서브타입은 더 적은 조건을 요구할 수 있음 - Weaker)
    *   Postcondition(사후 조건): $Post_{B} \implies Post_{A}$ (서브타입은 더 많은 결과/엄격한 상태를 보장해야 함 - Stronger)
*   **클래스 불변식(Class Invariant)**: $Inv_{B} \implies Inv_{A}$
    *   $B$의 불변식 $Inv_{B}$는 $A$의 불변식 $Inv_{A}$를 항상 만족해야 합니다.

**구체적 예시**
*   **클래스 관계**: `Square` (정사각형)가 `Rectangle` (직사각형)의 서브타입인 경우
    *   `Rectangle`의 불변식 ($Inv_{A}$): "네 각이 모두 90도이다."
    *   `Square`의 불변식 ($Inv_{B}$): "네 각이 모두 90도이고, **네 변의 길이가 모두 같다.**"
    *   결과: $Inv_{B}$는 $Inv_{A}$를 포함하며 더 구체적이므로 더 강한(stronger) 불변식입니다.

**시험 포인트**
*   ⭐ 서브타입의 명세는 슈퍼타입보다 항상 **Stronger** 해야 함을 기억하세요. (Weaker이면 안 됨)
*   ⭐ **Behavioral Subtyping**: 단순히 문법적인 상속을 넘어, 서브타입이 슈퍼타입의 행위적 계약(contract)을 모두 준수하는지 묻는 문제가 출제될 수 있습니다.
*   ⭐ 메소드 오버라이딩 시, 서브타입의 메소드는 슈퍼타입보다 더 강한 사후 조건(Postcondition)을 가져야 한다는 점이 중요합니다.

---

## Slide 4

### 핵심 개념
- **계약에 의한 설계 (Design by Contract)**: 클래스와 메서드의 동작을 명확한 제약 조건(불변식, 사전 조건, 사후 조건)으로 정의하는 기법입니다.
- **불변식 (Invariant)**: 객체의 생명 주기 동안 항상 참이어야 하는 조건입니다. 상속 시 하위 클래스는 부모의 불변식을 유지하거나 더 강화할 수 있습니다.
- **사전 조건 (Pre-condition, `requires`)**: 메서드 실행 전에 호출자가 만족시켜야 하는 조건입니다.
- **사후 조건 (Post-condition, `ensures`)**: 메서드 실행 후 해당 메서드가 보장해야 하는 결과입니다. `\old()`는 실행 전의 값을 참조합니다.
- **Specification Strengthening**: 하위 클래스($Car$)는 상위 클래스($Vehicle$)보다 더 구체적이고 엄격한 제약 조건을 가질 수 있습니다.

### 코드/수식 해설
- **불변식 강화**:
    - $Vehicle$: $speed < limit$
    - $Car$: $speed < limit \land fuel \ge 0$
    - $Car$는 $Vehicle$의 조건을 포함하면서 추가 조건($fuel \ge 0$)을 가지므로 더 강력한(Stronger) 명세를 가집니다.
- **메서드 명세 (`brake`)**:
```java
//@ requires: speed > 0
//@ ensures: speed < \old(speed)
void brake();
```
- 사전 조건: $speed > 0$일 때만 호출 가능합니다.
- 사후 조건: 실행 후의 $speed$는 실행 전의 $speed$($\old(speed)$)보다 작아야 함을 보장합니다.

### 구체적 예시
- **불변식 비교**: $Vehicle$에서는 $speed$와 $limit$의 관계만 정의하지만, $Car$에서는 $fuel$이라는 새로운 상태 변수에 대한 제약($fuel \ge 0$)을 추가하여 객체의 유효 상태를 더 좁게 제한합니다.
- **행위적 서브타이핑**: $Car$는 $Vehicle$이 할 수 있는 모든 동작($brake$)을 수행하면서도, 자신만의 동작($start$)과 더 엄격한 상태 관리를 수행합니다.

### 시험 포인트
- ⭐ **Liskov Substitution Principle (LSP)**: 자식 클래스는 부모 클래스의 명세를 위반해서는 안 됩니다. (불변식 강화, 사전 조건 완화, 사후 조건 강화는 허용됨)
- ⭐ **`\old(expression)`**: 사후 조건에서 메서드 호출 전의 상태 값을 참조하기 위해 사용되는 문법임을 숙지하세요.
- ⭐ **Stronger Specification**: 상속 관계에서 "더 강한 명세"가 의미하는 바(더 많은 제약 조건 추가)를 논리 기호($\land$)와 연결하여 이해해야 합니다.

---

## Slide 5

### 핵심 개념
- **Behavioral Subtyping (행위적 서브타이핑)**: 서브클래스(`HybridCar`)는 부모 클래스(`Car`)의 명세(Specification)를 준수해야 하며, 부모 객체가 사용되는 곳에 자식 객체를 대신 넣어도 프로그램의 논리적 일관성이 깨지지 않아야 합니다.
- **Design by Contract (DbC)**: 클래스와 메서드에 대해 `invariant`(불변 조건), `requires`(사전 조건), `ensures`(사후 조건)를 정의하여 소프트웨어의 정확성을 보장하는 방법론입니다.
- **명세의 강도 (Strength of Specification)**: 서브클래스는 부모보다 **사전 조건을 완화(`weaken`)**하거나 **사후 조건을 강화(`strengthen`)**할 수 있습니다. 슬라이드에서는 `HybridCar`가 더 강력한 명세를 가짐을 보여줍니다.

### 코드/수식 해설
- **`invariant` (불변 조건)**: 객체의 생명 주기 동안 항상 참이어야 하는 조건입니다.
    - `Car`: `speed < Limit && fuel >= 0`
    - `HybridCar`: 상속받은 조건에 `charge >= 0`이 추가됨.
- **`start()` 메서드의 사전 조건 변화 ($Pre_{Car} \leftarrow Pre_{Hybrid}$)**:
    - `Car`: `fuel > 0` (연료 필수)
    - `HybridCar`: `charge > 0 || fuel > 0` (연료나 전력 중 하나만 있어도 됨)
    - $Pre_{Car} \implies Pre_{Hybrid}$ 이므로 사전 조건이 **완화**되었습니다.
- **`brake()` 메서드의 사후 조건 변화 ($Post_{Hybrid} \implies Post_{Car}$)**:
    - `Car`: `speed < \old(speed)` (속도 감소)
    - `HybridCar`: `speed < \old(speed) && charge > \old(charge)` (속도 감소 + 에너지 회생 충전)
    - $Post_{Hybrid}$가 $Post_{Car}$의 내용을 포함하므로 사후 조건이 **강화**되었습니다.

### 구체적 예시
1. **사전 조건 완화**: `Car`는 연료가 없으면 시동을 못 걸지만, `HybridCar`는 배터리만 있어도 시동을 걸 수 있어 호출자가 더 넓은 범위의 상태에서 메서드를 사용할 수 있습니다.
2. **사후 조건 강화**: `brake()` 호출 시 `Car`는 단순히 감속만 보장하지만, `HybridCar`는 감속과 동시에 `charge` 증가라는 추가적인 보장을 제공합니다.

### 시험 포인트
- ⭐ **Liskov Substitution Principle (LSP)**: 자식 클래스는 부모 클래스의 계약을 어겨서는 안 됩니다. (사전 조건 강화 금지, 사후 조건 완화 금지)
- ⭐ **`\old(v)` 기호**: 메서드 실행 전의 변수 $v$ 값을 참조할 때 사용하며, 사후 조건 정의 시 필수적입니다.
- ⭐ **명세 비교**: 어떤 클래스의 명세가 더 강력한지 판단할 때, $Pre$는 더 넓은 범위(더 쉬운 조건)를 허용하는지, $Post$는 더 좁은 범위(더 구체적인 결과)를 보장하는지 확인해야 합니다.

---

## Slide 6

### 핵심 개념: 리스코프 치환 원칙 (Liskov Substitution Principle, LSP)
리스코프 치환 원칙은 객체지향 설계의 기본 원칙 중 하나로, 서브타입(Subtype) 관계에 있는 두 타입 간의 **행위적 일관성**을 정의합니다.
- **정의**: 타입 $B$가 타입 $A$의 서브타입이라면, 프로그램의 동작을 방해하지 않고 $A$의 인스턴스를 $B$의 인스턴스로 치환할 수 있어야 합니다.
- **핵심 목표**: 상위 타입 $A$를 기반으로 작성된 코드가 하위 타입 $B$를 사용하더라도 논리적으로 정확하게 동작함을 보장하는 것입니다.

### 코드/수식 해설
LSP를 만족하기 위한 명세(Specification)의 변화 규칙은 다음과 같습니다:
- **명세 강화 (Strengthening)**: 서브타입 $B$는 명세를 강화할 수 있습니다.
  - $B$에서 오버라이딩된 메서드는 $A$의 메서드보다 더 강하거나(Stronger) 같은 수준의 명세를 가져야 합니다.
  - 새로운 메서드를 추가할 수 있으나, 기존의 불변성(Invariants)을 유지해야 합니다.
- **명세 약화 금지 (Weakening)**: 서브타입 $B$는 명세를 약화할 수 없습니다.
  - $A$로부터 상속받은 메서드를 임의로 제거할 수 없습니다.
  - 오버라이딩된 메서드가 $A$의 기존 명세보다 약한(Weaker) 조건을 가져서는 안 됩니다.

### 구체적 예시
어떤 함수 $f$가 클래스 `Shape`를 매개변수로 받는다고 가정할 때:
```cpp
void render(Shape* s) {
    s->draw(); // Shape의 명세를 기대함
}
```
- 만약 `Circle`이 `Shape`의 서브타입이라면, `render(new Circle())`은 `Shape`가 정의한 모든 속성과 동작을 충실히 수행해야 합니다.
- 만약 `Circle`에서 `draw()` 메서드를 제거하거나, 호출 시 기존에 없던 예외를 던진다면 이는 명세 약화에 해당하며 LSP 위반입니다.

### 시험 포인트
- ⭐ **치환 가능성(Substitutability)**: "서브타입은 언제나 슈퍼타입을 대신할 수 있어야 한다"는 명제가 LSP의 핵심입니다.
- ⭐ **명세의 강화 vs 약화**: 서브타입에서 메서드를 오버라이딩할 때, **사전 조건(Pre-condition)은 완화**될 수 있고 **사후 조건(Post-condition)은 강화**될 수 있다는 개념과 연결됩니다. (슬라이드에서는 포괄적으로 "Stronger specification"으로 표현됨)
- ⭐ **불변성(Invariants) 유지**: 하위 클래스에서 어떤 기능을 추가하더라도 상위 클래스가 보장하던 객체의 상태(Invariant)가 깨져서는 안 됩니다.

---

## Slide 7

### 핵심 개념

메서드 오버라이딩(Overriding) 시 부모 클래스와 자식 클래스 간의 타입 관계를 정의하는 세 가지 원칙입니다.

1.  **반공변성 (Contravariance)**: 더 넓은 범위의 타입(Supertype)으로 교체되는 성질. 이론적으로 메서드 인자(Argument)에 적용될 수 있습니다.
2.  **불변성 (Invariance)**: 타입이 반드시 일치해야 하는 성질. Java 등 많은 언어는 메서드 인자에 대해 이 규칙을 적용합니다.
3.  **공변성 (Covariance)**: 더 좁은 범위의 타입(Subtype)으로 교체되는 성질. 메서드 반환 타입(Return type)과 예외 처리에 적용됩니다.

---

### 코드/수식 해설

*   **메서드 인자 (Method Arguments)**:
    *   이론적 원칙: $T_{sub} \leq T_{super}$ 일 때, 메서드 인자는 $T_{super}$로 확장 가능(Contravariant).
    *   Java/C++의 실제: 인자 타입이 다르면 오버라이딩이 아닌 **오버로딩(Overloading)**으로 처리됨. 즉, 인자에 대해서는 **불변성(Invariance)**을 유지해야 함.

*   **메서드 결과 (Method Results)**:
    *   반환 타입: 부모 메서드의 반환 타입이 $R_{super}$라면, 자식은 $R_{sub}$를 반환할 수 있음 (**Covariance**).
    *   예외(Exception): 부모가 던지는 예외 $E_{super}$에 대해 자식은 그 하위 예외인 $E_{sub}$만 던질 수 있음. 새로운 예외를 선언하는 것은 불가능함.

---

### 구체적 예시

```cpp
class Animal {};
class Dog : public Animal {};

class Base {
public:
    virtual Animal* getProcess(Dog* d);
};

class Derived : public Base {
public:
    // Covariant Return Type: Animal* 대신 Dog* 반환 가능
    // Invariant Argument: Dog* 인자는 그대로 유지해야 오버라이딩 성립
    Dog* getProcess(Dog* d) override; 
};
```

---

### 시험 포인트

*   ⭐ **인자의 반공변성 vs 실제 언어의 제약**: 이론적으로 인자는 반공변적일 수 있지만, Java/C++에서는 메서드 오버로딩과의 혼동을 피하기 위해 **인자의 불변성**을 강제한다는 점을 기억하세요.
*   ⭐ **반환 타입의 공변성**: 오버라이딩 시 자식 클래스에서 더 구체적인(Subtype) 타입을 반환하는 것은 허용됩니다.
*   ⭐ **예외 처리 규칙**: 오버라이딩된 메서드는 부모보다 더 "넓은" 범위의 예외를 던질 수 없습니다. 오직 더 구체적인 예외나 같은 예외만 허용됩니다.

---

## Slide 8

### 핵심 개념

**메서드 오버라이딩(Method Overriding) 규칙**
상속 관계에서 서브클래스가 부모 클래스의 메서드를 재정의할 때 지켜야 할 시그니처와 반환 타입의 규칙을 다룹니다.

1.  **공변 반환 타입 (Covariant Return Type)**: 오버라이딩 시 부모 클래스 메서드의 반환 타입보다 더 구체적인(하위) 타입을 반환하는 것은 허용됩니다.
2.  **매개변수 타입 (Parameter Types)**: 오버라이딩을 위해서는 매개변수 타입이 정확히 일치해야 합니다. 매개변수가 더 구체적으로 변하면 오버라이딩이 성립되지 않거나 타입 안전성이 깨집니다.
3.  **예외 처리 (Exception Handling)**: 서브클래스의 메서드는 부모 클래스 메서드가 정의한 것보다 더 넓은 범위의 예외를 던질 수 없습니다.

---

### 코드/수식 해설

슬라이드 예제 기준 (기본 메서드: `Vehicle recommend(Vehicle ref)`)

*   **반환 타입 변경**:
    ```cpp
    // Good: Vehicle의 하위 타입인 Car를 반환 (Covariant Return Type)
    Car recommend(Vehicle ref); 
    ```
*   **매개변수 타입 변경**:
    ```cpp
    // Bad: 매개변수가 Vehicle에서 Car로 구체화됨 (오버라이딩 불가)
    Vehicle recommend(Car ref); 
    ```
    *   $Vehicle$ 타입 인자를 기대하는 호출자에게 $Car$만 받는 메서드를 제공하면 타입 안전성에 문제가 생깁니다.
*   **오버로딩(Overloading)의 경우**:
    ```cpp
    // OK: 매개변수 타입이 달라졌으므로 오버라이딩이 아닌 새로운 메서드 정의(오버로딩)
    Vehicle recommend(Object ref); 
    ```
*   **예외(Exception) 추가**:
    ```cpp
    // Bad: 부모에 없던 새로운 예외를 던지는 것은 허용되지 않음
    Vehicle recommend(Vehicle ref) throws NoVehicleException;
    ```

---

### 구체적 예시

**왜 매개변수를 더 구체적으로 바꾸면 안 되는가?**
*   부모 클래스 $Vehicle$의 `recommend`는 모든 $Vehicle$ 객체(기차, 비행기 등)를 인자로 받을 수 있습니다.
*   자식 클래스 $Car$에서 이를 오버라이딩하면서 인자를 $Car$로만 제한한다면, $Vehicle$ 인터페이스를 통해 접근하는 사용자가 기차 객체를 넣었을 때 런타임 에러가 발생할 수 있습니다. (Liskov Substitution Principle 위배)

---

### 시험 포인트

*   ⭐ **공변 반환 타입(Covariant Return Type)**: 오버라이딩 시 자식 클래스 타입을 반환하는 것이 문법적으로 허용됨을 기억하세요.
*   ⭐ **매개변수 불변성**: 오버라이딩 시 매개변수 타입은 부모와 정확히 일치해야 하며, 더 구체적인 타입으로 바꾸는 것은 오버라이딩이 아닙니다.
*   ⭐ **예외 제약**: 오버라이딩된 메서드는 부모 메서드보다 더 많은(또는 더 넓은 범위의) Checked Exception을 던질 수 없습니다.

---

## Slide 9

## Subtyping vs. Subclassing

### **핵심 개념**
*   **Subtyping (Substitution)**: **명세(Specification)** 관점의 개념입니다.
    *   서브타입 객체의 동작이 슈퍼타입 명세의 부분 집합(Subset)이어야 함을 의미합니다.
    *   즉, 슈퍼타입이 예상되는 모든 곳에 서브타입 객체를 문제없이 갈아 끼울 수 있어야 합니다 (Liskov Substitution Principle).
*   **Subclassing (Inheritance)**: **구현(Implementation)** 관점의 개념입니다.
    *   이미 존재하는 클래스의 코드를 재사용하고, 차이점(Differences)만 새로 작성하여 새로운 클래스를 만드는 기술입니다.
*   **Orthogonality (직교성)**: Subclassing과 Subtyping은 서로 독립적인 개념입니다.
    *   **Subclassing $\neq$ Subtyping**: 단순히 상속을 받았다고 해서 항상 서브타입인 것은 아닙니다. (예: 상속을 통해 기능을 물려받았지만, 부모 클래스의 불변 조건을 깨뜨리는 경우)
    *   **Subtyping without subclassing**: 상속 관계가 아니더라도 명세를 완벽히 충족한다면 서브타입이 될 수 있습니다. (다만, C++과 같은 정적 타입 언어에서는 컴파일러 수준에서 지원되지 않을 수 있습니다.)

### **코드/수식 해설**
*   두 개념의 관계는 다음과 같이 표현할 수 있습니다:
    $$Subclassing \nrightarrow Subtyping$$
    (상속이 서브타이핑을 보장하지 않음)
*   C++ 예시: `Square`가 `Rectangle`을 상속(Subclassing)할 때, `setWidth` 함수가 가로/세로를 동시에 바꾼다면 `Rectangle`의 명세(가로/세로 독립 변경)를 위반하므로 Subtyping 관계가 성립하지 않습니다.

```cpp
class Rectangle {
public:
    virtual void setWidth(int w) { width = w; }
    virtual void setHeight(int h) { height = h; }
};

// Subclassing 이지만 Subtyping은 아님 (LSP 위반 사례)
class Square : public Rectangle {
public:
    void setWidth(int w) override { width = height = w; }
    void setHeight(int h) override { width = height = h; }
};
```

### **구체적 예시**
*   **Subclassing (Implementation reuse)**: `Stack` 클래스를 구현하기 위해 `Array` 클래스를 상속받아 내부 저장소로 사용하는 경우 (이때 `Stack`은 `Array`가 아니므로 서브타입이 아님).
*   **Subtyping (Interface satisfaction)**: 인터페이스 `Shape`를 구현하는 `Circle`과 `Triangle`. 이들은 동일한 메시지에 응답하며 대체 가능함.

### **시험 포인트**
*   ⭐ **Specification vs. Implementation**: Subtyping은 명세(행동)의 문제이고, Subclassing은 구현(코드)의 문제임을 구분하는 문제가 자주 출제됩니다.
*   ⭐ **Orthogonality**: "상속(Subclassing)을 하면 반드시 서브타입(Subtype)이 되는가?"라는 질문에 대해 **아니오(No)**라고 답할 수 있어야 하며, 그 이유(LSP 위반 등)를 설명할 수 있어야 합니다.
*   ⭐ **Subtyping without Subclassing**: 상속 없이도 타입 호환성을 가질 수 있는 개념적 가능성을 이해해야 합니다.

---

## Slide 10

### 핵심 개념
- **서브타이핑(Subtyping)**: `Square`가 `Rectangle`의 하위 타입이 될 수 있는지에 대한 설계적 고민을 다룹니다.
- **클래스 불변식(Class Invariant)**: 객체의 생명 주기 동안 항상 참이어야 하는 조건입니다.
    - `Rectangle`: 높이($h$)와 너비($w$)가 양수여야 함.
    - `Square`: `Rectangle`의 조건을 만족하면서 추가로 $h = w$여야 함.
- **Liskov Substitution Principle (LSP) 예고**: 상위 타입의 메서드가 하위 타입의 불변식을 깨뜨릴 수 있는 상황을 보여줍니다.

### 코드/수식 해설
- **Rectangle의 상태 및 불변식**
  - 상태: `int h, w`
  - 불변식: $h > 0 \land w > 0$
- **Square의 상태 및 불변식**
  - `Rectangle`을 상속(`extends`)받음.
  - 불변식 강화: $h > 0 \land w > 0 \land h = w$
- **문제 메서드 (`setWidth`)**
  ```cpp
  void setWidth(int neww) {
      w = neww;
  }
  ```
  - 이 메서드는 $w$만 수정하고 $h$는 건드리지 않습니다. `Rectangle`에서는 문제가 없지만, $h = w$를 유지해야 하는 `Square`에서는 불변식을 깨뜨릴 위험이 있습니다.

### 구체적 예시
1. `Square s = new Square(5);` 생성 ($h=5, w=5$)
2. `s.setWidth(10);` 호출
3. 결과: $h=5, w=10 \Rightarrow h \neq w$ 이므로 `Square`의 불변식($h=w$) 위반

### 시험 포인트
- ⭐ **불변식 강화(Strengthening Invariants)**: 서브클래스는 슈퍼클래스의 불변식을 유지하거나 더 강화할 수 있지만, 슈퍼클래스에서 상속받은 메서드가 강화된 불변식을 만족하지 못하면 LSP 위반이 발생합니다.
- ⭐ **가변성(Mutability)의 문제**: `setWidth`와 같이 객체의 상태를 변경하는 메서드가 있을 때, 직사각형-정사각형 상속 관계는 전형적인 객체지향 설계의 오류 사례로 꼽힙니다.
- ⭐ **Behavioral Subtyping**: 단순히 문법적으로 상속이 가능하다고 해서 올바른 서브타입인 것은 아니며, 부모의 행위 규약(Contract)을 모두 준수해야 함을 이해해야 합니다.

---

## Slide 11

### 핵심 개념
**Liskov Substitution Principle (LSP, 리스코프 치환 원칙)** 관점에서 `Square`(정사각형)와 `Rectangle`(직사각형)의 상속 관계가 성립할 수 없는 이유를 설명합니다. 객체지향 설계에서 서브타입($Sub$)은 슈퍼타입($Super$)의 계약(Contract)을 반드시 준수해야 하지만, 정사각형은 직사각형의 가로 길이를 바꾸는 동작(`setWidth`)에 대해 동일한 기대를 충족시키지 못합니다.

---

### 코드/수식 해설
슬라이드에 제시된 세 가지 `setWidth` 명세(Specification)는 모두 리스코프 치환 원칙을 위반합니다.

**1. Precondition 강화 (Option 1)**
```cpp
//@ requires: h == neww
//@ ensures: w is set to neww
void setWidth(int neww);
```
- **설명**: `neww`가 현재 높이 `$h$`와 같을 때만 함수를 호출할 수 있게 제한함.
- **위반**: 서브타입은 슈퍼타입보다 **강한 선행 조건(Stronger Precondition)**을 가질 수 없음 ($Pre_{super} \implies Pre_{sub}$여야 함).

**2. Postcondition 변경 및 불변성 유지 실패 (Option 2)**
```cpp
//@ requires: neww > 0
//@ ensures: h and w are set to neww
void setWidth(int neww);
```
- **설명**: 가로를 바꿀 때 세로(`$h$`)까지 함께 바꿈.
- **위반**: `Rectangle`을 사용하는 클라이언트는 `setWidth` 호출 후에도 높이 `$h$`는 변하지 않을 것이라고 기대함. 서브타입은 슈퍼타입의 행위적 의무를 위반함.

**3. 예외 상황 도입 (Option 3)**
```cpp
//@ requires: neww > 0
//@ ensures: w is set to neww if h == neww; 
//           throws an exception if h != neww;
void setWidth(int neww);
```
- **설명**: 조건이 맞지 않으면 예외를 던짐.
- **위반**: 슈퍼타입 명세에 없던 새로운 예외 조건은 클라이언트 코드의 예기치 못한 종료를 유발하므로 서브타이핑 실패.

---

### 구체적 예시
`Rectangle`을 사용하는 다음 클라이언트 코드를 고려해 봅시다:
```cpp
void update(Rectangle& r) {
    int oldHeight = r.getHeight();
    r.setWidth(100);
    assert(r.getHeight() == oldHeight); // Rectangle에서는 당연히 참이어야 함
}
```
만약 `r`에 `Square` 객체가 전달된다면 위 `assert`는 실패하거나(Option 2), 함수 호출 자체가 불가능해지거나(Option 1), 예외가 발생(Option 3)하게 됩니다. 따라서 `Square`는 `Rectangle`의 진정한 서브타입이 아닙니다.

---

### 시험 포인트
- ⭐ **Liskov Substitution Principle (LSP)**: 자식 클래스는 언제나 부모 클래스를 대체할 수 있어야 함.
- ⭐ **행위적 서브타이핑(Behavioral Subtyping) 규칙**:
    - 선행 조건(Precondition)은 강화될 수 없다. (같거나 약화되어야 함)
    - 후행 조건(Postcondition)은 약화될 수 없다. (같거나 강화되어야 함)
- ⭐ **Is-a 관계의 함정**: 실세계의 "정사각형은 직사각형이다"라는 논리가 가변 객체(Mutable Object)의 설계에서는 성립하지 않을 수 있음을 이해해야 함.

---

## Slide 12

### 핵심 개념
- **가변 객체(Mutable Object)에서의 상속 문제**: 수학적으로 정사각형(Square)은 직사각형(Rectangle)의 일종이지만, 프로그래밍의 가변 객체 모델에서는 상속 관계가 성립하지 않을 수 있습니다.
- **리스코프 치환 원칙(LSP) 위반**: 서브타입은 기반 타입의 행위적 제약 조건을 모두 만족해야 합니다. 가변 객체일 경우, `Square`와 `Rectangle`은 서로의 불변 속성(Invariant)이나 사후 조건(Post-condition)을 깨뜨리게 됩니다.
    - **Square $\not\subset$ Rectangle**: 직사각형은 가로와 세로가 독립적으로 변할 것을 기대하지만, 정사각형은 이를 허용하지 않습니다.
    - **Rectangle $\not\subset$ Square**: 정사각형은 가로와 세로가 항상 같아야 한다는 제약($width = height$)이 있지만, 직사각형은 이를 위반합니다.

### 코드/수식 해설
- **Rectangle의 기대 동작 (Post-condition)**:
  ```cpp
  void setWidth(double w) {
      this->width = w;
      // Post-condition: height는 변하지 않아야 함
  }
  ```
- **Square가 Rectangle을 상속받을 때의 문제**:
  정사각형은 가로를 변경하면 세로도 함께 변경되어야 하므로, `Rectangle` 사용자가 기대하는 "가로만 바뀐다"는 사후 조건을 위반합니다.

### 구체적 예시
1. **Square $\to$ Rectangle 상속 시**:
   사용자가 `Rectangle* r = new Square(5);`를 가질 때, `r->setWidth(10);`을 호출한 직후 `r->getHeight()`가 여전히 `5`이기를 기대하지만, `Square`는 자신의 성질을 유지하기 위해 높이를 `10`으로 바꿔버립니다.
2. **해결책**:
   - **Immutable**: 객체의 상태를 변경할 수 없게 만들어(Read-only), 가로/세로를 독립적으로 수정할 상황 자체를 제거합니다.
   - **Common Abstraction**: 둘의 공통점(예: `getArea()`)만 모아 별도의 인터페이스나 추상 클래스(예: `Shape`)를 정의하고 각자 상속받게 합니다.

### 시험 포인트
- ⭐ **LSP(Liskov Substitution Principle)** 관점에서 왜 가변 `Square`가 `Rectangle`의 서브타입이 될 수 없는지 서술할 수 있어야 합니다.
- ⭐ 가변 객체(Mutable)와 불변 객체(Immutable)일 때 상속 관계의 성립 여부가 어떻게 달라지는지 이해해야 합니다.
- ⭐ 이 문제를 해결하기 위한 설계 패턴(공통 인터페이스 추출 등)을 제시할 수 있어야 합니다.

---

## Slide 13

### 핵심 개념
- **리스코프 치환 원칙 (Liskov Substitution Principle, LSP)**: 서브타입은 언제나 기반 타입(Supertype)으로 교체할 수 있어야 하며, 기반 타입의 계약(Invariant, Precondition, Postcondition)을 준수해야 합니다.
- **불변성(Invariant)의 유지**: `Rect` 클래스는 $h > 0$ 및 $w > 0$이라는 불변 조건을 가집니다. `MutableRect`가 `Rect`를 상속받을 때, 이 불변 조건을 깨뜨릴 가능성이 있다면 올바른 서브타입이라 할 수 없습니다.

### 코드/수식 해설
- **기반 클래스 `Rect`**:
  - 상태: $h, w$
  - 불변 조건: $h > 0 \land w > 0$
- **파생 클래스 `MutableRect`**:
  - `scale(int factor)` 메서드가 추가됨.
  - 메서드 내부 연산:
    ```cpp
    w = w * factor;
    h = h * factor;
    ```
- **문제점**:
  - 만약 `factor`가 $0$ 이하의 값($factor \le 0$)일 경우, 연산 후의 $h$와 $w$는 $0$ 또는 음수가 됩니다.
  - 이는 기반 클래스 `Rect`에서 정의한 $h > 0 \land w > 0$이라는 불변 조건을 위반하게 됩니다.

### 구체적 예시
`MutableRect` 객체의 인스턴스가 `Rect` 타입으로 사용되고 있을 때:
```cpp
Rect* r = new MutableRect(10, 10);
// 어떤 코드에서 MutableRect의 scale을 호출하여 factor에 -1을 전달할 경우
// r->h와 r->w는 -10이 됨 -> Rect의 불변 조건(h>0, w>0) 파괴
```
이처럼 서브타입의 행위가 슈퍼타입의 불변 조건을 깨뜨린다면, **Behavioral Subtyping** 관점에서 `MutableRect`는 `Rect`의 진정한 서브타입이 아닙니다.

### 시험 포인트
- ⭐ **불변 조건(Invariant) 보존**: 자식 클래스에서 추가된 메서드가 부모 클래스의 불변 조건을 깨뜨리지 않는지 확인하는 것이 서브타입 판별의 핵심입니다.
- ⭐ **가변성(Mutability) 추가**: 불변(Immutable) 객체를 상속받아 가변(Mutable) 객체를 만드는 것은 LSP를 위반할 가능성이 매우 높으므로 주의해야 합니다.
- ⭐ **Behavioral Subtyping**: 단순히 문법적(Syntactic) 상속이 가능하다고 해서 서브타입인 것은 아니며, 의미론적(Semantic) 규약을 지켜야 합니다.

---

## Slide 14

### 핵심 개념
- **가변 확장과 서브타이핑(Mutable Extensions and Subtyping)**: 부모 클래스가 객체의 상태가 변하지 않음을 전제로 설계되었을 때, 이를 상속받아 상태를 변경할 수 있는(mutable) 기능을 추가하면 서브타이핑 관계가 깨질 수 있습니다.
- **불변 조건(Invariant)의 파괴**: 상위 타입을 사용하는 클래스는 상위 타입의 행동 방식을 신뢰하고 불변 조건을 설정합니다. 하지만 상태를 변경하는 하위 타입이 전달되면, 상위 타입 관점에서 유지되어야 할 불변 조건이 예기치 않게 깨지게 됩니다.

### 코드/수식 해설
- **AreaCache의 불변 조건**:
  ```java
  // @ invariant: rect.getArea() == cached
  ```
  `AreaCache`는 생성 시점의 면적을 `cached` 변수에 저장하며, `$rect.getArea() == cached$`라는 수식이 항상 참일 것이라고 가정합니다. 이는 `Rect`가 불변(Immutable)임을 전제로 합니다.

- **Client에 의한 불변 조건 위반**:
  ```java
  Rect r = new MutableRect(2, 3);
  AreaCache cache = new AreaCache(r);
  ((MutableRect) r).scale(10); // Invariant violated!
  ```
  1. `MutableRect`는 `Rect`의 하위 타입이므로 `AreaCache`에 전달 가능합니다.
  2. `scale(10)` 호출 시 `$rect.getArea()$` 값은 변하지만, `AreaCache` 내부의 `$cached$` 값은 업데이트되지 않습니다.
  3. 결과적으로 `$rect.getArea() \neq cached$`가 되어 불변 조건이 깨집니다.

### 구체적 예시
- **상황**: `Rect`(불변)를 상속받은 `MutableRect`(가변)가 존재.
- **문제**: `AreaCache`는 `Rect`가 변하지 않을 것이라 믿고 면적 계산 결과를 캐싱하지만, `MutableRect`를 통해 외부에서 크기를 조절해버리면 캐싱된 데이터는 '쓰레기 값(Stale data)'이 됩니다.

### 시험 포인트
- ⭐ **행동적 서브타이핑(Behavioral Subtyping)**: 단순히 시그니처가 일치한다고 해서 올바른 서브타입이 아닙니다. 부모 클래스의 불변 조건과 제약 사항을 자식 클래스에서도 준수해야 합니다.
- ⭐ **Liskov Substitution Principle (LSP) 위반**: 상위 타입 `Rect`를 `MutableRect`로 치환했을 때, `AreaCache`의 프로그램 정확성(Correctness)이 깨지므로 이는 LSP 위반 사례에 해당할 수 있습니다.
- ⭐ **설계 원칙**: 하위 타입에 새로운 필드를 추가하는 것은 안전할 수 있으나, 상위 타입의 상태(inherited state)를 변경하는 메서드를 추가할 때는 주의가 필요합니다.

---

## Slide 15

### 핵심 개념
**불변성(Immutability)**은 객체가 생성된 후 그 상태를 변경할 수 없는 성질을 의미합니다. C++에서는 멤버 변수를 `const`로 선언하거나 상태를 변경하는 메서드(Setter)를 제공하지 않음으로써 구현합니다. 슬라이드에서는 불변성이 제공하는 세 가지 주요 이점을 다룹니다.

1.  **표현 노출(Representation Exposure) 방지**: 내부 가변 객체에 대한 참조를 외부에 노출하더라도, 외부에서 해당 객체의 상태를 변경할 수 없으므로 안전합니다.
2.  **키 변형 오류(Key Mutation Errors) 방지**: `std::map`이나 `std::set`의 키(Key)로 사용되는 객체의 값이 바뀌면 자료구조의 불변성(Invariants)이 깨지는데, 불변 객체는 이 위험을 원천 차단합니다.
3.  **예측 가능한 서브타이핑(Subtyping)**: 가변 객체에서 발생하는 타입 변환 시의 부작용(Side-effect)이 없으므로, 상속 구조에서 객체를 더 안전하게 다룰 수 있습니다.

### 코드/수식 해설
불변 객체는 내부 데이터를 직접 수정하는 대신, 변경된 상태를 가진 **새로운 객체**를 반환하는 방식을 취합니다.

```cpp
class ImmutablePoint {
    const int x; // 멤버 변수를 const로 선언하여 불변성 강제
    const int y;

public:
    ImmutablePoint(int _x, int _y) : x(_x), y(_y) {}

    // 상태를 변경하는 대신 새로운 객체 반환
    ImmutablePoint move(int dx, int dy) const {
        return ImmutablePoint(x + dx, y + dy);
    }
};
```

### 구체적 예시
*   **Key Mutation Error**: 만약 가변 객체 $P$가 해시맵의 키로 들어가 있는데, 외부에서 $P.x = 100$으로 값을 바꾸면 해당 객체는 원래 해시 버킷에서 찾을 수 없게 되어 논리적 오류가 발생합니다. 불변 객체는 $x$ 값을 바꿀 수 없으므로 이 문제가 발생하지 않습니다.
*   **Defensive Copy 생략**: 불변 객체는 값이 변하지 않음을 보장하므로, 함수 인자로 넘기거나 반환할 때 복사본을 만드는 `Defensive Copy` 비용을 줄일 수 있습니다.

### 시험 포인트
*   ⭐ **Representation Exposure**: 불변 객체를 사용하면 `get` 메서드에서 내부 포인터나 참조를 반환해도 캡슐화가 깨지지 않는 이유를 서술할 수 있어야 합니다.
*   ⭐ **Liskov Substitution Principle (LSP)**: 가변성(Mutability)은 서브타이핑에서 '가변성 문제'를 일으키지만, 불변 객체는 서브타입 관계를 더 직관적으로 만들어줍니다.
*   ⭐ **Key Invariance**: 자료구조(Map, Set)의 정렬 및 해싱 상태를 유지하기 위해 불변성이 왜 필수적인지 이해해야 합니다.

---

## Slide 16

### 핵심 개념
- **제네릭(Generics)**: 데이터 타입에 의존하지 않고 함수나 클래스를 일반화하여 정의하는 프로그래밍 패러다임입니다.
- C++에서는 **템플릿(Template)** 기능을 통해 제네릭 프로그래밍을 구현하며, 이는 코드의 재사용성과 타입 안정성(Type Safety)을 동시에 확보하게 해줍니다.

### 코드/수식 해설
제네릭 함수 정의의 가장 기본적인 형태는 다음과 같습니다.
```cpp
template <typename T>
T func(T arg) {
    // T 타입에 대한 처리 로직
    return arg;
}
```

### 구체적 예시
- **STL(Standard Template Library)**: `std::vector<T>`, `std::list<T>` 등 모든 표준 컨테이너 라이브러리가 제네릭을 기반으로 설계되었습니다.
- 임의의 타입 $T$에 대해 덧셈을 수행하는 함수나, 서로 다른 타입의 데이터를 저장하는 자료구조를 만들 때 사용됩니다.

### 시험 포인트
- ⭐ **Compile-time Polymorphism**: C++의 템플릿은 컴파일 타임에 해당 타입에 맞는 코드가 생성(Instantiation)되는 정적 다형성의 한 형태임을 이해해야 합니다.
- ⭐ **Type Safety**: `void*` 등을 사용하는 방식과 달리, 컴파일러가 엄격하게 타입을 체크하여 런타임 오류를 방지합니다.

---

## Slide 17

## Motivating Example: 타입 안전성(Type Safety)의 부재

### **핵심 개념**
- **Object 기반 컨테이너**: 모든 클래스의 최상위 타입인 `Object`를 사용하여 다양한 타입의 데이터를 담을 수 있는 클래스를 설계할 수 있습니다.
- **런타임 타입 오류**: `Object` 타입을 사용하면 컴파일 시점에는 타입 일치 여부를 확인할 수 없으며, 잘못된 타입 캐스팅으로 인한 오류가 프로그램 실행 중에 발생하게 됩니다.
- **제네릭(Generics)의 필요성**: 컴파일 타임에 타입 체크를 수행하여 프로그래머의 실수를 방지하고 코드의 안정성을 높이기 위해 제네릭이 도입되었습니다.

### **코드/수식 해설**
```java
public class Box {
    private Object object; // 모든 타입을 담기 위해 Object 사용

    public void set(Object obj) { object = obj; }
    public Object get() { return object; }
}
```
- `private Object object`: $Object$ 타입은 모든 참조 타입을 참조할 수 있는 다형성을 가집니다.
- `public Object get()`: 데이터를 반환할 때 항상 $Object$ 타입을 반환하므로, 실제 사용을 위해서는 명시적인 **다운캐스팅(Downcasting)**이 필요합니다.

```java
Box box = new Box();
box.set(Integer.valueOf(3)); // Integer 객체를 저장

String str = (String) box.get(); // 컴파일 오류 없음, 그러나 실행 시 ClassCastException 발생
```
- `box.set(...)`: $Integer$ 객체가 $Object$ 타입으로 업캐스팅되어 저장됩니다.
- `(String) box.get()`: 컴파일러는 `get()`의 반환 타입이 $Object$라는 것만 알기 때문에, $String$으로 캐스팅하는 코드에 대해 문법적 오류를 제기하지 않습니다. 하지만 실제 런타임에는 $Integer$를 $String$으로 바꿀 수 없으므로 프로그램이 비정상 종료됩니다.

### **구체적 예시**
1. **의도**: 개발자는 `Box`에 숫자를 넣고 숫자로 꺼내기를 기대함.
2. **실수**: 실수로 `String` 변수에 대입하며 강제 형변환을 시도함.
3. **결과**: 컴파일러는 이 실수를 잡아내지 못하고, 사용자에게 프로그램이 전달된 이후에야 오류가 발견됨.

### **시험 포인트**
- ⭐ **컴파일 타임(Compile-time) vs 런타임(Runtime)**: 위 예시에서 타입 불일치 문제가 어느 시점에 발견되는지 구분하는 것이 중요합니다. (위 예시는 런타임에 발견됨)
- ⭐ **Type Safety**: 위와 같은 설계가 왜 "Type-safe하지 않다"고 말하는지 그 이유를 설명할 수 있어야 합니다.
- ⭐ **Casting의 위험성**: 명시적 형변환(`(String)`)이 컴파일러의 타입 체크를 무력화시키는 지점을 이해해야 합니다.

---

## Slide 18

### 핵심 개념
- **제네릭(Generics)**: 클래스 내부에서 사용할 데이터 타입을 외부에서 지정하는 기법입니다.
- **타입 파라미터 ($T$)**: 실제 타입 대신 임시로 사용하는 식별자로, 클래스나 메서드 정의 시 유연성을 제공합니다.
- **컴파일 타임 타입 체크**: 제네릭을 사용하면 잘못된 타입이 들어오는 것을 컴파일 단계에서 방지하여 프로그램의 안정성을 높입니다.

### 코드/수식 해설
- **제네릭 클래스 정의**:
  ```java
  public class Box<T> {
      private T t;
      public void set(T t) { this.t = t; }
      public T get() { return t; }
  }
  ```
  - `Box<T>`: $T$라는 타입 파라미터를 가지는 제네릭 클래스를 선언합니다.
  - `private T t`: 필드 $t$의 타입을 $T$로 지정하여, 인스턴스 생성 시 결정된 타입만 저장 가능하게 합니다.

- **타입 안정성 검사**:
  ```java
  Box<Integer> box = new Box<Integer>();
  box.set(Integer.valueOf(3));
  String str = (String) box.get(); // compile-time error
  ```
  - `Box<Integer>`로 선언된 객체는 오직 `Integer` 타입만 다룹니다.
  - `box.get()`의 결과는 `Integer`임이 보장되므로, 이를 `String`으로 강제 형변환하려는 시도는 컴파일러에 의해 차단됩니다.

### 구체적 예시
- **`Box<Integer>`**: $T$가 `Integer`로 치환되어 정수 데이터만 관리하는 전용 상자처럼 동작합니다.
- **`Box<String>`**: $T$가 `String`으로 치환되어 문자열 데이터만 관리합니다.

### 시험 포인트
- ⭐ **컴파일 타임 에러 발생**: 제네릭은 런타임(Runtime) 에러인 `ClassCastException`을 컴파일 타임(Compile-time) 에러로 전환하여 디버깅 비용을 낮춥니다.
- ⭐ **강력한 타입 체크(Stronger type checks)**: 제네릭을 사용하지 않았을 때(Object 타입 사용 등)와 비교하여 타입 안전성이 어떻게 향상되는지 이해해야 합니다.

---

## Slide 19

## Java Generics

**핵심 개념**
- **타입 파라미터화(Parameterized Types)**: 클래스, 인터페이스, 메서드를 정의할 때 사용할 데이터 타입을 확정 짓지 않고, 실행 시점 혹은 객체 생성 시점에 결정하도록 파라미터로 넘기는 기법입니다.
- **코드 재사용성**: 동일한 로직을 가진 코드를 다양한 데이터 타입에 대해 중복 작성 없이 재사용할 수 있게 합니다.
- **주요 목적**: 컴파일 타임에 엄격한 타입 체크를 수행하여 런타임 오류를 줄이고, 불필요한 형변환(Casting)을 제거합니다.

**코드/수식 해설**
- **제네릭 클래스 선언 구조**:
  ```java
  public class Box<T> { // T는 타입 파라미터
      private T content;
      public void set(T content) { this.content = content; }
      public T get() { return content; }
  }
  ```
- **수식 기호 활용**: 일반적인 타입 파라미터 관례로 $T$ (Type), $E$ (Element), $K$ (Key), $V$ (Value) 등이 사용됩니다. 제네릭을 통해 타입 $T$에 대한 종속성을 제거하고 추상화할 수 있습니다.

**구체적 예시**
- **형변환 제거 (Elimination of casts)**:
  - 제네릭 미사용: `String s = (String) list.get(0);` (명시적 캐스팅 필요)
  - 제네릭 사용: `List<String> list = new ArrayList<>(); String s = list.get(0);` (캐스팅 생략 가능)
- **제네릭 알고리즘**: 특정 타입에 국한되지 않고, 정렬(Sorting)이나 검색(Searching)과 같은 알고리즘을 다양한 객체 타입에 대해 일관되게 적용할 수 있습니다.

**시험 포인트**
- ⭐ **Compile-time Type Safety**: 제네릭의 가장 큰 장점은 런타임에 발생할 수 있는 `ClassCastException`을 컴파일 시점에 미리 방지한다는 점입니다.
- ⭐ **Type Erasure**: (슬라이드에는 명시되지 않았으나 관련 개념으로 빈번히 출제) Java의 제네릭은 하위 호환성을 위해 컴파일 후에는 타입 정보가 제거되고 `Object`나 `Bound` 타입으로 치환됩니다.
- ⭐ **Generic vs Object**: `Object`를 사용한 다형성과 제네릭의 차이점(타입 안정성 유무 및 캐스팅 필요성)을 비교하는 문제가 나올 수 있습니다.

---

## Slide 20

## Declaring and Instantiating Generics

**핵심 개념**
*   **제네릭 선언(Declaration)**: 클래스나 인터페이스를 정의할 때 구체적인 타입 대신 타입 변수($TypeVar$)를 사용하여 정의하는 방식입니다.
*   **타입 변수 관례(Convention)**: 관습적으로 단일 대문자를 사용하며, 이는 코드의 가독성을 높입니다.
*   **인스턴스화(Instantiation)**: 제네릭 클래스/인터페이스를 실제 사용할 때, 클라이언트가 구체적인 타입 인자($Type \ Argument$)를 제공하여 타입을 확정 짓는 단계입니다.

**코드/수식 해설**
*   **제네릭 선언 형식**
    ```java
    class Name<TypeVar1, ..., TypeVarN> { ... }
    interface Name<TypeVar1, ..., TypeVarN> { ... }
    ```
*   **제네릭 인스턴스화 형식**
    ```java
    Name<Type1, ..., TypeN>
    ```
    *   여기서 $N$은 사용된 타입 변수의 개수를 의미합니다.

**구체적 예시**
*   **타입 변수 명명 관례**:
    *   `T`: Type (일반적인 타입)
    *   `E`: Element (리스트 등 컬렉션의 원소)
    *   `K`: Key (맵의 키)
    *   `V`: Value (맵의 값)

**시험 포인트**
*   ⭐ **명명 관례**: 타입 변수로 $T, E, K$ 등 단일 대문자를 사용하는 관례를 기억하세요.
*   ⭐ **타입 파라미터 전달**: 제네릭 클래스를 인스턴스화할 때는 반드시 선언된 타입 변수의 개수($N$)와 일치하는 구체적 타입을 명시해야 합니다.
*   ⭐ **컴파일 타임 체크**: 제네릭은 런타임이 아닌 컴파일 타임에 타입 안정성을 보장하기 위해 사용됩니다.

---

## Slide 21

### 핵심 개념
- **다중 타입 매개변수(Multiple Type Parameters)**: 제네릭 클래스는 하나 이상의 타입 매개변수를 가질 수 있습니다. 본 슬라이드에서는 $K$(Key)와 $V$(Value) 두 개의 타입을 사용하는 예시를 보여줍니다.
- **제네릭 인터페이스 구현**: 제네릭 클래스는 제네릭 인터페이스를 구현할 수 있으며, 이때 인터페이스의 타입 매개변수($K, V$)를 그대로 전달하여 타입을 일치시켜야 합니다.

### 코드/수식 해설
```java
public class OrderedPair<K, V> implements Pair<K, V> {
    private K key;
    private V value;

    // 생성자: 필드 타입이 매개변수화된 타입 K와 V를 따름
    public OrderedPair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    // Getter 메소드: 반환 타입이 제네릭 타입임
    public K getKey() { return key; }
    public V getValue() { return value; }
}
```
- `OrderedPair<K, V>`: 클래스 선언부에 꺽쇠괄호(`<>`)를 사용하여 임의의 타입 $K$와 $V$를 정의합니다.
- `implements Pair<K, V>`: `Pair`라는 제네릭 인터페이스를 $K$와 $V$ 타입을 사용하여 상속/구현함을 의미합니다.

### 구체적 예시
이 클래스를 실제로 사용할 때는 구체적인 타입을 명시합니다.
- `Pair<String, Integer> p = new OrderedPair<>("Even", 8);`
- 위 예시에서 $K$는 `String`이 되고, $V$는 `Integer`가 됩니다.

### 시험 포인트
- ⭐ **타입 매개변수 관례**: 관습적으로 $K$는 Key, $V$는 Value, $E$는 Element, $T$는 Type을 의미합니다.
- ⭐ **인터페이스 일치**: 클래스가 제네릭 인터페이스를 구현할 때, 타입 매개변수의 개수와 전달 방식이 올바른지 확인해야 합니다.
- ⭐ **타입 안전성(Type Safety)**: 컴파일 타임에 $K$와 $V$의 타입이 결정되므로, 잘못된 타입의 객체가 삽입되는 것을 방지할 수 있습니다.

---

## Slide 22

### 핵심 개념
- **제네릭 타입 인스턴스화 (Generic Instantiation)**: 제네릭 클래스를 사용할 때 구체적인 타입을 지정하여 객체를 생성하는 과정입니다.
- **타입 추론 (Type Inference)**: 컴파일러가 선언문의 타입을 보고 생성자 부분의 타입을 자동으로 결정하는 기능입니다. Java의 다이아몬드 연산자 `<>`가 대표적입니다.
- **중첩된 제네릭 (Nested Generics)**: 제네릭 타입의 인자로 또 다른 제네릭 타입을 전달하여 복잡한 데이터 구조를 형성할 수 있습니다.

### 코드/수식 해설
- **명시적 타입 지정 (Explicit Types)**: 좌변과 우변 모두에 구체적인 타입을 명시합니다.
```java
Pair<String, Integer> p1 = new OrderedPair<String, Integer>("Even", 8);
```
- **다이아몬드 연산자를 이용한 추론**: 우변의 타입을 `<>`로 생략하여 코드를 간결하게 작성합니다.
```java
OrderedPair<String, Integer> p1 = new OrderedPair<>("Even", 8);
```
- **중첩된 타입 인자**: `Box<Integer>`라는 제네릭 타입 자체를 `OrderedPair`의 두 번째 인자로 전달합니다.
```java
OrderedPair<String, Box<Integer>> p = new OrderedPair<>("primes", new Box<>());
```

### 구체적 예시
- **타입 인자(Type Argument)**: 위 코드에서 `String`, `Integer`는 타입 파라미터 $T$, $V$ 등에 대입되는 실제 타입 인자입니다.
- **계층 구조**: `OrderedPair<K, V>`는 `Pair<K, V>`의 하위 타입(Subtype)일 때, 다형성을 활용하여 `Pair` 타입 참조 변수에 `OrderedPair` 객체를 할당할 수 있습니다.

### 시험 포인트
- ⭐ **다이아몬드 연산자 `<>`의 역할**: 컴파일러가 좌변의 선언을 바탕으로 우변의 타입 인자를 추론하므로 중복 코드를 줄일 수 있음을 이해해야 합니다.
- ⭐ **제네릭 타입 간의 상속 관계**: `Pair<String, Integer>`와 `OrderedPair<String, Integer>` 사이의 상속 관계가 성립하더라도, `Pair<Object, Object>`와 `Pair<String, Integer>` 사이에는 직접적인 상속 관계가 없음에 주의해야 합니다.
- ⭐ **중첩 제네릭 문법**: `Box<Integer>`와 같이 제네릭이 중첩될 때 각 괄호(`<>`)의 쌍이 정확히 맞아야 하며, 각 단계에서 타입 추론이 어떻게 발생하는지 파악해야 합니다.

---

## Slide 23

### 핵심 개념
- **제네릭의 범용성**: 제네릭은 `List`나 `Map` 같은 컬렉션(Collection)뿐만 아니라, `Pair`와 같은 일반 객체나 유틸리티 클래스 등 다양한 곳에서 타입 안정성을 위해 사용됩니다.
- **클래스 수준 제네릭의 한계**: 유틸리티 클래스를 정의할 때 클래스 레벨에서 제네릭 타입($K, V$)을 선언하면, 타입 조합이 바뀔 때마다 매번 새로운 인스턴스를 생성해야 하는 메모리 및 구조적 비효율성이 발생합니다.

### 코드/수식 해설

**1. Pair 클래스**
두 개의 서로 다른 타입 $K$와 $V$를 저장하는 범용 컨테이너입니다.
```java
public class Pair<K, V> {
    private K key;
    private V value;
    // Getter, Setter, Constructor 생략
}
```

**2. Util 클래스의 문제점**
슬라이드 예시의 `Util` 클래스는 클래스 레벨에 제네릭을 선언했습니다.
```java
public class Util<K, V> {
    public boolean compare(Pair<K, V> p1, Pair<K, V> p2) {
        return p1.getKey().equals(p2.getKey()) && 
               p1.getValue().equals(p2.getValue());
    }
}
```
- **단점**: `compare` 메서드는 특정 인스턴스의 상태(state)를 사용하지 않는 동작임에도 불구하고, 비교하려는 $K, V$ 타입 쌍이 달라질 때마다 `new Util<String, Integer>()` 등을 계속 생성해야 합니다.

### 구체적 예시
만약 `Pair<String, Integer>`를 비교하다가 `Pair<Double, Long>`을 비교해야 한다면, 클래스 레벨 제네릭 설계에서는 서로 다른 두 개의 `Util` 객체가 메모리에 존재해야 합니다. 이는 상태를 가지지 않는 유틸리티 메서드 특성상 불필요한 자원 낭비입니다.

### 시험 포인트
- ⭐ **클래스 제네릭 vs 제네릭 메서드**: 위와 같은 문제를 해결하기 위해 클래스 전체를 제네릭으로 만드는 대신, 메서드 단위에서 제네릭을 선언하는 '제네릭 메서드(Generic Method)'의 필요성을 이해해야 합니다.
- ⭐ **인스턴스 종속성**: 클래스 레벨에 제네릭 타입 $T$가 선언되면, 해당 타입은 인스턴스 생성 시점에 결정되므로 `static` 컨텍스트에서 사용할 수 없음을 유의하세요.
- ⭐ **Efficiency**: 상태를 유지하지 않는 유틸리티 함수는 클래스 레벨 제네릭보다 제네릭 메서드로 설계하는 것이 객체 생성 오버헤드를 줄이는 방법입니다.

---

## Slide 24

### Generic Methods

**핵심 개념**
- **제네릭 메서드**: 클래스 전체가 제네릭이 아니더라도, 특정 메서드만 제네릭으로 선언하여 다양한 타입에 대응할 수 있게 하는 기법입니다.
- **타입 파라미터 범위**: 메서드 레벨에서 선언된 타입 파라미터는 해당 메서드 내부로만 범위(Scope)가 한정됩니다.
- **독립성**: 클래스에 정의된 타입 파라미터와 별개로 메서드만의 고유한 타입을 가질 수 있습니다.

**코드/수식 해설**
```java
public class Util {
    // 리턴 타입(boolean) 앞에 타입 파라미터 <K, V>를 선언함
    public static <K, V> boolean compare(Pair<K, V> p1, Pair<K, V> p2) {
        return p1.getKey().equals(p2.getKey()) && p1.getValue().equals(p2.getValue());
    }
}
```
- `<K, V>`: 메서드에서 사용할 타입 파라미터를 선언하는 부분입니다. 리턴 타입인 `boolean` 바로 앞에 위치합니다.
- `Pair<K, V>`: 선언된 $K$와 $V$ 타입을 인자(Parameter)의 타입으로 사용합니다.
- 슬라이드 예시에서는 두 $Pair$ 객체의 $Key$와 $Value$가 모두 같은지 `.equals()`로 비교합니다.

**구체적 예시**
- 메서드 호출 시 타입을 명시하거나 추론(Inference)하게 할 수 있습니다.
- 예: `Util.<Integer, String>compare(p1, p2)` 또는 컴파일러의 타입 추론을 통해 `Util.compare(p1, p2)`로 호출 가능합니다.

**시험 포인트**
- ⭐ **타입 파라미터의 위치**: 제네릭 메서드에서 타입 파라미터($<T>$)는 반드시 리턴 타입 바로 앞에 선언되어야 함을 기억하세요.
- ⭐ **정적 메서드(Static Method)**: 클래스의 타입 파라미터를 사용할 수 없는 `static` 메서드에서 제네릭을 사용하려면, 반드시 메서드 레벨에서 타입 파라미터를 독립적으로 선언해야 합니다.
- ⭐ **Scope**: 메서드에 선언된 $K, V$는 클래스 레벨의 타입 파라미터와 이름이 같더라도 서로 별개로 취급될 수 있습니다.

---

## Slide 25

### 핵심 개념
제네릭 메서드(Generic Method)를 호출하는 두 가지 주요 방법인 **명시적 타입 인자 전달(Explicit Type Arguments)**과 **타입 추론(Type Inference)**을 다룹니다.

1.  **명시적 타입 지정**: 메서드 호출 시 사용할 구체적인 타입을 꺾쇠괄호(`<>`) 안에 직접 명시합니다.
2.  **타입 추론**: 컴파일러가 메서드에 전달된 인자의 타입을 확인하여 적절한 제네릭 타입을 자동으로 결정합니다.

---

### 코드/수식 해설

**1. 명시적 타입 인자 사용 (With explicit type arguments)**
```java
// 메서드 이름 앞에 <Integer, String>을 명시하여 호출
boolean same = Util.<Integer, String>compare(p1, p2);
```
*   제네릭 메서드 `compare`가 어떤 타입 파라미터를 사용할지 코드로 직접 선언하는 방식입니다.
*   복잡한 타입 구조에서 컴파일러가 타입을 모호하게 판단할 때 명확성을 제공합니다.

**2. 타입 추론 사용 (With type inference)**
```java
// 타입을 생략해도 컴파일러가 p1, p2를 보고 타입을 추론함
boolean same = Util.compare(p1, p2);
```
*   코드의 가독성이 높아지며, 대부분의 상황에서 Java/C++ 컴파일러는 인자를 통해 타입을 정확히 추론할 수 있습니다.

---

### 구체적 예시
슬라이드에서는 `Pair<Integer, String>` 객체인 `p1`과 `p2`를 생성한 후, `Util` 클래스의 제네릭 메서드인 `compare`를 호출하여 두 객체가 동일한지 비교하고 있습니다. 
*   `p1`: `(1, "apple")`
*   `p2`: `(2, "pear")`
*   두 방식 모두 결과적으로 `same` 변수에 `boolean` 값을 반환합니다.

---

### 시험 포인트
*   ⭐ **타입 추론(Type Inference)**: 컴파일러가 인자(arguments)를 바탕으로 타입 파라미터를 결정하는 과정을 이해하고 있는지 묻는 문제가 나올 수 있습니다.
*   ⭐ **문법적 위치**: 명시적 타입 지정 시 `<Type>`의 위치가 메서드 이름 바로 앞(예: `Util.<Integer>compare(...)`)이라는 점에 유의하세요.
*   ⭐ **다이아몬드 연산자(`<>`)**: 객체 생성 시(`new Pair<>()`) 타입을 중복해서 적지 않아도 되는 자바의 타입 추론 방식도 함께 기억해 두면 좋습니다.

---

## Slide 26

### Bounded Type Parameters

**핵심 개념**
- 제네릭(Generics)에서 타입 매개변수 $T$가 가질 수 있는 타입을 특정 타입의 하위 타입으로 제한하는 기능입니다.
- 특정 클래스를 상속받거나 특정 인터페이스를 구현한 타입만을 인자로 받음으로써, 해당 타입이 제공하는 메서드를 안전하게 호출할 수 있게 합니다.

**코드/수식 해설**
- **단일 경계 (Single Bound)**
  ```java
  <T extends B>
  ```
  타입 매개변수 $T$는 반드시 $B$ 클래스이거나 $B$의 하위 클래스(또는 인터페이스 구현체)여야 합니다.

- **다중 경계 (Multiple Bounds)**
  ```java
  <T extends ClassT & InterfaceT1 & InterfaceT2>
  ```
  타입 매개변수 $T$는 여러 개의 조건을 동시에 만족해야 합니다.
  - $T$는 `ClassT`를 상속받아야 함.
  - $T$는 `InterfaceT1`, `InterfaceT2` 등의 인터페이스를 모두 구현해야 함.

**구체적 예시**
- 숫자를 다루는 제네릭 클래스에서 $T$가 산술 연산이 가능한 타입임을 보장하고 싶을 때 사용합니다.
- 예: `<T extends Number>`를 사용하면 $T$ 타입의 객체에서 `doubleValue()`와 같은 `Number` 클래스의 메서드를 자유롭게 호출할 수 있습니다.

**시험 포인트**
- ⭐ **다중 경계의 순서**: 다중 경계를 정의할 때, 클래스 타입이 인터페이스보다 반드시 앞에 와야 합니다 (예: `<T extends Interface & Class>`는 컴파일 에러).
- ⭐ **타입 안정성**: 제한된 타입 파라미터를 사용하면 컴파일 타임에 타입 체크를 수행하여 런타임 에러를 방지할 수 있습니다.
- ⭐ **API 활용**: 특정 기능을 가진 객체만 인자로 허용하도록 강제함으로써 코드의 재사용성과 안정성을 높입니다.

---

## Slide 27

### 핵심 개념
- **제네릭 클래스 및 메서드**: 타입을 파라미터화하여 정의함으로써 코드의 재사용성을 높이고 타입 안정성을 보장함.
- **제한된 타입 파라미터 (Bounded Type Parameters)**: `extends` 키워드를 사용하여 특정 타입의 하위 클래스로만 타입을 제한할 수 있음.
- **타입 검사 (Type Checking)**: 컴파일 타임에 타입 제약 조건을 확인하여 런타임 오류를 방지함.

### 코드/수식 해설
```java
public <U extends Number> void inspect(U u) {
    System.out.println("T: " + t.getClass().getName());
    System.out.println("U: " + u.getClass().getName());
}
```
- `<U extends Number>`: 타입 파라미터 $U$가 반드시 `Number` 클래스 또는 그 자식 클래스(`Integer`, `Double` 등)여야 함을 명시함.
- `t.getClass().getName()`: 제네릭 타입 $T$로 전달된 실제 객체의 클래스 이름을 런타임에 확인.

### 구체적 예시
- **성공 케이스**: `Box<Integer>` 인스턴스에서 `inspect(10)`을 호출하면 $10$은 `Integer`이며 `Number`의 하위 타입이므로 정상 작동함.
- **실패 케이스**: `integerBox.inspect("some text")`
    - `"some text"`는 `String` 타입임.
    - `String`은 `Number`를 상속받지 않으므로 $U$의 제약 조건(`<U extends Number>`)을 위반하여 컴파일 에러가 발생함.

### 시험 포인트
- ⭐ **Bounded Type Parameter의 목적**: 특정 메서드 내에서 특정 클래스의 메서드(예: `Number`의 `intValue()`)를 안전하게 사용하기 위해 타입을 제한함.
- ⭐ **컴파일 에러 판별**: 제네릭 제약 조건(`extends`)에 맞지 않는 인자가 전달되었을 때 컴파일 단계에서 에러가 발생함을 이해해야 함.
- ⭐ **독립적 타입 파라미터**: 클래스 레벨의 제네릭 $T$와 메서드 레벨의 제네릭 $U$는 서로 독립적으로 정의될 수 있음.

---

## Slide 28

### 핵심 개념
- **제한된 타입 파라미터(Bounded Type Parameters)의 활용**: 제네릭 타입을 특정 클래스의 자식 클래스나 특정 인터페이스의 구현체로 제한하면, 해당 범위(Bound) 내에 정의된 메서드를 제네릭 코드 내에서 자유롭게 호출할 수 있습니다.
- **메서드 가용성**: 타입 파라미터 $T$가 특정 타입 $B$를 상속(`extends`)한다면, $T$ 타입의 객체는 $B$에 정의된 모든 public 메서드를 사용할 수 있음이 컴파일 타임에 보장됩니다.

### 코드/수식 해설
**1. 클래스 수준의 Bound**
```java
public class NaturalNumber<T extends Integer> {
    private T n;
    public boolean isEven() {
        return n.intValue() % 2 == 0; // Integer의 intValue() 호출 가능
    }
}
```
- $T$가 `Integer`로 제한되어 있으므로, `n` 객체에 대해 `Integer` 클래스의 메서드인 `intValue()`를 안전하게 호출할 수 있습니다.

**2. 메서드 수준의 Bound (Generic Method)**
```java
public static <T extends Comparable<T>> int countGreaterThan(T[] anArray, T elem) {
    int count = 0;
    for (T e : anArray)
        if (e.compareTo(elem) > 0) // Comparable의 compareTo() 호출 가능
            ++count;
    return count;
}
```
- `<T extends Comparable<T>>`: 타입 $T$가 자기 자신과 비교 가능한 `Comparable` 인터페이스를 구현했음을 명시합니다.
- 이를 통해 산술 연산자(`>`) 대신 `compareTo()` 메서드를 사용하여 객체 간의 크기 비교를 수행할 수 있습니다.

### 구체적 예시
- `NaturalNumber<Integer>`는 가능하지만, `NaturalNumber<String>`은 `String`이 `Integer`를 상속받지 않으므로 컴파일 에러가 발생합니다.
- `countGreaterThan` 메서드는 `Integer`, `String`, `Double` 등 `Comparable` 인터페이스가 구현된 모든 타입의 배열에 대해 동작합니다.

### 시험 포인트
- ⭐ **Bound의 이점**: 제네릭 코드 내에서 특정 메서드(예: `intValue()`, `compareTo()`)를 호출하기 위해서는 반드시 해당 메서드를 포함하는 타입으로 Bound를 설정해야 합니다.
- ⭐ **키워드**: Java 제네릭에서는 클래스와 인터페이스 구분 없이 Bound 설정 시 항상 `extends` 키워드를 사용함에 유의하세요.
- ⭐ **타입 안전성**: 잘못된 타입이 인자로 들어오는 것을 컴파일 단계에서 방지하여 런타임 오류(`ClassCastException`)를 예방합니다.

---

## Slide 29

### 핵심 개념
- **제네릭(Generics)**: 데이터 타입을 매개변수화하여 다양한 타입에 대해 동일한 로직을 재사용할 수 있게 하는 프로그래밍 기법입니다.
- **서브타입(Subtypes)**: 한 타입 $S$가 다른 타입 $T$의 모든 기능을 포함하고 있어, $T$가 필요한 곳에 $S$를 대신 사용할 수 있는 관계($S <: T$)를 의미합니다.
- 본 단원에서는 제네릭 타입과 서브타입 관계가 결합되었을 때 발생하는 타입 안정성(Type Safety) 이슈와 설계 원칙을 다룹니다.

### 코드/수식 해설
- **서브타입 관계 표기**:
  - 타입 $S$가 타입 $T$의 서브타입임을 다음과 같이 표기합니다: $$S <: T$$
- **제네릭의 불변성(Invariance)**:
  - 일반적으로 C++에서 `Student`가 `Person`의 서브타입($Student <: Person$)이더라도, `vector<Student>`는 `vector<Person>`의 서브타입이 아닙니다. 이를 **불변성(Invariance)**이라고 합니다.

### 구체적 예시
- **서브타입 예시**: `class Circle : public Shape` 관계에서 `Circle` 객체는 `Shape` 포인터에 할당될 수 있습니다.
- **제네릭 예시**: `template <typename T>`를 사용하는 클래스나 함수가 해당하며, `T`에 `int`, `double`, 혹은 사용자 정의 클래스가 대입될 수 있습니다.

### 시험 포인트
- ⭐ **제네릭과 서브타이핑의 차이**: 제네릭은 '타입 추상화'를 통한 코드 재사용에, 서브타이핑은 '런타임 다형성'과 '인터페이스 공유'에 초점이 맞춰져 있음을 구분해야 합니다.
- ⭐ **타입 안정성**: 제네릭 컨테이너 간에 서브타입 관계를 허용했을 때 발생할 수 있는 런타임 오류(예: `vector<Person*>`에 `Student*`를 넣고 나중에 `Professor*`로 접근하려는 시도 등)를 방지하기 위해 C++이 취하는 엄격한 타입 체킹 방식을 이해해야 합니다.

---

## Slide 30

## Generics and Subtyping

### 핵심 개념
- **제네릭과 서브타입 관계**: 일반적인 타입 간의 상속 관계(Subtyping)가 제네릭 타입(Generic types)으로 그대로 전이되는지에 대한 문제를 다룹니다.
- **타입 전이의 의문**: $Integer$가 $Number$의 서브타입일 때, 이를 감싸는 제네릭 클래스인 $Box<Integer>$가 $Box<Number>$의 서브타입이 될 수 있는지를 분석합니다.
- **불변성(Invariance)**: 대부분의 객체지향 언어(C++, Java 등)에서 제네릭 타입은 기본적으로 **불변(Invariant)**합니다. 즉, 타입 인자 간에 상속 관계가 있더라도 제네릭 타입 간에는 상속 관계가 성립하지 않습니다.

### 코드/수식 해설
- **기본 상속 관계**: $Integer \leq Number$ ($Integer$는 $Number$의 서브타입)
- **제네릭 서브타이핑 질문**: $Box<Integer> \stackrel{?}{\leq} Box<Number>$
- **명세 비교(Comparing specifications)**: $Box<Integer>$가 $Box<Number>$의 서브타입이 되려면, $Box<Number>$의 모든 명세를 $Box<Integer>$가 만족해야 합니다(Liskov Substitution Principle).

### 구체적 예시
- 만약 $Box<Integer>$가 $Box<Number>$의 서브타입이라고 가정하면 다음과 같은 문제가 발생할 수 있습니다:
  1. `Box<Number>` 타입의 포인터가 `Box<Integer>` 객체를 가리킴.
  2. `Box<Number>` 인터페이스를 통해 해당 객체에 `Double` 값을 넣으려고 시도함.
  3. 실제 객체는 `Integer`만 담을 수 있는 $Box<Integer>$이므로 타입 안전성(Type Safety)이 깨짐.

### 시험 포인트
- ⭐ **제네릭의 불변성(Invariance)**: $S \leq T$라고 해서 $G<S> \leq G<T>$가 성립하지 않는다는 사실은 시험에 자주 출제되는 단골 개념입니다.
- ⭐ **Subtyping 판단 근거**: 두 제네릭 타입 간의 관계를 정의할 때는 단순히 타입 인자를 보는 것이 아니라, 각 타입의 **명세(Specification)**를 비교하여 대체 가능성을 따져야 합니다.

---

## Slide 31

### 핵심 개념
- **제네릭의 불변성(Invariance)**: $Integer$가 $Number$의 하위 타입($Integer \le Number$)일지라도, `Box<Integer>`와 `Box<Number>` 사이에는 아무런 상속 관계가 성립하지 않습니다.
- **가변성(Variance)의 충돌**:
    - **공변성(Covariance)**: 리턴 타입은 하위 타입으로 갈수록 구체적이어야 합니다.
    - **반공변성(Contravariance)**: 메서드 인자 타입은 하위 타입으로 갈수록 더 추상적(넓은 범위)이어야 합니다.
- `Box` 클래스는 데이터를 입력($set$)받고 출력($get$)하는 기능을 모두 포함하므로, 두 방향의 가변성을 동시에 만족할 수 없어 서로 하위 타입이 될 수 없습니다.

### 코드/수식 해설
**1. 메서드 사양(Specification) 비교**
- **입력 ($set$ 메서드)**:
    - `Box<Number>.set(Number t)`는 `Box<Integer>.set(Integer t)`보다 더 넓은 타입 범위를 수용합니다.
    - 따라서 입력 조건의 유연성 측면에서 `Box<Number>.set` $>$ `Box<Integer>.set` 관계를 가집니다 (반공변성 원리).
- **출력 ($get$ 메서드)**:
    - `Box<Integer>.get()`은 `Integer`를 보장하지만, `Box<Number>.get()`은 `Number`까지만 보장합니다.
    - 더 구체적인 정보를 제공하는 `Box<Integer>.get`이 `Box<Number>.get`보다 강한 보장을 제공합니다 (공변성 원리).

**2. 하위 타입 불성립 원인**
- $Box<Integer> \le Box<Number>$ 가 성립하려면 $set$ 메서드의 인자가 $Number$이거나 그보다 넓어야 하는데, 실제로는 $Integer$로 더 좁기 때문에 LSP(리스코프 치환 원칙) 위반입니다.
- $Box<Number> \le Box<Integer>$ 가 성립하려면 $get$ 메서드의 반환 타입이 $Integer$이거나 그보다 구체적이어야 하는데, 실제로는 $Number$로 더 넓기 때문에 LSP 위반입니다.

### 구체적 예시
만약 `Box<Number> b = new Box<Integer>();` (공변성)가 허용된다고 가정하면:
```java
Box<Number> b = new Box<Integer>();
b.set(3.14); // Number의 하위 타입인 Double 입력 시도
// 실제 객체는 Box<Integer>이므로 실행 시 타입 에러 발생 가능
```
이러한 타입 부정합을 방지하기 위해 Java/C++ 등의 언어에서 제네릭은 기본적으로 **Invariance**를 유지합니다.

### 시험 포인트
- ⭐ **Invariance 개념**: `Box<Number>`와 `Box<Integer>`는 서로 남남 관계임을 명확히 이해해야 합니다.
- ⭐ **LSP와 가변성**: 서브타이핑이 성립하기 위해 메서드 인자는 반공변($Contravariant$), 반환 값은 공변($Covariant$)이어야 한다는 원칙을 실제 코드에 적용할 수 있어야 합니다.
- ⭐ **컴파일 에러 판단**: $Box<Integer>$ 객체를 $Box<Number>$ 타입 레퍼런스에 할당하려는 시도가 왜 컴파일 타임에 거부되는지 논리적으로 기술하는 문제가 출제될 수 있습니다.

---

## Slide 32

## 핵심 개념
- **제네릭의 유연성(Generics Flexibility)**: 제네릭 타입을 설계할 때, 고정된 타입 파라미터 $E$만 사용하면 상속 관계에 있는 하위 타입 객체들을 처리할 수 없어 재사용성이 떨어집니다.
- **한정적 타입 파라미터(Bounded Type Parameters)**: `<T extends E>`와 같은 구문을 사용하여, 특정 타입 $E$ 및 그 하위 타입 $T$를 모두 수용할 수 있는 유연한 설계를 구현합니다.
- **불변성(Invariance) 문제**: 제네릭에서 `Collection<Integer>`는 `Collection<Number>`의 하위 타입이 아닙니다. 이를 해결하기 위해 공변성(Covariance)을 허용하는 문법이 필요합니다.

## 코드/수식 해설
- **제약이 심한 설계 (Invariant)**:
  ```java
  void addAll(Collection<E> c);
  ```
  - 이 경우, `Set<Number>`에 `List<Integer>`를 추가하려고 하면 타입 불일치 오류가 발생합니다.

- **유연한 설계 (Bounded Type Parameter)**:
  ```java
  <T extends E> void addAll(Collection<T> c);
  ```
  - $T$가 $E$의 하위 타입($T \subseteq E$)이기만 하면 어떤 컬렉션이든 인자로 받을 수 있습니다.
  - 슬라이드 예시: `Set<Number>`의 `addAll`에 `List<Integer>` 전달이 가능해집니다 ($Integer$가 $Number$를 상속하기 때문).

## 구체적 예시
- **상황**: `Set<Number> numberSet`이 있고, `List<Integer> intList`를 추가하려는 경우
  - `void addAll(Collection<E> c)` 사용 시: $E$는 $Number$로 고정되므로, `Collection<Integer>`인 `intList`는 인자로 전달될 수 없음 (컴파일 에러).
  - `<T extends E> void addAll(Collection<T> c)` 사용 시: $T$를 $Integer$로 추론할 수 있고, $Integer$는 $Number$를 확장하므로 정상 작동.

## 시험 포인트
- ⭐ **Invariance vs Covariance**: 제네릭 타입 자체는 기본적으로 불변(Invariant)임을 이해하고, 왜 `<T extends E>`가 필요한지 서술할 수 있어야 합니다.
- ⭐ **Type Safety**: 유연성을 높이면서도 타입 안정성($T$는 반드시 $E$의 일종이어야 함)을 유지하는 원리를 파악해야 합니다.
- ⭐ **Wildcard Preview**: 슬라이드 마지막에서 언급된 "더 간결한 문법"은 와일드카드(`? extends E`)를 의미하며, 이는 구현부에서 $T$라는 이름을 사용할 필요가 없을 때 유용합니다.

---

## Slide 33

### 핵심 개념
- **와일드카드 (Wildcard)**: 제네릭 프로그래밍에서 '알 수 없는 타입'을 나타내기 위해 기호 `?`를 사용합니다.
- **제한된 와일드카드 (Bounded Wildcards)**: 변수나 메서드 매개변수에서 타입의 범위를 제한하여 유연성과 타입 안정성을 동시에 확보합니다.
    - **Upper Bounded**: 특정 클래스와 그 하위 클래스들만 허용합니다.
    - **Lower Bounded**: 특정 클래스와 그 상위 클래스들만 허용합니다.

### 코드/수식 해설
- **상한 제한 (Upper Bounded)**: $<? \text{ extends } T>$
    - $T$ 또는 $T$의 하위 타입(subtype)인 불특정 타입을 의미합니다.
- **무제한 (Unbounded)**: $<?>$
    - $<? \text{ extends Object}>$의 축약형으로, 어떤 타입이든 올 수 있음을 의미합니다.
- **하한 제한 (Lower Bounded)**: $<? \text{ super } T>$
    - $T$ 또는 $T$의 상위 타입(supertype)인 불특정 타입을 의미합니다.

### 구체적 예시
- **Upper Bound**: `List<? extends Number>` 
    - `List<Integer>`, `List<Double>` 등 `Number`를 상속받는 모든 리스트를 참조할 수 있습니다.
- **Lower Bound**: `List<? super Integer>`
    - `List<Integer>`, `List<Number>`, `List<Object>`와 같이 `Integer`의 부모 클래스 리스트를 참조할 수 있습니다.

### 시험 포인트
- ⭐ **와일드카드 범위 구분**: $<? \text{ extends } T>$는 읽기(Reading) 작업에, $<? \text{ super } T>$는 쓰기(Writing) 작업에 주로 사용됨을 이해해야 합니다 (PECS 원칙: Producer Extends, Consumer Super).
- ⭐ **타입 호환성**: $<?>$와 $<? \text{ extends Object}>$가 논리적으로 동일하다는 점을 숙지하세요.
- ⭐ **상속 관계**: 제네릭 클래스 간의 상속 관계(Invariance)를 해결하기 위해 와일드카드가 도입되었음을 파악하는 것이 중요합니다.

---

## Slide 34

### 핵심 개념
- **한정적 와일드카드(Bounded Wildcards)**: 제네릭 타입을 사용할 때 `? extends E`와 같은 문법을 통해 타입의 범위를 제한하면서도 유연성을 극대화하는 기법입니다.
- **API 유연성**: 고정된 타입 $E$만 받는 것보다 $E$의 하위 타입까지 수용함으로써 재사용성을 높입니다.

### 코드/수식 해설
```java
interface Set<E> {
    void addAll(Collection<? extends E> c);
}
```
1. **`void addAll(Collection<E> c)`와의 비교**:
   - 이 방식은 정확히 $E$ 타입의 컬렉션만 인자로 받을 수 있어 유연성이 떨어집니다.
   - 와일드카드를 사용하면 $E$를 상속받은 모든 타입의 컬렉션을 다룰 수 있습니다.

2. **`<T extends E> void addAll(Collection<T> c)`와의 비교**:
   - 두 방식은 기능적으로 동일(Equally powerful)합니다.
   - 하지만 타입 매개변수 $T$를 명시적으로 선언하지 않는 와일드카드 방식이 더 간결(Concise)하며, 가독성이 좋습니다.
   - 일반적으로 타입 매개변수가 메서드 선언에서 한 번만 등장한다면 와일드카드를 사용하는 것이 권장됩니다.

### 구체적 예시
- 만약 `Set<Number>` 객체가 있다면:
    - `addAll(Collection<Number> c)` 방식: `List<Integer>`를 인자로 넣을 수 없음 (컴파일 에러).
    - `addAll(Collection<? extends Number> c)` 방식: `Integer`는 `Number`의 하위 타입이므로 `List<Integer>`를 안전하게 추가할 수 있음.

### 시험 포인트
- ⭐ **PECS 원칙 (Producer-Extends, Consumer-Super)**: 데이터를 가져오는(생산하는) 쪽은 `extends`를, 데이터를 넣는(소비하는) 쪽은 `super`를 사용해야 합니다. 위 예시는 `c`로부터 데이터를 읽어오므로 `extends`를 사용한 것입니다.
- ⭐ **와일드카드 vs 타입 매개변수**: 두 방식의 기능적 차이점과 코드 간결성 측면에서의 선택 기준을 구분할 수 있어야 합니다.
- ⭐ **상속 관계의 불공변성(Invariance)**: `List<Integer>`는 `List<Number>`의 하위 타입이 아니라는 점을 해결하기 위해 와일드카드가 필요함을 이해해야 합니다.

---

## Slide 35

### 핵심 개념
- **Upper Bounded Wildcards (`? extends T`)**: 제네릭 타입을 특정 클래스($T$)나 그 하위 클래스로 제한하는 방식입니다.
- **공변성(Covariance) 활용**: `List<? extends Number>`는 `Number` 뿐만 아니라 `Integer`, `Double` 등 `Number`를 상속받는 모든 타입의 리스트를 인자로 받을 수 있게 합니다.
- **읽기 전용 안전성**: 리스트의 각 요소가 최소한 `Number` 타입임이 보장되므로, 이를 `Number` 타입 변수에 할당하여 사용하는 것이 안전합니다.

### 코드/수식 해설
```java
public static double sumOfList(List<? extends Number> list) {
    double s = 0.0;
    for (Number n : list) s += n.doubleValue();
    return s;
}
```
- `List<? extends Number>`: 리스트에 담긴 요소의 타입이 $Number$의 하위 타입임을 명시합니다.
- `for (Number n : list)`: 리스트 내부의 객체가 무엇이든 $Number$의 기능을 가지고 있으므로 `n.doubleValue()` 호출이 가능합니다.
- **주의**: `List<? super Number>`를 사용하면 `Number`의 상위 타입(예: `Object`)이 올 수 있어, `doubleValue()`와 같은 $Number$의 메서드를 안전하게 호출할 수 없으므로 컴파일 에러가 발생합니다.

### 구체적 예시
- **허용되는 호출**: `sumOfList(new ArrayList<Integer>())`, `sumOfList(new ArrayList<Double>())` 등.
- **허용되지 않는 호출**: `sumOfList(new ArrayList<Object>())` (상위 타입이므로 부적합).

### 시험 포인트
- ⭐ **PECS 원칙 (Producer Extends, Consumer Super)**: 데이터를 읽어오는 "생산자" 입장에서는 `extends`를, 데이터를 삽입하는 "소비자" 입장에서는 `super`를 사용해야 함을 이해해야 합니다.
- ⭐ **상한 제한(Upper Bound)의 목적**: 다형성을 제네릭에 적용하여, 특정 클래스의 인터페이스/메서드를 안전하게 사용하기 위함입니다.
- ⭐ **컴파일 타임 체크**: `List<? extends Number>`에 새로운 요소를 `add()` 하려고 시도할 경우, 구체적인 타입을 확신할 수 없으므로 컴파일 에러가 발생한다는 점에 주의하세요.

---

## Slide 36

### 핵심 개념
- **Lower Bounded Wildcards (`? super T`)**: 특정 타입 $T$ 또는 그 부모 타입들을 허용하는 제네릭 제약입니다.
- **쓰기 가능성(Writability)**: `? super T`를 사용하면 해당 컬렉션에 $T$ 타입의 객체를 안전하게 추가(add)할 수 있습니다. 이는 컬렉션의 실제 타입이 최소한 $T$이거나 그보다 상위 타입임이 보장되기 때문입니다.
- **Upper Bounded Wildcards (`? extends T`)와의 차이**: `? extends T`는 읽기 전용에 가깝습니다. 실제 타입이 $T$의 하위 타입(예: `Integer`가 아닌 `Double`)일 수 있으므로, 특정 타입을 추가하려고 하면 타입 불일치로 인해 컴파일 에러가 발생합니다.

### 코드/수식 해설
```java
public static void addNumbers(List<? super Integer> list) {
    for (int i = 1; i <= 10; i++) {
        list.add(i); // 안전하게 추가 가능
    }
}
```
- `List<? super Integer>`: `List<Integer>`, `List<Number>`, `List<Object>` 등이 인자로 전달될 수 있습니다.
- `list.add(i)`: $i$는 `Integer` 타입입니다. 위에서 언급된 모든 가능한 리스트 타입들은 `Integer`를 요소로 받아들일 수 있으므로 타입 안정성이 보장됩니다.

### 구체적 예시
- **성공 케이스**: `addNumbers`에 `List<Number>`를 전달할 경우, `Number`는 `Integer`의 부모 타입이므로 `Integer` 객체를 추가하는 데 문제가 없습니다.
- **실패 케이스**: 만약 매개변수가 `List<? extends Number>`였다면, 실제 인자로 `List<Double>`이 들어올 수 있습니다. 이 경우 `Integer`를 추가하는 코드는 컴파일 단계에서 거부됩니다.

### 시험 포인트
- ⭐ **PECS 원칙**: **P**roducer-**E**xtends, **C**onsumer-**S**uper. 데이터를 제공(Read)할 때는 `extends`를, 데이터를 소비/수집(Write)할 때는 `super`를 사용해야 합니다.
- ⭐ **컴파일 에러 원인 분석**: `List<? extends T>`에 객체를 `add`하려고 시도할 때 발생하는 에러의 이유(런타임 타입의 불확실성)를 서술하는 문제가 자주 출제됩니다.
- ⭐ **상속 관계**: `Integer` $\subset$ `Number` $\subset$ `Object` 관계에서 `? super Integer`가 허용하는 범위와 그에 따른 다형성 활용 능력을 평가합니다.

---

## Slide 37

### 핵심 개념
**PECS (Producer Extends, Consumer Super)**는 제네릭 프로그래밍에서 와일드카드(`?`)를 언제 어떻게 사용할지 결정하는 가이드라인입니다. 

*   **Producer (생성자)**: 데이터를 제공(read)하는 역할을 하는 변수. 객체로부터 값을 꺼내와야 할 때 사용합니다.
*   **Consumer (소비자)**: 데이터를 소비(write)하는 역할을 하는 변수. 객체에 값을 집어넣어야 할 때 사용합니다.
*   **Invariant (불변)**: 데이터를 읽고 쓰는 작업을 동시에 수행해야 하는 경우 와일드카드를 사용하지 않고 구체적인 타입 $T$를 명시합니다.

### 코드/수식 해설
*   **`<? extends T>`**: Upper Bounded Wildcard. $T$ 또는 $T$의 하위 클래스들만 허용합니다. (Covariance)
*   **`<? super T>`**: Lower Bounded Wildcard. $T$ 또는 $T$의 상위 클래스들만 허용합니다. (Contravariance)

```java
// Producer: 데이터를 읽기만 함
void copy(List<? extends T> src, List<? super T> dest) {
    for (T item : src) { // src는 T를 생산(produce)함
        dest.add(item);  // dest는 T를 소비(consume)함
    }
}
```

### 구체적 예시
1.  **`List<? extends Number>`**: `Integer`, `Double` 등을 `Number` 타입으로 안전하게 **읽을(get)** 수 있지만, 어떤 하위 타입이 올지 알 수 없으므로 새로운 요소를 **추가(add)**하는 것은 불가능합니다.
2.  **`List<? super Integer>`**: `Integer`, `Number`, `Object` 리스트에 `Integer` 객체를 안전하게 **추가(add)**할 수 있습니다. 하지만 꺼낼 때 어떤 상위 타입일지 보장할 수 없으므로 `Object` 외의 특정 타입으로 **읽는(get)** 것은 제한됩니다.

### 시험 포인트
*   ⭐ **PECS 법칙 암기**: "읽을 때는 `extends`, 쓸 때는 `super`" 공식을 반드시 숙지해야 합니다.
*   ⭐ **제약 사항**: `<? extends T>`로 선언된 컬렉션에 `null` 이외의 요소를 추가하려고 하면 컴파일 에러가 발생한다는 점이 자주 출제됩니다.
*   ⭐ **다형성과의 관계**: 제네릭의 불변성(Invariance) 문제를 해결하고 유연한 API를 설계하기 위해 와일드카드가 필요함을 이해해야 합니다.

---

## Slide 38

### 핵심 개념
와일드카드를 이용한 제네릭 프로그래밍에서 **PECS(Producer-Extends, Consumer-Super)** 원칙을 적용한 예시입니다.
- **`? extends T` (Upper Bounded Wildcard)**: $T$ 또는 $T$의 하위 타입을 읽기만 할 때(Producer) 사용합니다.
- **`? super T` (Lower Bounded Wildcard)**: $T$ 또는 $T$의 상위 타입에 쓰기만 할 때(Consumer) 사용합니다.
- 이 원칙을 통해 제네릭 타입의 유연성(Subtyping)을 확보하면서도 타입 안정성을 유지할 수 있습니다.

### 코드/수식 해설
```java
static <T> void copyTo(Box<? extends T> src, Box<? super T> dst) {
    dst.set(src.get());
}
```
- `src.get()`은 최소 $T$ 타입임이 보장되므로, $T$ 또는 그 상위 타입을 저장할 수 있는 `dst.set()`에 전달하는 것이 안전합니다.
- `src`는 데이터를 제공하므로 `extends`, `dst`는 데이터를 받아 소비하므로 `super`를 사용합니다.

### 구체적 예시
$T$가 `Number`인 상황을 가정합니다.
- **`copyTo(intBox, numBox);` // OK**: `Integer`는 `Number`를 상속받으므로 `src`가 될 수 있고, `Number`는 `Number` 자신(또는 상위)이므로 `dst`가 될 수 있습니다.
- **`copyTo(numBox, intBox);` // Error**: `numBox`에는 `Double`이 들어있을 수 있는데, 이를 `intBox`에 넣으려고 하면 런타임 에러가 발생할 수 있으므로 컴파일 단계에서 차단합니다.

### 시험 포인트
- ⭐ **PECS 원칙 적용**: 데이터를 꺼내오는 객체(Producer)에는 `extends`를, 데이터를 담는 객체(Consumer)에는 `super`를 사용해야 함을 반드시 기억하세요.
- ⭐ **컴파일 에러 판별**: 상속 관계(Subtyping)를 분석하여 특정 제네릭 메서드 호출이 가능한지 여부를 묻는 문제가 자주 출제됩니다.
- ⭐ **타입 안전성**: 와일드카드를 사용함으로써 얻는 이점은 "컴파일 타임에 타입 불일치를 잡아낼 수 있다"는 점입니다.

---

## Slide 39

### 핵심 개념
- **와일드카드 `?`**: "구체적이지만 알 수 없는 특정 타입(specific but unknown type)"을 의미합니다.
- **제네릭의 불변성(Invariance)**: Java 등의 언어에서 `Box<String>`은 `Box<Object>`의 하위 타입이 아니므로 대입이 불가능합니다. 하지만 `Box<?>`는 모든 `Box<T>`의 상위 타입처럼 동작하여 대입이 가능합니다.
- **상한 제한 와일드카드 (`? extends Foo`)**: `Foo` 또는 `Foo`를 상속받은 하위 타입 중 하나를 의미합니다.

### 코드/수식 해설
```java
// 1. Box<?> vs Box<Object>
Box<?> box1 = new Box<String>();      // 유효 (Wildcard는 모든 타입을 수용)
Box<Object> box2 = new Box<String>(); // 오류 (제네릭 타입 간에는 상속 관계가 성립하지 않음)

// 2. Box<Foo> vs Box<? extends Foo>
// Box<? extends Foo>는 'Foo의 하위 타입 중 결정되지 않은 어느 하나'를 의미
// Box<Foo>는 'Foo 자체'를 타입으로 가지며 Foo의 모든 자식을 원소로 가질 수 있음
```
- `$Box<T>$`에서 `$T$`가 `$Object$`로 지정된 것과 `$?$`로 지정된 것은 할당 가능성($assignability$)에서 큰 차이를 보입니다.

### 구체적 예시
`Animal` 클래스를 `Dog`와 `Cat`이 상속받는 경우:
- **`Box<Animal>`**: `Dog` 객체와 `Cat` 객체를 **동시에** 담을 수 있는 상자입니다.
- **`Box<? extends Animal>`**: "어떤 동물의 하위 타입" 전용 상자입니다. 만약 실제 타입이 `Box<Dog>`로 결정되었다면, 그 상자에는 `Dog`만 넣을 수 있고 `Cat`은 넣을 수 없습니다. (즉, 런타임에 타입 안전성을 보장하기 위해 사용됩니다.)

### 시험 포인트
- ⭐ `Box<Object> b = new Box<String>();`이 컴파일 에러가 발생하는 이유(Generic Invariance)를 이해해야 합니다.
- ⭐ `Box<?>`는 읽기(read)는 `$Object$` 타입으로 가능하지만, 쓰기(write)는 타입 안전성 문제로 제한된다는 점이 중요합니다.
- ⭐ `Box<Foo>`와 `Box<? extends Foo>`의 차이점: 전자는 다형성을 통해 여러 자식 타입을 섞어서 저장할 수 있지만, 후자는 특정 자식 타입 **하나**에 고정되어야 함을 시사합니다.

---

## Slide 40

### 핵심 개념
- **와일드카드(Wildcard)와 상한/하한 제한**: Java 제네릭에서 `?`는 알 수 없는 타입을 의미하며, `extends`와 `super`를 통해 타입을 제한할 수 있습니다.
- **Upper Bounded Wildcard (`? extends T`)**: $T$ 또는 $T$의 하위 클래스만 허용합니다. 데이터를 안전하게 **읽기(Get)** 위한 목적으로 사용됩니다 (Producer).
- **Lower Bounded Wildcard (`? super T`)**: $T$ 또는 $T$의 상위 클래스만 허용합니다. 데이터를 안전하게 **쓰기(Set)** 위한 목적으로 사용됩니다 (Consumer).
- **PECS 원칙**: **P**roducer-**E**xtends, **C**onsumer-**S**uper. 데이터를 제공하면 `extends`, 데이터를 소비(저장)하면 `super`를 사용합니다.

### 코드/수식 해설

#### 1. `Box<? extends Number>` (Upper Bound)
- **할당**: `Box<Number>`나 `Box<Integer>`는 가능하지만, 상한선인 $Number$보다 높은 `Box<Object>`는 할당 불가입니다.
- **Set (Write) 불가**: `box.set()`에 `null` 이외의 객체를 넣을 수 없습니다. 런타임 시 실제 타입이 `Box<Double>`일지 `Box<Integer>`일지 알 수 없으므로 타입 안전성을 위해 금지합니다.
- **Get (Read) 가능**: 꺼내는 모든 객체는 최소 $Number$임을 보장받으므로 `Number num = box.get()`은 가능합니다.

#### 2. `Box<? super Number>` (Lower Bound)
- **할당**: `Box<Number>`나 `Box<Object>`는 가능하지만, 하한선인 $Number$보다 낮은 `Box<Integer>`는 할당 불가입니다.
- **Set (Write) 가능**: $Number$ 및 그 하위 타입($Integer$ 등)을 안전하게 넣을 수 있습니다. 어떤 경우든 최소 $Number$ 이상의 타입을 수용할 수 있는 박스이기 때문입니다.
- **Get (Read) 제한**: 꺼낸 객체가 $Number$라는 보장이 없으며(예: `Box<Object>`), 오직 $Object$ 타입으로만 안전하게 받을 수 있습니다.

### 구체적 예시
슬라이드 오른쪽 예시(`? super Number`)에서:
```java
box.set(num);      // OK: Number는 Number의 하위 타입(자신)이므로 안전
num = box.get();   // Error: 실제 타입이 Box<Object>일 수 있어 Number로 확신 불가
```
- 실제 인스턴스가 `new Box<Object>()`인 경우, `get()`으로 반환된 값이 $Number$가 아닐 수 있기 때문에 컴파일 에러가 발생합니다.

### 시험 포인트
- ⭐ **Assignment Rule**: 특정 와일드카드 변수에 어떤 제네릭 인스턴스를 할당할 수 있는지 묻는 문제가 자주 출제됩니다. (예: `Box<? extends T>`에 `Box<S>` 할당 시 $S <: T$ 관계 확인)
- ⭐ **Get/Set 가능 여부**: `extends`는 'Read-Only' (단, $Object$로만 읽는 것은 둘 다 가능), `super`는 'Write-Only' (단, $Number$ 이하 타입만 write 가능) 특성을 정확히 이해해야 합니다.
- ⭐ **Type Safety**: 왜 `? extends Number`에서 `set(Integer)`가 불가능한지 논리적으로 설명할 수 있어야 합니다 (실제 타입이 `Box<Double>`일 가능성 때문).

---

## Slide 41

## Wildcards and Subtyping

### **핵심 개념**
제네릭 타입의 불공변성(Invariance)을 해결하기 위해 와일드카드($?$)를 사용하며, 이를 통해 제네릭 클래스 간의 상속 관계(Subtyping)를 정의합니다.
*   **Unbounded Wildcard ($?$):** 모든 제네릭 타입의 공통 조상입니다.
*   **Upper Bounded Wildcard ($? \text{ extends } T$):** $T$ 또는 $T$를 상속받는 하위 타입들을 의미하며, 공변성(Covariance)을 가집니다.
*   **Lower Bounded Wildcard ($? \text{ super } T$):** $T$ 또는 $T$의 상위 타입들을 의미하며, 반공변성(Contravariance)을 가집니다.

### **코드/수식 해설**
1. **불공변성 및 무제한 와일드카드**
    ```java
    Box<Integer> intBox = new Box<>();
    Box<Number> numBox = intBox;    // Compile-time error: Box<Integer>는 Box<Number>의 서브타입이 아님
    Box<?> anyBox = intBox;         // OK: Box<?>는 모든 Box<T>의 슈퍼타입
    ```
    *   $Box<Integer>$와 $Box<Number>$는 상속 관계가 없습니다.
    *   $Box<?>$는 $Box<Integer>$ 및 $Box<Number>$의 공통 부모입니다.

2. **상한 제한 와일드카드 (Upper Bound)**
    *   수식: $A$ 가 $B$ 의 서브타입($A <: B$)이면, $Box<? \text{ extends } A> <: Box<? \text{ extends } B>$ 입니다.
    ```java
    Box<? extends Integer> intBox = new Box<>();
    Box<? extends Number> numBox = intList; // OK: Integer는 Number의 서브타입이므로 성립
    ```

3. **하한 제한 와일드카드 (Lower Bound)**
    *   수식: $A$ 가 $B$ 의 서브타입($A <: B$)이면, $Box<? \text{ super } B> <: Box<? \text{ super } A>$ 입니다. (관계가 역전됨)

### **구체적 예시**
*   **Subtyping Hierarchy:**
    *   $Box<? \text{ extends } \text{Integer}>$ $\subset$ $Box<? \text{ extends } \text{Number}>$ $\subset$ $Box<?>$
    *   $Box<? \text{ super } \text{Number}>$ $\subset$ $Box<? \text{ super } \text{Integer}>$ $\subset$ $Box<?>$

### **시험 포인트**
*   ⭐ **Invariance:** 일반적인 제네릭 타입 $Box<A>$와 $Box<B>$는 $A$와 $B$의 관계에 상관없이 아무런 상속 관계가 없음을 이해해야 합니다.
*   ⭐ **Wildcard Subtyping Rule:** `extends`는 클래스 계층 구조의 방향과 일치하게 서브타이핑이 이뤄지지만, `super`는 그 방향이 반대(Contravariant)가 된다는 점이 자주 출제됩니다.
*   ⭐ **Assignability:** 어떤 와일드카드 타입 변수에 어떤 객체를 대입할 수 있는지(Liskov Substitution Principle 적용) 판단하는 문제가 나올 수 있습니다.

---

## Slide 42

### 핵심 개념
제네릭 타입에서 와일드카드(`?`)를 사용한 **서브타이핑(Subtyping)** 계층 구조를 설명합니다. 일반적인 제네릭 클래스 `Box<T>`는 $T$의 상속 관계와 상관없이 서로 독립적(Invariant)이지만, 와일드카드를 통해 공변성(Covariance)과 반공변성(Contravariance)을 부여할 수 있습니다.

- **Unbounded Wildcard (`Box<?>`)**: 모든 `Box` 제네릭 타입의 최상위 루트입니다.
- **Upper Bounded Wildcard (`? extends T`)**: $T$ 및 그 하위 타입을 허용하며, 계층 구조에서 위쪽으로 갈수록 범위가 넓어집니다.
- **Lower Bounded Wildcard (`? super T`)**: $T$ 및 그 상위 타입을 허용하며, 계층 구조에서 아래쪽으로 갈수록 구체화됩니다.

### 코드/수식 해설
슬라이드에 나타난 계층 구조를 기호 $\subset$ (서브타입 관계)으로 나타내면 다음과 같습니다.

1.  **Upper Bound (공변성) 경로**:
    - `Box<Integer>` $\subset$ `Box<? extends Integer>` $\subset$ `Box<? extends Number>` $\subset$ `Box<?>`
2.  **Lower Bound (반공변성) 경로**:
    - `Box<Number>` $\subset$ `Box<? super Number>` $\subset$ `Box<? super Integer>` $\subset$ `Box<?>`
3.  **교차 지점**:
    - `Box<Integer>`는 `Box<? super Integer>`의 서브타입입니다.
    - `Box<Number>`는 `Box<? extends Number>`의 서브타입입니다.

### 구체적 예시
- **`Box<? extends Number>`**: `Box<Integer>`나 `Box<Double>` 등을 할당받을 수 있어 읽기 작업(Getter)에 안전합니다.
- **`Box<? super Integer>`**: `Box<Integer>`나 `Box<Number>` 등을 할당받을 수 있어 `Integer` 데이터를 쓰기 작업(Setter)에 안전합니다.

### 시험 포인트
- ⭐ **Invariance(무변성)**: `Integer`가 `Number`의 서브타입일지라도, `Box<Integer>`는 `Box<Number>`의 서브타입이 아닙니다.
- ⭐ **Wildcard Hierarchy**: 모든 와일드카드 타입의 최종 조상은 `Box<?>`입니다.
- ⭐ **관계 파악**: `Box<? extends Integer>`가 `Box<? extends Number>`의 서브타입이 되는 방향(상속 관계가 유지됨)과 `Box<? super Number>`가 `Box<? super Integer>`의 서브타입이 되는 방향(상속 관계가 역전됨)을 정확히 구분해야 합니다.

---

## Slide 43

## References

**핵심 개념**
- **강의 참고 자료**: 본 강의의 내용을 심화 학습하기 위한 주요 문헌 목록입니다. 
- **Liskov Substitution Principle (LSP)**: 리스코프 치환 원칙은 객체지향 설계의 핵심 원칙 중 하나로, 하위 타입 객체가 상위 타입 객체를 프로그램의 정확성을 해치지 않으면서 대체할 수 있어야 함을 의미합니다.

**코드/수식 해설**
- 해당 슬라이드에는 코드 및 수식이 포함되어 있지 않습니다.

**구체적 예시**
- **주요 문헌**:
    - *Core Java* (Chapter 8): 주로 제네릭(Generics) 관련 내용을 다룹니다.
    - *Effective Java* (Chapter 5): 제네릭의 올바른 사용법에 대한 실무 지침을 제공합니다.
    - *Program Development in Java* (B. Liskov 저): 추상화 및 계층 구조 설계 이론을 다룹니다.

**시험 포인트**
- ⭐ **리스코프 치환 원칙(LSP)**: 객체지향의 다형성과 상속 관계에서 자식 클래스가 부모 클래스의 규약(pre-condition, post-condition)을 어떻게 준수해야 하는지 묻는 문제가 출제될 가능성이 높습니다.
- ⭐ **제네릭(Generics)**: 참고 문헌의 챕터 구성으로 보아, C++의 Template과 대응되는 Java의 Generics 개념 및 타입 안정성에 대한 이해가 요구됩니다.

---

## Slide 44

- **핵심 개념**: 강의 마무리 및 질의응답(Q&A) 세션입니다. 학습한 내용 중 명확하지 않은 개념이나 보충 설명이 필요한 부분에 대해 소통하는 단계입니다.

- **코드/수식 해설**: 해당 사항 없음

- **구체적 예시**: 해당 사항 없음

- **시험 포인트**: ⭐ 슬라이드 자체의 내용은 시험과 무관하나, 질의응답 시간에 나온 교수님의 추가 설명이나 강조 사항은 시험에 반영될 수 있으므로 주의 깊게 확인해야 합니다.

---

## Slide 45

## 핵심 개념
- **Java Subtypes and Generics**: Java의 서브타입(Subtype) 관계와 제네릭(Generics) 시스템이 상호작용하는 원리를 다룹니다.
- **타입 계층 구조**: 객체지향 프로그래밍에서 클래스 간의 상속 관계가 제네릭 타입 파라미터로 전달될 때, 해당 제네릭 타입들 간에도 서브타입 관계가 유지되는지(공변성, 불변성 등)를 분석합니다.

## 코드/수식 해설
- **서브타입 관계 표기**: 타입 $S$가 타입 $T$의 서브타입인 경우, 일반적으로 $S \le T$ 또는 $S <: T$로 표기합니다.
- **제네릭의 불변성(Invariance)**: 일반적인 객체 지향의 다형성과 달리, Java의 제네릭은 기본적으로 불변성을 띱니다. 즉, $S \le T$라고 해서 `List<S>` $\le$ `List<T>`가 성립하지 않습니다.

## 구체적 예시
- `String`은 `Object`의 서브타입입니다 ($String \le Object$).
- 하지만 `ArrayList<String>` 객체를 `ArrayList<Object>` 타입의 참조 변수에 할당하려고 하면 컴파일 에러가 발생합니다. 이는 런타임에 발생할 수 있는 타입 불일치 오류를 방지하기 위함입니다.

## 시험 포인트
- ⭐ **Generics의 불변성(Invariance)**: 왜 `List<String>`이 `List<Object>`의 서브타입이 될 수 없는지 그 이유를 타입 안정성(Type Safety) 측면에서 서술할 수 있어야 합니다.
- ⭐ **Wildcards ($?$ 익명 타입)**: 서브타입 관계를 유연하게 적용하기 위해 사용하는 `<? extends T>`(공변성)와 `<? super T>`(반공변성)의 차이점을 숙지해야 합니다.

---

## Slide 46

## Java Arrays and Subtype (1)

**핵심 개념**
- **Java 배열의 특성**: `Type[]` 형태로 선언되며, 동일한 타입의 원소들을 저장함.
- **공변성 (Covariance)**: Java에서는 $T_1$이 $T_2$의 서브타입($T_1 \le T_2$)이면, $T_1[]$도 $T_2[]$의 서브타입($T_1[] \le T_2[]$)으로 간주함.
- **설계 배경**: 이론적으로 배열은 무관(unrelated/invariant)해야 하지만, Java는 초기 설계 당시의 하위 호환성(backward compatibility)을 위해 공변성을 채택함. 이는 엄밀한 의미에서 **True Subtyping**이 아님.

**코드/수식 해설**
- **배열 연산**:
  - 원소 참조: `x[i]`
  - 원소 수정: `x[i] = e`
- **서브타입 관계 수식**:
  - 이론적 원칙: $T_1 \le T_2 \implies T_1[] \text{ and } T_2[] \text{ are unrelated}$
  - Java의 실제 구현: $T_1 \le T_2 \implies T_1[] \le T_2[]$

**구체적 예시**
- `String`은 `Object`의 서브타입임.
- Java의 공변성 규칙에 따라 `String[]` 타입의 객체를 `Object[]` 타입의 변수에 할당할 수 있음.
```java
String[] strArray = new String[10];
Object[] objArray = strArray; // Java에서는 허용됨 (Covariance)
```

**시험 포인트**
- ⭐ **Covariance(공변성)**의 정의와 Java 배열에서의 적용 방식 이해.
- ⭐ Java 배열의 서브타이핑이 왜 **"not true subtyping"**인지, 그리고 이를 허용한 주된 이유(**backward compatibility**)가 무엇인지 파악.
- ⭐ 이론적 모델(Invariant)과 Java의 실제 구현 모델(Covariant) 사이의 차이점 비교.

---

## Slide 47

### 핵심 개념
- **Java 배열의 공변성(Covariance)**: Java에서 $S$가 $T$의 서브타입($S \leq T$)이면, 배열 $S[]$도 $T[]$의 서브타입($S[] \leq T[]$)으로 간주됩니다.
- **타입 안전성(Type Safety) 문제**: 이러한 공변성 때문에 컴파일 타임에는 올바른 코드로 보이지만, 런타임에 타입 불일치 오류가 발생할 수 있는 비안전한 상태가 됩니다.
- **동적 검사(Dynamic Check)**: Java는 런타임에 각 배열의 실제 타입(run-time type)을 유지하며, 호환되지 않는 타입의 저장을 시도할 때 이를 감지합니다.

### 코드/수식 해설
```java
String[] strs = new String[10];
Object[] objs = strs; // Java의 배열 공변성에 의해 허용됨

objs[1] = Integer.valueOf(1); // 컴파일은 성공하지만, 런타임에 ArrayStoreException 발생
int len = strs[1].length();    // 만약 위 줄이 실행되었다면 여기서 런타임 에러 발생
```
- $String \leq Object$ 관계에 따라 $String[] \leq Object[]$가 성립하여 `objs = strs` 할당이 가능합니다.
- 하지만 `objs`가 가리키는 실제 힙 메모리의 객체는 $String$ 배열이므로, $Integer$를 저장하려는 시도는 런타임에 차단됩니다.

### 구체적 예시
- **ArrayStoreException**: 런타임 시 배열 요소 할당 시점에 발생합니다. 코드의 4행에서 `objs[1]`에 $Integer$를 넣으려 할 때, JVM은 `objs`가 실제로는 `String[]`임을 확인하고 예외를 던집니다.

### 시험 포인트
- ⭐ Java 배열은 **공변(Covariant)**하지만, 이후 배우게 될 Generic은 **무공변(Invariant)**하다는 차이점을 비교하는 문제가 자주 출제됩니다.
- ⭐ 배열 공변성으로 인한 타입 오류는 컴파일 타임(Static)이 아닌 **런타임(Dynamic)**에 `ArrayStoreException`을 통해 발견된다는 점을 명심하세요.

---

## Slide 48

## Type Erasure

### 핵심 개념
- **Type Erasure(타입 소거)**: Java 컴파일러가 제네릭 타입을 컴파일 시점에 제거하고, 이를 일반 클래스, 인터페이스, 혹은 메서드로 변환하는 프로세스입니다.
- **동작 원리**:
    - 제네릭 타입의 타입 파라미터($T$)를 해당 파라미터의 **Bound**(제한 범위)가 있다면 그 타입으로, 없다면 `Object`로 치환합니다.
    - 타입 안정성(Type Safety)을 보장하기 위해 필요한 곳에 컴파일러가 자동으로 형 변환(Type Cast) 코드를 삽입합니다.
- **런타임 특성**: 런타임에는 제네릭 타입 정보가 존재하지 않으며, 모든 인스턴스화된 제네릭 객체는 동일한 로우 타입(Raw Type)을 공유합니다.

### 코드 해설
슬라이드 예제는 런타임에 타입 정보가 소거됨을 증명합니다.
```java
Box<String> box1 = new Box<>();
Box<Integer> box2 = new Box<>();

// 런타임에는 두 객체의 클래스 정보가 동일함
System.out.println(box1.getClass() == box2.getClass()); // true!
```
- `box1`과 `box2`는 컴파일 타임에는 각각 `Box<String>`, `Box<Integer>`로 다르게 취급되지만, 컴파일 후에는 둘 다 `Box`라는 동일한 클래스 파일 정보를 가집니다.
- 따라서 `getClass()` 결과는 동일하게 나타납니다.

### 구체적 예시
만약 제네릭 클래스가 `<T extends Number>`와 같이 정의되어 있다면, 컴파일러는 모든 $T$를 `Number`로 치환합니다. 별도의 상속 제한이 없는 `<T>`의 경우에는 모든 $T$가 `Object`로 치환됩니다.

### 시험 포인트
- ⭐ **런타임 타입 정보**: 제네릭 타입 정보는 런타임에 유지되지 않는다는 점(Runtime overhead 감소 및 하위 호환성 유지 목적)이 가장 중요합니다.
- ⭐ **Raw Type**: `Box<String>`과 `Box<Integer>`의 런타임 클래스 타입은 동일한 `Box.class`임을 기억하세요.
- ⭐ **자동 형 변환**: 컴파일러가 Type Erasure 과정에서 타입 안정성을 위해 `checkcast` 바이트코드 명령어를 자동으로 삽입한다는 점을 숙지해야 합니다.

---

## Slide 49

### 핵심 개념
- **Type Erasure (타입 소거)**: Java 제네릭에서 컴파일 타임에 타입 체크를 마친 후, 런타임에는 제네릭 타입 정보($<E>$, $<Integer>$ 등)를 제거하는 메커니즘입니다.
- **Runtime Type Identification (RTTI) 제약**: 타입 소거로 인해 실행 시점에는 객체가 어떤 구체적인 제네릭 타입으로 생성되었는지 알 수 없습니다. 따라서 `instanceof` 연산자를 구체적인 타입 파라미터(Parameterized type)와 함께 사용할 수 없습니다.

### 코드/수식 해설
```java
public static <E> void rtti(List<E> list) {
    // 오류: 런타임에는 list가 ArrayList<Integer>인지 ArrayList<String>인지 구분 불가
    if (list instanceof ArrayList<Integer>) // compile-time error
    
    // 허용: Unbounded wildcard(?)는 타입 정보에 의존하지 않으므로 사용 가능
    if (list instanceof ArrayList<?>) // OK
}
```
- `instanceof ArrayList<Integer>`: 런타임에 $<Integer>$ 정보가 사라지기 때문에 컴파일러가 이 검사를 허용하지 않습니다.
- `instanceof ArrayList<?>`: 단순히 `list`가 `ArrayList`의 인스턴스인지만 확인하는 것이므로 런타임에 안전하게 실행 가능합니다.

### 구체적 예시
- 만약 $List<String>$ 객체를 넘기더라도, 런타임에는 둘 다 $List$라는 로우 타입(Raw type)으로만 인식됩니다.
- 이로 인해 `instanceof`를 통한 구체적인 타입 비교는 논리적으로 불가능해집니다.

### 시험 포인트
- ⭐ **Type Erasure의 결과**: 제네릭 타입 정보는 런타임에 존재하지 않으므로 `instanceof List<String>`과 같은 코드는 컴파일 에러가 발생함을 반드시 숙지하세요.
- ⭐ **Wildcard 활용**: `instanceof`와 함께 제네릭 타입을 쓰고 싶다면, 반드시 `ArrayList<?>`와 같이 **Unbounded wildcard** 형태를 사용해야 합니다.
- ⭐ **Reifiable Type**: 런타임에 정보를 유지하는 타입을 Reifiable 타입이라 하며, 제네릭 타입 파라미터가 포함된 타입은 대부분 Non-reifiable 타입이기에 `instanceof` 제약을 받습니다.

---

## Slide 50

### 핵심 개념
- **타입 소거(Type Erasure)의 결과**: Java 제네릭은 컴파일 타임에만 타입 정보를 사용하고 런타임에는 이를 제거합니다. 이로 인해 런타임 시점에 객체가 정확히 어떤 파라미터화된 타입(Parameterized Type)인지 확인할 수 없습니다.
- **캐스팅 제한**: 실질적인 타입 정보가 사라지기 때문에, 비한정 와일드카드(`?`)를 제외하고는 구체적인 제네릭 타입으로의 형 변환이 제한되거나 경고를 발생시킵니다.

### 코드/수식 해설
```java
Box<Integer> box1 = new Box<>();
Box<Number> box2 = (Box<Number>) box1;  // compile-time error
Box<?> box3 = box1;                      // OK
```
- `Box<Integer>`를 `Box<Number>`로 캐스팅하는 것은 불가능합니다. Java의 제네릭은 **무공변성(Invariant)**을 가지기 때문에 $Integer$가 $Number$의 하위 타입이라 하더라도 `Box<Integer>`는 `Box<Number>`의 하위 타입이 아닙니다.
- `Box<?>`는 모든 제네릭 타입의 상위 타입으로 간주되므로 캐스팅이 허용됩니다.

```java
Box<Number> box4 = (Box<Number>) box3;  // Compiles, but unsafe (Unchecked warning)
```
- `Box<?>` 타입을 구체적인 `Box<Number>`로 캐스팅할 때는 컴파일러가 **Unchecked Warning**을 발생시킵니다. 런타임에는 타입 소거로 인해 `box3` 내부의 실제 타입이 $Number$인지 확인할 방법이 없기 때문입니다.

### 구체적 예시
- **런타임 ClassCastException 발생 원인**:
  - 만약 `box3`가 실제로는 `Box<String>` 객체를 참조하고 있다면, 이를 `Box<Number>`로 강제 캐스팅한 후 `box4.get()`을 통해 데이터를 꺼내려 할 때 런타임에 `ClassCastException`이 발생합니다.
  - 타입 소거 때문에 런타임의 `box3`은 그저 `Box`일 뿐이며, 컴파일러는 캐스팅 시점에 실제 내부 원소의 타입을 검증할 수 없습니다.

### 시험 포인트
- ⭐ **제네릭의 무공변성(Invariant)**: `Box<Integer>`를 `Box<Number>`에 대입하거나 캐스팅할 수 없는 이유를 서술할 수 있어야 합니다.
- ⭐ **Unchecked Warning**: 타입 소거로 인해 런타임에 타입 안전성(Type Safety)을 완벽히 보장할 수 없을 때 컴파일러가 주는 경고의 의미를 이해해야 합니다.
- ⭐ **와일드카드(`?`)의 특권**: 비한정 와일드카드는 유일하게 런타임에 안전하게 캐스팅이 허용되는 파라미터화된 타입임을 기억하세요.

---

## Slide 51

## Consequence of Type Erasure (3)

### **핵심 개념**
*   **제네릭 타입 인스턴스화 불가**: Type Erasure(타입 소거)로 인해 런타임 시점에는 타입 매개변수 $T$에 대한 구체적인 정보가 사라집니다.
*   따라서 컴파일러는 $T$가 어떤 생성자를 가지고 있는지, 혹은 구체적으로 어떤 타입인지 알 수 없기 때문에 `new T()`와 같이 직접적으로 인스턴스를 생성하는 것을 허용하지 않습니다.

### **코드/수식 해설**
```java
public class SomeClass<T> {
    private T t;

    public SomeClass() {
        // Compile-time error 발생
        this.t = new T(); 
    }
}
```
*   위 코드에서 `new T()`는 컴파일 오류를 유발합니다.
*   **원인**: 자바(또는 유사한 제네릭 모델)의 경우, 컴파일 단계에서 $T$는 해당 타입의 상한선(Bounded Type)인 `Object` 등으로 치환(Erasure)됩니다. 런타임에는 $T$가 무엇인지 알 수 없으므로 실제 객체를 메모리에 할당할 수 없습니다.

### **구체적 예시**
만약 `SomeClass<String>`과 `SomeClass<Integer>`가 있다면, Type Erasure 이후 두 클래스는 모두 런타임에 동일한 `SomeClass` 로 취급됩니다. 런타임 엔진 입장에서는 `new T()`를 만났을 때 이것이 `new String()`을 의미하는지 `new Integer()`를 의미하는지 결정할 수 없습니다.

### **시험 포인트**
*   ⭐ **Type Erasure의 제약 사항**: 제네릭 타입 매개변수 $T$를 사용하여 객체를 직접 생성(`new T()`)하는 것은 불가능하다는 점을 반드시 기억해야 합니다.
*   ⭐ **이유**: 런타임에 타입 정보가 소거되어 $T$의 실체를 알 수 없기 때문입니다.
*   ⭐ **해결책**: 이를 해결하기 위해 보통 `Class<T>` 객체를 인자로 전달받아 Reflection을 사용하거나, Factory 패턴 등을 활용합니다. (이 슬라이드 범위를 넘어서는 내용이나 참고용)

---

## Slide 52

## Creating Instance of Parameterized Types

### **핵심 개념**
- **직접 생성 지양**: 클래스 내부에서 매개변수화된 타입 $T$의 인스턴스를 직접 생성(`new T()`)하는 것은 설계상 유연성을 떨어뜨리므로 꼭 필요한 경우가 아니면 피해야 합니다.
- **제어의 역전 (IoC)**: 클라이언트가 인스턴스를 직접 제공하거나, 인스턴스 생성 로직을 담은 객체를 전달하도록 설계합니다.
- **간접 생성 (Factory Method)**: $T$ 타입의 객체를 생성하는 방법을 추상화한 인터페이스(예: `Supplier<T>`)를 사용하여 간접적으로 객체를 생성합니다.

### **코드/수식 해설**
슬라이드에 제시된 구조는 객체 생성의 책임을 외부로 위임하는 패턴을 보여줍니다.

```java
// 객체 생성을 담당하는 함수형 인터페이스
public interface Supplier<T> {
    T get();
}

// 매개변수화된 타입을 사용하는 클래스
public class SomeClass<T> {
    ...
    // 생성자에서 Supplier를 받아 객체를 초기화
    public SomeClass(Supplier<T> supp) {
        this.t = supp.get(); // Supplier의 get()을 호출하여 T 타입 인스턴스 획득
    }
}
```

- $T$: 타입 매개변수 (Parameterized Type)
- $Supplier<T>$: $T$ 타입의 객체를 공급(Supply)하는 역할을 정의한 인터페이스
- $supp.get()$: 실제 어떤 구체 클래스가 생성될지는 $Supplier$의 구현체에 따라 달라짐

### **구체적 예시**
- 만약 $T$가 `Circle` 클래스라면, 클라이언트는 `() -> new Circle()`과 같은 람다식이나 `CircleFactory` 클래스를 `Supplier<Circle>`로서 전달할 수 있습니다. 
- 이를 통해 `SomeClass`는 $T$가 구체적으로 무엇인지, 어떻게 생성되는지 몰라도 $T$ 타입의 객체를 안전하게 다룰 수 있습니다.

### **시험 포인트**
- ⭐ **직접 생성의 문제점**: 많은 객체지향 언어(Java 등)에서 `new T()`는 타입 소거(Type Erasure) 등의 이유로 컴파일 에러가 발생하거나, C++에서도 템플릿 인자의 기본 생성자 존재 여부에 의존하게 되어 결합도가 높아집니다.
- ⭐ **Factory/Supplier 패턴의 장점**: 객체 생성 로직과 사용 로직을 분리하여 코드의 재사용성과 테스트 용이성을 높입니다.
- ⭐ **Subclass의 역할**: $Supplier<T>$를 상속받은 하위 클래스가 실제 인스턴스 생성 방법(How to create)을 정의한다는 점을 이해해야 합니다.

---

## Slide 53

### 핵심 개념
- **제네릭 배열 생성 불가**: Java에서는 `List<String>[]`과 같은 파라미터화된 타입(parameterized type)의 배열 생성을 금지합니다.
- **런타임 타입 체크의 한계**: 배열은 공변성(Covariance)을 가지며 런타임에 자신의 원소 타입을 확인하지만, 제네릭은 **타입 소거(Type Erasure)**로 인해 런타임에 타입 정보가 사라집니다. 만약 제네릭 배열 생성을 허용한다면, 런타임에 타입 안정성을 보장할 수 없게 됩니다.

### 코드/수식 해설
```java
// 1. 컴파일 에러 발생
Object[] strLists = new List<String>[2]; // compile-time error
```
*   제네릭 배열 생성을 시도하면 컴파일러가 이를 사전에 차단합니다.

```java
// 2. 만약 생성이 허용된다면 발생할 문제 (가정)
strLists[0] = new ArrayList<String>();  // OK
strLists[1] = new ArrayList<Integer>(); // 런타임 에러 발생 불가 (ArrayStoreException 미발생)
```
*   `Type Erasure`로 인해 런타임 시 `ArrayList<String>`과 `ArrayList<Integer>`는 모두 동일한 `ArrayList`로 취급됩니다. 
*   따라서 배열의 특징인 `ArrayStoreException`(잘못된 타입 저장 시 발생)을 던질 수 없게 되어 타입 안정성이 깨집니다.

```java
// 3. 권장되는 대안: 제네릭 컬렉션 사용
List<List<String>> list = new ArrayList<>();
list.add(new ArrayList<String>());
```
*   배열 대신 제네릭 컬렉션을 중첩하여 사용하면 컴파일 타임에 모든 타입 체크가 이루어지므로 안전합니다.

### 구체적 예시
배열은 런타임에 `String[]` 배열에 `Integer`를 넣으려고 하면 에러를 발생시키지만, `List<String>[]`이 가능하다면 런타임에는 단지 `List[]`로 보이기 때문에 `List<Integer>`가 들어오는 것을 막지 못합니다. 이로 인해 나중에 데이터를 꺼낼 때 원치 않는 `ClassCastException`이 발생할 위험이 있습니다.

### 시험 포인트
- ⭐ **Type Erasure와 배열의 관계**: 왜 제네릭 배열 생성이 금지되는지 그 이유(런타임 타입 정보의 부재)를 서술할 수 있어야 합니다.
- ⭐ **타입 안정성(Type Safety)**: 제네릭 배열을 허용했을 때 발생할 수 있는 잠재적 위험(런타임에 타입 불일치를 감지하지 못함)을 이해해야 합니다.
- ⭐ **대안 제시**: 배열 대신 `List<List<T>>`와 같은 구조를 사용하는 것이 왜 더 안전한지 파악해야 합니다.

---
