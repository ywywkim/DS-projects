﻿### Grupo Bimbo Inventory Demand Forecast - Predictive analysis using XGBoost machine learning regression model

#### Introduction

Grupo Bimbo invites participants to develop a model to accurately forecast inventory demand based on historical sales data. Doing so will make sure consumers of its over 100 bakery products aren’t staring at empty shelves, while also reducing the amount spent on refunds to store owners with surplus product unfit for sale.

Effective inventory management hinges on precise demand forecasting, which is essential for ensuring that products are readily available to satisfy consumer demand without incurring the costs of overstocking. In this light, harnessing machine learning methodologies can significantly boost the accuracy of demand predictions. This project presents a detailed framework for forecasting weekly demand for products at individual stores, utilizing the XGBoost algorithm. Through careful data preprocessing, the development of relevant features, and the training of a finely-tuned model, this approach aims to generate trustworthy demand forecasts based on historical sales data collected in Mexico.

#### Dataset

The dataset consists of 9 weeks of sales transactions in Mexico. Every week, there are delivery trucks that deliver products to the vendors. Each transaction consists of sales and returns. Returns are the products that are unsold and expired. The demand for a product in a certain week is defined as the sales this week subtracted by the return next week.

- Semana: Week number (From Thursday to Wednesday)
- Agencia_ID: Sales Depot ID
- Canal_ID: Sales Channel ID
- Ruta_SAK: Route ID (Several routes = Sales Depot)
- Cliente_ID: Client ID
- NombreCliente: Client name
- Producto_ID: Product ID
- NombreProducto: Product Name
- Venta_uni_hoy: Sales unit this week (integer)
- Venta_hoy: Sales this week (unit: pesos)
- Dev_uni_proxima: Returns unit next week (integer)
- Dev_proxima: Returns next week (unit: pesos)
- Demanda_uni_equil: Adjusted Demand (integer) (target variable)

More details regarding this project and the data can be found in Kaggle : https://www.kaggle.com/competitions/grupo-bimbo-inventory-demand/data
