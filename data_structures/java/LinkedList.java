public class LinkedList {
    public Node head;
    public Node tail;

    public LinkedList() {
        this.head = null;
        this.tail = null;
    }

    public LinkedList(Node h) {
        this.head = h;
        this.tail = null;
    }

    public LinkedList(Node h, Node t) {
        this.head = h;
        this.tail = t;
    }

    public void setHead(Node h) {
        this.head = h;
    }

    public Node getHead() {
        return this.head;
    }

    public void setTail(Node t) {
        this.tail = t;
    }

    public Node getTail() {
        return this.tail;
    }

    public void addToHead(int data) {
        Node node = new Node(data, null, this.getHead());

        if (this.getHead() != null) {
            this.getHead().setPrev(node);
        }

        this.setHead(node);

        if (this.getTail() == null) {
            this.setTail(this.getHead());
        }
    }

    public void addToTail(int data) {
        if (this.getTail() != null) {
            Node node = new Node(data, this.getTail(), null);
            this.getTail().setNext(node);
            this.setTail(node);
        } else {
            this.addToHead(data);
        }
    }

    public int removeFromHead() {
        Node temp = this.getHead();

        this.setHead(this.getHead().getNext());

        if (this.getHead() != null) {
            this.getHead().setPrev(null);
        } else {
            this.setTail(null);
        }

        return temp.getData();
    }

    public int removeFromTail() {
        Node temp = this.getTail();

        if (this.getTail() != null) {
            this.setTail(this.getTail().getPrev());
            this.getTail().setNext(null);
        } else {
            this.getHead().setNext(null);
        }
        return temp.getData();
    }

    public void printList() {
        Node temp = this.getHead();

        while (temp != null) {
            System.out.println(temp.getData());
            temp = temp.getNext();
        }
    }
}
