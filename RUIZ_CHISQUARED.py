{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "07a87947-5d5c-44a5-ab6b-d247dbfa3b75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chi-squared Statistic: 7.059945782172535\n",
      "P-value: 0.6308781316926666\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import scipy.stats as stats\n",
    "\n",
    "data = pd.read_csv('chisquared.csv')\n",
    "\n",
    "# Extract the data column\n",
    "data_values = data['DATA'].values\n",
    "\n",
    "# Number of bins\n",
    "num_bins = 10\n",
    "\n",
    "# Calculate observed frequencies\n",
    "observed_freq, bin_edges = np.histogram(data_values, bins=num_bins)\n",
    "\n",
    "# Calculate the expected frequencies assuming a Gaussian distribution\n",
    "mu, sigma = np.mean(data_values), np.std(data_values)\n",
    "expected_freq = np.diff(stats.norm.cdf(bin_edges, mu, sigma)) * len(data_values)\n",
    "\n",
    "# Normalize the expected frequencies\n",
    "expected_freq = expected_freq * (observed_freq.sum() / expected_freq.sum())\n",
    "\n",
    "# Perform the chi-squared test\n",
    "chi_squared_stat, p_value = stats.chisquare(observed_freq, expected_freq)\n",
    "\n",
    "print(f\"Chi-squared Statistic: {chi_squared_stat}\")\n",
    "print(f\"P-value: {p_value}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "466eb49d-3d49-44e8-99b5-3b21e72b29ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:cx_team]",
   "language": "python",
   "name": "conda-env-cx_team-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
