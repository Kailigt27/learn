using System;

class Program
{
    class Node
    {
        public int data;
        public Node? next;

        public Node(int data)
        {
            this.data = data;
            this.next = null;
        }
    }

    class LinkedList
    {
        public Node? head;
        public Node? tail;

        public LinkedList()
        {
            this.head = null;
            this.tail = null;
        }

        // 添加节点
        public void AddNode(int data)
        {
            Node newNode = new Node(data);

            if (head == null) // 链表为空时
            {
                head = tail = newNode;
                tail.next = head; // 形成循环
            }
            else
            {
                tail.next = newNode;
                tail = newNode;
                tail.next = head; // 继续保持循环
            }
        }

        // 删除指定数据的节点
        public void deleteNode(int data)
        {
            if (head == null) return; // 空链表

            Node temp = head;
            Node prev = null;

            // 处理头节点的删除
            if (head.data == data)
            {
                if (head == tail) // 只有一个节点时
                {
                    head = tail = null;
                }
                else
                {
                    head = head.next;
                    tail.next = head; // 维持循环
                }
                return;
            }

            // 从头节点的下一个节点开始遍历
            prev = head;
            temp = head.next;
            while (temp != head)
            {
                if (temp.data == data)
                {
                    if (temp == tail) // 删除尾节点
                    {
                        tail = prev;
                        tail.next = head;
                    }
                    else // 删除中间节点
                    {
                        prev.next = temp.next;
                    }
                    return;
                }

                prev = temp;
                temp = temp.next;
            }
        }

        // 遍历并显示链表内容
        public void display()
        {
            if (head == null)
            {
                Console.WriteLine("链表为空");
                return;
            }

            Node temp = head;
            do
            {
                Console.WriteLine(temp.data);
                temp = temp.next;
            } while (temp != head); // 确保回到头节点，结束循环
        }
    }

    static void Main(string[] args)
    {
        LinkedList list = new LinkedList();

        // 添加节点
        list.AddNode(1);
        list.AddNode(2);
        list.AddNode(3);
        list.AddNode(4);
        list.AddNode(5);

        // 显示链表内容
        Console.WriteLine("初始链表:");
        list.display();

        // 删除节点
        list.deleteNode(3);

        // 删除后的链表内容
        Console.WriteLine("删除节点 3 后的链表:");
        list.display();
    }
}
   