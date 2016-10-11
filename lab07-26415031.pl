#!/usr/bin/perl

my $counter=0;
my @names;
sub greet{
  if($counter==0){
    print "Hi $_! You are the first one here!\n";
    $counter+=1;
  }
  else{
    print "Hi $_! I've seen ";
    foreach $i(@names){
      print "$i ";
    }
  }
  $names[$counter]=@_;
  $counter+=1;
  print "\n";

}

greet( "Robb" );
greet( "Jon" );
greet( "Sansa" );
greet( "Arya" );
greet( "Bran" );
greet( "Rickon" );
