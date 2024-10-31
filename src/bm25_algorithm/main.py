import bm25

def main():
    i = input("List your interests separated by commas: ")
    print(bm25.BM25(i))

if __name__ == "__main__":
    main()