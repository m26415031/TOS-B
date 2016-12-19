array=() # Create array
while IFS= read -r line # Read a line
do
    array+=("$line") # Append line to the array
done < data.txt

for i in "${array[@]}"
do
	echo $i
	echo "aaa"
done
