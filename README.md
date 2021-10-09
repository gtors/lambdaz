# LambdaZ

DSL for writing lambda expressions.

## Installation

```bash
pip install lambdaz
```

## Units

`a0..6` - positional arguments

`kw` - kwargs, `kw.kwarg_name_here`

`val` - wrapper for the existed python objects

Every DSL expression should be terminated with `._`


## Examples:

List sorting:

```python
>>> from lambdaz import a0  # argument with index 0

>>> scores = [
...     {'name': 'Nikita', 'score': 2},
...     {'name': 'Oleg', 'score': 1},
...     {'name': 'Pavel', 'score': 4},
... ]

>>> print(sorted(scores, key=a0['score']._))
[{'name': 'Oleg', 'score': 1}, {'name': 'Nikita', 'score': 2}, {'name': 'Pavel', 'score': 4}]
```

Strings manipulation: 

```python
>>> from lambdaz import a0
>>> users = [
...     '  nikita  ',
...     '  oLeg',
...     'paveL   ',
... ]

>>> print(list(map(a0.strip().title()._, users)))
['Nikita', 'Oleg', 'Pavel']
```

Math expressions:

```python
>>> from lambdaz import a0, a1, a2

>>> math_expression = (a0 * a1 + a2)._
>>> print(math_expression(10, 2, 1))
21
>>> complex_math_expression = (50 / (a0 ** 2) * 2)._
>>> print(complex_math_expression(5))
100.0
```

Kwargs: 

```python
>>> from lambdaz import kw, val

>>> hello = val("Hello {}!").format(kw.first_name + " " + kw.last_name)._
>>> hello(first_name="Foo", last_name="Bar")
Hello Foo Bar!
```

## Similar projects
- https://github.com/Suor/whatever
- https://github.com/dry-python/lambdas
- https://gist.github.com/internetimagery/05082fac28bc17860ec23fa0d7172df7
- https://github.com/sspipe/sspipe
