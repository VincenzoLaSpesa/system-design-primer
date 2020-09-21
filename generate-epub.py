from pathlib import Path
import os
from subprocess import check_output
from MarkdownPP import MarkdownPP

def run(cmd, echo=True, shell=True, printOutput = True):
    if echo:
        print(cmd)
    output = check_output(cmd, shell=shell).decode("utf-8") 
    if printOutput:
      print(output)
    return output

def generate_epub(infile: str, outfile: str, language: str):
  print("Generating", language)
  run(f"pandoc --metadata-file=epub-metadata.yaml --metadata=lang:{language} --from=markdown -i {infile} -o {outfile}")
  print(f"Done! You can find the '{language}' book at ./{outfile}")

def generate():
  name="system-design-primer"
  outfile = open(name+".mdPP", "w",encoding="utf8")
  f = open('README.md', "r",encoding="utf8")
  outfile.write(f.read())

  outfile.write("\r\n# Example system designs\r\nAll the solution inside the repository\r\n")

  flist=Path('./solutions/').rglob('README.md')
  for fname in flist:
    print(fname)
    outfile.write(f"Merging {fname}\r\n!INCLUDE \"{fname}\", 1\r\n")
  outfile.close()

  infile = open(name+".mdPP", "r",encoding="utf8")
  outfile = open(name+".md", "w",encoding="utf8")
  MarkdownPP(input=infile, modules=['include'], output=outfile)
  generate_epub(name+".md",name+".epub", "en")

# main
generate()

