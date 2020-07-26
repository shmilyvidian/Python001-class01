import queue

if __name__ == "__main__":
    q = queue.PriorityQueue()
    q.put((1, 'hello'))
    q.put((-2, 'ni'))
    q.put((3, '33'))
    # print(f'c {q.full()}')
    # print(f'c {q.qsize()}')

    print(f'{q.get()}')
    print(f'{q.get()}')
    print(f'{q.get()}')
    # print(f'c {q.qsize()}')

    print(f'{q.get()}')
    q.task_done()

