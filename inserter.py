import yaml
from subprocess import Popen, PIPE
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--show-updates", action="store_true")
args = parser.parse_args()
inputfile = open(args.file, "r")

def get_command(kind):
    return ["bash", "-c", "curl -s -X POST -L http://localhost:9999/namespace/sam/sparql -H'Accept: text/csv' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -G --data-urlencode '" + kind + "@query.sparql'"]

for document in yaml.safe_load_all(inputfile):
    if "comment" in document:
        print(document["comment"])
    kind = None

    if "query" in document:
        kind = "query"
    if "update" in document:
        kind = "update"

    f = open("query.sparql", "w")
    f.write(document[kind])
    f.close()
    command = get_command(kind)
    process = Popen(command, stdout=PIPE)
    output = process.stdout.read().decode("utf-8")
    if kind == "query" or args.show_updates: 
        print(output)
