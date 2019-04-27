#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lph time:2018/3/8


class LNode:
    """
        创建一个新节点: LNode(elem, next_)
        elem: 数据域
        next_: 指针域

    """
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkList:
    """
        创建一个单链表结构

    """
    def __init__(self, node=None):
        """
        self._head: 表头指针

        """
        self._head = node

    def is_empty(self):
        """
        判断单链表LinkList是否为空

        """
        return self._head is None

    def prepend(self, elem):
        """
        表头插入节点
        (头插法)
        :param elem:    在表头插入元素的值

        """
        self._head = LNode(elem, self._head)

    def length(self):
        """
        返回单链表的长度

        """
        p = self._head
        # p 相当于游标
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count

    def printall(self):
        """
        遍历整个单链表

        """
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def elements(self):
        """
        将单链表变为迭代器，可用for遍历循环
        """
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def append(self, elem):
        """
        在单链表的尾部添加元素
        (尾插法)
        :param elem:    添加尾部节点数据域的值elem

        """
        node = LNode(elem)
        if self.is_empty():
            self._head = node
        else:
            p = self._head
            while p.next is not None:
                p = p.next
            p.next = node

    def insert(self, pos, elem):
        """
        指定位置添加元素
        :param pos:     插入的位置, 从0开始
        :param elem:    插入的元素

        """
        # print("Current LinkList's Length: ", self.length())
        if pos < 0 or pos > self.length()-1:
            raise IndexError("LinkList index out of range")
        else:
            node = LNode(elem)
            pre = self._head
            while pre.next is not None and pos > 1:
                pos -= 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, elem):
        """
        删除节点
        :param elem:    删除节点数据域中的值elem

        """
        pre = self._head
        if pre.elem is elem:
            self._head = pre.next
        else:
            while pre.next.elem is not elem:
                pre = pre.next
            pre.next = pre.next.next

    def rm(self, elem):
        """
        使用两个游标指针变量完成删除节点
        :param elem:    删除节点数据域中的值elem
        :return:
        """
        cur = self._head
        pre = None
        while cur is not None:
            if cur.elem is elem:
                # 先判断此节点是否是头节点
                # 头节点
                if cur is self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, elem):
        """
        判断某个元素是否在这个单链表中
        :param elem:

        """
        p = self._head
        while p is not None:
            if p.elem is elem:
                return True
            else:
                p = p.next
        return False


if __name__ == '__main__':
    linklist = LinkList()
    print(linklist.length())




