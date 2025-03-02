### Australia Tourism Demand Forecast - Time Series Forecasting using Traditional ML Models (Python)

#### Introduction

In this project, we aim to forecast the total number of quarterly trips for each of the 76 regions in Australia, resulting in 76 distinct time series. We will utilize an independent multi-series modeling approach, known as the Global Forecasting Model.
This approach involves constructing a unified predictive model that simultaneously learns from multiple time series. By capturing the common dynamics influencing the entire dataset, we can effectively reduce the noise associated with individual series. 
The benefits of this methodology include computational efficiency, ease of maintenance, and the potential for more robust generalizations across the various time series. Plus, since all time series are combined during training, the model has a higher learning capacity even if the series are short, which is suitable for this case.

#### Dataset

Quarterly overnight trips (in thousands) from 1998 Q1 to 2016 Q4 across
Australia. The tourism regions are formed through the aggregation of Statistical
Local Areas (SLAs) which are defined by the various State and Territory tourism
authorities according to their research and marketing needs.
Wang, E, D Cook, and RJ Hyndman (2020). A new tidy data structure to support
exploration and modeling of temporal data, Journal of Computational and
Graphical Statistics, 29:3, 466-478, doi:10.1080/10618600.2019.1695624.
Shape of the dataset: (24320, 5)

- date_time: quarterly
- Region
- State
- Purpose
- Trips : number of total trips, in thousands