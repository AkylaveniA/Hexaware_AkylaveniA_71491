//done
import java.util.Scanner;
class RevPal
{  
	public static void main(String args[])  
	{  
		String s;
		String rev="";  
		Scanner sc=new Scanner(System.in);  
		System.out.print("Enter a String: ");  
		s=sc.nextLine();               
		for(int i=s.length();i>0;--i)           
		{  
			rev+=s.charAt(i-1);     
		}  
		System.out.println("Reversed string: "+rev);
		if(s.equals(rev))
		{
			System.out.println(rev+" is a Palindrome.");	
		}else
		{
			System.out.println(rev+" is not a Palindrome.");
		}
		
		sc.close();
		
	}  
}