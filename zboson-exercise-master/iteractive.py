from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

def f(a, b):
    display(a + b)
    return a+b

w = interactive(f, a=10, b=20)

type(w)
w.children
display(w)
w.kwargs
w.result
