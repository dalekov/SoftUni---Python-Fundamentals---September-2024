def check_ticket(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'

    symbols = ['@', '#', '$', '^']
    left_half = ticket[:10]
    right_half = ticket[10:]

    def longest_sequence(half, symbol):
        max_length = 0
        current_length = 0
        for char in half:
            if char == symbol:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
        return max_length

    # Check for each symbol
    for symbol in symbols:
        left_seq = longest_sequence(left_half, symbol)
        right_seq = longest_sequence(right_half, symbol)
        min_seq = min(left_seq, right_seq)

        # If both halves have at least 6 of the same symbol uninterrupted
        if min_seq >= 10:
            return f'ticket "{ticket}" - 10{symbol} Jackpot!'
        elif min_seq >= 6:
            return f'ticket "{ticket}" - {min_seq}{symbol}'

    return f'ticket "{ticket}" - no match'


# Read tickets from input and process them
input_tickets = input().split(', ')

for ticket in input_tickets:
    ticket = ticket.strip()  # Remove any leading or trailing spaces
    print(check_ticket(ticket))
