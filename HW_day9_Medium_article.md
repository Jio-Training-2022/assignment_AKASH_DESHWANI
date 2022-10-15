Python Tuples and Lists : A Beginner's Guide

Python lists and tuples are two of the most commonly used data structures in Python. They are both used to store a collection of items. However, there are some key differences between them. In this article, we will discuss the differences between lists and tuples in Python.

Properties and Syntax: 

List = [item1, item2, item3, ...]
Lists are created using square brackets [] and tuples are created using parentheses ().
Lists are mutable, while tuples are immutable.
Lists are used to store a collection of items, while tuples are used to store a collection of items that are related to each other.

Properties and Syntax:
Tuple = (item1, item2, item3, ...)
Tuple are immutable, while lists are mutable.
Tuple are used to store a collection of items, while lists are used to store a collection of items that are related to each other.

example of a list: 
    
    ```python
    list = [1, 2, 3, 4, 5]
    ```

example of a tuple: 
    
    ```python
    tuple = (1, 2, 3, 4, 5)
    ```


Tuple do look like lists, but they are different. The main difference between lists and tuples is that lists are mutable, while tuples are immutable. This means that lists can be changed, while tuples cannot be changed.

Conversion funciton between lists and tuples:

All sequence type object are interchangable in python. This means that you can convert a list into a tuple and vice versa. This is done using the list() and tuple() functions.

list()	converts a tuple or string to list
tuple()	converts list or string to tuple
str()	returns string representation of list or tuple object


## When to use lists and tuples over each other:

Well it depends on what you want to do with the data. If you want to change the data, then you should use a list. If you want to keep the data the same, then you should use a tuple.

There may be some occasion you specifically dont want to change the data. 
For example, if you are using a tuple as a key in a dictionary, you cannot change the tuple. If you want to change the tuple, you will have to create a new tuple and change the key in the dictionary to the new tuple.

There should be one more section about the differences between lists and tuples. I will add it later.


Conclusion and Key takeaways:

In this short article, we have discussed the differences between lists and tuples in Python. We have also discussed when to use lists and tuples over each other.

- The key difference between lists and tuples is that lists are mutable, while tuples are immutable.
- Lists are created using square brackets [] and tuples are created using parentheses ().
- Lists are used to store a collection of items, while tuples are used to store a collection of items that are related to each other.