#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 24


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. Is it permissible to use several import statements to import the same module? What would the goal be? Can you think of a situation where it would be beneficial');get_ipython().run_line_magic('pinfo', 'beneficial')

Answer: If a module has already been imported, it's not loaded again. we will simply get a reference to the module that has already been imported.


# In[ ]:





# In[ ]:


Q2. What are some of a module's characteristics? (Name at least one.)

Answer: Characteristics of Modules

Modules contain instructions, processing logic, and data.
Modules can be separately compiled and stored in a library.
Modules can be included in a program.
Module segments can be used by invoking a name and some parameters.
Module segments can be used by other modules.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q3. Circular importing, such as when two modules import each other, can lead to dependencies and bugs that aren't visible. How can you go about creating a program that avoids mutual importing");get_ipython().run_line_magic('pinfo', 'importing')

Answer: Circular importing is a form of circular dependency that is created with the import statement in Python.

ircular imports are the result of bad designs. A deeper analysis of the program could have concluded that the dependency isn't actually required, or that the depended functionality can be moved to different modules that wouldn't contain the circular reference.

A simple solution is that sometimes both modules can just be merged into a single, larger module.


# In[ ]:





# In[ ]:



get_ipython().set_next_input('Q4. Why is _ all _ in Python');get_ipython().run_line_magic('pinfo', 'Python')

Answer: The all tells the semantically “public” names from the module. If there is a name in all, the users are expected to use it, and they can expect that it will not change. By default, Python will export all names that do not start with an _. we certainly could rely on this mechanism.


# In[ ]:





# In[ ]:


Q5. In what situation is it useful to refer to the _ name _ attribute or the string '_ main _'?

Answer: name is a built-in variable which evaluates to the name of the current module. Thus it can be used to check whether the current script is being run on its own or being imported somewhere else by combining it with if statement


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What are some of the benefits of attaching a program counter to the RPN interpreter application, which interprets an RPN script line by line');get_ipython().run_line_magic('pinfo', 'line')

Answer: An advantage of reverse Polish notation is that it removes the need for parentheses that are required by infix notation. While 3 − 4 × 5 can also be written 3 − (4 × 5), that means something quite different from (3 − 4) × 5. A program counter is also known as an instruction counter, instruction pointer, instruction address register or sequence control register. It is a digital counter needed for faster execution of tasks as well as for tracking the current execution point


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q7. What are the minimum expressions or statements (or both) that you'd need to render a basic programming language like RPN primitive but complete— that is, capable of carrying out any computerised task theoretically possible");get_ipython().run_line_magic('pinfo', 'possible')

Answer:


# In[3]:


# Reverse Polish Notation (RPN) Evaluator in Python
import logging
import operator as op
import sys
from typing import Any, List, Union

logging.getLogger(__name__).setLevel("INFO")
supported_operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}
Number = Union[int, float]

def tokenize(expr: str) -> List[str]:
    """Breaks expression `expr` into a list of tokens"""
    return expr.split(" ")

def mpop(stack: List[Any], n: int = 1) -> List[Any]:
    """Pops and returns `n` items from a stack. Mutates `stack`"""
    return [stack.pop() for _ in range(n)]

def to_num(x: Any) -> Number:
    """Converts a value to a its appropriate numeric type"""
    n = float(x)
    return int(n) if n.is_integer() else n

def consume_token(token: str, stack: List[Number]) -> List[Number]:
    """Consumes a token given the current stack and returns the updated stack"""
    if token in supported_operators:
        try:
            num1, num2 = mpop(stack, 2)
        except IndexError:
            logging.error("SyntaxError: Malformed expression")
            sys.exit(1)

        result = supported_operators[token](num2, num1)
        return [*stack, result]
    else:
        try:
            return [*stack, to_num(token)]
        except ValueError:
            logging.error("SyntaxError: Unsupported token '%s'", token)
            sys.exit(1)

def get_result_from_stack(stack: List[Number]) -> Number:
    """Gets the result from `stack`"""
    result, *rest = mpop(stack, 1)
    if rest:
        logging.error("SyntaxError: Found extra tokens")
        sys.exit(1)
    return result

def evaluate_v1(tokens: List[str]) -> Number:
    """Evaluates a tokenized expression and returns the result"""
    stack: List = []

    for token in tokens:
        stack = consume_token(token, stack)

    return get_result_from_stack(stack)

def evaluate_v2(tokens: List[str]) -> Number:
    """Evaluates a tokenized expression and returns the result"""

    def _evaluate(tokens: List[str], stack: List) -> Number:
        if not tokens:
            return get_result_from_stack(stack)

        stack = consume_token(tokens[0], stack)

        return _evaluate(tokens[1:], stack)

    return _evaluate(tokens, [])

if __name__ == "__main__":
    
    print(evaluate_v2(tokenize(input())))
     


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




