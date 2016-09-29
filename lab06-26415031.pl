#!/usr/bin/perl

chomp(@input=<STDIN>);
@reversed=reverse(@input);
@sorted=sort(@input);
print "You entered:\n";
foreach $a(@input){
   print $a " ";
}
print "Reversed:\n";
foreach $a(@reversed){
   print $a " ";
}
print "Sorted:\n";
foreach $a(@sorted){
   print $a " ";
}

