let LinkedList = require("./LinkedList");

function main() {
  let myList = new LinkedList();

  myList.head.setData(1);

  myList.addToHead(0);
  myList.addToTail(2);

  console.log("Before Reverse");
  myList.print();

  myList.reverseList();

  console.log("After Reverse");
  myList.print();
}

main();
