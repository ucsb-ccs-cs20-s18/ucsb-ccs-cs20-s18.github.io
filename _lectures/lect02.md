---
num: "Lecture 2"
desc: "Orientation to the course"
ready: false
date: 2017-04-05 12:30:00.00-7:00
---

# Earthquakes!

Source of data: <https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson>

# How to do pip install stuff on Mac and Windows

To install new packages, you use `pip3 install blah` where `blah` is the name of the package.

On Mac, e.g. to install `requests`

```
pip3 install requests
```

On Windows, here's the currently ugly version.  Maybe we can make this nicer.

This depends on you having already installed git for Windows.

1. Run menu, enter %appdata%
2. That takes you to the Windows File Explorer, where you can click through the following directories:
    ```
    Appdata/Local/Programs/Python/Python36/Scripts
    ```
3. Under Scripts, locate `pip3.exe`, right click, and choose "Git Bash Here"
4. That should open a terminal window, where you can type:
   ```
   ./pip3 install requests
   ```

# What we did with the Earthquakes

TODO Insert this later.

# Self Submission of Homework

You can scan your assignment to PDF from any iOS or Android device.

Instructions are available here: <http://www.cs.ucsb.edu/~pconrad/cs32/15F/pdf/GradescopeSubmissionHelp.pdf>

There are also PDF scanners available for Windows Phone&mdash;do a web search on "Windows Phone PDF Scanner".

# Scan your pages in the correct order!!!

The result should be a two page PDF, with page 1 first, and page 2 second.

You may be penalized if your submission has the pages in the incorrect order.

Your resulting PDF should be exactly won

# Alternative: editing the PDF (no scanning needed)

An alternative is to:
1. Get an electronic copy of the homework assignment from the website
2. Save to PDF (On Mac, you can "print to PDF", for example.)
3. Use software that edits/annotates PDFs to enter your answers directly.
4. Upload that PDF.


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


