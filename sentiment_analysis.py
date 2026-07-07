import pandas as pd
import matplotlib.pyplot as plt

# CSV file read
df = pd.read_csv("customer_feedback.csv")

# Sentiment function
def sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"

# New column
df["Sentiment"] = df["Rating"].apply(sentiment)

# Print data
print(df)

# Count sentiments
print("\nSentiment Count:")
print(df["Sentiment"].value_counts())

# Graph
df["Sentiment"].value_counts().plot(kind="bar")
plt.title("Customer Feedback Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()