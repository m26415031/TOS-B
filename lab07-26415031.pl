#!/usr/bin/perl

$counter=0;
my @names;
sub greet{
  if($counter==0){
    print "Hi @_! You are the first one here!";
    $counter+=1;
  }
  else{
    print "Hi @_! I've seen ";
    foreach $i(@names){
      print $i;
      print " ";
    }
  }
  $names[counter]=@_;
  print "\n";
}

greet( "David" );
greet( "Ziggy" );
greet( "Aladdin" );
greet( "Thin White Duke" );
