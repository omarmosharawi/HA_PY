quotes_list = [
    "I am a machine learning engineer and I love to code.",
    "Python is my favorite programming language because it's easy to learn and has a vast ecosystem of libraries.",
    "Machine Learning is the future of artificial intelligence."
]

def get_quotes():
    return '\n'.join(quotes_list)

def add_quote():
    quote = input("Enter your favorite quote: ")
    if isinstance(quote, str) and len(quote.split()) >  0:
        quotes_list.append(quote)
        print('Your quote has been added!')
    else:
        print('Please enter a valid quote. The quote must be a string.')

def get_random_quote():
    from random import choice
    return choice(quotes_list)



def main():
    while True:
        print('\n\n--- Quote Machine ---')
        print('1. Get all quotes')
        print('2. Add a new quote')
        print('3. Get a random quote')
        print('4. Exit')

        user_input = int(input("\nChoose an option (1-4): "))

        if user_input ==  1:
            print(get_quotes())
        elif user_input == 2:
            add_quote()
        elif user_input == 3:
            print(get_random_quote())
        elif user_input == 4:
            break
        else:
            print('Enter a valid option number. Pleas, Try again.')

if __name__ == '__main__ ':
    main()
