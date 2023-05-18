def bit_stuffing(data):
    stuffed_data = ''
    count = 0
    
    for bit in data:
        if bit == '1':
            count += 1
            stuffed_data += bit
        else:
            count = 0
            stuffed_data += bit

        if count == 5:
            stuffed_data += '0'
            count = 0

    return stuffed_data


# Test the bit stuffing function
data = '0111110101111101'
stuffed_data = bit_stuffing(data)

print("Original data: ", data)
print("Stuffed data:  ", stuffed_data)