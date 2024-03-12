def decode(message_file):
    # Step 1: Get all the lines from the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Step 2: Sort the lines based on the number from each line
    lines.sort(key=lambda x: int(x.split()[0]))

    # Step 3: Create a map to store numbers as keys and words as values
    number_word_map = {}
    for line in lines:
        num, word = line.split()
        number_word_map[int(num)] = word
    
    print (number_word_map)

     # Step 4: Create a pyramid structure based on available numbers
    max_num = max(number_word_map.keys())

    print (max_num)
    pyramid = []
    current_num = 1
    range_num = 1
    while current_num <= max_num:
        row = []
        for _ in range(range_num):
            if current_num <= max_num:
                row.append(current_num)
                current_num += 1
        range_num +=1
        pyramid.append(row)
    print(pyramid)    
    # Step 5: Take only the last number from each line
    last_numbers = [row[-1] for row in pyramid]
    print("Last Numbers   :", last_numbers)
    # Step 6: Get words of corresponding numbers
    words = [number_word_map[num] for num in last_numbers]
    return ' '.join(words)
# Provide the path to your local file
file_path = "c:\\Users\\riyas\\Downloads\\coding_qual_input.txt"

# Call the decode function with the file path
decoded_message = decode(file_path)

# Print the decoded message
print(decoded_message)

# path to local file


