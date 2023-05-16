import java.util.Scanner;
public class Sorting // in Ascending order
{
    public static void main(String[] args)
    {
        //initializing the array
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements");
        int n=sc.nextInt();
        int i,j;
        int arr[]=new int[n];
        for(i=0;i<n;i++)
        {
            System.out.println("Enter value for position "+(i+1)+" in the array ");
            arr[i]=sc.nextInt();
        }

        int temp =0;

        //displaying the elements of the original array
        for(i=0;i<n;i++)
        {
            System.out.print(arr[i] + " ");
        }

        //sorting the array in ascending order
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(arr[i]<arr[j])
                {
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        System.out.println();

        //displaying the elements of the array after sorting
        for(i=0;i<n;i++)
        {
            System.out.print(arr[i] + " ");
        }

    }
}
