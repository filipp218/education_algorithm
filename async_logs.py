import asyncio


def read_file(name_file):
    with open(name_file, 'r') as file:
        for i in file:
            yield i


async def write_data(name_file):
    result = []
    for i in read_file(name_file):
        time, user_id, res_id = i.split(";")
        if user_id == "c90f4b45":
            result.append([time, user_id, res_id])
    return result


async def print_file():
    result = []
    for num in range(1, 100):
        name_file = f'{num}.txt'
        result.append(write_data(name_file))
    res = await asyncio.gather(*result)
    w_page = 1
    counter = 0
    for num in res:
        for seq in num:
            to_write = ";".join(seq)
            with open(f'out_{w_page}.txt', 'a') as file:
                file.write(to_write + '\n')
            counter += 1
            if counter == 100:
                counter = 0
                w_page += 1


loop = asyncio.get_event_loop()
loop.run_until_complete(print_file())
