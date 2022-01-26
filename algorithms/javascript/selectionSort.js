// iterates through data, starting at the first position and moving up positions on each iteration
// locates the smallest element and saves its position in a variable
// once it reaches the end it swaps the smallest variables value with its current position

const testArr = require("./testData");

const selectionSort = (arr) => {
  let size = arr.length;

  for (let i = 0; i < size - 1; i++) {
    minValuePos = i;

    for (let j = i + 1; j < size; j++) {
      if (arr[j] < arr[minValuePos]) minValuePos = j;
    }

    let temp = arr[minValuePos];
  }
  console.log(arr);
};

const swap = ([a, b]) => [b, a];

// console.log(selectionSort(testArr));
console.log(swap(5, 2));
