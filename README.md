# Algo-Trading Using Exponential Moving Averages
Exponential moving averages (EMAs) are a type of weighted moving averages, which seek to represent the average price of a stock over a defined period of time. Since this cancels out daily fluctuations of stock prices, the concept can be used to define buy and sell points within a specified dataset.
## Data Used
The data used in this project belongs to the [NSEPY](https://nsepy.xyz/) library, which allows for the pulling of real-time NSE (National Stock Exchange of India) data. More specifically, the specific dataset pulled from the library is that of the Bharti Airtel's stock value between 2019 and 2021. The gh() function in the code could be referred to to understand how the data is pulled.
## Working of the Code
The code, as per main.py, allows for the dataset pulled from the NSEpy library. After doing so, the short, middle and long EMAs are defined for the dataset, which are 5, 18 and 62 days long respectively. These values were chosen from hyperparameter testing done beforehand. Then, the buy-sell-function decides to buy when the long EMA value is higher than that of the middle EMA and the middle EMA value is higher than that of the short EMA. It decides to sell when the middle EMA value is lower than that of the short EMA, and the price we previously bought at was lower then the current price point. The profits are then calculated using simple multiplacation taking into account the stock value at buy/sell point and amount of stocks bought. The full dataset is saved in a CSV file named after the stock symbol. 

Note 1: The algorithm is such that it will sell all balance stocks on the last day of the dataset, do keep this in mind when doing your own testing, and change it if needed under the comment within the buy-sell-function in utils.py. 

Note 2: The functions dataset() and find-profits() exist in utils.py to make the code simpler and reusable, do use these functions if you intend on replicating this repository. 
## Evaluation 
The algorithm is seen to be profitable for all known stocks tested except for situations in which the stock price never came back up (for instance, for stocks wherein the company declared bankruptcy). Here is an example of the algorithm tested with the BHARTIARTL stock, wherein strategy 1 implies investing a certain amount of money into the stock and holding on it for the duration of the timeframe, and strategy 2 implies using our EMA algorithm: 
![Figure_1](https://user-images.githubusercontent.com/77375209/116540148-650abd80-a907-11eb-9d47-582b743421eb.png)
Herein, instead of a specified number of stocks, a specified budget is instantiated and which is further invested into the stocks and further taken out of the stocks repeatedly. 

Note 3: This project was made for research purposes and in no way exists to motivate individuals into using it to profit from the stock market. 
