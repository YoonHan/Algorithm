# 게리맨더링 2

## 핵심 포인트

- 각 경계선의 꼭지점 네 개를 구하는 건 쉬웠는데, 그 내부 영역을 표시하는 로직을 처음에 너무 복잡하게 구상해서 도중에 다른 방식으로 바꾸었다. 재현시의 각 행에서, 몇 열부터 몇 열까지가 5구역인지 매 행 반복마다 판단하도록 했다.