//done
class Sort
{
	public static void main(String args[])
	{
		int[] arr={100,250,150,350,490,560,440};
		int[] greaterarr=new int[5];
		int temp=0,m=0;
		for(int i=0;i<7;i++)
		{
			for(int j=i+1;j<7;j++)
			{
				if(arr[i]>arr[j])
				{
					temp=arr[i];
					arr[i]=arr[j];
					arr[j]=temp;
				}
			}
		}
		System.out.println("ascending order:");
		for(int i=0;i<7;i++)
		{
			if(arr[i]>200)
			{
				greaterarr[m++]=arr[i];
			}
			System.out.println(arr[i]);
		}
		for(int i=0;i<7;i++)
		{
			for(int j=i+1;j<7;j++)
			{
				if(arr[i]<arr[j])
				{
					temp=arr[i];
					arr[i]=arr[j];
					arr[j]=temp;
				}
			}
		}
		System.out.println("descending order:");
		for(int i:arr)
		{
			System.out.println(i);
		}
		System.out.println("Greater then 200:");
		for(int i:greaterarr)
		{
			System.out.println(i);
		}
	} 
}