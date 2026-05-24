import csv_reader
def main():
    reader = csv_reader.CSVReader('.\\globishwords.csv')
    print('Vocabulary quiz!')
    count = 0
    correct_answers = 0
    for row in reader.data:
        word = row[0]
        meaning = row[1]
        print(f'What is the meaning of "{word}"?')
        user_input = input('Your answer: ')
        if user_input.strip().lower() == meaning.strip().lower():
            print('Correct!')
            correct_answers += 1
        else:
            print(f'Wrong! The correct answer is: {meaning}')
        count += 1
        if count >= 10:  # Limit to 10 questions for the quiz
            print(f'You got {correct_answers} out of {count} questions correct.')
            print(f'Your score: {correct_answers / count * 100:.2f}%')
            break
if __name__ == "__main__":
    main()
        