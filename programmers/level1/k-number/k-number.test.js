const solution = (array, commands) => {
  return commands.reduce((answers, command) => {
    const [start, end, index] = command;
    const answer = findNumber(array, start, end, index);
    return [...answers, answer];
  }, [])
}

const findNumber = (array, start, end, index) => {
  return [...array]
    .slice(start - 1, end)
    .sort((a, b) => a - b)[index - 1];
}

test('solution', () => {
  expect(
    solution(
      [1,5,2,6,3,7,4], 
      [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    )
  ).toEqual([5, 6, 3]);
})

test('find number', () => {
  expect(findNumber([1, 5, 2, 6, 3, 7, 4], 2, 5, 3)).toBe(5);
  expect(findNumber([1, 5, 2, 6, 3, 7, 4], 4, 4, 1)).toBe(6);
  expect(findNumber([1, 5, 2, 6, 3, 7, 4], 1, 7, 3)).toBe(3);
})