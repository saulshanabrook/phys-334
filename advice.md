# Advice
I know you aren't taking a programming class, but since you seem to be doing a bit of programming
I figured it might be helpful to put up some guidance on how to not code
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


Another that is applicable is the [Google Python Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html)

## Basic Formatting

Your code show be formatted to follow [PEP8](https://www.python.org/dev/peps/pep-0008/).

If you wanna test and see if your code is following all the standards, you can
use [this online PEP8 checker](http://pep8online.com/).

Keeping your code properly formatted is like checking your paper for spelling/grammatical mistakes. I can still read your code if you format it badly, but it looks sloppy and unprofessional.

Also, it makes it harder to read if everyone's style is different. That is why python has PEP8, to standardize all coding styles.

### Comments
In Python, comments describing what a module (file) or function are called **docstrings**. They are written with triple quotes, like this:

```python
def doppler_shift(v):
    '''
    Given a velocity, computes the relative doppler shift
    and return as an RGB tuple.
    
    For a positive velocity it will be all red, and all blue for a 
    negative one.
    '''
    if v > 0:
        return (1, 0, 0)
    return (0, 0, 1)
```

All functions should have docstrings. Your script should also have a
docstring. You can think of this sort of like an intro/thesis for an essay. If I read the docstring at the top of your script, it should
say everything the script hope to do. Like this:

```python
'''
This module prints out example velocity and their resaulting
doppler shifts, to show how the change in color is dependent
on the velocity.
'''

def doppler_shift(v):
    '''
    Given a velocity, computes the relative doppler shift
    and return as an RGB tuple.
    
    For a positive velocity it will be all red, and all blue for a 
    negative one.
    '''
    if v > 0:
        return (1, 0, 0)
    return (0, 0, 1)

def log_doppler_shift(v):
    '''
    Will log the input velocity along it's doppler shifted color
    '''
    color = doppler_shift(v)
    print  'With velocity {}, the red is {} and the blue is {}'.format(
        v,
        color[0],
        color[1]
    )

log_doppler_shift(10)
log_doppler_shift(-1)
log_doppler_shift(0)
```

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
    '''
    Given a velocity, computes the relative doppler shift
    and return as an RGB tuple.
    
    For a positive velocity it will be all red, and all blue for a 
    negative one.
    '''
    if v > 0:
        return (1, 0, 0)
    return (0, 0, 1)
    
points(src=[(1,1,1)], color=doppler_shift(-4))
```

So please, just write more functions. It is possible to make things too generic, by creating too much abstraction
but none of you have that problem. All the code I have seen has been basically one big block. Which is totally
fine for testing stuff out. But you will actually be able to increase your productivity if you start using
functions, as well as make it easier for others to follow what you are doing.


