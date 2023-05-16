package Experiment_2;
import java.util.Scanner;
class Palindrome
{
    public static void main(String[] args)
    {
        Scanner sc =new Scanner(System.in); //Creating a scanner object to take input of the number from user
        System.out.println("Enter number");
        int n=sc.nextInt();
        int temp=n;
        int rev=0;
        while(n!=0)
        {
            rev=10*rev + n%10;
            n=n/10;
        }
        if(rev==temp) System.out.println("It is a palindrome");
        else System.out.println("It is not a palindrome");
        sc.close();
    }
}
