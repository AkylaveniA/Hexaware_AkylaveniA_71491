//done
import java.util.*;
public class ThirtyValues {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        //int even[],odd[],positive[],negative[],zero[];
        int arr[]=new int[30];
        for(int i=0;i<30;i++){
            arr[i]=sc.nextInt();
        }
        ArrayList<Integer> even=new ArrayList<Integer>();
        ArrayList<Integer> odd=new ArrayList<Integer>();
        ArrayList<Integer> pos=new ArrayList<Integer>();
        ArrayList<Integer> neg=new ArrayList<Integer>();
        ArrayList<Integer> zero=new ArrayList<Integer>();
        for(int i:arr){
            
            if(i%2==0){
                even.add(i);
            }
            if(i%2!=0){
                odd.add(i);
            }
            if(i>0){
                pos.add(i);
            }
            if(i<0){
                neg.add(i);
            }
            if(i==0){
                zero.add(i);
            }
            
        }
        System.out.println("even: "+even+"\nodd: "+odd+"\n+ve: "+pos+"\n-ve: "+neg+"\nzero: "+zero);

        sc.close();
    }
}
