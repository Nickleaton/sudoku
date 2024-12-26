Token Documentation
====================

The `Token` class and its subclasses represent regular expression patterns and provide various ways to combine them
using the `+`, `|`, and other operators to build more complex patterns.

The following examples demonstrate how to create and combine tokens using the provided subclasses.

Creating a Token
----------------

A `Token` represents a single regular expression pattern. To create a token,
simply pass a string to the constructor for the pattern.
The pattern can contain groups, and that enables the removal of any helping text

```python
# Create a token with a simple pattern
token = Token('ab')
print(token)  # Output: Token('ab')
``` 

Creating a Choice Token
------------------------

A `ChoiceToken` represents an alternation (choice) between multiple tokens. To create a choice token, simply use the `|`
operator between two or more tokens.

```python
# Define some basic tokens
token_a = Token('a')
token_b = Token('b')

# Create a choice token between 'a' and 'b'
choice_token = token_a | token_b
print(choice_token)  # Output: ChoiceToken(['a', 'b'])
```

Creating a Sequence Token
--------------------------

A `SequenceToken` represents a sequence of tokens. To create a sequence token, simply use the `+` operator between two
or more tokens.

```python
# Define some basic tokens
token_a = Token('a')
token_b = Token('b')

# Create a sequence token where 'a' comes before 'b'
sequence_token = token_a + token_b
print(sequence_token)  # Output: SequenceToken(['a', 'b'])
```

Creating a Repeat Token
-------------------------

A `RepeatToken` represents a repetition of a token.

```python
# Define some basic tokens
token_a = Token('a')

# Create a repeat token of 3 'a' tokens
repeat_token = token_a * 3
print(repeat_token)  # Output: RepeatToken('a', 3, 3)
```

A 'RepeatToken' can also have a lower and upper bound for the number of repetitions.
If the upper bound is not specified, it is effectively unlimited.

```python
# Define some basic tokens
token_a = Token('a')

# Create a repeat token of 3 to 5 'a' tokens
repeat_token = token_a * (3, 5)
print(repeat_token)  # Output: RepeatToken('a', 3, 5)
``` 

Creating an Optional Token
----------------------------

An `OptionalToken` represents an optional token. It either appears once or not at all.

```python
# Define some basic tokens
token_a = Token('a')

# Create an optional token of 'a'
optional_token = OptionalToken(token_a)
print(optional_token)  # Output: OptionalToken(Token('a'))
```

Creating a ZeroOrMoreToken
----------------------------

A `ZeroOrMoreToken` represents a zero or more repetitions of a token.

```python
# Define some basic tokens
token_a = Token('a')

# Create a zero or more token of 'a'
zero_or_more_token = ZeroOrMoreToken(token_a)
print(zero_or_more_token)  # Output: ZeroOrMoreToken(Token('a'))
```

Standard Tokens
----------------

These are predefined tokens that are to be used by the parsers.
That way if the format changes, then there is only one place to update.

{% for token in tokens|sort(attribute='name') %}
{% if token.name != 'Token' %}
{{ token.name }}Token
-----------------
{{ token.description }}
{% endif %}
{% endfor %}
