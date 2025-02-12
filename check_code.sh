#!/bin/bash
isort src tests
black src tests
flake8
mypy src tests
