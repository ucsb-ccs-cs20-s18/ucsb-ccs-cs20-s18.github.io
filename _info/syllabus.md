---
title: "Syllabus, CMPTGCS 20, Spring 2018"
layout: handout
ready: true
---

Basic Facts
-----------

* **Course Web Site**: <http://ucsb-ccs-cs20-s18.github.io>
* **Instructor**:  [Phill Conrad](http://www.cs.ucsb.edu/~pconrad)
   * Email is pconrad@cs.ucsb.edu, BUT please use Piazza for course related communication.
* **Course Meets**: TR 12:30pm-2:20pm
* Office Hours: See: <http://www.cs.ucsb.edu/~pconrad/ofchrs>  

This course is a CCS version of the College of Engineering course CMPSC 8.  Here is the description of that course:

<div style="background-color:#eee; border: 8px inset #333; font-size:90%; margin:1em; width:45em; padding: 0.5em;" markdown="1">


Introduction to computer program development for students with little to no programming experience. Basic programming concepts, variables and expressions, data and control structures, algorithms, debugging, program design, and documentation.

</div>

## What this course is about 

This course is an introduction to Computer Science, and programming. 

Computer Science is the study of <strong>abstractions </strong>and <strong>algorithms</strong>. 

* In Computer Science, an <strong>abstraction</strong> is a useful representation of something from the real world that allows us to work with it more easily or efficiently.

* An <strong>algorithm</strong> is a well-defined, step-by-step sequence of instructions that can be used to mechanically determine the solution to some well-defined problem.

You probably use <strong>abstractions</strong> and <strong>algorithms</strong> every day—for example:

* If you pick up any textbook, you'll probably find an index in the back of the book. The index is an <strong>abstraction</strong>—whether the book is about biology, modern art, political science, or computers, the &quot;way the index works&quot; is the always the same. It is composed of the same pieces (topics and page numbers), and organized in the same way (alphabetically by topic, then lists of page numbers in numerical order from smallest to largest.)

* If you are looking in the index of a U.S. history textbook for &quot;Gettysburg&quot; you'll probably use an <strong>algorithm</strong> to find the entry quickly. Here the input to the algorithm is some topic, and the output is a list of pages on which that topic appears.

* If you are looking for a parking lot on campus, you might use an <strong>abstraction</strong> called a &quot;map&quot; to locate the parking lot. You know the features of a map, and how it corresponds to the reality of a college campus, and parking spaces. The way a map can work to help you find a parking lot (or garage) is the same whether it's a map of UCSB, Downtown Santa Barbara, or the Staples Center in LA.

* If you are searching through a parking lot (or garage) to either (a) find a parking space, or (b) determine that there are no spaces left, you probably use an <strong>algorithm</strong> to do that—again, without even thinking about what you are doing.


## Algorithms have to be both designed, and &quot;coded&quot; so the computer can carry them out 

In the case of using an index, this is probably an algorithm you may have learned in grade school, and it has been so long since you learned it, that now you don't even think about it—you just do it. Finding a space in a parking lot—and knowing when to give up and look elsewhere—is &quot;just common sense&quot;; this probably isn't something you were ever &quot;taught&quot;, or even have to think very much about. You just do it.

Computers don't currently have this capability—i.e. the capability to &quot;pick up things by common sense&quot;—and it seems unlikely that they  will within our lifetime—unless there are major breakthroughs in the field of Artificial Intelligence. Such breakthroughs have been predicted for a while, but they haven't happened yet. (Maybe you'll be the one to figure out how to achieve this!)

So, for the time being at least, it falls to humans to design algorithms that computers can use to solve problems. In many cases, these algorithms are &quot;just common sense&quot;—the computer equivalent of looking for an empty parking space in a parking lot (and knowing when to give up). Algorithms like this are easy to design. Many of the algorithms we'll see in this course are like that.

In other cases, the algorithms are very complex, or very subtle, and coming up with them is a deep intellectual challenge. Furthermore, the impact of a better algorithm on society can be very large. For example, new algorithms in the field of computational science—modeling chemical and biological reactions with computer simulations—can lead to breakthroughs such as new drugs to fight disease, or renewable sources of energy.

And often, what goes along with finding a good algorithm is finding a good abstraction of the real world concepts we are interested in: cells, molecules, oil fields, words, sentences, students, courses, GPAs, etc. Algorithms and abstractions really go hand-in-hand.

## Coding, or Writing Software, or Programming

Coding is expressing algorithms in a programming language.

Human languages such as English and Spanish are not very well suited for expressing algorithms—at least not for expressing them to a computer (they have their problems for communicating with humans too!). So, special languages are used. In this course, we'll learn the Python programming language. We choose Python rather than Java or C++ because:

* If you are learning your first programming language, Python is easier to learn than the others
* Learning Python provides a good foundation for learning C, C++ or Java
* If you only learn one programming language, Python is a good choice—in spite of being easy to learn, it is not a &quot;toy&quot; language by any means. It is widely used by scientists and web application developers just for starters. Many internal systems at Google are based on Python code.
 
This course provides you with the opportunity to become a pretty good beginning programmer, and be well prepared for an intermediate programming course such as CS16 (the first course that counts towards the CS major at UCSB, and which requires at least one quarter of prior programming experience.)

I say that the course &quot;provides an opportunity,&quot; because you will only become a good beginning-level programmer if <strong>you</strong> put a lot of time and effort into this course—that is true no matter how much thought and attention I put in my lectures, assignments, and exams

## The swimming/guitar/painting analogy

You cannot learn to swim, play guitar, or paint from a textbook or a lecture. You can only:

* learn  to swim by spending many hours in the pool
* learn to play guitar by spending many hours playing the instrument
* learn to paint by spending many hours putting brush to canvas

The same is true of programming. Programming is not a series of facts to be memorized—you cannot &quot;cram&quot; for a computer science exam. You must practice, practice, practice.

<div style="page-break-before:always;">
&nbsp;
</div>

# What you need to learn to become <br />a skilled beginning level programmer


So, what is it that you need to know to be a skilled beginning-level programmer in Python? Here's the  list of what you'll need to be ready for CMPSC&nbsp;16 (aka CS16, the next programming course):

<table border="1" cellspacing="1" cellpadding="1" id="topicTable">
  <tr>
    <td><ul class="style11">
      <li>Problem solving
        <ul>
            <li>breaking down a problem into a sequence of steps</li>
          <li>abstracting specific problems into general ones<br />
            and finding general solutions</li>
        </ul>
      </li>
      <li>Memory concepts
        <ul>
            <li>variables, primitive vs. reference variables, name, type, value</li>
          <li>assignment statements</li>
          <li>scope of variables</li>
        </ul>
      </li>
      <li>Control structures
        <ul>
            <li>for loops, if/else, while loops</li>
        </ul>
      </li>
      <li>Lists in Python (similar to arrays in other languages)
        <ul>
            <li>index vs. value, finding sum, min, max, average, count of elements matching some condition, making a new list of elements containing only those that match some condition</li>
        </ul>
      </li>
    </ul>    </td>
    <td><ul class="style11">
      <li>Functions
        <ul>
            <li>function call vs. function definition</li>
          <li>formal vs. actual parameters (arguments)</li>
        </ul>
      </li>
      <li>Testing
        <ul>
            <li>How to test your code</li>
        </ul>
      </li>
      <li>Input/output concepts
        <ul>
            <li>Writing to the terminal</li>
          <li>Reading from the keyboard</li>
          <li>Reading and writing to files</li>
          <li>Neatly formatting output</li>
        </ul>
      </li>
      <li>Program style
        <ul>
            <li>How to write code that other people can read and understand</li>
        </ul>
      </li>
    </ul>    </td>
  </tr>
</table>



Final Course Units
==================

To learning Computer Science and Python Programming, you need to *do* CS and Programming.

I will be offering opportunity to build learning and demonstrate learning throughout the quarter, in the form of

* programming assignments (labs) borrowed from CMPSC 8 (which I'm also teaching this quarter)
* supplemental assignments (formal and informal)

To earn full course units (4), you need to demonstrate your mastery of the learning objectives by succesfully completing all (or the the vast majority) of at least the programming assignments.

Fewer than 4 units may be awarded for students that have spotty attendance, or fail to complete 

Completion of the homework assignents is optional&mdash;if you find it helpful, please do them. If they are busy work to you, then skip them.

Extra units may be awarded (5 or 6) for completing all course requirements, and going above and beyond those through independent work.

Accommodations for disabilities
-------------------------------

Students with disabilities may request academic accommodations for exams online through the UCSB Disabled Students Program at http://dsp.sa.ucsb.edu/. Please make your requests for exam accommodations through the online system as early in the quarter as possible to ensure proper arrangement.

Managing stress
---------------

Personal concerns such as stress, anxiety, relationships, depression, cultural differences, can interfere with the ability of students to succeed and thrive. For helpful resources, please contact UCSB Counseling & Psychological Services (CAPS) at 805-893-4411 or visit <http://caps.sa.ucsb.edu/> .

Responsible scholarship
-----------------------

Honesty and integrity in all academic work is essential for a valuable educational experience.  The Office of Judicial Affairs has policies, tips, and resources for proper citation use, recognizing actions considered to be cheating or other forms of academic theft, and students’ responsibilities, available on their website at: http://judicialaffairs.sa.ucsb.edu.  Students are responsible for educating themselves on the policies and to abide by them.

Furthermore, for general academic support, students are encouraged to visit Campus Learning Assistance Services (CLAS) early and often. CLAS offers instructional groups, drop-in tutoring, writing and ESL services, skills workshops and one-on-one consultations. CLAS is located on the third floor of the Student Resource Building, or visit http://clas.sa.ucsb.edu


<div markdown="1">

![Python cartoon](https://foo.cs.ucsb.edu/8wiki/LocalImages/python.jpg)

(Image credit: Randall Munro http://xkcd.com/353/)

Standard Disclaimer
-------------------

This syllabus is as accurate as possible, but is subject to change at
the instructor's discretion, within the bounds of UC policy.

(end of syllabus)

</div>


