a=1
while [ $a -le 100 ]
do
    echo $a
    a=$((a+2))
done

# using for loop and iterator step
for number in {1..99..2}
do
    echo $number
done
