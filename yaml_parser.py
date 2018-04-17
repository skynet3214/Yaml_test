import yaml
from pprint import pprint
import argparse

filename = "/Users/gos/Downloads/Yaml_test/dbgdmp.yaml"
#filename = "/Users/gos/Downloads/20180323184502_vicfw-user-ucs40g-1_BC1_MEZZ0402/MEZZ42_TechSupport/debugdump.yaml"


parser = argparse.ArgumentParser(description = "Yaml Parser v0.1")
parser.add_argument('-f', type = str, required = True, help = "Enter the debug dump yaml file path within double quotes")
parser.add_argument('-c', nargs='*' ,type=str, help = "Enter the commands you want to see the output for in double quotes. For multiple commands, enter each command within double quotes seperate by a space")
args = parser.parse_args()

def test_valid_yaml(filename, commands):
    try:
        with open(filename, 'r') as yaml_f:
            doc = yaml.load(yaml_f)
    except IOError:
        print("Wrong file or file path")
        exit()
    
    try:
        with open(filename, 'r') as yaml_f:
            content = yaml_f.read()
            doc2 = yaml.load(content)
    except IOError:
        print("Wrong file or file path")
        exit()

    print sorted(doc.keys())
    print sorted(doc2.keys())

    for command in commands:
        print command
        print doc[command]
        print doc2[command]
    #print doc 



def main():
    print args.c
    test_valid_yaml(args.f, args.c)


if __name__ == "__main__":
    main()
