public class BinaryTree {
    private static class Node {
        int item;
        Node left;
        Node right;

        Node(int item) {
            this.item = item;
            this.left = this.right = null;
        }

        @Override
        public String toString() {
            return Integer.toString(item);
        }
    }

    Node root;

    private static void addItem(Node cur, int item) {
        if (cur.item <= item) {
           if (cur.left == null) { 
                cur.left = new Node(item);
           } else {
                addItem(cur.left, item);
           }
        } else {
           if (cur.right == null) { 
                cur.right = new Node(item);
           } else {
                addItem(cur.right, item);
           }
        }
    }

    void addItem(int item) {
        if (root == null) {
            root = new Node(item);
        } else {
            addItem(root, item);
        }
    }

    void print() {
        print(0, root);
    }

    private static void print(int indent, Node node) {
        if (node != null) {
            for (int i = 0; i < indent; ++i) {
                System.out.print(" ");
            }
            System.out.println(node); 

            print(indent + 1, node.left);
            print(indent + 1, node.right);
        }
    }

    public static void main(String[] args) {
        BinaryTree t = new BinaryTree();
        for (int i = 0; i < 10; ++i) {
            t.addItem((i * i * i) % 37); 
        }
        t.print();
        System.out.println("\n" + t.isBalanced());
    }

    private static int getHeightIfBalanced(Node node) {
        if (node == null) {
            return 0;
        } else {
           int lHeight = getHeightIfBalanced(node.left); 
           int rHeight = getHeightIfBalanced(node.right);
           if (lHeight < 0 || rHeight < 0) {
               return -1;
           } else {
               boolean isBalanced = Math.abs(lHeight - rHeight) <= 1;
               if (isBalanced) {
                   return Math.max(lHeight, rHeight) + 1;
               } else {
                   return -1; 
               }
           }
        }
    }

    public boolean isBalanced() {
        return getHeightIfBalanced(root) >= 0;
    }
}
