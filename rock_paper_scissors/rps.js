function rock_paper_scissors(n) {
  rps_list = [['rock'], ['paper'], ['scissors']];

  if (n == 0) {
    return [[]];
  }

  if (n == 1) {
    return list;
  }

  combo = [];

  for (let i = 0; i < 3 ** n; i++) {
    if (i < Math.ceil(0.3333 * 3 ** n)) {
      combo.push(rps_list[0]);
    } else if (i < Math.ceil(0.6666 * 3 ** n)) {
      combo.push(rps_list[1]);
    } else {
      combo.push(rps_list[2]);
    }
  }

  while (combo[0].length !== n)
    for (let i = 0; i < 3 ** n; i++) {
      combo[i] = [...combo[i], ...rps_list[i % 3]];
    }

  //   combo[0] += rps_list[0];
  return combo;
}

console.log(rock_paper_scissors(3));
