**Stack**
Stack is a linear data structure which follows LIFO(last-in-first-out) principle to organize ans use data.
**Basic operations of stack are following:**
1. Push: add an element on the top index of the stack.
2. Pop: remove the topmost item of the stack.
3. isEmpty: check either the stack is empty.
4. isFull: check either the stack is full to its capacity.
5. Peek: get the topmost element of the stack without removing from the stack.
**Working of Stack operations:**
+ a pointer "top" is maintained to track the top index of the stack.
+ stack is initialized with value of top equal to -1.
+ before pushing an element isFull is checked then increase the value of top and place the new element on the position pointing by top.
+ before poping the top element isEmpty is checked then return the element and decrese the value of top.
**Implementaion**
The stack is implemented using Python, there are some points to focus when python implementation is used:
+ the "top" pointer is not needed to be maintained
+ isFull() function not required to be created as the list or array in python are dynamically increase their size.
