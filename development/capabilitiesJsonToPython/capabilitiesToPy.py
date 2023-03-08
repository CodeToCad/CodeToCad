import jinja2
import os
import json


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

outputDir = f"{SCRIPT_DIR}/../../core/"
templatesDir = f"{SCRIPT_DIR}/templates"

capabilitiesJson = f"{SCRIPT_DIR}/../../core/capabilities.json"

capabilitiesToPyInterface = f"capabilitiesToPyInterface.j2"
capabilitiesToPyInterfaceOut = f"{outputDir}/CodeToCADInterface.py"


capabilitiesToPyProvider = f"capabilitiesToPyProvider.j2"
capabilitiesToPyProviderOut = f"{outputDir}/CodeToCADProvider.py"


capabilitiesToPyTest = f"capabilitiesToPyTest.j2"
capabilitiesToPyTestOut = f"{outputDir}/TestCodeToCADProvider.py"

with open(capabilitiesJson) as f:
    capabilities = json.load(f)

templatesToGenerate = ((capabilitiesToPyInterface, capabilitiesToPyInterfaceOut), (
    capabilitiesToPyProvider, capabilitiesToPyProviderOut), (capabilitiesToPyTest, capabilitiesToPyTestOut))

templateLoader = jinja2.FileSystemLoader(searchpath=templatesDir)
templateEnv = jinja2.Environment(loader=templateLoader)

for template, output in templatesToGenerate:
    print("Generating", template)

    template = templateEnv.get_template(template)
    output_from_parsed_template = template.render(**capabilities)
    with open(output, "w") as fh:
        fh.write(output_from_parsed_template)

    print("Done")