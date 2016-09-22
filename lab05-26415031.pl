#!/usr/bin/perl

print'enter a string: ';
$this=<STDIN>;
print'enter a number: ';
$times=<STDIN>;
chomp($times);
print "$this" x $times;
