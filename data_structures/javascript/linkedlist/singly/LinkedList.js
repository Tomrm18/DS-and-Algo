/*
Implementation of a Singly Linked List in JavaScript
*/

let Node = require("./Node");

module.exports = class LinkedList {
  constructor() {
    this.head = new Node();
    this.tail = null;
  }

  getHead() {
    return this.head;
  }

  setHead(headPtr) {
    this.head = headPtr;
  }

  getTail() {
    return this.tail;
  }

  setTail(tailPtr) {
    this.tail = tailPtr;
  }

  addToHead(data) {
    if (this.getHead() == null) {
      let newNode = new Node();
      newNode.setData(data);
      this.setHead(newNode);
    } else {
      let newNode = new Node(data);

      let tempNode = this.head;

      this.head = newNode;
      this.head.next = tempNode;
    }
  }

  addToTail(data) {
    if (this.getTail() == null) {
      this.addToHead(data);
    } else {
      let newNode = new Node(data);
      this.tail.setNext(newNode);
      this.setTail(newNode);
    }
  }

  removeFromHead() {
    let temp = this.getHead();

    this.setHead(this.getHead().getNext());

    if (this.getHead() == null) {
      this.tail = null;
    }
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

  // search the list for the data
  // if the data is there remove it
  // if not, do nothing
  remove(data) {
    let prev_pointer = this.getHead();
    let curr_pointer = this.getHead();

    while (curr_pointer != null) {
      // we have found the node
      if (curr_pointer.getData() == data) {
        // temp node is the head node
        if (curr_pointer == this.getHead()) {
          this.removeFromHead();
        }
        // temp node is the tail node
        else if (curr_pointer == this.tail) {
          this.removeFromTail();
        }
        // temp node is an inner node
        else {
          // now prev pointer will traverse the list to find currents previous node
          while (prev_pointer.getNext().getData() != curr_pointer.getData()) {
            prev_pointer = prev_pointer.getNext();
          }

          // now we unlink the target node
          prev_pointer.setNext(curr_pointer.getNext());
        }
      }
      // move the current pointer up one node each
      curr_pointer = curr_pointer.getNext();
    }
  }

  getSize() {
    let temp = this.getHead();
    let nodeCount = 0;

    while (temp != null) {
      nodeCount++;
      temp = temp.getNext();
    }

    return nodeCount;
  }

  // finds and replaces the first instance of replaceValue with newValue
  replace(replaceValue, newValue) {
    let temp = this.getHead();

    while (temp != null) {
      if (temp.getData() == replaceValue) {
        temp.setData(newValue);
        break;
      }
      temp = temp.getNext();
    }
  }

  // finds and replaces all instances of replaceValue with newValue
  replaceAll(replaceValue, newValue) {
    let temp = this.getHead();

    while (temp != null) {
      if (temp.getData() == replaceValue) {
        temp.setData(newValue);
      }
      temp = temp.getNext();
    }
  }

  reverseList() {
    let tempList = new LinkedList();
    let tempPointer = this.getHead();

    while (tempPointer != null) {
      tempList.addToHead(tempPointer.getData());
      tempPointer = tempPointer.getNext();
      this.removeFromHead();
    }

    tempPointer = tempList.getHead();

    while (tempPointer != null) {
      this.addToTail(tempPointer.getData());
      tempPointer = tempPointer.getNext();
    }
  }

  print() {
    let temp = this.getHead();

    while (temp != null) {
      console.log(temp);
      temp = temp.getNext();
    }
  }
};

// LinkedList.prototype.insertAtBeginning = function (data) {
//   let newNode = new Node(data);
// };
