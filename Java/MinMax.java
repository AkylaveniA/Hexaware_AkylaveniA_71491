//done
import java.util.*;
public class MinMax {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        int size=sc.nextInt();
        int[] arr=new int[size];
        for(int i=0;i<size;i++){
            arr[i]=sc.nextInt();
        }
        
        
        int temp=0;
        for(int i=0;i<size;i++)
		{
			for(int j=i+1;j<size;j++)
			{
				if(arr[i]>arr[j])
				{
					temp=arr[i];
					arr[i]=arr[j];
					arr[j]=temp;
				}
			}
		}
        System.out.println("smallest: "+arr[0]+"\nsecond largest: "+arr[size-2]+"\nlargest: "+arr[size-1]);
        
        
        sc.close();
    }

}
