#!/bin/bash

# echo 'a b c'  | phrases
# echo 'A B C' | phrases
# echo 'a B c' | phrases
# echo 'a !B C$' | phrases

test_array=('a b c' 'A B C' 'a B c' 'a !b c#')

array=()
len=${#test_array[@]}
for (( i=0; i+1 <= $len; i++ )); do
    output1=$(echo "${test_array[$i]}" | phrases)
    output2=$(echo "${test_array[$i+1]}" | phrases)
    if [[ $output1 -eq $output2 ]]; then
        echo "wtf"
    fi
done

# for (( i=0; i < $len; i++ )); do
#     for (( j=$((i+1)); j < $len; j++ )); do 
#         echo ${array[$i]} 

#     done
# done 
