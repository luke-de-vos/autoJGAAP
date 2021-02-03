# autoJGAAP
Automate bottlenecks in the JGAAP experimentation process.

[Download JGAAP](https://github.com/evllabs/JGAAP/releases) 

## Usage

Place plaintext documents to experiment on in 'Documents'. Each file should be stored in a folder named after its author or category, such as "Hemingway" or "Left-handed". NOTE: ensure no document or directory names contain commas, or experimentation will fail.

Specify experiment settings in 'settings.csv'. Names and brief explanations experiment settings can be found by browsing JGAAP's GUI.


## Background

As the scale of a research project grows, the convenience of JGAAP command line experimentation becomes necessity. However, configuration files for massive experiments are time-consuming to write, and thousands of results are difficult to interpret.

autoJGAAP.py automates these elements of the research pipeline to fit a user's research needs, both to increase time efficiency and lower the learning curve for less experienced researchers.

## Per-script Breakdown

* **printCorpusConfig.py**

Writes corpus configuration file. This config file provides JGAAP with the author, path, and name of each document to experiment on.

* **printSettingsConfig.py**

Writes settings config file. Each line of this config file is a combonation of user-provided settings in settings.csv and provides instructions for one experiment.

* **print_tmp.py**

JGAAP experiment results are written to text files in tmp. print_tmp.py combines all results files. The combined results are written to rawResults.txt.

* **refineResults.py**

Condenses rawResults.txt to the number of currect and total classifications for a given combonation of experiment settings for a given author's documents. This information is written to refinedResults.csv.

* **getSettingPerformance.py**

From refinedResults.csv, determines average success rate, standard deviation of success rates, median success rate, and average success rate across all authors for each individual experiment setting used in settings.csv. Performance written to singleSettingPerformance.csv.

* **autoJGAAP.py**

Wrapper for above scripts.
All results files moved to 'Results' directory.
Configuration files moved to 'Configuration' directory.
JGAAP standard output written to 'JGAAP_status_output.txt'




