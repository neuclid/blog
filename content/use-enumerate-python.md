Title: Use enumerate() in python instead of your boring for loops
Date: 2017-12-28
Category: Programming
Tags: python, code

This is going to be a short one.
For many tasks, we iterate using `for` loops of this sort:

```python
#Example: Getting odd numbers out of a list
some_list = [x for x in range(5,20)]

#Boring
for i in range(len(some_list)):
    value = some_list[i]
    if value%2 != 0:
    print value

# Neat!
for i,value in enumerate(some_list):
    if value%2 != 0:
    print value

```
Basically, `enumerate()` returns an iterator with the tuple of `(index,item)`

**Bonus tip**: if for some reason you don't like to count from zero, you can add an offset using `enumerate(list,offset)`.

As an example, I haven't seen aisles numbered 0 anywhere, so:
```python
grocery_store =['apples','mangoes','oranges', 'guavas']
for i, fruit in enumerate(grocery_store,1):
    print "We have {} at Aisle #{}".format(fruit,i)
```
To which you have the following sensible output:
```
We have apples at Aisle #1
We have mangoes at Aisle #2
We have oranges at Aisle #3
We have guavas at Aisle #4
```
Start using it already!