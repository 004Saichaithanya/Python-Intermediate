class QuickSort {
    public static void PrintArray(int[] a) {
        for (int i = 0; i < a.length; i++) {
            System.out.printf("%d ", a[i]);
        }
        System.out.println();
    }

    public static int parition(int[] a, int low, int high) {
        int i = low;
        int j = high;
        int pivot = a[low];
        int temp = 0;

        do {
            while (pivot >= a[i] && i < high) {
                i++;
            }
            while (a[j] > pivot && j > low) {
                j--;
            }
            if (i < j) {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        } while (i < j);
        temp = a[low];
        a[low] = a[j];
        a[j] = temp;

        return j;

    }

    public static void quick(int[] a, int low, int high) {
        if (low < high) {
            int pivotIndex = parition(a, low, high);
            quick(a, low, pivotIndex - 1);
            quick(a, pivotIndex + 1, high);
        }
    }

    public static void main(String[] s) {
        int[] A = { 1, 6, 4, 3, 2, 7, 10, 9 };
        System.out.println("hello");

        PrintArray(A);
        quick(A, 0, A.length - 1);
        PrintArray(A);
    }
}