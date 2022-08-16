# xml_tag_cutter
A small tool to cut specific tags from an XML

## Usage

```
usage: xml_tag_cutter.py [-h] -t TAGS [TAGS ...] -f FILE [-n NAME_TAG]

This is a simple XML cut tool

optional arguments:
  -h, --help            show this help message and exit
  -t TAGS [TAGS ...], --tags TAGS [TAGS ...]
                        List of tags
  -f FILE, --file FILE  target_xml
  -n NAME_TAG, --name_tag NAME_TAG
                        tag for name of the parsed file 
```

## Examples
Example 1:
```
>grep -iE "<certificate>" config.xml | wc -l
1
>python3 xml_tag_cutter.py -f config.xml -n PARSED --tags hostname certificate password
> ls -l
config.xml config.xml_PARSED
>grep -iE "<certificate>" config.xml | wc -l 
0

```
