import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


def forecast_with_lstm(df: pd.DataFrame, periods: int = 30):
    data = df["sales"].values.reshape(-1, 1)

    X, y = [], []
    for i in range(30, len(data)):
        X.append(data[i-30:i])
        y.append(data[i])

    X, y = np.array(X), np.array(y)

    model = Sequential()
    model.add(LSTM(64, activation="relu", return_sequences=True, input_shape=(30, 1)))
    model.add(LSTM(32, activation="relu"))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mse")

    model.fit(X, y, epochs=20, batch_size=16, verbose=0)

    last_window = data[-30:]
    predictions = []

    for _ in range(periods):
        pred = model.predict(last_window.reshape(1, 30, 1), verbose=0)
        predictions.append(pred[0][0])
        last_window = np.append(last_window[1:], pred).reshape(30, 1)

    future_dates = pd.date_range(df["date"].max(), periods=periods + 1)[1:]
    return pd.DataFrame({"date": future_dates, "forecast": predictions})
