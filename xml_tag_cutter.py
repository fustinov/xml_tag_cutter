import xml.etree.ElementTree as ET
import argparse


# Input parameters
parser = argparse.ArgumentParser(description='This is a simple XML cut tool')
parser.add_argument("-t", "--tags", help="List of tags", nargs='+', required=True)
parser.add_argument("-f", "--file", help="target_xml", type=str, required=True)
parser.add_argument("-n", "--name_tag", help="tag for name of the parsed file", type=str, default="_PARSED")
args = parser.parse_args()


tree = ET.parse('{}'.format(args.file))
root = tree.getroot()

for child in root:
	for tag in args.tags:
		if child.tag == "{}".format(tag):
			root.remove(child)

tree.write("{}_{}".format(args.file, args.name_tag))