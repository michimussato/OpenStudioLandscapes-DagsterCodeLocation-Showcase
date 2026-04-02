[![ Logo OpenStudioLandscapes ](https://github.com/michimussato/OpenStudioLandscapes/raw/main/media/images/logo128.png)](https://github.com/michimussato/OpenStudioLandscapes)

---

<!-- TOC -->
* [Openstudiolandscapes-DagsterCodeLocation-Showcase](#openstudiolandscapes-dagstercodelocation-showcase)
  * [Install into OpenStudioLandscapes-Dagster](#install-into-openstudiolandscapes-dagster)
  * [Automation and Functionality](#automation-and-functionality)
<!-- TOC -->

---

# Openstudiolandscapes-DagsterCodeLocation-Showcase

## Install into OpenStudioLandscapes-Dagster

> [!TIP]
> 
> This package is already integrated into the default
> `config.yml`.

The following code snippet is added to the
`dagster_code_locations` section in the `config.yml` file of
[OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster#default-configuration):

```yaml
dagster_code_locations:
  load_from:
  # [...]
  - python_module:
      location_name: OpenStudioLandscapes-DagsterCodeLocation-Showcase Package Code Location
      module_name: OpenStudioLandscapes.DagsterCodeLocation.Showcase.definitions
      working_directory: src
      pip_path: OpenStudioLandscapes-DagsterCodeLocation-Showcase @ git+https://github.com/michimussato/OpenStudioLandscapes-DagsterCodeLocation-Showcase.git@main
  # [...]
```

## Automation and Functionality

This is a dummy showcase Dagster package for the 
[OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster) Feature. 
It does nothing productive:

```mermaid
graph TB
    start([Start])
    file_found{File Found}
    create_file["Create File"]
    delete_file["Delete File"]
    
    start --> file_found 
    file_found -- Yes --> delete_file
    file_found -- No --> create_file
    
    create_file -- job_create_file --> file_found
    delete_file -- job_delete_file --> file_found
```

However, the project implements Dagster sensors which execute Dagster
jobs based on certain circumstances. OpenStudioLandscapes-Dagster-Showcase
demonstrates Dagsters power by running jobs autonomously without human interaction.
