def parse_recipes_from_file(file_path: str) -> dict:
    cook_book = {}

    with open(file_path) as file:
        lines = iter(file)

        for line in lines:
            dish_name = line.strip()
            if not dish_name:
                continue

            ingr_count = int(next(lines))

            ingrs = []
            for _ in range(ingr_count):
                ingr_line = next(lines)

                first_pipe = ingr_line.find("|")
                second_pipe = ingr_line.find("|", first_pipe + 1)

                ingrs.append(
                    {
                        "ingredient_name": ingr_line[:first_pipe].strip(),
                        "quantity": int(ingr_line[first_pipe + 1 : second_pipe]),
                        "measure": ingr_line[second_pipe + 1 :].strip(),
                    }
                )

            cook_book[dish_name] = ingrs

    return cook_book


print(parse_recipes_from_file("recipes.txt"))
