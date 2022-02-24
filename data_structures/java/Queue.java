// implementation of a queue class using a LinkedList under the hood

public class Queue {
    public LinkedList queue;

    public Queue() {
        this.queue = new LinkedList();
    }

    // adds an item to the end of the queue
    public void enqueue(int item) {
        this.queue.addToTail(item);
    }

    // removes an item from the front of the queue
    public int dequeue() {
        return this.queue.removeFromHead();
    }

    // returns the item's value from the front of the queue
    public int peek() {
        return this.queue.getHead().getData();
    }

    public boolean isEmpty() {
        return this.queue.getHead() == null;
    }

    public void print() {
        this.queue.printList();
    }



}
