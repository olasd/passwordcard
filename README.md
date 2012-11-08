PasswordCard
============

A python-powered PasswordCard generator

What is a passwordcard?
-----------------------

A passwordcard is a grid of random characters that are generated using
a given 64-bit seed.

The original idea for this software comes from passwordcard.org.

Original code is GPLv3, this code is AGPLv3 as it is intended to be
used as a webservice.

I strived for compatibility with the original algorithm. Basically
this boils down to a minimalistic reimplementation of the Java RNG,
and a strict implementation of the original algorithm.
