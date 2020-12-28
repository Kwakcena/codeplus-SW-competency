const solution = (array, commands) => {
  return commands.reduce((answers, command) => {
    const [start, end, number] = command;
    const answer = findNumber(sortArray(sliceArray(array, start, end)), number);
    return [...answers, answer];
  }, [])
}

const sliceArray = (array, start, end) => {
  return [...array].slice(start - 1, end);
}

const sortArray = (array) => {
  return [...array].sort((a, b) => a - b);
}

const findNumber = (array, index) => {
  return array[index - 1];
}

test('solution', () => {
  expect(
    solution(
      [1,5,2,6,3,7,4], 
      [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    )
  ).toEqual([5, 6, 3]);
})

test('slice array', () => {
  expect(sliceArray([1, 5, 2, 6, 3, 7, 4], 2, 5)).toEqual([5, 2, 6, 3]);
  expect(sliceArray([1, 5, 2, 6, 3, 7, 4], 4, 4)).toEqual([6]);
  expect(sliceArray([1, 5, 2, 6, 3, 7, 4], 1, 7)).toEqual([1, 5, 2, 6, 3, 7, 4]);
})

test('sort array', () => {
  expect(sortArray([5, 2, 6, 3])).toEqual([2, 3, 5, 6]);
  expect(sortArray([6])).toEqual([6]);
  expect(sortArray([1, 5, 2, 6, 3, 7, 4])).toEqual([1, 2, 3, 4, 5, 6, 7]);
})

test('find number', () => {
  expect(findNumber([2, 3, 5, 6], 3)).toBe(5);
  expect(findNumber([6], 1)).toBe(6);
  expect(findNumber([1, 2, 3, 4, 5, 6, 7], 3)).toBe(3);
})