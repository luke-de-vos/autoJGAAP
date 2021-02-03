# autoJGAAP
Streamline the JGAAP experimentation process by automating configuration file creation, experiment execution, and results info extraction.

[Download JGAAP](https://github.com/evllabs/JGAAP/releases) 

## Background

As the scale of a research project grows, the convenience of JGAAP command line experimentation becomes a necessity. However, configuration files for massive experiments are time-consuming to write, and thousands of experiment results are difficult to interpret.

**autoJGAAP.py** automates these elements of the research pipeline, both to significantly increase time efficiency and lower the learning curve for less experienced researchers.

## Usage

#### Documents
Place plaintext documents to experiment on in **Documents**. Place documents for training in the **Known** subdirectory. Place documents for validation in the **Unknown** directory. Within these directories, store each document in a folder named after its author or category, such as "Hemingway" or "EastCoastResidents". [Example directory tree](/example.jpg)

NOTE: ensure no document or directory names contain commas.

#### Experiment Settings
Specify experiment settings in **settings.csv**. Place each desired experiment setting in its corresponding column, beginning at the second row. JGAAP will be configured to run experiments with every combination of the provided settings. Names and brief explanations experiment settings can be found by browsing JGAAP's GUI.

#### Execution Syntax
Within the **autoJGAAP** directory, enter on the command line:

```python3 autoJGAAP.py```

NOTE: python3 -> python if using Windows

## Per-script Breakdown

```printCorpusConfig.py```

Writes corpus configuration file. This config file provides JGAAP with the author, path, and name of each document to experiment on.

```printSettingsConfig.py```

Writes settings config file. Each line of this config file is a combonation of user-provided settings in **settings.csv** and provides instructions for one experiment.

```print_tmp.py```

JGAAP experiment results are written to text files in tmp. **print_tmp.py** combines all results files. The combined results are written to **rawResults.txt**.

```refineResults.py```

Condenses **rawResults.txt** to the number of currect and total classifications for a given combonation of experiment settings for a given author's documents. This information is written to **refinedResults.csv**.

```getSettingPerformance.py```

From **refinedResults.csv**, determines average success rate, standard deviation of success rates, median success rate, and average success rate across all authors for each individual experiment setting used in settings.csv. Performance written to **singleSettingPerformance.csv**.

```autoJGAAP.py```

Wrapper for above scripts.
All results files moved to **Results** directory.
Configuration files moved to **Configuration** directory.
JGAAP standard output written to **JGAAP_status_output.txt**




