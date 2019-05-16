Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    O(1) because it is always going to insert the new
    node at the end, no matter how many items are in 
    the queue.

2. What is the runtime complexity of `dequeue`?
    O(1) because the node that will be removed is 
    always going to be in the same location, at the head,
    not matter how many items are in the queue. 

3. What is the runtime complexity of `len`?
    O(n) this would be effected by how many items are
    in the queue.

## Binary Search Tree

1. What is the runtime complexity of `insert`?
    Insert in a BST is a O(log n) runtime complexity.

2. What is the runtime complexity of `contains`?
    Contains would be an O(n) runtime complexity because
    it relies completely on how many nodes are in the BST
    because it will have to loop through all of them to find it.

3. What is the runtime complexity of `get_max`? 
    Similarly to the runtime of contains, get max would be a
    runtime complexity of O(n) because the runtime complexity
    would be reliant on how many nodes were in the BST.

## Heap

1. What is the runtime complexity of `_bubble_up`?
    O(log n) is the runtime complexity of bubble up because it's really just
    a simple swap function but it could increase by log n, depending on how many
    times it needs to swap.

2. What is the runtime complexity of `_sift_down`?
    O(log n) is the runtime complexity of sift down because it's really just
    a simple swap function, just like bubble up. However, it could increase by log n, 
    depending on how many times the node needs to swap.

3. What is the runtime complexity of `insert`?
    O(log n) because of the need for the insert function to use the
    bubble up function. The number of operations that must be completed
    on insert relies on how many times the newly inserted node has to
    "bubble up" the heap, therefore the runtime complexity is dependent on log n.

4. What is the runtime complexity of `delete`?
    This has the same runtime complexity of insert, O(log n) for the same reason.
    Because deletion requires the sift down function, which might have to run n
    times, depending on how many levels there are.

5. What is the runtime complexity of `get_max`?
    O(1) because the max in a max heap is always going to be located 
    at the same position [0] so it never has to loop or sort because it's
    location is a set constant.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
    This would be a runtime complexity of O(1) because the runtime
    is not effected by how many items are in the list. All that needs
    to happen, is for the item to be inserted and the pointer(s) changed.

2. What is the runtime complexity of `ListNode.insert_before`?
    Just like above, this would be a runtime complexity of O(1) because
    the runtime is not effected by how many items are in the list. 
    All that needs to happen, is for the item to be inserted and 
    the pointer(s) changed.

3. What is the runtime complexity of `ListNode.delete`?
    ListNode.delete would also be a O(1) runtime complexity because
    it would only have to change the pointer(s), it's runtime is not
    effected at all by how many items are in the list.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    O(1) because it is a simple insertion and the number of items in
    the list do not matter since it just goes right at the beginning.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    O(1) is the runtime complexity, because once again, we are only going 
    to perform the function on the item at the head and then change its
    pointer. The runtime is not effected by how many items are in the list.

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    O(1) is the runtime complexity, it does not matter how many items are in
    the list, you just assign the new tail and change pointer(s).

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    O(1) for the same reason the adding to the tail is O(1)--there is not
    a difference in the time complexity depending on the number of items in
    the list. All that has to happen for an item to be removed from the
    tail, is that pointers need to be altered.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    O(1), the quantity of items in the list have no effect on the 
    runtime complexity for this function.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    O(1), same as above. :)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    Deletion for a doubly linked list is a runtime complexity of O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
        Array.splice in JS is a O(n) runtime complexity, so it could get 
        slower depending on the number of items in the array. In general,
        the doubly linked list deletion would perform better.