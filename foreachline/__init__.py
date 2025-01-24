#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import click

@click.group()
def cli():
    pass

@cli.command
@click.argument('code')
def run(code: str):
    function = f"lambda l: {code}"
    function = eval(function)
    while True:
        try:
            l = input()
            print(function(l))
        except EOFError:
            break

@cli.command
@click.argument('code')
def filter(code: str):
    function = f"lambda l: {code}"
    function = eval(function)
    while True:
        try:
            l = input()
            if function(l):
                print(l)
        except EOFError:
            break
