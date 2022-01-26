/*
Implementation of a Singly Linked List in JavaScript
*/

let Node = require("./Node");

module.exports = class LinkedList {
  constructor() {
    this.head = new Node();
    this.tail = this.head;
  }

  getHead() {
    return this.head;
  }

  setHead(headPtr) {
    this.head = headPtr;
  }

  addToHead(data) {
    let newNode = new Node(data);

    let tempNode = this.head;

    this.head = newNode;
    this.head.next = tempNode;
  }

  addToTail(data) {
    let newNode = new Node(data);
    this.tail.setNext(newNode);
    this.tail = newNode;
  }

  removeFromHead() {
    this.head = this.head.getNext();
  }

  removeFromTail() {
    let temp = this.head;

    while (temp != null) {
      if ((temp.next = this.tail)) {
        temp.next = null;
      }

      temp = temp.next;
    }
  }

  print() {
    let temp = this.head;

    while (temp != null) {
      console.log(temp);
      temp = temp.getNext();
    }
  }
};

// LinkedList.prototype.insertAtBeginning = function (data) {
//   let newNode = new Node(data);
// };
