"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      num1, num2 = [], []
      curr1, curr2 = l1, l2
      while curr1:
        num1.append(curr1.val)
        curr1 = curr1.next
      while curr2:
        num2.append(curr2.val)
        curr2 = curr2.next
      i = 0
      result, end = None, None
      carry = 0

      while i < len(num1) or i < len(num2):
        if i >= len(num1):
          num1_digit = 0
        else:
          num1_digit = num1[i]
        if i >= len(num2):
          num2_digit = 0
        else:
          num2_digit = num2[i]         
        digit = carry + num1_digit + num2_digit
        if not result:
          result = ListNode(digit % 10, None)
          end = result
        else:
          end.next = ListNode(digit % 10, None)
          end = end.next
        carry = digit // 10
        i += 1
      if carry != 0:
        end.next = ListNode(carry, None)
        end = end.next
      return result