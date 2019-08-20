from collections import namedtuple
from typing import List, Dict, Tuple

Task = namedtuple('Task', ['index', 'weight', 'length']) # add index to distinguish tasks with same weight and length
#Schedule = List[Task]


class Scheduler:

    @staticmethod
    def read_input(filename: str) -> Tuple[List[Task], int]:
        tasks = []
        f = open(filename, 'r')
        number_of_tasks = int(f.readline())
        line = f.readline()
        index = 1
        while line:
            weight = int(line.split()[0])
            length = int(line.split()[1])
            tasks.append(Task(index, weight, length))
            line = f.readline()
            index += 1
        f.close()
        return tasks, number_of_tasks

    @staticmethod
    def sort_tasks(tasks: List[Task]) -> List[Task]:
        scores = dict()
        for task in tasks:
            scores[task] = task.weight / task.length
        print("Scored computation finished.")
        sorted_scores = sorted(scores.items(), key = lambda task_score: task_score[1], reverse=True)
        return [task_score[0] for task_score in sorted_scores]
    
    @staticmethod
    def compute_weighted_completion_time(tasks: List[Task]) -> int:
        completion_time = 0
        weighted_completion_time = 0
        for task in tasks:
            completion_time += task.length
            weighted_completion_time += task.weight * completion_time
        return weighted_completion_time

if __name__ == "__main__":

    tasks, number_of_tasks = Scheduler.read_input('Part2/jobs.txt')
    print("Number of tasks: ", number_of_tasks)
    sorted_tasks = Scheduler.sort_tasks(tasks)
    print("Sorting completed.")
    weighted_completion_time = Scheduler.compute_weighted_completion_time(sorted_tasks)
    print(weighted_completion_time)


    