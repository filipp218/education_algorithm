
def read_file(name_file):
    with open(name_file, 'r') as file:
        for i in file:
            yield i


def print_file():
    w_page = 1
    counter = 0
    for num in range(1, 100):
        name_file = f'{num}.txt'
        for i in read_file(name_file):
            time, user_id, res_id = i.split(";")
            if user_id == "c90f4b45":
                with open(f'out_{w_page}.txt', 'a') as file:
                    file.write(i)
                counter += 1
                if counter == 100:
                    counter = 0
                    w_page += 1


print_file()

