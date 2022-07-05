# Definition for singly-linked list.

class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}

def add_two_numbers(l1, l2)
    dummyHead = ListNode.new
    curr = dummyHead
    carry = 0
    while l1 != nil || l2 != nil || carry != 0
        l1Val = l1 != nil ? l1.val : 0
        l2Val = l2 != nil ? l2.val : 0

        columnSum = l1Val + l2Val + carry
        carry = columnSum / 10
        newNode = ListNode.new(columnSum % 10)
        p dummyHead
        curr.next = newNode
        p dummyHead
        curr = newNode

        l1 = l1.next if l1 != nil ? l1 : nil
        l2 = l2.next if l2 != nil ? l2 : nil
    end

    dummyHead.next
end

l1 = ListNode.new(2, ListNode.new(4, ListNode.new(3)))
l2 = ListNode.new(5, ListNode.new(6, ListNode.new(4)))

add_two_numbers(l1, l2)


def test()
    dummyHead = []
    curr = dummyHead
    5.times do |i|
      curr.push(i)
      curr = []
    end
    p curr
    p dummyHead
end

test()
