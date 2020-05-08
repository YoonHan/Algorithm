function solution(n, t, m, p) {
  var answer = "";
  let sequence = "";
  let number = 0;
  let round = 1;
  while (round <= t) {
    sequence += number.toString(n).toUpperCase();
    const totalLength = sequence.length;
    if (round * m < totalLength) {
      answer += sequence[(round - 1) * m - 1 + p];
      round += 1;
    }
    number += 1;
  }
  return answer;
}
