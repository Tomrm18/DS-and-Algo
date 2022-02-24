public class Deque {
    public Queue queue;

    public Deque() {
        this.queue = new Queue();
    }

    public int first() {
        return this.queue.peek();
    }

    public int last() {
        return this.queue.queue.getTail().getData();
    }

    public void insertFirst(int item) {
        this.queue.queue.addToHead(item);
    }

    public void insertLast(int item) {
        this.queue.enqueue(item);
    }

    public int removeFirst() {
        return this.queue.dequeue();
    }

    public int removeLast() {
        return this.queue.queue.removeFromTail();
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public void print() {
        this.queue.print();
    }
}
