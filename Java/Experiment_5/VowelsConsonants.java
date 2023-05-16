import java.util.Scanner;
public class VowelsConsonants
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string");
        String s = sc.nextLine();
        String s1 = s.toLowerCase();
        int vowels=0, consonants=0;

        for(int i=0;i<s1.length();i++)
        {
            if(s1.charAt(i)=='a' || s1.charAt(i) == 'e' || s1.charAt(i) == 'i' || s1.charAt(i) == 'o' || s1.charAt(i) == 'u') vowels++;
            else if(s1.charAt(i)>'a' && s1.charAt(i)<'z') consonants++;
        }

        System.out.println("Number of vowels = " + vowels + "\nNumber of consonants = " + consonants);
    }
}