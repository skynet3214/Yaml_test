#!/bin/sh

generate_yaml_version(){
    a=${@}
    echo $a
    yaml_quote=\"
    echo "the no of srguments is : " $#
    eval $2 > tst
    while IFS= read -r line
    do
        echo "\ $line \n" | sed s/'---'/'----'/g | sed s/\"/\\\\\"/g >> tst.yaml 
    done < tst
    rm tst
}


generate_yaml_version "PATH" "echo mona;echo mona"
generate_yaml_version "PATH" "echo gowtham"