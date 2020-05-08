function solution(n) {
  var answer = "";
  let digits = [1, 2, 4];

  let count = 1;
  while (true) {
    if (n - Math.pow(3, count) >= 0) {
      n -= Math.pow(3, count);
      count += 1;
    } else {
      break;
    }
  }

  if (n == 0) {
    answer = "4".repeat(count - 1);
  } else {
    let number = "";
    while (count > 0) {
      const quo = parseInt((n - 1) / Math.pow(3, count - 1));
      number += digits[quo % 3];
      count -= 1;
    }
    answer = number;
  }

  return answer;
}
