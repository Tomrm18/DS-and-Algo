// Java implementation of a Node, with prev and next pointers

public class Node {
    public int data;
    public Node prev;
    public Node next;

    public Node() {
        this.data = 0;
        this.next = null;
    }

    public Node(int data) {
        this.data = data;
        this.prev = null;
        this.next= null;
    }

    public Node(int data, Node p) {
        this.data = data;
        this.prev= p;
        this.next = null;
    }

    public Node(int data, Node p, Node n) {
        this.data = data;
        this.prev= p;
        this.next = n;
    }

    public void setData(int data) {
        this.data = data;
    }

    public int getData() {
        return this.data;
    }

    public void setPrev(Node prev) {
        this.prev = prev;
    }

    public Node getPrev() {
        return this.prev;
    }

    public void setNext(Node next) {
        this.next = next;
    }

    public Node getNext() {
        return this.next;
    }
}
