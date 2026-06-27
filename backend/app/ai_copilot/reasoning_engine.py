def reasoning_steps(intent, context, message):
    steps = []

    steps.append(f"Intent detected: {intent}")
    steps.append(f"Context: {context}")
    steps.append(f"Message: {message}")

    if "چرا" in message:
        steps.append("User is asking for explanation.")
    if "بهترین" in message:
        steps.append("User is asking for ranking or comparison.")
    if "پیش بینی" in message:
        steps.append("User is asking for forecasting.")

    return steps
