import trigram

linked_list = trigram.LinkedList()
print("#####  Linked list tests  #####")
print(f"Size: {len(linked_list)}")

node_01 = trigram.Node("carl", 10, 10/100)
node_02 = trigram.Node("luke", 20, 20/100)
node_03 = trigram.Node("jason", 30, 30/100)
node_04 = trigram.Node("andy", 40, 40/100)
node_05 = trigram.Node("ethan", 50, 50/100)
node_06 = trigram.Node("bille", 60, 60/100)

print()
print("#####  Test add list tests  #####")
linked_list.add(node_01)
linked_list.add(node_02)
linked_list.add(node_03)
linked_list.add(node_04)
for i in linked_list.list:
    print(i)
print("#####  Finished adding  #####")
print()


print("#####  Test insert ethan at index 2  #####")
print("Test insert at index 2")
linked_list.add_at_index(2, node_05)
for i in linked_list.list:
    print(i)
print("#####  Finished Test insert at index 2  #####")
print()

print("#####  Appending node 06 billie  #####")
linked_list.add(node_06)
print("appending last node")
for i in linked_list.list:
    print(i)
print("#####  Appending node 06 billie  #####")
print()

print()
print("#####  Test contains ethan #####")
test_node = trigram.Node("ethan", 40, 40 / 100)
print(f"Contains ethan: {linked_list.contains(test_node)}")

print()
print("#####  Test contains ethan #####")
test_node = trigram.Node("ethan", 40, 40 / 100)
print(f"Contains ethan: {linked_list.contains(test_node)}")

print()
print("#####  Test index of ethan #####")
test_node = trigram.Node("ethan", 40, 40 / 100)
print(f"Index ethan: {linked_list.index_of(test_node)}")

print()
print("#####  Test index of Coco #####")
test_node = trigram.Node("Coco", 40, 40 / 100)
print(f"Index coco: {linked_list.index_of(test_node)}")


print()
print("#####  Test get word #####")
jason = linked_list.get("jason")
print(f"Print jason: {jason}")


print()
print("#####  Test get word not exists #####")
jason = linked_list.get("jason_not")
print(f"Print jason: {jason}")
