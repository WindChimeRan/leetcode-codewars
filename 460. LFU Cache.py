#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU缓存
#
from collections import Counter, defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.cnt = Counter()
        self.cache = {}
        self.capacity = capacity
        self.time = 0
        self.used = {}
        self.reverse_cnt = defaultdict(set)

    def get(self, key: int) -> int:
        self.time += 1
        result = self.cache.get(key, -1)
        if result != -1:
            self.cnt[key] += 1
            self.used[key] = self.time
            self.reverse_cnt[self.cnt[key]].add(key)
            self.reverse_cnt[self.cnt[key]-1].remove(key)
            if len(self.reverse_cnt[self.cnt[key]-1]) == 0:
                self.reverse_cnt.pop(self.cnt[key]-1)
        # print('return %d' % result)
        return result

    def put(self, key: int, value: int) -> None:
        self.time += 1

        if self.capacity == 0:
            return
        elif key in self.cache:
            self.cache[key] = value
            self.cnt[key] += 1
            self.used[key] = self.time
            self.reverse_cnt[self.cnt[key]].add(key)
            self.reverse_cnt[self.cnt[key]-1].remove(key)
            if len(self.reverse_cnt[self.cnt[key]-1]) == 0:
                self.reverse_cnt.pop(self.cnt[key]-1)
        else:

            # add ok
            if len(self.cache) < self.capacity:
                pass
            # add and remove LRU
            else:

                least =self.reverse_cnt[min(self.reverse_cnt.keys())]
                least_recent = sorted(least, key=lambda x: self.used[x])[0]

                self.reverse_cnt[self.cnt[least_recent]].remove(least_recent)
                if len(self.reverse_cnt[self.cnt[least_recent]]) == 0:
                    self.reverse_cnt.pop(self.cnt[least_recent])
                self.cache.pop(least_recent)
                self.cnt.pop(least_recent)
                self.used.pop(least_recent)
        self.cache[key] = value
        self.cnt[key] += 1
        self.reverse_cnt[self.cnt[key]].add(key)
        if self.cnt[key] > 1:
            self.reverse_cnt[self.cnt[key]-1].remove(key)
            if len(self.reverse_cnt[self.cnt[key]-1]) == 0:
                self.reverse_cnt.pop(self.cnt[key]-1)
        self.used[key] = self.time
