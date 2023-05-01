# Genotype-Character-Mean-Calculator
This script can be useful for students, scholars, researchers and data analysts who need to calculate means for multiple genotypes and characters in large datasets. It provides an efficient way to perform these calculations and output the results to a new file.

## Description

This repository contains code for processing genotype data and calculating the mean values for various characters across three replications. The code reads in an Excel file, calculates the means for each genotype and character, and outputs the results to a new Excel file.

## Usage

To use this code, simply download or clone the repository and run the `main.py` script. The input data should be in an Excel file with the following format:

- Column 1: Genotype name
- Column 2: Replication number
- Columns 3 and beyond: Character values for each replication

The output file will contain a pivot table with the mean values for each genotype and character.

## Help

A model input: [model_data](https://github.com/Insight-deviler/Genotype-Character-Mean-Calculator/blob/main/model_data.xlsx) and its output: [mean_genotype_data.xlsx](https://github.com/Insight-deviler/Genotype-Character-Mean-Calculator/blob/main/mean_genotype_data.xlsx) file has been provided within this repository to give you an idea how the script works.

## Dependencies

This code requires the following Python packages:

- pandas
- numpy

## License

This code is licensed under the GNU General Public License version 3.0. See the `LICENSE` file for more information.
