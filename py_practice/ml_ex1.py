import numpy


def prediction(weights, inputs):
    # activation = sum(weight_i * input_i) + bias
    # prediction = 1.0 if activation >= 0.0 else 0.0

    bias = weights[0]  # first weight is bias???
    activation_output = 0

    for i in range(0, len(inputs) - 1):
        activation_output += (weights[i + 1] * inputs[i])
    activation_output += bias
    return activation_output


def train_weights():
    weights = 0
    return weights
