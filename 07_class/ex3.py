# 3. 다형성 (Polymorphism)

# ===========================================================
#  1. 다형성이란?
#  - 같은 이름의 메소드를 호출해도, 객체의 종류에 따라 ( 서로 다르게. ) 동작하는 성질
#  - 전자제품의 "전원" 버튼 : TV, 에어컨, 세탁기에 있는 전원버튼은 같지만 실제 동작은 모두 다르다.
#  - 일반적으로 ( 상속 ) + ( 메소드 오버라이딩 )으로 다형성을 구현한다. (파이썬은 같은 이름의 메소드만 있으면 다형성 성립)
# ===========================================================

# 이미 우리가 쓰고 있던 다형성 기능
print(1 + 2)
print("1" + "2")
print([1] + [2])

# ===========================================================
#  2. 다형성 없이 구현한다면?
# ===========================================================


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self,name}: 멍멍")


class Cat:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self,name}: 야옹")


def make_sound(animal):
    if isinstance(animal, Dog):
        animal.bark()
    elif isinstance(animal, Cat):
        animal.meow()


# ===========================================================
#  3. 다형성 구현 (상속 + 오버라이딩)
# ===========================================================


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self,name}: ...")


class Dog(Animal):
    def speak(self):
        print(f"{self.name}: 멍멍")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 야옹")


class Cow(Animal):
    def speak(self):
        print(f"{self.name}: 음메")


# 새로운 클래스를 추가해도 make_sound2()는 그대로 사용 가능
# 확장에는 열려있고, 수정에는 닫혀있다.
def make_sound2(animal):
    animal.speak()


make_sound2(Dog("멍멍이"))
make_sound2(Cat("야옹이"))
make_sound2(Cow("얼룩이"))
# 자식 객체 리스트 생성
animals = [Dog("멍멍이"), Cat("야옹이"), Cow("얼룩이")]

for a in animals:
    a.speak()


# (참고) 덕 타이핑(Duck typing)
# - 파이썬은 함수 호출 시 객체의 타입을 검사하지 않음 (실행 시 메소드만 확인)
# - 따라서, 같은 이름의 메소드만 있으면 다형성을 구현할 수 있음
# - 파이썬에서는 상속이 다형성의 필수 조건은 아니지만 메소드가 없으면 에러가 나므로 주의!


class Duck:
    def speak(self):
        print("꽥꽥")


class Robot:
    def speak(self):
        print("삐리삑")


for x in [Duck(), Robot()]:
    x.speak()
# =========================================================
#  🔥 실습 문제 : 도형 넓이 계산
# =========================================================


# Shape 부모 클래스 작성하기
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0


# Rectangle 자식 클래스 작성하기
class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__("사각형")
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


# Circle 자식 클래스 작성하기
class Circle(Shape):
    def __init__(self, r):
        super().__init__("원")
        self.r = r

    def area(self):
        return (
            3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216
            * self.r
            * self.r
        )


# Triangle 자식 클래스 작성하기
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("삼각형")
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


# 3️⃣ 자식 객체 리스트 생성
shapes = [Rectangle(3, 4), Circle(5), Triangle(6, 3)]


# 4️⃣ 도형 넓이 출력 (반복문 사용)
total = 0

for shape in shapes:
    result = shape.area()
    print(f"{shape.name} 넓이: {result:g}cm²")
    total += result

print(f"전체 넓이: {total:g}cm²")
