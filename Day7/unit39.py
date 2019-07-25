# 이터레이터(iterator), 값을 차례대로 꺼낼 수 있는 객체(object)입니다.
# 리스트, 튜플, 딕셔너리, 세트
dir([1, 2, 3])
# 객체가 반복 가능한 객체인지 알아보는 방법은 객체에 __iter__ 메서드가 들어있는지 확인해보면 됩니다.
# 다음과 같이 dir 함수를 사용하면 객체의 메서드를 확인할 수 있습니다.
it = [1, 2, 3].__iter__()
it.__next__()
