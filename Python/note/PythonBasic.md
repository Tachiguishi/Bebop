## Statements
* Conditional Steps - if ... elif .. else
```Python
if (expression):
   (command)
elif (expression):
   (command)
else:
   (command)
```
* Conditional Steps (Multi elif) - if ... elif .. else
```Python
if x < 0:
    x = 0
    print 'negative changed to zero'
elif x == 0:
    print 'zero'
elif x == 1:
    print 'single'
elif x == 2:
    print 'double'
else:
    print 'more'
```
* Repeated steps - while
```Python
while i < 6:
    print "At the top i is %d" % i
```
* Repeated steps - another example \
Assign a value to i which is greater than 2
```Python
while i > 2:
    print "Right now i is %d" % i
    i=i-1
```
* Loop - for
```Python
for (y) in (x):
    (command)
```

## Reserved words

    and
    as
    assert
    break
    class
    continue
    def
    del
    elif
    else
    except
    exec
    finally
    for
    from
    global
    if
    import
    in
    is
    lambda
    not
    or
    pass
    print
    raise
    return
    try
    while
    with
    yield

## hardware architecture
* __CPU__ (central processing unit) – runs the program; not the brains exactly; very very fast
* __RAM__ (random access memory) – main memory; fast, small, temporary storage; lost on shutdown or reboot
* __secondary memory__ - slower, large, permanent memory; lasts until deleted; examples are disk drives and memory sticks
* __input devices__ – used to give data to the CPU;keyboard, mouse, touch screen
* __output devices__ – screen, speakers, printer, DVD burner
* __network__ - retrieve info from network, but not always available; almost like a secondary memory, slower and less reliable'


## Variable Naming
* Variable names can only contain letters (a, b, c, A, etc.), numeric digits (1, 2, 3, etc.), or _underscore_ characters.
    * However they cannot start with a digit
* Also strictly avoid using Python reserved words

## Mathematical Expressions
* Addition `+`\
    `x = 5 + 10`
* Subtraction `-`\
    `x = 5 - 10`
* Multiplication `*`\
    `x = 5 * 10`
* Power `**`\
    * Exponentiation ( 5^10 )\
    `x = 5**10`
* Division `/`\
    `x = 5 / 10`
* Modulus `%`\
    * Used to return the remainder of a division instead of the quotient answer ( 10 % 3 = 1, since 3 * 3 = 9 and 10 - 9 leaves a remainder 1 )\
    `x = 10 % 3`


## Operator Precedence (PEMDAS)
**PEMDAS:**
1. Parenthesis (P)
2. Exponents / Roots (E)
3. Multiplication and Division (M D)
4. Addition and Subtraction (A S)


## User Input
`raw_input()`\
`name = raw_input("What is your name, human? ")`


## Data Types
* **Numeric types**
    * **Integer numbers**
        * A whole number, i.e. a number that is not a fraction
        * Ex: 1, 5, 33, -24, 5000
    * **Floating-point numbers**
        * A number with a fraction or decimal point
        * 17.34, 98.2, -768.001, 0.2
* **Strings**
    * A collection of characters
    * This can be alphabetic characters, special characters, or even numeric characters (but saved as type string, enclosed in "quotes")
    * Ex: "Alphabetic", "ch@r@cter$!!!", "1234567890"
* `type()`\
    return the type of varibable

## Type Conversion
`int()`, `float()`, or `str()`