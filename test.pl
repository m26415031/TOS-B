#!/usr/bin/perl

$counter=0;
my @names;
sub greet{
  $names[$counter]=@_;
  $counter+=1;
  if($counter==1){
    print "Hi $names[0]! You are the first one here!";
  }
  else{
    print "Hi $names[$counter]! I've seen ";
    foreach $i(@names){
      print "$i ";
    }
  }
  #$names[$counter]=@_;
  #$counter+=1;
  print "\n";
}

greet( "Robb" );
greet( "Jon" );
greet( "Sansa" );
greet( "Arya" );
