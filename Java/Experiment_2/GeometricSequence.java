package Experiment_2;
import java.lang.Math;
public class GeometricSequence
{
    public static void main(String[] args)
    {
        int n=5, r=2, a=1;
        double result;
        System.out.print(a);
        for(int i=2;i<=n;i++)
        {
            result = a*Math.pow(r,i-1);
            System.out.print(", "+(int)result);
        }
    }
}