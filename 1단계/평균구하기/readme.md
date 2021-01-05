# 나의 방법
sum 변수에 값을 모두 집어넣고 더한 후 배열의 길이로 나누어 평균을 구했다
* * *
# 새로운 방법
**Arrays.stream** 메소드를 이용하는 방법이다.

* Arrays.stream(arr).average().orElse(0);

**스트림(Stream)** 이란 자바8부터 추가된 컬레션의 저장 요소를 하나씩 참조해서 람다식으로 처리할 수 있도록 해주는 반복자이다.

average()는 평균을 구하는 메소드, orElse(double other)는 average 값이 있으면 average를 반환하고, 없으면 other을 반환한다.

* Arrays.stream을 이용하면 코드는 간결해지지만 효율성이 기존 알고리즘에 비해 현저이 낮은 결과가 나타난다.
