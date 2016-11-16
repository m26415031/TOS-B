#!usr/bin/perl

open(my $txtfile, '<:encoding(UTF-8)','lab08-input.txt')
or die "Could not open file $!";

while(my $row=<$txtfile>){
  chomp $row;
  my($firstname,$surname)=split /,/,$row;
  #print "$firstname $surname \n";
  $hash{$firstname}=$surname;
}

while(($key,$value)=each %hash){
  print "$key => $value\n";
}
