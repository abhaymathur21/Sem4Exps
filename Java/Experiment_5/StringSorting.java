import java.util.Scanner;
public class StringSorting
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of strings");
        int n = sc.nextInt();
        sc.nextLine(); // Consume the newline character left by nextInt() or else it will take that as the next string value

        String s[] = new String[n];
        String temp;

        //input the strings
        for(int i = 0; i < n; i++)
        {
            System.out.println("Enter string " + (i+1)+ " ");
            s[i] = sc.nextLine();
        }

        //sort strings in descending order
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(s[i].compareTo(s[j])<0)
                {
                    temp = s[i];
                    s[i] = s[j];
                    s[j] = temp;
                }
            }
        }

        //display the sorted strings
        System.out.println("\nSorted strings in descending order: ");
        for(int i=0;i<n;i++)
        {
            System.out.println((i+1)+". "+s[i]);
        }
    }
}
