# Advice
I know you aren't taking a programming class, but since you seem to be doing a bit of programming
I figured it might be helpful to put up some guidance on how to not make piles of shit code
that you will hate writing and I will hate reading and that will make kittens cry.


Guidelines:

1. Make your code readable. 
2. Don't repeat yourself (DRY). That mean's any code that is copy and pasted should be abstracted into
   a function.
3. Fewer lines is better, unless if interferes with #1.


One great resource in the [Python Guide on Code Style:](http://docs.python-guide.org/en/latest/writing/style/)

> If you ask Python programmers what they like most in Python, they will often say its high readability. Indeed, a high level of readability is at the heart of the design of the Python language, following the recognised fact that code is read much more often than it is written.

> One reason for Python code to be easily read and understood is its relatively complete set of Code Style guidelines and “Pythonic” idioms.

> Moreover, when a veteran Python developer (a Pythonista) points to portions of code and says they are not “Pythonic”, it usually means that these lines of code do not follow the common guidelines and fail to express the intent in what is considered the best (hear: most readable) way.

That is a great reference page to look back on. I am now gonna highlight some particular areas which
I think are important.

## Basic Formatting
Your code show be formatted to follow [PEP8](https://www.python.org/dev/peps/pep-0008/). The only one
that is variable is the max line size. While having too long lines can be sign that there is too
much complexity, it is also sometimes painful to break them.

If you wanna test and see if your code is following all the standards, you can
use [this online PEP8 checker](http://pep8online.com/).


## Variable Names
Some people say that choosing what to name things is the hardest part of writing a program.

Good names can help with **local readbility**. This means that each chunk of your code
should be able to stand by itself and be obvious what it means.

Write a program like you would a math proof. Each step should be obvious and explicit.

If you have good variable names, the code should speak for itself.

## Functions (... are your friends)

They are awesome because they isolate inputs and outputs of one part of your code. That
way you can reason about things in blocks. It allows your code to be composable and reusable.

For example, if you are generating the color you want to plot your points with based on the
velocity, create a function that takes in velocity and return the color.

```python
def doppler_shift(v):
    if v > 0:
        return (1, 0, 0)
    return (0, 0, 1)
    
points(src=[(1,1,1)], color=doppler_shift(-4))
```

So please, just write more functions. It is possible to make things too generic, by creating too much abstraction
but none of you have that problem. All the code I have seen has been basically one big block. Which is totally
fine for testing stuff out. But you will actually be able to increase your productivity if you start using
functions, as well as make it easier for others to follow what you are doing.


