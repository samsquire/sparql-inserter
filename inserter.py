import yaml
from subprocess import Popen, PIPE

def get_command(kind):
    return ["bash", "-c", "curl -X POST -L http://localhost:9999/namespace/sam/sparql -H"Accept: text/csv" -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -G --data-urlencode '" + kind + "@query.sparql'"]

for document in yaml.safe_load_all():
    if "query" in document:
        f = open("query.sparql", "w")
        f.write(document["query"])
        command = get_command("query")

    if "update" in document:
        f = open("query.sparql", "w")
        f.write(document["update"])
        command = get_command("query")

    process = Popen(command, stdout=PIPE)
    output = process.stdout.decode("utf-8").split("\n")
    print(output)
