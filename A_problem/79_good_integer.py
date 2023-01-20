def main():
    N = sorted(input())
    if len(set(N)) == 1 or (len(set(N)) == 2 and N[-1] != N[-2]):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
