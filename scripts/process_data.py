import json
import os

raw_data_dir = "raw_data"
processed_data_dir = "processed_data"

elements_project_count = {}

def process_file(filename):
  elements_project_count[filename] = 0
  projects = []

  with open(f"{raw_data_dir}/{filename}") as f:
    file_json = json.load(f)

    for project in file_json["items"]:
      projects.append(project)
      elements_project_count[filename] += 1

  with open(f"{processed_data_dir}/{filename}.json", "w") as f:
    json.dump(projects, f)

  print(f"{filename} has {elements_project_count[filename]} projects")

def main():
  if not os.path.exists(processed_data_dir):
    os.makedirs(processed_data_dir)

  for filename in os.listdir(raw_data_dir):
    process_file(filename)

  with open(f"element-symbols.json") as element_symbols_file:
    d = {}
    symbol_data = json.load(element_symbols_file)

    for key in symbol_data:
      d[key] = symbol_data[key]
      d[key]["count"] = elements_project_count[key]
      d[key]["name"] = key

    with open(f"{processed_data_dir}/meta.json", "w") as f:
      json.dump(d, f)

if __name__ == "__main__":
  main()
