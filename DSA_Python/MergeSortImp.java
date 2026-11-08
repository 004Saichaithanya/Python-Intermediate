import java.util.Scanner;
import java.util.ArrayList;

public class MergeSortImp {

    public static void merge(int[] a,int low,int mid,int high){
        ArrayList<Integer> barr=new ArrayList<>();
        int i=low;
        int j=mid+1;
        while(i<=mid && j<=high){
            if(a[i]<a[j]){
                barr.add(a[i]);
                i++;
            }
            else{
                barr.add(a[j]);
                j++;
            }
        }
        while(i<=mid){
            barr.add(a[i]);
            i++;
        
        }

        while(j<=high){
            barr.add(a[j]);
            j++;
        }
        int k=0;

        for(i=low;i<=high;i++,k++){
            a[i]=barr.get(k);
        }
        }

    public static void mergeSort(int[] a ,int low,int high){

        if(low<high){   
            int mid=(low+high)/2;
            mergeSort(a, low, mid);
            mergeSort(a, mid+1, high);
            merge(a,low,mid,high);
        }

    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int[] arr=new int[10];
        for(int i=0;i<arr.length;i++){
            System.out.printf("enter arr[%d]:",i);
            arr[i]=sc.nextInt();
        }
        for(Integer i:arr){
            System.out.print(i+" ");
        }

        mergeSort(arr, 0, arr.length-1);

        System.out.println();
        for(Integer i:arr){
            System.out.print(i+" ");
        }

        


        sc.close();
    }
}
