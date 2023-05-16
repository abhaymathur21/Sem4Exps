import java.util.Scanner;
class IdentityMatrix
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        boolean flag = true;
        System.out.println("Enter number of rows");
        int rows=sc.nextInt();
        System.out.println("Enter number of columns");
        int columns=sc.nextInt();
        if(rows!=columns) System.out.println("It is not an Identity matrix since it is not a Square matrix");
        else
        {
            int arr[][] = new int[rows][columns];
            System.out.print("Enter elements of array");
            for(int i=0;i<rows;i++)
            {
                for(int j=0;j<columns;j++)
                {
                    System.out.print("Enter the value of the position (" + (i+1) + "," + (j+1) + ") in the array");
                    arr[i][j] = sc.nextInt();
                }
            }

            for(int i=0;i<rows;i++)
            {
                for(int j=0;j<columns;j++)
                {
                    if(i==j && arr[i][j]!=1)
                    {
                        flag = false;
                        break;
                    }
                    if(i!=j && arr[i][j]!=0)
                    {
                        flag = false;
                        break;
                    }
                }
            }
            
            if(flag) System.out.println("The matrix is an identity matrix");
            else System.out.println("The matrix is not an identity matrix");
        }
    }
}