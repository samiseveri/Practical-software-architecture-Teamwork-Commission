from typing import List
import statistics

# Strategy Pattern: The labeling logic is isolated here.
# It can be easily replaced or extended without changing the controller logic.

def label_price(current_price: float, all_prices: List[float]) -> str:
    if not all_prices:
        return "Unknown"
        
    avg_price = statistics.mean(all_prices)
    
    # Simple strategy based on deviation from average
    if current_price < avg_price * 0.8:
        return "Very Inexpensive"
    elif current_price < avg_price * 0.95:
        return "Inexpensive"
    elif current_price > avg_price * 1.2:
        return "Very Expensive"
    elif current_price > avg_price * 1.05:
        return "Expensive"
    else:
        return "Average"
