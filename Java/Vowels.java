//done
public class Vowels{
	public static void main(String args[]) {
		String  c1="welcome to java Programming ";
		String vowels="",consonants="";
		c1=c1.toLowerCase();
		System.out.println(c1);
		//String[] data=c1.split("\\s");
		for(int i=0;i<c1.length();i++){
			char c=c1.charAt(i);
			if(c!=' '){
				if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
					vowels+=c;
				}else{
					consonants+=c;
				}
			}
			
		}
		System.out.println("vowels: "+vowels+"\nconsonants: "+consonants);
		
	}
}