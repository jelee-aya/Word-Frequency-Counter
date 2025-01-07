print("Word Frequency Counter~~\n")

def frequency ():
    free_queen_cy = {} #stores word count <3

    saint_tenz = input("Enter a sentence: ")
    weird = saint_tenz.split() 

    for words in weird:
        words = words.lower()

        if words in free_queen_cy:
            free_queen_cy[words] += 1
        else:
            free_queen_cy[words] = 1
    return free_queen_cy

def main ():
    word_freq = frequency()

    print(f"Word Frequencies:\n")
    for words, count in word_freq.items():
        print(f"Word: {words} | Frequency: {count}")

if __name__ == "__main__":
    main()
