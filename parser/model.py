import csv
from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse_line(self, line: str):
        pass

    @abstractmethod
    def write_file(self, line: str):
        pass


class ProxyLogParser(Parser):
    def __init__(self):
        super().__init__()
        self.id_count = []
        self.count = []
        self.id_time = []
        self.time = []
        self.failed = set()

    def parse_line(self, line: str):
        words = line.split()
        if words.__len__() >= 11 and words[6] == 'failed:' and words[5] != 'Highlight':
            self.failed.add(words[4])
            self.id_time.append(words[4])
            self.time.append(int(words[10]))
            return
        if words.__len__() < 9 or words[5].lower() != 'search':
            return
        if words.__len__() == 11:
            self.id_count.append(words[4])
            self.count.append(int(words[10]))
        elif words.__len__() == 9:
            self.id_time.append(words[4])
            self.time.append(int(words[8].replace('ms', '')))

    def write_file(self, path_to_out: str):
        counter = dict(zip(self.id_count, self.count))
        timer = dict(zip(self.id_time, self.time))
        with open(path_to_out, 'w', newline='') as csvfile:
            fieldnames = ['id', 'count', 'time', 'failed']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for cnt in counter:
                time = self.get_from_dict(timer, cnt)
                writer.writerow({'id': cnt, 'count': counter[cnt], 'time': time, 'failed': cnt in self.failed})

    @staticmethod
    def get_from_dict(dct: dict, key: str):
        try:
            return dct[key]
        except KeyError:
            return -1
