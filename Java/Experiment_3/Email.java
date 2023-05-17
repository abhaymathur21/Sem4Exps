import java.io.*;
public class Email// print number of letters, numvbers and special characters
{
    public static void main(String[] args)throws Exceptiona 
    {
        InputStreamReader r = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(r);
        System.out.println("Enter your email address");
        int n=Integer.parseInt(br.readLine());
        System.out.println(n);
        

    }
}
