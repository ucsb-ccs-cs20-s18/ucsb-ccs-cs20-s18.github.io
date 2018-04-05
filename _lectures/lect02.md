---
num: "Lecture 1"
desc: "Orientation to the course"
ready: false
date: 2017-04-03 12:30:00.00-7:00
---

# First hour: [lab00](/labs/lab00/): Hello World, Submitting on Gradescope

We'll go work through the steps of submitting the Hello, World program on Gradescope.

# Then: [lab00](/labs/lab01/): Writing and testing functions



# Python Dictionaries

In Python, we can use a *dictionary* to associate keys with values.

This code creates a simple dictionary called `en_to_es` (short for "English to Español), that
maps the words `one`, `two` and `three` (as Python strings) to their Spanish counterparts (as
Python strings):

```python
en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
```

Once you create a dictionary, you can access the values by looking up their key.
Here, we show trying some Python dictionary code at the interactive Python shell:

```python
>>> en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
>>> en_to_es['one']
'uno'
>>> en_to_es['three']
'tres'
>>> 
```


