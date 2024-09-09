# PRECEDENCE FROM UP THE MOST PRECEDNCE TO DOWN LOWEST 
"""
Binding or parenthesized expression, list display, dictionary display, set display
(expressions...),

[expressions...], {key: value...}, {expressions...}


Subscription, slicing, call, attribute reference
x[index], x[index:index], x(arguments...), x.attribute


Await expression
await x


Exponentiation [5]
**


Positive, negative, bitwise NOT
+x, -x, ~x


Multiplication, matrix multiplication, division, floor division, remainder [6]
*, @, /, //, %


Addition and subtraction
+, -


Shifts
<<, >>


Bitwise AND
&


Bitwise XOR
^


Bitwise OR
|


Comparisons, including membership tests and identity tests
in, not in, is, is not, <, <=, >, >=, !=, ==


Boolean NOT
not x


Boolean AND
and


Boolean OR
or


Conditional expression
if – else


Lambda expression
lambda


Assignment Expression
:=
"""