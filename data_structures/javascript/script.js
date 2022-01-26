let LinkedList = require("./LinkedList");

function main() {
  let myList = new LinkedList();

  myList.head.setData(1);

  myList.addToHead(0);
  myList.addToTail(2);

  myList.print();
}

main();
