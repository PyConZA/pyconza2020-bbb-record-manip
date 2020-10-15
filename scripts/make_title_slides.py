#!/usr/bin/env python3

import argparse
import csv
import os
import subprocess
import re

from bs4 import BeautifulSoup

def replace_contents(soup, box_id, text):
    box = soup.find(id=box_id)
    para = box.find("flowPara")
    para.string.replace_with(text.upper())
    
def adjust_title_size(soup):
    box = soup.find(id="titlebox")
    para = box.find("flowPara")
    text = para.string    
    fudge = int((8e5/len(text))**0.5) # Iä, iä, Cthulhu fhtagn
    box["style"] = re.sub(r"font-size:\d+px", f"font-size:{fudge}px", box["style"])

def make_title_slides(talks_tsv, template_svg, output_dir):
    with open(template_svg) as f:
        soup = BeautifulSoup(f.read(), "xml")
    
    with open(talks_tsv) as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for talk_id, title, speakers in reader:
            replace_contents(soup, "titlebox", title)
            replace_contents(soup, "presenterbox", speakers)
            adjust_title_size(soup)
            
            basename = os.path.join(output_dir, talk_id)
            svg = f"{basename}.svg"
            pdf = f"{basename}.pdf"
            
            with open(svg, "w") as f:
                print(str(soup), file=f)
            
            subprocess.run(["inkscape", f"--export-filename={pdf}", svg], stderr=subprocess.DEVNULL)
            os.remove(svg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate title slides for talks.')

    parser.add_argument('--talks', help='Path to a TSV file of talk identifiers, titles and speakers.', required=True)
    parser.add_argument('--template', help='Path to an SVG template with text placeholders for the title and speakers.', required=True)
    parser.add_argument('--output-dir', help='Path to the output directory.', default=".")
    
    args = parser.parse_args()
    make_title_slides(args.talks, args.template, args.output_dir)
