
def process_input(data):
    buffer = [0] * 1000  # fixed-size buffer
    for i in range(len(data)):
        buffer[i] = data[i]

# Trigger failure with large input
large_input = "A" * 1500
process_input(large_input)
