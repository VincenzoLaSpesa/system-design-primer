from pathlib import Path
import os
from subprocess import check_output

def run(cmd, echo=True, shell=True, printOutput = True):
    if echo:
        print(cmd)
    output = check_output(cmd, shell=shell).decode("utf-8") 
    if printOutput:
      print(output)
    return output

def generate_epub(infile: str, outfile: str, language: str):
  print("Generating", language)
  run(f"pandoc --metadata-file=epub-metadata.yaml --metadata=lang:{language} --from=markdown -i {infile} -o {outfile}.epub")
  print(f"Done! You can find the '{language}' book at ./{outfile}")

def generate_with_solutions():
  name="system-design-primer"
  outputname = name+".md"
  outfile = open(outputname, "w",encoding="utf8")
  flist=Path('.').rglob('README.md')
  for fname in flist:
    print(fname)
    f = open(fname, "r",encoding="utf8")
    outfile.writelines(("\r\n",f"Merging {fname}","\r\n"))
    outfile.write(f.read())
    f.close()
  outfile.close()
  generate_epub(outputname,name, "en")

# main
generate_with_solutions()

