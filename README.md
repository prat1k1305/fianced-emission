# fianced-emission for banks as per pcaf guideline using EEIO database
This repository contains a simple code to calculate financed emissions for banks as per the PCAF guidelines using the EEIO database. The code calculates the financed emissions for a bank based on the loans and investments made by the bank. The code uses the `pandas` library to read the data and perform the calculations. The code also uses the `numpy` library to perform numerical calculations. The code reads the data from a CSV file and calculates the financed emissions based on the emissions intensity of the sectors in which the bank has invested or provided loans.

## Requirements
The code requires the following libraries:
- pandas
- numpy

You can install the required libraries using the following command:
```bash
pip install pandas numpy
```

## Usage
To use the code, you need to provide the following inputs:
- A CSV file containing the loans and investments made by the bank
- A CSV file containing the emissions intensity of the sectors

The code will read the data from the CSV files and calculate the financed emissions for the bank.

You can run the code using the following command:
```bash
python financed_emissions.py loans_and_investments.csv emissions_intensity.csv
```

The code will print the financed emissions for the bank.

## Example
You can find an example of the input files in the `data` directory. The `loans_and_investments.csv` file contains the loans and investments made by the bank, and the `emissions_intensity.csv` file contains the emissions intensity of the sectors. You can run the code using the following command:
```bash
python financed_emissions.py data/loans_and_investments.csv data/emissions_intensity.csv
```

The code will print the financed emissions for the bank based on the example data.

## License
This code is released under the MIT License. You can find the full license text in the `LICENSE` file.
```

```python
def calculate_financed_emissions(loans_and_investments_file, emissions_intensity_file):
    # Read the loans and investments data
    loans_and_investments = pd.read_csv(loans_and_investments_file)

    # Read the emissions intensity data
    emissions_intensity = pd.read_csv(emissions_intensity_file)

    # Merge the loans and investments data with the emissions intensity data
    financed_emissions = loans_and_investments.merge(emissions_intensity, on='sector', how='left')

    # Calculate the financed emissions
    financed_em