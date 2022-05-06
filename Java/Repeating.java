import java.util.ArrayList;

public class Repeating {
    public static void main(String[] args) {
        int arr[]={1,2,3,4,5,6,7,8,9,10};
        int arr1[]={2,3,4,5,6,7,2};
        ArrayList<Integer> repeat=new ArrayList<Integer>();
        ArrayList<Integer> missing=new ArrayList<Integer>();
        for(int i:arr){
            for(int j:arr1){
                if(i==j){
                    repeat.add(i);
                }else{
                    missing.add(i);
                }
            }
        }
        System.out.println("repeating: ");
        for(int i:repeat){
            System.out.print(i+" ");
        }
        System.out.println("missing: ");
        for(int i:missing){
            System.out.print(i+" ");
        }
    }
}
