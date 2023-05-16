
public class Prime 
{
    public static void main(String[] args) // taking input from command line arguments -> javac Prime.java -> java Prime 12 -> Output = It is not a prime number
    {
        int n = Integer.parseInt(args[0]);
        System.out.println(n);
        boolean flag=false;
        for(int i=2;i<n;i++)
        {
            if(n%i==0)
            {
                flag=true;
                break;
            }
        }
        if(flag==false) System.out.println("It is a prime number");
        else System.out.println("It is not a prime number");
    }
}
