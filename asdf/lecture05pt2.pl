#!/usr/bin/perl

@array=qw(low heroes lodger);
@removed=splice @array,1,2,qw(blackstar);
@removed=splice @array,1,0,qw(bowie);
foreach $element (@array){
print $element;
print "\n";
}
#print (@array);
#print (@removed);
#print "\n";


