{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Assignment4 Pandas 2804.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python378jvsc74a57bd057baa5815c940fdaff4d14510622de9616cae602444507ba5d0b6727c008cbd6",
      "display_name": "Python 3.7.8 64-bit"
    },
    "language_info": {
      "name": "python",
      "version": "3.7.8"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WQnE-FIctD3X"
      },
      "source": [
        "# Assignment 4: Practice Pandas"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XWndkUcMt0Y6"
      },
      "source": [
        "# PartA\n",
        "Basic operations with Pandas."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wCIa805ItoIh"
      },
      "source": [
        "### 1. Create an empty DataFrame"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Eukmdzr8tr1O"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.DataFrame()"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vxGmJIP74KS6"
      },
      "source": [
        "### 2. Create a complete empty DataFrame without any column name or indices and then appending columns one by one to it. {Result must be as in a given image. Remove a given image after use}  "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {},
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Articles  Improved    Name\n0      97.0    2200.0   Ankit\n1     600.0      75.0  Ankita\n"
          ]
        }
      ],
      "source": [
        "dfA2 = pd.DataFrame()\n",
        "\n",
        "dfA2_row1 = {'Name':'Ankit', 'Articles':97, 'Improved':2200}\n",
        "dfA2_row2 = {'Name':'Ankita', 'Articles':600, 'Improved':75}\n",
        "dfA2_row3 = {'Name':'Yashvardhan', 'Articles':200, 'Improved':100}\n",
        "\n",
        "dfA2_append_row = dfA2.append(dfA2_row1,ignore_index = True)\n",
        "dfA2_append_row2 = dfA2_append_row.append(dfA2_row2,ignore_index = True)\n",
        "dfA2_append_row3 = dfA2_append_row2.append(dfA2_row,ignore_index = True)\n",
        "\n",
        "print(dfA2_append_row3)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qdLANLn8uiUs"
      },
      "source": [
        "### 3. Copy this code and add a row to display this set as a DataFrame\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mf3h1DsruXxP"
      },
      "source": [
        "Following the \"sequence of rows with the same order of fields\" principle, you can create a DataFrame from a list that contains such a sequence, or from multiple lists zip()-ed together in such a way that they provide a sequence like that:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HmjAzR5LufVD"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "listPepper = [ \n",
        "            [50, \"Bell pepper\", \"Not even spicy\"], \n",
        "            [5000, \"Espelette pepper\", \"Uncomfortable\"], \n",
        "            [500000, \"Chocolate habanero\", \"Practically ate pepper spray\"]\n",
        "            ]\n",
        "# add your code here\n",
        "df_create = pd.DataFrame(listPepper)\n",
        "new_row = {0:45000, 1:'Cold', 2:'Sheesh'}\n",
        "df_create = df_create.append(new_row, ignore_index=True)\n",
        "print(df_create)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        0                   1                             2\n0      50         Bell pepper                Not even spicy\n1    5000    Espelette pepper                 Uncomfortable\n2  500000  Chocolate habanero  Practically ate pepper spray\n3   45000                Cold                        Sheesh\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "73sQd1aK47hY"
      },
      "source": [
        "### 4. Create an empty DataFrame with columns name only then appending rows one by one to it using append() method. The result must be as in a given image.\n",
        "![python-empty-dataframe.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {},
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        Name  Articles  Improved\n0      Ankit        97      2200\n1  Alishwary        30        50\n2       yash        17       220\n"
          ]
        }
      ],
      "source": [
        "new_df = pd.DataFrame()\n",
        "data = {'Name': ['Ankit', 'Alishwary', 'yash'],\n",
        "\t'Articles': [97, 30, 17],\n",
        "\t'Improved': [2200, 50, 220]\n",
        "    }\n",
        "TABLE = pd.DataFrame(data)\n",
        "print(TABLE)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "__T1mWsOwFqx"
      },
      "source": [
        "# Part B"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bY8801ORgTDz"
      },
      "source": [
        "{In this exercise, we will use pandas to examine house sale price data.\n",
        "\n",
        "This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.\n",
        "\n",
        "[Download file](https://www.kaggle.com/harlfoxem/housesalesprediction/download) kc_house_data.csv and use it in your project \n",
        "\n",
        "A very common filetype is .csv (Comma-Separated-Values). The rows are provided as lines, with the values they are supposed to contain separated by a delimiter (most often a comma). You can set another delimiter via the sep argument.}\n",
        "\n",
        "{ } - section inside braces must be deleted before submission."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lKype_DEg4RG"
      },
      "source": [
        "### 5. Start by importing panda and Use Pandas' read_csv function to read a file as a DataFrame. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ty-uRczPiCmi"
      },
      "source": [
        "import pandas as pd \n",
        "\n",
        "my_dataframe = pd.read_csv(\"kc_house_data.csv\")\n",
        "\n",
        "print(my_dataframe)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "               id             date     price  bedrooms  bathrooms  \\\n0      7129300520  20141013T000000  221900.0         3       1.00   \n1      6414100192  20141209T000000  538000.0         3       2.25   \n2      5631500400  20150225T000000  180000.0         2       1.00   \n3      2487200875  20141209T000000  604000.0         4       3.00   \n4      1954400510  20150218T000000  510000.0         3       2.00   \n...           ...              ...       ...       ...        ...   \n21608   263000018  20140521T000000  360000.0         3       2.50   \n21609  6600060120  20150223T000000  400000.0         4       2.50   \n21610  1523300141  20140623T000000  402101.0         2       0.75   \n21611   291310100  20150116T000000  400000.0         3       2.50   \n21612  1523300157  20141015T000000  325000.0         2       0.75   \n\n       sqft_living  sqft_lot  floors  waterfront  view  ...  grade  \\\n0             1180      5650     1.0           0     0  ...      7   \n1             2570      7242     2.0           0     0  ...      7   \n2              770     10000     1.0           0     0  ...      6   \n3             1960      5000     1.0           0     0  ...      7   \n4             1680      8080     1.0           0     0  ...      8   \n...            ...       ...     ...         ...   ...  ...    ...   \n21608         1530      1131     3.0           0     0  ...      8   \n21609         2310      5813     2.0           0     0  ...      8   \n21610         1020      1350     2.0           0     0  ...      7   \n21611         1600      2388     2.0           0     0  ...      8   \n21612         1020      1076     2.0           0     0  ...      7   \n\n       sqft_above  sqft_basement  yr_built  yr_renovated  zipcode      lat  \\\n0            1180              0      1955             0    98178  47.5112   \n1            2170            400      1951          1991    98125  47.7210   \n2             770              0      1933             0    98028  47.7379   \n3            1050            910      1965             0    98136  47.5208   \n4            1680              0      1987             0    98074  47.6168   \n...           ...            ...       ...           ...      ...      ...   \n21608        1530              0      2009             0    98103  47.6993   \n21609        2310              0      2014             0    98146  47.5107   \n21610        1020              0      2009             0    98144  47.5944   \n21611        1600              0      2004             0    98027  47.5345   \n21612        1020              0      2008             0    98144  47.5941   \n\n          long  sqft_living15  sqft_lot15  \n0     -122.257           1340        5650  \n1     -122.319           1690        7639  \n2     -122.233           2720        8062  \n3     -122.393           1360        5000  \n4     -122.045           1800        7503  \n...        ...            ...         ...  \n21608 -122.346           1530        1509  \n21609 -122.362           1830        7200  \n21610 -122.299           1020        2007  \n21611 -122.069           1410        1287  \n21612 -122.299           1020        1357  \n\n[21613 rows x 21 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NaCZwXTqh4KR"
      },
      "source": [
        "### 6. Use describe to get the basic statistics of all the columns\n",
        " Note the highest and lowest price of the house in the dataset."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VeIbhKz6iAuM"
      },
      "source": [
        "my_dataframe.describe(include='all')"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                  id             date         price      bedrooms  \\\n",
              "count   2.161300e+04            21613  2.161300e+04  21613.000000   \n",
              "unique           NaN              372           NaN           NaN   \n",
              "top              NaN  20140623T000000           NaN           NaN   \n",
              "freq             NaN              142           NaN           NaN   \n",
              "mean    4.580302e+09              NaN  5.400881e+05      3.370842   \n",
              "std     2.876566e+09              NaN  3.671272e+05      0.930062   \n",
              "min     1.000102e+06              NaN  7.500000e+04      0.000000   \n",
              "25%     2.123049e+09              NaN  3.219500e+05      3.000000   \n",
              "50%     3.904930e+09              NaN  4.500000e+05      3.000000   \n",
              "75%     7.308900e+09              NaN  6.450000e+05      4.000000   \n",
              "max     9.900000e+09              NaN  7.700000e+06     33.000000   \n",
              "\n",
              "           bathrooms   sqft_living      sqft_lot        floors    waterfront  \\\n",
              "count   21613.000000  21613.000000  2.161300e+04  21613.000000  21613.000000   \n",
              "unique           NaN           NaN           NaN           NaN           NaN   \n",
              "top              NaN           NaN           NaN           NaN           NaN   \n",
              "freq             NaN           NaN           NaN           NaN           NaN   \n",
              "mean        2.114757   2079.899736  1.510697e+04      1.494309      0.007542   \n",
              "std         0.770163    918.440897  4.142051e+04      0.539989      0.086517   \n",
              "min         0.000000    290.000000  5.200000e+02      1.000000      0.000000   \n",
              "25%         1.750000   1427.000000  5.040000e+03      1.000000      0.000000   \n",
              "50%         2.250000   1910.000000  7.618000e+03      1.500000      0.000000   \n",
              "75%         2.500000   2550.000000  1.068800e+04      2.000000      0.000000   \n",
              "max         8.000000  13540.000000  1.651359e+06      3.500000      1.000000   \n",
              "\n",
              "                view  ...         grade    sqft_above  sqft_basement  \\\n",
              "count   21613.000000  ...  21613.000000  21613.000000   21613.000000   \n",
              "unique           NaN  ...           NaN           NaN            NaN   \n",
              "top              NaN  ...           NaN           NaN            NaN   \n",
              "freq             NaN  ...           NaN           NaN            NaN   \n",
              "mean        0.234303  ...      7.656873   1788.390691     291.509045   \n",
              "std         0.766318  ...      1.175459    828.090978     442.575043   \n",
              "min         0.000000  ...      1.000000    290.000000       0.000000   \n",
              "25%         0.000000  ...      7.000000   1190.000000       0.000000   \n",
              "50%         0.000000  ...      7.000000   1560.000000       0.000000   \n",
              "75%         0.000000  ...      8.000000   2210.000000     560.000000   \n",
              "max         4.000000  ...     13.000000   9410.000000    4820.000000   \n",
              "\n",
              "            yr_built  yr_renovated       zipcode           lat          long  \\\n",
              "count   21613.000000  21613.000000  21613.000000  21613.000000  21613.000000   \n",
              "unique           NaN           NaN           NaN           NaN           NaN   \n",
              "top              NaN           NaN           NaN           NaN           NaN   \n",
              "freq             NaN           NaN           NaN           NaN           NaN   \n",
              "mean     1971.005136     84.402258  98077.939805     47.560053   -122.213896   \n",
              "std        29.373411    401.679240     53.505026      0.138564      0.140828   \n",
              "min      1900.000000      0.000000  98001.000000     47.155900   -122.519000   \n",
              "25%      1951.000000      0.000000  98033.000000     47.471000   -122.328000   \n",
              "50%      1975.000000      0.000000  98065.000000     47.571800   -122.230000   \n",
              "75%      1997.000000      0.000000  98118.000000     47.678000   -122.125000   \n",
              "max      2015.000000   2015.000000  98199.000000     47.777600   -121.315000   \n",
              "\n",
              "        sqft_living15     sqft_lot15  \n",
              "count    21613.000000   21613.000000  \n",
              "unique            NaN            NaN  \n",
              "top               NaN            NaN  \n",
              "freq              NaN            NaN  \n",
              "mean      1986.552492   12768.455652  \n",
              "std        685.391304   27304.179631  \n",
              "min        399.000000     651.000000  \n",
              "25%       1490.000000    5100.000000  \n",
              "50%       1840.000000    7620.000000  \n",
              "75%       2360.000000   10083.000000  \n",
              "max       6210.000000  871200.000000  \n",
              "\n",
              "[11 rows x 21 columns]"
            ],
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>id</th>\n      <th>date</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>...</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>2.161300e+04</td>\n      <td>21613</td>\n      <td>2.161300e+04</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>2.161300e+04</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>...</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n    </tr>\n    <tr>\n      <th>unique</th>\n      <td>NaN</td>\n      <td>372</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>...</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>top</th>\n      <td>NaN</td>\n      <td>20140623T000000</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>...</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>freq</th>\n      <td>NaN</td>\n      <td>142</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>...</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>4.580302e+09</td>\n      <td>NaN</td>\n      <td>5.400881e+05</td>\n      <td>3.370842</td>\n      <td>2.114757</td>\n      <td>2079.899736</td>\n      <td>1.510697e+04</td>\n      <td>1.494309</td>\n      <td>0.007542</td>\n      <td>0.234303</td>\n      <td>...</td>\n      <td>7.656873</td>\n      <td>1788.390691</td>\n      <td>291.509045</td>\n      <td>1971.005136</td>\n      <td>84.402258</td>\n      <td>98077.939805</td>\n      <td>47.560053</td>\n      <td>-122.213896</td>\n      <td>1986.552492</td>\n      <td>12768.455652</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>2.876566e+09</td>\n      <td>NaN</td>\n      <td>3.671272e+05</td>\n      <td>0.930062</td>\n      <td>0.770163</td>\n      <td>918.440897</td>\n      <td>4.142051e+04</td>\n      <td>0.539989</td>\n      <td>0.086517</td>\n      <td>0.766318</td>\n      <td>...</td>\n      <td>1.175459</td>\n      <td>828.090978</td>\n      <td>442.575043</td>\n      <td>29.373411</td>\n      <td>401.679240</td>\n      <td>53.505026</td>\n      <td>0.138564</td>\n      <td>0.140828</td>\n      <td>685.391304</td>\n      <td>27304.179631</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>1.000102e+06</td>\n      <td>NaN</td>\n      <td>7.500000e+04</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>290.000000</td>\n      <td>5.200000e+02</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>1.000000</td>\n      <td>290.000000</td>\n      <td>0.000000</td>\n      <td>1900.000000</td>\n      <td>0.000000</td>\n      <td>98001.000000</td>\n      <td>47.155900</td>\n      <td>-122.519000</td>\n      <td>399.000000</td>\n      <td>651.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>2.123049e+09</td>\n      <td>NaN</td>\n      <td>3.219500e+05</td>\n      <td>3.000000</td>\n      <td>1.750000</td>\n      <td>1427.000000</td>\n      <td>5.040000e+03</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>7.000000</td>\n      <td>1190.000000</td>\n      <td>0.000000</td>\n      <td>1951.000000</td>\n      <td>0.000000</td>\n      <td>98033.000000</td>\n      <td>47.471000</td>\n      <td>-122.328000</td>\n      <td>1490.000000</td>\n      <td>5100.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>3.904930e+09</td>\n      <td>NaN</td>\n      <td>4.500000e+05</td>\n      <td>3.000000</td>\n      <td>2.250000</td>\n      <td>1910.000000</td>\n      <td>7.618000e+03</td>\n      <td>1.500000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>7.000000</td>\n      <td>1560.000000</td>\n      <td>0.000000</td>\n      <td>1975.000000</td>\n      <td>0.000000</td>\n      <td>98065.000000</td>\n      <td>47.571800</td>\n      <td>-122.230000</td>\n      <td>1840.000000</td>\n      <td>7620.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>7.308900e+09</td>\n      <td>NaN</td>\n      <td>6.450000e+05</td>\n      <td>4.000000</td>\n      <td>2.500000</td>\n      <td>2550.000000</td>\n      <td>1.068800e+04</td>\n      <td>2.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>8.000000</td>\n      <td>2210.000000</td>\n      <td>560.000000</td>\n      <td>1997.000000</td>\n      <td>0.000000</td>\n      <td>98118.000000</td>\n      <td>47.678000</td>\n      <td>-122.125000</td>\n      <td>2360.000000</td>\n      <td>10083.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>9.900000e+09</td>\n      <td>NaN</td>\n      <td>7.700000e+06</td>\n      <td>33.000000</td>\n      <td>8.000000</td>\n      <td>13540.000000</td>\n      <td>1.651359e+06</td>\n      <td>3.500000</td>\n      <td>1.000000</td>\n      <td>4.000000</td>\n      <td>...</td>\n      <td>13.000000</td>\n      <td>9410.000000</td>\n      <td>4820.000000</td>\n      <td>2015.000000</td>\n      <td>2015.000000</td>\n      <td>98199.000000</td>\n      <td>47.777600</td>\n      <td>-121.315000</td>\n      <td>6210.000000</td>\n      <td>871200.000000</td>\n    </tr>\n  </tbody>\n</table>\n<p>11 rows × 21 columns</p>\n</div>"
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KKrq8f_OiD3K"
      },
      "source": [
        "### 7. Use sort_values to get the top 20 houses by price"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DNiL44-YiL2e"
      },
      "source": [
        "my_dataframe.sort_values(by=['price'], ascending=False).head(20) #7700000.0"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "               id             date      price  bedrooms  bathrooms  \\\n",
              "7252   6762700020  20141013T000000  7700000.0         6       8.00   \n",
              "3914   9808700762  20140611T000000  7062500.0         5       4.50   \n",
              "9254   9208900037  20140919T000000  6885000.0         6       7.75   \n",
              "4411   2470100110  20140804T000000  5570000.0         5       5.75   \n",
              "1448   8907500070  20150413T000000  5350000.0         5       5.00   \n",
              "1315   7558700030  20150413T000000  5300000.0         6       6.00   \n",
              "1164   1247600105  20141020T000000  5110800.0         5       5.25   \n",
              "8092   1924059029  20140617T000000  4668000.0         5       6.75   \n",
              "2626   7738500731  20140815T000000  4500000.0         5       5.50   \n",
              "8638   3835500195  20140618T000000  4489000.0         4       3.00   \n",
              "12370  6065300370  20150506T000000  4208000.0         5       6.00   \n",
              "4149   6447300265  20141014T000000  4000000.0         4       5.50   \n",
              "2085   8106100105  20141114T000000  3850000.0         4       4.25   \n",
              "19017  2303900100  20140911T000000  3800000.0         3       4.25   \n",
              "7035    853200010  20140701T000000  3800000.0         5       5.50   \n",
              "16302  7397300170  20140530T000000  3710000.0         4       3.50   \n",
              "6508   4217402115  20150421T000000  3650000.0         6       4.75   \n",
              "18482  4389201095  20150511T000000  3650000.0         5       3.75   \n",
              "15255  2425049063  20140911T000000  3640900.0         4       3.25   \n",
              "19148  3625049042  20141011T000000  3635000.0         5       6.00   \n",
              "\n",
              "       sqft_living  sqft_lot  floors  waterfront  view  ...  grade  \\\n",
              "7252         12050     27600     2.5           0     3  ...     13   \n",
              "3914         10040     37325     2.0           1     2  ...     11   \n",
              "9254          9890     31374     2.0           0     4  ...     13   \n",
              "4411          9200     35069     2.0           0     0  ...     13   \n",
              "1448          8000     23985     2.0           0     4  ...     12   \n",
              "1315          7390     24829     2.0           1     4  ...     12   \n",
              "1164          8010     45517     2.0           1     4  ...     12   \n",
              "8092          9640     13068     1.0           1     4  ...     12   \n",
              "2626          6640     40014     2.0           1     4  ...     12   \n",
              "8638          6430     27517     2.0           0     0  ...     12   \n",
              "12370         7440     21540     2.0           0     0  ...     12   \n",
              "4149          7080     16573     2.0           0     0  ...     12   \n",
              "2085          5770     21300     2.0           1     4  ...     11   \n",
              "19017         5510     35000     2.0           0     4  ...     13   \n",
              "7035          7050     42840     1.0           0     2  ...     13   \n",
              "16302         5550     28078     2.0           0     2  ...     12   \n",
              "6508          5480     19401     1.5           1     4  ...     11   \n",
              "18482         5020      8694     2.0           0     1  ...     12   \n",
              "15255         4830     22257     2.0           1     4  ...     11   \n",
              "19148         5490     19897     2.0           0     0  ...     12   \n",
              "\n",
              "       sqft_above  sqft_basement  yr_built  yr_renovated  zipcode      lat  \\\n",
              "7252         8570           3480      1910          1987    98102  47.6298   \n",
              "3914         7680           2360      1940          2001    98004  47.6500   \n",
              "9254         8860           1030      2001             0    98039  47.6305   \n",
              "4411         6200           3000      2001             0    98039  47.6289   \n",
              "1448         6720           1280      2009             0    98004  47.6232   \n",
              "1315         5000           2390      1991             0    98040  47.5631   \n",
              "1164         5990           2020      1999             0    98033  47.6767   \n",
              "8092         4820           4820      1983          2009    98040  47.5570   \n",
              "2626         6350            290      2004             0    98155  47.7493   \n",
              "8638         6430              0      2001             0    98004  47.6208   \n",
              "12370        5550           1890      2003             0    98006  47.5692   \n",
              "4149         5760           1320      2008             0    98039  47.6151   \n",
              "2085         5770              0      1980             0    98040  47.5850   \n",
              "19017        4910            600      1997             0    98177  47.7296   \n",
              "7035         4320           2730      1978             0    98004  47.6229   \n",
              "16302        3350           2200      2000             0    98039  47.6395   \n",
              "6508         3910           1570      1936             0    98105  47.6515   \n",
              "18482        3970           1050      2007             0    98004  47.6146   \n",
              "15255        4830              0      1990             0    98039  47.6409   \n",
              "19148        5490              0      2005             0    98039  47.6165   \n",
              "\n",
              "          long  sqft_living15  sqft_lot15  \n",
              "7252  -122.323           3940        8800  \n",
              "3914  -122.214           3930       25449  \n",
              "9254  -122.240           4540       42730  \n",
              "4411  -122.233           3560       24345  \n",
              "1448  -122.220           4600       21750  \n",
              "1315  -122.210           4320       24619  \n",
              "1164  -122.211           3430       26788  \n",
              "8092  -122.210           3270       10454  \n",
              "2626  -122.280           3030       23408  \n",
              "8638  -122.219           3720       14592  \n",
              "12370 -122.189           4740       19329  \n",
              "4149  -122.224           3140       15996  \n",
              "2085  -122.222           4620       22748  \n",
              "19017 -122.370           3430       45302  \n",
              "7035  -122.220           5070       20570  \n",
              "16302 -122.234           2980       19602  \n",
              "6508  -122.277           3510       15810  \n",
              "18482 -122.213           4190       11275  \n",
              "15255 -122.241           3820       25582  \n",
              "19148 -122.236           2910       17600  \n",
              "\n",
              "[20 rows x 21 columns]"
            ],
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>id</th>\n      <th>date</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>...</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>7252</th>\n      <td>6762700020</td>\n      <td>20141013T000000</td>\n      <td>7700000.0</td>\n      <td>6</td>\n      <td>8.00</td>\n      <td>12050</td>\n      <td>27600</td>\n      <td>2.5</td>\n      <td>0</td>\n      <td>3</td>\n      <td>...</td>\n      <td>13</td>\n      <td>8570</td>\n      <td>3480</td>\n      <td>1910</td>\n      <td>1987</td>\n      <td>98102</td>\n      <td>47.6298</td>\n      <td>-122.323</td>\n      <td>3940</td>\n      <td>8800</td>\n    </tr>\n    <tr>\n      <th>3914</th>\n      <td>9808700762</td>\n      <td>20140611T000000</td>\n      <td>7062500.0</td>\n      <td>5</td>\n      <td>4.50</td>\n      <td>10040</td>\n      <td>37325</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>2</td>\n      <td>...</td>\n      <td>11</td>\n      <td>7680</td>\n      <td>2360</td>\n      <td>1940</td>\n      <td>2001</td>\n      <td>98004</td>\n      <td>47.6500</td>\n      <td>-122.214</td>\n      <td>3930</td>\n      <td>25449</td>\n    </tr>\n    <tr>\n      <th>9254</th>\n      <td>9208900037</td>\n      <td>20140919T000000</td>\n      <td>6885000.0</td>\n      <td>6</td>\n      <td>7.75</td>\n      <td>9890</td>\n      <td>31374</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>4</td>\n      <td>...</td>\n      <td>13</td>\n      <td>8860</td>\n      <td>1030</td>\n      <td>2001</td>\n      <td>0</td>\n      <td>98039</td>\n      <td>47.6305</td>\n      <td>-122.240</td>\n      <td>4540</td>\n      <td>42730</td>\n    </tr>\n    <tr>\n      <th>4411</th>\n      <td>2470100110</td>\n      <td>20140804T000000</td>\n      <td>5570000.0</td>\n      <td>5</td>\n      <td>5.75</td>\n      <td>9200</td>\n      <td>35069</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>13</td>\n      <td>6200</td>\n      <td>3000</td>\n      <td>2001</td>\n      <td>0</td>\n      <td>98039</td>\n      <td>47.6289</td>\n      <td>-122.233</td>\n      <td>3560</td>\n      <td>24345</td>\n    </tr>\n    <tr>\n      <th>1448</th>\n      <td>8907500070</td>\n      <td>20150413T000000</td>\n      <td>5350000.0</td>\n      <td>5</td>\n      <td>5.00</td>\n      <td>8000</td>\n      <td>23985</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>6720</td>\n      <td>1280</td>\n      <td>2009</td>\n      <td>0</td>\n      <td>98004</td>\n      <td>47.6232</td>\n      <td>-122.220</td>\n      <td>4600</td>\n      <td>21750</td>\n    </tr>\n    <tr>\n      <th>1315</th>\n      <td>7558700030</td>\n      <td>20150413T000000</td>\n      <td>5300000.0</td>\n      <td>6</td>\n      <td>6.00</td>\n      <td>7390</td>\n      <td>24829</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>5000</td>\n      <td>2390</td>\n      <td>1991</td>\n      <td>0</td>\n      <td>98040</td>\n      <td>47.5631</td>\n      <td>-122.210</td>\n      <td>4320</td>\n      <td>24619</td>\n    </tr>\n    <tr>\n      <th>1164</th>\n      <td>1247600105</td>\n      <td>20141020T000000</td>\n      <td>5110800.0</td>\n      <td>5</td>\n      <td>5.25</td>\n      <td>8010</td>\n      <td>45517</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>5990</td>\n      <td>2020</td>\n      <td>1999</td>\n      <td>0</td>\n      <td>98033</td>\n      <td>47.6767</td>\n      <td>-122.211</td>\n      <td>3430</td>\n      <td>26788</td>\n    </tr>\n    <tr>\n      <th>8092</th>\n      <td>1924059029</td>\n      <td>20140617T000000</td>\n      <td>4668000.0</td>\n      <td>5</td>\n      <td>6.75</td>\n      <td>9640</td>\n      <td>13068</td>\n      <td>1.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>4820</td>\n      <td>4820</td>\n      <td>1983</td>\n      <td>2009</td>\n      <td>98040</td>\n      <td>47.5570</td>\n      <td>-122.210</td>\n      <td>3270</td>\n      <td>10454</td>\n    </tr>\n    <tr>\n      <th>2626</th>\n      <td>7738500731</td>\n      <td>20140815T000000</td>\n      <td>4500000.0</td>\n      <td>5</td>\n      <td>5.50</td>\n      <td>6640</td>\n      <td>40014</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>6350</td>\n      <td>290</td>\n      <td>2004</td>\n      <td>0</td>\n      <td>98155</td>\n      <td>47.7493</td>\n      <td>-122.280</td>\n      <td>3030</td>\n      <td>23408</td>\n    </tr>\n    <tr>\n      <th>8638</th>\n      <td>3835500195</td>\n      <td>20140618T000000</td>\n      <td>4489000.0</td>\n      <td>4</td>\n      <td>3.00</td>\n      <td>6430</td>\n      <td>27517</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>12</td>\n      <td>6430</td>\n      <td>0</td>\n      <td>2001</td>\n      <td>0</td>\n      <td>98004</td>\n      <td>47.6208</td>\n      <td>-122.219</td>\n      <td>3720</td>\n      <td>14592</td>\n    </tr>\n    <tr>\n      <th>12370</th>\n      <td>6065300370</td>\n      <td>20150506T000000</td>\n      <td>4208000.0</td>\n      <td>5</td>\n      <td>6.00</td>\n      <td>7440</td>\n      <td>21540</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>12</td>\n      <td>5550</td>\n      <td>1890</td>\n      <td>2003</td>\n      <td>0</td>\n      <td>98006</td>\n      <td>47.5692</td>\n      <td>-122.189</td>\n      <td>4740</td>\n      <td>19329</td>\n    </tr>\n    <tr>\n      <th>4149</th>\n      <td>6447300265</td>\n      <td>20141014T000000</td>\n      <td>4000000.0</td>\n      <td>4</td>\n      <td>5.50</td>\n      <td>7080</td>\n      <td>16573</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>12</td>\n      <td>5760</td>\n      <td>1320</td>\n      <td>2008</td>\n      <td>0</td>\n      <td>98039</td>\n      <td>47.6151</td>\n      <td>-122.224</td>\n      <td>3140</td>\n      <td>15996</td>\n    </tr>\n    <tr>\n      <th>2085</th>\n      <td>8106100105</td>\n      <td>20141114T000000</td>\n      <td>3850000.0</td>\n      <td>4</td>\n      <td>4.25</td>\n      <td>5770</td>\n      <td>21300</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>11</td>\n      <td>5770</td>\n      <td>0</td>\n      <td>1980</td>\n      <td>0</td>\n      <td>98040</td>\n      <td>47.5850</td>\n      <td>-122.222</td>\n      <td>4620</td>\n      <td>22748</td>\n    </tr>\n    <tr>\n      <th>19017</th>\n      <td>2303900100</td>\n      <td>20140911T000000</td>\n      <td>3800000.0</td>\n      <td>3</td>\n      <td>4.25</td>\n      <td>5510</td>\n      <td>35000</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>4</td>\n      <td>...</td>\n      <td>13</td>\n      <td>4910</td>\n      <td>600</td>\n      <td>1997</td>\n      <td>0</td>\n      <td>98177</td>\n      <td>47.7296</td>\n      <td>-122.370</td>\n      <td>3430</td>\n      <td>45302</td>\n    </tr>\n    <tr>\n      <th>7035</th>\n      <td>853200010</td>\n      <td>20140701T000000</td>\n      <td>3800000.0</td>\n      <td>5</td>\n      <td>5.50</td>\n      <td>7050</td>\n      <td>42840</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>2</td>\n      <td>...</td>\n      <td>13</td>\n      <td>4320</td>\n      <td>2730</td>\n      <td>1978</td>\n      <td>0</td>\n      <td>98004</td>\n      <td>47.6229</td>\n      <td>-122.220</td>\n      <td>5070</td>\n      <td>20570</td>\n    </tr>\n    <tr>\n      <th>16302</th>\n      <td>7397300170</td>\n      <td>20140530T000000</td>\n      <td>3710000.0</td>\n      <td>4</td>\n      <td>3.50</td>\n      <td>5550</td>\n      <td>28078</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>2</td>\n      <td>...</td>\n      <td>12</td>\n      <td>3350</td>\n      <td>2200</td>\n      <td>2000</td>\n      <td>0</td>\n      <td>98039</td>\n      <td>47.6395</td>\n      <td>-122.234</td>\n      <td>2980</td>\n      <td>19602</td>\n    </tr>\n    <tr>\n      <th>6508</th>\n      <td>4217402115</td>\n      <td>20150421T000000</td>\n      <td>3650000.0</td>\n      <td>6</td>\n      <td>4.75</td>\n      <td>5480</td>\n      <td>19401</td>\n      <td>1.5</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>11</td>\n      <td>3910</td>\n      <td>1570</td>\n      <td>1936</td>\n      <td>0</td>\n      <td>98105</td>\n      <td>47.6515</td>\n      <td>-122.277</td>\n      <td>3510</td>\n      <td>15810</td>\n    </tr>\n    <tr>\n      <th>18482</th>\n      <td>4389201095</td>\n      <td>20150511T000000</td>\n      <td>3650000.0</td>\n      <td>5</td>\n      <td>3.75</td>\n      <td>5020</td>\n      <td>8694</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>...</td>\n      <td>12</td>\n      <td>3970</td>\n      <td>1050</td>\n      <td>2007</td>\n      <td>0</td>\n      <td>98004</td>\n      <td>47.6146</td>\n      <td>-122.213</td>\n      <td>4190</td>\n      <td>11275</td>\n    </tr>\n    <tr>\n      <th>15255</th>\n      <td>2425049063</td>\n      <td>20140911T000000</td>\n      <td>3640900.0</td>\n      <td>4</td>\n      <td>3.25</td>\n      <td>4830</td>\n      <td>22257</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>11</td>\n      <td>4830</td>\n      <td>0</td>\n      <td>1990</td>\n      <td>0</td>\n      <td>98039</td>\n      <td>47.6409</td>\n      <td>-122.241</td>\n      <td>3820</td>\n      <td>25582</td>\n    </tr>\n    <tr>\n      <th>19148</th>\n      <td>3625049042</td>\n      <td>20141011T000000</td>\n      <td>3635000.0</td>\n      <td>5</td>\n      <td>6.00</td>\n      <td>5490</td>\n      <td>19897</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>12</td>\n      <td>5490</td>\n      <td>0</td>\n      <td>2005</td>\n      <td>0</td>\n      <td>98039</td>\n      <td>47.6165</td>\n      <td>-122.236</td>\n      <td>2910</td>\n      <td>17600</td>\n    </tr>\n  </tbody>\n</table>\n<p>20 rows × 21 columns</p>\n</div>"
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "q10hrDpliMZI"
      },
      "source": [
        "### 8. Select all rows and columns (id, price, bedrooms, sqft_living) and display it below"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0Xx2UaNLiQmR"
      },
      "source": [
        "my_dataframe_new = my_dataframe[[\"id\",\"price\",\"bedrooms\", \"sqft_living\"]]\n",
        "print(my_dataframe_new)"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "               id     price  bedrooms  sqft_living\n0      7129300520  221900.0         3         1180\n1      6414100192  538000.0         3         2570\n2      5631500400  180000.0         2          770\n3      2487200875  604000.0         4         1960\n4      1954400510  510000.0         3         1680\n...           ...       ...       ...          ...\n21608   263000018  360000.0         3         1530\n21609  6600060120  400000.0         4         2310\n21610  1523300141  402101.0         2         1020\n21611   291310100  400000.0         3         1600\n21612  1523300157  325000.0         2         1020\n\n[21613 rows x 4 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YE8ZMwQGiQ9n"
      },
      "source": [
        "### 9. Find the most expensive 10 houses with the highest number of sqft_living"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cpsqGJijiVW9"
      },
      "source": [
        "my_dataframe.sort_values(by=['price','sqft_living'], ascending=False).head(10)"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              id             date      price  bedrooms  bathrooms  \\\n",
              "7252  6762700020  20141013T000000  7700000.0         6       8.00   \n",
              "3914  9808700762  20140611T000000  7062500.0         5       4.50   \n",
              "9254  9208900037  20140919T000000  6885000.0         6       7.75   \n",
              "4411  2470100110  20140804T000000  5570000.0         5       5.75   \n",
              "1448  8907500070  20150413T000000  5350000.0         5       5.00   \n",
              "1315  7558700030  20150413T000000  5300000.0         6       6.00   \n",
              "1164  1247600105  20141020T000000  5110800.0         5       5.25   \n",
              "8092  1924059029  20140617T000000  4668000.0         5       6.75   \n",
              "2626  7738500731  20140815T000000  4500000.0         5       5.50   \n",
              "8638  3835500195  20140618T000000  4489000.0         4       3.00   \n",
              "\n",
              "      sqft_living  sqft_lot  floors  waterfront  view  ...  grade  sqft_above  \\\n",
              "7252        12050     27600     2.5           0     3  ...     13        8570   \n",
              "3914        10040     37325     2.0           1     2  ...     11        7680   \n",
              "9254         9890     31374     2.0           0     4  ...     13        8860   \n",
              "4411         9200     35069     2.0           0     0  ...     13        6200   \n",
              "1448         8000     23985     2.0           0     4  ...     12        6720   \n",
              "1315         7390     24829     2.0           1     4  ...     12        5000   \n",
              "1164         8010     45517     2.0           1     4  ...     12        5990   \n",
              "8092         9640     13068     1.0           1     4  ...     12        4820   \n",
              "2626         6640     40014     2.0           1     4  ...     12        6350   \n",
              "8638         6430     27517     2.0           0     0  ...     12        6430   \n",
              "\n",
              "      sqft_basement  yr_built  yr_renovated  zipcode      lat     long  \\\n",
              "7252           3480      1910          1987    98102  47.6298 -122.323   \n",
              "3914           2360      1940          2001    98004  47.6500 -122.214   \n",
              "9254           1030      2001             0    98039  47.6305 -122.240   \n",
              "4411           3000      2001             0    98039  47.6289 -122.233   \n",
              "1448           1280      2009             0    98004  47.6232 -122.220   \n",
              "1315           2390      1991             0    98040  47.5631 -122.210   \n",
              "1164           2020      1999             0    98033  47.6767 -122.211   \n",
              "8092           4820      1983          2009    98040  47.5570 -122.210   \n",
              "2626            290      2004             0    98155  47.7493 -122.280   \n",
              "8638              0      2001             0    98004  47.6208 -122.219   \n",
              "\n",
              "      sqft_living15  sqft_lot15  \n",
              "7252           3940        8800  \n",
              "3914           3930       25449  \n",
              "9254           4540       42730  \n",
              "4411           3560       24345  \n",
              "1448           4600       21750  \n",
              "1315           4320       24619  \n",
              "1164           3430       26788  \n",
              "8092           3270       10454  \n",
              "2626           3030       23408  \n",
              "8638           3720       14592  \n",
              "\n",
              "[10 rows x 21 columns]"
            ],
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>id</th>\n      <th>date</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>...</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>7252</th>\n      <td>6762700020</td>\n      <td>20141013T000000</td>\n      <td>7700000.0</td>\n      <td>6</td>\n      <td>8.00</td>\n      <td>12050</td>\n      <td>27600</td>\n      <td>2.5</td>\n      <td>0</td>\n      <td>3</td>\n      <td>...</td>\n      <td>13</td>\n      <td>8570</td>\n      <td>3480</td>\n      <td>1910</td>\n      <td>1987</td>\n      <td>98102</td>\n      <td>47.6298</td>\n      <td>-122.323</td>\n      <td>3940</td>\n      <td>8800</td>\n    </tr>\n    <tr>\n      <th>3914</th>\n      <td>9808700762</td>\n      <td>20140611T000000</td>\n      <td>7062500.0</td>\n      <td>5</td>\n      <td>4.50</td>\n      <td>10040</td>\n      <td>37325</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>2</td>\n      <td>...</td>\n      <td>11</td>\n      <td>7680</td>\n      <td>2360</td>\n      <td>1940</td>\n      <td>2001</td>\n      <td>98004</td>\n      <td>47.6500</td>\n      <td>-122.214</td>\n      <td>3930</td>\n      <td>25449</td>\n    </tr>\n    <tr>\n      <th>9254</th>\n      <td>9208900037</td>\n      <td>20140919T000000</td>\n      <td>6885000.0</td>\n      <td>6</td>\n      <td>7.75</td>\n      <td>9890</td>\n      <td>31374</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>4</td>\n      <td>...</td>\n      <td>13</td>\n      <td>8860</td>\n      <td>1030</td>\n      <td>2001</td>\n      <td>0</td>\n      <td>98039</td>\n      <td>47.6305</td>\n      <td>-122.240</td>\n      <td>4540</td>\n      <td>42730</td>\n    </tr>\n    <tr>\n      <th>4411</th>\n      <td>2470100110</td>\n      <td>20140804T000000</td>\n      <td>5570000.0</td>\n      <td>5</td>\n      <td>5.75</td>\n      <td>9200</td>\n      <td>35069</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>13</td>\n      <td>6200</td>\n      <td>3000</td>\n      <td>2001</td>\n      <td>0</td>\n      <td>98039</td>\n      <td>47.6289</td>\n      <td>-122.233</td>\n      <td>3560</td>\n      <td>24345</td>\n    </tr>\n    <tr>\n      <th>1448</th>\n      <td>8907500070</td>\n      <td>20150413T000000</td>\n      <td>5350000.0</td>\n      <td>5</td>\n      <td>5.00</td>\n      <td>8000</td>\n      <td>23985</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>6720</td>\n      <td>1280</td>\n      <td>2009</td>\n      <td>0</td>\n      <td>98004</td>\n      <td>47.6232</td>\n      <td>-122.220</td>\n      <td>4600</td>\n      <td>21750</td>\n    </tr>\n    <tr>\n      <th>1315</th>\n      <td>7558700030</td>\n      <td>20150413T000000</td>\n      <td>5300000.0</td>\n      <td>6</td>\n      <td>6.00</td>\n      <td>7390</td>\n      <td>24829</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>5000</td>\n      <td>2390</td>\n      <td>1991</td>\n      <td>0</td>\n      <td>98040</td>\n      <td>47.5631</td>\n      <td>-122.210</td>\n      <td>4320</td>\n      <td>24619</td>\n    </tr>\n    <tr>\n      <th>1164</th>\n      <td>1247600105</td>\n      <td>20141020T000000</td>\n      <td>5110800.0</td>\n      <td>5</td>\n      <td>5.25</td>\n      <td>8010</td>\n      <td>45517</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>5990</td>\n      <td>2020</td>\n      <td>1999</td>\n      <td>0</td>\n      <td>98033</td>\n      <td>47.6767</td>\n      <td>-122.211</td>\n      <td>3430</td>\n      <td>26788</td>\n    </tr>\n    <tr>\n      <th>8092</th>\n      <td>1924059029</td>\n      <td>20140617T000000</td>\n      <td>4668000.0</td>\n      <td>5</td>\n      <td>6.75</td>\n      <td>9640</td>\n      <td>13068</td>\n      <td>1.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>4820</td>\n      <td>4820</td>\n      <td>1983</td>\n      <td>2009</td>\n      <td>98040</td>\n      <td>47.5570</td>\n      <td>-122.210</td>\n      <td>3270</td>\n      <td>10454</td>\n    </tr>\n    <tr>\n      <th>2626</th>\n      <td>7738500731</td>\n      <td>20140815T000000</td>\n      <td>4500000.0</td>\n      <td>5</td>\n      <td>5.50</td>\n      <td>6640</td>\n      <td>40014</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>12</td>\n      <td>6350</td>\n      <td>290</td>\n      <td>2004</td>\n      <td>0</td>\n      <td>98155</td>\n      <td>47.7493</td>\n      <td>-122.280</td>\n      <td>3030</td>\n      <td>23408</td>\n    </tr>\n    <tr>\n      <th>8638</th>\n      <td>3835500195</td>\n      <td>20140618T000000</td>\n      <td>4489000.0</td>\n      <td>4</td>\n      <td>3.00</td>\n      <td>6430</td>\n      <td>27517</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>12</td>\n      <td>6430</td>\n      <td>0</td>\n      <td>2001</td>\n      <td>0</td>\n      <td>98004</td>\n      <td>47.6208</td>\n      <td>-122.219</td>\n      <td>3720</td>\n      <td>14592</td>\n    </tr>\n  </tbody>\n</table>\n<p>10 rows × 21 columns</p>\n</div>"
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3SBCSR_nianx"
      },
      "source": [
        "### 10. Find the average price for different number of bedrooms?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rcD4Qfvsib3W"
      },
      "source": [
        "my_dataframe.groupby('bedrooms')['price'].agg(['mean'])"
      ],
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                  mean\n",
              "bedrooms              \n",
              "0         4.095038e+05\n",
              "1         3.176429e+05\n",
              "2         4.013727e+05\n",
              "3         4.662321e+05\n",
              "4         6.354195e+05\n",
              "5         7.865998e+05\n",
              "6         8.255206e+05\n",
              "7         9.511847e+05\n",
              "8         1.105077e+06\n",
              "9         8.939998e+05\n",
              "10        8.193333e+05\n",
              "11        5.200000e+05\n",
              "33        6.400000e+05"
            ],
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>mean</th>\n    </tr>\n    <tr>\n      <th>bedrooms</th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>4.095038e+05</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>3.176429e+05</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>4.013727e+05</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>4.662321e+05</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>6.354195e+05</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>7.865998e+05</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>8.255206e+05</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>9.511847e+05</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>1.105077e+06</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>8.939998e+05</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>8.193333e+05</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>5.200000e+05</td>\n    </tr>\n    <tr>\n      <th>33</th>\n      <td>6.400000e+05</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {},
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ypYfA0ndicMm"
      },
      "source": [
        "### 11. Create a new column (sqft_price) in Pandas DataFrame based on the existing columns (price, sqft_lot). Calculate sqft_price with formula price/sqft_lot and fill result for each row."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WqwHuDaDo59F"
      },
      "source": [
        "my_dataframe['sqft_price'] = my_dataframe['price'] / my_dataframe['sqft_lot']\n",
        "print(my_dataframe)"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "               id             date     price  bedrooms  bathrooms  \\\n0      7129300520  20141013T000000  221900.0         3       1.00   \n1      6414100192  20141209T000000  538000.0         3       2.25   \n2      5631500400  20150225T000000  180000.0         2       1.00   \n3      2487200875  20141209T000000  604000.0         4       3.00   \n4      1954400510  20150218T000000  510000.0         3       2.00   \n...           ...              ...       ...       ...        ...   \n21608   263000018  20140521T000000  360000.0         3       2.50   \n21609  6600060120  20150223T000000  400000.0         4       2.50   \n21610  1523300141  20140623T000000  402101.0         2       0.75   \n21611   291310100  20150116T000000  400000.0         3       2.50   \n21612  1523300157  20141015T000000  325000.0         2       0.75   \n\n       sqft_living  sqft_lot  floors  waterfront  view  ...  sqft_above  \\\n0             1180      5650     1.0           0     0  ...        1180   \n1             2570      7242     2.0           0     0  ...        2170   \n2              770     10000     1.0           0     0  ...         770   \n3             1960      5000     1.0           0     0  ...        1050   \n4             1680      8080     1.0           0     0  ...        1680   \n...            ...       ...     ...         ...   ...  ...         ...   \n21608         1530      1131     3.0           0     0  ...        1530   \n21609         2310      5813     2.0           0     0  ...        2310   \n21610         1020      1350     2.0           0     0  ...        1020   \n21611         1600      2388     2.0           0     0  ...        1600   \n21612         1020      1076     2.0           0     0  ...        1020   \n\n       sqft_basement  yr_built  yr_renovated  zipcode      lat     long  \\\n0                  0      1955             0    98178  47.5112 -122.257   \n1                400      1951          1991    98125  47.7210 -122.319   \n2                  0      1933             0    98028  47.7379 -122.233   \n3                910      1965             0    98136  47.5208 -122.393   \n4                  0      1987             0    98074  47.6168 -122.045   \n...              ...       ...           ...      ...      ...      ...   \n21608              0      2009             0    98103  47.6993 -122.346   \n21609              0      2014             0    98146  47.5107 -122.362   \n21610              0      2009             0    98144  47.5944 -122.299   \n21611              0      2004             0    98027  47.5345 -122.069   \n21612              0      2008             0    98144  47.5941 -122.299   \n\n       sqft_living15  sqft_lot15  sqft_price  \n0               1340        5650   39.274336  \n1               1690        7639   74.288870  \n2               2720        8062   18.000000  \n3               1360        5000  120.800000  \n4               1800        7503   63.118812  \n...              ...         ...         ...  \n21608           1530        1509  318.302387  \n21609           1830        7200   68.811285  \n21610           1020        2007  297.852593  \n21611           1410        1287  167.504188  \n21612           1020        1357  302.044610  \n\n[21613 rows x 22 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XuZjz--ho8rV"
      },
      "source": [
        "### 12. Define average value for every sqft_living via price average and count"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IyR89YJ4o87h"
      },
      "source": [
        "my_dataframe.groupby('sqft_living')['price'].agg(['count','mean']).sort_values(by=['sqft_living'], ascending=False).head(250)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             count          mean\n",
              "sqft_living                     \n",
              "13540            1  2.280000e+06\n",
              "12050            1  7.700000e+06\n",
              "10040            1  7.062500e+06\n",
              "9890             1  6.885000e+06\n",
              "9640             1  4.668000e+06\n",
              "...            ...           ...\n",
              "4083             1  6.370000e+05\n",
              "4080             7  1.166714e+06\n",
              "4073             1  5.100000e+05\n",
              "4070            10  1.273450e+06\n",
              "4065             1  1.950000e+06\n",
              "\n",
              "[250 rows x 2 columns]"
            ],
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>count</th>\n      <th>mean</th>\n    </tr>\n    <tr>\n      <th>sqft_living</th>\n      <th></th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>13540</th>\n      <td>1</td>\n      <td>2.280000e+06</td>\n    </tr>\n    <tr>\n      <th>12050</th>\n      <td>1</td>\n      <td>7.700000e+06</td>\n    </tr>\n    <tr>\n      <th>10040</th>\n      <td>1</td>\n      <td>7.062500e+06</td>\n    </tr>\n    <tr>\n      <th>9890</th>\n      <td>1</td>\n      <td>6.885000e+06</td>\n    </tr>\n    <tr>\n      <th>9640</th>\n      <td>1</td>\n      <td>4.668000e+06</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>4083</th>\n      <td>1</td>\n      <td>6.370000e+05</td>\n    </tr>\n    <tr>\n      <th>4080</th>\n      <td>7</td>\n      <td>1.166714e+06</td>\n    </tr>\n    <tr>\n      <th>4073</th>\n      <td>1</td>\n      <td>5.100000e+05</td>\n    </tr>\n    <tr>\n      <th>4070</th>\n      <td>10</td>\n      <td>1.273450e+06</td>\n    </tr>\n    <tr>\n      <th>4065</th>\n      <td>1</td>\n      <td>1.950000e+06</td>\n    </tr>\n  </tbody>\n</table>\n<p>250 rows × 2 columns</p>\n</div>"
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OPU6WIC43wnE"
      },
      "source": [
        "### 13. Find unqiue value of zipcode to define how many address we have"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KOXpaf-Ko8gW"
      },
      "source": [
        "my_dataframe['zipcode'].unique()"
      ],
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([98178, 98125, 98028, 98136, 98074, 98053, 98003, 98198, 98146,\n",
              "       98038, 98007, 98115, 98107, 98126, 98019, 98103, 98002, 98133,\n",
              "       98040, 98092, 98030, 98119, 98112, 98052, 98027, 98117, 98058,\n",
              "       98001, 98056, 98166, 98023, 98070, 98148, 98105, 98042, 98008,\n",
              "       98059, 98122, 98144, 98004, 98005, 98034, 98075, 98116, 98010,\n",
              "       98118, 98199, 98032, 98045, 98102, 98077, 98108, 98168, 98177,\n",
              "       98065, 98029, 98006, 98109, 98022, 98033, 98155, 98024, 98011,\n",
              "       98031, 98106, 98072, 98188, 98014, 98055, 98039], dtype=int64)"
            ]
          },
          "metadata": {},
          "execution_count": 70
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YkeiLBavo8Pk"
      },
      "source": [
        "### 14. Define date range to find what kind a people buy house in this date"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n6sqvjo1o8Dc"
      },
      "source": [
        "my_dataframe.loc[my_dataframe['date'] == '20150116T000000'].head(25)"
      ],
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            id             date      price  bedrooms  bathrooms  sqft_living  \\\n",
              "0   7129300520  20150116T000000   221900.0         3       1.00         1180   \n",
              "1   6414100192  20150116T000000   538000.0         3       2.25         2570   \n",
              "2   5631500400  20150116T000000   180000.0         2       1.00          770   \n",
              "3   2487200875  20150116T000000   604000.0         4       3.00         1960   \n",
              "4   1954400510  20150116T000000   510000.0         3       2.00         1680   \n",
              "5   7237550310  20150116T000000  1225000.0         4       4.50         5420   \n",
              "6   1321400060  20150116T000000   257500.0         3       2.25         1715   \n",
              "7   2008000270  20150116T000000   291850.0         3       1.50         1060   \n",
              "8   2414600126  20150116T000000   229500.0         3       1.00         1780   \n",
              "9   3793500160  20150116T000000   323000.0         3       2.50         1890   \n",
              "10  1736800520  20150116T000000   662500.0         3       2.50         3560   \n",
              "11  9212900260  20150116T000000   468000.0         2       1.00         1160   \n",
              "12   114101516  20150116T000000   310000.0         3       1.00         1430   \n",
              "13  6054650070  20150116T000000   400000.0         3       1.75         1370   \n",
              "14  1175000570  20150116T000000   530000.0         5       2.00         1810   \n",
              "15  9297300055  20150116T000000   650000.0         4       3.00         2950   \n",
              "16  1875500060  20150116T000000   395000.0         3       2.00         1890   \n",
              "17  6865200140  20150116T000000   485000.0         4       1.00         1600   \n",
              "18    16000397  20150116T000000   189000.0         2       1.00         1200   \n",
              "19  7983200060  20150116T000000   230000.0         3       1.00         1250   \n",
              "20  6300500875  20150116T000000   385000.0         4       1.75         1620   \n",
              "21  2524049179  20150116T000000  2000000.0         3       2.75         3050   \n",
              "22  7137970340  20150116T000000   285000.0         5       2.50         2270   \n",
              "23  8091400200  20150116T000000   252700.0         2       1.50         1070   \n",
              "24  3814700200  20150116T000000   329000.0         3       2.25         2450   \n",
              "\n",
              "    sqft_lot  floors  waterfront  view  ...  sqft_above  sqft_basement  \\\n",
              "0       5650     1.0           0     0  ...        1180              0   \n",
              "1       7242     2.0           0     0  ...        2170            400   \n",
              "2      10000     1.0           0     0  ...         770              0   \n",
              "3       5000     1.0           0     0  ...        1050            910   \n",
              "4       8080     1.0           0     0  ...        1680              0   \n",
              "5     101930     1.0           0     0  ...        3890           1530   \n",
              "6       6819     2.0           0     0  ...        1715              0   \n",
              "7       9711     1.0           0     0  ...        1060              0   \n",
              "8       7470     1.0           0     0  ...        1050            730   \n",
              "9       6560     2.0           0     0  ...        1890              0   \n",
              "10      9796     1.0           0     0  ...        1860           1700   \n",
              "11      6000     1.0           0     0  ...         860            300   \n",
              "12     19901     1.5           0     0  ...        1430              0   \n",
              "13      9680     1.0           0     0  ...        1370              0   \n",
              "14      4850     1.5           0     0  ...        1810              0   \n",
              "15      5000     2.0           0     3  ...        1980            970   \n",
              "16     14040     2.0           0     0  ...        1890              0   \n",
              "17      4300     1.5           0     0  ...        1600              0   \n",
              "18      9850     1.0           0     0  ...        1200              0   \n",
              "19      9774     1.0           0     0  ...        1250              0   \n",
              "20      4980     1.0           0     0  ...         860            760   \n",
              "21     44867     1.0           0     4  ...        2330            720   \n",
              "22      6300     2.0           0     0  ...        2270              0   \n",
              "23      9643     1.0           0     0  ...        1070              0   \n",
              "24      6500     2.0           0     0  ...        2450              0   \n",
              "\n",
              "    yr_built  yr_renovated  zipcode      lat     long  sqft_living15  \\\n",
              "0       1955             0    98178  47.5112 -122.257           1340   \n",
              "1       1951          1991    98125  47.7210 -122.319           1690   \n",
              "2       1933             0    98028  47.7379 -122.233           2720   \n",
              "3       1965             0    98136  47.5208 -122.393           1360   \n",
              "4       1987             0    98074  47.6168 -122.045           1800   \n",
              "5       2001             0    98053  47.6561 -122.005           4760   \n",
              "6       1995             0    98003  47.3097 -122.327           2238   \n",
              "7       1963             0    98198  47.4095 -122.315           1650   \n",
              "8       1960             0    98146  47.5123 -122.337           1780   \n",
              "9       2003             0    98038  47.3684 -122.031           2390   \n",
              "10      1965             0    98007  47.6007 -122.145           2210   \n",
              "11      1942             0    98115  47.6900 -122.292           1330   \n",
              "12      1927             0    98028  47.7558 -122.229           1780   \n",
              "13      1977             0    98074  47.6127 -122.045           1370   \n",
              "14      1900             0    98107  47.6700 -122.394           1360   \n",
              "15      1979             0    98126  47.5714 -122.375           2140   \n",
              "16      1994             0    98019  47.7277 -121.962           1890   \n",
              "17      1916             0    98103  47.6648 -122.343           1610   \n",
              "18      1921             0    98002  47.3089 -122.210           1060   \n",
              "19      1969             0    98003  47.3343 -122.306           1280   \n",
              "20      1947             0    98133  47.7025 -122.341           1400   \n",
              "21      1968             0    98040  47.5316 -122.233           4110   \n",
              "22      1995             0    98092  47.3266 -122.169           2240   \n",
              "23      1985             0    98030  47.3533 -122.166           1220   \n",
              "24      1985             0    98030  47.3739 -122.172           2200   \n",
              "\n",
              "    sqft_lot15  sqft_price  \n",
              "0         5650   39.274336  \n",
              "1         7639   74.288870  \n",
              "2         8062   18.000000  \n",
              "3         5000  120.800000  \n",
              "4         7503   63.118812  \n",
              "5       101930   12.018052  \n",
              "6         6819   37.762135  \n",
              "7         9711   30.053548  \n",
              "8         8113   30.722892  \n",
              "9         7570   49.237805  \n",
              "10        8925   67.629645  \n",
              "11        6000   78.000000  \n",
              "12       12697   15.577107  \n",
              "13       10208   41.322314  \n",
              "14        4850  109.278351  \n",
              "15        4000  130.000000  \n",
              "16       14018   28.133903  \n",
              "17        4300  112.790698  \n",
              "18        5095   19.187817  \n",
              "19        8850   23.531819  \n",
              "20        4980   77.309237  \n",
              "21       20336   44.576192  \n",
              "22        7005   45.238095  \n",
              "23        8386   26.205538  \n",
              "24        6865   50.615385  \n",
              "\n",
              "[25 rows x 22 columns]"
            ],
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>id</th>\n      <th>date</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>...</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n      <th>sqft_price</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>7129300520</td>\n      <td>20150116T000000</td>\n      <td>221900.0</td>\n      <td>3</td>\n      <td>1.00</td>\n      <td>1180</td>\n      <td>5650</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1180</td>\n      <td>0</td>\n      <td>1955</td>\n      <td>0</td>\n      <td>98178</td>\n      <td>47.5112</td>\n      <td>-122.257</td>\n      <td>1340</td>\n      <td>5650</td>\n      <td>39.274336</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>6414100192</td>\n      <td>20150116T000000</td>\n      <td>538000.0</td>\n      <td>3</td>\n      <td>2.25</td>\n      <td>2570</td>\n      <td>7242</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>2170</td>\n      <td>400</td>\n      <td>1951</td>\n      <td>1991</td>\n      <td>98125</td>\n      <td>47.7210</td>\n      <td>-122.319</td>\n      <td>1690</td>\n      <td>7639</td>\n      <td>74.288870</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>5631500400</td>\n      <td>20150116T000000</td>\n      <td>180000.0</td>\n      <td>2</td>\n      <td>1.00</td>\n      <td>770</td>\n      <td>10000</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>770</td>\n      <td>0</td>\n      <td>1933</td>\n      <td>0</td>\n      <td>98028</td>\n      <td>47.7379</td>\n      <td>-122.233</td>\n      <td>2720</td>\n      <td>8062</td>\n      <td>18.000000</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>2487200875</td>\n      <td>20150116T000000</td>\n      <td>604000.0</td>\n      <td>4</td>\n      <td>3.00</td>\n      <td>1960</td>\n      <td>5000</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1050</td>\n      <td>910</td>\n      <td>1965</td>\n      <td>0</td>\n      <td>98136</td>\n      <td>47.5208</td>\n      <td>-122.393</td>\n      <td>1360</td>\n      <td>5000</td>\n      <td>120.800000</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1954400510</td>\n      <td>20150116T000000</td>\n      <td>510000.0</td>\n      <td>3</td>\n      <td>2.00</td>\n      <td>1680</td>\n      <td>8080</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1680</td>\n      <td>0</td>\n      <td>1987</td>\n      <td>0</td>\n      <td>98074</td>\n      <td>47.6168</td>\n      <td>-122.045</td>\n      <td>1800</td>\n      <td>7503</td>\n      <td>63.118812</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>7237550310</td>\n      <td>20150116T000000</td>\n      <td>1225000.0</td>\n      <td>4</td>\n      <td>4.50</td>\n      <td>5420</td>\n      <td>101930</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>3890</td>\n      <td>1530</td>\n      <td>2001</td>\n      <td>0</td>\n      <td>98053</td>\n      <td>47.6561</td>\n      <td>-122.005</td>\n      <td>4760</td>\n      <td>101930</td>\n      <td>12.018052</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>1321400060</td>\n      <td>20150116T000000</td>\n      <td>257500.0</td>\n      <td>3</td>\n      <td>2.25</td>\n      <td>1715</td>\n      <td>6819</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1715</td>\n      <td>0</td>\n      <td>1995</td>\n      <td>0</td>\n      <td>98003</td>\n      <td>47.3097</td>\n      <td>-122.327</td>\n      <td>2238</td>\n      <td>6819</td>\n      <td>37.762135</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>2008000270</td>\n      <td>20150116T000000</td>\n      <td>291850.0</td>\n      <td>3</td>\n      <td>1.50</td>\n      <td>1060</td>\n      <td>9711</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1060</td>\n      <td>0</td>\n      <td>1963</td>\n      <td>0</td>\n      <td>98198</td>\n      <td>47.4095</td>\n      <td>-122.315</td>\n      <td>1650</td>\n      <td>9711</td>\n      <td>30.053548</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>2414600126</td>\n      <td>20150116T000000</td>\n      <td>229500.0</td>\n      <td>3</td>\n      <td>1.00</td>\n      <td>1780</td>\n      <td>7470</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1050</td>\n      <td>730</td>\n      <td>1960</td>\n      <td>0</td>\n      <td>98146</td>\n      <td>47.5123</td>\n      <td>-122.337</td>\n      <td>1780</td>\n      <td>8113</td>\n      <td>30.722892</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>3793500160</td>\n      <td>20150116T000000</td>\n      <td>323000.0</td>\n      <td>3</td>\n      <td>2.50</td>\n      <td>1890</td>\n      <td>6560</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1890</td>\n      <td>0</td>\n      <td>2003</td>\n      <td>0</td>\n      <td>98038</td>\n      <td>47.3684</td>\n      <td>-122.031</td>\n      <td>2390</td>\n      <td>7570</td>\n      <td>49.237805</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>1736800520</td>\n      <td>20150116T000000</td>\n      <td>662500.0</td>\n      <td>3</td>\n      <td>2.50</td>\n      <td>3560</td>\n      <td>9796</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1860</td>\n      <td>1700</td>\n      <td>1965</td>\n      <td>0</td>\n      <td>98007</td>\n      <td>47.6007</td>\n      <td>-122.145</td>\n      <td>2210</td>\n      <td>8925</td>\n      <td>67.629645</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>9212900260</td>\n      <td>20150116T000000</td>\n      <td>468000.0</td>\n      <td>2</td>\n      <td>1.00</td>\n      <td>1160</td>\n      <td>6000</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>860</td>\n      <td>300</td>\n      <td>1942</td>\n      <td>0</td>\n      <td>98115</td>\n      <td>47.6900</td>\n      <td>-122.292</td>\n      <td>1330</td>\n      <td>6000</td>\n      <td>78.000000</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>114101516</td>\n      <td>20150116T000000</td>\n      <td>310000.0</td>\n      <td>3</td>\n      <td>1.00</td>\n      <td>1430</td>\n      <td>19901</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1430</td>\n      <td>0</td>\n      <td>1927</td>\n      <td>0</td>\n      <td>98028</td>\n      <td>47.7558</td>\n      <td>-122.229</td>\n      <td>1780</td>\n      <td>12697</td>\n      <td>15.577107</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>6054650070</td>\n      <td>20150116T000000</td>\n      <td>400000.0</td>\n      <td>3</td>\n      <td>1.75</td>\n      <td>1370</td>\n      <td>9680</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1370</td>\n      <td>0</td>\n      <td>1977</td>\n      <td>0</td>\n      <td>98074</td>\n      <td>47.6127</td>\n      <td>-122.045</td>\n      <td>1370</td>\n      <td>10208</td>\n      <td>41.322314</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>1175000570</td>\n      <td>20150116T000000</td>\n      <td>530000.0</td>\n      <td>5</td>\n      <td>2.00</td>\n      <td>1810</td>\n      <td>4850</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1810</td>\n      <td>0</td>\n      <td>1900</td>\n      <td>0</td>\n      <td>98107</td>\n      <td>47.6700</td>\n      <td>-122.394</td>\n      <td>1360</td>\n      <td>4850</td>\n      <td>109.278351</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>9297300055</td>\n      <td>20150116T000000</td>\n      <td>650000.0</td>\n      <td>4</td>\n      <td>3.00</td>\n      <td>2950</td>\n      <td>5000</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>3</td>\n      <td>...</td>\n      <td>1980</td>\n      <td>970</td>\n      <td>1979</td>\n      <td>0</td>\n      <td>98126</td>\n      <td>47.5714</td>\n      <td>-122.375</td>\n      <td>2140</td>\n      <td>4000</td>\n      <td>130.000000</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>1875500060</td>\n      <td>20150116T000000</td>\n      <td>395000.0</td>\n      <td>3</td>\n      <td>2.00</td>\n      <td>1890</td>\n      <td>14040</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1890</td>\n      <td>0</td>\n      <td>1994</td>\n      <td>0</td>\n      <td>98019</td>\n      <td>47.7277</td>\n      <td>-121.962</td>\n      <td>1890</td>\n      <td>14018</td>\n      <td>28.133903</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>6865200140</td>\n      <td>20150116T000000</td>\n      <td>485000.0</td>\n      <td>4</td>\n      <td>1.00</td>\n      <td>1600</td>\n      <td>4300</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1600</td>\n      <td>0</td>\n      <td>1916</td>\n      <td>0</td>\n      <td>98103</td>\n      <td>47.6648</td>\n      <td>-122.343</td>\n      <td>1610</td>\n      <td>4300</td>\n      <td>112.790698</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>16000397</td>\n      <td>20150116T000000</td>\n      <td>189000.0</td>\n      <td>2</td>\n      <td>1.00</td>\n      <td>1200</td>\n      <td>9850</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1200</td>\n      <td>0</td>\n      <td>1921</td>\n      <td>0</td>\n      <td>98002</td>\n      <td>47.3089</td>\n      <td>-122.210</td>\n      <td>1060</td>\n      <td>5095</td>\n      <td>19.187817</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>7983200060</td>\n      <td>20150116T000000</td>\n      <td>230000.0</td>\n      <td>3</td>\n      <td>1.00</td>\n      <td>1250</td>\n      <td>9774</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1250</td>\n      <td>0</td>\n      <td>1969</td>\n      <td>0</td>\n      <td>98003</td>\n      <td>47.3343</td>\n      <td>-122.306</td>\n      <td>1280</td>\n      <td>8850</td>\n      <td>23.531819</td>\n    </tr>\n    <tr>\n      <th>20</th>\n      <td>6300500875</td>\n      <td>20150116T000000</td>\n      <td>385000.0</td>\n      <td>4</td>\n      <td>1.75</td>\n      <td>1620</td>\n      <td>4980</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>860</td>\n      <td>760</td>\n      <td>1947</td>\n      <td>0</td>\n      <td>98133</td>\n      <td>47.7025</td>\n      <td>-122.341</td>\n      <td>1400</td>\n      <td>4980</td>\n      <td>77.309237</td>\n    </tr>\n    <tr>\n      <th>21</th>\n      <td>2524049179</td>\n      <td>20150116T000000</td>\n      <td>2000000.0</td>\n      <td>3</td>\n      <td>2.75</td>\n      <td>3050</td>\n      <td>44867</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>4</td>\n      <td>...</td>\n      <td>2330</td>\n      <td>720</td>\n      <td>1968</td>\n      <td>0</td>\n      <td>98040</td>\n      <td>47.5316</td>\n      <td>-122.233</td>\n      <td>4110</td>\n      <td>20336</td>\n      <td>44.576192</td>\n    </tr>\n    <tr>\n      <th>22</th>\n      <td>7137970340</td>\n      <td>20150116T000000</td>\n      <td>285000.0</td>\n      <td>5</td>\n      <td>2.50</td>\n      <td>2270</td>\n      <td>6300</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>2270</td>\n      <td>0</td>\n      <td>1995</td>\n      <td>0</td>\n      <td>98092</td>\n      <td>47.3266</td>\n      <td>-122.169</td>\n      <td>2240</td>\n      <td>7005</td>\n      <td>45.238095</td>\n    </tr>\n    <tr>\n      <th>23</th>\n      <td>8091400200</td>\n      <td>20150116T000000</td>\n      <td>252700.0</td>\n      <td>2</td>\n      <td>1.50</td>\n      <td>1070</td>\n      <td>9643</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1070</td>\n      <td>0</td>\n      <td>1985</td>\n      <td>0</td>\n      <td>98030</td>\n      <td>47.3533</td>\n      <td>-122.166</td>\n      <td>1220</td>\n      <td>8386</td>\n      <td>26.205538</td>\n    </tr>\n    <tr>\n      <th>24</th>\n      <td>3814700200</td>\n      <td>20150116T000000</td>\n      <td>329000.0</td>\n      <td>3</td>\n      <td>2.25</td>\n      <td>2450</td>\n      <td>6500</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>2450</td>\n      <td>0</td>\n      <td>1985</td>\n      <td>0</td>\n      <td>98030</td>\n      <td>47.3739</td>\n      <td>-122.172</td>\n      <td>2200</td>\n      <td>6865</td>\n      <td>50.615385</td>\n    </tr>\n  </tbody>\n</table>\n<p>25 rows × 22 columns</p>\n</div>"
          },
          "metadata": {},
          "execution_count": 92
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dO27GbNso7lk"
      },
      "source": [
        "### 15. To find all renovated house in this DateFrame"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "D_oNIdTGo7RU"
      },
      "source": [
        "my_dataframe.loc[my_dataframe['yr_renovated'] != 0].head(25)\n"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             id             date      price  bedrooms  bathrooms  sqft_living  \\\n",
              "1    6414100192  20141209T000000   538000.0         3       2.25         2570   \n",
              "35   9547205180  20140613T000000   696000.0         3       2.50         2300   \n",
              "95   1483300570  20140908T000000   905000.0         4       2.50         3300   \n",
              "103  2450000295  20141007T000000  1088000.0         3       2.50         2920   \n",
              "115  3626039325  20141121T000000   740500.0         3       3.50         4380   \n",
              "125  4389200955  20150302T000000  1450000.0         4       2.75         2750   \n",
              "158  8029200135  20141113T000000   247000.0         3       2.00         1270   \n",
              "209  6300000550  20140717T000000   464000.0         6       3.00         2300   \n",
              "216    46100204  20150221T000000  1505000.0         5       3.00         3300   \n",
              "230  8096000060  20150413T000000   655000.0         2       1.75         1450   \n",
              "237  7228500560  20150320T000000   410000.0         4       1.00         1970   \n",
              "269  7960900060  20150504T000000  2900000.0         4       3.25         5050   \n",
              "274  4235400186  20141124T000000   331000.0         3       1.75         1080   \n",
              "282  7424700045  20150513T000000  2050000.0         5       3.00         3830   \n",
              "324  7520000520  20140905T000000   232000.0         2       1.00         1240   \n",
              "325  7520000520  20150311T000000   240500.0         2       1.00         1240   \n",
              "330  3179100060  20140916T000000   880000.0         4       3.50         2800   \n",
              "358   325059171  20140505T000000   900000.0         3       1.00         1330   \n",
              "379  7132300695  20150421T000000   435000.0         3       1.50         1300   \n",
              "398  1604601375  20140619T000000   378750.0         3       2.50         2160   \n",
              "426   936000060  20141114T000000   310000.0         5       1.75         2190   \n",
              "435  2268400350  20140916T000000   749000.0         4       2.50         1710   \n",
              "450  4055700030  20150502T000000  1450000.0         3       4.50         3970   \n",
              "470  2172000075  20140623T000000   290900.0         2       2.00         1610   \n",
              "472  8820902200  20141113T000000  1199000.0         4       2.75         4110   \n",
              "\n",
              "     sqft_lot  floors  waterfront  view  ...  sqft_above  sqft_basement  \\\n",
              "1        7242     2.0           0     0  ...        2170            400   \n",
              "35       3060     1.5           0     0  ...        1510            790   \n",
              "95      10250     1.0           0     0  ...        2390            910   \n",
              "103      8113     2.0           0     0  ...        2920              0   \n",
              "115      6350     2.0           0     0  ...        2780           1600   \n",
              "125     17789     1.5           0     0  ...        1980            770   \n",
              "158      7198     1.5           0     0  ...        1270              0   \n",
              "209      3404     2.0           0     0  ...        1600            700   \n",
              "216     33474     1.0           0     3  ...        1870           1430   \n",
              "230     15798     2.0           1     4  ...        1230            220   \n",
              "237      4740     1.5           0     0  ...        1670            300   \n",
              "269     20100     1.5           0     2  ...        4750            300   \n",
              "274      1306     1.0           0     0  ...         580            500   \n",
              "282      8480     2.0           0     1  ...        2630           1200   \n",
              "324     12092     1.0           0     0  ...         960            280   \n",
              "325     12092     1.0           0     0  ...         960            280   \n",
              "330      6750     2.0           0     0  ...        1890            910   \n",
              "358     77972     1.0           0     0  ...        1330              0   \n",
              "379      3348     1.5           0     0  ...        1300              0   \n",
              "398      3000     1.5           0     0  ...        1260            900   \n",
              "426     27260     1.0           0     0  ...        2190              0   \n",
              "435      9627     1.0           0     0  ...        1440            270   \n",
              "450     24920     2.0           0     2  ...        3260            710   \n",
              "470     17600     2.0           0     0  ...        1610              0   \n",
              "472      8400     2.0           0     1  ...        3130            980   \n",
              "\n",
              "     yr_built  yr_renovated  zipcode      lat     long  sqft_living15  \\\n",
              "1        1951          1991    98125  47.7210 -122.319           1690   \n",
              "35       1930          2002    98115  47.6827 -122.310           1590   \n",
              "95       1946          1991    98040  47.5873 -122.249           1950   \n",
              "103      1950          2010    98004  47.5814 -122.196           2370   \n",
              "115      1900          1999    98117  47.6981 -122.368           1830   \n",
              "125      1914          1992    98004  47.6141 -122.212           3060   \n",
              "158      1916          2013    98022  47.2086 -121.996           1160   \n",
              "209      1920          1994    98133  47.7067 -122.343           1560   \n",
              "216      1957          1991    98040  47.5673 -122.210           3836   \n",
              "230      1915          1978    98166  47.4497 -122.375           2030   \n",
              "237      1904          2005    98122  47.6136 -122.303           1510   \n",
              "269      1982          2008    98004  47.6312 -122.223           3890   \n",
              "274      1954          2003    98199  47.6601 -122.400           1440   \n",
              "282      1905          1994    98122  47.6166 -122.287           3050   \n",
              "324      1922          1984    98146  47.4957 -122.352           1820   \n",
              "325      1922          1984    98146  47.4957 -122.352           1820   \n",
              "330      1951          2002    98105  47.6690 -122.275           2370   \n",
              "358      1928          1954    98033  47.6891 -122.159           1340   \n",
              "379      1904          2014    98144  47.5920 -122.307           1590   \n",
              "398      1909          2011    98118  47.5644 -122.289           1060   \n",
              "426      1947          1974    98166  47.4546 -122.337           1620   \n",
              "435      1976          2014    98006  47.5590 -122.164           2140   \n",
              "450      1977          1999    98034  47.7183 -122.258           2610   \n",
              "470      1930          1983    98178  47.4855 -122.266           1310   \n",
              "472      1928          2013    98125  47.7170 -122.281           2820   \n",
              "\n",
              "     sqft_lot15  dimesions  \n",
              "1          7639   0.000000  \n",
              "35         3264   0.000000  \n",
              "95         6045   0.000000  \n",
              "103        8113   0.000000  \n",
              "115        6350   0.000000  \n",
              "125       11275   0.000000  \n",
              "158        7198   0.000000  \n",
              "209        1312   0.000000  \n",
              "216       20953   0.000000  \n",
              "230       13193  46.236284  \n",
              "237        4740   0.000000  \n",
              "269       20060   0.000000  \n",
              "274        2225   0.000000  \n",
              "282        7556   0.000000  \n",
              "324        7460   0.000000  \n",
              "325        7460   0.000000  \n",
              "330        6120   0.000000  \n",
              "358       17689   0.000000  \n",
              "379        2577   0.000000  \n",
              "398        3500   0.000000  \n",
              "426       39480   0.000000  \n",
              "435        9131   0.000000  \n",
              "450       13838   0.000000  \n",
              "470       12950   0.000000  \n",
              "472        8400   0.000000  \n",
              "\n",
              "[25 rows x 22 columns]"
            ],
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>id</th>\n      <th>date</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>...</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n      <th>dimesions</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>6414100192</td>\n      <td>20141209T000000</td>\n      <td>538000.0</td>\n      <td>3</td>\n      <td>2.25</td>\n      <td>2570</td>\n      <td>7242</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>2170</td>\n      <td>400</td>\n      <td>1951</td>\n      <td>1991</td>\n      <td>98125</td>\n      <td>47.7210</td>\n      <td>-122.319</td>\n      <td>1690</td>\n      <td>7639</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>35</th>\n      <td>9547205180</td>\n      <td>20140613T000000</td>\n      <td>696000.0</td>\n      <td>3</td>\n      <td>2.50</td>\n      <td>2300</td>\n      <td>3060</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1510</td>\n      <td>790</td>\n      <td>1930</td>\n      <td>2002</td>\n      <td>98115</td>\n      <td>47.6827</td>\n      <td>-122.310</td>\n      <td>1590</td>\n      <td>3264</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>95</th>\n      <td>1483300570</td>\n      <td>20140908T000000</td>\n      <td>905000.0</td>\n      <td>4</td>\n      <td>2.50</td>\n      <td>3300</td>\n      <td>10250</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>2390</td>\n      <td>910</td>\n      <td>1946</td>\n      <td>1991</td>\n      <td>98040</td>\n      <td>47.5873</td>\n      <td>-122.249</td>\n      <td>1950</td>\n      <td>6045</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>103</th>\n      <td>2450000295</td>\n      <td>20141007T000000</td>\n      <td>1088000.0</td>\n      <td>3</td>\n      <td>2.50</td>\n      <td>2920</td>\n      <td>8113</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>2920</td>\n      <td>0</td>\n      <td>1950</td>\n      <td>2010</td>\n      <td>98004</td>\n      <td>47.5814</td>\n      <td>-122.196</td>\n      <td>2370</td>\n      <td>8113</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>115</th>\n      <td>3626039325</td>\n      <td>20141121T000000</td>\n      <td>740500.0</td>\n      <td>3</td>\n      <td>3.50</td>\n      <td>4380</td>\n      <td>6350</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>2780</td>\n      <td>1600</td>\n      <td>1900</td>\n      <td>1999</td>\n      <td>98117</td>\n      <td>47.6981</td>\n      <td>-122.368</td>\n      <td>1830</td>\n      <td>6350</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>125</th>\n      <td>4389200955</td>\n      <td>20150302T000000</td>\n      <td>1450000.0</td>\n      <td>4</td>\n      <td>2.75</td>\n      <td>2750</td>\n      <td>17789</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1980</td>\n      <td>770</td>\n      <td>1914</td>\n      <td>1992</td>\n      <td>98004</td>\n      <td>47.6141</td>\n      <td>-122.212</td>\n      <td>3060</td>\n      <td>11275</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>158</th>\n      <td>8029200135</td>\n      <td>20141113T000000</td>\n      <td>247000.0</td>\n      <td>3</td>\n      <td>2.00</td>\n      <td>1270</td>\n      <td>7198</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1270</td>\n      <td>0</td>\n      <td>1916</td>\n      <td>2013</td>\n      <td>98022</td>\n      <td>47.2086</td>\n      <td>-121.996</td>\n      <td>1160</td>\n      <td>7198</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>209</th>\n      <td>6300000550</td>\n      <td>20140717T000000</td>\n      <td>464000.0</td>\n      <td>6</td>\n      <td>3.00</td>\n      <td>2300</td>\n      <td>3404</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1600</td>\n      <td>700</td>\n      <td>1920</td>\n      <td>1994</td>\n      <td>98133</td>\n      <td>47.7067</td>\n      <td>-122.343</td>\n      <td>1560</td>\n      <td>1312</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>216</th>\n      <td>46100204</td>\n      <td>20150221T000000</td>\n      <td>1505000.0</td>\n      <td>5</td>\n      <td>3.00</td>\n      <td>3300</td>\n      <td>33474</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>3</td>\n      <td>...</td>\n      <td>1870</td>\n      <td>1430</td>\n      <td>1957</td>\n      <td>1991</td>\n      <td>98040</td>\n      <td>47.5673</td>\n      <td>-122.210</td>\n      <td>3836</td>\n      <td>20953</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>230</th>\n      <td>8096000060</td>\n      <td>20150413T000000</td>\n      <td>655000.0</td>\n      <td>2</td>\n      <td>1.75</td>\n      <td>1450</td>\n      <td>15798</td>\n      <td>2.0</td>\n      <td>1</td>\n      <td>4</td>\n      <td>...</td>\n      <td>1230</td>\n      <td>220</td>\n      <td>1915</td>\n      <td>1978</td>\n      <td>98166</td>\n      <td>47.4497</td>\n      <td>-122.375</td>\n      <td>2030</td>\n      <td>13193</td>\n      <td>46.236284</td>\n    </tr>\n    <tr>\n      <th>237</th>\n      <td>7228500560</td>\n      <td>20150320T000000</td>\n      <td>410000.0</td>\n      <td>4</td>\n      <td>1.00</td>\n      <td>1970</td>\n      <td>4740</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1670</td>\n      <td>300</td>\n      <td>1904</td>\n      <td>2005</td>\n      <td>98122</td>\n      <td>47.6136</td>\n      <td>-122.303</td>\n      <td>1510</td>\n      <td>4740</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>269</th>\n      <td>7960900060</td>\n      <td>20150504T000000</td>\n      <td>2900000.0</td>\n      <td>4</td>\n      <td>3.25</td>\n      <td>5050</td>\n      <td>20100</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>2</td>\n      <td>...</td>\n      <td>4750</td>\n      <td>300</td>\n      <td>1982</td>\n      <td>2008</td>\n      <td>98004</td>\n      <td>47.6312</td>\n      <td>-122.223</td>\n      <td>3890</td>\n      <td>20060</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>274</th>\n      <td>4235400186</td>\n      <td>20141124T000000</td>\n      <td>331000.0</td>\n      <td>3</td>\n      <td>1.75</td>\n      <td>1080</td>\n      <td>1306</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>580</td>\n      <td>500</td>\n      <td>1954</td>\n      <td>2003</td>\n      <td>98199</td>\n      <td>47.6601</td>\n      <td>-122.400</td>\n      <td>1440</td>\n      <td>2225</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>282</th>\n      <td>7424700045</td>\n      <td>20150513T000000</td>\n      <td>2050000.0</td>\n      <td>5</td>\n      <td>3.00</td>\n      <td>3830</td>\n      <td>8480</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>...</td>\n      <td>2630</td>\n      <td>1200</td>\n      <td>1905</td>\n      <td>1994</td>\n      <td>98122</td>\n      <td>47.6166</td>\n      <td>-122.287</td>\n      <td>3050</td>\n      <td>7556</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>324</th>\n      <td>7520000520</td>\n      <td>20140905T000000</td>\n      <td>232000.0</td>\n      <td>2</td>\n      <td>1.00</td>\n      <td>1240</td>\n      <td>12092</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>960</td>\n      <td>280</td>\n      <td>1922</td>\n      <td>1984</td>\n      <td>98146</td>\n      <td>47.4957</td>\n      <td>-122.352</td>\n      <td>1820</td>\n      <td>7460</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>325</th>\n      <td>7520000520</td>\n      <td>20150311T000000</td>\n      <td>240500.0</td>\n      <td>2</td>\n      <td>1.00</td>\n      <td>1240</td>\n      <td>12092</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>960</td>\n      <td>280</td>\n      <td>1922</td>\n      <td>1984</td>\n      <td>98146</td>\n      <td>47.4957</td>\n      <td>-122.352</td>\n      <td>1820</td>\n      <td>7460</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>330</th>\n      <td>3179100060</td>\n      <td>20140916T000000</td>\n      <td>880000.0</td>\n      <td>4</td>\n      <td>3.50</td>\n      <td>2800</td>\n      <td>6750</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1890</td>\n      <td>910</td>\n      <td>1951</td>\n      <td>2002</td>\n      <td>98105</td>\n      <td>47.6690</td>\n      <td>-122.275</td>\n      <td>2370</td>\n      <td>6120</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>358</th>\n      <td>325059171</td>\n      <td>20140505T000000</td>\n      <td>900000.0</td>\n      <td>3</td>\n      <td>1.00</td>\n      <td>1330</td>\n      <td>77972</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1330</td>\n      <td>0</td>\n      <td>1928</td>\n      <td>1954</td>\n      <td>98033</td>\n      <td>47.6891</td>\n      <td>-122.159</td>\n      <td>1340</td>\n      <td>17689</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>379</th>\n      <td>7132300695</td>\n      <td>20150421T000000</td>\n      <td>435000.0</td>\n      <td>3</td>\n      <td>1.50</td>\n      <td>1300</td>\n      <td>3348</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1300</td>\n      <td>0</td>\n      <td>1904</td>\n      <td>2014</td>\n      <td>98144</td>\n      <td>47.5920</td>\n      <td>-122.307</td>\n      <td>1590</td>\n      <td>2577</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>398</th>\n      <td>1604601375</td>\n      <td>20140619T000000</td>\n      <td>378750.0</td>\n      <td>3</td>\n      <td>2.50</td>\n      <td>2160</td>\n      <td>3000</td>\n      <td>1.5</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1260</td>\n      <td>900</td>\n      <td>1909</td>\n      <td>2011</td>\n      <td>98118</td>\n      <td>47.5644</td>\n      <td>-122.289</td>\n      <td>1060</td>\n      <td>3500</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>426</th>\n      <td>936000060</td>\n      <td>20141114T000000</td>\n      <td>310000.0</td>\n      <td>5</td>\n      <td>1.75</td>\n      <td>2190</td>\n      <td>27260</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>2190</td>\n      <td>0</td>\n      <td>1947</td>\n      <td>1974</td>\n      <td>98166</td>\n      <td>47.4546</td>\n      <td>-122.337</td>\n      <td>1620</td>\n      <td>39480</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>435</th>\n      <td>2268400350</td>\n      <td>20140916T000000</td>\n      <td>749000.0</td>\n      <td>4</td>\n      <td>2.50</td>\n      <td>1710</td>\n      <td>9627</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1440</td>\n      <td>270</td>\n      <td>1976</td>\n      <td>2014</td>\n      <td>98006</td>\n      <td>47.5590</td>\n      <td>-122.164</td>\n      <td>2140</td>\n      <td>9131</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>450</th>\n      <td>4055700030</td>\n      <td>20150502T000000</td>\n      <td>1450000.0</td>\n      <td>3</td>\n      <td>4.50</td>\n      <td>3970</td>\n      <td>24920</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>2</td>\n      <td>...</td>\n      <td>3260</td>\n      <td>710</td>\n      <td>1977</td>\n      <td>1999</td>\n      <td>98034</td>\n      <td>47.7183</td>\n      <td>-122.258</td>\n      <td>2610</td>\n      <td>13838</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>470</th>\n      <td>2172000075</td>\n      <td>20140623T000000</td>\n      <td>290900.0</td>\n      <td>2</td>\n      <td>2.00</td>\n      <td>1610</td>\n      <td>17600</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>1610</td>\n      <td>0</td>\n      <td>1930</td>\n      <td>1983</td>\n      <td>98178</td>\n      <td>47.4855</td>\n      <td>-122.266</td>\n      <td>1310</td>\n      <td>12950</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>472</th>\n      <td>8820902200</td>\n      <td>20141113T000000</td>\n      <td>1199000.0</td>\n      <td>4</td>\n      <td>2.75</td>\n      <td>4110</td>\n      <td>8400</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>1</td>\n      <td>...</td>\n      <td>3130</td>\n      <td>980</td>\n      <td>1928</td>\n      <td>2013</td>\n      <td>98125</td>\n      <td>47.7170</td>\n      <td>-122.281</td>\n      <td>2820</td>\n      <td>8400</td>\n      <td>0.000000</td>\n    </tr>\n  </tbody>\n</table>\n<p>25 rows × 22 columns</p>\n</div>"
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": []
    }
  ]
}