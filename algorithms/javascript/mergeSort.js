// import { testArr } from "./testData";
const testArr = require("./testData");

// recursive function
// return a sorted array
const mergeSort = (arr) => {
  if (arr.length > 1) {
    let middle = Math.floor(arr.length / 2);

    let leftArr = [];
    for (let i = 0; i < middle; i++) {
      leftArr.push(arr[i]);
    }
    // console.log(leftArr);

    let rightArr = [];
    for (let i = arr.length - 1; i >= middle; i--) {
      rightArr.push(arr[i]);
    }
    // console.log(rightArr);

    // recursively call mergeSort to break down each array
    // until only 1 element remains
    leftArr = mergeSort(leftArr);
    rightArr = mergeSort(rightArr);

    return merge(leftArr, rightArr);
  }
  return arr;
};

const merge = (arrA, arrB) => {
  let arrC = [];

  // while both arrays still have elements
  while (arrA.length && arrB.length) {
    if (arrA[0] > arrB[0]) {
      arrC.push(arrB.shift());
    } else {
      arrC.push(arrA.shift());
    }
  }

  return [...arrC, ...arrA, ...arrB];
};

console.log(testArr);
console.log(mergeSort(testArr));
