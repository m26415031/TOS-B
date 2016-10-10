#!/usr/bin/perl

chomp(@input=<STDIN>);
@reversed=reverse(@input);
@sorted=sort(@input);
print "You entered: ";
foreach $a(@input){
   print "$a ";
}
print "\nReversed: ";
foreach $a(@reversed){
   print "$a ";
}
print "\nSorted: ";
foreach $a(@sorted){
   print "$a ";
}
print "\n";

