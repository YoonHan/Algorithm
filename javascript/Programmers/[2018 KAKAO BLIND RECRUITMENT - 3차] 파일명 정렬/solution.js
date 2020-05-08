function solution(files) {
  var answer = [];
  let fileNames = [];

  const regexHead = /[a-zA-Z]+/;
  const regexNumber = /\d+/;
  for (let [idx, item] of files.entries()) {
    let fileName = {};
    const matchHead = item.match(regexHead);
    const matchNumber = item.match(regexNumber);
    let idxHead, idxNumber, head, number;
    (idxHead = matchHead.index), (idxNumber = matchNumber.index);
    (head = matchHead[0]), (number = matchNumber[0]);
    fileName["head"] = item.slice(0, idxNumber);
    fileName["number"] = item.slice(idxNumber, idxNumber + number.length);
    fileName["tail"] = item.slice(idxNumber + number.length);
    fileName["priority"] = idx;
    fileNames.push(fileName);
  }
  // 기준에 맞게 secondary sort
  fileNames.sort((a, b) => {
    if (a.head.toLowerCase() < b.head.toLowerCase()) return -1;
    else if (a.head.toLowerCase() === b.head.toLowerCase()) {
      if (parseInt(a.number) < parseInt(b.number)) return -1;
      else if (parseInt(a.number) === parseInt(b.number)) {
        if (a.priority < b.priority) return -1;
        else return 1;
      } else return 1;
    } else if (a.head.toLowerCase() > b.head.toLowerCase()) return 1;
  });
  // 분리된 파일명들을 원 상태로 복구
  for (let item of fileNames) {
    answer.push([item.head, item.number, item.tail].join(""));
  }
  return answer;
}
