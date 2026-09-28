def print_reverse(text):
    """Надрукувати рядок у зворотному порядку рекурсивно."""
    def print_character(index):
        if index < 0:
            return
        print(text[index], end="")
        print_character(index - 1)

    print_character(len(text) - 1)
    print()


if __name__ == "__main__":
    print_reverse("tiger")

   