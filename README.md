# Text Grader
Text Grader determines the readability of a given text using Flesch-Kincaid readability tests and provides stats about the text.

***NOTE:** The web app is deployed on a free server which goes into sleep mode and takes about 10s for boot up, once loaded the bot will work as expected.* 

![Demo 2](/text-grader-demo2.gif)


## How it Works
When user inputs a text, backend performs to following.

**Test 1: The Flesch Reading Ease**

In the Flesch reading-ease test, higher scores indicate material that is easier to read; lower numbers mark passages that are more difficult to read.

Flesch reading-ease score (FRES):

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/bd4916e193d2f96fa3b74ee258aaa6fe242e110e)

**Test 2: The Flesch Grade Level**

This test presents a score as a U.S. grade level, making it easier for teachers, parents, librarians, and others to judge the readability level of various books and texts.

Flesch Grade Level test score:

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/8e68f5fc959d052d1123b85758065afecc4150c3)

Readability Tests on [Wikipedia link](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)
