# autoJGAAP
**autoJGAAP** streamlines the JGAAP experimentation process by automating configuration file creation, experiment execution, and results analysis.

[Download JGAAP](https://github.com/evllabs/JGAAP/releases) 

## Background

As the scale of a research project grows, the convenience of JGAAP command line experimentation becomes a necessity. However, configuration files for massive experiments are time-consuming to write, and thousands of experiment results are difficult to interpret.

**autoJGAAP.py** automates these elements of the research pipeline, both to increase time efficiency and lower the learning curve for less experienced researchers.

## Execution

* Place a copy of the JGAAP .jar file in the **autoJGAAP** directory. 
* Navigate to this directory on your command line and enter the following command:

  * ```python3 autoJGAAP.py```

* NOTE: Enter 'python' instead of 'python3' if using Windows.
* Experiment results and other output will be stored in the **Output** directory. 

## Experiment Setup

### Documents
* The **Documents** directory contains all plaintext documents to experiment on.
* Documents in **Known** are used to train JGAAP to recognize patterns in each author's writing. 
* Documents in **Unknown** are used to test JGAAP's training; JGAAP attempts to determine the author of each document in **Unknown** by applying its understanding of each author's style gained by training on the **Known** documents. 
* Within **Known** and **Unknown**, store each document in a folder named after its author or category, such as "Hemingway" or "EastCoastResidents". Any number of authors can be provided.
* [Example directory tree](/example.jpg)
* NOTE: ensure no document or directory names contain commas.

### Settings
* Specify experiment settings in **settings.csv**.
* JGAAP will be configured to run an experiment with every combination of the provided settings: one setting from each column.
* Place each desired experiment setting in its corresponding column, beginning at the second row. 
  * If a setting references a variable, such as character n-grams, specify this variable's value like so:
    * Character Ngrams|N:4  
    *for n=4*
* Names and brief explanations experiment settings can be found in JGAAP's GUI.

## Per-script Breakdown

```autoJGAAP.py```

* Wrapper for the following scripts.
* Organizes produced files, checks for errors

```printCorpusConfig.py```

* Writes corpus configuration file, placed in **Configuration**.
* This config file provides JGAAP with the author, path, and name of each document to experiment on.

```printSettingsConfig.py```

* Writes settings config file, placed in **Configuration**.
* Each line of this config file is a combonation of user-provided settings in **settings.csv** and provides instructions for one experiment.

```print_tmp.py```

* JGAAP writes experiment results to text files in tmp. 
* **print_tmp.py** combines all files in tmp and its subdirectories.
* The combined results are written to **rawResults.txt**.

```refineResults.py```

* Condenses **rawResults.txt** to the number of currect and total classifications for a given combonation of experiment settings for a given author's documents. 
* This information is written to **refinedResults.csv**.

```getSettingPerformance.py```

* From **refinedResults.csv**, determines average success rate, standard deviation of success rates, median success rate, and average success rate across all authors for each individual experiment setting used in settings.csv. 
* Performance stats written to **singleSettingPerformance.csv**.




