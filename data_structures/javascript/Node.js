module.exports = class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }

  getNext() {
    return this.next;
  }

  getData() {
    return this.data;
  }

  setNext(node) {
    this.next = node;
  }

  setData(data) {
    this.data = data;
  }
};
