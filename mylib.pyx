#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2025 
# Developer : Mohammed Al-Baqer

cdef public int add_numbers(int a, int b):
    return a + b

def py_add_numbers(a, b):
    return add_numbers(a, b)

